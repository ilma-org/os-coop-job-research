---
doc_type: topic-note
topic: 10-server-and-database-software
title: "Replication, consensus, backups and data integrity"
updated: 2026-10-14
claims:
  - id: 10-20
    claim: "The report Creating a Production Launch Plan says a product should have backups, its teams should have experience recovering the data fully, and data corruption risks, especially ones that can go unnoticed, must be added to the Risks and Mitigations table."
    type: fact
    status: ai-checked
    source:
      title: "Creating a Production Launch Plan: For a Successful Launch, Planning Isn't Optional (O'Reilly/Google report)"
      url: https://sre.google/static/pdf/CreatingProductionLaunchPlan.pdf
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260306001135/https://sre.google/static/pdf/CreatingProductionLaunchPlan.pdf
    quote: "The product should have backups, and the teams should have experience recovering the data fully. Data corruption risks, especially if they can go unnoticed, must be added to your Risks and Mitigations table."
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
  - id: 10-21
    claim: "The SRE book says a study of 19 data recovery efforts at Google found that the most common user-visible data loss scenarios involved data deletion or loss of referential integrity caused by software bugs."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering (SRE book) - Data Integrity: What You Read Is What You Wrote"
      url: https://sre.google/sre-book/data-integrity/
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20261001045117/https://sre.google/sre-book/data-integrity/
    quote: "A study of 19 data recovery efforts at Google found that the most common user-visible data loss scenarios involved data deletion or loss of referential integrity caused by software bugs."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-server-db-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-10-reviewer-recheck.md
      result: supported
  - id: 10-22
    claim: "The SRE book says SRE makes sure global Chubby meets, but does not significantly exceed, its service level objective: in any quarter where a true failure has not dropped availability below the target, a controlled outage is synthesized by intentionally taking down the system."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering (SRE Book) - Service Level Objectives"
      url: https://sre.google/sre-book/service-level-objectives/
      kind: official-doc
      accessed: 2026-10-12
      archive: https://web.archive.org/web/20260930004440/https://sre.google/sre-book/service-level-objectives/
    quote: "SRE makes sure that global Chubby meets, but does not significantly exceed, its service level objective. In any given quarter, if a true failure has not dropped availability below the target, a controlled outage will be synthesized by intentionally taking down the system."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-server-db-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-10-reviewer-recheck.md
      result: supported
  - id: 10-23
    claim: "The SRE book says that in its replicated cron service, as long as the majority of group members are available, the distributed system as a whole can process new state changes despite the failure of bounded subsets of the infrastructure."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering (SRE book) - Distributed Periodic Scheduling with Cron"
      url: https://sre.google/sre-book/distributed-periodic-scheduling/
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260928184306/https://sre.google/sre-book/distributed-periodic-scheduling/
    quote: "As long as the majority of group members are available, the distributed system as a whole can successfully process new state changes despite the failure of bounded subsets of the infrastructure."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-server-db-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-10-reviewer-recheck.md
      result: supported
  - id: 10-24
    claim: "The SRE book says its distributed cron stores snapshots on local disk and, because they are critical, also backs them up onto a distributed filesystem, protecting against failures affecting all three machines."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering (SRE book) - Distributed Periodic Scheduling with Cron"
      url: https://sre.google/sre-book/distributed-periodic-scheduling/
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260928184306/https://sre.google/sre-book/distributed-periodic-scheduling/
    quote: "We store the snapshots on local disk as well. However, because they are critical, we also back them up onto a distributed filesystem, thus protecting against failures affecting all three machines."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-server-db-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-10-reviewer-recheck.md
      result: supported
  - id: 10-25
    claim: "The SRE book says the real focus of backup efforts should be data recovery, which distinguishes real backups from archives, and notes that, as is sometimes observed, no one really wants to make backups; what people really want are restores."
    type: fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering (SRE book) - Data Integrity: What You Read Is What You Wrote"
      url: https://sre.google/sre-book/data-integrity/
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20261001045117/https://sre.google/sre-book/data-integrity/
    quote: "However, the real focus of such backup efforts should be data recovery, which distinguishes real backups from archives. As is sometimes observed: No one really wants to make backups; what people really want are restores."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-server-db-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-10-reviewer-recheck.md
      result: supported
  - id: 10-27
    claim: "The SRE book recommends using distributed consensus systems that have been formally proven and tested thoroughly whenever you see leader election, critical shared state or distributed locking."
    type: fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering (SRE Book) - Managing Critical State: Distributed Consensus for Reliability"
      url: https://sre.google/sre-book/managing-critical-state/
      kind: official-doc
      accessed: 2026-10-07
      archive: null
    quote: "Whenever you see leader election, critical shared state, or distributed locking, we recommend using distributed consensus systems that have been formally proven and tested thoroughly."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-server-db-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-10-reviewer-recheck.md
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
---

