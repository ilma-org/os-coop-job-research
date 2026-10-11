---
doc_type: topic-note
topic: 11-os-course-concepts
title: "Distributed failure detection and recovery for SRE"
updated: 2026-10-11
claims:
  - id: 11-31
    claim: "Based on probe results, Kubernetes can restart unhealthy containers or stop sending traffic to containers that are not ready."
    type: fact
    status: human-verified
    source:
      title: "Kubernetes documentation: Liveness, Readiness, and Startup Probes"
      url: https://kubernetes.io/docs/concepts/workloads/pods/probes/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "Based on the probe results, Kubernetes can restart unhealthy containers or stop sending traffic to containers that are not ready."
    os_concepts: ["distributed systems", "failure detection", "recovery"]
    pr: null
    ai_check:
      platform: Codex
      model: "gpt-6.1-sol"
      prompt_log: prompts/2026-10-11-TonCS05-11-course-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-11-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-11
      result: pass
      opened_source: true
  - id: 11-32
    claim: "The SRE book recommends limiting retries per request rather than retrying indefinitely."
    type: fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Chapter 22: Addressing Cascading Failures"
      url: https://sre.google/sre-book/addressing-cascading-failures/
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "Limit retries per request. Don’t retry a given request indefinitely."
    os_concepts: ["distributed systems", "recovery", "overload"]
    pr: null
    ai_check:
      platform: Codex
      model: "gpt-6.1-sol"
      prompt_log: prompts/2026-10-11-TonCS05-11-course-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-11-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-11
      result: pass
      opened_source: true
  - id: 11-33
    claim: "Recommended course connection: relate periodic health probes to the lecture failure-detection model, distinguish an observed failed check from a confirmed root cause, and compare traffic removal with container restart as different responses. Test bounded retries in the hypothetical service rather than assuming retries always restore availability. This is a proposed exercise, not evidence of Google deployment."
    type: assumption
    status: unverified
    os_concepts: ["distributed systems", "failure detection", "recovery"]
    pr: null
---

# "Distributed failure detection and recovery for SRE"

## Summary

Kubernetes can restart unhealthy containers or stop traffic to containers that are not ready based on probe results (11-31). The SRE book recommends bounded retries (11-32). The proposed exercise connects these examples to the course's failure-detection and recovery model without asserting a Google deployment (11-33).

## Key points

- Probe results can lead to container restart or traffic removal. (11-31)
- The SRE book recommends limiting retries per request. (11-32)
- Recommended connection: distinguish failed checks from confirmed causes, compare recovery responses and test bounded retries. (11-33)

## Proposed connection to SRE work

Apply these mechanisms to the hypothetical workload in 11-23 (11-31 to 11-33). This is an application of the course model, not a claim that a Kubernetes probe is identical to the lecture heartbeat protocol. Kubernetes and the SRE book provide complementary examples, not evidence of the complete proposed deployment.
