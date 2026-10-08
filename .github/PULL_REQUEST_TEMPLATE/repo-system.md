## What this PR changes

Area (keep the ones that apply): rules (`AGENTS.md`, `docs/`) · lint or scripts · skills (`.agents/skills/`) · CI or GitHub templates · other

Closes #<issue> (delete this line if there is no Issue)

This PR changes how the repo works. It adds, edits or verifies no claim. Claims go in a topic PR.

## Why

What problem this solves, and who runs into it.

## Author checklist

- [ ] One purpose per PR. Commits are atomic, and tooling or lint changes are separate from rules and docs (`AGENTS.md`, Commits).
- [ ] `python3 scripts/lint_front_matter.py` passes.
- [ ] `python3 scripts/pr_leak_scan.py --body-file <this body saved to a file outside the repo>` passes. It scans every added line, the commit messages and this text.
- [ ] I ran every changed script or skill on a copy of real notes and prompt logs, and pasted the result under "How I tested it".
- [ ] Existing merged notes and prompt logs still pass, or this PR says what breaks and who must fix it.
- [ ] No cover-page data, real names, emails, home-directory paths, tokens or agent scratch paths anywhere, including commit messages and this text.
- [ ] A change that alters how topic owners or reviewers work is announced to them, in the Issue or in the team chat.

## How I tested it

Commands and results. Cut long output to the decisive lines.

## Impact and rollback

Who is affected, and what they must do. How to undo it, for example `git revert <commit>`.

## Session summary

Written by my agent from my session. Redacted. No raw transcript.

- Platform and model:
- Goal:
- Prompt log: id, or "none" with the reason (the work produced no report content)
- Decisions, and AI errors I corrected:
- Searches and commands run:

---

## Reviewer section

Filled by the reviewer. Do not review or merge your own PR.

- [ ] I read the whole diff, including scripts, skills and workflow files. They run on members' machines or in CI.
- [ ] I ran the changed tool or skill myself, or I explain below why I could not.
- [ ] I ran `python3 scripts/pr_leak_scan.py --pr <number>` and scanned the diff for sensitive information.
- [ ] The change matches `AGENTS.md` and `docs/schema.md`, or this PR updates them.
- [ ] A code owner who is not the author approved. Squash-merge by someone other than the author. If the author is a reviewer, another reviewer merges.

Reviewer notes:
