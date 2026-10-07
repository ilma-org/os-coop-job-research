#!/usr/bin/env python3
"""Refresh the notes list in a topic's index.md from the notes' own front matter.

  python3 scripts/update_index.py [<topic>] [--issue N] [--dry-run]

<topic> is a directory name, a number prefix (07) or a path. Default: the topic
named by the current branch. The notes list sits between these markers, which the
script adds on the first run:

  <!-- notes:start -->
  <!-- notes:end -->

It writes one line per note, in claim id order: file, the note's title, claim id ranges and counts by status.
It replaces hand-written descriptions in that list with the note title.
Everything else in index.md (scope, gaps, sources covered) is left alone.
It sets `issue` when you pass --issue, and bumps `updated` only when something changed.
"""
from __future__ import annotations

import argparse
import difflib
import re
import sys
from collections import Counter

import kb_common as kb

START, END = "<!-- notes:start -->", "<!-- notes:end -->"
HEADING = "## Notes in this directory"


def id_key(cid: str) -> tuple[int, str]:
    m = re.search(r"(\d+)$", cid)
    return (int(m.group(1)) if m else 0, cid)


def id_runs(ids: list[str]) -> str:
    """07-01, 07-02, 07-03, 07-29 -> "07-01 to 07-03, 07-29"."""
    runs: list[list[str]] = []
    for cid in ids:
        if runs and id_key(cid)[0] == id_key(runs[-1][-1])[0] + 1:
            runs[-1].append(cid)
        else:
            runs.append([cid])
    return ", ".join(r[0] if len(r) == 1 else f"{r[0]} to {r[-1]}" for r in runs)


def note_line(note) -> tuple[tuple[int, str], str]:
    _, data, _ = kb.load_note(note)
    claims = [c for c in (data.get("claims") or []) if isinstance(c, dict)]
    ids = sorted((str(c.get("id")) for c in claims), key=id_key)
    counts = Counter(str(c.get("status")) for c in claims)
    span = id_runs(ids) if ids else "no claims"
    by_status = ", ".join(f"{n} {s}" for s, n in sorted(counts.items()))
    suffix = f" {len(claims)} claims ({span})" + (f": {by_status}." if by_status else ".")
    first = id_key(ids[0]) if ids else (10**9, note.name)
    return first, f"- [{note.name}]({note.name}): {data.get('title', note.stem)}.{suffix}"


def replace_list(body: str, lines: list[str]) -> str:
    managed = f"{START}\n" + "\n".join(lines) + f"\n{END}"
    if START in body and END in body:
        return re.sub(rf"{re.escape(START)}.*?{re.escape(END)}", lambda _: managed, body, count=1, flags=re.S)
    pos = body.find(HEADING)
    if pos < 0:
        sys.exit(f"index.md has no `{HEADING}` heading")
    sec_start = body.index("\n", pos) + 1
    nxt = re.search(r"^## ", body[sec_start:], re.M)
    sec_end = sec_start + nxt.start() if nxt else len(body)
    section = body[sec_start:sec_end]
    m = re.search(r"(?:^- .*(?:\n|$))+", section, re.M)
    if m:
        section = section[:m.start()] + managed + "\n" + section[m.end():]
    else:
        section = section.rstrip("\n") + "\n\n" + managed + "\n\n"
    return body[:sec_start] + section + body[sec_end:]


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("topic", nargs="?")
    p.add_argument("--issue", type=int)
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()

    topic = kb.resolve_topic(a.topic)
    index = topic / "index.md"
    text = index.read_text(encoding="utf-8")
    notes = kb.notes_in(topic)
    lines = [line for _, line in sorted(note_line(n) for n in notes)] or ["- none yet"]

    end = kb.front_matter_end(text)
    new = text[:end] + replace_list(text[end:], lines)
    if a.issue is not None:
        new = kb.set_scalar(new, "issue", str(a.issue))
    if new != text:
        new = kb.set_scalar(new, "updated", kb.today())
    if new == text:
        print(f"{index.relative_to(kb.ROOT)}: already up to date")
        return 0
    diff = difflib.unified_diff(text.splitlines(), new.splitlines(), "index.md (before)", "index.md (after)", lineterm="", n=1)
    print("\n".join(diff))
    if a.dry_run:
        print("(dry run: nothing written)")
        return 0
    index.write_text(new, encoding="utf-8")
    print(f"wrote {index.relative_to(kb.ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
