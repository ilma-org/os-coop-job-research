---
doc_type: topic-note
topic: 09-monitoring-and-incident-tools
title: "Alerting, paging and on-call tools in Google's SRE books"
updated: 2026-10-14
claims:
  - id: 09-27
    claim: "The SRE book says the Alertmanager, which Borgmon connects to, is responsible for routing alert notifications to the correct destination."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.10 Practical Alerting from Time-Series Data"
      url: https://sre.google/sre-book/practical-alerting/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260806204024/https://sre.google/sre-book/practical-alerting/
    quote: "The Alertmanager is responsible for routing the alert notification to the correct destination."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-28
    claim: "The SRE book says Google teams send page-worthy alerts to their on-call rotation and important but subcritical alerts to their ticket queues."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.10 Practical Alerting from Time-Series Data"
      url: https://sre.google/sre-book/practical-alerting/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260806204024/https://sre.google/sre-book/practical-alerting/
    quote: "teams send their page-worthy alerts to their on-call rotation and their important but subcritical alerts to their ticket queues."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-29
    claim: "The SRE book says Google teams use a tool called Prober, which runs a protocol check against a target and reports success or failure, to cover what white-box monitoring cannot see."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.10 Practical Alerting from Time-Series Data"
      url: https://sre.google/sre-book/practical-alerting/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260806204024/https://sre.google/sre-book/practical-alerting/
    quote: "Teams at Google solve this coverage issue with Prober, which runs a protocol check against a target and reports success or failure."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-30
    claim: "The Workbook says that, for SLO-based alerting, a significant event is an event that consumes a large fraction of the error budget."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.5 Alerting on SLOs"
      url: https://sre.google/workbook/alerting-on-slos/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "an event that consumes a large fraction of the error budget."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-31
    claim: "The Workbook says multiple burn-rate alerts let an alert be given an appropriate priority based on how quickly a response is needed."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.5 Alerting on SLOs"
      url: https://sre.google/workbook/alerting-on-slos/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "Multiple burn rates allow you to adjust the alert to give appropriate priority based on how quickly you have to respond."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-32
    claim: "The SRE book says all alert notifications for Google SRE share a central replicated system that tracks whether a human has acknowledged receipt."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.16 Tracking Outages"
      url: https://sre.google/sre-book/tracking-outages/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260913212844/https://sre.google/sre-book/tracking-outages/
    quote: "At Google, all alert notifications for SRE share a central replicated system that tracks whether a human has acknowledged receipt of the notification."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-33
    claim: "The SRE book says that, when no acknowledgment arrives within a configured interval, this system escalates to the next configured destination, for example from primary on-call to secondary."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.16 Tracking Outages"
      url: https://sre.google/sre-book/tracking-outages/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260913212844/https://sre.google/sre-book/tracking-outages/
    quote: "If no acknowledgment is received after a configured interval, the system escalates to the next configured destination(s)—e.g., from primary on-call to secondary."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-34
    claim: "The SRE book says Outalator is Google's outage tracker: it passively receives all alerts sent by monitoring systems and lets users annotate, group and analyze them."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.16 Tracking Outages"
      url: https://sre.google/sre-book/tracking-outages/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260913212844/https://sre.google/sre-book/tracking-outages/
    quote: "Outalator is a system that passively receives all alerts sent by our monitoring systems and allows us to annotate, group, and analyze this data."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-35
    claim: "The SRE book says the Outalator can combine multiple escalating notifications (alerts) into a single entity (an incident)."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.16 Tracking Outages"
      url: https://sre.google/sre-book/tracking-outages/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260913212844/https://sre.google/sre-book/tracking-outages/
    quote: "Multiple escalating notifications (\"alerts\") can be combined into a single entity (\"incident\") in the Outalator."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-36
    claim: "The SRE book says many organizations use messaging systems such as Slack, Hipchat or IRC for internal communication or status dashboards, and that these are good places to hook into an outage tracker like Outalator."
    type: fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.16 Tracking Outages"
      url: https://sre.google/sre-book/tracking-outages/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "Many organizations use messaging systems like Slack, Hipchat, or even IRC for internal communication and/or updating status dashboards. These systems are great places to hook into with a system like Outalator."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-37
    claim: "The SRE book says Google SRE strives to invest at least 50% of SRE time in engineering, and of the remainder no more than 25% can be spent on-call."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.11 Being On-Call"
      url: https://sre.google/sre-book/being-on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261011073700/https://sre.google/sre-book/being-on-call/
    quote: "we strive to invest at least 50% of SRE time into engineering: of the remainder, no more than 25% can be spent on-call, leaving up to another 25% on other types of operational, nonproject work."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-09-author-check-3.md
      result: supported
  - id: 09-38
    claim: "The SRE book says many Google SRE teams have both a primary and a secondary on-call rotation."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.11 Being On-Call"
      url: https://sre.google/sre-book/being-on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261011073700/https://sre.google/sre-book/being-on-call/
    quote: "Many teams have both a primary and a secondary on-call rotation."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-39
    claim: "The Workbook says that in Google SRE a playbook entry is usually created whenever an alert is created."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.8 On-Call"
      url: https://sre.google/workbook/on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20261011015106/https://sre.google/workbook/on-call/
    quote: "In SRE, whenever an alert is created, a corresponding playbook entry is usually created."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-40
    claim: "The Workbook says aggregating change information into a searchable timeline helps correlate bugs with the changes that caused them, and names the Slack plug-in for Jenkins as a tool that can help."
    type: fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.8 On-Call"
      url: https://sre.google/workbook/on-call/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "Aggregating change information into a searchable timeline makes it simpler (and hopefully quicker) to correlate new bugs with the corresponding change that introduced them. Tools like the Slack plug-in for Jenkins can be helpful."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-09-author-check.md
      result: supported
  - id: 09-46
    claim: "The SRE book says the central replicated system that tracks alert acknowledgment for Google SRE is called \"The Escalator\", and that it was first a largely transparent tool that received copies of emails sent to on-call aliases."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.16 Tracking Outages"
      url: https://sre.google/sre-book/tracking-outages/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20260913212844/https://sre.google/sre-book/tracking-outages/
    quote: "This system, called \"The Escalator,\" was initially designed as a largely transparent tool that received copies of emails sent to on-call aliases."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-09-author-check-3.md
      result: supported
