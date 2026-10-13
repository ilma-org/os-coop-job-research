---
doc_type: topic-note
topic: 13-preparation-plan
title: "A practical SRE preparation roadmap and completion gates"
updated: 2026-10-13
claims:
  - id: 13-07
    claim: "A Git commit records a project snapshot that can later be reverted to or compared with another snapshot."
    type: fact
    status: ai-checked
    source:
      title: "Pro Git, second edition: Recording Changes to the Repository"
      url: https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "Every time you perform a commit, you’re recording a snapshot of your project that you can revert to or compare to later."
    os_concepts: []
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
  - id: 13-08
    claim: "Prometheus collects target metrics by scraping HTTP metrics endpoints."
    type: fact
    status: ai-checked
    source:
      title: "Prometheus documentation: Getting started"
      url: https://prometheus.io/docs/prometheus/latest/getting_started/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "Prometheus collects metrics from targets by scraping metrics HTTP endpoints."
    os_concepts: ["networking"]
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
  - id: 13-09
    claim: "The SRE book identifies latency, traffic, errors and saturation as the four golden signals of monitoring."
    type: fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, chapter 6: Monitoring Distributed Systems"
      url: https://sre.google/sre-book/monitoring-distributed-systems/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "The four golden signals of monitoring are latency, traffic, errors, and saturation."
    os_concepts: ["resource management"]
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
  - id: 13-10
    claim: "The SRE book recommends regular review sessions to ensure completed postmortem drafts are reviewed."
    type: fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, chapter 15: Postmortem Culture"
      url: https://sre.google/sre-book/postmortem-culture/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "To ensure that each completed draft is reviewed, we encourage regular review sessions for postmortems."
    os_concepts: []
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
  - id: 13-11
    claim: "The SRE workbook cautions that automation should not remove human understanding of what is going wrong."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, chapter 6: Eliminating Toil"
      url: https://sre.google/workbook/eliminating-toil/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "Also note that automation shouldn’t eliminate human understanding of what’s going wrong."
    os_concepts: []
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
  - id: 13-12
    claim: "Proposed core roadmap with completion gates: (1) configure the Linux lab and demonstrate SSH login plus inspection of processes, memory, files and sockets; (2) version a small HTTP service and a Bash or Python health-check script, testing both healthy and failed responses; (3) containerize the service and show reproducible startup, an HTTP request and logs; (4) instrument and scrape service metrics with Prometheus, record the four golden signals and test a documented practice alert; (5) stop the service or introduce a lab permission error, document detection, evidence, mitigation and recovery, then write a postmortem with impact, timeline, contributing causes and a preventive action. Advance when each gate passes; duration depends on prior skills and available time."
    type: assumption
    status: unverified
    os_concepts: ["processes", "memory", "file systems", "networking", "permissions"]
    pr: null
  - id: 13-13
    claim: "Proposed optional extension: after the core roadmap, deploy the same service to local minikube with kubectl and reproduce a configuration change and recovery. Pass when the learner can explain the manifests, inspect workload state and demonstrate recovery; this extension is conditional on prerequisite resources."
    type: assumption
    status: unverified
    os_concepts: ["containers", "resource management"]
    pr: null
  - id: 13-14
    claim: "Proposed career-preparation deliverables: keep a reproducible README, versioned lab configuration and health-check script, monitoring evidence and a reviewed postmortem; explain the job-to-OS-to-infrastructure-to-tools connection. Have a peer reproduce the documented setup and review the incident explanation, revise unclear steps, and use the resulting evidence in a portfolio and mock technical discussion. This plan is a general SRE preparation recommendation, not Google hiring criteria or a guarantee of readiness."
    type: assumption
    status: unverified
    os_concepts: []
    pr: null
---

## Summary

Git snapshots, Prometheus scraping and the four golden signals provide building blocks for an SRE practice project. Published SRE guidance supports postmortem review and maintaining understanding when automating. The roadmap, completion gates and portfolio are proposed exercises; progress depends on demonstrated results rather than a fixed schedule.

## Key points

- Record reproducible changes with Git; collect HTTP metrics with Prometheus and interpret latency, traffic, errors and saturation. (13-07, 13-08, 13-09)
- Review incident writeups and explain failures even when scripts automate checks. (13-10, 13-11)
- The core sequence, optional Kubernetes extension and career evidence are recommendations. (13-12, 13-13, 13-14)

## Proposed roadmap

Every row is an assumption under 13-12, not an organization's training requirement.

| Stage | Practice | Completion evidence |
|---|---|---|
| 1. Linux | Install/configure the lab; inspect processes, memory, files and sockets. | SSH key login and an explained inspection record. |
| 2. Code and automation | Version a small HTTP service and Bash/Python health check. | Healthy and failed responses are tested; code and results are recorded. |
| 3. Containers | Containerize the service; inspect startup and logs. | Reproducible startup, an HTTP response and explained logs. |
| 4. Monitoring | Instrument/scrape service metrics; document a practice alert. | Four golden signals recorded and an alert condition demonstrated. |
| 5. Incident exercise | Stop the service or introduce a lab permission error; diagnose and recover. | Impact, timeline, evidence, mitigation, recovery and a preventive action documented. |

Optional extension: deploy the same service with minikube/kubectl after checking capacity; explain manifests, inspect state and demonstrate recovery. (13-13)

For career preparation, assemble a reproducible README, configuration, script, monitoring evidence and postmortem; obtain peer feedback and revise. Explain the OS/infrastructure/tool connection in a mock technical discussion. This is a portfolio proposal, not Google hiring criteria. (13-14)
