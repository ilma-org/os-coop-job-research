---
doc_type: topic-note
topic: 01-position-and-job-description
title: "SRE role and duties"
updated: 2026-10-11
claims:
  - id: 01-01
    claim: "The Google SRE book says SRE teams at Google focus on hiring software engineers to run products and to build systems that do work sysadmins would otherwise do, often manually."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, Ch.1 Introduction"
      url: https://sre.google/sre-book/introduction/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260919013803/https://sre.google/sre-book/introduction/
    quote: "our Site Reliability Engineering teams focus on hiring software engineers to run our products and to create systems to accomplish the work that would otherwise be performed, often manually, by sysadmins"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
  - id: 01-02
    claim: "The Google SRE book says SRE is what happens when a software engineer is asked to design an operations team, as SRE has come to be defined at Google."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, Ch.1 Introduction"
      url: https://sre.google/sre-book/introduction/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260919013803/https://sre.google/sre-book/introduction/
    quote: "SRE is what happens when you ask a software engineer to design an operations team."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
  - id: 01-03
    claim: "The Google SRE book says an SRE team is generally responsible for the availability, latency, performance, efficiency, change management, monitoring, emergency response and capacity planning of its services."
    type: fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, Ch.1 Introduction"
      url: https://sre.google/sre-book/introduction/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "In general, an SRE team is responsible for the availability, latency, performance, efficiency, change management, monitoring, emergency response, and capacity planning of their service(s)."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
  - id: 01-04
    claim: "The SRE Workbook says an SRE in general has particular expertise in the availability, latency, performance, efficiency, change management, monitoring, emergency response and capacity planning of the services they look after."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, Ch.1 How SRE Relates to DevOps"
      url: https://sre.google/workbook/how-sre-relates/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "In general, an SRE has particular expertise around the availability, latency, performance, efficiency, change management, monitoring, emergency response, and capacity planning of the service(s) they are looking after."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
  - id: 01-05
    claim: "The SRE Workbook says the basic tenet of SRE is that doing operations well is a software problem."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, Ch.1 How SRE Relates to DevOps"
      url: https://sre.google/workbook/how-sre-relates/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "The basic tenet of SRE is that doing operations well is a software problem."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
  - id: 01-07
    claim: "The SRE Workbook says that, in a way, class SRE implements interface DevOps."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, Ch.1 How SRE Relates to DevOps"
      url: https://sre.google/workbook/how-sre-relates/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "So, in a way, class SRE implements interface DevOps"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
  - id: 01-08
    claim: "The Google SRE book says SRE can be viewed as a specific implementation of DevOps with some idiosyncratic extensions."
    type: fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, Ch.1 Introduction"
      url: https://sre.google/sre-book/introduction/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "One could equivalently view SRE as a specific implementation of DevOps with some idiosyncratic extensions."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
  - id: 01-09
    claim: "The Google SRE book says Google caps operational work for SREs at 50% of their time, and that the remaining time should go to project work using coding skills."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, Ch.1 Introduction"
      url: https://sre.google/sre-book/introduction/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260919013803/https://sre.google/sre-book/introduction/
    quote: "Google caps operational work for SREs at 50% of their time. Their remaining time should be spent using their coding skills on project work."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
  - id: 01-10
    claim: "The SRE Workbook says the term Site Reliability Engineering and its associated job role were coined by a VP of engineering at Google."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, Ch.1 How SRE Relates to DevOps"
      url: https://sre.google/workbook/how-sre-relates/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260714011758/https://sre.google/workbook/how-sre-relates/
    quote: "Site Reliability Engineering (SRE) is a term (and associated job role) coined by Ben Treynor Sloss, a VP of engineering at Google."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
  - id: 01-11
    claim: "The SRE Workbook describes SRE as a job role and a set of practices."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, Ch.1 How SRE Relates to DevOps"
      url: https://sre.google/workbook/how-sre-relates/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "SRE is a job role, a set of practices"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
  - id: 01-75
    claim: "A Google job ad for Software Engineer, Android SRE says Site Reliability Engineering combines software and systems engineering to build and run large-scale, massively distributed, fault-tolerant systems."
    type: org-fact
    status: ai-checked
    source:
      title: "Software Engineer, Android SRE, Google Careers job ad"
      url: https://www.google.com/about/careers/applications/jobs/results/121141635160384198-software-engineer-android-sre
      kind: job-ad
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261011101435/https://www.google.com/about/careers/applications/jobs/results/121141635160384198-software-engineer-android-sre
    quote: "Site Reliability Engineering (SRE) combines software and systems engineering to build and run large-scale, massively distributed, fault-tolerant systems."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
  - id: 01-76
    claim: "A Google job ad for Software Engineer, Android SRE lists, as a responsibility, writing product or system development code."
    type: org-fact
    status: ai-checked
    source:
      title: "Software Engineer, Android SRE, Google Careers job ad"
      url: https://www.google.com/about/careers/applications/jobs/results/121141635160384198-software-engineer-android-sre
      kind: job-ad
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261011101435/https://www.google.com/about/careers/applications/jobs/results/121141635160384198-software-engineer-android-sre
    quote: "Write product or system development code."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
  - id: 01-77
    claim: "A Google job ad for Software Engineer, Android SRE lists, as a responsibility, triaging product or system issues and debugging, tracking and resolving them by analyzing the sources of issues and their impact on hardware, network, or service operations and quality."
    type: org-fact
    status: ai-checked
    source:
      title: "Software Engineer, Android SRE, Google Careers job ad"
      url: https://www.google.com/about/careers/applications/jobs/results/121141635160384198-software-engineer-android-sre
      kind: job-ad
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261011101435/https://www.google.com/about/careers/applications/jobs/results/121141635160384198-software-engineer-android-sre
    quote: "Triage product or system issues and debug/track/resolve by analyzing the sources of issues and the impact on hardware, network, or service operations and quality."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
  - id: 01-78
    claim: "A Google job ad for Software Engineer, Android SRE lists, as a responsibility, participating in or leading design reviews with peers and stakeholders to decide amongst available technologies."
    type: org-fact
    status: ai-checked
    source:
      title: "Software Engineer, Android SRE, Google Careers job ad"
      url: https://www.google.com/about/careers/applications/jobs/results/121141635160384198-software-engineer-android-sre
      kind: job-ad
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261011101435/https://www.google.com/about/careers/applications/jobs/results/121141635160384198-software-engineer-android-sre
    quote: "Participate in, or lead design reviews with peers and stakeholders to decide amongst available technologies."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