# Replication, consensus, backups and data integrity

## Summary

The SRE book says the focus of backups should be data recovery (10-25) and that replication and redundancy are not recoverability (10-26), and a Google SRE prodverb says backups are only as good as the last restore (10-19). The SRE book says a study of 19 data recovery efforts at Google found the most common user-visible data loss came from data deletion or loss of referential integrity caused by software bugs (10-21), and the report Creating a Production Launch Plan says a product should have backups and teams experienced in recovering the data (10-20). On consensus, the SRE book recommends formally proven, thoroughly tested distributed consensus systems for leader election, critical shared state and distributed locking (10-27), and describes a replicated cron service that keeps working while a majority is available and backs up its snapshots (10-23, 10-24). The SRE book also says SRE takes global Chubby down on purpose in a quarter where a true failure has not dropped availability below its target (10-22). Each claim rests on one source; no second source was compared, and most claims come from the 2016 SRE book.

## Key points

- The SRE book says the real focus of backup efforts should be data recovery, and notes that, as is sometimes observed, what people really want are restores (10-25).
- The SRE book says replication and redundancy are not recoverability (10-26).
- A Google SRE prodverb says backups are only as good as the last restore (10-19).
- The SRE book says the most common user-visible data loss in a study of 19 Google data recovery efforts involved data deletion or loss of referential integrity caused by software bugs (10-21).
- The report Creating a Production Launch Plan says a product should have backups, teams experienced in recovering the data, and data corruption risks listed in its Risks and Mitigations table (10-20).
- The SRE book recommends formally proven, thoroughly tested distributed consensus systems for leader election, critical shared state or distributed locking (10-27).
- The SRE book says its replicated cron service can process state changes while a majority of group members is available (10-23), and backs its snapshots up onto a distributed filesystem (10-24).
- The SRE book says SRE synthesizes a controlled outage of global Chubby in a quarter where a true failure has not dropped availability below the target (10-22).

Claims are listed newest source first. Each claim's `status` in the front matter says how far it has been checked.

Source years in this note: 2025, 2019, 2016. A year is the publication or last-update year of the source, or the book edition year when the page gives none (SRE book 2016, Workbook 2018, Building Secure and Reliable Systems 2020).

## Claims at a glance

- `10-19` (fact): A Google SRE prodverb says backups are only as good as the last restore.
- `10-20` (fact): The report Creating a Production Launch Plan says a product should have backups, its teams should have experience recovering the data fully, and data corruption risks, especially ones that can go unnoticed, must be added to the Risks and Mitigations table.
- `10-21` (org-fact): The SRE book says a study of 19 data recovery efforts at Google found that the most common user-visible data loss scenarios involved data deletion or loss of referential integrity caused by software bugs.
- `10-22` (org-fact): The SRE book says SRE makes sure global Chubby meets, but does not significantly exceed, its service level objective: in any quarter where a true failure has not dropped availability below the target, a controlled outage is synthesized by intentionally taking down the system.
- `10-23` (org-fact): The SRE book says that in its replicated cron service, as long as the majority of group members are available, the distributed system as a whole can process new state changes despite the failure of bounded subsets of the infrastructure.
- `10-24` (org-fact): The SRE book says its distributed cron stores snapshots on local disk and, because they are critical, also backs them up onto a distributed filesystem, protecting against failures affecting all three machines.
- `10-25` (fact): The SRE book says the real focus of backup efforts should be data recovery, which distinguishes real backups from archives, and notes that, as is sometimes observed, no one really wants to make backups; what people really want are restores.
- `10-26` (fact): The SRE book says that in designing a data integrity program, it's important to recognize that replication and redundancy are not recoverability.
- `10-27` (fact): The SRE book recommends using distributed consensus systems that have been formally proven and tested thoroughly whenever you see leader election, critical shared state or distributed locking.

## Notes

- `org-fact` claims carry a Wayback Machine snapshot in `source.archive`. The exact quote was found in that snapshot on the claim's `source.accessed` date.
- Podcast speakers are named in the claim. A speaker who is not a Google employee is not evidence about Google, so those claims are `fact`, not `org-fact`.
