---
name: issue-status
description: Show the status of a topic Issue in this repo. Covers Issue state, milestone, linked PRs, claim counts by status and what is left to do. Read-only. Use when asked for "issue status", "where are we on topic NN" or "what is left for issue N".
---

# issue-status

Read-only. Do not edit an Issue or PR here. Use `issue-update` for that.

Input: a topic Issue number `<n>` and its directory `<NN-slug>`. Find them with `gh issue list --label topic`.

## Steps

1. Issue: `gh issue view <n> --json number,title,state,assignees,milestone,body`. Read the "done when" checklist in the body.
2. PRs: `gh pr list --state all --search "Closes #<n>" --json number,title,state,headRefName,reviewDecision`.
3. Claims on this branch: `python3 scripts/status.py <NN-slug>` (counts by status and type, claims past `unverified` with no `ai_check`, notes missing a summary, and the "not found yet" list). `python3 scripts/status.py` alone shows every topic.
4. Branch: `git branch --show-current`, `git status --short` and `git log --oneline origin/main..HEAD`.

## Report

At most 12 lines:

- Issue state, owner, milestone due date.
- Each "done when" item as done or not done, with the evidence (a file, a commit or a PR).
- Claim counts by status.
- PR state and review decision, or "no PR".
- The single next step.

Say so when a number comes from this branch and not from `main`.
