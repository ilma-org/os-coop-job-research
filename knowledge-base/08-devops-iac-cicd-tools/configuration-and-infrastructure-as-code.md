---
doc_type: topic-note
topic: 08-devops-iac-cicd-tools
title: "Configuration management and infrastructure-as-code in Google's SRE books"
updated: 2026-10-09
claims:
  - id: 08-17
    claim: "The SRE book says all of Google's schemes for distributing configuration store it in the primary source code repository and enforce a strict code review requirement."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.8 Release Engineering"
      url: https://sre.google/sre-book/release-engineering/
      kind: official-doc
      accessed: 2026-10-09
      archive: https://web.archive.org/web/20261005125731/https://sre.google/sre-book/release-engineering/
    quote: "All schemes involve storing configuration in our primary source code repository and enforcing a strict code review requirement."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-18
    claim: "The SRE Workbook says checking configuration files into a versioning system such as Subversion or Git is common practice, and equally important for configuration ingested by a web UI or remote APIs."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.14 Configuration Design and Best Practices"
      url: https://sre.google/workbook/configuration-design/
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "Checking configuration files into a versioning system, such as Subversion or Git, is a common practice nowadays, but this practice is equally important for configuration ingested by web UI or remote APIs."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-19
    claim: "The SRE Workbook says a new configuration should be pushed out gradually, so that issues can be detected and a problematic push aborted before it causes a 100% outage."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.14 Configuration Design and Best Practices"
      url: https://sre.google/workbook/configuration-design/
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "Instead, push the new configuration out gradually—doing so allows you to detect issues and abort a problematic push before causing a 100% outage."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-20
    claim: "The SRE Workbook says Kubernetes uses a rolling update strategy for software or configuration, instead of updating every pod at once, as one reason to avoid global all-at-once pushes."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.14 Configuration Design and Best Practices"
      url: https://sre.google/workbook/configuration-design/
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "This is one reason why tools such as Kubernetes use a rolling update strategy for updating software or configuration instead of updating every pod all at once."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-21
    claim: "The SRE Workbook says Box.com's infrastructure uses Git hooks to push configuration changes to production."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.15 Configuration Specifics"
      url: https://sre.google/workbook/configuration-specifics/
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "Box.com 's infrastructure uses Git hooks to push configuration changes to production."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-22
    claim: "The SRE Workbook gives, as an example of what a configuration language can do, emitting an Nginx web server configuration and a Terraform firewall configuration from a single Jsonnet evaluation that defines the port only once."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.15 Configuration Specifics"
      url: https://sre.google/workbook/configuration-specifics/
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "Output an Nginx web server configuration and a Terraform firewall configuration from a single Jsonnet evaluation that defines the port only once."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-23
    claim: "The SRE book says tools such as Puppet, Chef, cfengine and Perl all automate particular tasks and differ mostly in the level of abstraction of the components they provide."
    type: fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.7 The Evolution of Automation at Google"
      url: https://sre.google/sre-book/automation-at-google/
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "Widely available tools like Puppet, Chef, cfengine, and even Perl, which all provide ways to automate particular tasks, differ mostly in terms of the level of abstraction of the components provided to help the act of automating."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-24
    claim: "The SRE book says that requiring idempotent fixes let Google teams run their fix scripts every 15 minutes without fearing damage to a cluster's configuration."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.7 The Evolution of Automation at Google"
      url: https://sre.google/sre-book/automation-at-google/
      kind: official-doc
      accessed: 2026-10-09
      archive: https://web.archive.org/web/20260910213452/https://sre.google/sre-book/automation-at-google/
    quote: "Requiring idempotent fixes meant teams could run their \"fix script\" every 15 minutes without fearing damage to the cluster’s configuration."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-35
    claim: "Building Secure and Reliable Systems says that, instead of setting services up by hand, you might write imperative turnup automation or use a declarative high-level configuration language such as Terraform, and that you should capture the state of how the service is created."
    type: fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.9 Design for Recovery"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch09.html
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "Instead of setting up your services by hand, you might set them up by writing imperative turnup automation or using a declarative high-level configuration language (e.g., a container orchestration configuration tool like Terraform). In these scenarios, you should capture the state of how the service is created."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-36
    claim: "The SRE Workbook names GCP Deployment Manager, AWS Cloud Formation and Terraform as examples of tools for base infrastructure, used together with Kubernetes for containers."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.15 Configuration Specifics"
      url: https://sre.google/workbook/configuration-specifics/
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "this is true if you use a deployment architecture that uses GCP Deployment Manager , AWS Cloud Formation , or Terraform for base infrastructure, plus Kubernetes for containers."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
---

# Configuration management and infrastructure-as-code in Google's SRE books

## Summary

The books treat configuration like code: it is kept in a version control system, reviewed, and pushed out gradually. The tools named in these claims are Git and Subversion, Git hooks at Box.com, Terraform, GCP Deployment Manager, AWS Cloud Formation, Jsonnet, Puppet, Chef and cfengine, with Kubernetes named for its rolling updates. The pages searched do not teach an infrastructure-as-code tool: Terraform and the others appear as examples, and no claim recommends one. Ansible does not appear in the 106 book pages searched.

## Key points

- Google stores configuration in its primary source repository under strict code review (08-17). The Workbook says versioning matters for all configuration, including configuration set through a web UI or remote API (08-18).
- Push configuration gradually so a bad push can be stopped before it causes a full outage. Kubernetes rolling updates are the example (08-19, 08-20).
- Box.com uses Git hooks to push configuration changes to production (08-21).
- One Jsonnet evaluation can emit both an Nginx configuration and a Terraform firewall configuration (08-22).
- Named infrastructure tools: Terraform, GCP Deployment Manager and AWS Cloud Formation, used with Kubernetes for containers (08-35). Terraform is also the example of a declarative configuration language, with the advice to capture how the service was created (08-36).
- Puppet, Chef, cfengine and Perl differ mostly in the level of abstraction they offer for automation (08-23).
- Idempotent fixes can be run on a schedule, every 15 minutes in Google's example, without damaging a cluster's configuration (08-24).
