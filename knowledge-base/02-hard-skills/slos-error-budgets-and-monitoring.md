---
doc_type: topic-note
topic: 02-hard-skills
title: SLIs, SLOs, error budgets, monitoring and alerting
updated: 2026-10-09
claims:
  - id: 02-07
    claim: "The SRE Fundamentals with Google course covers identifying key metrics, building SLOs and alerts, and systems design including single points of failure, performance and capacity planning."
    type: org-fact
    status: ai-checked
    source:
      title: "SRE Fundamentals online course with Google"
      url: https://sre.google/resources/practices-and-processes/sre-fundamentals-course/
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260828005315/https://sre.google/resources/practices-and-processes/sre-fundamentals-course/
    quote: "Learn to identify key metrics, build effective SLOs, and create alerts to maintain performance standards. Dive into Systems Design by developing systems from product specifications, assessing single points of failure, and understanding performance and capacity planning."
    os_concepts: []
    pr: 20
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-hard-skills-author-check-2.md
      result: supported
  - id: 02-08
    claim: "A report says SLOs are reliability targets measured by SLIs, and measurable SLOs eliminate conflicts around change management and event handling."
    type: fact
    status: ai-checked
    source:
      title: "Google SRE - Adoption and usage of slo with google sre"
      url: https://sre.google/resources/practices-and-processes/slo-adoption-and-usage/
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "To realize the full benefits of SRE, organizations need well-thought out reliability targets known as service level objectives (SLOs) that are measured by service level indicators (SLIs), a quantitative measure of an aspect of the service. As examined in this report, these measurable goals set forth in an organization’s SLOs eliminate the conflicts inherent in change management and event handling that cause the pace of innovation to slow and business to suffer."
    os_concepts: []
    pr: 20
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-hard-skills-author-check.md
      result: supported
  - id: 02-09
    claim: "Peter Pellerzi, who works on Google data center infrastructure, says the metric they look at is availability, with a target of five nines."
    type: org-fact
    status: ai-checked
    source:
      title: "Google SRE Prodcast transcript: The One With Data Centers and Peter Pellerzi"
      url: https://sre.google/prodcast/transcripts/sre-prodcast-04-02/
      kind: other
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260413020631/https://sre.google/prodcast/transcripts/sre-prodcast-04-02/
    quote: "So what's of concern, the metric that we look at is availability, 99.999, whatever, five nines of availability. That's our target."
    os_concepts: []
    pr: 20
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-hard-skills-author-check-2.md
      result: supported
  - id: 02-10
    claim: "The talk defines an SLI as time series data showing how good the level of service is, often from logs or sampled counters."
    type: fact
    status: ai-checked
    source:
      title: "Google SRE - SLOs ecosystem to measure reliability"
      url: https://sre.google/resources/practices-and-processes/measuring-reliability/
      kind: official-doc
      accessed: 2026-10-07
      archive: null
    quote: "Time series data which can tell us how good the level of service is. Often from logs or sampled counters."
    os_concepts: []
    pr: 20
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-hard-skills-author-check.md
      result: supported
  - id: 02-11
    claim: "Data processing can be declared reliable if well-reasoned SLOs are met; the freshness SLO asks whether the job completed in time and measures how long we can wait for the data to be available."
    type: fact
    status: ai-checked
    source:
      title: "Reliable Data Processing with Minimal Toil (Google SRE, Oct 12, 2021)"
      url: https://sre.google/static/pdf/reliable_data_processing_with_minimal_toil.pdf
      kind: official-doc
      accessed: 2026-10-09
      archive: https://web.archive.org/web/20260321103629/https://sre.google/static/pdf/reliable_data_processing_with_minimal_toil.pdf
    quote: "To apply an SRE approach, we can declare data processing to be reliable if well-reasoned SLOs are met. The freshness SLO (\"Did the job complete in time?\") is fairly straightforward to measure: it is a measure of how long we can wait for the data to be available."
    os_concepts: []
    pr: 20
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-hard-skills-author-check.md
      result: supported
  - id: 02-12
    claim: "The Workbook says each alert condition should have a playbook entry describing the steps to recovery, and that Google finds it useful to link this documentation in alert messages sent to on-call engineers."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook: Data Processing Pipelines"
      url: https://sre.google/workbook/data-processing/
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260827232609/https://sre.google/workbook/data-processing/
    quote: "Each alert condition in your system should have a corresponding playbook entry that describes the steps to recovery. At Google, we find it useful to link this documentation in any alert messages sent to on-call engineers."
    os_concepts: []
    pr: 20
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-hard-skills-author-check.md
      result: supported
  - id: 02-13
    claim: "SRE is a term and job role coined by Ben Treynor Sloss, a VP of engineering at Google."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook: How SRE Relates to DevOps"
      url: https://sre.google/workbook/how-sre-relates/
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260918074533/https://sre.google/workbook/how-sre-relates/
    quote: "Site Reliability Engineering (SRE) is a term (and associated job role) coined by Ben Treynor Sloss, a VP of engineering at Google."
    os_concepts: []
    pr: 20
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-hard-skills-author-check.md
      result: supported
  - id: 02-14
    claim: "At Google, a well-thought-out and adopted SLO is key to making data-informed decisions about the opportunity cost of reliability work and how to prioritize it."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook: Implementing SLOs"
      url: https://sre.google/workbook/implementing-slos/
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20261001130301/https://sre.google/workbook/implementing-slos/
    quote: "At Google, we’ve learned that a well-thought-out and adopted SLO is key to making data-informed decisions about the opportunity cost of reliability work, and to determining how to appropriately prioritize that work."
    os_concepts: []
    pr: 20
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-hard-skills-author-check.md
      result: supported
