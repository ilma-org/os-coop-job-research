---
doc_type: topic-note
topic: 04-operating-systems
title: "Container-Optimized OS on Google Cloud"
updated: 2026-10-09
claims:
  - id: 04-52
    claim: "Google Cloud documentation says Container-Optimized OS is maintained by Google and based on the open source Chromium OS project."
    type: org-fact
    status: ai-checked
    source:
      title: "Container-Optimized OS documentation, Container-Optimized OS Overview"
      url: https://cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20250903063505/https://cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits
    quote: "is maintained by Google and based on the open source Chromium OS project"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
  - id: 04-53
    claim: "Google Cloud documentation says Container-Optimized OS is the default node OS image in Google Kubernetes Engine."
    type: org-fact
    status: ai-checked
    source:
      title: "Container-Optimized OS documentation, Container-Optimized OS Overview"
      url: https://cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20250903063505/https://cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits
    quote: "Container-Optimized OS is the default node OS Image in Kubernetes Engine"
    os_concepts: ["containers"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
  - id: 04-54
    claim: "Google Cloud documentation says Container-Optimized OS instances automatically download weekly updates in the background and need only a reboot to use them."
    type: org-fact
    status: ai-checked
    source:
      title: "Container-Optimized OS documentation, Container-Optimized OS Overview"
      url: https://cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20250903063505/https://cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits
    quote: "configured to automatically download weekly updates in the background; only a reboot is necessary"
    os_concepts: ["booting"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
  - id: 04-55
    claim: "Google Cloud documentation says the Container-Optimized OS kernel is locked down, so third-party kernel modules or drivers cannot be installed."
    type: org-fact
    status: ai-checked
    source:
      title: "Container-Optimized OS documentation, Container-Optimized OS Overview"
      url: https://cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20250903063505/https://cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits
    quote: "kernel is locked down; you'll be unable to install third-party kernel modules or drivers"
    os_concepts: ["kernel", "security"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
---

# Container-Optimized OS on Google Cloud

## Summary

Google Cloud documentation says Container-Optimized OS is maintained by Google, is based on the open source Chromium OS project, and is the default node OS image in Google Kubernetes Engine (04-52, 04-53). Its instances download weekly updates automatically and need only a reboot to apply them, and its kernel is locked down so third-party kernel modules and drivers cannot be installed (04-54, 04-55). These claims describe a Google Cloud product for customers, not the operating system on Google's internal production machines.

## Key points

- Container-Optimized OS: maintained by Google, based on Chromium OS, default node image in GKE. (04-52, 04-53)
- Operation: automatic weekly updates applied by a reboot; locked-down kernel with no third-party modules or drivers. (04-54, 04-55)

## Notes for the write-up

- Use this note for the Google Cloud side of an SRE's environment (GKE nodes). Do not use it as evidence about Google's internal servers; see linux-in-google-production.md for those.

## Sources and limits

Round 1 used only the three books on https://sre.google/books/. Round 2 adds official Google pages (Google Cloud documentation and the Google Cloud Blog), the Linux kernel documentation, the gVisor documentation and one USENIX paper by a Google engineer. The SRE book page footer says copyright 2017 and the Workbook page footer says copyright 2018; the Building Secure and Reliable Systems pages show no date. Each claim describes what its source says at the time of that source, not necessarily current practice. Quotes are kept short on purpose; open the source to read the full passage.
