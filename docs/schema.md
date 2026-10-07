---
doc_type: spec
title: Knowledge base schema
updated: 2026-10-05
---

# Knowledge base schema

This file defines every field that `scripts/lint_front_matter.py` checks. If this file and the script disagree, fix the one that is wrong in the same PR.

## Document types

Every `.md` file in `knowledge-base/`, `prompts/` and this file starts with YAML front matter that has a `doc_type`.

| `doc_type` | Where | What it is |
|---|---|---|
| `topic-index` | `knowledge-base/NN-slug/index.md` | Topic metadata: owner, assignment section, scope |
| `topic-note` | `knowledge-base/NN-slug/*.md` | Claims, organized by the topic owner into files |
| `prompt-log` | `prompts/*.md` | One exact GenAI conversation |
| `spec` | `docs/schema.md` | This file |

`AGENTS.md`, `README.md`, `docs/assignment.md` and the files in `.github/` have no front matter and are not checked for it. Every `.md` file is still scanned for leaks.

## Topics

Each topic is a directory. The topic owner creates and organizes the notes inside it. Only the owner opens PRs for that directory. To change an owner, edit `owner` in `index.md` in a PR.

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

The target company is Google. Topic 12 covers it. A claim about Google is an `org-fact`; anything about Google's internal environment that no published source states must be `type: assumption`.

## `topic-index` fields

```yaml
---
doc_type: topic-index
topic: 02-hard-skills            # must equal the directory name
title: Hard skills and technical knowledge
assignment_section: "4.2"
report_sections: [4]
owner: "@handle"                 # "@TBD" until assigned
issue: 4                         # topic Issue number, or null
updated: 2026-10-05
---
```

## `topic-note` fields

```yaml
---
doc_type: topic-note
topic: 02-hard-skills            # must equal the directory name
title: Linux troubleshooting skills
updated: 2026-10-05
claims:
  - id: 02-01
    ...                          # see "Claim fields"
---
```

The body is optional prose: reasoning, context, drafting notes. Anything the report relies on must be a claim in the front matter.

## Claim fields

```yaml
- id: 02-01                      # <topic number>-<n>, unique inside the topic directory
  claim: Google SRE teams aim to cap operational work (toil) at 50% of time.
  type: fact                     # fact | org-fact | assumption
  status: human-verified         # unverified | ai-checked | human-verified | disputed
  source:
    title: "Google SRE Book, ch.1 Introduction"
    url: https://sre.google/sre-book/introduction/
    kind: official-doc           # job-ad | official-doc | paper | article | video | other
    accessed: 2026-10-06
    archive: null                # archive URL, required for org-fact
  quote: "<exact sentence copied from the source>"
  os_concepts: []                # optional: OS course concepts this claim supports
  pr: 12                         # PR number, or null
  ai_check:                      # the author's blind AI check (claim text and URL only)
    platform: Claude Code
    model: "<model name and version>"
    prompt_log: prompts/2026-10-06-member1-toil.md
    result: supported            # supported | partial | unsupported
  ai_recheck:                    # the reviewer's AI recheck, separate session
    platform: Codex CLI
    model: "<model name and version>"
    prompt_log: prompts/2026-10-07-member3-toil-recheck.md
    result: supported
  review:                        # the human reviewer
    by: "@member3"
    date: 2026-10-07
    result: pass                 # pass | fail
    opened_source: true
  note: null                     # required when status is disputed
  issue: null                    # dispute Issue number, required when status is disputed
```

### Types

- `fact`: a general claim backed by a source. Needs `source` and an exact `quote`.
- `org-fact`: a claim about the chosen company. Needs real evidence and an `archive` link, because job ads and pages disappear.
- `assumption`: a recommendation or typical environment with no company evidence. The assignment allows it only when it is labeled clearly. It can never become `human-verified`.

### Status gates

