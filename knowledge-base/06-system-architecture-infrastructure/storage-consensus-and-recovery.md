---
doc_type: topic-note
topic: 06-system-architecture-infrastructure
title: "Distributed storage, consensus, backups and disaster recovery"
updated: 2026-10-09
claims:
  - id: 06-16
    claim: "The SRE book says Colossus creates a cluster-wide filesystem with usual filesystem semantics, plus replication and encryption."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "a cluster-wide filesystem that offers usual filesystem semantics, as well as replication and encryption"
    os_concepts: ["file systems"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-17
    claim: "The SRE book describes Bigtable as a NoSQL database system that can handle databases that are petabytes in size."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "a NoSQL database system that can handle databases that are petabytes in size"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-18
    claim: "The SRE book says Spanner offers an SQL-like interface for users that require real consistency across the world."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "offers an SQL-like interface for users that require real consistency across the world"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-19
    claim: "The SRE book says the Chubby lock service handles locks across datacenter locations and uses the Paxos protocol for asynchronous consensus."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "handles these locks across datacenter locations. It uses the Paxos protocol for asynchronous Consensus"
    os_concepts: ["synchronization"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-20
    claim: "The SRE book defines a failure domain as the set of components of a system that can become unavailable as a result of a single failure."
    type: fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.23 Managing Critical State: Distributed Consensus for Reliability"
      url: https://sre.google/sre-book/managing-critical-state/
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "failure domain is the set of components of a system that can become unavailable"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-21
    claim: "The SRE book says the most important difference between backups and archives is that backups can be loaded back into an application, while archives cannot."
    type: fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.26 Data Integrity: What You Read Is What You Wrote"
      url: https://sre.google/sre-book/data-integrity/
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "backups can be loaded back into an application, while archives cannot"
    os_concepts: ["file systems"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-22
    claim: "The SRE book warns that replication and redundancy are not recoverability."
    type: fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.26 Data Integrity: What You Read Is What You Wrote"
      url: https://sre.google/sre-book/data-integrity/
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "replication and redundancy are not recoverability"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-23
    claim: "The SRE book says Google recovered lost Gmail data in 2011 from its previously undisclosed tape backup system."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.26 Data Integrity: What You Read Is What You Wrote"
      url: https://sre.google/sre-book/data-integrity/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20261001045117/https://sre.google/sre-book/data-integrity/
    quote: "recovered this data from our previously undisclosed tape backup system"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-24
    claim: "Building Secure and Reliable Systems says Google runs annual Disaster Recovery Training (DiRT) exercises."
    type: org-fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.16 Disaster Planning"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch16.html
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260420235255/https://google.github.io/building-secure-and-reliable-systems/raw/ch16.html
    quote: "one of our annual Disaster Recovery Training (DiRT) exercises"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-25
    claim: "In its case study on decommissioning Google's filer-backed home directories, the SRE Workbook says the data was owned by 60,000 POSIX users in 400 disk volumes on 124 NAS appliances."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.6 Eliminating Toil"
      url: https://sre.google/workbook/eliminating-toil/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260909103330/https://sre.google/workbook/eliminating-toil/
    quote: "owned by 60,000 POSIX users in 400 disk volumes on 124 NAS appliances"
    os_concepts: ["file systems"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
---

# Distributed storage, consensus, backups and disaster recovery

## Summary

The SRE book describes Google's storage stack: Colossus as a cluster-wide filesystem with replication and encryption, Bigtable as a NoSQL store for petabyte-size databases, and Spanner for an SQL-like interface with real consistency across the world (06-16 to 06-18). The Chubby lock service handles locks across datacenters using the Paxos protocol (06-19). The SRE Workbook also shows classic network-attached storage: Google's filer-backed home directories, which it decommissioned, sat on 124 NAS appliances (06-25). For recovery, the book defines failure domains, separates backups from archives, warns that replication and redundancy are not recoverability, and recounts restoring Gmail data from tape; Building Secure and Reliable Systems adds Google's annual DiRT exercises (06-20 to 06-24).

## Key points

- Storage layers: Colossus (filesystem), Bigtable (NoSQL), Spanner (globally consistent, SQL-like). (06-16, 06-17, 06-18)
- Coordination: Chubby locks with Paxos consensus. (06-19)
- Network-attached storage: filer-backed home directories for 60,000 POSIX users on 124 NAS appliances, in a decommissioning case study. (06-25)
- Failure domains decide what a single failure can take down. (06-20)
- Backups can be restored into an application, archives cannot, and replication alone is not recovery. (06-21, 06-22)
- Google restored Gmail data from tape backups and runs annual disaster recovery exercises. (06-23, 06-24)

## Sources and limits

Round 1 uses only the three books on https://sre.google/books/. The SRE book page footer says copyright 2017 and the Workbook page footer says copyright 2018. The Building Secure and Reliable Systems pages show no date. Claims about Google describe what the books say, not current practice. Quotes are kept short on purpose; open the source to read the full passage.
