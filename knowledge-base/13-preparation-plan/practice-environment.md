---
doc_type: topic-note
topic: 13-preparation-plan
title: "OS, hardware and tool setup for an SRE practice lab"
updated: 2026-10-13
claims:
  - id: 13-01
    claim: "The Ubuntu Server basic-installation tutorial recommends at least 2 GB of RAM and 5 GB of disk space for that tutorial."
    type: fact
    status: human-verified
    source:
      title: "Ubuntu Server documentation: Basic installation"
      url: https://ubuntu.com/server/docs/tutorial/basic-installation/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "The recommended minimal system requirements for this tutorial are: RAM: 2 GB or more Disk: 5 GB or more"
    os_concepts: ["virtualization", "memory", "file systems"]
    pr: null
    ai_check:
      platform: Codex
      model: "gpt-6.1-sol"
      prompt_log: prompts/2026-10-11-TonCS05-13-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-13-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-13
      result: pass
      opened_source: true
  - id: 13-02
    claim: "SSH supports authentication between two hosts using cryptographic keys instead of a password."
    type: fact
    status: human-verified
    source:
      title: "Ubuntu Server documentation: OpenSSH server"
      url: https://ubuntu.com/server/docs/how-to/security/openssh-server/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "SSH allows authentication between two hosts without the need of a password, using cryptographic keys instead."
    os_concepts: ["networking", "security"]
    pr: null
    ai_check:
      platform: Codex
      model: "gpt-6.1-sol"
      prompt_log: prompts/2026-10-11-TonCS05-13-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-13-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-13
      result: pass
      opened_source: true
  - id: 13-03
    claim: "Docker's Ubuntu installation guide verifies installation by running the hello-world image."
    type: fact
    status: human-verified
    source:
      title: "Docker Docs: Install Docker Engine on Ubuntu"
      url: https://docs.docker.com/engine/install/ubuntu/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "Verify that the installation is successful by running the hello-world image:"
    os_concepts: ["containers"]
    pr: null
    ai_check:
      platform: Codex
      model: "gpt-6.1-sol"
      prompt_log: prompts/2026-10-11-TonCS05-13-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-13-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-13
      result: pass
      opened_source: true
  - id: 13-04
    claim: "The minikube start guide lists at least 2 CPUs, 2 GB of free memory and 20 GB of free disk space among its prerequisites."
    type: fact
    status: human-verified
    source:
      title: "minikube documentation: minikube start"
      url: https://minikube.sigs.k8s.io/docs/start/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "2 CPUs or more 2GB of free memory 20GB of free disk space"
    os_concepts: ["virtualization", "memory", "storage"]
    pr: null
    ai_check:
      platform: Codex
      model: "gpt-6.1-sol"
      prompt_log: prompts/2026-10-11-TonCS05-13-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-13-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-13
      result: pass
      opened_source: true
  - id: 13-05
    claim: "Proposed practice environment: install Ubuntu Server 24.04 LTS in a disposable local VM, initially allocate 2 vCPUs, 4 GB RAM and 40 GB disk, and reserve resources for the host. Complete installation, package updates, user/permission and network configuration, then demonstrate SSH key login. These allocations are a starting proposal, not a measured requirement for the combined lab; check available memory and disk before extensions."
    type: assumption
    status: unverified
    os_concepts: ["virtualization", "security", "memory"]
    pr: null
  - id: 13-06
    claim: "Proposed setup order: OS and basic administration, then Git and Bash/Python, Docker Engine, and Prometheus. Add minikube and kubectl only after the core lab passes and its prerequisites are available. Use a local lab without requiring a cloud account; a cloud variant can be considered later if local resources are insufficient, after choosing and checking a specific service."
    type: assumption
    status: unverified
    os_concepts: ["containers", "networking"]
    pr: null
---

## Summary

Published guides support an Ubuntu installation exercise, SSH key authentication, Docker verification and minikube prerequisites. The proposed local VM and tool order are recommendations with resource checks before extensions. Combined workload sizing and a specific cloud alternative remain unmeasured.

## Key points

- Ubuntu's tutorial baseline is 2 GB RAM and 5 GB disk; this is not sizing for the complete lab. (13-01)
- SSH key login and Docker's `hello-world` check provide observable setup milestones. (13-02, 13-03)
- Minikube lists 2 CPUs, 2 GB free memory and 20 GB free disk among its prerequisites. (13-04)
- Proposed setup: Ubuntu Server 24.04 LTS in a disposable VM, initially 2 vCPUs / 4 GB RAM / 40 GB disk; preserve host resources and check capacity before extensions. (13-05)
- Proposed order: OS administration -> Git and Bash/Python -> Docker -> Prometheus -> optional minikube/kubectl. The local route requires no cloud account. (13-06)
