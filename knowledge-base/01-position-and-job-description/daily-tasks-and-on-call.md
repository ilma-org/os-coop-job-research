---
doc_type: topic-note
topic: 01-position-and-job-description
title: "Daily tasks and on-call"
updated: 2026-10-14
claims:
  - id: 01-12
    claim: "The Google SRE book says on-call engineers, as guardians of production systems, manage outages that affect the team and perform or vet production changes."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.11 Being On-Call"
      url: https://sre.google/sre-book/being-on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261011073700/https://sre.google/sre-book/being-on-call/
    quote: "As the guardians of production systems, on-call engineers take care of their assigned operations by managing outages that affect the team and performing and/or vetting production changes."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-13
    claim: "The Google SRE book says typical paging response times are 5 minutes for user-facing or otherwise highly time-critical services and 30 minutes for less time-sensitive systems."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.11 Being On-Call"
      url: https://sre.google/sre-book/being-on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261011073700/https://sre.google/sre-book/being-on-call/
    quote: "Typical values are 5 minutes for user-facing or otherwise highly time-critical services, and 30 minutes for less time-sensitive systems."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-15
    claim: "The Google SRE book says nonpaging production events, such as lower priority alerts or software releases, can also be handled or vetted by the on-call engineer during business hours."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.11 Being On-Call"
      url: https://sre.google/sre-book/being-on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261011073700/https://sre.google/sre-book/being-on-call/
    quote: "Nonpaging production events, such as lower priority alerts or software releases, can also be handled and/or vetted by the on-call engineer during business hours."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-16
    claim: "The Google SRE book says many Google SRE teams have both a primary and a secondary on-call rotation."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.11 Being On-Call"
      url: https://sre.google/sre-book/being-on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261011073700/https://sre.google/sre-book/being-on-call/
    quote: "Many teams have both a primary and a secondary on-call rotation."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-17
    claim: "The Google SRE book says SRE aims for at least 50% of time on engineering, with no more than 25% of the remainder spent on-call and up to another 25% on other operational, nonproject work."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, Ch.11 Being On-Call"
      url: https://sre.google/sre-book/being-on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261011073700/https://sre.google/sre-book/being-on-call/
    quote: "we strive to invest at least 50% of SRE time into engineering: of the remainder, no more than 25% can be spent on-call, leaving up to another 25% on other types of operational, nonproject work."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
  - id: 01-18
    claim: "The Google SRE book says the maximum number of incidents per day is 2 per 12-hour on-call shift."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, Ch.11 Being On-Call"
      url: https://sre.google/sre-book/being-on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261011073700/https://sre.google/sre-book/being-on-call/
    quote: "It follows that the maximum number of incidents per day is 2 per 12-hour on-call shift."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
  - id: 01-19
    claim: "The Google SRE book says Google offers time-off-in-lieu or straight cash compensation for on-call, capped at some proportion of overall salary."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.11 Being On-Call"
      url: https://sre.google/sre-book/being-on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261011073700/https://sre.google/sre-book/being-on-call/
    quote: "Google offers time-off-in-lieu or straight cash compensation, capped at some proportion of overall salary."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-20
    claim: "The Google SRE book lists clear escalation paths, well-defined incident-management procedures and a blameless postmortem culture as the most important on-call resources."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.11 Being On-Call"
      url: https://sre.google/sre-book/being-on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261011073700/https://sre.google/sre-book/being-on-call/
    quote: "The most important on-call resources are: Clear escalation paths Well-defined incident-management procedures A blameless postmortem culture"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-21
    claim: "The Google SRE book says SRE teams must write postmortems after significant incidents and detail a full timeline of the events that occurred."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.11 Being On-Call"
      url: https://sre.google/sre-book/being-on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261011073700/https://sre.google/sre-book/being-on-call/
    quote: "SRE teams must write postmortems after significant incidents and detail a full timeline of the events that occurred."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-23
    claim: "The Google SRE book says all paging alerts should be actionable."
    type: fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.11 Being On-Call"
      url: https://sre.google/sre-book/being-on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "All paging alerts should also be actionable."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-24
    claim: "The Google SRE book defines toil as work tied to running a production service that tends to be manual, repetitive, automatable, tactical, devoid of enduring value, and that scales linearly as a service grows."
    type: fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.5 Eliminating Toil"
      url: https://sre.google/sre-book/eliminating-toil/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "Toil is the kind of work tied to running a production service that tends to be manual, repetitive, automatable, tactical, devoid of enduring value, and that scales linearly as a service grows."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-25
    claim: "The Google SRE book says toil is interrupt-driven and reactive, and that handling pager alerts is toil."
    type: fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.5 Eliminating Toil"
      url: https://sre.google/sre-book/eliminating-toil/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "Toil is interrupt-driven and reactive, rather than strategy-driven and proactive. Handling pager alerts is toil."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-26
    claim: "The Google SRE book says operational load falls into three general categories: pages, tickets, and ongoing operational activities."
    type: fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.29 Dealing with Interrupts"
      url: https://sre.google/sre-book/dealing-with-interrupts/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "operational load falls into three general categories: pages, tickets, and ongoing operational activities."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-27
    claim: "The Google SRE book says tickets concern customer requests that require you to take an action."
    type: fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.29 Dealing with Interrupts"
      url: https://sre.google/sre-book/dealing-with-interrupts/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "Tickets concern customer requests that require you to take an action."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-28
    claim: "The Google SRE book says pages are most commonly managed by a dedicated primary on-call engineer."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.29 Dealing with Interrupts"
      url: https://sre.google/sre-book/dealing-with-interrupts/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260910213016/https://sre.google/sre-book/dealing-with-interrupts/
    quote: "Pages are most commonly managed by a dedicated primary on-call engineer."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-29
    claim: "The Google SRE book says tickets are handled in different ways depending on the SRE team: by the primary on-call engineer, by the secondary, or by a dedicated ticket person who is not on-call."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.29 Dealing with Interrupts"
      url: https://sre.google/sre-book/dealing-with-interrupts/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260910213016/https://sre.google/sre-book/dealing-with-interrupts/
    quote: "a primary on-call engineer might work on tickets while on-call, a secondary engineer might work on tickets while on-call, or a team can have a dedicated ticket person who is not on-call."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-30
    claim: "The SRE Workbook says that during on-call shifts SREs diagnose, mitigate, fix, or escalate incidents as needed, and are regularly responsible for nonurgent production duties."
    type: fact
    status: human-verified
    source:
      title: "The Site Reliability Workbook, Ch.8 On-Call"
      url: https://sre.google/workbook/on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "During on-call shifts, SREs diagnose, mitigate, fix, or escalate incidents as needed. In addition, SREs are regularly responsible for nonurgent production duties."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-31
    claim: "The SRE Workbook says that at Google, being on-call is one of the defining characteristics of SRE."
    type: org-fact
    status: human-verified
    source:
      title: "The Site Reliability Workbook, Ch.8 On-Call"
      url: https://sre.google/workbook/on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261011015106/https://sre.google/workbook/on-call/
    quote: "At Google, being on-call is one of the defining characteristics of SRE."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-32
    claim: "In a Workbook case study of a new Google SRE team, the guidelines said the on-call engineer reads the handoff from the previous shift at the start of each shift."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, Ch.8 On-Call"
      url: https://sre.google/workbook/on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261011015106/https://sre.google/workbook/on-call/
    quote: "At the start of each shift, the on-call engineer reads the handoff from the previous shift."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
  - id: 01-33
    claim: "In a Workbook case study of a new Google SRE team, the guidelines said the on-call engineer minimizes user impact first, then makes sure the issues are fully addressed."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, Ch.8 On-Call"
      url: https://sre.google/workbook/on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261011015106/https://sre.google/workbook/on-call/
    quote: "The on-call engineer minimizes user impact first, then makes sure the issues are fully addressed."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
  - id: 01-34
    claim: "In a Workbook case study of a new Google SRE team, the guidelines said the on-call engineer sends a handoff email to the next on-call engineer at the end of the shift."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, Ch.8 On-Call"
      url: https://sre.google/workbook/on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260807232155/https://sre.google/workbook/on-call/
    quote: "At the end of the shift, the on-call engineer sends a handoff email to the next engineer on-call."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
  - id: 01-35
    claim: "The SRE Workbook says playbooks contain high-level instructions on how to respond to automated alerts."
    type: fact
    status: human-verified
    source:
      title: "The Site Reliability Workbook, Ch.8 On-Call"
      url: https://sre.google/workbook/on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "Playbooks contain high-level instructions on how to respond to automated alerts."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-105
    claim: "The Google SRE book says that once a page is received and acknowledged, the on-call engineer is expected to triage the problem and work toward its resolution, possibly involving other team members and escalating as needed."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.11 Being On-Call"
      url: https://sre.google/sre-book/being-on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261011073700/https://sre.google/sre-book/being-on-call/
    quote: "As soon as a page is received and acknowledged, the on-call engineer is expected to triage the problem and work toward its resolution, possibly involving other team members and escalating as needed."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check-2.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-106
    claim: "The Google SRE book says SRE can ask the developer team to be exclusively on-call for a system until it meets the standards of the SRE team in question."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, Ch.11 Being On-Call"
      url: https://sre.google/sre-book/being-on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261011073700/https://sre.google/sre-book/being-on-call/
    quote: "SRE can ask the developer team to be exclusively on-call for the system until it meets the standards of the SRE team in question."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check-2.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
