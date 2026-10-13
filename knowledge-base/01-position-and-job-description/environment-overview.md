---
doc_type: topic-note
topic: 01-position-and-job-description
title: "Environment overview"
updated: 2026-10-14
claims:
  - id: 01-79
    claim: "The Google SRE book says most of Google’s compute resources are in Google-designed datacenters with proprietary power distribution, cooling, networking, and compute hardware."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "Most of Google’s compute resources are in Google-designed datacenters with proprietary power distribution, cooling, networking, and compute hardware"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-80
    claim: "The Google SRE book says the compute hardware in a Google-designed datacenter is the same across the board."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "the compute hardware in a Google-designed datacenter is the same across the board."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
  - id: 01-81
    claim: "The Google SRE book says that in a single cluster in a typical year, thousands of machines fail and thousands of hard disks break."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "In a single cluster in a typical year, thousands of machines fail and thousands of hard disks break"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-83
    claim: "The Google SRE book says Google datacenters are connected to each other with a globe-spanning backbone network."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "Datacenters are connected to each other with our globe-spanning backbone network"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-84
    claim: "The Google SRE book says Google uses an OpenFlow-based software-defined network."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "we use an OpenFlow-based software-defined network"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-85
    claim: "The Google SRE book says resource allocation on Google machines is handled by its cluster operating system, Borg."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "resource allocation is handled by our cluster operating system, Borg"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-86
    claim: "The Google SRE book says that when Borg starts a job, it finds machines for the tasks and tells the machines to start the server program."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "When Borg starts a job, it finds machines for the tasks and tells the machines to start the server program."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-87
    claim: "The Google SRE book says that if a Borg task malfunctions, it is killed and restarted, possibly on a different machine."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "If a task malfunctions, it is killed and restarted, possibly on a different machine."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-88
    claim: "The Google SRE book says a layer called Colossus creates a cluster-wide filesystem with usual filesystem semantics, replication and encryption."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "A layer on top of D called Colossus creates a cluster-wide filesystem that offers usual filesystem semantics, as well as replication and encryption."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-89
    claim: "The Google SRE book says Bigtable is a NoSQL database system that can handle databases that are petabytes in size."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "is a NoSQL database system that can handle databases that are petabytes in size"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-90
    claim: "The Google SRE book says Google’s Global Software Load Balancer (GSLB) performs load balancing on three levels."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "Global Software Load Balancer (GSLB) performs load balancing on three levels"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-91
    claim: "The Google SRE book says the Chubby lock service handles locks across datacenter locations and uses the Paxos protocol for asynchronous consensus."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "Chubby handles these locks across datacenter locations. It uses the Paxos protocol for asynchronous Consensus"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-92
    claim: "The Google SRE book says Google runs many instances of its Borgmon monitoring program."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "we run many instances of our Borgmon monitoring program"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-93
    claim: "The Google SRE book says Google code is heavily multithreaded, so one task can easily use many cores."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "Our code is heavily multithreaded, so one task can easily use many cores."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-94
    claim: "The Google SRE book says every Google server has an HTTP server that provides diagnostics and statistics for a given task."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "every server has an HTTP server that provides diagnostics and statistics for a given task"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-96
    claim: "The Google SRE book says data is transferred to and from an RPC using protocol buffers."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "Data is transferred to and from an RPC using protocol buffers"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-97
    claim: "The Google SRE book says that, apart from a few groups with their own open source repositories, Google Software Engineers work from a single shared repository."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "Apart from a few groups that have their own open source repositories (e.g., Android and Chrome), Google Software Engineers work from a single shared repository"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-98
    claim: "The Google SRE book says all software is reviewed before being submitted."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "All software is reviewed before being submitted."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-99
    claim: "The Google SRE book says that each time a CL is submitted, tests run on all software that may depend on that CL, either directly or indirectly."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "Each time a CL is submitted, tests run on all software that may depend on that CL, either directly or indirectly."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-100
    claim: "The Google SRE book says each datacenter campus has teams dedicated to maintaining the hardware and datacenter infrastructure."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "Each datacenter campus has teams dedicated to maintaining the hardware and datacenter infrastructure"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-102
    claim: "The Google SRE book says a Google datacenter building usually houses multiple clusters."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "Usually a datacenter building houses multiple clusters"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-103
    claim: "The Google SRE book says that, in Google datacenters, one or more rows form a cluster."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "One or more rows form a cluster"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-104
    claim: "The Google SRE book says Google created a very fast virtual switch with tens of thousands of ports by connecting hundreds of Google-built switches in a Clos network fabric."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "we created a very fast virtual switch with tens of thousands of ports. We accomplished this by connecting hundreds of Google-built switches in a Clos network fabric"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 01-110
    claim: "The Google SRE book says all of Google’s services communicate using a Remote Procedure Call (RPC) infrastructure named Stubby."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-11
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "All of Google’s services communicate using a Remote Procedure Call (RPC) infrastructure named Stubby"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-bximai-01-position-author-check-3.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-13-nacs-970-01-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
---

