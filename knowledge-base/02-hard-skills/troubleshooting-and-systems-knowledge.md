---
doc_type: topic-note
topic: 02-hard-skills
title: Troubleshooting, OS, kernel and network knowledge
updated: 2026-10-09
claims:
- id: 02-23
  claim: Heather Adkins says insider-threat controls and mistake prevention often have very similar solutions.
  type: fact
  status: unverified
  source:
    title: 'Google SRE Prodcast transcript: The One With Heather Adkins'
    url: https://sre.google/prodcast/transcripts/sre-prodcast-05-03/
    kind: other
    accessed: '2026-10-07'
    archive: null
  quote: And if you think about, how do I keep an employee from doing something malicious, or how do I keep an employee from making a mistake, the solutions are often very similar.
  os_concepts: []
  pr: null
- id: 02-24
  claim: With global load balancing between GFE and backends, Google can redirect traffic during a datacenter outage, reducing mitigation time.
  type: org-fact
  status: ai-checked
  source:
    title: Building Secure and Reliable Systems, Chapter 7
    url: https://google.github.io/building-secure-and-reliable-systems/raw/ch07.html
    kind: official-doc
    accessed: '2026-10-07'
    archive: https://web.archive.org/web/20260616012631/https://google.github.io/building-secure-and-reliable-systems/raw/ch07.html
  quote: Global load balancing helps move traffic between GFE and backends. For example, we can redirect traffic during a datacenter outage, reducing mitigation time.
  os_concepts: []
  pr: null
  ai_check:
    platform: Claude Code
    model: "Sonnet 5.5 (claude-sonnet-5-5)"
    prompt_log: prompts/2026-10-09-nacs-970-hard-skills-author-check.md
    result: supported
- id: 02-25
  claim: Unchecked recurring outages increase operational toil and can exhaust error budgets, erode user trust and hurt revenue.
  type: fact
  status: ai-checked
  source:
    title: 'Google SRE: Incident Management Guide (PDF)'
    url: https://sre.google/static/pdf/IncidentManagementGuide.pdf
    kind: official-doc
    accessed: '2026-10-07'
    archive: https://web.archive.org/web/20260702124541/https://sre.google/static/pdf/IncidentManagementGuide.pdf
  quote: Left unchecked, outages tend to regularly resurface and accumulate over time. This increases the operational toil for the team and can lead to expended error budgets, eroded user trust, and impacted revenue.
  os_concepts: []
  pr: null
  ai_check:
    platform: Claude Code
    model: "Sonnet 5.5 (claude-sonnet-5-5)"
    prompt_log: prompts/2026-10-09-nacs-970-hard-skills-author-check.md
    result: supported
- id: 02-26
  claim: Resilience testing checks a system survives faults, latency or disruptions, while recovery testing checks it can return to a stable state after a full shutdown.
  type: fact
  status: ai-checked
  source:
    title: Lessons Learned from Two Decades of Site Reliability Engineering (Google SRE 20th anniversary PDF)
    url: https://sre.google/static/pdf/LessonsLearnedFromTwoDecades.pdf
    kind: official-doc
    accessed: '2026-10-07'
    archive: https://web.archive.org/web/20260908065110/https://sre.google/static/pdf/LessonsLearnedFromTwoDecades.pdf
  quote: While resilience testing verifies that your service or system could survive in the event of faults, latency, or disruptions, recovery testing verifies that your service can transition back to homeostasis after a full shutdown.
  os_concepts: []
  pr: null
  ai_check:
    platform: Claude Code
    model: "Sonnet 5.5 (claude-sonnet-5-5)"
    prompt_log: prompts/2026-10-09-nacs-970-hard-skills-author-check.md
    result: supported
- id: 02-27
  claim: Nonfunctional requirements include SLOs for metrics such as uptime and 95th- and 99th-percentile latency, and behavior under load above a threshold.
  type: fact
  status: ai-checked
  source:
    title: Building Secure and Reliable Systems, Chapter 4
    url: https://google.github.io/building-secure-and-reliable-systems/raw/ch04.html
    kind: official-doc
    accessed: '2026-10-07'
    archive: https://web.archive.org/web/20260606131700/https://google.github.io/building-secure-and-reliable-systems/raw/ch04.html
  quote: What are the service level objectives (SLOs) for metrics such as uptime or 95th-percentile and 99th-percentile response latency? How does the system respond under load above a certain threshold?
  os_concepts: []
  pr: null
  ai_check:
    platform: Claude Code
    model: "Sonnet 5.5 (claude-sonnet-5-5)"
    prompt_log: prompts/2026-10-09-nacs-970-hard-skills-author-check.md
    result: supported
