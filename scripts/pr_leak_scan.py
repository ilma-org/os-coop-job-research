#!/usr/bin/env python3
"""Scan a pull request for leaks before it goes public.

The front matter lint scans Markdown files only. This tool also scans:
  - the lines a PR adds, in every file type (scripts, YAML, text), not just *.md
  - commit messages, and author and committer email addresses
  - the PR title and body, where session summaries tend to leak paths
  - added file paths that must never be committed (cover page, .env, .local)

Usage:
    python3 scripts/pr_leak_scan.py                        # origin/main..HEAD, no PR text
    python3 scripts/pr_leak_scan.py --body-file body.md    # also scan the PR body you will submit
    python3 scripts/pr_leak_scan.py --pr 12                # also scan title and body of PR 12 (needs gh)
    python3 scripts/pr_leak_scan.py --base <sha> --head <sha> --title "..." --body-file body.md

It reuses the leak patterns of scripts/lint_front_matter.py. A line containing
`lint-allow` is skipped. The tool never prints a matched value, only where it is.
Exit code 1 on any error. Warnings (commit email addresses) fail only with --strict.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lint_front_matter as lint  # noqa: E402  (reuse its patterns so both tools agree)

EXTRA_PATTERNS = [
    ("agent scratch path", re.compile(r"/tmp/claude-\d+/")),
]
DENIED_PATHS = [
    ("cover page file", re.compile(r"^cover/|(^|/)cover-page\.[^/]+$|^report/cover[^/]*$")),
    ("environment file", re.compile(r"(^|/)\.env(\.(?!example$|sample$)[^/]+)?$")),
    ("local-only file", re.compile(r"^\.local/")),
]
EMAIL_META_OK = set(lint.EMAIL_OK_DOMAINS) | {"github.com"}
NOREPLY_LOCAL_PARTS = {"noreply", "no-reply"}


class Findings:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.lines = 0

    def error(self, where: str, msg: str) -> None:
        self.errors.append(f"ERROR   {where}: {msg}")

    def warn(self, where: str, msg: str) -> None:
        self.warnings.append(f"WARNING {where}: {msg}")


def git(*args: str) -> str:
    res = subprocess.run(["git", *args], capture_output=True, text=True)
    if res.returncode != 0:
        sys.exit(f"git {' '.join(args)} failed: {res.stderr.strip()}")
    return res.stdout


def scan_line(f: Findings, where: str, lineno: int, line: str) -> None:
    f.lines += 1
    if "lint-allow" in line:
        return
    seen = set()
    for kind, pattern in lint.LEAK_PATTERNS + EXTRA_PATTERNS:
        if kind not in seen and pattern.search(line):
            seen.add(kind)
            f.error(where, f"line {lineno}: possible {kind}")
    for match in lint.EMAIL_RE.finditer(line):
        if match.group(0).split("@", 1)[0].lower() in NOREPLY_LOCAL_PARTS:
            continue  # a noreply address names no person, for example a Co-Authored-By trailer
        if match.group(1).lower() not in lint.EMAIL_OK_DOMAINS:
            f.error(where, f"line {lineno}: possible email address")
            break


def scan_text(f: Findings, where: str, text: str) -> None:
    for n, line in enumerate(text.splitlines(), 1):
        scan_line(f, where, n, line)


def scan_diff(f: Findings, base: str, head: str) -> int:
    paths = git("diff", "--name-only", "--no-renames", "--diff-filter=ACMR", f"{base}...{head}").splitlines()
    for path in paths:
        for kind, pattern in DENIED_PATHS:
            if pattern.search(path):
                f.error(f"diff {path}", f"{kind} must not be committed")
    diff = git("diff", "--unified=0", "--no-color", "--no-ext-diff", "--no-renames", f"{base}...{head}")
    path, lineno = None, 0
    for line in diff.splitlines():
        if line.startswith("+++ "):
            path = line[6:] if line.startswith("+++ b/") else None
        elif line.startswith("@@"):
            match = re.match(r"@@ -\S+ \+(\d+)", line)
            lineno = int(match.group(1)) if match else 0
        elif line.startswith("+") and path:
            scan_line(f, f"diff {path}", lineno, line[1:])
            lineno += 1
    return len(paths)


def scan_commits(f: Findings, base: str, head: str) -> int:
    out = git("log", "--format=%H%x1f%ae%x1f%ce%x1f%B%x1e", f"{base}..{head}")
    records = [r.strip("\n") for r in out.split("\x1e") if r.strip()]
    for rec in records:
        sha, author, committer, message = rec.split("\x1f", 3)
        short = sha.strip()[:7]
        scan_text(f, f"commit {short} message", message)
        for role, email in (("author", author), ("committer", committer)):
            domain = email.rsplit("@", 1)[-1].lower()
            if domain not in EMAIL_META_OK:
                f.warn(f"commit {short}", f"{role} email is on {domain}. Use a GitHub noreply address "
                       "(git config user.email <id>+<handle>@users.noreply.github.com) before you push")
    return len(records)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--base", default="origin/main", help="base ref or sha (default origin/main)")
    p.add_argument("--head", default="HEAD", help="head ref or sha (default HEAD)")
    p.add_argument("--title", help="PR title text to scan")
    p.add_argument("--body-file", help="file holding the PR body to scan")
    p.add_argument("--pr", type=int, help="scan title and body of this PR number, read with gh")
    p.add_argument("--strict", action="store_true", help="fail on warnings too")
    args = p.parse_args()

    f = Findings()
    files = scan_diff(f, args.base, args.head)
    commits = scan_commits(f, args.base, args.head)

    title, body = args.title, None
    if args.body_file:
        body = Path(args.body_file).read_text(encoding="utf-8")
    if args.pr is not None:
        res = subprocess.run(["gh", "pr", "view", str(args.pr), "--json", "title,body"], capture_output=True, text=True)
        if res.returncode != 0:
            sys.exit(f"gh pr view {args.pr} failed: {res.stderr.strip()}")
        data = json.loads(res.stdout)
        title, body = title or data["title"], body if body is not None else data["body"]
    if title:
        scan_text(f, "PR title", title)
    if body is not None:
        scan_text(f, "PR body", body)
    text = "title and body" if (title and body is not None) else "title" if title else "body" if body is not None else "not given"

    print(f"scanned {f.lines} lines in {files} files, {commits} commits, PR text: {text}")
    if body is None and title is None:
        print("NOTICE  no PR text scanned. Pass --body-file or --pr to scan the PR body.")
    for line in f.warnings + f.errors:
        print(line)
    failed = bool(f.errors) or (args.strict and bool(f.warnings))
    print(f"pr leak scan {'FAILED' if failed else 'passed'}: {len(f.errors)} errors, {len(f.warnings)} warnings")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
