# OS job research: Site Reliability Engineer

Secondary-research knowledge base for the course 204341 final assignment (GenAI-assisted career and Operating Systems exploration for COOP/job training). Teammates research the target position, and every claim is fact-checked twice, by AI and by a human reviewer, before the report uses it.

- Position: Site Reliability Engineer
- Company: Google
- Assignment rules: [`docs/assignment.md`](docs/assignment.md)
- Field and workflow spec: [`docs/schema.md`](docs/schema.md)
- Git and `gh` commands for owners and reviewers: [`docs/workflow.md`](docs/workflow.md)
- Rules for AI agents: [`AGENTS.md`](AGENTS.md)

## Layout

```
AGENTS.md                      rules for any AI agent
docs/assignment.md             assignment text (the PDF next to it wins if they differ)
docs/FinalAssignment_*.pdf     the instructor's assignment PDF
docs/schema.md                 front matter fields, status gates, prompt-log rules
docs/workflow.md               git and gh commands
knowledge-base/NN-slug/        13 topic directories, one owner each
  index.md                     topic metadata and scope
  *.md                         notes with claims in the front matter
prompts/                       exact GenAI conversations (prompt logs)
scripts/                       lint, appendix budget, hook setup
.github/                       PR template, Issue templates, CI
```

## Knowledge base

`knowledge-base/` is where the research lives. It has 13 topic directories that follow the assignment's sections. Each directory has one owner, named in its `index.md`. The owner creates and organizes the notes inside it and is the only person who opens PRs for it.

| Directory | Assignment section | Report sections |
|---|---|---|
| `01-position-and-job-description` | 4.1 | 3 |
| `02-hard-skills` | 4.2 | 4 |
| `03-soft-skills` | 4.6 | 4 |
| `04-operating-systems` | 4.3 | 6 |
| `05-hardware-requirements` | 4.3 | 7 |
| `06-system-architecture-infrastructure` | 4.3 | 8 |
| `07-dev-and-runtime-tools` | 4.4 | 9 |
| `08-devops-iac-cicd-tools` | 4.4 | 9 |
| `09-monitoring-and-incident-tools` | 4.4 | 9 |
| `10-server-and-database-software` | 4.4 | 9 |
| `11-os-course-concepts` | 4.5 | 10 |
| `12-organization-and-working-environment` | 4.7 | 5 |
| `13-preparation-plan` | 10 (outcome 8) | 12 |

Each directory contains:

- `index.md`: the topic's scope, owner and Issue number.
- Notes (`*.md`): Markdown files whose front matter lists **claims**. A claim has a source, an exact quote, an access date, a `type` (`fact`, `org-fact` or `assumption`) and a `status` (`unverified`, `ai-checked`, `human-verified` or `disputed`). The body is optional prose.

The target company is Google, covered in topic 12. A claim about Google is an `org-fact` and needs published evidence and an archive link; anything about Google's internal environment that no published source states is labeled `assumption`. Every field is defined in [`docs/schema.md`](docs/schema.md).

## Using AI agents here

Every agent should follow [`AGENTS.md`](AGENTS.md). Codex CLI and Antigravity read it directly. Claude Code reads it directly from v2.1.277 on, but only when there is no `CLAUDE.md` or `CLAUDE.local.md` in the working directory or any directory above it. If you have one (for example in your home directory), Claude Code reads that file and skips `AGENTS.md`. Fix it in a Claude Code session: type `/config` and set **Project instructions** to `claude-md-and-agents-md`. Your `~/.claude/CLAUDE.md` does not count and needs no change. Do not add a `CLAUDE.md` to this repo.

## How a claim gets verified

1. The topic owner writes a claim with a source, an exact quote and an access date. Status: `unverified`.
2. A blind subagent re-checks every claim against its source. It sees only the claim text and the source URL, not the quote. The owner records the result in `ai_check`, with the check logged in `prompts/` as `role: author-check`. Status: `ai-checked`. The owner opens a PR with a detailed session summary.
3. A reviewer opens every cited source, runs an AI recheck in a separate session that sees only the claim and the source URL, and records `ai_recheck` and `review` in a verification commit on the PR branch. Passing claims become `human-verified`. The reviewer approves.
4. Someone other than the author merges. Claims that cannot be verified stay `unverified`, or become `assumption`.
5. A merged claim later found wrong is handled with a `dispute` Issue.

The step-by-step git and `gh` commands for each role are in [`docs/workflow.md`](docs/workflow.md).

## Each member: one-time setup

```
sh scripts/setup.sh
python3 -m pip install -r requirements.txt   # if setup.sh says PyYAML is missing
```

This turns on the pre-push hook, which runs the same lint as CI. Run it by hand any time:

```
python3 scripts/lint_front_matter.py
python3 scripts/appendix_budget.py
```

Keep your own scratch files, exports and notes in `.local/`. It is git-ignored and the lint skips it, so nothing there goes upstream.

## Maintainer reference: repo settings

These are configured on GitHub for `ilma-org/os-coop-job-research`. Apply them again if the repo is recreated.

- Public repository in a free GitHub Organization. Default branch `main`.
- Squash-merge only, and delete branches after merge.
- Protection on `main`: pull request required, 1 approval, "Require review from Code Owners" on, the `lint` status check required, applied to admins too. Do **not** turn on "Require approval of the most recent reviewable push", or the reviewer's own verification commit blocks their approval. "Dismiss stale approvals" is optional; if it is on, the reviewer must approve after pushing the verification commit.
- Reviewers: the 3 code owners listed in `.github/CODEOWNERS`. Because code-owner review is required, only their approvals count. Members who are not reviewers can open PRs but cannot approve them.
- Push and merge to `main` restricted by username to the same 3 reviewers (`restrictions.users` in the branch-protection settings; no team is used).
- To add or remove a reviewer: give them Write access first (a code owner without write access is ignored), then change `.github/CODEOWNERS` in a PR, then update the push restriction to match. Another reviewer approves and merges that PR.
- Labels: `topic`, `dispute`, `needs-review`.
- One `topic` Issue per topic directory, with the Issue number set in each `index.md` (`issue: null` and `owner: "@TBD"` until assigned).
- Branch-protection options depend on the GitHub plan. If one is unavailable, the rule becomes an honor rule.

## Before submission

- Run `python3 scripts/appendix_budget.py` to see how many pages the significant prompt logs use.
- Tag the submitted commit, for example `git tag submitted-2026-10-18`, and cite the tag URL in the report References with the access date. A moving `main` is a weak citation.
- The instructor accepts non-significant prompt logs through the repo URL, so the repo must stay public and unchanged until grading is done.
- The cover page (student IDs, full names, phone numbers) is built locally and is never committed. `.gitignore` covers the usual names.

## Still undecided

- The report toolchain (LaTeX or docx). Keep notes in Markdown so Pandoc can produce either. The assignment requires 12-point Times New Roman on A4.
- Any internal deadline for the knowledge base.