---

# Daily tasks and on-call

## Summary

Google's SRE books describe an SRE's work as on-call duty plus operational work that arrives as pages, tickets and ongoing operational activities (01-12, 01-26, 01-30). On-call engineers triage and resolve pages, handle nonpaging events and hand over to the next shift, and the books give limits on how much on-call and operational work one SRE should carry (01-105, 01-15, 01-17, 01-18, 01-34). They also describe supporting practices: escalation paths, postmortems, playbooks, actionable alerts and the option to give back the pager (01-20, 01-21, 01-35, 01-23, 01-106). The sources describe Google SRE teams as a general pattern. They do not give a day-by-day schedule for one SRE, and this note does not infer one.

## Key points

- On-call role: on-call engineers manage outages that affect the team and perform or vet production changes; during a shift SREs diagnose, mitigate, fix or escalate incidents and also handle nonurgent production duties. At Google, on-call is one of the defining characteristics of SRE. (01-12, 01-30, 01-31)
- Responding to a page: typical response times are 5 minutes for user-facing or time-critical services and 30 minutes for less time-sensitive ones; after acknowledging a page the engineer triages and works toward resolution, involving others and escalating as needed. (01-13, 01-105)
- Other work on shift: nonpaging events such as lower priority alerts or software releases can be handled or vetted by the on-call engineer during business hours; tickets may go to the primary on-call, the secondary, or a dedicated ticket person. (01-15, 01-29)
- Rotation structure: many teams run primary and secondary rotations, and pages are most commonly managed by a dedicated primary on-call engineer. (01-16, 01-28)
- Workload limits: at least 50% of SRE time goes to engineering, no more than 25% of the remainder on-call, and at most 2 incidents per 12-hour on-call shift. (01-17, 01-18)
- Operational load types: pages, tickets and ongoing operational activities; toil is manual, repetitive, automatable, tactical work with no enduring value that scales linearly, and handling pager alerts counts as toil. (01-26, 01-27, 01-24, 01-25)
- Handoffs (Workbook case study of a new Google SRE team): read the previous shift's handoff at the start, minimize user impact first, send a handoff email at the end. (01-32, 01-33, 01-34)
- Support for on-call: clear escalation paths, defined incident-management procedures and a blameless postmortem culture; postmortems with a full timeline after significant incidents; playbooks for automated alerts; all paging alerts should be actionable. (01-20, 01-21, 01-35, 01-23)
- Overload and pay: SRE can give back the pager to the developer team until a system meets its standards; Google offers time off in lieu or cash compensation for on-call, capped at a proportion of salary. (01-106, 01-19)

## Sources and limits

Used the SRE book chapters 5, 11 and 29 and the SRE Workbook chapter 8, all from https://sre.google/books/. The Workbook chapter re-states and extends the SRE book chapter, so they are not independent sources. The handoff claims come from one case study of a new team, not from a rule for all teams. The SRE book footer says copyright 2017 and the Workbook footer says copyright 2018, so each claim states what the book says, not necessarily current practice. Quotes are kept short; open the source for the full passage.

## Not found yet

- No source in this round gives a typical hour-by-hour or weekly schedule for an SRE.
- No Google job ad was used for daily tasks.