---

# Alerting, paging and on-call tools in Google's SRE books

## Summary

The books describe how alerts flow from monitoring to people at Google. Borgmon sends alerts to the Alertmanager, page-worthy alerts go to on-call and others go to ticket queues. Two internal tools track notifications: the Escalator and the Outalator. The books also cap on-call time at 25% of an SRE's time and say alerts normally get a playbook entry.

## Key points

- The Alertmanager routes alerts. Page-worthy alerts go to the on-call rotation and important but subcritical alerts go to ticket queues. Prober checks a target from the outside (09-27, 09-28, 09-29).
- SLO-based alerting aims at events that consume a large fraction of the error budget. Multiple burn rates let an alert's priority match how fast a response is needed (09-30, 09-31).
- A central replicated system, called the Escalator, tracks acknowledgment of every alert and escalates, for example from primary to secondary on-call (09-32, 09-33, 09-46). The Outalator receives alerts passively, lets users annotate and group them, and treats a group as an incident (09-34, 09-35). Messaging tools such as Slack, Hipchat and IRC are suggested hook points for a similar tool (09-36).
- Google SRE strives to spend at least 50% of SRE time on engineering, and of the remainder no more than 25% can go to on-call. Many teams run a primary and a secondary rotation (09-37, 09-38).
- Alerts normally have a playbook entry (09-39). The Workbook names the Slack plug-in for Jenkins as a tool for a searchable timeline of changes (09-40).
