#!/usr/bin/env python3
"""Check that a quote appears verbatim in a web page.

  python3 scripts/verify_quote.py <url> "<quote>"

Fetches the page, strips tags, collapses whitespace and looks for the quote.
Prints one of: EXACT, ONLY AFTER NORMALISING QUOTES, NOT FOUND (exit 1).
Needs only the Python standard library. Other scripts import find_quote().
"""
from __future__ import annotations

import html
import re
import sys
import urllib.request
from html.parser import HTMLParser


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def squash(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def plain_quotes(s: str) -> str:
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"')):
        s = s.replace(a, b)
    return s


def fetch_text(url: str) -> str:
    """Return the visible text of a page with whitespace collapsed."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (verify_quote)"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read().decode(resp.headers.get_content_charset() or "utf-8", "replace")
    parser = Text()
    parser.feed(raw)
    return squash(html.unescape(" ".join(parser.parts)))


def find_quote(page: str, quote: str) -> str | None:
    """Return "exact", "quotes" (only after normalising quote marks) or None."""
    q = squash(quote)
    if q in page:
        return "exact"
    if plain_quotes(q) in plain_quotes(page):
        return "quotes"
    return None


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 0 if sys.argv[1:] in (["-h"], ["--help"]) else 2
    found = find_quote(fetch_text(sys.argv[1]), sys.argv[2])
    if found == "exact":
        print("EXACT")
        return 0
    if found == "quotes":
        print("ONLY AFTER NORMALISING QUOTES: copy the quote again with the page's own quote marks")
        return 0
    print("NOT FOUND")
    return 1


if __name__ == "__main__":
    sys.exit(main())
