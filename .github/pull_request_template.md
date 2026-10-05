## What this PR changes

Topic: `<NN-slug>`
Closes #<issue>

## Author checklist

- [ ] I am the owner of this topic directory (or `owner` is reassigned in `index.md` in this PR).
- [ ] Every `fact` and `org-fact` has a source I opened, an exact quote and an access date.
- [ ] Anything without evidence is `type: assumption`.
- [ ] I ran the AI fact check and filled `ai_check`. No claim is `human-verified` (only a reviewer sets that).
- [ ] Prompt logs are in `prompts/`: exact conversation, redacted only at sensitive spans, tool-call ledger, `significant` set.
- [ ] `python3 scripts/lint_front_matter.py` passes.
- [ ] No cover-page data, real names, emails, home-directory paths or tokens anywhere.

## Session summary

Written by my agent from my session. Redacted. No raw transcript (the exact conversation is in `prompts/`).

- Platform and model:
- Session start and end:
- Topic directory and Issue:

### Goal

### Prompts

One line each: prompt log id and purpose.

### Sources opened

URL, access date, what was taken, claim IDs.

### Claims added, changed or dropped

Claim IDs and why.

### AI errors found and corrected

What the AI said, what the source says, what I changed.

### AI fact-check results per claim

### Open items

Claims still `unverified` and assumptions.

### Searches and commands run

---

## Reviewer section

Filled by the reviewer. Do not review or merge your own PR.

- [ ] I opened every cited source and each quote matches the claim.
- [ ] I ran the AI recheck in a separate session that saw only the claim and the source URL. It is logged in `prompts/` with `role: reviewer-recheck`.
- [ ] I pushed a verification commit to this branch that fills `ai_recheck` and `review`, and set `human-verified` for passing claims.
- [ ] Claims I could not verify stay `unverified` or are relabeled `assumption`.
- [ ] I scanned the diff for sensitive information and for prompt logs that were altered or shortened.
- [ ] I approved after the verification commit.
- [ ] Merge: squash-merge, by someone other than the author. If the author is a reviewer, another reviewer merges.

Reviewer session summary (same shape as above, short):