# Environment overview

## Summary

The SRE book describes the environment Google SREs work in as Google-designed datacenters with uniform compute hardware, a cluster operating system called Borg, layered cluster storage, a software-defined network and a shared software infrastructure (01-79, 01-80, 01-85, 01-88, 01-84, 01-110). Services are managed by software because hardware failures are frequent (01-81, 01-86, 01-87). Engineers work from a single shared repository with mandatory review and automatic testing (01-97, 01-98, 01-99). This note is an overview and points to topics 04 to 09 for detail. All claims come from one chapter, the SRE book's production-environment chapter, and describe what that book says Google uses, not what any other company uses or what a COOP student would touch.

## Key points

- Hardware: most compute resources are in Google-designed datacenters with proprietary power distribution, cooling, networking and compute hardware; the compute hardware is the same across the board; each campus has teams dedicated to maintaining hardware and datacenter infrastructure. (01-79, 01-80, 01-100)
- Layout: one or more rows form a cluster, and a datacenter building usually houses multiple clusters. (01-103, 01-102)
- Failures: in a single cluster in a typical year, thousands of machines fail and thousands of hard disks break. (01-81)
- Network: a very fast virtual switch built from hundreds of Google-built switches in a Clos network fabric; datacenters are linked by a globe-spanning backbone; an OpenFlow-based software-defined network. (01-104, 01-83, 01-84)
- Cluster operating system: resource allocation is handled by Borg, which finds machines for a job's tasks and restarts a malfunctioning task, possibly on a different machine. (01-85, 01-86, 01-87)
- Storage: Colossus provides a cluster-wide filesystem with replication and encryption; Bigtable is a NoSQL database that can handle petabyte-size databases. (01-88, 01-89)
- Load balancing, locks and monitoring: GSLB balances load on three levels; Chubby handles locks across datacenter locations using Paxos; Google runs many instances of Borgmon. (01-90, 01-91, 01-92)
- Software infrastructure: code is heavily multithreaded; every server has an HTTP server for diagnostics and statistics; services communicate via the Stubby RPC infrastructure, and data is transferred to and from an RPC using protocol buffers. (01-93, 01-94, 01-110, 01-96)
- Development environment: Google Software Engineers work from a single shared repository (a few groups such as Android and Chrome excepted); all software is reviewed before submission; each submitted change triggers tests on dependent software. (01-97, 01-98, 01-99)

## Sources and limits

Used one chapter, SRE book ch.2 "The Production Environment at Google, from the Viewpoint of an SRE" from https://sre.google/books/. Only one source supports these claims, so they are not cross-checked here; topics 04 to 09 add other sources for operating systems, hardware, infrastructure and tools. The SRE book footer says copyright 2017, so each claim states what the book says, not necessarily current practice. Quotes are kept short; open the source for the full passage.

## Not found yet

- Hardware, operating systems and tools a COOP or intern SRE would actually use: no source in this round.
- Google's current internal environment after the 2017 book: no source in this round, so this note does not assume it.
