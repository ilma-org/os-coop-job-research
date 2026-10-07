# Git and GitHub workflow with `gh`

This guide uses the GitHub CLI (`gh`) so nobody has to remember the git and pull request steps. An AI agent can run these commands for you. The rules for what goes into a PR are in `AGENTS.md` and `docs/schema.md`.

## One-time setup

1. Install git, Python 3 and the GitHub CLI (https://cli.github.com).
2. Log in: `gh auth login` (choose GitHub.com and follow the browser prompts).
3. Clone the repo: `gh repo clone ilma-org/os-coop-job-research`, then `cd os-coop-job-research`.
4. Turn on the pre-push lint: `sh scripts/setup.sh`.

## Topic owner: do new work

```
gh issue list --label topic              # find your topic Issue
git switch main && git pull              # start from the latest main
git switch -c 02-hard-skills/networking  # branch: <NN-slug>/<short-description>
# ... add claims (scripts/add_claim.py), run the blind AI check (agent-fact-check skill),
# ... build the prompt log (scripts/make_prompt_log.py), refresh the index (scripts/update_index.py) ...
python3 scripts/lint_front_matter.py     # must pass
git add knowledge-base/02-hard-skills/networking.md
git commit -m "Add networking claims to 02-hard-skills"
git add prompts/2026-10-06-member1-networking.md
git commit -m "Add prompt log for networking research"
git push -u origin HEAD                  # the pre-push hook runs the lint
```

Open the PR. Copy `.github/pull_request_template.md` to a temporary file outside the repo, fill in the session summary, then:

```
python3 scripts/pr_leak_scan.py --body-file /tmp/pr-body.md   # added lines, commits and PR text; must pass
gh pr create --title "[02-hard-skills] add networking claims" --body-file /tmp/pr-body.md
```

`gh pr create --web` opens the PR form in the browser with the template instead. The body must say `Closes #<issue>`.

Or let the scripts do it: `python3 scripts/ship.py prepare` runs the lint and the leak scan and drafts the body in `.local/pr-body.md`. Fill the `<agent: ...>` placeholders, then run `python3 scripts/ship.py open --title-text "add networking claims"` for a dry run, and add `--yes` to push and open the PR.

Useful follow-ups:

```
gh pr checks <number>        # CI status
gh pr view <number> --web    # open in the browser
gh pr status                 # your open PRs and review requests
```

## Reviewer: verify a PR

```
gh pr list                       # PRs waiting for review
gh pr checkout <number>          # switch to the PR branch
gh pr diff <number>              # read the changes
python3 scripts/pr_leak_scan.py --pr <number>   # leak scan: added lines, commits, PR title and body
# open every cited source, run the blind AI recheck in a separate session,
# fill ai_recheck, review and status in the notes
python3 scripts/lint_front_matter.py
git add <paths>
git commit -m "Verify networking claims in 02-hard-skills"
git push
gh pr review <number> --approve --body "Sources opened, quotes match."
gh pr merge <number> --squash --delete-branch   # never your own PR
```

To ask for changes instead: `gh pr review <number> --request-changes --body "..."`.

## Change the repo system (rules, scripts, skills, CI, templates)

Work that adds no claim is not a topic PR. Use a `chore/<short-description>` or `meta/<short-description>` branch from `origin/main` and the title `[meta] what changed`.

```
git fetch && git switch -c chore/short-description origin/main
# ... edit, then commit atomically ...
python3 scripts/lint_front_matter.py
python3 scripts/pr_leak_scan.py --body-file /tmp/pr-body.md
gh pr create --title "[meta] what changed" --body-file /tmp/pr-body.md
```

Fill `/tmp/pr-body.md` from `.github/PULL_REQUEST_TEMPLATE/repo-system.md`. On the web, add `?template=repo-system.md` to the new-PR URL. The same approval rule applies: one code owner who is not the author.

## Scripts that write the repetitive parts

Run these instead of typing the output by hand. Each has `--help`.

| Script | What it does |
|---|---|
| `scripts/add_claim.py` | Adds one claim to a note. Checks the quote against the page and finds an archive snapshot by code, takes the next free ID, writes the YAML block. |
| `scripts/update_index.py` | Rewrites the notes list in a topic's `index.md` from the notes' front matter. |
| `scripts/make_prompt_log.py` | Builds `prompts/<id>.md` from a saved session: verbatim turns, redaction, ledger, front matter. |
| `scripts/status.py` | Claim counts per topic, claims missing `ai_check`, notes missing a summary. |
| `scripts/make_pr_body.py` | Drafts the PR body from the repo. Leaves `<agent: ...>` placeholders for judgment. |
| `scripts/ship.py` | `prepare` runs the checks and drafts the body. `open` pushes and opens the PR, only with `--yes`. |
| `scripts/verify_quote.py` | Checks one quote against one URL. |
| `scripts/lint_front_matter.py`, `scripts/pr_leak_scan.py` | The checks. |

The blind AI check has its own helper in `.agents/skills/agent-fact-check/scripts/`.

## Report a wrong claim

```
gh issue create --web            # choose the Dispute template
```

## Rules to remember

- `main` is protected. Push to a branch and open a PR, never push to `main`.
- Commit in small, separate steps. See "Commits" in `AGENTS.md`.
- A PR needs one approval from a reviewer (a code owner in `.github/CODEOWNERS`) who is not its author. Approvals from other members do not count.
- If `git push` is rejected, run `git pull --rebase` and push again. Do not force-push a branch that others use.
- If the pre-push lint fails, read the errors, fix them, commit the fix, and push again. Do not skip the hook.
