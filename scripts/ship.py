#!/usr/bin/env python3
"""Run the pre-PR checks, draft the PR body, and open the PR only when told to.

  python3 scripts/ship.py prepare                  # lint, leak scan, draft body in .local/pr-body.md
  python3 scripts/ship.py open --title-text "add networking claims"             # dry run: checks, prints the commands
  python3 scripts/ship.py open --title-text "add networking claims" --yes       # push and open the PR

prepare   refuses `main`, runs the lint and make_pr_body.py, scans the body with
          pr_leak_scan.py, and tells you how many `<agent: ...>` placeholders to fill.
open      checks the branch name, a clean tree, the filled body (no placeholders,
          a `Closes #n` line for a topic PR), the lint and the leak scan on the diff,
          commits and the body. The title is `[<topic>] <title-text>` for a topic branch
          or `[meta] <title-text>` for a chore/ or meta/ branch.
          Without --yes it stops and prints what it would run. With --yes it runs
          `git push -u origin HEAD` and `gh pr create`. It never approves or merges.
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

import kb_common as kb

DEFAULT_BODY = kb.ROOT / ".local" / "pr-body.md"


def step(label: str, proc: subprocess.CompletedProcess) -> bool:
    ok = proc.returncode == 0
    last = (proc.stdout.strip().splitlines() or [""])[-1]
    print(f"{'ok  ' if ok else 'FAIL'} {label}: {last}")
    if not ok:
        print("\n".join(l for l in proc.stdout.splitlines() if l.startswith(("ERROR", "FAIL"))) or proc.stderr.strip())
    return ok


def current_branch() -> str:
    branch = kb.git("branch", "--show-current").strip()
    if branch in ("main", ""):
        sys.exit("you are on main (or a detached HEAD). Switch to your PR branch first.")
    return branch


def title_prefix(branch: str) -> tuple[str, bool]:
    """Return (prefix, is_topic) from the branch name."""
    head = branch.split("/", 1)[0]
    if head in ("chore", "meta"):
        return "[meta]", False
    if kb.lint.TOPIC_DIR_RE.match(head):
        return f"[{head}]", True
    sys.exit(f"branch {branch!r} does not look like <NN>-<slug>/<short-description>, chore/<...> or meta/<...>")


def cmd_prepare(a: argparse.Namespace) -> int:
    branch = current_branch()
    title_prefix(branch)
    body = kb.outside_repo_or_local(Path(a.body_file))
    body.parent.mkdir(parents=True, exist_ok=True)
    if kb.git("status", "--porcelain").strip():
        print("warning: uncommitted changes. The body describes commits only.")
    if not step("lint", kb.run(sys.executable, "scripts/lint_front_matter.py")):
        return 1
    res = kb.run(sys.executable, "scripts/make_pr_body.py", "--base", a.base, "--out", str(body))
    print(res.stderr.strip())
    if not step("draft body", res):
        return 1
    holes = len(re.findall(r"<agent:", body.read_text(encoding="utf-8")))
    ok = step("leak scan", kb.run(sys.executable, "scripts/pr_leak_scan.py", "--base", a.base, "--body-file", str(body)))
    print(f"\nbody: {body}\nfill the {holes} `<agent: ...>` placeholders and review the unchecked boxes, then run: "
          f"python3 scripts/ship.py open --title-text \"...\"")
    return 0 if ok else 1


def cmd_open(a: argparse.Namespace) -> int:
    branch = current_branch()
    prefix, is_topic = title_prefix(branch)
    body = Path(a.body_file)
    if not body.is_file():
        sys.exit(f"{body} not found. Run `ship.py prepare` first.")
    text = body.read_text(encoding="utf-8")
    problems = []
    if kb.git("status", "--porcelain").strip():
        problems.append("the working tree has uncommitted changes")
    if re.search(r"<agent:", text):
        problems.append(f"{len(re.findall(r'<agent:', text))} `<agent: ...>` placeholders are still in the body")
    if is_topic and not re.search(r"^Closes #\d+\s*$", text, re.M):
        problems.append("a topic PR body needs a `Closes #<issue>` line")
    if problems:
        print("not ready:\n- " + "\n- ".join(problems))
        return 1
    title = f"{prefix} {a.title_text}"
    ok = step("lint", kb.run(sys.executable, "scripts/lint_front_matter.py"))
    ok &= step("leak scan", kb.run(sys.executable, "scripts/pr_leak_scan.py", "--base", a.base,
                                   "--title", title, "--body-file", str(body)))
    if not ok:
        return 1
    push = ["git", "push", "-u", "origin", "HEAD"]
    create = ["gh", "pr", "create", "--title", title, "--body-file", str(body), "--base", "main"] + (["--draft"] if a.draft else [])
    print("\nwould run:\n  " + " ".join(push) + "\n  " + " ".join(f'"{c}"' if " " in c else c for c in create))
    if not a.yes:
        print("\ndry run. Add --yes to push and open the PR.")
        return 0
    if not shutil.which("gh"):
        sys.exit("gh is not installed")
    if subprocess.run(push, cwd=kb.ROOT).returncode:
        return 1
    return subprocess.run(create, cwd=kb.ROOT).returncode


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("prepare", "open"):
        s = sub.add_parser(name)
        s.add_argument("--base", default="origin/main")
        s.add_argument("--body-file", default=str(DEFAULT_BODY))
    o = sub.choices["open"]
    o.add_argument("--title-text", required=True, help="the part after the [topic] prefix")
    o.add_argument("--draft", action="store_true")
    o.add_argument("--yes", action="store_true", help="really push and open the PR")
    a = p.parse_args()
    return cmd_prepare(a) if a.cmd == "prepare" else cmd_open(a)


if __name__ == "__main__":
    sys.exit(main())
