---
doc_type: topic-note
topic: 10-server-and-database-software
title: "Storage and database systems: GFS, Colossus, Spanner and caches"
updated: 2026-10-14
claims:
  - id: 10-10
    claim: "On the Google SRE Prodcast, Silvia Botros describes a culture shift in database engineering away from relying on one DBA, and says it is more about predicting failure and planning accordingly, so you don't want a single database failure to take down your whole product."
    type: fact
    status: ai-checked
    source:
      title: "Google SRE Prodcast transcript: Building Reliable Systems"
      url: https://sre.google/prodcast/transcripts/sre-prodcast-03-05/
      kind: other
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260306061753/https://sre.google/prodcast/transcripts/sre-prodcast-03-05/
    quote: "And it's more about you predict failure, and you plan accordingly. And therefore, you don't want a single database failure to take down your whole product."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-nine14282-server-db-author-check-5.md
      result: supported
  - id: 10-11
    claim: "In a section headed \"Example: Temporary Files\", Building Secure and Reliable Systems says that, according to normal behavior, a Spanner server buffered recent writes in memory and, as it ran low on memory, flushed the data to files on Colossus."
    type: org-fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, Chapter 15: Investigating Systems"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch15.html
      kind: official-doc
      accessed: 2026-10-12
      archive: https://web.archive.org/web/20260616012631/https://google.github.io/building-secure-and-reliable-systems/raw/ch15.html
    quote: "According to normal behavior, recent writes (updates) were buffered in memory; as the server ran low on memory, it flushed the data to files on Colossus."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-nine14282-server-db-author-check-4.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-10-reviewer-recheck.md
      result: supported
  - id: 10-12
    claim: "The report Case Studies in Infrastructure Change Management says GFS was designed in 2001 as Google's first cluster-level file system, supported many petabytes of storage and allowed thousands of servers to interact with thousands of clients."
    type: org-fact
    status: ai-checked
    source:
      title: "Case Studies in Infrastructure Change Management: How Google Rebuilds the Jet While Flying It (O'Reilly/Google report)"
      url: https://sre.google/static/pdf/CaseStudiesInfrastructureChangeManagement.pdf
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260219151023/https://sre.google/static/pdf/CaseStudiesInfrastructureChangeManagement.pdf
    quote: "GFS was designed in 2001 as Google’s first cluster-level file system. It supported many petabytes of storage and allowed thousands of servers to interact with thousands of clients."
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
  - id: 10-13
    claim: "The report Case Studies in Infrastructure Change Management says that in GFS, machines ran a daemon called a chunkserver to store chunks on the local filesystem, while the GFS client code split files into chunks, stored them on chunkservers and replicated them to other chunkservers for redundancy and bandwidth."
    type: org-fact
    status: ai-checked
    source:
      title: "Case Studies in Infrastructure Change Management: How Google Rebuilds the Jet While Flying It (O'Reilly/Google report)"
      url: https://sre.google/static/pdf/CaseStudiesInfrastructureChangeManagement.pdf
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260219151023/https://sre.google/static/pdf/CaseStudiesInfrastructureChangeManagement.pdf
    quote: "Machines would run a daemon called a chunkserver to store blocks of data (chunks) on the local filesystem while the GFS client code split the files into a series of chunks and stored them on the chunkservers, replicating the chunks to other chunkservers for redundancy and bandwidth."
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
  - id: 10-14
    claim: "The report Case Studies in Infrastructure Change Management says that in Colossus, the D server managed access to the raw data while Colossus managed the map of what data was on which D server."
    type: org-fact
    status: ai-checked
    source:
      title: "Case Studies in Infrastructure Change Management: How Google Rebuilds the Jet While Flying It (O'Reilly/Google report)"
      url: https://sre.google/static/pdf/CaseStudiesInfrastructureChangeManagement.pdf
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260219151023/https://sre.google/static/pdf/CaseStudiesInfrastructureChangeManagement.pdf
    quote: "Similar to how a GFS chunkserver managed reading and writing the raw chunk data while the GFS Master kept track of the filesystem metadata, the D server managed access to the raw data while Colossus managed the map of what data was on which D server."
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
  - id: 10-15
    claim: "The report Creating a Production Launch Plan gives as an example that if a relational database has an upper limit on transaction throughput, there is only so much scaling you can get by adding more CPU or memory, which doesn't scale horizontally."
    type: fact
    status: ai-checked
    source:
      title: "Creating a Production Launch Plan: For a Successful Launch, Planning Isn't Optional (O'Reilly/Google report)"
      url: https://sre.google/static/pdf/CreatingProductionLaunchPlan.pdf
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260306001135/https://sre.google/static/pdf/CreatingProductionLaunchPlan.pdf
    quote: "For example, if a relational database has an upper limit on transaction throughput, there’s only so much scaling you can accomplish by adding more CPU or memory, which doesn’t scale horizontally."
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
  - id: 10-16
    claim: "The report Creating a Production Launch Plan says a product may require significantly more resources when operating on a cold cache; in its video example, if pointers to stored videos are lost when the cache clears, all video view requests start going to the video metadata service."
    type: fact
    status: ai-checked
    source:
      title: "Creating a Production Launch Plan: For a Successful Launch, Planning Isn't Optional (O'Reilly/Google report)"
      url: https://sre.google/static/pdf/CreatingProductionLaunchPlan.pdf
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260306001135/https://sre.google/static/pdf/CreatingProductionLaunchPlan.pdf
    quote: "Similarly, a product may require significantly more resources when operating on a cold cache. If pointers to stored videos are lost when the cache clears, all video view requests start going to the video metadata service."
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
  - id: 10-17
    claim: "The SRE book says caches are sometimes added to a service to improve performance but actually wind up being hard dependencies."
    type: fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering (SRE book) - Addressing Cascading Failures"
      url: https://sre.google/sre-book/addressing-cascading-failures/
      kind: official-doc
      accessed: 2026-10-07
      archive: null
    quote: "Sometimes caches are added to a service to improve performance, but actually wind up being hard dependencies."
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
  - id: 10-18
    claim: "The SRE book says it may be worthwhile to move caching from a server to a separate binary like memcache, which also allows cache sharing between many servers, at the cost of introducing another RPC and slight additional latency."
    type: fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering (SRE book) - Addressing Cascading Failures"
      url: https://sre.google/sre-book/addressing-cascading-failures/
      kind: official-doc
      accessed: 2026-10-07
      archive: null
    quote: "It may be worthwhile to move caching from a server to a separate binary like memcache, which also allows cache sharing between many servers, albeit at the cost of introducing another RPC and slight additional latency."
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
---

