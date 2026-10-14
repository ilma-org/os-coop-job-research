---
doc_type: topic-note
topic: 10-server-and-database-software
title: "Message queues, pipelines and operating data services"
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
  - id: 10-30
    claim: "The SRE Workbook says the internals of data storage often have a lowest level of granularity that may become unavailable if accessed heavily; for example, a Spanner tablet can become overloaded due to a problematic section of data even though most of the data storage is fine."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook: Data Processing Pipelines"
      url: https://sre.google/workbook/data-processing/
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260827232609/https://sre.google/workbook/data-processing/
    quote: "Often, the internals of your data storage have a lowest level of granularity that may become unavailable if accessed heavily (e.g., a Spanner tablet can become overloaded due to a problematic section of data even though most of the data storage is fine)."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-server-db-author-check-2.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-10-reviewer-recheck.md
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
  - id: 10-32
    claim: "The SRE Workbook names two main steps in fixing corrupt data: mitigate the impact by preventing further corrupt data from entering the system, and restore the data from a previously known good version or reprocess to repair it."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook: Data Processing Pipelines"
      url: https://sre.google/workbook/data-processing/
      kind: official-doc
      accessed: 2026-10-12
      archive: https://web.archive.org/web/20260827232609/https://sre.google/workbook/data-processing/
    quote: "There are two main steps involved in fixing corrupt data: Mitigate the impact by preventing further corrupt data from entering the system. Restore your data from a previously known good version, or reprocess to repair the data."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-server-db-author-check-2.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-10-reviewer-recheck.md
      result: supported
  - id: 10-34
    claim: "In its AdWords example of non-abstract large system design, the SRE Workbook says to have the replicas of a shared service such as ClickMap use a consensus algorithm such as Paxos, so that the state of the calculations can be reliably stored if a datacenter-sized failure occurs."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, Chapter 12: Introducing Non-Abstract Large System Design"
      url: https://sre.google/workbook/non-abstract-design/
      kind: official-doc
      accessed: 2026-10-07
      archive: null
    quote: "Have the replicas use a consensus algorithm such as Paxos to ensure that we can reliably store the state of the calculations if a datacenter-sized failure occurs."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-nine14282-server-db-author-check-5.md
      result: supported
  - id: 10-35
    claim: "In its AdWords example of non-abstract large system design, the SRE Workbook assumes that executing Paxos with fault-isolated datacenters at least a few hundred kilometers apart takes roughly 25 milliseconds per operation."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, Chapter 12: Introducing Non-Abstract Large System Design"
      url: https://sre.google/workbook/non-abstract-design/
      kind: official-doc
      accessed: 2026-10-07
      archive: null
    quote: "The latency of executing the Paxos algorithm with fault-isolated datacenters means that each operation needs roughly 25 milliseconds to complete. This latency assumption is based upon datacenters at least a few hundred kilometers apart."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-nine14282-server-db-author-check-5.md
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

# Message queues, pipelines and operating data services

## Summary

The SRE Workbook says stale data is almost always better than incorrect data (10-31) and names two main steps in fixing corrupt data: mitigate the impact, then restore or reprocess the data (10-32). On message queues, Building Secure and Reliable Systems says a queue that stores data in volatile memory only can lose transactions (10-29), and a Workbook case study says Waze's message queueing system was critical because every component used it (10-36). Workbook examples and case studies cover a Spanner tablet overloaded by a problematic section of data (10-30), NFS/CIFS degrading over a WAN (10-33) and the cost of running Paxos across datacenters (10-34, 10-35). On the Google SRE Prodcast, Swapnil Haria says there are many ways to do admission control right, FIFO among them (10-28). Each claim rests on one source; no second source was compared, and this note has no claim yet on a specific message queue product such as Kafka or RabbitMQ.

## Key points

- The SRE Workbook says stale data is almost always better than incorrect data (10-31).
- The SRE Workbook names two main steps in fixing corrupt data: stop further corrupt data from entering, then restore from a known good version or reprocess (10-32).
- Building Secure and Reliable Systems says a message queue that stores data in volatile memory only can lose transactions (10-29).
- In its Waze case study, the SRE Workbook says the message queueing system was critical because every component of Waze used it to communicate internally (10-36).
- The SRE Workbook says a lowest level of data storage granularity, such as a Spanner tablet, may become unavailable if accessed heavily (10-30).
- In a case study, the SRE Workbook says NFS/CIFS were never designed to operate over a WAN, so user experience degraded with a few tens of milliseconds of latency (10-33).
- In a design example, the SRE Workbook says replicas can use Paxos to store calculation state reliably (10-34), at roughly 25 milliseconds per operation across fault-isolated datacenters (10-35).
- On the Google SRE Prodcast, Swapnil Haria says there are many ways to do admission control right, FIFO among them (10-28).

Claims are listed newest source first. Each claim's `status` in the front matter says how far it has been checked.

Source years in this note: 2025, 2020, 2018. A year is the publication or last-update year of the source, or the book edition year when the page gives none (SRE book 2016, Workbook 2018, Building Secure and Reliable Systems 2020).

## Claims at a glance

- `10-28` (fact): On the Google SRE Prodcast, Swapnil Haria says there are many ways to do admission control right, FIFO among them.
- `10-29` (fact): Building Secure and Reliable Systems says that if a message queue is not designed to be reliable, for example if it stores data in volatile memory only, you can lose transactions, a new risk surface.
- `10-30` (fact): The SRE Workbook says the internals of data storage often have a lowest level of granularity that may become unavailable if accessed heavily; for example, a Spanner tablet can become overloaded due to a problematic section of data even though most of the data storage is fine.
- `10-31` (fact): The SRE Workbook says stale data is almost always better than incorrect data.
- `10-32` (fact): The SRE Workbook names two main steps in fixing corrupt data: mitigate the impact by preventing further corrupt data from entering the system, and restore the data from a previously known good version or reprocess to repair it.
- `10-33` (fact): In a case study, the SRE Workbook says NFS/CIFS protocols were never designed to operate over a WAN, so user experience rapidly degraded with even a few tens of milliseconds of latency.
- `10-34` (fact): In a design example, the SRE Workbook says to have the replicas use a consensus algorithm such as Paxos so that the state of the calculations can be reliably stored if a datacenter-sized failure occurs.
- `10-35` (fact): In the same design example, the SRE Workbook says executing Paxos with fault-isolated datacenters means each operation needs roughly 25 milliseconds, an assumption based on datacenters at least a few hundred kilometers apart.
- `10-36` (org-fact): In its Waze case study, the SRE Workbook says the message queueing system was critical to operations because every component of Waze used it to communicate with other components internally.

## Notes

- `org-fact` claims carry a Wayback Machine snapshot in `source.archive`. The exact quote was found in that snapshot on the claim's `source.accessed` date.
- Podcast speakers are named in the claim. A speaker who is not a Google employee is not evidence about Google, so those claims are `fact`, not `org-fact`.
- `10-28` is one speaker's view on the Prodcast, not a statement of general SRE practice.
