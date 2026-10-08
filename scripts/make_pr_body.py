#!/usr/bin/env python3
"""Draft a PR body from the repo, so an agent writes only the parts that need judgment.

  python3 scripts/make_pr_body.py [--base origin/main] [--head HEAD] [--out FILE]

A topic PR (changes inside one knowledge-base/<topic>/) is built from
.github/pull_request_template.md. Any other PR is built from
.github/PULL_REQUEST_TEMPLATE/repo-system.md. The script fills what the files and
git can tell:

  topic PR     topic, Issue, prompt logs, sources opened, claims added/changed/dropped,
               AI-check results, open items, platform and model, and the boxes it can check
  repo-system  areas touched, the commit list, and the boxes it can check

and leaves `<agent: ...>` placeholders for the rest: the goal, why, AI errors found,
how it was tested. It ticks a box only when code proved it. Fill every placeholder,
then run ship.py. --out must be outside the repo or under .local/.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

import kb_common as kb

TOPIC_TEMPLATE = ".github/pull_request_template.md"
SYSTEM_TEMPLATE = ".github/PULL_REQUEST_TEMPLATE/repo-system.md"
CONTENT_KEYS = ("claim", "type", "source", "quote", "os_concepts")
PLACEHOLDER = re.compile(r"<agent:")


def ph(text: str) -> str:
    return f"<agent: {text}>"


def files_changed(base: str, head: str) -> list[str]:
    return kb.git("diff", "--name-only", "--no-renames", "--diff-filter=ACMR", f"{base}...{head}").splitlines()


def parse_at(ref: str, path: str) -> tuple[dict | None, str]:
    text = kb.git("show", f"{ref}:{path}", check=False)
    if not text:
        return None, ""
    data, body, err = kb.lint.split_front_matter(text)
    return (None if err else data), body


def tick(text: str, needle: str) -> tuple[str, bool]:
    new, n = re.subn(rf"^- \[ \] (.*{re.escape(needle)}.*)$", r"- [x] \1", text, count=1, flags=re.M)
    return new, bool(n)


def set_item(text: str, label: str, value: str) -> str:
    return re.sub(rf"^- {re.escape(label)}:.*$", lambda _: f"- {label}: {value}", text, count=1, flags=re.M)


def set_section(text: str, heading: str, body: str, level: str = "###") -> str:
    pat = re.compile(rf"(^{level} {re.escape(heading)}[ \t]*\n)(.*?)(?=^#{{2,3}} |^---[ \t]*$|\Z)", re.M | re.S)
    m = pat.search(text)
    if not m:
        print(f"warning: template has no `{level} {heading}` section", file=sys.stderr)
        return text
    return text[:m.start(2)] + "\n" + body.strip("\n") + "\n\n" + text[m.end(2):]


def id_runs(ids: list[str]) -> str:
    def num(c: str) -> int:
        m = re.search(r"(\d+)$", c)
        return int(m.group(1)) if m else 0
    ids = sorted(ids, key=num)
    runs: list[list[str]] = []
    for cid in ids:
        if runs and num(cid) == num(runs[-1][-1]) + 1:
            runs[-1].append(cid)
        else:
            runs.append([cid])
    return ", ".join(r[0] if len(r) == 1 else f"{r[0]} to {r[-1]}" for r in runs) or "none"


def prompt_logs(head: str, changed: list[str]) -> list[dict]:
    logs = []
    for path in changed:
        if path.startswith("prompts/") and path.endswith(".md"):
            data, _ = parse_at(head, path)
            if data and data.get("doc_type") == "prompt-log":
                logs.append(data)
    return logs


def run_check(*cmd: str) -> bool:
    return kb.run(sys.executable, *cmd).returncode == 0


def topic_body(base: str, head: str, topic: str, changed: list[str]) -> str:
    template = (kb.ROOT / TOPIC_TEMPLATE).read_text(encoding="utf-8")
    merge_base = kb.git("merge-base", base, head).strip()
    index, index_body = parse_at(head, f"knowledge-base/{topic}/index.md")
    issue = (index or {}).get("issue")
    notes = [p for p in changed if p.startswith(f"knowledge-base/{topic}/") and p.endswith(".md")
             and not p.endswith("/index.md")]

    added, removed, changed_ids = [], [], {}
    by_url, results, open_items, claims_now = defaultdict(list), defaultdict(list), [], []
    all_have_check = True
    for path in notes:
        now, _ = parse_at(head, path)
        before, _ = parse_at(merge_base, path)
        now_c = {c["id"]: c for c in (now or {}).get("claims") or [] if isinstance(c, dict) and c.get("id")}
        old_c = {c["id"]: c for c in (before or {}).get("claims") or [] if isinstance(c, dict) and c.get("id")}
        added += [i for i in now_c if i not in old_c]
        removed += [i for i in old_c if i not in now_c]
        for cid, c in now_c.items():
            if cid in old_c:
                diff = [k for k in CONTENT_KEYS if json.dumps(c.get(k), sort_keys=True, default=str)
                        != json.dumps(old_c[cid].get(k), sort_keys=True, default=str)]
                if diff:
                    changed_ids[cid] = diff
            claims_now.append(c)
            src = c.get("source") or {}
            if src.get("url"):
                by_url[(src["url"], str(src.get("accessed")))].append(cid)
            if c.get("type") != "assumption":
                chk = c.get("ai_check") or {}
                if chk.get("result"):
                    results[chk["result"]].append(cid)
                else:
                    all_have_check = False
            if c.get("status") in ("unverified",) or c.get("type") == "assumption":
                open_items.append(cid)
    no_review_fields = not any(c.get("status") == "human-verified" or "review" in c or "ai_recheck" in c
                               for c in claims_now)

    logs = prompt_logs(head, changed)
    text = template
    text = text.replace("Topic: `<NN-slug>`", f"Topic: `{topic}`")
    text = text.replace("Closes #<issue>", f"Closes #{issue}" if issue else "Closes #<issue>")
    pm = "; ".join(dict.fromkeys(f"{d.get('platform')} / {d.get('model')}" for d in logs)) or ph("platform and model")
    dates = sorted(str(d.get("date")) for d in logs)
    text = set_item(text, "Platform and model", pm)
    text = set_item(text, "Session start and end", (f"{dates[0]} to {dates[-1]} (dates from the prompt logs; add times)"
                                                    if dates else ph("start and end")))
    text = set_item(text, "Topic directory and Issue", f"`knowledge-base/{topic}/`, Issue #{issue}" if issue else ph("topic and Issue"))

    text = set_section(text, "Goal", ph("one or two sentences: what this PR set out to find"))
    text = set_section(text, "Prompts", "\n".join(
        f"- `{d.get('id')}`: {d.get('role')}; {d.get('purpose')}" for d in logs) or ph("no prompt logs in this PR; say why"))
    text = set_section(text, "Sources opened", "\n".join(
        f"- {url} (accessed {acc}): claims {id_runs(ids)}" for (url, acc), ids in sorted(by_url.items()))
        or ph("no sources; every claim is an assumption?"))
    parts = [f"Added: {id_runs(added)} ({len(added)})" if added else "Added: none"]
    parts.append("Changed: " + ", ".join(f"{k} ({', '.join(v)})" for k, v in sorted(changed_ids.items())) if changed_ids
                 else "Changed: none")
    parts.append(f"Dropped: {id_runs(removed)}" if removed else "Dropped: none")
    text = set_section(text, "Claims added, changed or dropped", "\n".join(f"- {x}" for x in parts) + "\n\n"
                       + ph("why: one line per group"))
    text = set_section(text, "AI errors found and corrected", ph("what the AI said, what the source says, what you changed; or none found"))
    summary = ", ".join(f"{len(ids)} {res}" for res, ids in sorted(results.items())) or "no ai_check recorded"
    bad = [f"{res}: {id_runs(ids)}" for res, ids in results.items() if res != "supported"]
    log_ids = sorted({(c.get("ai_check") or {}).get("prompt_log", "") for c in claims_now if c.get("ai_check")} - {""})
    text = set_section(text, "AI fact-check results per claim", f"{summary}" + (f" ({'; '.join(bad)})" if bad else "")
                       + ("\n\nLogs: " + ", ".join(f"`{x}`" for x in log_ids) if log_ids else ""))
    gaps = re.search(r"^## Not found yet\s*\n(.*?)(?=^## |\Z)", index_body, re.M | re.S)
    gap_lines = [ln for ln in (gaps.group(1).splitlines() if gaps else []) if ln.startswith("- ")]
    text = set_section(text, "Open items", f"- Unverified claims and assumptions: {id_runs(open_items)}\n"
                       + ("- Not found yet (from index.md):\n" + "\n".join("  " + g for g in gap_lines) if gap_lines else ""))
    text = set_section(text, "Searches and commands run", "See the Tool-call ledger of each prompt log above.\n\n"
                       + ph("anything that is not in a ledger"))

    boxes = []
    text, ok = tick(text, "scripts/lint_front_matter.py` passes") if run_check("scripts/lint_front_matter.py") else (text, False)
    boxes.append(("lint passes", ok))
    if all_have_check and no_review_fields and claims_now:
        text, ok = tick(text, "I ran the blind AI check")
        boxes.append(("AI check recorded, no human-verified", ok))
    text = add_scan_box(text)
    return finish(text, base, head, boxes, scan_needle="pr_leak_scan.py")


def add_scan_box(text: str) -> str:
    if "pr_leak_scan.py" in text:
        return text
    box = ("- [ ] `python3 scripts/pr_leak_scan.py --body-file <this body saved to a file outside the repo>` passes. "
           "It scans every added line, the commit messages and this text.\n")
    return re.sub(r"(^- \[ \] `python3 scripts/lint_front_matter.py` passes\.\n)", lambda m: m.group(1) + box, text, count=1, flags=re.M)


def system_body(base: str, head: str, changed: list[str], issue: int | None) -> str:
    text = (kb.ROOT / SYSTEM_TEMPLATE).read_text(encoding="utf-8")
    areas = []
    for label, test in (("rules", lambda p: p in ("AGENTS.md", "README.md") or p.startswith("docs/")),
                        ("lint or scripts", lambda p: p.startswith("scripts/") or p == "requirements.txt"),
                        ("skills", lambda p: p.startswith(".agents/")),
                        ("CI or GitHub templates", lambda p: p.startswith(".github/"))):
        if any(test(p) for p in changed):
            areas.append(label)
    text = re.sub(r"^Area \(keep the ones that apply\):.*$", lambda _: "Area: " + (", ".join(areas) or "other"), text, count=1, flags=re.M)
    closes = f"Closes #{issue}" if issue else ""
    text = re.sub(r"^Closes #<issue>.*\n\n?", lambda _: closes + "\n\n" if closes else "", text, count=1, flags=re.M)
    commits = kb.git("log", "--reverse", "--format=- %h %s", f"{base}..{head}").strip()
    text = text.replace("This PR changes how the repo works. It adds, edits or verifies no claim. Claims go in a topic PR.",
                        "This PR changes how the repo works. It adds, edits or verifies no claim. Claims go in a topic PR.\n\n"
                        "Commits:\n" + commits, 1)
    for heading, hint in (("Why", "what problem this solves and who runs into it"),
                          ("How I tested it", "commands and decisive output"),
                          ("Impact and rollback", "who is affected, and how to undo it")):
        text = set_section(text, heading, ph(hint), level="##")
    logs = prompt_logs(head, changed)
    text = set_item(text, "Platform and model", "; ".join(dict.fromkeys(f"{d.get('platform')} / {d.get('model')}" for d in logs))
                    or ph("platform and model"))
    text = set_item(text, "Goal", ph("one sentence"))
    text = set_item(text, "Prompt log", ", ".join(f"`{d.get('id')}`" for d in logs) or ph('id, or "none" with the reason'))
    text = set_item(text, "Decisions, and AI errors I corrected", ph("what, or none"))
    text = set_item(text, "Searches and commands run", ph("summary"))
    boxes = []
    text, ok = tick(text, "scripts/lint_front_matter.py` passes") if run_check("scripts/lint_front_matter.py") else (text, False)
    boxes.append(("lint passes", ok))
    return finish(text, base, head, boxes, scan_needle="pr_leak_scan.py")


def finish(text: str, base: str, head: str, boxes: list[tuple[str, bool]], scan_needle: str) -> str:
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as tmp:
        tmp.write(text)
        name = tmp.name
    try:
        res = kb.run(sys.executable, "scripts/pr_leak_scan.py", "--base", base, "--head", head, "--body-file", name)
    finally:
        Path(name).unlink(missing_ok=True)
    clean = res.returncode == 0
    if clean:
        text, ok = tick(text, scan_needle)
        boxes.append(("leak scan passes", ok))
    else:
        print("leak scan FAILED, so its box stays unchecked:\n" + "\n".join(l for l in res.stdout.splitlines() if l.startswith("ERROR")),
              file=sys.stderr)
    print("boxes checked by code: " + (", ".join(n for n, ok in boxes if ok) or "none")
          + "; left for you: the rest", file=sys.stderr)
    return text


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--base", default="origin/main")
    p.add_argument("--head", default="HEAD")
    p.add_argument("--out", help="write the body here (outside the repo, or under .local/)")
    p.add_argument("--issue", type=int, help="Issue number for a repo-system PR (a topic PR reads it from index.md)")
    a = p.parse_args()

    changed = files_changed(a.base, a.head)
    if not changed:
        sys.exit(f"no changes between {a.base} and {a.head}")
    topics = sorted({p.split("/")[1] for p in changed if p.startswith("knowledge-base/") and p.count("/") >= 2})
    if len(topics) > 1:
        sys.exit("this PR touches more than one topic directory: " + ", ".join(topics) + ". Split it.")
    stray = [p for p in changed if topics and not (p.startswith(f"knowledge-base/{topics[0]}/") or p.startswith("prompts/"))]
    if stray:
        print("warning: a topic PR should hold only its topic directory and prompt logs. Also changed: "
              + ", ".join(stray[:6]) + (" ..." if len(stray) > 6 else ""), file=sys.stderr)
    body = topic_body(a.base, a.head, topics[0], changed) if topics else system_body(a.base, a.head, changed, a.issue)
    holes = len(PLACEHOLDER.findall(body))
    if a.out:
        out = kb.outside_repo_or_local(Path(a.out))
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(body, encoding="utf-8")
        print(f"wrote {out} ({holes} `<agent: ...>` placeholders to fill)")
    else:
        print(body)
        print(f"({holes} `<agent: ...>` placeholders to fill)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