# Storage and database systems: GFS, Colossus, Spanner and caches

## Summary

The report Case Studies in Infrastructure Change Management describes GFS, designed in 2001 as Google's first cluster-level file system, with chunkservers storing replicated chunks (10-12, 10-13), and Colossus, where D servers managed access to the raw data (10-14). In an outage example headed "Example: Temporary Files", Building Secure and Reliable Systems says a Spanner server flushed buffered writes to files on Colossus when it ran low on memory (10-11), and the SRE Workbook says a lowest level of storage granularity, such as a Spanner tablet, may become unavailable if accessed heavily (10-30). The report Creating a Production Launch Plan gives examples of a relational database with a transaction throughput limit that adding CPU or memory can scale only so far (10-15) and of a cold cache that sends all video view requests to a metadata service (10-16), and the SRE book says caches sometimes become hard dependencies and that moving them to a separate binary like memcache may be worthwhile (10-17, 10-18). On the Google SRE Prodcast, describing a culture shift away from relying on one DBA, Silvia Botros says you don't want a single database failure to take down your whole product (10-10). Each claim rests on one source; no second source was compared, and this note has no claim yet on operating MySQL, PostgreSQL, MongoDB, Redis or Bigtable.

## Key points

- The report Case Studies in Infrastructure Change Management says GFS was designed in 2001 as Google's first cluster-level file system (10-12).
- The same report says GFS chunkservers stored chunks on the local filesystem, and the client code replicated chunks to other chunkservers (10-13).
- The same report says that in Colossus the D server managed access to the raw data, while Colossus managed the map of which data was on which D server (10-14).
- In an outage example headed "Example: Temporary Files", Building Secure and Reliable Systems says a Spanner server buffered recent writes in memory and flushed them to files on Colossus when it ran low on memory (10-11).
- The SRE Workbook says a lowest level of data storage granularity, such as a Spanner tablet, may become unavailable if accessed heavily (10-30).
- The report Creating a Production Launch Plan gives as an example that a relational database with an upper limit on transaction throughput can be scaled only so far by adding CPU or memory (10-15).
- The same report says a product may need significantly more resources on a cold cache (10-16).
- The SRE book says caches are sometimes added for performance but wind up being hard dependencies (10-17), and that moving caching to a separate binary like memcache may be worthwhile (10-18).
- On the Google SRE Prodcast, describing a culture shift away from relying on one DBA, Silvia Botros says you don't want a single database failure to take down your whole product (10-10).

