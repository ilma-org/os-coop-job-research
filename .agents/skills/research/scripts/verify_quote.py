#!/usr/bin/env python3
"""Check that a quote appears verbatim in a web page.

  python3 verify_quote.py <url> "<quote>"

Fetches the page, strips tags, collapses whitespace and looks for the quote.
Prints one of: EXACT, ONLY AFTER NORMALISING QUOTES, NOT FOUND (exit 1).
Needs only the Python standard library.
"""
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


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    url, quote = sys.argv[1], sys.argv[2]
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (verify_quote)"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read().decode(resp.headers.get_content_charset() or "utf-8", "replace")
    parser = Text()
    parser.feed(raw)
    page = squash(html.unescape(" ".join(parser.parts)))
    q = squash(quote)
    if q in page:
        print("EXACT")
        return 0
    if plain_quotes(q) in plain_quotes(page):
        print("ONLY AFTER NORMALISING QUOTES: copy the quote again with the page's own quote marks")
        return 0
    print("NOT FOUND")
    return 1


if __name__ == "__main__":
    sys.exit(main())
