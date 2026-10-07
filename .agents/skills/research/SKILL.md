---
name: research
description: Research claims for a topic note in this repo. Find published sources, copy exact quotes, verify them against the page, find archive links, and write claims as unverified with a summary. Use when asked to research a topic or Issue, add claims, or "start research on <topic>".
---

# research

Follows `AGENTS.md` and `docs/schema.md`. Read both first, then the topic's `index.md` (scope, owner, Issue, gaps).

## Steps

1. Check you are the topic owner and on a topic branch `<NN>-<slug>/<short-description>`, created from `origin/main`. Never work on `main`.
2. Choose sources. Prefer official docs and books, then job ads, papers and articles. Secondary research only. A claim about Google needs a Google-published source (SRE books, Google careers pages, official Google pages).
3. Open each source yourself. Pick one or two sentences per claim. Write the claim no broader than the quote. If the passage is an example or an anecdote, say so in the claim text.
4. Check every quote against the live page. The command must print `EXACT`:
   `python3 .agents/skills/research/scripts/verify_quote.py <url> "<quote>"`
5. For an org-fact, find an archive snapshot: `curl -s "https://archive.org/wayback/available?url=<url>"`. Then run `verify_quote.py` on the snapshot URL. If no snapshot exists, ask the person before requesting a new one.
6. Write the claims in a topic note, following `docs/schema.md`. Set `status: unverified`, `pr: null` and today's `accessed` date. Add no `ai_check`. Use `type: assumption` for anything no source states, and never write it as a fact.
7. Start the note body with `## Summary` and `## Key points`, written only from the claims. Cite claim IDs in each key point. Add no fact that is not a claim.
8. Update `index.md`: Issue number, the note list, `updated`, and a "Not found yet" list for scope items no source covered.
9. Run `python3 scripts/lint_front_matter.py`. Save the research session as a prompt log with `role: research` (`AGENTS.md`, Prompt logs).
10. Run the `agent-fact-check` skill on the new claims.

## Never

- Invent a URL, title, quote or date. If a source will not open, set `status: unverified` and say so.
- Set `human-verified` or write `review`.
- Commit or push unless the person asks.
