#!/usr/bin/env python3
"""Show claim progress per topic, computed from the files (read-only).

  python3 scripts/status.py                 # one row per topic
  python3 scripts/status.py <topic>         # detail for one topic (name, number prefix or path)
  python3 scripts/status.py --json          # the same data as JSON

Columns: notes, claims, unverified / ai-checked / human-verified / disputed,
`no ai_check` (fact and org-fact claims past `unverified` with no ai_check block,
or `ai-checked` without one), and `no summary` (notes missing `## Summary`
or `## Key points`). The Issue state needs gh; see the issue-status skill.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

import kb_common as kb

STATUSES = ["unverified", "ai-checked", "human-verified", "disputed"]


def gaps(index_body: str) -> list[str]:
    m = re.search(r"^## Not found yet\s*\n(.*?)(?=^## |\Z)", index_body, re.M | re.S)
    return [ln[2:].strip() for ln in (m.group(1).splitlines() if m else []) if ln.startswith("- ")]


def topic_stats(topic: Path) -> dict:
    _, idx, idx_body = kb.load_note(topic / "index.md")
    counts, types, no_ai, no_summary, claims_out = Counter(), Counter(), [], [], []
    notes = kb.notes_in(topic)
    for note in notes:
        _, data, body = kb.load_note(note)
        if not all(re.search(rf"^##[ \t]+{h}[ \t]*$", body, re.M) for h in ("Summary", "Key points")):
            no_summary.append(note.name)
        for c in data.get("claims") or []:
            if not isinstance(c, dict):
                continue
            status, ctype = str(c.get("status")), str(c.get("type"))
            counts[status] += 1
            types[ctype] += 1
            if ctype != "assumption" and status != "unverified" and not c.get("ai_check"):
                no_ai.append(str(c.get("id")))
            claims_out.append({"id": c.get("id"), "status": status, "type": ctype, "note": note.name})
    return {
        "topic": topic.name, "owner": idx.get("owner"), "issue": idx.get("issue"), "notes": len(notes),
        "claims": sum(counts.values()), "by_status": {s: counts.get(s, 0) for s in STATUSES},
        "by_type": dict(types), "no_ai_check": no_ai, "notes_without_summary": no_summary,
        "not_found_yet": gaps(idx_body), "claim_list": claims_out,
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("topic", nargs="?")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    topics = [kb.resolve_topic(a.topic)] if a.topic else kb.topic_dirs()
    stats = [topic_stats(t) for t in topics]
    if a.json:
        print(json.dumps(stats, indent=2))
        return 0
    if a.topic:
        s = stats[0]
        print(f"{s['topic']}  owner {s['owner']}  issue #{s['issue']}  {s['notes']} notes, {s['claims']} claims")
        print("  by status:", ", ".join(f"{k} {v}" for k, v in s["by_status"].items()))
        print("  by type:  ", ", ".join(f"{k} {v}" for k, v in sorted(s["by_type"].items())) or "none")
        print("  claims past unverified with no ai_check:", ", ".join(s["no_ai_check"]) or "none")
        print("  notes without Summary/Key points:", ", ".join(s["notes_without_summary"]) or "none")
        print("  not found yet:")
        for g in s["not_found_yet"] or ["(none listed)"]:
            print("   -", g)
        return 0
    head = f"{'topic':40} {'owner':14} {'iss':>4} {'notes':>5} {'claims':>6} {'unv':>4} {'ai':>4} {'hum':>4} {'dis':>4} {'no ai_check':>11} {'no summary':>10}"
    print(head)
    for s in stats:
        b = s["by_status"]
        print(f"{s['topic']:40} {str(s['owner']):14} {str(s['issue'] or '-'):>4} {s['notes']:>5} {s['claims']:>6} "
              f"{b['unverified']:>4} {b['ai-checked']:>4} {b['human-verified']:>4} {b['disputed']:>4} "
              f"{len(s['no_ai_check']):>11} {len(s['notes_without_summary']):>10}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