| Status | Required in addition to the base fields |
|---|---|
| `unverified` | `id`, `claim`, `type`; for `fact` and `org-fact` also `source` and `quote` |
| `ai-checked` | `ai_check` |
| `human-verified` | `ai_check`, `ai_recheck`, and `review` with `result: pass` and `opened_source: true` |
| `disputed` | `note` and `issue` |

Rules enforced across fields:

- `ai_check.prompt_log` and `ai_recheck.prompt_log` must be different existing prompt logs.
- The `ai_check` log must have `role: author-check`. The `ai_recheck` log must have `role: reviewer-recheck`, and its `author` must equal `review.by`.
- The `ai_check` is blind: the checking agent gets only the claim text, the source URL and the archive URL, never the `quote` or the research session. The lint cannot enforce this. The PR author states it in the checklist and the reviewer reads the `author-check` log.
- `review.by` must not be the PR author. CI checks this for the notes the PR changes; older claims keep the reviewer they had. The pre-push hook skips it because it does not know the PR author.
- Agents never set `status: human-verified` and never write `review`. Only a human reviewer does.

### Disputed claims

A claim is `disputed` when it has already merged and someone later reports that it is wrong, outdated, or not supported by its source. The flow is:

1. Anyone opens a `dispute` Issue that names the claim, for example `02-01`, with evidence.
2. A PR sets `status: disputed`, `note` and `issue`. The report cannot use the claim while it is disputed.
3. The claim is then re-checked and returns to `human-verified`, is corrected, is downgraded to `assumption`, or is deleted.

A disagreement between author and reviewer before merge is settled in the PR. It never becomes `disputed`.

## Prompt logs

One file per significant GenAI interaction, named `prompts/<id>.md`. The file name without `.md` must equal `id`.

```yaml
---
doc_type: prompt-log
id: 2026-10-06-member1-toil
author: "@member1"
date: 2026-10-06
platform: Claude Code
model: "<model name and version>"
phase: exploration               # exploration | report
role: author-check               # research | author-check | reviewer-recheck | session-summary | drafting
significant: false
significant_reason: null         # required when significant is true
purpose: Check claim 02-01 against the SRE book ch.1
pr: null                         # PR number, or null until the PR exists
claims: [02-01]
redactions: 2                    # number of [REDACTED:...] markers in this file
supporting_docs:
  - https://sre.google/sre-book/introduction/
---
```

The body is the exact conversation:

```markdown
## Turn 1 — user
<message, verbatim>

## Turn 1 — assistant
<reply, verbatim>

## Tool-call ledger
- WebFetch https://sre.google/sre-book/introduction/
- Read docs/assignment.md
```

Rules:

- Every user message and every AI reply is copied verbatim and in order. Only sensitive spans are replaced, with `[REDACTED:kind]` (for example `[REDACTED:email]`). Never reword anything.
- Hidden system prompts are not included. Files and URLs given to the model are listed in `supporting_docs`.
- The `## Tool-call ledger` heading is required. Put one line per tool call (tool name and arguments, no results), or `None.`
- `redactions` must equal the number of `[REDACTED:` markers in the file.
- The author redacts. The reviewer scans the diff for anything left over.

### What is significant

The instructor's rule: trivial prompts are not significant. Examples are fixing grammar or wording, and looking up where a phrase appears in a source.

- `significant: true`: the interaction produced content the report relies on. That means report text, the relationship diagram, or a key claim. Add a one-line `significant_reason`.
- `significant: false`: grammar or wording fixes, "where is this phrase in the source" lookups, formatting help, routine recheck lookups, session summaries, abandoned attempts.

Significant logs are copied into the report appendix in full. The instructor accepts non-significant logs through the repo URL, so they stay in `prompts/` and are not copied into the report. The appendix counts toward the 10–15 page cap, so keep significant logs focused. `scripts/appendix_budget.py` estimates the pages they use.

## Leak scan

The lint scans every `.md` file for emails, absolute home-directory paths, token patterns, Thai mobile numbers, and 9-digit or 13-digit numbers that look like IDs. A line containing the text `lint-allow` is skipped. Use that only for a false positive.
