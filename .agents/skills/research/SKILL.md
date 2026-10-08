---
name: research
description: Research claims for a topic note in this repo. Find published sources, add claims with scripts/add_claim.py (it checks the quote and archive link by code), write the summary, update the index and save the prompt log. Use when asked to research a topic or Issue, add claims, or "start research on <topic>".
---

# research

Follows `AGENTS.md` and `docs/schema.md`. Read both first, then the topic's `index.md` (scope, owner, Issue, gaps). Do not hand-write what a script generates.

## Steps

1. Check you are the topic owner and on a topic branch `<NN>-<slug>/<short-description>`, created from `origin/main`. Never work on `main`.
2. Choose sources. Prefer official docs and books, then job ads, papers and articles. Secondary research only. A claim about Google needs a Google-published source (SRE books, Google careers pages, official Google pages).
3. Open each source yourself. Pick one or two sentences per claim. Write the claim no broader than the quote. If the passage is an example or an anecdote, say so in the claim text.
4. Add each claim with the script. It takes the next free ID, refuses the claim unless the quote is in the page word for word, finds an archive snapshot that contains the quote for an org-fact, and writes the block with today's access date, `status: unverified` and `pr: null`:
   `python3 scripts/add_claim.py knowledge-base/<NN-slug>/<note>.md --claim "..." --url <url> --quote "..." --title "<source title>" [--type org-fact] [--os-concepts "a,b"] [--new-note "Note title"]`
   For something no source states, use `--type assumption` with only `--claim`. If the script refuses, fix the quote or pick another source. Never edit the YAML by hand to get around it. To test a quote alone: `python3 scripts/verify_quote.py <url> "<quote>"`.
5. In the note body, replace the `_TODO_` lines under `## Summary` and `## Key points`. Write them only from the claims and cite claim IDs in each key point.
6. Refresh the index: `python3 scripts/update_index.py <NN> --issue <n>`. Then add a "Not found yet" list by hand for scope items no source covered.
7. Run `python3 scripts/lint_front_matter.py`.
8. Save the research session as a prompt log. List the turns, then build the log from the saved session. Never retype it:
   `python3 scripts/make_prompt_log.py <session export> --list`
   `python3 scripts/make_prompt_log.py <session export> --turns <n> --slug <slug> --author @<handle> --platform "<platform>" --model "<name and version>" --role research --purpose "<one line>" --claims <ids> [--significant --reason "..."]`
   Use `--format json` for an agent whose export is not Claude Code's. Read the printed list of dropped lines and redactions.
9. Run the `agent-fact-check` skill on the new claims.

## Never

- Invent a URL, title, quote or date. If a source will not open, set `status: unverified` and say so.
- Set `human-verified` or write `review`.
- Commit or push unless the person asks.