---

# SRE role and duties

## Summary

Google's SRE books describe Site Reliability Engineering as a job role in which software engineers run services and build systems to replace manual operations work (01-01, 01-02, 01-11). Both the SRE book and the SRE Workbook list the same duties: availability, latency, performance, efficiency, change management, monitoring, emergency response and capacity planning (01-03, 01-04). The books also say Google caps SRE operational work at 50% of time and treat SRE as a specific implementation of DevOps (01-07, 01-08, 01-09). Nearly all claims come from Google's own books and describe Google's view of the role. One Google job ad, for Software Engineer, Android SRE, repeats the software-plus-systems description and lists responsibilities (01-75 to 01-78). Not found yet: other companies' definitions.

## Key points

- Origin of the role: the term and its job role were coined by a VP of engineering at Google. (01-10)
- Definition: SRE is what happens when a software engineer is asked to design an operations team; Google SRE teams hire software engineers to run products and build systems that replace manual sysadmin work. (01-01, 01-02)
- Nature of the role: the Workbook calls SRE a job role plus a set of practices, and says the basic tenet is that doing operations well is a software problem. (01-05, 01-11)
- Duties: availability, latency, performance, efficiency, change management, monitoring, emergency response and capacity planning of the services the team supports; stated in both books. (01-03, 01-04)
- Time split: Google caps operational work for SREs at 50% of their time; the rest goes to project work that uses coding skills. (01-09)
- Relation to DevOps: the SRE book views SRE as a specific implementation of DevOps with some idiosyncratic extensions; the Workbook says "class SRE implements interface DevOps". (01-07, 01-08)
- Job ad description (one Google ad, Software Engineer, Android SRE): SRE combines software and systems engineering to build and run large-scale, massively distributed, fault-tolerant systems. (01-75)
- Job ad responsibilities (same ad): write product or system development code; triage product or system issues and debug, track and resolve them by analyzing the sources of issues and the impact on hardware, network, or service operations and quality; participate in or lead design reviews with peers and stakeholders. (01-76, 01-77, 01-78)

## Sources and limits

The SRE book and the SRE Workbook on https://sre.google/books/ were used, plus one Google Careers job ad (archived 2026-10-11) for the job-ad claims, which show one posting's wording and not every SRE role. The two books share authors' employer, so they are not independent sources; the duties list appears in both in almost the same words. The SRE book footer says copyright 2017 and the Workbook footer says copyright 2018, so each claim states what the book says, not necessarily current practice. Quotes are kept short; open the source for the full passage.
