---
doc_type: topic-note
topic: 09-monitoring-and-incident-tools
title: "Metrics, logging and tracing tools in Google's SRE books"
updated: 2026-10-14
claims:
  - id: 09-01
    claim: "The SRE book says Google built its monitoring system Borgmon shortly after the Borg job scheduler was created in 2003, to complement it."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.10 Practical Alerting from Time-Series Data"
      url: https://sre.google/sre-book/practical-alerting/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260806204024/https://sre.google/sre-book/practical-alerting/
    quote: "Shortly after the job scheduling infrastructure Borg [Ver15] was created in 2003, a new monitoring system—Borgmon—was built to complement it."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-02
    claim: "The SRE book says Borgmon collects metrics by fetching the /varz URI of each monitored target at predefined intervals and storing the values in memory."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.10 Practical Alerting from Time-Series Data"
      url: https://sre.google/sre-book/practical-alerting/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260806204024/https://sre.google/sre-book/practical-alerting/
    quote: "At predefined intervals, Borgmon fetches the /varz URI on each target, decodes the results, and stores the values in memory."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-03
    claim: "The SRE book says Borgmon keeps its time-series data in an in-memory database that is regularly checkpointed to disk."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.10 Practical Alerting from Time-Series Data"
      url: https://sre.google/sre-book/practical-alerting/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260806204024/https://sre.google/sre-book/practical-alerting/
    quote: "Borgmon stores all the data in an in-memory database, regularly checkpointed to disk."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-04
    claim: "The SRE book says the idea behind Borgmon, using time-series data to generate alerts, is available outside Google through open source tools such as Prometheus, Riemann, Heka and Bosun."
    type: fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.10 Practical Alerting from Time-Series Data"
      url: https://sre.google/sre-book/practical-alerting/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "Even though Borgmon remains internal to Google, the idea of treating time-series data as a data source for generating alerts is now accessible to everyone through those open source tools like Prometheus, Riemann, Heka, and Bosun, and probably others by the time you read this."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-05
    claim: "The Workbook names grafanalib as a third-party solution that lets components traditionally configured with a UI be configured as code."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.4 Monitoring"
      url: https://sre.google/workbook/monitoring/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "Some third-party solutions like grafanalib enable this approach for components that are traditionally configured with a UI."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-06
    claim: "The Workbook says Google's approach to monitoring has evolved toward a single framework that is run centrally as a service."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.4 Monitoring"
      url: https://sre.google/workbook/monitoring/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260909103330/https://sre.google/workbook/monitoring/
    quote: "Google’s approach has evolved over time toward convergence on a single framework run centrally as a service."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-07
    claim: "The SRE book says the four golden signals of monitoring are latency, traffic, errors and saturation."
    type: fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.6 Monitoring Distributed Systems"
      url: https://sre.google/sre-book/monitoring-distributed-systems/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "The four golden signals of monitoring are latency, traffic, errors, and saturation."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-08
    claim: "The SRE book says Google SRE combines heavy use of white-box monitoring with modest but critical uses of black-box monitoring."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.6 Monitoring Distributed Systems"
      url: https://sre.google/sre-book/monitoring-distributed-systems/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261009042224/https://sre.google/sre-book/monitoring-distributed-systems/
    quote: "We combine heavy use of white-box monitoring with modest but critical uses of black-box monitoring."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-09
    claim: "The SRE book says text logs help with reactive debugging in real time, while storing logs in a structured binary format can make it possible to build tools for retrospective analysis."
    type: fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.12 Effective Troubleshooting"
      url: https://sre.google/sre-book/effective-troubleshooting/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "Text logs are very helpful for reactive debugging in real time, while storing logs in a structured binary format can make it possible to build tools to conduct retrospective analysis with much more information."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check-2.md
      result: supported
  - id: 09-10
    claim: "The SRE book says Google servers have endpoints that show a sample of recently sent or received RPCs."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.12 Effective Troubleshooting"
      url: https://sre.google/sre-book/effective-troubleshooting/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260908010650/https://sre.google/sre-book/effective-troubleshooting/
    quote: "For example, Google servers have endpoints that show a sample of RPCs recently sent or received, so it’s possible to understand how any one server is communicating with others without referencing an architecture diagram."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-21
    claim: "The SRE book says Borgmon rules can query the history of a single time-series, query different subsets of labels from many time-series at once, and apply many mathematical operations."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.10 Practical Alerting from Time-Series Data"
      url: https://sre.google/sre-book/practical-alerting/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260806204024/https://sre.google/sre-book/practical-alerting/
    quote: "These rules can be quite powerful because they can query the history of a single time-series (i.e., the time axis), query different subsets of labels from many time-series at once (i.e., the space axis), and apply many mathematical operations."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-22
    claim: "The SRE book says the Viceroy project began in 2012, when a number of teams were considering how to move to Monarch, the new monitoring system at Google."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.31 Communication and Collaboration in SRE"
      url: https://sre.google/sre-book/communication-and-collaboration/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260910213235/https://sre.google/sre-book/communication-and-collaboration/
    quote: "It began in 2012 when a number of teams were considering how to move to Monarch, the new monitoring system at Google."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check-2.md
      result: supported
  - id: 09-23
    claim: "The Workbook says Viceroy, a separate dashboarding service, could display graphs based on data from both Borgmon and Monarch, so users could migrate gradually from Borgmon to Monarch."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.4 Monitoring"
      url: https://sre.google/workbook/monitoring/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260909103330/https://sre.google/workbook/monitoring/
    quote: "Since users could use Viceroy to display graphs based on data from both monitoring systems, they could gradually migrate from Borgmon to Monarch."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check-2.md
      result: supported
  - id: 09-24
    claim: "The Workbook says other monitoring systems are now adopting the Prometheus format, which is being standardized as OpenMetrics."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.4 Monitoring"
      url: https://sre.google/workbook/monitoring/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "Other systems are now adopting the Prometheus format, and it is being standardized as OpenMetrics"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-25
    claim: "The Workbook strongly recommends treating monitoring configuration as code."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.4 Monitoring"
      url: https://sre.google/workbook/monitoring/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "We strongly recommend also treating monitoring configuration as code"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-26
    claim: "The SRE book names Dapper as a tool for tracing requests through the whole stack to understand a distributed system, and says tracing designs differ by use case."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.12 Effective Troubleshooting"
      url: https://sre.google/sre-book/effective-troubleshooting/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260908010650/https://sre.google/sre-book/effective-troubleshooting/
    quote: "Tracing requests through the whole stack using tools such as Dapper [Sig10] provides a very powerful way to understand how a distributed system is working, though varying use cases imply significantly different tracing designs"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-09-author-check-3.md
      result: supported
