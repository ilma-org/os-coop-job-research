---
doc_type: topic-note
topic: 12-organization-and-working-environment
title: "SRE working environment and culture at Google"
updated: 2026-10-14
claims:
  - id: 12-18
    claim: "The SRE Workbook says SRE at Google inherited much of its culture from the surrounding company."
    type: org-fact
    status: human-verified
    source:
      title: "The Site Reliability Workbook, ch.1 How SRE Relates to DevOps"
      url: https://sre.google/workbook/how-sre-relates/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20260714011758/https://sre.google/workbook/how-sre-relates/
    quote: "SRE at Google inherited much of its culture from the surrounding company before the term SRE became widely popularized across the industry."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-15-nine14282-12-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-15
      result: pass
      opened_source: true
  - id: 12-19
    claim: "Building Secure and Reliable Systems says Google does not get culture right all the time and keeps trying to improve it."
    type: org-fact
    status: human-verified
    source:
      title: "Building Secure and Reliable Systems, ch.21 Building a Culture of Security and Reliability"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch21.html
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20261011173502/https://google.github.io/building-secure-and-reliable-systems/raw/ch21.html
    quote: "At Google too, we don’t get culture right all the time, and we’re constantly seeking to improve upon the status quo."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-15-nine14282-12-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-15
      result: pass
      opened_source: true
  - id: 12-20
    claim: "Building Secure and Reliable Systems says Google assumes failure can happen at any time."
    type: org-fact
    status: human-verified
    source:
      title: "Building Secure and Reliable Systems, ch.21 Building a Culture of Security and Reliability"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch21.html
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20261011173502/https://google.github.io/building-secure-and-reliable-systems/raw/ch21.html
    quote: "At Google, we assume failure can happen at any time"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-15-nine14282-12-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-15
      result: pass
      opened_source: true
  - id: 12-21
    claim: "Building Secure and Reliable Systems says Google has large teams of dedicated SREs and operational security staff, and that these teams work in \"follow the sun\" shifts to avoid stress and burnout."
    type: org-fact
    status: human-verified
    source:
      title: "Building Secure and Reliable Systems, ch.21 Building a Culture of Security and Reliability"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch21.html
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20261011173502/https://google.github.io/building-secure-and-reliable-systems/raw/ch21.html
    quote: "Google has many moving parts and a correspondingly complex adversary landscape, which necessitates large teams of dedicated SREs and operational security personnel. These teams operate in “follow the sun” shifts in order to avoid stress and burnout, and are designed to be staffed accordingly."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-15-nine14282-12-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-15
      result: pass
      opened_source: true
  - id: 12-22
    claim: "Building Secure and Reliable Systems says Google trains managers to build and maintain healthy teams, and that these principles are part of Project Oxygen."
    type: org-fact
    status: human-verified
    source:
      title: "Building Secure and Reliable Systems, ch.21 Building a Culture of Security and Reliability"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch21.html
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20261011173502/https://google.github.io/building-secure-and-reliable-systems/raw/ch21.html
    quote: "Managers are trained to focus on building and maintaining healthy teams, which includes addressing negative impacts of the work. These principles are encoded in our culture as part of Project Oxygen"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-15-nine14282-12-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-15
      result: pass
      opened_source: true
  - id: 12-23
    claim: "Building Secure and Reliable Systems says Google provides mandatory annual security and reliability training for all employees."
    type: org-fact
    status: human-verified
    source:
      title: "Building Secure and Reliable Systems, ch.21 Building a Culture of Security and Reliability"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch21.html
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20261011173502/https://google.github.io/building-secure-and-reliable-systems/raw/ch21.html
    quote: "Google takes several approaches to educating employees about security and reliability. On a broad scale, we provide mandatory annual training for all employees."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-15-nine14282-12-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-15
      result: pass
      opened_source: true
  - id: 12-24
    claim: "The SRE Workbook says Google compensates on-call work with time-off-in-lieu or cash, capped at a proportion of overall salary."
    type: org-fact
    status: human-verified
    source:
      title: "The Site Reliability Workbook, ch.8 On-Call"
      url: https://sre.google/workbook/on-call/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20261011015106/https://sre.google/workbook/on-call/
    quote: "Google offers time-off-in-lieu or cash compensation, capped at some proportion of the overall salary."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-15-nine14282-12-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-15
      result: pass
      opened_source: true
  - id: 12-25
    claim: "The SRE book says that when a service justifies growing a single-site team, Google prefers to create a multi-site team, and gives as one reason that night shifts harm people's health."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, ch.11 Being On-Call"
      url: https://sre.google/sre-book/being-on-call/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20261011174517/https://sre.google/sre-book/being-on-call/
    quote: "If a service entails enough work to justify growing a single-site team, we prefer to create a multi-site team. A multi-site team is advantageous for two reasons: Night shifts have detrimental effects on people’s health"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-15-nine14282-12-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-15
      result: pass
      opened_source: true
  - id: 12-26
    claim: "The SRE Workbook says all new SREs at Google attend SRE EDU, an immersive weeklong training on key concepts, tooling and platforms."
    type: org-fact
    status: human-verified
    source:
      title: "The Site Reliability Workbook, ch.20 SRE Team Lifecycles"
      url: https://sre.google/workbook/team-lifecycles/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20251231223709/https://sre.google/workbook/team-lifecycles/
    quote: "At Google, all new SREs attend SRE EDU, an immersive weeklong training that introduces key concepts, tooling, and platforms that almost all SREs work with."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-15-nine14282-12-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-15
      result: pass
      opened_source: true
  - id: 12-27
    claim: "The SRE Workbook says Google's SRE Exchange program lets an SRE spend a week working alongside a different SRE team."
    type: org-fact
    status: human-verified
    source:
      title: "The Site Reliability Workbook, ch.20 SRE Team Lifecycles"
      url: https://sre.google/workbook/team-lifecycles/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20251231223709/https://sre.google/workbook/team-lifecycles/
    quote: "Google’s SRE Exchange program lets an SRE spend a week working alongside a different SRE team."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-15-nine14282-12-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-15
      result: pass
      opened_source: true
  - id: 12-28
    claim: "The SRE Workbook says that at Google, SREs without performance issues are free to transfer to other SRE teams with open headcount."
    type: org-fact
    status: human-verified
    source:
      title: "The Site Reliability Workbook, ch.20 SRE Team Lifecycles"
      url: https://sre.google/workbook/team-lifecycles/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20251231223709/https://sre.google/workbook/team-lifecycles/
    quote: "Assuming there are no performance issues, SREs are free to transfer to other SRE teams with open headcount."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-15-nine14282-12-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-15
      result: pass
      opened_source: true
  - id: 12-29
    claim: "The SRE Workbook says Google has had success giving SRE teams a regular forum for learning and discussing SRE practices and reflecting on team performance."
    type: org-fact
    status: human-verified
    source:
      title: "The Site Reliability Workbook, ch.20 SRE Team Lifecycles"
      url: https://sre.google/workbook/team-lifecycles/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20251231223709/https://sre.google/workbook/team-lifecycles/
    quote: "At Google, we’ve had success providing a regular forum for learning and discussing SRE practices and reflecting on how the team is performing."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-15-nine14282-12-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-15
      result: pass
      opened_source: true
