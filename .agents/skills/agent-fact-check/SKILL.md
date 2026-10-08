---
name: agent-fact-check
description: Run the blind AI author check on claims in a topic note. A fresh agent sees only the claim text and the source URL, never the stored quote. Records ai_check and the author-check prompt log. Use after researching claims and before opening a PR, or when asked to "ai-check" or "fact-check" claims.
---

# agent-fact-check

Runs the **Author check** from `AGENTS.md` (Roles). It needs a shell, Python 3 with PyYAML, and a way to start a fresh agent context (a subagent, or a new session).

Rules: the checker never sees the stored `quote`, the research session or any earlier AI output. Never set `human-verified` or write `ai_recheck` or `review`. Commit only when the person asks.

## Steps

1. Run `python3 scripts/lint_front_matter.py`. Fix errors first.
2. Make a work directory outside the repo: `WORK=$(mktemp -d)`. The script refuses a directory inside the repo.
3. Prepare the blind inputs, one file per note:
   `python3 .agents/skills/agent-fact-check/scripts/blind_check.py prepare <note.md>... --out "$WORK"`
   It covers every `unverified` fact and org-fact. Add `--ids 07-01,07-02` to pick claims. It writes claim text, source URL and archive URL, never the quote, and prints the exact prompt for the checker.
4. Start one fresh checker per note, in parallel. Use a subagent if the platform has them. Otherwise start a new session whose working directory is `$WORK`, not the repo. Give each checker the printed prompt and nothing else. It writes `report_<note>.md` in `$WORK`.
5. Wait for every report. Do not edit a report. Do not read the notes to help the checker.
6. Judge the reports without writing anything:
   `python3 .agents/skills/agent-fact-check/scripts/blind_check.py finish <note.md>... --out "$WORK" --log-id <log-id> --author @<handle> --platform "<platform>" --dry-run`
   A claim passes when the verdict is `supported`, the checker's quote equals or contains the stored quote, and, for an org-fact, the archive link loads with the quote present.
7. Run the same command without `--dry-run`. Add `--model "<name and version>"` when the reports name the model differently. It then:
   - writes `prompts/<log-id>.md` with `role: author-check` and `significant: false`, temp paths redacted;
   - sets `status: ai-checked` and fills `ai_check` on the claims that passed;
   - leaves failed claims `unverified`.
   Use a log id like `2026-10-08-<handle>-<topic>-author-check`.
8. For each failed claim, read its `ISSUES` line in the report. Fix the claim wording or the source, then check again with `--ids` and a new log id (add `-2`).
9. Run `python3 scripts/lint_front_matter.py` again.
10. Report how many claims passed, which failed and why, and which log file was written.

## Limits

- The checker's own tool calls are not visible to you. The ledger in the log says so. Do not invent calls.
- This is the author check only. The reviewer's blind recheck is a separate step by a different person, logged with `role: reviewer-recheck`.
- Keep note edits and the prompt log in separate commits (`AGENTS.md`, Commits).
