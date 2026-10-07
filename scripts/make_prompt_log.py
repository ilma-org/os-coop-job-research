#!/usr/bin/env python3
"""Build a prompt log (prompts/<id>.md) from a saved session, so no agent retypes it.

  python3 scripts/make_prompt_log.py export.txt --list
  python3 scripts/make_prompt_log.py export.txt --turns 5 --slug sre-book-claims \\
      --author @handle --platform "Claude Code" --model "<name and version>" \\
      --role research --purpose "Research topic 07 claims" --significant \\
      --reason "Produced the claims the report relies on" --claims 07-01,07-02

Input formats (--format):
  claude-export  the text of Claude Code's /export (default). Turns start with "❯ ",
                 replies with "● ". Terminal chrome (spinners, recaps, tool results,
                 subagent messages) is dropped and counted. Tool calls become the ledger.
  json           any agent: {"turns": [{"user": "...", "assistant": "...", "ledger": ["- Bash ..."]}],
                 "ledger": ["..."]}. Produce it with your agent's own transcript tooling,
                 not by asking a model to retype the conversation.

The text of each turn is copied as exported, only redacted. Redactions: home and agent
scratch paths, tokens, ID and phone numbers, personal emails, plus --redact "text=kind".
It never guesses the model: pass --model. Then it runs the lint on the new file.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

import kb_common as kb

COLLAPSED = re.compile(r"^  [A-Z][a-z]+\b.*\(ctrl\+o to expand\)\s*$")
TOOLCALL = re.compile(r"^● ([A-Z][A-Za-z]+)\((.*)\)\s*$")
ADVISOR = re.compile(r"^● Advising using (.+?)\s*$")
AGENTS = re.compile(r"^● \d+ background agents? launched")
NOTICE = re.compile(r"^● (?:Agent \".*\" finished|Background command |.*safeguards stopped the response|User answered)")
SUMMARY_TAG = re.compile(r"\s·\s+summary$")
TOOL_NAMES = {"Fetch": "WebFetch", "Update": "Edit"}
URL_RE = re.compile(r"https?://[^\s<>\"'`)\]]+")
PATH_RULES = [
    re.compile(r"/tmp/claude-\d+/\S*"),
    re.compile(r"(?:/home|/Users)/[^\s'\"`)\]>]+"),
    re.compile(r"[A-Za-z]:\\Users\\[^\s'\"`)]+"),
]
NOREPLY = {"noreply", "no-reply"}


def is_chrome(line: str) -> bool:
    return bool(COLLAPSED.match(line)) or line.startswith("  ⎿")


def indent_ge(line: str, n: int) -> bool:
    return line.startswith(" " * n)


def parse_claude_export(text: str) -> tuple[list[dict], Counter, list[str]]:
    lines = text.split("\n")
    turns: list[dict] = []
    dropped: Counter = Counter()
    unknown: list[str] = []
    cur: dict | None = None
    i = 0

    def next_nonblank(j: int) -> int:
        while j < len(lines) and not lines[j].strip():
            j += 1
        return j

    while i < len(lines):
        ln = lines[i].rstrip()
        for marker in "●❯✻※›":
            if ln.startswith(marker + "\xa0"):  # the export sometimes puts a no-break space after the marker
                ln = marker + " " + ln[2:]
        if ln.startswith("❯ ") or ln == "❯":
            cur = {"user_lines": [ln[2:]], "blocks": [], "ledger": []}
            turns.append(cur)
            i += 1
            while i < len(lines):
                j = i if lines[i].strip() else next_nonblank(i)
                if j < len(lines) and indent_ge(lines[j], 2) and not is_chrome(lines[j]):
                    cur["user_lines"].append(lines[j].rstrip()[2:] if lines[j].strip() else "")
                    i = j + 1
                else:
                    break
            continue
        if cur is None:
            i += 1  # banner before the first turn
            continue
        if not ln:
            i += 1
        elif COLLAPSED.match(ln):
            cur["ledger"].append(("collapsed", ln.strip()))
            dropped["collapsed tool lines"] += 1
            i += 1
        elif ln.startswith("✻ "):
            dropped["spinner lines"] += 1
            i += 1
        elif ln.startswith("  ⎿"):
            dropped["tool result lines"] += 1
            i += 1
            while i < len(lines) and lines[i].strip() and indent_ge(lines[i], 3):
                i += 1
        elif ln.startswith("※ "):
            dropped["recap lines"] += 1
            i += 1
            while i < len(lines) and lines[i].strip() and indent_ge(lines[i], 2):
                i += 1
        elif ln.startswith("› "):
            dropped["subagent messages"] += 1
            i += 1
            while i < len(lines) and (not lines[i].strip() or indent_ge(lines[i], 2)):
                i += 1
        elif ln.startswith("●"):
            m_tool, m_adv = TOOLCALL.match(ln), ADVISOR.match(ln)
            if AGENTS.match(ln):
                names = []
                i += 1
                while i < len(lines) and re.match(r"^\s+[├└]\s", lines[i]):
                    names.append(re.sub(r"^\s+[├└]\s+", "", lines[i]).strip())
                    i += 1
                cur["ledger"].append(("agents", names))
            elif NOTICE.match(ln):
                dropped["harness notices"] += 1
                i += 1
                while i < len(lines) and lines[i].strip() and (
                        indent_ge(lines[i], 2) or (len(lines[i]) < 40 and lines[i][0] not in "●❯✻※›")):
                    i += 1
            elif m_tool or m_adv:
                if m_adv:
                    cur["ledger"].append(("advisor", m_adv.group(1)))
                else:
                    cur["ledger"].append(("tool", m_tool.group(1), m_tool.group(2)))
                i += 1
                while i < len(lines):
                    j = i if lines[i].strip() else next_nonblank(i)
                    if j < len(lines) and (lines[j].startswith("  ⎿") or indent_ge(lines[j], 3)):
                        dropped["tool result lines"] += 1 if lines[j].startswith("  ⎿") else 0
                        i = j + 1
                    else:
                        break
            else:
                block = [ln[2:]]
                i += 1
                while i < len(lines):
                    nxt = lines[i].rstrip()
                    if nxt == "":
                        j = next_nonblank(i)
                        if j < len(lines) and indent_ge(lines[j], 2) and not is_chrome(lines[j]):
                            block.append("")
                            i += 1
                            continue
                        break
                    if is_chrome(nxt) or not indent_ge(nxt, 2):
                        break
                    block.append(nxt[2:])
                    i += 1
                block[-1] = SUMMARY_TAG.sub("", block[-1])
                cur["blocks"].append(block)
        else:
            unknown.append(ln)
            i += 1
    return turns, dropped, unknown


def ledger_lines(entries: list) -> list[str]:
    out = []
    for e in entries:
        kind = e[0]
        if kind == "tool":
            out.append(f"- {TOOL_NAMES.get(e[1], e[1])} {e[2]}".rstrip())
        elif kind == "advisor":
            out.append(f"- advisor ({e[1]}, no arguments)")
        elif kind == "agents":
            out += [f"- Agent ({n}): subagent tool calls not visible to this session" for n in e[1]]
        else:
            for piece in re.sub(r"\s*\(ctrl\+o to expand\)", "", e[1]).split(", "):
                m = re.match(r"^(Read|Ran|Listed|Made)\s+(\d+)\s+(.*)$", piece.strip(), re.I)
                if not m:
                    out.append(f"- {piece.strip()} (collapsed in export)")
                    continue
                verb, n, noun = m.group(1).lower(), m.group(2), m.group(3)
                label = {"read": "Read", "ran": "Bash", "listed": "Directory listing", "made": "Edit"}[verb]
                out.append(f"- {label} ({n} {noun}, collapsed in export)")
    return out


def turn_texts(turn: dict, unwrap: bool) -> tuple[str, str]:
    lines = turn["user_lines"]
    while lines and not lines[-1].strip():
        lines = lines[:-1]
    user = " ".join(s.strip() for s in lines) if unwrap else "\n".join(lines)
    assistant = "\n\n".join("\n".join(b).rstrip() for b in turn["blocks"])
    return user, assistant


def parse_selection(spec: str, n: int) -> list[int]:
    chosen: list[int] = []
    for part in spec.split(","):
        a, _, b = part.partition("-")
        lo, hi = int(a), int(b or a)
        chosen += list(range(lo, hi + 1))
    bad = [k for k in chosen if not 1 <= k <= n]
    if bad:
        sys.exit(f"turn {bad[0]} does not exist; the file has {n} turns")
    return chosen


def redactor(extra: list[str]):
    rules = []
    for item in extra:
        lit, _, kind = item.partition("=")
        if not lit or not kind:
            sys.exit(f"--redact needs text=kind, got {item!r}")
        rules.append((lit, kind))

    def mark(kind: str) -> str:
        return f"[REDACTED:{kind.replace(' ', '-')}]"

    def run(text: str) -> str:
        for pat in PATH_RULES:
            text = pat.sub(lambda m: mark("path") + m.group(0)[len(m.group(0).rstrip(".,;:)'\"`]")):], text)
        for kind, pat in kb.lint.LEAK_PATTERNS:
            if kind != "absolute home path":
                text = pat.sub(mark(kind), text)

        def email(m):
            ok = m.group(1).lower() in kb.lint.EMAIL_OK_DOMAINS or m.group(0).split("@", 1)[0].lower() in NOREPLY
            return m.group(0) if ok else mark("email")
        text = kb.lint.EMAIL_RE.sub(email, text)
        for lit, kind in rules:
            text = text.replace(lit, mark(kind))
        return text
    return run


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("source", help="saved session file")
    p.add_argument("--format", choices=["claude-export", "json"], default="claude-export")
    p.add_argument("--list", action="store_true", help="list the turns and stop")
    p.add_argument("--turns", help="turns to log: 5, 5-7 or 1,3-4")
    p.add_argument("--unwrap-user", action="store_true", help="join the terminal's hard-wrapped lines of each user message")
    p.add_argument("--redact", action="append", default=[], metavar="TEXT=KIND", help="also redact this exact text")
    p.add_argument("--slug"); p.add_argument("--author", help="@handle"); p.add_argument("--platform")
    p.add_argument("--model", help="name and version; never guessed")
    p.add_argument("--role", choices=sorted(kb.lint.ROLES)); p.add_argument("--purpose")
    p.add_argument("--phase", choices=sorted(kb.lint.PHASES), default="exploration")
    p.add_argument("--significant", action="store_true"); p.add_argument("--reason")
    p.add_argument("--pr", type=int); p.add_argument("--claims", default="")
    p.add_argument("--supporting-doc", action="append", default=[])
    p.add_argument("--date"); p.add_argument("--id"); p.add_argument("--out"); p.add_argument("--force", action="store_true")
    a = p.parse_args()

    raw = Path(a.source).read_text(encoding="utf-8")
    dropped, unknown = Counter(), []
    if a.format == "json":
        data = json.loads(raw)
        turns = [{"user": t["user"], "assistant": t["assistant"], "ledger_lines": t.get("ledger", data.get("ledger", []))}
                 for t in data["turns"]]
        for t in turns:
            t["ledger_lines"] = list(t["ledger_lines"])
        texts = [(t["user"], t["assistant"]) for t in turns]
    else:
        turns, dropped, unknown = parse_claude_export(raw)
        texts = [turn_texts(t, a.unwrap_user) for t in turns]

    if a.list or not a.turns:
        for k, (user, _) in enumerate(texts, 1):
            print(f"{k:3}  {user.splitlines()[0][:80] if user.strip() else '(empty)'}")
        if not a.list:
            print("pick turns with --turns, for example --turns 5 or --turns 5-7")
        return 0

    for need in ("slug", "author", "platform", "model", "role", "purpose"):
        if not getattr(a, need):
            sys.exit(f"--{need} is required")
    if a.significant and not a.reason:
        sys.exit("--significant needs --reason")
    if not a.author.startswith("@"):
        sys.exit("--author must be a GitHub handle like @nacs-970")
    chosen = parse_selection(a.turns, len(texts))
    date = a.date or kb.today()
    log_id = a.id or f"{date}-{a.author.lstrip('@')}-{a.slug}"
    out = Path(a.out) if a.out else kb.ROOT / "prompts" / f"{log_id}.md"
    if out.exists() and not a.force:
        sys.exit(f"{out} exists. Pass --force to overwrite it.")

    scrub = redactor(a.redact)
    body, ledger, urls = [], [], []
    for n, k in enumerate(chosen, 1):
        user, assistant = texts[k - 1]
        body.append(f"## Turn {n} — user\n{scrub(user)}\n\n## Turn {n} — assistant\n{scrub(assistant)}\n")
        for u in URL_RE.findall(user):
            u = u.rstrip(".,;:")
            if u not in urls:
                urls.append(u)
        t = turns[k - 1]
        ledger += t["ledger_lines"] if a.format == "json" else ledger_lines(t["ledger"])
    ledger = [scrub(x) for x in ledger] or ["None."]
    collapsed_note = any("collapsed in export" in x for x in ledger)

    docs = list(dict.fromkeys(a.supporting_doc + urls))
    front = ["---", "doc_type: prompt-log", f"id: {log_id}", f'author: "{a.author}"', f"date: {date}",
             f"platform: {a.platform}", f"model: {kb.jstr(a.model)}", f"phase: {a.phase}", f"role: {a.role}",
             f"significant: {'true' if a.significant else 'false'}",
             f"significant_reason: {kb.jstr(a.reason) if a.significant else 'null'}",
             f"purpose: {a.purpose}", f"pr: {a.pr if a.pr is not None else 'null'}",
             "claims: [" + ", ".join(c.strip() for c in a.claims.split(",") if c.strip()) + "]", "redactions: 0"]
    front += (["supporting_docs:"] + [f"  - {u}" for u in docs]) if docs else ["supporting_docs: []"]
    front += ["---", ""]
    text = "\n".join(front) + "\n" + "\n".join(body) + "\n## Tool-call ledger\n" + "\n".join(ledger) + "\n"
    if collapsed_note:
        text += "\nThe terminal export collapses shell commands and reads, so their arguments are not listed.\n"
    text = text.replace("redactions: 0", f"redactions: {text.count('[REDACTED:')}", 1)
    out.write_text(text, encoding="utf-8")

    rel = out.relative_to(kb.ROOT) if kb.ROOT in out.resolve().parents else out
    print(f"wrote {rel}: {len(chosen)} turns, {text.count('[REDACTED:')} redactions, {len(ledger)} ledger lines")
    if dropped:
        print("dropped chrome:", ", ".join(f"{n} {k}" for k, n in sorted(dropped.items())))
    if unknown:
        print(f"{len(unknown)} unclassified lines were ignored; check the export. First: {unknown[0][:70]!r}")
    res = kb.run(sys.executable, "scripts/lint_front_matter.py")
    print("lint:", (res.stdout.strip().splitlines() or ["(no output)"])[-1])
    if res.returncode:
        print("\n".join(l for l in res.stdout.splitlines() if l.startswith("ERROR")))
    return res.returncode


if __name__ == "__main__":
    sys.exit(main())
