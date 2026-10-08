#!/usr/bin/env python3
"""Add one claim to a topic note, with the quote and archive link checked by code.

  python3 scripts/add_claim.py <note.md> --claim "..." --url URL --quote "..." --title "Source title"
        [--type fact|org-fact|assumption] [--kind official-doc] [--archive auto|URL]
        [--os-concepts "processes,file systems"] [--new-note "Note title"] [--dry-run]

What it does, so an agent does not type it by hand:
  - takes the next free claim id in the topic directory
  - opens the page and refuses the claim unless the quote is in it word for word
  - for an org-fact, finds a Wayback snapshot and refuses it unless the quote is in it too
  - writes the YAML block with today's access date, status: unverified and pr: null
  - bumps `updated` in the note

An assumption needs only --claim. Needs PyYAML and network access.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import kb_common as kb
import verify_quote as vq

NOTE_STUB = """---
doc_type: topic-note
topic: {topic}
title: {title}
updated: {date}
claims: []
---

# {title}

## Summary

_TODO: 2 to 5 sentences, written only from the claims in the front matter._

## Key points

- _TODO: one point per line, ending with its claim IDs._
"""


def next_id(topic_dir: Path) -> str:
    prefix = topic_dir.name[:2]
    used = []
    for note in kb.notes_in(topic_dir):
        for claim in kb.claims_of(note):
            m = re.fullmatch(rf"{prefix}-(\d+)", str(claim.get("id", "")))
            if m:
                used.append(int(m.group(1)))
    return f"{prefix}-{max(used, default=0) + 1:02d}"


def find_archive(url: str, quote: str) -> str:
    """Newest Wayback snapshot of url that contains the quote."""
    api = ("https://web.archive.org/cdx/search/cdx?output=json&fl=timestamp&filter=statuscode:200&limit=-6&url="
           + urllib.parse.quote(url, safe=""))
    try:
        with urllib.request.urlopen(urllib.request.Request(api, headers={"User-Agent": "add_claim"}), timeout=60) as r:
            rows = json.load(r)
    except Exception as exc:  # network, timeout, bad JSON
        sys.exit(f"archive lookup failed ({exc}). Pass --archive <snapshot URL> yourself.")
    stamps = [row[0] for row in rows[1:]][::-1]  # newest first
    if not stamps:
        sys.exit("the Wayback Machine has no snapshot of this URL. Ask the person before requesting one, or pass --archive.")
    for ts in stamps:
        snap = f"https://web.archive.org/web/{ts}/{url}"
        try:
            if vq.find_quote(vq.fetch_text(snap), quote) == "exact":
                return snap
        except Exception:
            continue
    sys.exit("no recent snapshot contains the quote. Pass --archive <snapshot URL> yourself.")


def claim_block(cid: str, a: argparse.Namespace, archive: str | None) -> str:
    lines = [f"  - id: {cid}", f"    claim: {kb.jstr(a.claim)}", f"    type: {a.type}", "    status: unverified"]
    if a.type != "assumption":
        lines += ["    source:", f"      title: {kb.jstr(a.title)}", f"      url: {a.url}", f"      kind: {a.kind}",
                  f"      accessed: {kb.today()}", f"      archive: {archive or 'null'}",
                  f"    quote: {kb.jstr(a.quote)}"]
    concepts = [c.strip() for c in (a.os_concepts or "").split(",") if c.strip()]
    lines += [f"    os_concepts: [{', '.join(kb.jstr(c) for c in concepts)}]", "    pr: null"]
    return "\n".join(lines)


def insert_block(text: str, block: str) -> str:
    end = kb.front_matter_end(text)
    head, tail = text[:end], text[end:]
    if re.search(r"^claims: \[\]\s*$", head, re.M):
        head = re.sub(r"^claims: \[\]\s*$", "claims:\n" + block, head, count=1, flags=re.M)
        return head + tail
    pos = head.find("\nclaims:")
    if pos < 0 or re.search(r"^[A-Za-z_]\w*:", head[pos + 1:].split("\n", 1)[1], re.M):
        sys.exit("claims: is not the last key in the front matter. Add the block by hand.")
    return head + "\n" + block + tail


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("note", help="topic note file")
    p.add_argument("--claim", required=True)
    p.add_argument("--type", choices=["fact", "org-fact", "assumption"], default="fact")
    p.add_argument("--url")
    p.add_argument("--quote")
    p.add_argument("--title", help="source title")
    p.add_argument("--kind", default="official-doc", choices=sorted(kb.lint.SOURCE_KINDS))
    p.add_argument("--archive", help="'auto' (default for an org-fact) or a snapshot URL")
    p.add_argument("--os-concepts")
    p.add_argument("--new-note", metavar="TITLE", help="create the note with this title if it does not exist")
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()

    note = Path(a.note)
    if not note.exists():
        if not a.new_note:
            sys.exit(f"{note} does not exist. Pass --new-note \"Title\" to create it.")
        text = NOTE_STUB.format(topic=note.resolve().parent.name, title=kb.jstr(a.new_note), date=kb.today())
    else:
        text = note.read_text(encoding="utf-8")
    topic_dir = note.resolve().parent

    archive = None
    if a.type != "assumption":
        missing = [n for n in ("url", "quote", "title") if not getattr(a, n)]
        if missing:
            sys.exit("a fact or org-fact needs " + ", ".join("--" + m for m in missing))
        found = vq.find_quote(vq.fetch_text(a.url), a.quote)
        if found != "exact":
            sys.exit("quote is NOT in the page word for word" if found is None else
                     "quote matches only after normalising quote marks. Copy it again with the page's own quote marks.")
        if a.type == "org-fact" or a.archive:
            archive = a.archive if a.archive and a.archive != "auto" else find_archive(a.url, a.quote)
            if a.archive and a.archive != "auto" and vq.find_quote(vq.fetch_text(archive), a.quote) != "exact":
                sys.exit("quote is NOT in the archive snapshot word for word")

    cid = next_id(topic_dir)
    block = claim_block(cid, a, archive)
    new_text = kb.set_scalar(insert_block(text, block), "updated", kb.today())
    print(block)
    if a.dry_run:
        print(f"(dry run: {note} not written)")
        return 0
    note.write_text(new_text, encoding="utf-8")
    print(f"added {cid} to {note}. Run: python3 scripts/lint_front_matter.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
