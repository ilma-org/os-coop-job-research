#!/usr/bin/env python3
"""Helper for the blind AI author check (see ../SKILL.md).

  prepare  write one blind input file per note: claim text and URLs only, never the quote
  finish   read the checker's reports, compare quotes, write the author-check prompt log,
           and record ai_check on claims that passed

Needs PyYAML (pip install -r requirements.txt). The work directory (--out) must be
outside the repo, so the checker cannot read the notes by accident.
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is missing. Run: pip install -r requirements.txt")

DEFAULT_ROOT = Path(__file__).resolve().parents[4]
WRAPPER = "Read the file {path} and follow its instructions exactly. Read no other file on this machine."
HEADER = """You are an independent fact checker. You have no other context.

For each claim below, open its source URL yourself (WebFetch or curl) and decide whether the page supports the claim. Do not read any other file on this machine except this one. Do not look for other sources. Do not guess: if you cannot open a URL, say so.

For each claim, output exactly these five lines:
ID: <id>
VERDICT: supported | partial | unsupported
QUOTE: <one or two sentences copied verbatim from the page that best support the claim. Confirm in code that it is an exact substring of the page text.>
ARCHIVE: loads+quote-present | loads+quote-missing | fails | not-given   (only when an archive URL is listed)
ISSUES: <any wording in the claim that goes beyond what the page says, or: none>

Start your report with one line: MODEL: <your model name and exact model ID as given in your system prompt>.
Write the complete report to {report} and also return the same text as your final answer.