- id: 02-28
  claim: When Google set tighter memory limits on Borg jobs, tasks that exceeded them even slightly were killed immediately, causing service disruptions and latency.
  type: org-fact
  status: ai-checked
  source:
    title: 'Case Studies in Infrastructure Change Management: How Google Rebuilds the Jet While Flying It (O''Reilly/Google report)'
    url: https://sre.google/static/pdf/CaseStudiesInfrastructureChangeManagement.pdf
    kind: official-doc
    accessed: '2026-10-07'
    archive: https://web.archive.org/web/20260219151023/https://sre.google/static/pdf/CaseStudiesInfrastructureChangeManagement.pdf
  quote: Therefore, if any tasks went over their new memory limits, even by a small amount, Borg killed them immediately, causing localized service disruptions and latency.
  os_concepts: []
  pr: null
  ai_check:
    platform: Claude Code
    model: "Sonnet 5.5 (claude-sonnet-5-5)"
    prompt_log: prompts/2026-10-09-nacs-970-hard-skills-author-check.md
    result: supported
- id: 02-29
  claim: Google's Disaster Recovery Testing (DiRT) frequently simulates regional outages against pipelines that depend on a datacenter.
  type: org-fact
  status: ai-checked
  source:
    title: 'The Site Reliability Workbook: Data Processing Pipelines'
    url: https://sre.google/workbook/data-processing/
    kind: official-doc
    accessed: '2026-10-07'
    archive: https://web.archive.org/web/20260827232609/https://sre.google/workbook/data-processing/
  quote: For example, many pipelines at Google depend on the availability of the datacenter where they run. Our Disaster Recovery Testing (DiRT) frequently targets these systems, simulating a regional outage.
  os_concepts: []
  pr: null
  ai_check:
    platform: Claude Code
    model: "Sonnet 5.5 (claude-sonnet-5-5)"
    prompt_log: prompts/2026-10-09-nacs-970-hard-skills-author-check.md
    result: supported
- id: 02-30
  claim: Google announces IPs via BGP from multiple points in its network and relies on BGP routing to deliver packets to the closest frontend location that can terminate a TCP session.
  type: org-fact
  status: ai-checked
  source:
    title: 'The Site Reliability Workbook: Managing Load'
    url: https://sre.google/workbook/managing-load/
    kind: official-doc
    accessed: '2026-10-07'
    archive: https://web.archive.org/web/20260909104922/https://sre.google/workbook/managing-load/
  quote: Google announces IPs via Border Gateway Protocol (BGP) from multiple points in our network.
  os_concepts: []
  pr: null
  ai_check:
    platform: Claude Code
    model: "Sonnet 5.5 (claude-sonnet-5-5)"
    prompt_log: prompts/2026-10-09-nacs-970-hard-skills-author-check.md
    result: supported
---

# Troubleshooting, OS, kernel and network knowledge

Claims are listed newest source first. Everything here is `unverified`: an AI agent copied each quote from the source page; no human has checked it yet.

Source years in this note: 2026, 2020, 2019, 2018. A year is the publication or last-update year of the source, or the book edition year when the page gives none (SRE book 2016, Workbook 2018, Building Secure and Reliable Systems 2020).

## Claims at a glance

- `02-23` (fact): Heather Adkins says insider-threat controls and mistake prevention have very similar solutions, which is why reliability and security were blended in the book.
- `02-24` (org-fact): With global load balancing between GFE and backends, Google can redirect traffic during a datacenter outage, reducing mitigation time.
- `02-25` (fact): Unchecked recurring outages increase operational toil and can exhaust error budgets, erode user trust and hurt revenue.
- `02-26` (fact): Resilience testing checks a system survives faults, latency or disruptions, while recovery testing checks it can return to a stable state after a full shutdown.
- `02-27` (fact): Nonfunctional requirements include SLOs for metrics such as uptime and 95th- and 99th-percentile latency, and behavior under load above a threshold.
- `02-28` (org-fact): When Google set tighter memory limits on Borg jobs, tasks that exceeded them even slightly were killed immediately, causing service disruptions and latency.
- `02-29` (org-fact): Google's Disaster Recovery Testing (DiRT) frequently simulates regional outages against pipelines that depend on a datacenter.
- `02-30` (org-fact): Google announces IPs via BGP from multiple points in its network and relies on BGP routing to deliver packets to the closest frontend location that can terminate a TCP session.

## Notes

- `org-fact` claims carry a Wayback Machine snapshot in `source.archive`. The exact quote was found in that snapshot on 2026-10-07.
- Podcast speakers are named in the claim. A speaker who is not a Google employee is not evidence about Google, so those claims are `fact`, not `org-fact`.
