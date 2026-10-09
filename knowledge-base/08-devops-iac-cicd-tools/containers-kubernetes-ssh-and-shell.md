---
doc_type: topic-note
topic: 08-devops-iac-cicd-tools
title: "Containers, Kubernetes, SSH and shell in Google's SRE books"
updated: 2026-10-09
claims:
  - id: 08-25
    claim: "The SRE Workbook describes Kubernetes as an open source system for orchestrating containerized workloads on a cluster of machines."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.15 Configuration Specifics"
      url: https://sre.google/workbook/configuration-specifics/
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "Kubernetes is an open source system for orchestrating containerized workloads on a cluster of machines."
    os_concepts: ["containers", "process scheduling"]
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-26
    claim: "A footnote in the SRE book's production-environment chapter calls Kubernetes Borg's descendant, an open source container cluster orchestration framework started by Google in 2014."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-09
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "Some readers may be more familiar with Borg’s descendant, Kubernetes—an open source Container Cluster orchestration framework started by Google in 2014"
    os_concepts: ["containers", "process scheduling"]
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-27
    claim: "The SRE Workbook says the out-of-the-box way to use Kubernetes is to write YAML files that represent Kubernetes objects and run kubectl to deploy them to a cluster."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.15 Configuration Specifics"
      url: https://sre.google/workbook/configuration-specifics/
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "The out-of-the-box user experience involves writing YAML files that represent Kubernetes objects and running kubectl to deploy them to a cluster."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-28
    claim: "In an SRE Workbook incident case study on GKE, the certificate signer was not starting because it was trying to pull an apparently corrupted image from DockerHub."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.9 Incident Response"
      url: https://sre.google/workbook/incident-response/
      kind: official-doc
      accessed: 2026-10-09
      archive: https://web.archive.org/web/20260919200614/https://sre.google/workbook/incident-response/
    quote: "The certificate signer was trying to pull an image from DockerHub, and the image appeared to be corrupted."
    os_concepts: ["containers"]
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-29
    claim: "The SRE book says much of Google's distributed automation once relied on SSH, which was clumsy from a security perspective because people needed root on many machines."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.7 The Evolution of Automation at Google"
      url: https://sre.google/sre-book/automation-at-google/
      kind: official-doc
      accessed: 2026-10-09
      archive: https://web.archive.org/web/20260910213452/https://sre.google/sre-book/automation-at-google/
    quote: "Much of distributed automation relied at that time on SSH. This is clumsy from a security perspective, because people must have root on many machines to run most commands."
    os_concepts: ["security", "permissions"]
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-30
    claim: "The SRE book says Google had to replace its use of sshd with an authenticated, ACL-driven, RPC-based Local Admin Daemon, also known as Admin Servers."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.7 The Evolution of Automation at Google"
      url: https://sre.google/sre-book/automation-at-google/
      kind: official-doc
      accessed: 2026-10-09
      archive: https://web.archive.org/web/20260910213452/https://sre.google/sre-book/automation-at-google/
    quote: "We had to replace our use of sshd with an authenticated, ACL-driven, RPC-based Local Admin Daemon, also known as Admin Servers, which had permissions to perform those local changes."
    os_concepts: ["security", "permissions"]
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-31
    claim: "The SRE book says SREs moved from writing shell scripts in their home directories to building peer-reviewed RPC servers with fine-grained ACLs."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.7 The Evolution of Automation at Google"
      url: https://sre.google/sre-book/automation-at-google/
      kind: official-doc
      accessed: 2026-10-09
      archive: https://web.archive.org/web/20260910213452/https://sre.google/sre-book/automation-at-google/
    quote: "SREs moved from writing shell scripts in their home directories to building peer-reviewed RPC servers with fine-grained ACLs."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-32
    claim: "The SRE Workbook says that if configuration data resists representation in the configuration language, for example a Bash script, basic string templating can be used as a last resort."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.15 Configuration Specifics"
      url: https://sre.google/workbook/configuration-specifics/
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "If configuration data resists representation within the configuration language (for example, a Bash script), you can use basic string templating techniques as a last resort."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-33
    claim: "Building Secure and Reliable Systems names using SSH to run commands on the machine as one path by which an administrator could make a change without review."
    type: fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.14 Deploying Code"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch14.html
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "consider all of the paths where an administrator could make a change without review—for example, making a change by configuring the CI/CD pipeline directly or using SSH to run commands on the machine."
    os_concepts: ["security", "permissions"]
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check-2.md
      result: supported
---

# Containers, Kubernetes, SSH and shell in Google's SRE books

## Summary

The books mention Kubernetes as Borg's open source descendant and as an application whose configuration needs managing, and Docker only inside one incident case study (a corrupted image pulled from DockerHub). SSH and shell scripts appear mostly as things Google moved away from: SSH-based automation was replaced for security reasons, and ad hoc shell scripts gave way to peer-reviewed RPC servers. A Bash script appears once, as an example of data that is hard to express in a configuration language. The pages searched do not teach Docker, Kubernetes, SSH or Bash as skills, so these claims show how the books mention each tool, not what a Google SRE must know.

## Key points

- Kubernetes is an open source system for orchestrating containerized workloads, described as Borg's descendant and started by Google in 2014 (08-25, 08-26). Users write YAML objects and deploy them with kubectl (08-27).
- Docker appears in one GKE incident, where the certificate signer failed to pull an apparently corrupted image from DockerHub (08-28).
- Google's distributed automation once relied on SSH, which needed root on many machines. It was replaced by an authenticated, ACL-driven Admin Server (08-29, 08-30). Building Secure and Reliable Systems names SSH as a path by which an administrator could make a change without review (08-33).
- SREs moved from shell scripts in home directories to peer-reviewed RPC servers (08-31). A Bash script is an example of configuration data that resists a configuration language (08-32).