Claims are listed newest source first. Each claim's `status` in the front matter says how far it has been checked.

Source years in this note: 2024, 2020, 2019, 2018, 2016. A year is the publication or last-update year of the source, or the book edition year when the page gives none (SRE book 2016, Workbook 2018, Building Secure and Reliable Systems 2020).

## Claims at a glance

- `10-10` (fact): On the Google SRE Prodcast, Silvia Botros describes a culture shift in database engineering away from relying on one DBA, and says it is more about predicting failure and planning accordingly, so you don't want a single database failure to take down your whole product.
- `10-11` (org-fact): In a section headed "Example: Temporary Files", Building Secure and Reliable Systems says that, according to normal behavior, a Spanner server buffered recent writes in memory and, as it ran low on memory, flushed the data to files on Colossus.
- `10-12` (org-fact): The report Case Studies in Infrastructure Change Management says GFS was designed in 2001 as Google's first cluster-level file system, supported many petabytes of storage and allowed thousands of servers to interact with thousands of clients.
- `10-13` (org-fact): The report Case Studies in Infrastructure Change Management says that in GFS, machines ran a daemon called a chunkserver to store chunks on the local filesystem, while the GFS client code split files into chunks, stored them on chunkservers and replicated them to other chunkservers for redundancy and bandwidth.
- `10-14` (org-fact): The report Case Studies in Infrastructure Change Management says that in Colossus, the D server managed access to the raw data while Colossus managed the map of what data was on which D server.
- `10-15` (fact): The report Creating a Production Launch Plan gives as an example that if a relational database has an upper limit on transaction throughput, there is only so much scaling you can get by adding more CPU or memory, which doesn't scale horizontally.
- `10-16` (fact): The report Creating a Production Launch Plan says a product may require significantly more resources when operating on a cold cache; in its video example, if pointers to stored videos are lost when the cache clears, all video view requests start going to the video metadata service.
- `10-17` (fact): The SRE book says caches are sometimes added to a service to improve performance but actually wind up being hard dependencies.
- `10-18` (fact): The SRE book says it may be worthwhile to move caching from a server to a separate binary like memcache, which also allows cache sharing between many servers, at the cost of introducing another RPC and slight additional latency.
- `10-30` (fact): The SRE Workbook says the internals of data storage often have a lowest level of granularity that may become unavailable if accessed heavily; for example, a Spanner tablet can become overloaded due to a problematic section of data even though most of the data storage is fine.

## Notes

- `org-fact` claims carry a Wayback Machine snapshot in `source.archive`. The exact quote was found in that snapshot on the claim's `source.accessed` date.
- Podcast speakers are named in the claim. A speaker who is not a Google employee is not evidence about Google, so those claims are `fact`, not `org-fact`.
- `10-10` is one speaker's view on the Prodcast, not a statement of general SRE practice.
