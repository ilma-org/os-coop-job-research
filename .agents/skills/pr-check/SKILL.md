---
name: pr-check
description: Check a branch before its PR opens (author mode) or check an open PR (reviewer mode) in this repo. Runs the lint and leak scan, checks claim gates, prompt logs, commits and the PR text. Use when asked to "check the PR", "pr-check" or "is this ready to open".
---

# pr-check

Read-only. It reports problems and does not fix, push, approve or merge. Rules are in `AGENTS.md` and `docs/schema.md`. Commands are in `docs/workflow.md`.

## Author mode (before the PR opens)

1. `python3 scripts/lint_front_matter.py` has 0 errors. This includes the leak scan, prompt-log fields and `redactions` counts.
2. Branch is `<NN>-<slug>/<short-description>`, or `chore/...` or `meta/...` for repo-system changes. The PR title is `[<NN>-<slug>] ...` or `[meta] ...`. The body has `Closes #<n>`.
3. No agent-only status gate is crossed. This must print nothing:
   `git diff origin/main...HEAD -U0 -- knowledge-base | grep -E '^\+ +(status: human-verified|review:|ai_recheck:)'`
4. Every claim is `ai-checked`, or is `unverified` or `assumption` and listed under "Open items" with a reason.
5. Every `ai_check.prompt_log` exists, has `role: author-check`, and is a different file from the research log.
6. Each topic note body has `## Summary` and `## Key points`.
7. `git log --oneline origin/main..HEAD`: one logical change per commit, imperative subject of 72 characters or fewer, and the separations in `AGENTS.md` (Commits) hold.
8. The PR body uses `.github/pull_request_template.md`, with a redacted session summary and no raw transcript.

## Reviewer mode (an open PR)

1. `gh pr checkout <n>`, then run the lint with the PR context:
   `PR_AUTHOR=<author login> BASE_SHA=$(git merge-base origin/main HEAD) python3 scripts/lint_front_matter.py`
2. Walk the "Reviewer section" of the PR template. List which boxes are done and which are not.
3. Remind the human of what only they do: open every cited source, run the blind recheck in a separate session that sees only the claim and the URL, then push the verification commit with `ai_recheck`, `review` and `human-verified`.
4. Never set `human-verified`, write `review`, approve or merge.

## Report

Pass or fail per numbered item, with the file or command output behind each fail.