---

# SRE working environment and culture at Google

## Summary

The SRE books say SRE at Google took much of its culture from the rest of the company, assumes failure can happen at any time, and admits Google does not always get culture right. Workload is shaped to protect people: "follow the sun" shifts and multi-site teams avoid night shifts and burnout, on-call work is paid in time off or cash up to a cap, and managers are trained to build healthy teams under Project Oxygen. New SREs attend a weeklong SRE EDU course, all employees take mandatory annual security and reliability training, and SREs can visit other teams (SRE Exchange) or transfer to teams with open headcount. The books do not describe offices, working hours, remote-work policy or pay beyond on-call compensation.

## Key points

- SRE at Google inherited much of its culture from the surrounding company. (12-18)
- Google says it does not always get culture right, and it assumes failure can happen at any time. (12-19, 12-20)
- SRE and operational security teams work "follow the sun" shifts to avoid stress and burnout; Google prefers multi-site teams partly because night shifts harm health. (12-21, 12-25)
- Managers are trained to build healthy teams, as part of Project Oxygen. (12-22)
- On-call work is compensated with time-off-in-lieu or cash, capped at a proportion of salary. (12-24)
- Training: mandatory annual security and reliability training for all employees, and the weeklong SRE EDU for all new SREs. (12-23, 12-26)
- SREs can spend a week with another team through SRE Exchange, and can transfer to SRE teams with open headcount if there are no performance issues. (12-27, 12-28)
- Teams have used a regular forum for learning SRE practices and reflecting on team performance. (12-29)
