---
doc_type: topic-note
topic: 08-devops-iac-cicd-tools
title: "Release engineering and CI/CD in Google's SRE books"
updated: 2026-10-09
claims:
  - id: 08-01
    claim: "The SRE book says running reliable services requires reliable release processes, and that SREs need to know releases are built in a reproducible, automated way rather than as \"unique snowflakes.\""
    type: fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.8 Release Engineering"
      url: https://sre.google/sre-book/release-engineering/
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "Running reliable services requires reliable release processes. Site Reliability Engineers (SREs) need to know that the binaries and configurations they use are built in a reproducible, automated way so that releases are repeatable and aren’t “unique snowflakes.”"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-02
    claim: "The SRE book says Google has developed an automated release system called Rapid."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.8 Release Engineering"
      url: https://sre.google/sre-book/release-engineering/
      kind: official-doc
      accessed: 2026-10-09
      archive: https://web.archive.org/web/20261005125731/https://sre.google/sre-book/release-engineering/
    quote: "Google has developed an automated release system called Rapid"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-03
    claim: "The SRE book says Google has embraced the philosophy that frequent releases mean fewer changes between versions, which makes testing and troubleshooting easier."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.8 Release Engineering"
      url: https://sre.google/sre-book/release-engineering/
      kind: official-doc
      accessed: 2026-10-09
      archive: https://web.archive.org/web/20261005125731/https://sre.google/sre-book/release-engineering/
    quote: "We have embraced the philosophy that frequent releases result in fewer changes between versions. This approach makes testing and troubleshooting easier."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-04
    claim: "The SRE book says some Google teams use a \"Push on Green\" release model, in which they deploy every build that passes all tests."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.8 Release Engineering"
      url: https://sre.google/sre-book/release-engineering/
      kind: official-doc
      accessed: 2026-10-09
      archive: https://web.archive.org/web/20261005125731/https://sre.google/sre-book/release-engineering/
    quote: "Other teams have adopted a “Push on Green” release model and deploy every build that passes all tests"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-05
    claim: "The SRE book says most major Google projects do not release from the mainline: they branch from it at a specific revision and never merge the branch back."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.8 Release Engineering"
      url: https://sre.google/sre-book/release-engineering/
      kind: official-doc
      accessed: 2026-10-09
      archive: https://web.archive.org/web/20261005125731/https://sre.google/sre-book/release-engineering/
    quote: "However, most major projects don’t release directly from the mainline. Instead, we branch from the mainline at a specific revision and never merge changes from the branch back into the mainline."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-06
    claim: "In the SRE book's description of Google's release branches, bug fixes are submitted to the mainline and then cherry picked into the release branch."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.8 Release Engineering"
      url: https://sre.google/sre-book/release-engineering/
      kind: official-doc
      accessed: 2026-10-09
      archive: https://web.archive.org/web/20261005125731/https://sre.google/sre-book/release-engineering/
    quote: "Bug fixes are submitted to the mainline and then cherry picked into the branch for inclusion in the release."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-07
    claim: "The SRE book says almost all changes to Google's codebase require a code review that is built into the normal developer workflow."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.8 Release Engineering"
      url: https://sre.google/sre-book/release-engineering/
      kind: official-doc
      accessed: 2026-10-09
      archive: https://web.archive.org/web/20261005125731/https://sre.google/sre-book/release-engineering/
    quote: "Almost all changes to the codebase require a code review, which is a streamlined action integrated into our normal developer workflow."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-08
    claim: "The SRE book says a continuous test system at Google runs unit tests against the mainline each time a change is submitted, so build and test failures are detected quickly."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.8 Release Engineering"
      url: https://sre.google/sre-book/release-engineering/
      kind: official-doc
      accessed: 2026-10-09
      archive: https://web.archive.org/web/20261005125731/https://sre.google/sre-book/release-engineering/
    quote: "A continuous test system runs unit tests against the code in the mainline each time a change is submitted, allowing us to detect build and test failures quickly."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-09
    claim: "The SRE book says Google uses Sisyphus, a rollout automation framework developed by SRE, for its more complicated deployments."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.8 Release Engineering"
      url: https://sre.google/sre-book/release-engineering/
      kind: official-doc
      accessed: 2026-10-09
      archive: https://web.archive.org/web/20261005125731/https://sre.google/sre-book/release-engineering/
    quote: "For more complicated deployments, we use Sisyphus, which is a general-purpose rollout automation framework developed by SRE."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-10
    claim: "The SRE Workbook lists automated deployments among its basic release engineering principles: deployments should be performed by computers, not humans."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.16 Canarying Releases"
      url: https://sre.google/workbook/canarying-releases/
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "Deployments should be performed by computers, not humans."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-11
    claim: "The SRE Workbook defines canarying as a partial and time-limited deployment of a change in a service and its evaluation."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.16 Canarying Releases"
      url: https://sre.google/workbook/canarying-releases/
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "We define canarying as a partial and time-limited deployment of a change in a service and its evaluation."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-12
    claim: "The SRE Workbook says automating releases helps avoid the toil of manual tasks, the inconsistency of a nonautomated process, not knowing the exact state of a rollout, and the difficulty of rolling back."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.16 Canarying Releases"
      url: https://sre.google/workbook/canarying-releases/
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "Automating releases can help avoid many of the traditional pitfalls associated with release engineering: the toil of repetitive and manual tasks, the inconsistency of a nonautomated process, the inability of knowing the exact state of a rollout, and the difficulty of rolling back."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-13
    claim: "Building Secure and Reliable Systems uses the term software supply chain for the process of writing, building, testing and deploying a software system, and says its steps include the typical responsibilities of a version control system, a continuous integration (CI) pipeline and a continuous delivery (CD) pipeline."
    type: fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.14 Deploying Code"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch14.html
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "We use the term software supply chain to describe the process of writing, building, testing, and deploying a software system. These steps include the typical responsibilities of a version control system (VCS), a continuous integration (CI) pipeline, and a continuous delivery (CD) pipeline."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check-2.md
      result: supported
  - id: 08-14
    claim: "Building Secure and Reliable Systems gives, as an example, configuring GitHub, GitLab or BitBucket to require a set number of approvals for every pull or merge request."
    type: fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.14 Deploying Code"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch14.html
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "For example, you can configure GitHub, GitLab, or BitBucket to require a certain number of approvals for every pull/merge request."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-15
    claim: "Building Secure and Reliable Systems says scripted deployment steps let humans and automation run the same steps consistently, and names CI/CD systems such as Jenkins for automating them."
    type: fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.14 Deploying Code"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch14.html
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "This allows both humans and automation to execute the same steps for consistency. You can use CI/CD systems (such as Jenkins ) for this purpose."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-16
    claim: "In its on-call chapter the SRE Workbook suggests aggregating change information into a searchable timeline to correlate new bugs with the change that caused them, and names the Slack plug-in for Jenkins as a helpful tool."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.8 On-Call"
      url: https://sre.google/workbook/on-call/
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "Aggregating change information into a searchable timeline makes it simpler (and hopefully quicker) to correlate new bugs with the corresponding change that introduced them. Tools like the Slack plug-in for Jenkins can be helpful."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
  - id: 08-34
    claim: "In the SRE Workbook's Waze case study of organizational change (Waze is a navigation app that Google acquired in 2013 and that kept operating relatively autonomously within Google), a small coalition of SREs and developers proposed shifting to continuous deployment using Spinnaker, an open source, multicloud continuous delivery platform. This is one team's case, not a statement of general Google practice."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.21 Organizational Change Management in SRE"
      url: https://sre.google/workbook/organizational-change/
      kind: official-doc
      accessed: 2026-10-09
      archive: null
    quote: "In response, a small coalition of SREs and developers sketched out a strategic vision to shift to a continuous deployment strategy using Spinnaker , an open source, multicloud, continuous delivery platform for building and executing deployment workflows."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nacs-970-devops-iac-cicd-author-check.md
      result: supported
