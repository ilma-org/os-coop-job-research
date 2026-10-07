#!/usr/bin/env python3
"""Lint the knowledge base: front matter, status gates, and a leak scan.

Usage:
    python scripts/lint_front_matter.py

Optional environment variables (CI sets them on pull requests):
    PR_AUTHOR  GitHub login of the PR author. Enables the review.by check.
    BASE_SHA   Base commit of the PR. Enables the topic-owner warning.

The exit code is 1 when any error is found. Warnings never fail the run.
The rules are described in docs/schema.md.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is missing. Run: pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parent.parent
KB = "knowledge-base"
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__", ".local"}

TOPIC_DIR_RE = re.compile(r"^(\d{2})-[a-z0-9]+(?:-[a-z0-9]+)*$")
CLAIM_ID_RE = re.compile(r"^(\d{2})-(\d+)$")
HANDLE_RE = re.compile(r"^@[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?$")
URL_RE = re.compile(r"^https?://\S+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TURN_RE = re.compile(r"^## Turn \d+ [-–—] user\s*$", re.M)
LEDGER_RE = re.compile(r"^## Tool-call ledger\s*$", re.M)
REDACT_RE = re.compile(r"\[REDACTED:[^\]\s]+\]")

TYPES = {"fact", "org-fact", "assumption"}
STATUSES = {"unverified", "ai-checked", "human-verified", "disputed"}
SOURCE_KINDS = {"job-ad", "official-doc", "paper", "article", "video", "other"}
AI_RESULTS = {"supported", "partial", "unsupported"}
REVIEW_RESULTS = {"pass", "fail"}
PHASES = {"exploration", "report"}
ROLES = {"research", "author-check", "reviewer-recheck", "session-summary", "drafting"}
CLAIM_KEYS = {
    "id", "claim", "type", "status", "source", "quote", "os_concepts", "pr",
    "ai_check", "ai_recheck", "review", "note", "issue",
}

EMAIL_OK_DOMAINS = {"example.com", "example.org", "users.noreply.github.com"}
LEAK_PATTERNS = [
    ("absolute home path", re.compile(r"(?<![\w.:/-])/(?:home|Users)/[A-Za-z0-9._-]+")),
    ("absolute home path", re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+")),
    ("phone number", re.compile(r"(?<![\d-])0[6-9]\d[- .]?\d{3}[- .]?\d{4}(?![\d-])")),
    ("phone number", re.compile(r"\+66[- ]?\d{1,2}[- ]?\d{3,4}[- ]?\d{4}")),
    ("9-digit ID", re.compile(r"(?<![\d.])\d{9}(?![\d.])")),
    ("13-digit ID", re.compile(r"(?<![\d.])\d{13}(?![\d.])")),
    ("token", re.compile(r"\b(?:ghp|gho|ghs|ghu|ghr)_[A-Za-z0-9]{20,}")),
    ("token", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}")),
    ("token", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}")),
    ("token", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("token", re.compile(r"\bAIza[0-9A-Za-z_-]{35}")),
    ("token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}")),
    ("private key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
]
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@([A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,})")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.notices: list[str] = []

    def error(self, path: str, msg: str) -> None:
        self.errors.append(f"ERROR   {path}: {msg}")

    def warn(self, path: str, msg: str) -> None:
        self.warnings.append(f"WARNING {path}: {msg}")

    def notice(self, msg: str) -> None:
        self.notices.append(f"NOTICE  {msg}")


def nonblank(value: object) -> bool:
    return isinstance(value, str) and value.strip() != ""


def is_date(value: object) -> bool:
    if isinstance(value, dt.date):
        return True
    if isinstance(value, str) and DATE_RE.match(value):
        try:
            dt.date.fromisoformat(value)
            return True
        except ValueError:
            return False
    return False


def is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def split_front_matter(text: str) -> tuple[dict | None, str, str | None]:
    """Return (data, body, error). data is None when there is no front matter."""
    text = text.lstrip("﻿")
    if not text.startswith("---"):
        return None, text, None
    match = re.match(r"---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|$)", text, re.S)
    if not match:
        return None, text, "front matter is not closed with a line containing only ---"
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return None, text, f"front matter is not valid YAML: {str(exc).splitlines()[0]}"
    if not isinstance(data, dict):
        return None, text, "front matter must be a YAML mapping"
    return data, text[match.end():], None


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def handle_ok(value: object) -> bool:
    return isinstance(value, str) and bool(HANDLE_RE.match(value))


def same_handle(a: str, b: str) -> bool:
    return a.lstrip("@").lower() == b.lstrip("@").lower()


class Linter:
    def __init__(self, pr_author: str | None, base_sha: str | None) -> None:
        self.rep = Report()
        self.pr_author = pr_author or None
        self.base_sha = base_sha or None
        self.claim_ids: dict[tuple[str, str], str] = {}
        self.prompt_meta: dict[str, dict | None] = {}
        self.owners: dict[str, str] = {}
        self.changed: set[str] | None = None  # files changed in the PR, when known

    # ---------- file discovery ----------
    def markdown_files(self) -> list[Path]:
        files = []
        for path in ROOT.rglob("*.md"):
            if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
                continue
            files.append(path)
        return sorted(files)

    # ---------- shared checks ----------
    def require_str(self, path: str, data: dict, key: str, where: str = "") -> None:
        if not nonblank(data.get(key)):
            self.rep.error(path, f"{where}`{key}` is required and must be non-empty text")

    def check_ai_block(self, path: str, label: str, block: object, role: str) -> dict | None:
        where = f"{label}: "
        if not isinstance(block, dict):
            self.rep.error(path, f"{where}missing or not a mapping")
            return None
        for key in ("platform", "model", "prompt_log"):
            self.require_str(path, block, key, where)
        if block.get("result") not in AI_RESULTS:
            self.rep.error(path, f"{where}`result` must be one of {sorted(AI_RESULTS)}")
        ref = block.get("prompt_log")
        meta = self.load_prompt_meta(ref) if nonblank(ref) else None
        if nonblank(ref):
            if meta is None:
                self.rep.error(path, f"{where}prompt_log `{ref}` does not exist or has no prompt-log front matter")
            elif meta.get("role") != role:
                self.rep.error(path, f"{where}prompt_log `{ref}` must have role: {role}")
        return meta

    def load_prompt_meta(self, ref: str) -> dict | None:
        ref = ref.strip()
        if ref in self.prompt_meta:
            return self.prompt_meta[ref]
        meta = None
        target = (ROOT / ref).resolve()
        inside = ref.startswith("prompts/") and ".." not in ref.split("/")
        if inside and target.is_file():
            data, _, err = split_front_matter(target.read_text(encoding="utf-8"))
            if err is None and isinstance(data, dict) and data.get("doc_type") == "prompt-log":
                meta = data
        self.prompt_meta[ref] = meta
        return meta

    # ---------- claims ----------
    def check_claim(self, path: str, topic: str, index: int, claim: object) -> None:
        if not isinstance(claim, dict):
            self.rep.error(path, f"claims[{index}] is not a mapping")
            return
        cid = claim.get("id")
        where = f"claim {cid if nonblank(cid) else f'#{index}'}: "
        err = lambda msg: self.rep.error(path, where + msg)  # noqa: E731

        for key in claim:
            if key not in CLAIM_KEYS:
                self.rep.warn(path, where + f"unknown field `{key}` (typo?)")

        # id
        match = CLAIM_ID_RE.match(cid) if isinstance(cid, str) else None
        if not match:
            err("`id` must look like NN-n, for example 02-01")
        else:
            if match.group(1) != topic[:2]:
                err(f"`id` prefix {match.group(1)} does not match topic {topic}")
            key = (topic, cid)
            if key in self.claim_ids:
                err(f"duplicate id, already used in {self.claim_ids[key]}")
            else:
                self.claim_ids[key] = path

        if not nonblank(claim.get("claim")):
            err("`claim` is required and must be non-empty text")
        ctype = claim.get("type")
        status = claim.get("status")
        if ctype not in TYPES:
            err(f"`type` must be one of {sorted(TYPES)}")
        if status not in STATUSES:
            err(f"`status` must be one of {sorted(STATUSES)}")

        for key in ("pr", "issue"):
            if claim.get(key) is not None and not is_int(claim.get(key)):
                err(f"`{key}` must be a number or null")
        if claim.get("os_concepts") is not None and not (
            isinstance(claim["os_concepts"], list) and all(nonblank(x) for x in claim["os_concepts"])
        ):
            err("`os_concepts` must be a list of text values")

        # source and quote
        if ctype in ("fact", "org-fact"):
            source = claim.get("source")
            if not isinstance(source, dict):
                err("`source` is required for fact and org-fact")
            else:
                for key in ("title", "url", "kind", "accessed"):
                    if source.get(key) in (None, ""):
                        err(f"source.{key} is required")
                if source.get("url") and not (isinstance(source["url"], str) and URL_RE.match(source["url"])):
                    err("source.url must start with http:// or https://")
                if source.get("kind") and source["kind"] not in SOURCE_KINDS:
                    err(f"source.kind must be one of {sorted(SOURCE_KINDS)}")
                if source.get("accessed") and not is_date(source["accessed"]):
                    err("source.accessed must be a date like 2026-10-06")
                if ctype == "org-fact":
                    archive = source.get("archive")
                    if not (isinstance(archive, str) and URL_RE.match(archive)):
                        err("org-fact needs source.archive with an archive URL")
            if not nonblank(claim.get("quote")):
                err("`quote` is required for fact and org-fact")
        if ctype == "assumption" and status == "human-verified":
            err("an assumption can never be human-verified")

        # status gates
        check_ai = status in ("ai-checked", "human-verified")
        check_review = status == "human-verified"
        check_dispute = status == "disputed"
        ai_meta = None
        if check_ai:
            ai_meta = self.check_ai_block(path, where + "ai_check", claim.get("ai_check"), "author-check")
        if check_review:
            re_meta = self.check_ai_block(path, where + "ai_recheck", claim.get("ai_recheck"), "reviewer-recheck")
            self.check_review_block(path, where, claim, ai_meta, re_meta)
        if check_dispute:
            if not nonblank(claim.get("note")):
                err("`note` is required when status is disputed")
            if not is_int(claim.get("issue")):
                err("`issue` (the dispute Issue number) is required when status is disputed")

    def check_review_block(self, path: str, where: str, claim: dict, ai_meta, re_meta) -> None:
        err = lambda msg: self.rep.error(path, where + msg)  # noqa: E731
        review = claim.get("review")
        if not isinstance(review, dict):
            err("review is required when status is human-verified")
            return
        by = review.get("by")
        if not handle_ok(by):
            err('review.by must be a GitHub handle like "@handle"')
        if not is_date(review.get("date")):
            err("review.date must be a date like 2026-10-07")
        if review.get("result") != "pass":
            err("review.result must be pass for a human-verified claim")
        if review.get("opened_source") is not True:
            err("review.opened_source must be true")
        if handle_ok(by):
            # Only files changed in this PR: older claims keep the reviewer they had.
            if self.pr_author and self.changed is not None and path in self.changed \
                    and same_handle(by, self.pr_author):
                err(f"review.by {by} is the PR author; a different person must review")
            if re_meta is not None and isinstance(re_meta.get("author"), str) and not same_handle(by, re_meta["author"]):
                err("the ai_recheck prompt log author must be the reviewer (review.by)")
        check = claim.get("ai_check")
        recheck = claim.get("ai_recheck")
        if isinstance(check, dict) and isinstance(recheck, dict):
            if check.get("prompt_log") and check.get("prompt_log") == recheck.get("prompt_log"):
                err("ai_recheck must use a different prompt log than ai_check (separate session)")

    # ---------- document types ----------
    def check_topic_index(self, path: str, topic: str, data: dict) -> None:
        if data.get("doc_type") != "topic-index":
            self.rep.error(path, "doc_type must be topic-index")
        if data.get("topic") != topic:
            self.rep.error(path, f"`topic` must equal the directory name {topic}")
        self.require_str(path, data, "title")
        self.require_str(path, data, "assignment_section")
        sections = data.get("report_sections")
        if not (isinstance(sections, list) and sections and all(is_int(x) for x in sections)):
            self.rep.error(path, "`report_sections` must be a non-empty list of numbers")
        owner = data.get("owner")
        if not handle_ok(owner):
            self.rep.error(path, '`owner` must be a GitHub handle like "@handle" (use "@TBD" until assigned)')
        else:
            self.owners[topic] = owner
        if data.get("issue") is not None and not is_int(data.get("issue")):
            self.rep.error(path, "`issue` must be a number or null")
        if not is_date(data.get("updated")):
            self.rep.error(path, "`updated` must be a date like 2026-10-05")

    def check_topic_note(self, path: str, topic: str, data: dict) -> None:
        if data.get("doc_type") != "topic-note":
            self.rep.error(path, "doc_type must be topic-note")
        if data.get("topic") != topic:
            self.rep.error(path, f"`topic` must equal the directory name {topic}")
        self.require_str(path, data, "title")
        if not is_date(data.get("updated")):
            self.rep.error(path, "`updated` must be a date like 2026-10-05")
        claims = data.get("claims")
        if not isinstance(claims, list):
            self.rep.error(path, "`claims` must be a list (it may be empty)")
            return
        for i, claim in enumerate(claims):
            self.check_claim(path, topic, i, claim)

    def check_prompt_log(self, path: str, stem: str, data: dict, body: str, full_text: str) -> None:
        if data.get("doc_type") != "prompt-log":
            self.rep.error(path, "doc_type must be prompt-log")
        if data.get("id") != stem:
            self.rep.error(path, f"`id` must equal the file name without .md ({stem})")
        if not handle_ok(data.get("author")):
            self.rep.error(path, '`author` must be a GitHub handle like "@handle"')
        if not is_date(data.get("date")):
            self.rep.error(path, "`date` must be a date like 2026-10-06")
        for key in ("platform", "model", "purpose"):
            self.require_str(path, data, key)
        if data.get("phase") not in PHASES:
            self.rep.error(path, f"`phase` must be one of {sorted(PHASES)}")
        if data.get("role") not in ROLES:
            self.rep.error(path, f"`role` must be one of {sorted(ROLES)}")
        significant = data.get("significant")
        if not isinstance(significant, bool):
            self.rep.error(path, "`significant` must be true or false")
        elif significant and not nonblank(data.get("significant_reason")):
            self.rep.error(path, "`significant_reason` is required when significant is true")
        if data.get("pr") is not None and not is_int(data.get("pr")):
            self.rep.error(path, "`pr` must be a number or null")
        claims = data.get("claims")
        if not (isinstance(claims, list) and all(isinstance(c, str) and CLAIM_ID_RE.match(c) for c in claims)):
            self.rep.error(path, "`claims` must be a list of claim ids like 02-01 (it may be empty)")
        docs = data.get("supporting_docs")
        if not (isinstance(docs, list) and all(nonblank(d) for d in docs)):
            self.rep.error(path, "`supporting_docs` must be a list (it may be empty)")
        redactions = data.get("redactions")
        found = len(REDACT_RE.findall(full_text))
        if not is_int(redactions) or redactions < 0:
            self.rep.error(path, "`redactions` must be a number, 0 or more")
        elif redactions != found:
            self.rep.error(path, f"`redactions` is {redactions} but the file has {found} [REDACTED:...] markers")
        if not TURN_RE.search(body):
            self.rep.error(path, "body needs at least one '## Turn N — user' heading")
        if not LEDGER_RE.search(body):
            self.rep.error(path, "body needs a '## Tool-call ledger' heading (write 'None.' if there were no tool calls)")

    def check_spec(self, path: str, data: dict) -> None:
        if data.get("doc_type") != "spec":
            self.rep.error(path, "doc_type must be spec")

    # ---------- per-file dispatch ----------
    def lint_structured(self, files: list[Path]) -> None:
        kb_root = ROOT / KB
        if kb_root.is_dir():
            for entry in sorted(kb_root.iterdir()):
                if entry.is_dir() and not TOPIC_DIR_RE.match(entry.name):
                    self.rep.error(rel(entry), "topic directory must be named NN-slug in lowercase kebab-case")
                if entry.is_dir() and not (entry / "index.md").is_file():
                    self.rep.error(rel(entry), "topic directory needs an index.md")
        for file in files:
            parts = file.relative_to(ROOT).parts
            path = rel(file)
            top = parts[0]
            in_scope = top in (KB, "prompts") or parts == ("docs", "schema.md")
            if not in_scope:
                continue
            text = file.read_text(encoding="utf-8")
            data, body, err = split_front_matter(text)
            if err:
                self.rep.error(path, err)
                continue
            if data is None:
                self.rep.error(path, "front matter is required (a block starting and ending with ---)")
                continue
            if top == KB:
                if len(parts) < 3:
                    self.rep.error(path, "files in knowledge-base/ must live inside a topic directory")
                    continue
                topic = parts[1]
                if not TOPIC_DIR_RE.match(topic):
                    continue
                if parts[2:] == ("index.md",):
                    self.check_topic_index(path, topic, data)
                else:
                    self.check_topic_note(path, topic, data)
            elif top == "prompts":
                self.check_prompt_log(path, file.stem, data, body, text)
            else:
                self.check_spec(path, data)

    # ---------- leak scan ----------
    def leak_scan(self, files: list[Path]) -> None:
        for file in files:
            path = rel(file)
            for lineno, line in enumerate(file.read_text(encoding="utf-8").splitlines(), 1):
                if "lint-allow" in line:
                    continue
                for kind, pattern in LEAK_PATTERNS:
                    if pattern.search(line):
                        self.rep.error(path, f"line {lineno}: possible {kind}; redact it or add lint-allow if it is a false positive")
                for match in EMAIL_RE.finditer(line):
                    if match.group(1).lower() not in EMAIL_OK_DOMAINS:
                        self.rep.error(path, f"line {lineno}: possible email address; redact it as [REDACTED:email]")

    # ---------- PR-scoped checks ----------
    def load_changed_files(self) -> None:
        """Fill self.changed with the files changed in the PR (needs PR_AUTHOR and BASE_SHA)."""
        if not (self.pr_author and self.base_sha):
            self.rep.notice("PR_AUTHOR or BASE_SHA not set: skipped the review.by and topic-owner checks (CI runs them).")
            return
        try:
            out = subprocess.run(
                ["git", "diff", "--name-only", self.base_sha, "HEAD"],
                cwd=ROOT, capture_output=True, text=True, check=True,
            ).stdout
        except (OSError, subprocess.CalledProcessError) as exc:
            self.rep.notice(f"could not list changed files, skipped the review.by and topic-owner checks ({exc}).")
            return
        self.changed = {line.strip() for line in out.splitlines() if line.strip()}

    def owner_warnings(self) -> None:
        if self.changed is None:
            return
        topics = set()
        for line in self.changed:
            parts = Path(line).parts
            if len(parts) >= 3 and parts[0] == KB and TOPIC_DIR_RE.match(parts[1]):
                topics.add(parts[1])
        for topic in sorted(topics):
            owner = self.owners.get(topic)
            if owner and owner != "@TBD" and not same_handle(owner, self.pr_author):
                self.rep.warn(f"{KB}/{topic}", f"PR author @{self.pr_author} is not the topic owner {owner}")

    def run(self) -> int:
        files = self.markdown_files()
        self.load_changed_files()
        self.lint_structured(files)
        self.leak_scan(files)
        self.owner_warnings()
        for line in self.rep.notices + self.rep.warnings + self.rep.errors:
            print(line)
        status = "FAILED" if self.rep.errors else "passed"
        print(f"lint {status}: {len(files)} markdown files, "
              f"{len(self.rep.errors)} errors, {len(self.rep.warnings)} warnings")
        return 1 if self.rep.errors else 0


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--pr-author", default=os.environ.get("PR_AUTHOR"))
    parser.add_argument("--base", default=os.environ.get("BASE_SHA"))
    args = parser.parse_args()
    return Linter(args.pr_author, args.base).run()


if __name__ == "__main__":
    sys.exit(main())
