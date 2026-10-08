---
name: issue-update
description: Update a topic Issue in this repo. Posts a progress comment or ticks "done when" checklist items, after the person confirms the text. Use when asked to "update the issue", "post progress" or "tick the checklist".
---

# issue-update

An Issue comment is public and outward-facing. Always show the exact text first and wait for a yes.

## Steps

1. Run the `issue-status` steps to see what is really done. Do not tick an item that has no evidence.
2. Draft the update in English. Use GitHub handles only. Include no emails, absolute paths, tokens or cover-page data.
3. Show the draft and the exact `gh` command. Wait for confirmation.
4. Post a comment:
   `gh issue comment <n> --body-file <file outside the repo>`
5. Or tick checklist items. Fetch the body, change `- [ ]` to `- [x]` for the confirmed items, then write it back:
   `gh issue view <n> --json body -q .body > <file outside the repo>`
   `gh issue edit <n> --body-file <file outside the repo>`
6. Read the Issue again and confirm the change.

## Never

- Close an Issue. The PR with `Closes #<n>` does that on merge.
- Change labels, assignees or the milestone unless the person asks.
- Edit another owner's Issue.
