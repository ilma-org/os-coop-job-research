---
doc_type: topic-note
topic: 06-system-architecture-infrastructure
title: "Cluster management, containers and virtual machines"
updated: 2026-10-09
claims:
  - id: 06-09
    claim: "The SRE book says Borg jobs can be indefinitely running servers or batch processes such as MapReduce."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "which can either be indefinitely running servers or batch processes like a MapReduce"
    os_concepts: ["processes", "scheduling"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-10
    claim: "The SRE book says that if a Borg task malfunctions, it is killed and restarted, possibly on a different machine."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "If a task malfunctions, it is killed and restarted, possibly on a different machine."
    os_concepts: ["processes"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-11
    claim: "The SRE book says Borg accounts for failure domains when it places tasks; for example, it won't run all of a job's tasks on the same rack."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "Borg won’t run all of a job’s tasks on the same rack"
    os_concepts: ["scheduling"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-12
    claim: "The SRE book calls Kubernetes Borg's descendant: an open source container cluster orchestration framework that Google started in 2014."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "Borg’s descendant, Kubernetes—an open source Container Cluster orchestration framework started by Google in 2014"
    os_concepts: ["containers"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-13
    claim: "The SRE Workbook describes Google Kubernetes Engine (GKE) as a Google-managed system that creates, hosts and runs Kubernetes clusters for users."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.9 Incident Response"
      url: https://sre.google/workbook/incident-response/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260919200614/https://sre.google/workbook/incident-response/
    quote: "a Google-managed system that creates, hosts, and runs Kubernetes clusters for users"
    os_concepts: ["containers"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-14
    claim: "Building Secure and Reliable Systems says Google decided that running each App Engine user's code in an independent virtual machine was too inefficient."
    type: org-fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.8 Design for Resilience"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch08.html
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260704103623/https://google.github.io/building-secure-and-reliable-systems/raw/ch08.html
    quote: "running each user’s code in an independent virtual machine was too inefficient"
    os_concepts: ["virtualization"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-15
    claim: "Building Secure and Reliable Systems says running virtual machines controlled by mutually distrustful parties on the same hardware risks zero-day vulnerabilities in the virtualization layer or subtle cross-VM information leaks."
    type: fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.8 Design for Resilience"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch08.html
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "exposure to zero-day vulnerabilities in the virtualization layer perhaps, or subtle cross-VM information leaks"
    os_concepts: ["virtualization", "security"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-27
    claim: "A 2017 Google Cloud Blog post says Google Cloud uses the open-source KVM hypervisor."
    type: org-fact
    status: ai-checked
    source:
      title: "Google Cloud Blog, 7 ways we harden our KVM hypervisor at Google Cloud: security in plaintext (2017)"
      url: https://cloud.google.com/blog/products/gcp/7-ways-we-harden-our-kvm-hypervisor-at-google-cloud-security-in-plaintext
      kind: article
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260909122236/https://cloud.google.com/blog/products/gcp/7-ways-we-harden-our-kvm-hypervisor-at-google-cloud-security-in-plaintext
    quote: "Google Cloud uses the open-source KVM hypervisor"
    os_concepts: ["virtualization"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check-2.md
      result: supported
  - id: 06-28
    claim: "The same 2017 post says Google does not use QEMU and instead wrote its own user-space virtual machine monitor."
    type: org-fact
    status: ai-checked
    source:
      title: "Google Cloud Blog, 7 ways we harden our KVM hypervisor at Google Cloud: security in plaintext (2017)"
      url: https://cloud.google.com/blog/products/gcp/7-ways-we-harden-our-kvm-hypervisor-at-google-cloud-security-in-plaintext
      kind: article
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260909122236/https://cloud.google.com/blog/products/gcp/7-ways-we-harden-our-kvm-hypervisor-at-google-cloud-security-in-plaintext
    quote: "Instead, we wrote our own user-space virtual machine monitor"
    os_concepts: ["virtualization"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
---

# Cluster management, containers and virtual machines

## Summary

The SRE book says Borg jobs are long-running servers or batch processes, that a malfunctioning task is killed and restarted, possibly on another machine, and that Borg spreads a job's tasks across racks to account for failure domains (06-09 to 06-11). It calls Kubernetes Borg's descendant, and the SRE Workbook describes GKE as a Google-managed system that runs Kubernetes clusters for users (06-12, 06-13). For virtual machines, Building Secure and Reliable Systems says per-user VMs were too inefficient for App Engine, and that VMs of mutually distrustful parties on the same hardware risk virtualization-layer vulnerabilities and cross-VM leaks (06-14, 06-15). A 2017 Google Cloud Blog post names the hypervisor: Google Cloud uses the open-source KVM hypervisor and, instead of QEMU, Google's own user-space virtual machine monitor (06-27, 06-28).

## Key points

- Borg runs servers and batch jobs, restarts failed tasks, and avoids putting all of a job's tasks on one rack. (06-09, 06-10, 06-11)
- Kubernetes descends from Borg; GKE is Google's managed Kubernetes. (06-12, 06-13)
- VM trade-offs: a VM per user was too inefficient for App Engine, and shared hardware brings virtualization-layer risk. (06-14, 06-15)
- Hypervisor: open-source KVM, with Google's own user-space virtual machine monitor instead of QEMU. (06-27, 06-28)

## Notes for the write-up

- The hypervisor claims come from a 2017 post. Say "as of 2017"; no newer opened source confirms the current setup.

## Sources and limits

Round 1 used only the three books on https://sre.google/books/. Round 2 adds current official pages: Google Cloud documentation and blog posts, Google's data center site, and, for practice hardware, the Debian installation guide and the minikube documentation. The SRE book page footer says copyright 2017 and the Workbook page footer says copyright 2018; the Building Secure and Reliable Systems pages show no date. Each claim describes what its source says at the time of that source. Quotes are kept short on purpose; open the source to read the full passage.
