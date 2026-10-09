---
doc_type: topic-note
topic: 05-hardware-requirements
title: "Google datacenter hardware, network and storage"
updated: 2026-10-09
claims:
  - id: 05-01
    claim: "The SRE book says most of Google's compute resources are in Google-designed datacenters with proprietary power distribution, cooling, networking and compute hardware."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "Google-designed datacenters with proprietary power distribution, cooling, networking, and compute hardware"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-02
    claim: "In its main text, the SRE book says the compute hardware in a Google-designed datacenter is the same across the board; a footnote on that sentence qualifies it as roughly the same, mostly."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "the compute hardware in a Google-designed datacenter is the same across the board"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check-2.md
      result: supported
  - id: 05-03
    claim: "The SRE book's chapter on load balancing in the datacenter says not all machines in the same datacenter are necessarily the same."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.20 Load Balancing in the Datacenter"
      url: https://sre.google/sre-book/load-balancing-datacenter/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20261001130414/https://sre.google/sre-book/load-balancing-datacenter/
    quote: "not all machines in the same datacenter are necessarily the same"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-04
    claim: "The SRE book says tens of machines are placed in a rack in a Google datacenter."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "Tens of machines are placed in a rack"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-05
    claim: "The SRE book says a Google datacenter building usually houses multiple clusters."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "Usually a datacenter building houses multiple clusters."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-06
    claim: "The SRE book says that in a single Google cluster in a typical year, thousands of machines fail and thousands of hard disks break."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "in a typical year, thousands of machines fail and thousands of hard disks break"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-07
    claim: "The SRE book says Google built its Jupiter datacenter network by connecting hundreds of Google-built switches in a Clos network fabric."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "connecting hundreds of Google-built switches in a Clos network fabric"
    os_concepts: ["networking"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-08
    claim: "The SRE book says Jupiter supports 1.3 Pbps of bisection bandwidth among servers in its largest configuration."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "In its largest configuration, Jupiter supports 1.3 Pbps bisection bandwidth among servers."
    os_concepts: ["networking"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-09
    claim: "The SRE book says Google's datacenters are connected to each other by its globe-spanning backbone network, B4."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "Datacenters are connected to each other with our globe-spanning backbone network B4"
    os_concepts: ["networking"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-10
    claim: "The SRE book says D, the lowest layer of Google's storage stack, uses both spinning disks and flash storage."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "D uses both spinning disks and flash storage"
    os_concepts: ["file systems"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-11
    claim: "The SRE Workbook says that besides its proprietary datacenters, Google has racks of proxy/cache machines in colocation facilities (colos)."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.10 Postmortem Culture: Learning from Failure"
      url: https://sre.google/workbook/postmortem-culture/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20261001130312/https://sre.google/workbook/postmortem-culture/
    quote: "racks of proxy/cache machines in colocation facilities (or “colos”)"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-22
    claim: "Google's infrastructure security design overview says Google designs its server boards and networking equipment."
    type: org-fact
    status: ai-checked
    source:
      title: "Google Cloud, Google infrastructure security design overview"
      url: https://docs.cloud.google.com/docs/security/infrastructure/design
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260923013749/https://docs.cloud.google.com/docs/security/infrastructure/design
    quote: "We design the server boards and the networking equipment."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-23
    claim: "Google's data center website says Google custom builds servers exclusively for its data centers."
    type: org-fact
    status: ai-checked
    source:
      title: "Google Data Centers, homepage"
      url: https://datacenters.google/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260928062836/https://datacenters.google/
    quote: "We custom build servers exclusively for our data centers"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-36
    claim: "A footnote in the SRE book says some Google datacenters end up with multiple generations of compute hardware."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-09
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "Some datacenters end up with multiple generations of compute hardware"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check-2.md
      result: supported
---

# Google datacenter hardware, network and storage

## Summary

The SRE book says most of Google's compute runs in Google-designed datacenters with proprietary power distribution, cooling, networking and compute hardware, with tens of machines per rack and usually several clusters per building (05-01, 05-04, 05-05). Current Google pages say Google designs its server boards and networking equipment and custom builds servers exclusively for its data centers (05-22, 05-23). The SRE book's main text says the compute hardware in a datacenter is the same across the board, but its own footnote says some datacenters end up with multiple generations of compute hardware, which matches its load-balancing chapter: machines in one datacenter are not necessarily the same (05-02, 05-36, 05-03). Hardware fails often: thousands of machines and thousands of disks per cluster in a typical year (05-06). The network is Jupiter, a Clos fabric of Google-built switches, plus the B4 backbone between datacenters; storage uses spinning disks and flash; and proxy/cache racks sit in colocation facilities (05-07 to 05-11).

## Key points

- Google designs its own datacenters and hardware: power, cooling, network, server boards and networking equipment, with servers custom built for its data centers. (05-01, 05-22, 05-23)
- Topology: tens of machines per rack, and usually several clusters per datacenter building. (05-04, 05-05)
- Hardware is mostly uniform but not identical: some datacenters have several hardware generations, and machines in one datacenter can differ. (05-02, 05-36, 05-03)
- Hardware failure is routine at this scale. (05-06)
- Network: Jupiter (Clos fabric, 1.3 Pbps bisection bandwidth at its largest) inside datacenters, and B4 between them. (05-07, 05-08, 05-09)
- Storage hardware: spinning disks and flash under the D layer. (05-10)
- Edge: racks of proxy/cache machines in colos. (05-11)

## Notes for the write-up

- Write "Google-designed" or "custom-built", not "identical". The SRE book's own footnote (05-36) qualifies 05-02, and Google Cloud documents several CPU platforms (05-27 to 05-30).

## Sources and limits

Round 1 used only the three books on https://sre.google/books/. Round 2 adds current official pages: Google Cloud documentation and blog posts, Google's data center site, and, for practice hardware, the Debian installation guide and the minikube documentation. The SRE book page footer says copyright 2017 and the Workbook page footer says copyright 2018; the Building Secure and Reliable Systems pages show no date. Each claim describes what its source says at the time of that source. Quotes are kept short on purpose; open the source to read the full passage.
