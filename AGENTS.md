# AGENTS.md

Rules for any AI agent (Claude Code, Codex CLI, Antigravity, or another) working in this repo. Humans follow them too.

## Project

A secondary-research knowledge base for the course 204341 final assignment: GenAI-assisted career and Operating Systems exploration for COOP/job training.

- Target position: **Site Reliability Engineer (SRE)**.
- Target company: **Google**. Topic 12 covers Google; other topics stay about SRE in general unless a claim is about Google.
- Report deadline: Sunday 18 October 2026, 23:59 (CMU Mango). The report is 10–15 pages excluding the cover page, 12-point Times New Roman, A4. The prompts appendix counts toward the page cap.
- The report toolchain (LaTeX or docx) and the final report are not decided. This repo holds verified claims, not the report.

## Read first

1. `docs/assignment.md`: the assignment rules. If it and the PDF disagree, the PDF wins.
2. `docs/schema.md`: every front matter field, status gate and prompt-log rule.
3. The `index.md` of the topic directory you are working in.

## Hard rules

1. **No claim without a real source and an exact quote.** Every `fact` and `org-fact` needs a source you actually opened in this session, an access date, and a sentence copied verbatim from it. Never invent a URL, title, quote or date. If you cannot open the source, set `status: unverified` and say so.
2. **Secondary research only.** Use published sources: official docs, job ads, papers, articles. No interviews or surveys.
3. **Never claim what a company uses without evidence.** A claim about Google is an `org-fact` and needs real evidence from a published source (Google job ads, Google's SRE books, official Google pages) and an archive link. Anything about Google's internal environment that no published source states is `type: assumption`.
4. **Label assumptions and recommendations as `type: assumption`.** Never write them in the voice of a verified fact.
5. **Agents never set `status: human-verified` and never write the `review` block.** Only a human reviewer does. Agents may set `unverified` and `ai-checked`.
6. **Agents never merge or approve PRs and never push to `main`.**
7. **Compare sources where you can.** Prefer official documentation. Say when only one source exists.
8. **Write in English.** Readers who want Thai translate for themselves.
9. **Keep quotes brief.** One or two sentences per claim, not bulk copying.
10. **This repo is public.** Never write cover-page data (student ID, full name, phone number), emails, absolute home-directory paths, tokens or passwords into any file. Refer to people by GitHub handle only.
11. **Do not send confidential or private data to public GenAI services.**

## Roles

- **Researcher**: finds sources, writes claims as `unverified` in the topic owner's directory.
- **Author check**: after the researcher has written the claims and before the PR is opened, a blind check runs on every claim. The checker is a fresh subagent (or a fresh agent context if the platform has no subagents). Give it only the claim text, the source URL and the archive URL. Do not give it the stored `quote`, the research session or any earlier AI output. Its prompts and reports go in their own prompt log with `role: author-check`, which `ai_check.prompt_log` points to. The most a claim can reach here is `ai-checked`. The `agent-fact-check` skill runs these steps.
- **Reviewer recheck**: the reviewer's agent runs in a separate session that has none of the author's context. Give it only the claim text and the source URL. Do not give it the author's AI output or prompts. It fills `ai_recheck`. The human reviewer decides any disagreement.
- **Session summary**: when a PR opens, the agent writes a detailed, redacted summary of the session into the PR description using the PR template.
- **Drafter**: later, an agent may draft report text from the knowledge base. Use only claims that are `human-verified`, or `assumption` claims worded as recommendations. A human edits and verifies every draft. Pasting unverified AI text does not satisfy the assignment.

## Prompt logs

- Save every significant GenAI interaction as `prompts/<id>.md`, following `docs/schema.md`: exact conversation, redacted only at sensitive spans, with the tool-call ledger.
- Redact with `[REDACTED:kind]`. Never reword. Set `redactions` to the number of markers.
- Set `significant` by the instructor's rule: grammar or wording fixes and "where is this phrase in the source" lookups are not significant. Non-significant logs stay in `prompts/` and are provided through the repo URL. Significant logs go in the report appendix, so add a `significant_reason`.
- Keep one purpose per session and keep prompts focused. Shorter logs fit the page budget.
- Record the real platform and model name and version. Do not guess a version.

## Commits

- **Commit atomically.** One logical change per commit. If a change can be split, split it.
- Stage by path or by hunk (`git add <path>`, `git add -p`). Do not `git add -A` blindly.
- Keep these in separate commits: claims for different notes, a new note versus edits to an existing one, prompt logs versus the claims they support, tooling or lint changes versus knowledge-base content, and the reviewer's verification commit versus everything else.
- Subject line: imperative, 72 characters or fewer, says what changed (for example `Add networking claims to 02-hard-skills`). Add a body only to explain why.
- Run `python3 scripts/lint_front_matter.py` before committing content.
- Commit and push only when the person you work for asks. Never commit to `main`. Do not rewrite pushed commits or force-push a shared branch.

## Local files

`.local/` is git-ignored and skipped by the lint. Put scratch files, exports, to-do lists and personal notes there, anything that must not go upstream. Never link to it from a tracked file, and never copy its content into one without checking it against the leak rules above.

## Repo skills

Repo-only skills live in `.agents/skills/<name>/SKILL.md`. Codex CLI loads that folder by itself. For any other agent, open the file and follow it. The skills use plain shell commands and name no agent-specific tool.

- `research`: research claims for a topic note, from source to `unverified` claim.
- `agent-fact-check`: run the blind author check and record `ai_check`.
- `pr-check`: check a branch before its PR opens, or check a PR as reviewer.
- `issue-status`: read-only status of a topic Issue and its claims.
- `issue-update`: post a progress comment or tick the Issue checklist, after confirmation.

## Git and GitHub

Use `gh` for PRs and Issues. The exact commands for owners and reviewers are in `docs/workflow.md`. Use them instead of inventing your own steps.

## Workflow

1. The topic owner works from the topic Issue. Only the owner opens PRs for a topic directory.
2. Create a branch named `<NN>-<slug>/<short-description>`. PR title: `[<NN>-<slug>] what changed`. The PR body says `Closes #<issue>`.
3. Run `python scripts/lint_front_matter.py` before pushing and before opening a PR. Fix every error. Never bypass the pre-push hook.
4. The reviewer opens each cited source, runs the blind AI recheck, then pushes a **verification commit** to the PR branch that fills `ai_recheck` and `review` and sets `human-verified` for passing claims. The reviewer approves after that commit.
5. A PR is merged only after one approval from a reviewer (a code owner in `.github/CODEOWNERS`) who is not the author. Squash-merge. For a PR written by a reviewer, another reviewer merges it.
6. If a merged claim is found wrong, open a `dispute` Issue. See "Disputed claims" in `docs/schema.md`.
7. A change to the repo system (rules, docs, scripts, skills, CI, templates) adds no claims. Use a `chore/<short-description>` branch, the title `[meta] what changed` and `.github/PULL_REQUEST_TEMPLATE/repo-system.md`.
8. Run `python3 scripts/pr_leak_scan.py --body-file <PR body file>` before every PR. It scans what the lint does not: added lines in every file type, commit messages and the PR text.
9. Do not hand-write what a script generates: claims (`scripts/add_claim.py`), prompt logs (`scripts/make_prompt_log.py`), the index notes list (`scripts/update_index.py`), the PR body (`scripts/make_pr_body.py`) and the PR itself (`scripts/ship.py`, which pushes only with `--yes`). `scripts/status.py` shows progress. See `docs/workflow.md`.
