---
doc_type: topic-note
topic: 04-operating-systems
title: "Process isolation, sandboxing and OS resource limits"
updated: 2026-10-09
claims:
  - id: 04-15
    claim: "The SRE book says that if a task tries to use more resources than it requested, Borg kills the task and restarts it."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "use more resources than it requested, Borg kills the task and restarts it"
    os_concepts: ["resource isolation", "processes"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
  - id: 04-16
    claim: "Building Secure and Reliable Systems describes a Google debugging case in which a memory container ran out of RAM and the kernel issued a SIGKILL for all processes in the container."
    type: org-fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.15 Investigating Systems"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch15.html
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260616012631/https://google.github.io/building-secure-and-reliable-systems/raw/ch15.html
    quote: "container ran out of RAM and the kernel issued a SIGKILL for all processes"
    os_concepts: ["memory management", "processes", "containers"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
  - id: 04-17
    claim: "The SRE book says running out of file descriptors can lead to an inability to initialize network connections."
    type: fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.22 Addressing Cascading Failures"
      url: https://sre.google/sre-book/addressing-cascading-failures/
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "Running out of file descriptors can lead to the inability to initialize network connections"
    os_concepts: ["file descriptors", "networking"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
  - id: 04-18
    claim: "The SRE book says that in extreme cases thread starvation can cause a server to run out of process IDs."
    type: fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.22 Addressing Cascading Failures"
      url: https://sre.google/sre-book/addressing-cascading-failures/
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "thread starvation can also cause you to run out of process IDs"
    os_concepts: ["threads", "processes"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
  - id: 04-19
    claim: "Building Secure and Reliable Systems says the Linux kernel exposed Google App Engine to a large attack surface."
    type: org-fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.8 Design for Resilience"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch08.html
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260704103623/https://google.github.io/building-secure-and-reliable-systems/raw/ch08.html
    quote: "The Linux kernel meant that App Engine was exposed to a large attack surface"
    os_concepts: ["kernel", "security"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
  - id: 04-20
    claim: "Building Secure and Reliable Systems says Google added a second layer of ptrace sandboxing to App Engine to filter and alert on unexpected system calls."
    type: org-fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.8 Design for Resilience"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch08.html
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260704103623/https://google.github.io/building-secure-and-reliable-systems/raw/ch08.html
    quote: "a second layer of ptrace sandboxing to filter and alert on unexpected system calls"
    os_concepts: ["system calls", "security"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
  - id: 04-21
    claim: "Building Secure and Reliable Systems says a kernel vulnerability in the host operating system can be patched without changing the application container."
    type: fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.7 Design for a Changing Landscape"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch07.html
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "kernel vulnerability in the host operating system without having to change your application container"
    os_concepts: ["kernel", "containers"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
  - id: 04-33
    claim: "Google Cloud's \"What are containers?\" page says containers share the OS kernel and use a fraction of the memory that VMs require."
    type: fact
    status: ai-checked
    source:
      title: "Google Cloud, What are containers?"
      url: https://cloud.google.com/learn/what-are-containers
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "Containers share the OS kernel and use a fraction of the memory VMs require"
    os_concepts: ["containers", "virtualization", "kernel"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
  - id: 04-34
    claim: "The Linux kernel documentation describes cgroup as a mechanism to organize processes hierarchically and distribute system resources along the hierarchy."
    type: fact
    status: ai-checked
    source:
      title: "The Linux Kernel documentation, Control Group v2"
      url: https://docs.kernel.org/admin-guide/cgroup-v2.html
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "cgroup is a mechanism to organize processes hierarchically and distribute system resources"
    os_concepts: ["processes", "resource isolation"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
  - id: 04-35
    claim: "The Linux kernel's cgroup v2 documentation says that when a cgroup's memory usage reaches its memory.max hard limit and can't be reduced, the OOM killer is invoked in the cgroup."
    type: fact
    status: ai-checked
    source:
      title: "The Linux Kernel documentation, Control Group v2"
      url: https://docs.kernel.org/admin-guide/cgroup-v2.html
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "memory usage reaches this limit and can’t be reduced, the OOM killer is invoked"
    os_concepts: ["memory management", "resource isolation"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
  - id: 04-36
    claim: "The Linux kernel's cgroup v2 documentation says the memory.oom.group setting decides whether the OOM killer treats a cgroup as an indivisible workload, killing its tasks together or not at all."
    type: fact
    status: ai-checked
    source:
      title: "The Linux Kernel documentation, Control Group v2"
      url: https://docs.kernel.org/admin-guide/cgroup-v2.html
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "whether the cgroup should be treated as an indivisible workload by the OOM killer"
    os_concepts: ["memory management", "processes"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
  - id: 04-37
    claim: "Building Secure and Reliable Systems says Google has many out-of-memory (OOM) conditions every day."
    type: org-fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.15 Investigating Systems"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch15.html
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260616012631/https://google.github.io/building-secure-and-reliable-systems/raw/ch15.html
    quote: "Google has many OOM conditions every day"
    os_concepts: ["memory management"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
  - id: 04-38
    claim: "Building Secure and Reliable Systems says Google adapted the App Engine Python runtime to compile down to Native Client (NaCl) bitcode."
    type: org-fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.8 Design for Resilience"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch08.html
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260704103623/https://google.github.io/building-secure-and-reliable-systems/raw/ch08.html
    quote: "adapt the Python runtime to compile down to Native Client (NaCL) bitcode"
    os_concepts: ["security"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
  - id: 04-39
    claim: "The gVisor documentation describes gVisor as an application kernel that implements a Linux-like interface."
    type: fact
    status: ai-checked
    source:
      title: "gVisor documentation, What is gVisor?"
      url: https://gvisor.dev/docs/
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "It is an application kernel that implements a Linux-like interface"
    os_concepts: ["kernel"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
  - id: 04-40
    claim: "The gVisor documentation says gVisor intercepts application system calls and acts as the guest kernel."
    type: fact
    status: ai-checked
    source:
      title: "gVisor documentation, What is gVisor?"
      url: https://gvisor.dev/docs/
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "gVisor intercepts application system calls and acts as the guest kernel"
    os_concepts: ["system calls", "kernel"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
  - id: 04-41
    claim: "Google Kubernetes Engine documentation says the container runtime often runs as a privileged user on the node and has access to most system calls into the host kernel."
    type: org-fact
    status: ai-checked
    source:
      title: "Google Kubernetes Engine documentation, GKE Sandbox"
      url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260910202903/https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods
    quote: "has access to most system calls into the host kernel"
    os_concepts: ["system calls", "kernel", "containers"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
  - id: 04-56
    claim: "Google's infrastructure security design overview says the isolation and sandboxing techniques Google uses to protect a service from other services on the same machine include Linux user separation."
    type: org-fact
    status: ai-checked
    source:
      title: "Google Cloud, Google infrastructure security design overview"
      url: https://docs.cloud.google.com/docs/security/infrastructure/design
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260923013749/https://docs.cloud.google.com/docs/security/infrastructure/design
    quote: "These techniques include Linux user separation"
    os_concepts: ["security", "processes"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
  - id: 04-57
    claim: "Google's infrastructure security design overview lists an application kernel for containers, such as gVisor, among those isolation techniques."
    type: org-fact
    status: ai-checked
    source:
      title: "Google Cloud, Google infrastructure security design overview"
      url: https://docs.cloud.google.com/docs/security/infrastructure/design
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260923013749/https://docs.cloud.google.com/docs/security/infrastructure/design
    quote: "application kernel for containers (such as gVisor"
    os_concepts: ["containers", "kernel", "security"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
---

# Process isolation, sandboxing and OS resource limits

## Summary

Containers share the OS kernel (04-33), and Linux cgroups organize processes into a hierarchy and distribute system resources along it (04-34). In cgroup v2, when a cgroup reaches its memory.max limit and memory cannot be reduced, the OOM killer runs inside that cgroup; with memory.oom.group set, the cgroup's tasks are killed together (04-35, 04-36). Building Secure and Reliable Systems says Google has many OOM conditions every day, and describes a container that ran out of RAM until the kernel killed all its processes (04-37, 04-16). Borg kills and restarts a task that uses more than it requested, and the SRE book names file descriptors and process IDs as resources a server can run out of (04-15, 04-17, 04-18). For untrusted code, Google sandboxed App Engine with Native Client and ptrace because of the Linux kernel's attack surface, and gVisor is an application kernel that intercepts application system calls; GKE documentation notes that the container runtime has access to most system calls into the host kernel (04-19, 04-20, 04-38 to 04-41). Google's infrastructure security design overview says Google isolates services that share a machine with techniques that include Linux user separation and an application kernel for containers such as gVisor (04-56, 04-57).

## Key points

- Containers share the OS kernel; a kernel vulnerability on the host can be patched without changing the container. (04-33, 04-21)
- cgroups organize processes and distribute resources; hitting memory.max invokes the OOM killer in the cgroup, and memory.oom.group makes it kill the whole cgroup. (04-34, 04-35, 04-36)
- OOM events are common at Google, and a memory container that ran out of RAM had all its processes killed by the kernel. (04-37, 04-16)
- Borg kills and restarts a task that exceeds its requested resources. (04-15)
- File descriptors and process IDs can run out. (04-17, 04-18)
- App Engine: the Linux kernel was a large attack surface, so Google used Native Client plus a ptrace sandbox that filters system calls. (04-19, 04-20, 04-38)
- GKE: the container runtime has access to most system calls into the host kernel. gVisor is an application kernel that intercepts system calls and acts as the guest kernel. (04-41, 04-39, 04-40)
- Google's own infrastructure isolates services on a shared machine with Linux user separation and an application kernel such as gVisor. (04-56, 04-57)

## Notes for the write-up

- Building Secure and Reliable Systems does not say which kernel mechanism killed every process in 04-16. memory.oom.group (04-36) is one Linux mechanism that behaves this way; present it as background, not as what Google used.
- Google lists an application kernel such as gVisor among its isolation techniques (04-57). No checked source says which Google services, such as App Engine or GKE Sandbox, run in gVisor. A GKE Sandbox claim was dropped because the page changed after its only archive snapshot.

## Sources and limits

Round 1 used only the three books on https://sre.google/books/. Round 2 adds official Google pages (Google Cloud documentation and the Google Cloud Blog), the Linux kernel documentation, the gVisor documentation and one USENIX paper by a Google engineer. The SRE book page footer says copyright 2017 and the Workbook page footer says copyright 2018; the Building Secure and Reliable Systems pages show no date. Each claim describes what its source says at the time of that source, not necessarily current practice. Quotes are kept short on purpose; open the source to read the full passage.