---

# Metrics, logging and tracing tools in Google's SRE books

## Summary

The SRE book and the Workbook describe Google's internal monitoring stack and its open source counterparts. Borgmon, the older system, scrapes /varz endpoints and keeps time-series data in memory. Monarch is its successor, and Viceroy is a separate dashboarding service. Dapper is named as a request-tracing tool.

## Key points

- Borgmon was built shortly after Borg in 2003. It scrapes a /varz URI from each target, stores the data in an in-memory database and evaluates rules over time-series (09-01, 09-02, 09-03, 09-21).
- Monarch is described as Google's new monitoring system. Viceroy is a separate dashboarding service that showed data from both Borgmon and Monarch, so teams could migrate gradually (09-22, 09-23). The Workbook says Google has converged on one centrally run framework (09-06).
- Open source tools named: Prometheus, Riemann, Heka and Bosun as Borgmon-like tools (09-04), the Prometheus format and OpenMetrics (09-24), and grafanalib for monitoring configuration as code (09-05, 09-25).
- The four golden signals are latency, traffic, errors and saturation (09-07). Google SRE combines heavy white-box monitoring with modest but critical black-box monitoring (09-08).
- For debugging, the books describe text and structured logs (09-09), per-server endpoints that show recent RPCs (09-10) and Dapper for request tracing (09-26).
