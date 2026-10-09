---
doc_type: topic-note
topic: 05-hardware-requirements
title: "CPU platforms and accelerators on Google Cloud"
updated: 2026-10-09
claims:
  - id: 05-27
    claim: "Compute Engine's CPU platform documentation lists Google Axion processors, with Arm Neoverse V2 (Armv9) cores, among its Arm CPU platforms."
    type: org-fact
    status: ai-checked
    source:
      title: "Compute Engine documentation, CPU platforms"
      url: https://docs.cloud.google.com/compute/docs/cpu-platforms
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20261005183839/https://docs.cloud.google.com/compute/docs/cpu-platforms
    quote: "Google Axion Processors with Neoverse V2 Armv9 cores"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-28
    claim: "Compute Engine documentation says that for most x86 processors, each vCPU is implemented as a single hardware thread."
    type: org-fact
    status: ai-checked
    source:
      title: "Compute Engine documentation, CPU platforms"
      url: https://docs.cloud.google.com/compute/docs/cpu-platforms
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20261005183839/https://docs.cloud.google.com/compute/docs/cpu-platforms
    quote: "For most x86 processors, each vCPU is implemented as a single hardware thread."
    os_concepts: ["threads"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-29
    claim: "Compute Engine documentation says that for Arm processors it uses one thread per core, so each vCPU maps to a physical core with no simultaneous multithreading (SMT)."
    type: org-fact
    status: ai-checked
    source:
      title: "Compute Engine documentation, CPU platforms"
      url: https://docs.cloud.google.com/compute/docs/cpu-platforms
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20261005183839/https://docs.cloud.google.com/compute/docs/cpu-platforms
    quote: "Each vCPU maps to a physical core with no SMT"
    os_concepts: ["threads"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-30
    claim: "Compute Engine documentation says some machine types can run on more than one CPU platform."
    type: org-fact
    status: ai-checked
    source:
      title: "Compute Engine documentation, CPU platforms"
      url: https://docs.cloud.google.com/compute/docs/cpu-platforms
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20261005183839/https://docs.cloud.google.com/compute/docs/cpu-platforms
    quote: "Some machine types can run on more than one CPU platform."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-31
    claim: "Compute Engine documentation says you can see an instance's CPU platform by connecting to the guest OS and running the lscpu command."
    type: org-fact
    status: ai-checked
    source:
      title: "Compute Engine documentation, CPU platforms"
      url: https://docs.cloud.google.com/compute/docs/cpu-platforms
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20261005183839/https://docs.cloud.google.com/compute/docs/cpu-platforms
    quote: "connect to the guest OS and use the lscpu command"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-32
    claim: "Cloud TPU documentation says Tensor Processing Units (TPUs) are Google's custom-developed application-specific integrated circuits (ASICs) used to accelerate machine learning workloads."
    type: org-fact
    status: ai-checked
    source:
      title: "Cloud TPU documentation, Introduction to Cloud TPU"
      url: https://docs.cloud.google.com/tpu/docs/intro-to-tpu
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20261001134707/https://docs.cloud.google.com/tpu/docs/intro-to-tpu
    quote: "Google's custom-developed, application-specific integrated circuits (ASICs) used to accelerate machine learning"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check-2.md
      result: supported
  - id: 05-33
    claim: "Compute Engine documentation describes NVIDIA GPU models that can accelerate machine learning (ML) and data processing on Compute Engine instances."
    type: org-fact
    status: ai-checked
    source:
      title: "Compute Engine documentation, GPU machine types"
      url: https://docs.cloud.google.com/compute/docs/gpus
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260927102828/https://docs.cloud.google.com/compute/docs/gpus
    quote: "NVIDIA GPU models that you can use to accelerate machine learning (ML), data processing"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check-2.md
      result: supported
---

# CPU platforms and accelerators on Google Cloud

## Summary

Compute Engine documentation lists Google's own Arm processor, Axion, among its CPU platforms (05-27). On most x86 processors each vCPU is one hardware thread, while on Arm each vCPU maps to a physical core with no simultaneous multithreading (05-28, 05-29). Some machine types can run on more than one CPU platform, and the guest OS shows which one with the lscpu command (05-30, 05-31). For accelerators, Google offers its custom TPU chips for machine learning and NVIDIA GPUs (05-32, 05-33). These claims describe Google Cloud instances for customers, not Google's internal production machines.

## Key points

- CPU architectures on Google Cloud include Arm, among them Google's own Axion processors. (05-27)
- A vCPU is a hardware thread on most x86 processors and a full physical core on Arm. (05-28, 05-29)
- One machine type can run on more than one CPU platform; lscpu in the guest OS shows the platform. (05-30, 05-31)
- Accelerators: Google-designed TPUs (ASICs for machine learning) and NVIDIA GPUs. (05-32, 05-33)

## Notes for the write-up

- Use this note for the hardware an SRE meets on Google Cloud. Do not use it to describe the CPUs or accelerators inside Google's own production fleet; no opened source does that.

## Sources and limits

Round 1 used only the three books on https://sre.google/books/. Round 2 adds current official pages: Google Cloud documentation and blog posts, Google's data center site, and, for practice hardware, the Debian installation guide and the minikube documentation. The SRE book page footer says copyright 2017 and the Workbook page footer says copyright 2018; the Building Secure and Reliable Systems pages show no date. Each claim describes what its source says at the time of that source. Quotes are kept short on purpose; open the source to read the full passage.
