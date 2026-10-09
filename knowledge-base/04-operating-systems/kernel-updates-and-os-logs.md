---
doc_type: topic-note
topic: 04-operating-systems
title: "Kernel updates, live patching and OS logs in Google production"
updated: 2026-10-09
claims:
  - id: 04-09
    claim: "Building Secure and Reliable Systems says Google regularly pushes new kernels to its entire fleet of machines."
    type: org-fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.16 Disaster Planning"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch16.html
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260420235255/https://google.github.io/building-secure-and-reliable-systems/raw/ch16.html
    quote: "we regularly push new kernels to the entire fleet of machines"
    os_concepts: ["kernel"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
  - id: 04-10
    claim: "Building Secure and Reliable Systems says Google's fleet-wide kernel rollouts have a target of less than 30 days."
    type: org-fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.16 Disaster Planning"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch16.html
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260420235255/https://google.github.io/building-secure-and-reliable-systems/raw/ch16.html
    quote: "fleet of machines with a target of less than 30 days"
    os_concepts: ["kernel"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
  - id: 04-11
    claim: "Building Secure and Reliable Systems describes ksplice as a runtime kernel patch that uses function redirection tables so that rebooting into a new kernel is unnecessary."
    type: fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.16 Disaster Planning"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch16.html
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "uses function redirection tables to make rebooting a new kernel unnecessary"
    os_concepts: ["kernel"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
  - id: 04-12
    claim: "Building Secure and Reliable Systems says that, for two 2018 Linux kernel vulnerabilities, Google SREs were able to apply a ksplice to production systems."
    type: org-fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.16 Disaster Planning"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch16.html
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260420235255/https://google.github.io/building-secure-and-reliable-systems/raw/ch16.html
    quote: "SREs were able to apply the ksplice to production systems"
    os_concepts: ["kernel"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
  - id: 04-13
    claim: "In its case study of moving Google's Ads Database (MySQL) onto Borg from late 2008, the SRE book says the MySQL instances ran on shared machines that were subject to reboots for kernel upgrades."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.7 The Evolution of Automation at Google"
      url: https://sre.google/sre-book/automation-at-google/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260910213452/https://sre.google/sre-book/automation-at-google/
    quote: "we ran on shared machines and were subject to reboots for kernel upgrades"
    os_concepts: ["kernel"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check-2.md
      result: supported
  - id: 04-14
    claim: "Building Secure and Reliable Systems says Linux and Mac have syslog and auditd logs, while Windows has Windows Event logs."
    type: fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.15 Investigating Systems"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch15.html
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "Windows has Windows Event logs, while Linux and Mac have syslog and auditd logs."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
  - id: 04-43
    claim: "The Linux kernel's livepatch documentation says livepatching redirects function calls so that critical functions can be fixed without a system reboot."
    type: fact
    status: ai-checked
    source:
      title: "The Linux Kernel documentation, Livepatch"
      url: https://docs.kernel.org/livepatch/livepatch.html
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "function calls to be redirected; thus, fixing critical functions without a system reboot"
    os_concepts: ["kernel"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
---

# Kernel updates, live patching and OS logs in Google production

## Summary

Building Secure and Reliable Systems says Google regularly pushes new kernels to its whole fleet, with a target of less than 30 days. It describes ksplice, a runtime kernel patch that avoids a reboot, and says Google SREs applied one to production systems for two 2018 Linux kernel vulnerabilities (04-09 to 04-12). The Linux kernel's own documentation describes livepatching the same way: function calls are redirected so critical functions can be fixed without a reboot (04-43). In its Ads Database case study, the SRE book says MySQL instances on Borg ran on shared machines that were rebooted for kernel upgrades (04-13). For investigations, Linux provides syslog and auditd logs (04-14).

## Key points

- Kernel updates are routine fleet-wide work with a time target. (04-09, 04-10)
- Live patching redirects kernel function calls to fix code without a reboot; Google SREs have used it on production systems. (04-11, 04-12, 04-43)
- Workloads on shared machines must cope with reboots for kernel upgrades, as the Ads Database team found when moving MySQL onto Borg. (04-13)
- Linux keeps syslog and auditd logs; Windows keeps Windows Event logs. (04-14)

## Notes for the write-up

- Building Secure and Reliable Systems does not say whether its "ksplice" is the Oracle Ksplice product. Call it runtime kernel patching (live patching), not a named product.
- 04-14 is a general statement about operating systems. No source says which logging tools Google uses on its servers.

## Sources and limits

Round 1 used only the three books on https://sre.google/books/. Round 2 adds official Google pages (Google Cloud documentation and the Google Cloud Blog), the Linux kernel documentation, the gVisor documentation and one USENIX paper by a Google engineer. The SRE book page footer says copyright 2017 and the Workbook page footer says copyright 2018; the Building Secure and Reliable Systems pages show no date. Each claim describes what its source says at the time of that source, not necessarily current practice. Quotes are kept short on purpose; open the source to read the full passage.
