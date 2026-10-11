---
doc_type: topic-note
topic: 11-os-course-concepts
title: "Virtualization, containers and resource isolation for SRE"
updated: 2026-10-10
claims:
  - id: 11-16
    claim: "Linux namespaces can be used to implement containers."
    type: fact
    status: ai-checked
    source:
      title: "Linux man-pages: namespaces(7)"
      url: https://man7.org/linux/man-pages/man7/namespaces.7.html
      kind: official-doc
      accessed: 2026-10-10
      archive: null
    quote: "One use of namespaces is to implement containers."
    os_concepts: ["namespaces", "containers", "resource isolation"]
    pr: null
    ai_check:
      platform: Codex
      model: "gpt-6.1-sol"
      prompt_log: prompts/2026-10-10-TonCS05-11-author-check.md
      result: supported
  - id: 11-17
    claim: "Linux cgroups organize processes hierarchically and distribute system resources through that hierarchy in a controlled, configurable manner."
    type: fact
    status: ai-checked
    source:
      title: "Linux Kernel documentation: Control Group v2"
      url: https://docs.kernel.org/admin-guide/cgroup-v2.html
      kind: official-doc
      accessed: 2026-10-10
      archive: null
    quote: "cgroup is a mechanism to organize processes hierarchically and distribute system resources along the hierarchy in a controlled and configurable manner."
    os_concepts: ["cgroups", "processes", "resource management"]
    pr: null
    ai_check:
      platform: Codex
      model: "gpt-6.1-sol"
      prompt_log: prompts/2026-10-10-TonCS05-11-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-11-reviewer-recheck.md
      result: supported
  - id: 11-18
    claim: "Docker's introductory explanation describes multiple containers as sharing the same kernel."
    type: fact
    status: ai-checked
    source:
      title: "Docker Docs: What is a container?"
      url: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/
      kind: official-doc
      accessed: 2026-10-10
      archive: null
    quote: "If you run multiple containers, they all share the same kernel, allowing you to run more applications on less infrastructure."
    os_concepts: ["containers", "kernel", "resource isolation"]
    pr: null
    ai_check:
      platform: Codex
      model: "gpt-6.1-sol"
      prompt_log: prompts/2026-10-10-TonCS05-11-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-11-reviewer-recheck.md
      result: supported
  - id: 11-19
    claim: "Kubernetes CPU limits are enforced through CPU throttling."
    type: fact
    status: ai-checked
    source:
      title: "Kubernetes documentation: Resource Management for Pods and Containers"
      url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
      kind: official-doc
      accessed: 2026-10-10
      archive: null
    quote: "cpu limits are enforced by CPU throttling."
    os_concepts: ["CPU scheduling", "resource limits", "containers"]
    pr: null
    ai_check:
      platform: Codex
      model: "gpt-6.1-sol"
      prompt_log: prompts/2026-10-10-TonCS05-11-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-11-reviewer-recheck.md
      result: supported
  - id: 11-20
    claim: "Kubernetes memory limits are enforced by the kernel through out-of-memory kills."
    type: fact
    status: ai-checked
    source:
      title: "Kubernetes documentation: Resource Management for Pods and Containers"
      url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
      kind: official-doc
      accessed: 2026-10-10
      archive: null
    quote: "memory limits are enforced by the kernel with out of memory (OOM) kills."
    os_concepts: ["memory management", "OOM killer", "resource limits", "containers"]
    pr: null
    ai_check:
      platform: Codex
      model: "gpt-6.1-sol"
      prompt_log: prompts/2026-10-10-TonCS05-11-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-11-reviewer-recheck.md
      result: supported
  - id: 11-21
    claim: "QEMU system emulation supplies a virtual machine model containing CPU, memory and emulated devices to run a guest operating system."
    type: fact
    status: ai-checked
    source:
      title: "QEMU documentation: System Emulation Introduction"
      url: https://www.qemu.org/docs/master/system/introduction.html
      kind: official-doc
      accessed: 2026-10-10
      archive: null
    quote: "QEMU’s system emulation provides a virtual model of a machine (CPU, memory and emulated devices) to run a guest OS."
    os_concepts: ["virtualization", "virtual machines", "CPU", "memory", "I/O"]
    pr: null
    ai_check:
      platform: Codex
      model: "gpt-6.1-sol"
      prompt_log: prompts/2026-10-10-TonCS05-11-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-11-reviewer-recheck.md
      result: supported
  - id: 11-22
    claim: "Recommended SRE course connection: compare the guest OS and virtual hardware of a QEMU machine with the shared-kernel model described for containers; then distinguish namespace-based isolation from cgroup resource control. This is a proposed learning comparison, not a claim that Google uses these products in this configuration."
    type: assumption
    status: unverified
    os_concepts: ["virtualization", "virtual machines", "containers", "namespaces", "cgroups"]
    pr: null
  - id: 11-23
    claim: "Proposed relationship chain for the report: SRE -> a hypothetical containerized web-service workload -> Linux -> a server or VM providing CPU, RAM, storage and networking -> Docker containers managed by Kubernetes -> processes, scheduling, virtual memory, file I/O, networking, permissions and resource isolation. The complete chain is a recommended example, not a verified description of Google's infrastructure."
    type: assumption
    status: unverified
    os_concepts: ["processes", "CPU scheduling", "virtual memory", "file systems", "I/O", "networking", "permissions", "virtualization", "containers", "resource isolation"]
    pr: null
