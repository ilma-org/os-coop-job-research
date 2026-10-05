#!/usr/bin/env python3
"""Estimate how many report pages the significant prompt logs will use.

The appendix counts toward the 10-15 page cap, so this shows the overrun early.
The estimate is rough (about 550 words per page of 12-point Times New Roman on A4).
Check the real page count in the final PDF.

Usage:
    python scripts/appendix_budget.py [--budget-pages 5]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint_front_matter import ROOT, split_front_matter  # noqa: E402

WORDS_PER_PAGE = 550


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--budget-pages", type=float, default=5.0,
                        help="pages available for the appendix (default 5)")
    args = parser.parse_args()

    significant: list[tuple[str, int]] = []
    other = 0
    for path in sorted((ROOT / "prompts").glob("*.md")):
        data, body, err = split_front_matter(path.read_text(encoding="utf-8"))
        if err or data is None:
            print(f"skipped {path.name}: {err or 'no front matter'}")
            continue
        if data.get("significant") is True:
            significant.append((path.name, len(body.split())))
        else:
            other += 1

    total = sum(words for _, words in significant)
    pages = total / WORDS_PER_PAGE
    for name, words in significant:
        print(f"{words:7d} words  {name}")
    print(f"significant logs: {len(significant)}, {total} words, about {pages:.1f} pages")
    print(f"non-significant logs: {other} (provided through the repo URL, not in the report)")
    print(f"budget: {args.budget_pages:g} pages")
    if pages > args.budget_pages:
        print(f"OVER BUDGET by about {pages - args.budget_pages:.1f} pages: "
              "mark fewer logs significant or shorten them.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