CLAIMS
"""
FRONT_RE = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.S)


def norm(text: str) -> str:
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"')):
        text = text.replace(a, b)
    return re.sub(r"\s+", " ", text).strip()


def load_note(path: Path) -> tuple[str, dict]:
    text = path.read_text(encoding="utf-8")
    match = FRONT_RE.match(text)
    if not match:
        sys.exit(f"{path}: no front matter")
    return text, yaml.safe_load(match.group(1))


def to_check(data: dict, ids: set[str] | None) -> list[dict]:
    out = []
    for claim in data.get("claims") or []:
        if claim.get("type") not in ("fact", "org-fact"):
            continue
        if ids is not None:
            if claim.get("id") in ids:
                out.append(claim)
        elif claim.get("status") == "unverified":
            out.append(claim)
    return out


def outside_repo(out: Path, root: Path) -> Path:
    out = out.resolve()
    if out == root or root in out.parents:
        sys.exit(f"--out must be outside the repo ({root}), so the checker cannot read the notes")
    out.mkdir(parents=True, exist_ok=True)
    return out


def input_path(out: Path, note: Path) -> Path:
    return out / f"input_{note.stem}.txt"


def report_path(out: Path, note: Path) -> Path:
    return out / f"report_{note.stem}.md"


def cmd_prepare(args: argparse.Namespace) -> None:
    root = Path(args.root).resolve()
    out = outside_repo(Path(args.out), root)
    ids = set(args.ids.split(",")) if args.ids else None
    for note in map(Path, args.notes):
        _, data = load_note(note)
        claims = to_check(data, ids)
        if not claims:
            print(f"{note}: no claims to check")
            continue
        lines = [HEADER.format(report=report_path(out, note))]
        for c in claims:
            lines.append(f"ID: {c['id']}\nCLAIM: {c['claim']}\nURL: {c['source']['url']}")
            if c["source"].get("archive"):
                lines.append(f"ARCHIVE URL: {c['source']['archive']}")
            lines.append("")
        path = input_path(out, note)
        path.write_text("\n".join(lines), encoding="utf-8")
        print(f"{note}: {len(claims)} claims -> {path}")
        print("  prompt for the checker:", WRAPPER.format(path=path))


def parse_report(path: Path) -> tuple[str | None, dict[str, dict]]:
    text = path.read_text(encoding="utf-8")
    model = re.search(r"^MODEL: (.+)$", text, re.M)
    results = {}
    for block in re.split(r"^(?=ID: )", text, flags=re.M):
        cid = re.match(r"ID: (\S+)", block)
        if not cid:
            continue
        verdict = re.search(r"^VERDICT: (\S+)", block, re.M)
        quote = re.search(r"^QUOTE: (.*)$", block, re.M)
        archive = re.search(r"^ARCHIVE: (\S+)", block, re.M)
        results[cid.group(1)] = {
            "verdict": verdict.group(1) if verdict else None,
            "quote": quote.group(1) if quote else "",
            "archive": archive.group(1) if archive else None,
        }
    return (model.group(1).strip() if model else None), results


def quote_relation(stored: str, agent: str) -> str:
    a, s = norm(agent), norm(stored)
    if not a:
        return "missing"
    if a == s:
        return "equal"
    if s in a:
        return "stored-in-agent"
    if a in s:
        return "agent-in-stored"
    return "different"


def judge(claim: dict, res: dict | None) -> tuple[bool, str]:
    if res is None:
        return False, "no entry in the report"
    rel = quote_relation(claim.get("quote") or "", res["quote"])
    problems = []
    if res["verdict"] != "supported":
        problems.append(f"verdict {res['verdict']}")
    if rel not in ("equal", "stored-in-agent"):
        problems.append(f"quote {rel}")
    if claim["source"].get("archive") and res["archive"] != "loads+quote-present":
        problems.append(f"archive {res['archive']}")
    return (not problems), (", ".join(problems) if problems else f"supported, quote {rel}")


def add_ai_check(text: str, cid: str, block: str) -> str:
    fm_end = FRONT_RE.match(text).end(1)
    start = text.find(f"\n  - id: {cid}\n", 0, fm_end)
    if start < 0:
        sys.exit(f"claim {cid} not found in front matter")
    nxt = text.find("\n  - id: ", start + 1, fm_end)
    end = nxt if nxt >= 0 else fm_end
    region = text[start:end]
    region, n = re.subn(r"^    status: unverified$", "    status: ai-checked", region, count=1, flags=re.M)
    if n != 1:
        sys.exit(f"claim {cid} is not status: unverified")
    return text[:start] + region + "\n" + block + text[end:]


def cmd_finish(args: argparse.Namespace) -> None:
    root = Path(args.root).resolve()
    out = Path(args.out).resolve()
    ids = set(args.ids.split(",")) if args.ids else None
    date = args.date or datetime.date.today().isoformat()
    models, checked, passed, urls, turns = set(), [], {}, [], []
    for i, note in enumerate(map(Path, args.notes), 1):
        text, data = load_note(note)
        claims = to_check(data, ids)
        if not claims:
            continue
        model, res = parse_report(report_path(out, note))
        if model:
            models.add(model)
        print(f"== {note.name}")
        for c in claims:
            ok, why = judge(c, res.get(c["id"]))
            print(f"{c['id']}: {'PASS' if ok else 'FAIL'} ({why})")
            checked.append(c["id"])
            if ok:
                passed.setdefault(note, []).append(c["id"])
            for u in (c["source"]["url"], c["source"].get("archive")):
                if u and u not in urls:
                    urls.append(u)
        wrapper = WRAPPER.format(path=input_path(out, note))
        turns.append((i, note, wrapper,
                      input_path(out, note).read_text(encoding="utf-8").rstrip("\n"),
                      report_path(out, note).read_text(encoding="utf-8").rstrip("\n")))
    if not checked:
        sys.exit("nothing was checked")
    model = args.model or (models.pop() if len(models) == 1 else None)
    if not model:
        sys.exit("reports name different models or none; pass --model")
    n_pass, n_all = sum(map(len, passed.values())), len(checked)
    print(f"{n_pass} of {n_all} claims passed")
    if args.dry_run:
        return

    def redact(s: str) -> str:
        for p in sorted({str(out), str(root)}, key=len, reverse=True):
            s = s.replace(p, "[REDACTED:path]")
        return s

    body = []
    ledger = [f"- Bash: python3 .agents/skills/agent-fact-check/scripts/blind_check.py prepare {len(turns)} note(s)"]
    for i, note, wrapper, inp, rep in turns:
        body.append(f"## Turn {i} — user\n{redact(wrapper)}\n\nContent of the input file:\n\n{redact(inp)}\n\n"
                    f"## Turn {i} — assistant\n{redact(rep)}\n")
        ledger.append(f"- Fresh agent context (blind check of {note.name}): its tool calls are not visible to this session")
    ledger.append("- Bash: python3 .agents/skills/agent-fact-check/scripts/blind_check.py finish")
    topic = Path(args.notes[0]).resolve().parent.name
    front = "\n".join([
        "---", "doc_type: prompt-log", f"id: {args.log_id}", f'author: "{args.author}"', f"date: {date}",
        f"platform: {args.platform}", f"model: {json.dumps(model, ensure_ascii=False)}", "phase: exploration",
        "role: author-check", "significant: false", "significant_reason: null",
        f"purpose: Blind author check of {n_all} claims in {topic}", "pr: null",
        "claims: [" + ", ".join(checked) + "]", "redactions: 0", "supporting_docs:",
        *[f"  - {u}" for u in urls], "---", ""])
    log = front + "\n" + "\n".join(body) + "\n## Tool-call ledger\n" + "\n".join(ledger) + "\n"
    log = log.replace("redactions: 0", f"redactions: {log.count('[REDACTED:')}", 1)
    (root / "prompts" / f"{args.log_id}.md").write_text(log, encoding="utf-8")

    for note, cids in passed.items():
        text = note.read_text(encoding="utf-8")
        for cid in cids:
            block = "\n".join([
                "    ai_check:", f"      platform: {args.platform}",
                f"      model: {json.dumps(model, ensure_ascii=False)}",
                f"      prompt_log: prompts/{args.log_id}.md", "      result: supported"])
            text = add_ai_check(text, cid, block)
        text = re.sub(r"^updated: .*$", f"updated: {date}", text, count=1, flags=re.M)
        note.write_text(text, encoding="utf-8")
    print(f"wrote prompts/{args.log_id}.md and ai_check on {n_pass} claims. Fix the FAIL claims, then run again with --ids.")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    for name, fn in (("prepare", cmd_prepare), ("finish", cmd_finish)):
        s = sub.add_parser(name)
        s.add_argument("notes", nargs="+", help="topic note files")
        s.add_argument("--out", required=True, help="work directory outside the repo")
        s.add_argument("--ids", help="comma-separated claim ids; default is every unverified fact/org-fact")
        s.add_argument("--root", default=str(DEFAULT_ROOT), help=argparse.SUPPRESS)
        s.set_defaults(fn=fn)
        if name == "finish":
            s.add_argument("--log-id", required=True, help="prompt log id, for example 2026-10-08-nacs-970-sre-book-author-check")
            s.add_argument("--author", required=True, help="GitHub handle, for example @nacs-970")
            s.add_argument("--platform", required=True, help="platform that ran the check, for example 'Claude Code'")
            s.add_argument("--model", help="model name and version; default is the MODEL line the reports agree on")
            s.add_argument("--date", help="YYYY-MM-DD; default today")
            s.add_argument("--dry-run", action="store_true", help="judge the reports and write nothing")
    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
