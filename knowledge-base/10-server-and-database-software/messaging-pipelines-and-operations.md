---
doc_type: topic-note
topic: 10-server-and-database-software
title: "Message queues and data pipelines"
updated: 2026-10-14
claims:
  - id: 10-29
    claim: "In an example where a queue buffers transaction data while a payment provider is unreachable, Building Secure and Reliable Systems says that if the message queue is not designed to be reliable, for example if it stores data in volatile memory only, you can lose transactions, a new risk surface."
    type: fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, Chapter 4"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch04.html
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260606131700/https://google.github.io/building-secure-and-reliable-systems/raw/ch04.html
    quote: "If the message queue is not designed to be reliable (for example, it stores data in volatile memory only), you can lose transactions—a new risk surface."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-nine14282-server-db-author-check-5.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-10-reviewer-recheck-2.md
      result: supported
  - id: 10-31
    claim: "For data pipelines, in a section headed \"Delayed data\", the SRE Workbook says stale data is almost always better than incorrect data."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook: Data Processing Pipelines"
      url: https://sre.google/workbook/data-processing/
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260827232609/https://sre.google/workbook/data-processing/
    quote: "Stale data is almost always better than incorrect data."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-nine14282-server-db-author-check-5.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-10-reviewer-recheck-2.md
      result: supported
  - id: 10-36
    claim: "In its Waze case study, the SRE Workbook says the message queueing system was critical to operations because every component of Waze used it to communicate with other components internally."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, Chapter 21: Organizational Change Management in SRE"
      url: https://sre.google/workbook/organizational-change/
      kind: official-doc
      accessed: 2026-10-12
      archive: https://web.archive.org/web/20260920011350/https://sre.google/workbook/organizational-change/
    quote: "the message queueing system was critical to operations because every component of Waze (real time, geocoding, routing, etc.) used it to communicate with other components internally."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-server-db-author-check-3.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-10-reviewer-recheck.md
      result: supported
---

# Message queues and data pipelines

## Summary

On message queues, Building Secure and Reliable Systems says that in an example where a queue buffers payment transactions during a provider outage, a queue that stores data in volatile memory only can lose transactions (10-29), and a Workbook case study says Waze's message queueing system was critical because every component used it (10-36). For data pipelines, in a section headed "Delayed data", the SRE Workbook says stale data is almost always better than incorrect data (10-31). Each claim rests on one source; no second source was compared, and this note has no claim yet on a specific message queue product such as Kafka or RabbitMQ.

## Key points

- In an example where a queue buffers transaction data while a payment provider is unreachable, Building Secure and Reliable Systems says a message queue that stores data in volatile memory only can lose transactions (10-29).
- In its Waze case study, the SRE Workbook says the message queueing system was critical because every component of Waze used it to communicate internally (10-36).
- For data pipelines, in a section headed "Delayed data", the SRE Workbook says stale data is almost always better than incorrect data (10-31).

Claims are listed newest source first. Each claim's `status` in the front matter says how far it has been checked.

Source years in this note: 2020, 2018. A year is the publication or last-update year of the source, or the book edition year when the page gives none (SRE book 2016, Workbook 2018, Building Secure and Reliable Systems 2020).

## Claims at a glance

- `10-29` (fact): In an example where a queue buffers transaction data while a payment provider is unreachable, Building Secure and Reliable Systems says that if the message queue is not designed to be reliable, for example if it stores data in volatile memory only, you can lose transactions, a new risk surface.
- `10-31` (fact): For data pipelines, in a section headed "Delayed data", the SRE Workbook says stale data is almost always better than incorrect data.
- `10-36` (fact): In its Waze case study, the SRE Workbook says the message queueing system was critical to operations because every component of Waze used it to communicate with other components internally.

## Notes

- `org-fact` claims carry a Wayback Machine snapshot in `source.archive`. The exact quote was found in that snapshot on the claim's `source.accessed` date.
- Podcast speakers are named in the claim. A speaker who is not a Google employee is not evidence about Google, so those claims are `fact`, not `org-fact`.
- `10-36` is about Waze's own message queue in a Workbook case study, so it is `fact`, not `org-fact`. Its archive link is kept.
