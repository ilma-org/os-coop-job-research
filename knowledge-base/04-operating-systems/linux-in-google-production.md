---
doc_type: topic-note
topic: 04-operating-systems
title: "Linux and the cluster operating system in Google production"
updated: 2026-10-09
claims:
  - id: 04-01
    claim: "Building Secure and Reliable Systems says the Linux kernel underpins much of Google's production infrastructure."
    type: org-fact
    status: human-verified
    source:
      title: "Building Secure and Reliable Systems, ch.16 Disaster Planning"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch16.html
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260420235255/https://google.github.io/building-secure-and-reliable-systems/raw/ch16.html
    quote: "the Linux kernel, which underpins much of our production infrastructure"
    os_concepts: ["kernel"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-09
      result: pass
      opened_source: true
  - id: 04-02
    claim: "Building Secure and Reliable Systems says Google has an internal Linux distribution and describes how its rollout evolved."
    type: org-fact
    status: human-verified
    source:
      title: "Building Secure and Reliable Systems, ch.9 Design for Recovery"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch09.html
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260616012631/https://google.github.io/building-secure-and-reliable-systems/raw/ch09.html
    quote: "the rollout of our internal Linux distribution evolved"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-09
      result: pass
      opened_source: true
  - id: 04-03
    claim: "Building Secure and Reliable Systems says Google installed all the machines in its datacenters with a \"base\" or \"golden\" image."
    type: org-fact
    status: human-verified
    source:
      title: "Building Secure and Reliable Systems, ch.9 Design for Recovery"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch09.html
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260616012631/https://google.github.io/building-secure-and-reliable-systems/raw/ch09.html
    quote: "Google installed all the machines in our datacenters with a “base” or “golden” image"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-09
      result: pass
      opened_source: true
  - id: 04-04
    claim: "Building Secure and Reliable Systems says Google later designed more granular release units for its machines, one for each software package."
    type: org-fact
    status: human-verified
    source:
      title: "Building Secure and Reliable Systems, ch.9 Design for Recovery"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch09.html
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260616012631/https://google.github.io/building-secure-and-reliable-systems/raw/ch09.html
    quote: "We designed more granular release units that corresponded to each software package."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-09
      result: pass
      opened_source: true
  - id: 04-05
    claim: "The SRE book says resource allocation in Google's datacenters is handled by Borg, which it calls Google's cluster operating system."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "resource allocation is handled by our cluster operating system, Borg"
    os_concepts: ["resource allocation"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-09
      result: pass
      opened_source: true
  - id: 04-06
    claim: "The SRE Workbook says Borg is Google's internal container management system and that it runs huge numbers of Linux containers."
    type: org-fact
    status: human-verified
    source:
      title: "The Site Reliability Workbook, ch.7 Simplicity"
      url: https://sre.google/workbook/simplicity/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260701072242/https://sre.google/workbook/simplicity/
    quote: "Borg is Google’s internal container management system. It runs huge numbers of Linux containers"
    os_concepts: ["containers"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-09
      result: pass
      opened_source: true
  - id: 04-07
    claim: "Building Secure and Reliable Systems says that inside a Borg alloc, one or more sets of Linux processes can be run in a container."
    type: org-fact
    status: human-verified
    source:
      title: "Building Secure and Reliable Systems, ch.14 Deploying Code"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch14.html
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260923141205/https://google.github.io/building-secure-and-reliable-systems/raw/ch14.html
    quote: "one or more sets of Linux processes can be run in a container"
    os_concepts: ["processes", "containers"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-09
      result: pass
      opened_source: true
  - id: 04-08
    claim: "The SRE book uses \"node\" and \"machine\" interchangeably for a single instance of a running kernel, whether on a physical server, a virtual machine or a container."
    type: fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, ch.6 Monitoring Distributed Systems"
      url: https://sre.google/sre-book/monitoring-distributed-systems/
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "instance of a running kernel in either a physical server, virtual machine, or container"
    os_concepts: ["kernel", "virtualization", "containers"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-09
      result: pass
      opened_source: true
  - id: 04-26
    claim: "A 2013 USENIX LISA paper by Google engineer Marc Merlin says Google's server applications run in a different partition from the base Linux distribution that boots the machine."
    type: org-fact
    status: human-verified
    source:
      title: "Marc Merlin (Google), Live Upgrading Thousands of Servers from an Ancient Red Hat Distribution to 10 Year Newer Debian Based One, USENIX LISA '13"
      url: https://www.usenix.org/conference/lisa13/technical-sessions/presentation/merlin
      kind: paper
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20251115140621/https://www.usenix.org/conference/lisa13/technical-sessions/presentation/merlin
    quote: "running in a different partition than the base Linux distribution that boots the machine"
    os_concepts: ["file systems", "booting"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-09
      result: pass
      opened_source: true
  - id: 04-27
    claim: "The same 2013 LISA paper describes a difficult upgrade of Google's servers from a Red Hat 7.1 image snapshot with layers of patches."
    type: org-fact
    status: human-verified
    source:
      title: "Marc Merlin (Google), Live Upgrading Thousands of Servers from an Ancient Red Hat Distribution to 10 Year Newer Debian Based One, USENIX LISA '13"
      url: https://www.usenix.org/conference/lisa13/technical-sessions/presentation/merlin
      kind: paper
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20251115140621/https://www.usenix.org/conference/lisa13/technical-sessions/presentation/merlin
    quote: "a difficult upgrade from a Red Hat 7.1 image snapshot with layers of patches"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-09
      result: pass
      opened_source: true
  - id: 04-28
    claim: "The same 2013 LISA paper says the target of that upgrade was a Debian Testing based distribution built from source."
    type: org-fact
    status: human-verified
    source:
      title: "Marc Merlin (Google), Live Upgrading Thousands of Servers from an Ancient Red Hat Distribution to 10 Year Newer Debian Based One, USENIX LISA '13"
      url: https://www.usenix.org/conference/lisa13/technical-sessions/presentation/merlin
      kind: paper
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20251115140621/https://www.usenix.org/conference/lisa13/technical-sessions/presentation/merlin
    quote: "to a Debian Testing based distribution built from source"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-09
      result: pass
      opened_source: true
  - id: 04-29
    claim: "The same 2013 LISA paper says the distribution change was done as a live upgrade, without a long \"flag day\"."
    type: org-fact
    status: human-verified
    source:
      title: "Marc Merlin (Google), Live Upgrading Thousands of Servers from an Ancient Red Hat Distribution to 10 Year Newer Debian Based One, USENIX LISA '13"
      url: https://www.usenix.org/conference/lisa13/technical-sessions/presentation/merlin
      kind: paper
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20251115140621/https://www.usenix.org/conference/lisa13/technical-sessions/presentation/merlin
    quote: "achieved as a live upgrade and without ending up with a long \"flag day\""
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-09
      result: pass
      opened_source: true
  - id: 04-30
    claim: "Google Cloud's \"What are containers?\" page says everything at Google, from Gmail to YouTube to Search, runs in containers."
    type: org-fact
    status: human-verified
    source:
      title: "Google Cloud, What are containers?"
      url: https://cloud.google.com/learn/what-are-containers
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20261004203701/https://cloud.google.com/learn/what-are-containers
    quote: "From Gmail to YouTube to Search, everything at Google runs in containers."
    os_concepts: ["containers"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-09
      result: pass
      opened_source: true
  - id: 04-31
    claim: "Google Cloud's \"Containers at Google\" page says Google has been using containers since the early 2000s."
    type: org-fact
    status: human-verified
    source:
      title: "Google Cloud, Containers at Google"
      url: https://cloud.google.com/containers
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260927102824/https://cloud.google.com/containers
    quote: "Google has been using containers since the early 2000s"
    os_concepts: ["containers"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-09
      result: pass
      opened_source: true
  - id: 04-32
    claim: "Google Cloud's \"What are containers?\" page says Google contributed cgroups to the Linux kernel."
    type: org-fact
    status: human-verified
    source:
      title: "Google Cloud, What are containers?"
      url: https://cloud.google.com/learn/what-are-containers
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20261004203701/https://cloud.google.com/learn/what-are-containers
    quote: "from the early days of contributing cgroups to the Linux kernel"
    os_concepts: ["kernel", "resource isolation"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-04-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-09-nine14282-04-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-09
      result: pass
      opened_source: true
---

# Linux and the cluster operating system in Google production

## Summary

Google's books say the Linux kernel underpins much of Google's production infrastructure and that Google has an internal Linux distribution, first installed as a "golden" image and later released per software package (04-01 to 04-04). A 2013 USENIX paper by a Google engineer adds history: Google's servers were live-upgraded from a Red Hat 7.1 image to a Debian Testing based distribution built from source, and applications run in a separate partition from the base distribution (04-26 to 04-29). Google says everything at Google runs in containers, that it has used containers since the early 2000s, and that it contributed cgroups to the Linux kernel (04-30 to 04-32). Borg, which the SRE book calls Google's cluster operating system, runs huge numbers of Linux containers (04-05 to 04-07).

## Key points

- Production servers run Linux, and Google has an internal Linux distribution. (04-01, 04-02)
- Server distribution history: a Red Hat 7.1 image snapshot was live-upgraded to a Debian Testing based distribution built from source; later, Google moved from monthly "golden" images to release units per package. (04-03, 04-04, 04-27, 04-28, 04-29)
- Server applications run in a different partition from the base Linux distribution that boots the machine. (04-26)
- Everything at Google runs in containers, and has since the early 2000s; Google contributed cgroups to the Linux kernel. (04-30, 04-31, 04-32)
- Borg is called Google's cluster operating system. It allocates resources and runs huge numbers of Linux containers; inside a Borg alloc, sets of Linux processes run in a container. (04-05, 04-06, 04-07)
- The SRE book's "machine" or "node" is one running kernel instance, and its list includes containers; but containers share the OS kernel. (04-08, 04-33)

## Notes for the write-up

- Define a node as a physical server or a VM running its own kernel. Containers on that node share its kernel (04-33), so do not repeat the book's wording in 04-08 without that correction.
- Do not write that Borg uses cgroups. Google says it contributed cgroups to Linux (04-32) and that Borg runs Linux containers (04-06), but no opened source links the two.
- Do not write that the distribution in Building Secure and Reliable Systems (04-02) is the Debian-based one in the 2013 paper (04-28). No source says they are the same.
- The 2013 paper is a USENIX publication by a Google engineer, not a Google web page. The team should confirm that it is acceptable evidence for an org-fact.

## Sources and limits

Round 1 used only the three books on https://sre.google/books/. Round 2 adds official Google pages (Google Cloud documentation and the Google Cloud Blog), the Linux kernel documentation, the gVisor documentation and one USENIX paper by a Google engineer. The SRE book page footer says copyright 2017 and the Workbook page footer says copyright 2018; the Building Secure and Reliable Systems pages show no date. Each claim describes what its source says at the time of that source, not necessarily current practice. Quotes are kept short on purpose; open the source to read the full passage.