---

## Summary

Linux namespaces support containers, while cgroups organize processes and distribute resources; Docker's introductory container model shares a kernel (11-16 to 11-18). Kubernetes enforces CPU limits through throttling and memory limits through kernel OOM kills, and QEMU models a machine to run a guest OS (11-19 to 11-21). The proposed comparison and workload chain connect these mechanisms to virtualization and resource-management concepts, and are explicitly recorded as assumptions (11-22, 11-23).

## Key points

- Namespaces can implement containers; cgroups control resource distribution across a process hierarchy. (11-16, 11-17)
- Docker's introductory model describes containers sharing a kernel. (11-18)
- Kubernetes uses CPU throttling for CPU limits and kernel OOM kills for memory limits. (11-19, 11-20)
- QEMU system emulation models CPU, memory and devices to run a guest OS. (11-21)
- Recommended comparison: distinguish virtual-machine hardware and guest OS concepts from shared-kernel containers, and distinguish isolation from resource control. (11-22)
- Recommended report chain: connect an SRE role and hypothetical web-service workload to Linux, server resources, Docker/Kubernetes and OS knowledge. (11-23)

## Source comparison

The Linux references explain namespace use and cgroup resource distribution, while the Kubernetes reference explains CPU and memory limit enforcement at the workload level (11-16, 11-17, 11-19, 11-20). Docker supplies a shared-kernel container model and QEMU supplies a guest-machine model; comparing them is a proposed learning exercise (11-18, 11-21, 11-22). Most individual factual claims have one primary source; the two Kubernetes enforcement claims share a page. These sources do not establish the proposed configuration as Google's infrastructure.

## Proposed relationship visualization

This visualization represents assumption 11-23. It is a candidate example for later report creation; a human should review it before using it in the report.

```mermaid
flowchart LR
    A["Job: SRE"] --> B["Workload: hypothetical containerized web service"]
    B --> C["OS: Linux"]
    C --> D["Infrastructure: server or VM with CPU, RAM, storage and networking"]
    D --> E["Tools: Docker containers managed by Kubernetes"]
    E --> F["Knowledge: processes and scheduling; virtual memory; file I/O; networking; permissions; isolation"]
```

## Proposed workload-to-concept mapping

All rows are applications of the recommended example in 11-23. The factual IDs identify the supporting mechanisms; the complete mapping remains an assumption.

| Example workload question | OS concepts | Supporting mechanism claims | Recommendation claims |
|---|---|---|---|
| Why is a service slow or restarting? | Processes, threads, scheduling and signals | 11-01, 11-02, 11-03, 11-05 | 11-06, 11-23 |
| How should memory observations be interpreted? | Virtual address spaces and per-thread memory | 11-02, 11-04 | 11-07, 11-23 |
| What does a completed write establish? | File I/O, page cache and durability | 11-08, 11-09, 11-10 | 11-14, 11-23 |
| Where should a failed connection or file-access operation be investigated? | Sockets, TCP and permissions | 11-11, 11-12, 11-13 | 11-15, 11-23 |
| What separates isolation, resource limits and a guest machine? | Namespaces, cgroups, containers and virtualization | 11-16 to 11-21 | 11-22, 11-23 |
