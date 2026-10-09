---
doc_type: topic-note
topic: 05-hardware-requirements
title: "Machine sizing numbers and hardware for practice"
updated: 2026-10-09
claims:
  - id: 05-18
    claim: "The SRE Workbook's non-abstract large system design (NALSD) example assumes a standard machine footprint of 16 cores, 64 GB of RAM and 1 Gbps of network throughput."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.12 Introducing Non-Abstract Large System Design"
      url: https://sre.google/workbook/non-abstract-design/
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "standard machine footprint of 16 cores, 64 GB RAM, and 1 Gbps network throughput"
    os_concepts: ["memory management"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-19
    claim: "The SRE Workbook says a common 4 TB HDD might sustain about 200 input/output operations per second (IOPS)."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.12 Introducing Non-Abstract Large System Design"
      url: https://sre.google/workbook/non-abstract-design/
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "4 TB HDD might be able to sustain 200 input/output operations per second"
    os_concepts: ["I/O"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-20
    claim: "The SRE Workbook says a single-machine design has single points of failure such as CPU, memory, storage, power, network and cooling."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.12 Introducing Non-Abstract Large System Design"
      url: https://sre.google/workbook/non-abstract-design/
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "single points of failure (e.g., CPU, memory, storage, power, network, cooling)"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-21
    claim: "Recommendation (assumption): for hands-on practice before applying, a personal laptop or desktop with about 8 GB of RAM can run either minikube (05-35) or two or three small Debian virtual machines without a desktop (05-34); 16 GB runs both at once. Server-class hardware is not needed. These RAM figures are this note's estimate from the cited minimums, not a source's recommendation."
    type: assumption
    status: unverified
    os_concepts: ["virtualization", "containers"]
    pr: null
  - id: 05-34
    claim: "Debian's installation guide lists the RAM and disk for an install: without a desktop, 512MB RAM minimum, 1GB recommended and 4GB disk; with a desktop, 1GB RAM minimum, 2GB recommended and 10GB disk."
    type: fact
    status: ai-checked
    source:
      title: "Debian GNU/Linux Installation Guide, 3.4 Meeting Minimum Hardware Requirements"
      url: https://www.debian.org/releases/stable/amd64/ch03s04.en.html
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "No desktop 512MB 1GB 4GB With Desktop 1GB 2GB 10GB"
    os_concepts: ["memory management"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-35
    claim: "The minikube documentation says running local Kubernetes with minikube needs 2 CPUs or more, 2GB of free memory and 20GB of free disk space."
    type: fact
    status: ai-checked
    source:
      title: "minikube documentation, minikube start"
      url: https://minikube.sigs.k8s.io/docs/start/
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "2 CPUs or more 2GB of free memory 20GB of free disk space"
    os_concepts: ["containers", "virtualization"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
---

# Machine sizing numbers and hardware for practice

## Summary

The SRE Workbook's non-abstract large system design (NALSD) exercise sizes a system with a standard machine of 16 cores, 64 GB of RAM and 1 Gbps of network throughput, and a common 4 TB HDD of about 200 IOPS (05-18, 05-19). These numbers are exercise assumptions, not a statement of Google's hardware. The same exercise lists CPU, memory, storage, power, network and cooling as single points of failure of a one-machine design (05-20). For practice hardware, Debian's installation guide recommends 1GB of RAM and 4GB of disk for an install without a desktop, and minikube needs 2 CPUs, 2GB of free memory and 20GB of free disk (05-34, 05-35). The practice-machine recommendation built on those numbers is an assumption (05-21).

## Key points

- NALSD sizing inputs: 16 cores, 64 GB RAM, 1 Gbps per machine; about 200 IOPS per 4 TB HDD. (05-18, 05-19)
- A one-machine design has many single points of failure. (05-20)
- Minimums for practice: a Debian server install without a desktop (512MB RAM minimum, 1GB recommended, 4GB disk) and minikube (2 CPUs, 2GB free memory, 20GB free disk). (05-34, 05-35)
- Recommendation (assumption): about 8 GB of RAM is enough to run minikube or two or three small Debian VMs; 16 GB runs both at once. (05-21)

## Sources and limits

Round 1 used only the three books on https://sre.google/books/. Round 2 adds current official pages: Google Cloud documentation and blog posts, Google's data center site, and, for practice hardware, the Debian installation guide and the minikube documentation. The SRE book page footer says copyright 2017 and the Workbook page footer says copyright 2018; the Building Secure and Reliable Systems pages show no date. Each claim describes what its source says at the time of that source. Quotes are kept short on purpose; open the source to read the full passage.
