---
doc_type: topic-note
topic: 09-monitoring-and-incident-tools
title: "Incident response and postmortem practice in Google's SRE books"
updated: 2026-10-14
claims:
  - id: 09-11
    claim: "The Workbook says the Incident Command System (ICS) was established in 1968 by firefighters as a way to manage wildfires."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.9 Incident Response"
      url: https://sre.google/workbook/incident-response/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "ICS was established in 1968 by firefighters as a way to manage wildfires."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-12
    claim: "The SRE book says the incident commander holds the high-level state about the incident."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.14 Managing Incidents"
      url: https://sre.google/sre-book/managing-incidents/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260919195840/https://sre.google/sre-book/managing-incidents/
    quote: "The incident commander holds the high-level state about the incident."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-13
    claim: "The SRE book says the operations team should be the only group modifying the system during an incident."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.14 Managing Incidents"
      url: https://sre.google/sre-book/managing-incidents/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260919195840/https://sre.google/sre-book/managing-incidents/
    quote: "The operations team should be the only group modifying the system during an incident."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-14
    claim: "The SRE book says most Google teams keep the live incident document in Google Docs, while Google Docs SRE use Google Sites."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.14 Managing Incidents"
      url: https://sre.google/sre-book/managing-incidents/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260919195840/https://sre.google/sre-book/managing-incidents/
    quote: "Most of our teams use Google Docs, though Google Docs SRE use Google Sites"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-15
    claim: "The Workbook says SREs typically gather in a war room that can be physical or virtual, such as an IRC channel or Hangout."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.9 Incident Response"
      url: https://sre.google/workbook/incident-response/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260919200614/https://sre.google/workbook/incident-response/
    quote: "The war room can be a physical location like a conference room, or it can be virtual: teams might gather on an IRC channel or Hangout."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-16
    claim: "The Workbook's PagerDuty case study, written by a PagerDuty author, says PagerDuty stores its on-call information, service ownership, postmortems and incident metadata in PagerDuty."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.9 Incident Response"
      url: https://sre.google/workbook/incident-response/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "We store all of our on-call information, service ownership, postmortems, incident metadata, and the like, in PagerDuty."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-17
    claim: "The Workbook's PagerDuty case study says PagerDuty prefers that coordination decisions are made in the conference call and that decision outcomes are recorded in Slack."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.9 Incident Response"
      url: https://sre.google/workbook/incident-response/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "We prefer that all coordination decisions are made in the conference call, and that decision outcomes are recorded in Slack."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-09-author-check-3.md
      result: supported
  - id: 09-18
    claim: "The SRE book says blameless postmortems are a tenet of SRE culture."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.15 Postmortem Culture: Learning from Failure"
      url: https://sre.google/sre-book/postmortem-culture/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261007020432/https://sre.google/sre-book/postmortem-culture/
    quote: "Blameless postmortems are a tenet of SRE culture."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-19
    claim: "The Workbook's glossary describes OMG (Outage Management at Google) as an incident management dashboard or tool for tracking and managing all ongoing incidents at Google."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.10 Postmortem Culture: Learning from Failure"
      url: https://sre.google/workbook/postmortem-culture/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261001130312/https://sre.google/workbook/postmortem-culture/
    quote: "An incident management dashboard/tool that serves as a central place for tracking and managing all ongoing incidents at Google."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-20
    claim: "The Workbook says several Google offices have informal Postmortem Reading Clubs that are open to all employees."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.10 Postmortem Culture: Learning from Failure"
      url: https://sre.google/workbook/postmortem-culture/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261001130312/https://sre.google/workbook/postmortem-culture/
    quote: "At Google, several offices have informal Postmortem Reading Clubs that are open to all employees."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-41
    claim: "The Workbook says the main roles in Google's incident response are the Incident Commander (IC), Communications Lead (CL) and Operations or Ops Lead (OL)."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.9 Incident Response"
      url: https://sre.google/workbook/incident-response/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260919200614/https://sre.google/workbook/incident-response/
    quote: "The main roles in incident response are the Incident Commander (IC), Communications Lead (CL), and Operations or Ops Lead (OL)."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-42
    claim: "The SRE book says the incident commander's most important responsibility is to keep a living incident document."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.14 Managing Incidents"
      url: https://sre.google/sre-book/managing-incidents/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260919195840/https://sre.google/sre-book/managing-incidents/
    quote: "The incident commander’s most important responsibility is to keep a living incident document."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-43
    claim: "The SRE book says Google's postmortem documents are Google Docs that use an in-house template."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.15 Postmortem Culture: Learning from Failure"
      url: https://sre.google/sre-book/postmortem-culture/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261007020432/https://sre.google/sre-book/postmortem-culture/
    quote: "Our postmortem documents are Google Docs, with an in-house template"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-44
    claim: "The SRE book says postmortem criteria should be defined before an incident occurs so that everyone knows when a postmortem is necessary."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.15 Postmortem Culture: Learning from Failure"
      url: https://sre.google/sre-book/postmortem-culture/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261007020432/https://sre.google/sre-book/postmortem-culture/
    quote: "It is important to define postmortem criteria before an incident occurs so that everyone knows when a postmortem is necessary."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-45
    claim: "In the SRE book's example postmortem (appendix D), the Detection entry says Borgmon detected a high level of HTTP 500s and paged on-call."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, appendix D Example Postmortem"
      url: https://sre.google/sre-book/example-postmortem/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260910212546/https://sre.google/sre-book/example-postmortem/
    quote: "Borgmon detected high level of HTTP 500s and paged on-call."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check-2.md
      result: supported
---

# Incident response and postmortem practice in Google's SRE books

## Summary

The books describe Google's incident management as based on the Incident Command System, with an incident commander, an operations lead and a communications lead. The live incident document is usually a Google Doc, and teams gather in a war room on IRC or Hangout. Postmortems are blameless, written in Google Docs from an in-house template, and triggered by criteria defined in advance. In the 21 pages searched, the only commercial incident tool named is PagerDuty, in a case study written by a PagerDuty author.

## Key points

- ICS dates from 1968 and was created by firefighters. Google's main roles are the incident commander, communications lead and operations lead (09-11, 09-41). The commander holds the incident state, and only the operations team modifies the system (09-12, 09-13).
- The commander keeps a living incident document, usually in Google Docs (09-42, 09-14). Responders gather in a physical or virtual war room, such as an IRC channel or Hangout (09-15).
- OMG (Outage Management at Google) is an incident management dashboard or tool for tracking all ongoing incidents (09-19).
- PagerDuty's own case study in the Workbook says it stores on-call data and postmortems in PagerDuty and prefers to make coordination decisions in the conference call and record the outcomes in Slack (09-16, 09-17). This describes PagerDuty, not Google.
- Blameless postmortems are a tenet of SRE culture. Postmortems are Google Docs with an in-house template, and criteria are set before an incident (09-18, 09-43, 09-44). The book's example postmortem (appendix D) says Borgmon detected the problem and paged on-call (09-45).
- Some Google offices run Postmortem Reading Clubs open to all employees (09-20).
