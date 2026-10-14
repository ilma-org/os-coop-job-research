---
doc_type: topic-note
topic: 12-organization-and-working-environment
title: "How SRE is organized at Google"
updated: 2026-10-14
claims:
  - id: 12-07
    claim: "The SRE Workbook says SRE and product development are separate organizations at Google, each with its own focus, priorities and management."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.1 How SRE Relates to DevOps"
      url: https://sre.google/workbook/how-sre-relates/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20260714011758/https://sre.google/workbook/how-sre-relates/
    quote: "At Google, SRE and product development are separate organizations. Each group has its own focus, priorities, and management, and does not have to do the bidding of the other."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
  - id: 12-08
    claim: "The SRE Workbook says product development teams at Google fund the growth of SRE with new hires when a product is successful."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.1 How SRE Relates to DevOps"
      url: https://sre.google/workbook/how-sre-relates/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20260714011758/https://sre.google/workbook/how-sre-relates/
    quote: "However, the product development teams effectively fund the growth of SRE with new hires when a product is successful."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
  - id: 12-09
    claim: "The SRE Workbook says product development teams at Google own their service by default, and that SRE is not available or warranted for most services."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.1 How SRE Relates to DevOps"
      url: https://sre.google/workbook/how-sre-relates/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20260714011758/https://sre.google/workbook/how-sre-relates/
    quote: "product development teams in Google own their service by default. SRE is neither available nor warranted for the bulk of services, although SRE principles still inform how services are managed throughout Google."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
  - id: 12-10
    claim: "The SRE book says Google SRE has infrastructural teams, service teams and horizontal product teams."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.31 Communication and Collaboration in SRE"
      url: https://sre.google/sre-book/communication-and-collaboration/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20260910213235/https://sre.google/sre-book/communication-and-collaboration/
    quote: "We have infrastructural teams, service teams, and horizontal product teams."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
  - id: 12-11
    claim: "The SRE book says SRE at Google is not a command-and-control organization."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.31 Communication and Collaboration in SRE"
      url: https://sre.google/sre-book/communication-and-collaboration/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20260910213235/https://sre.google/sre-book/communication-and-collaboration/
    quote: "It's also true that SRE is not a command-and-control organization."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
  - id: 12-12
    claim: "The SRE book says Google is a multinational organization and that, because of emergency response and pager rotations, SRE is distributed across at least a few time zones."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.31 Communication and Collaboration in SRE"
      url: https://sre.google/sre-book/communication-and-collaboration/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20260910213235/https://sre.google/sre-book/communication-and-collaboration/
    quote: "Obviously, Google is a multinational organization. Because of the emergency response and pager rotation component of our role, we have very good business reasons to be a distributed organization, separated by at least a few time zones."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
  - id: 12-13
    claim: "The SRE Workbook says Google has hundreds of on-call rotations, and that many developer teams, not only SRE, are directly on-call for their service."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.8 On-Call"
      url: https://sre.google/workbook/on-call/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20261011015106/https://sre.google/workbook/on-call/
    quote: "Google has hundreds of on-call rotations across services of all sizes, and various on-call setups from simple to complicated. On-call is not exclusively an SRE function: many developer teams are directly on-call for their service."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
  - id: 12-14
    claim: "The SRE Workbook says Google SRE teams most commonly interact with a distinct product development team."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.20 SRE Team Lifecycles"
      url: https://sre.google/workbook/team-lifecycles/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20251231223709/https://sre.google/workbook/team-lifecycles/
    quote: "At Google, SRE teams most commonly interact with a distinct product development team."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
  - id: 12-15
    claim: "The SRE Workbook says Google uses horizontal teams, often staffed by experienced SREs, to build and run standard solutions that other SRE teams adopt."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.20 SRE Team Lifecycles"
      url: https://sre.google/workbook/team-lifecycles/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20251231223709/https://sre.google/workbook/team-lifecycles/
    quote: "Google approaches these efforts by using horizontal teams, which are often staffed by experienced SREs. These horizontal teams build and run a standard solution and partner with other SRE teams to ensure smooth adoption."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
  - id: 12-16
    claim: "In a case study, the SRE Workbook describes one of Google's internal storage SRE teams that ran backends for Gmail, Google Drive, Google Groups and other services."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.17 Identifying and Recovering from Overload"
      url: https://sre.google/workbook/overload/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20260701072242/https://sre.google/workbook/overload/
    quote: "One of Google’s internal storage SRE teams was in charge of backends for multiple services, including Gmail, Google Drive, and Google Groups, and many other internal or user-facing services."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
  - id: 12-17
    claim: "The SRE Workbook says it would be naive to assume that the efficacy of SRE at Google has nothing to do with Google's widely accessible unified codebase."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.1 How SRE Relates to DevOps"
      url: https://sre.google/workbook/how-sre-relates/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20260714011758/https://sre.google/workbook/how-sre-relates/
    quote: "it would be naive to assume that the efficacy of SRE in the Google context has nothing to do with the widely accessible unified codebase"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
---

# How SRE is organized at Google

## Summary

At Google, SRE and product development are separate organizations with their own management, and product teams own their services by default; SRE supports only some services and is funded with new hires when a product succeeds. SRE has infrastructural, service and horizontal teams, is not run command-and-control, and is spread over at least a few time zones because of on-call duty. Google has hundreds of on-call rotations, and many developer teams are on-call for their own services. The books do not give the size of the SRE organization or list its office locations.

## Key points

- SRE and product development are separate organizations, each with its own focus, priorities and management. (12-07)
- Product development teams fund SRE growth with new hires when a product succeeds. (12-08)
- Product teams own their services by default; SRE is not available or warranted for most services. (12-09)
- SRE has infrastructural, service and horizontal product teams, and is not a command-and-control organization. (12-10, 12-11)
- Google is multinational, and SRE is distributed over at least a few time zones for emergency response and pager rotations. (12-12)
- Google has hundreds of on-call rotations; on-call is not only an SRE job. (12-13)
- SRE teams most often pair with one distinct product development team; horizontal teams of experienced SREs build shared standard solutions. (12-14, 12-15)
- Example: one storage SRE team ran backends for Gmail, Google Drive and Google Groups. (12-16)
- The Workbook links SRE's efficacy at Google to its widely accessible unified codebase. (12-17)