---

# SLIs, SLOs, error budgets, monitoring and alerting

## Summary

SLIs and SLOs are the core measurement skill in these sources: an SLI is time series data about how good the service is (02-10), and SLOs are reliability targets measured by SLIs (02-08) that Google uses to make data-informed decisions about prioritizing reliability work (02-14). The same idea applies to batch data processing through a freshness SLO (02-11), and each alert should come with a playbook entry (02-12). The SRE Fundamentals with Google course groups these skills with systems design and capacity planning (02-07). Each claim rests on one source; no second source was compared. This note has no claim on specific monitoring tools, which belong to topic 09.

## Key points

- An SLI is time series data showing how good the level of service is, often from logs or sampled counters (02-10).
- SLOs are reliability targets measured by SLIs, and measurable SLOs eliminate conflicts around change management and event handling (02-08).
- At Google, a well-thought-out and adopted SLO is key to data-informed decisions on prioritizing reliability work (02-14).
- Data processing can be declared reliable if well-reasoned SLOs are met, for example a freshness SLO (02-11).
- Each alert condition should have a playbook entry with the steps to recovery, and Google links it in alert messages (02-12).
- Peter Pellerzi, who works on Google data center infrastructure, says availability is the metric they look at, with a five-nines target (02-09).
- The SRE Fundamentals with Google course covers key metrics, SLOs, alerts and systems design including capacity planning (02-07).
- Ben Treynor Sloss, a VP of engineering at Google, coined the term SRE (02-13).

Claims are listed newest source first. Each claim's `status` in the front matter says how far it has been checked.

Source years in this note: 2025, 2022, 2021, 2018. A year is the publication or last-update year of the source, or the book edition year when the page gives none (SRE book 2016, Workbook 2018, Building Secure and Reliable Systems 2020).

## Claims at a glance

- `02-07` (org-fact): The SRE Fundamentals with Google course covers identifying key metrics, building SLOs and alerts, and systems design including single points of failure, performance and capacity planning.
- `02-08` (fact): A report says SLOs are reliability targets measured by SLIs, and measurable SLOs eliminate conflicts around change management and event handling.
- `02-09` (org-fact): Peter Pellerzi, who works on Google data center infrastructure, says the metric they look at is availability, with a target of five nines.
- `02-10` (fact): The talk defines an SLI as time series data showing how good the level of service is, often from logs or sampled counters.
- `02-11` (fact): Data processing can be declared reliable if well-reasoned SLOs are met; the freshness SLO asks whether the job completed in time and measures how long we can wait for the data to be available.
- `02-12` (org-fact): The Workbook says each alert condition should have a playbook entry describing the steps to recovery, and that Google finds it useful to link this documentation in alert messages sent to on-call engineers.
- `02-13` (org-fact): SRE is a term and job role coined by Ben Treynor Sloss, a VP of engineering at Google.
- `02-14` (org-fact): At Google, a well-thought-out and adopted SLO is key to making data-informed decisions about the opportunity cost of reliability work and how to prioritize it.

## Notes

- `org-fact` claims carry a Wayback Machine snapshot in `source.archive`. The exact quote was found in that snapshot on the claim's `source.accessed` date.
- Podcast speakers are named in the claim. A speaker who is not a Google employee is not evidence about Google, so those claims are `fact`, not `org-fact`.
