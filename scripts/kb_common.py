"""Shared helpers for the workflow scripts in this folder (not run on its own)."""
from __future__ import annotations

import datetime
import json
import re
import subprocess
import sys
from pathlib import Path

import lint_front_matter as lint  # needs PyYAML; also gives the same ROOT and patterns

ROOT = lint.ROOT
KB = ROOT / "knowledge-base"
FRONT_RE = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.S)


def today() -> str:
    return datetime.date.today().isoformat()


def jstr(value: str) -> str:
    """A string as a YAML double-quoted scalar (JSON strings are valid YAML)."""
    return json.dumps(value, ensure_ascii=False)


def git(*args: str, check: bool = True) -> str:
    res = subprocess.run(["git", *args], capture_output=True, text=True, cwd=ROOT)
    if check and res.returncode != 0:
        sys.exit(f"git {' '.join(args)} failed: {res.stderr.strip()}")
    return res.stdout


def run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(list(args), capture_output=True, text=True, cwd=ROOT)


def load_note(path: Path) -> tuple[str, dict, str]:
    """Return (text, front matter, body) of a Markdown file with front matter."""
    text = Path(path).read_text(encoding="utf-8")
    data, body, err = lint.split_front_matter(text)
    if err or data is None:
        sys.exit(f"{path}: {err or 'no front matter'}")
    return text, data, body


def front_matter_end(text: str) -> int:
    """Index of the newline that closes the last front matter line."""
    match = FRONT_RE.match(text)
    if not match:
        sys.exit("no front matter")
    return match.end(1)


def set_scalar(text: str, key: str, value: str) -> str:
    """Set a top-level `key: value` line inside the front matter."""
    end = front_matter_end(text)
    head, tail = text[:end], text[end:]
    head, n = re.subn(rf"^{re.escape(key)}: .*$", f"{key}: {value}", head, count=1, flags=re.M)
    if n != 1:
        sys.exit(f"front matter has no `{key}:` line")
    return head + tail


def topic_dirs() -> list[Path]:
    return sorted(p for p in KB.iterdir() if p.is_dir() and lint.TOPIC_DIR_RE.match(p.name))


def notes_in(topic_dir: Path) -> list[Path]:
    return sorted(p for p in topic_dir.glob("*.md") if p.name != "index.md")


def claims_of(path: Path) -> list[dict]:
    _, data, _ = load_note(path)
    return [c for c in (data.get("claims") or []) if isinstance(c, dict)]


def resolve_topic(arg: str | None) -> Path:
    """A topic directory from a name, a number prefix or a path; default from the branch name."""
    if not arg:
        branch = git("branch", "--show-current").strip()
        arg = branch.split("/", 1)[0]
    candidate = Path(arg)
    if candidate.is_dir():
        return candidate.resolve()
    for d in topic_dirs():
        if d.name == arg or d.name.startswith(arg + "-"):
            return d
    sys.exit(f"no topic directory matches {arg!r}")


def outside_repo_or_local(path: Path) -> Path:
    """Refuse a file path inside the repo, except under .local/, so a draft is never committed by accident."""
    path = Path(path).resolve()
    if (path == ROOT or ROOT in path.parents) and ".local" not in path.relative_to(ROOT).parts[:1]:
        sys.exit(f"{path} is inside the repo. Use a path outside it, or under .local/")
    return path