---

# Release engineering and CI/CD in Google's SRE books

## Summary

This note collects what Google's SRE books say about releasing software: release engineering as a discipline, Google's branching and cherry-pick workflow, its in-house release and rollout tools, canarying, and CI/CD pipelines. The SRE book (page footer: copyright 2017) describes Google's own tooling, so those claims record what the book says, not how Google works today. The Workbook (copyright 2018) and Building Secure and Reliable Systems add general guidance and name Jenkins and Spinnaker as CI/CD tools, but none of the 106 book pages searched compares CI/CD tools. No source here shows which CI/CD tools Google SRE uses now.

## Key points

- Reliable services need release processes that are reproducible and automated (08-01, 08-10, 08-12).
- The SRE book describes Google's in-house release tooling: the Rapid release system, a continuous test system, and Sisyphus for more complicated rollouts (08-02, 08-08, 08-09).
- Google's workflow branches from the mainline at a specific revision, never merges back, and cherry-picks bug fixes into the branch; almost every change needs code review (08-05, 08-06, 08-07).
- Frequent releases mean fewer changes per release, and some teams deploy every build that passes all tests ("Push on Green") (08-03, 08-04).
- Canarying is a partial, time-limited deployment of a change together with its evaluation (08-11).
- Building Secure and Reliable Systems says the software supply chain includes the responsibilities of version control, CI and CD. Scripting every step lets humans and automation run the same steps, and hosted Git services can require approvals for each merge request (08-13, 08-14, 08-15).
- Named CI/CD tools are Jenkins (08-15, 08-16) and Spinnaker (08-34). Aggregating change information in a searchable timeline helps find which change caused a bug (08-16).
