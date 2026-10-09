---
doc_type: topic-note
topic: 05-hardware-requirements
title: "Firmware, BIOS and CPU platforms in Google's fleet"
updated: 2026-10-09
claims:
  - id: 05-12
    claim: "Building Secure and Reliable Systems gives a machine and its BIOS, and a network interface card (NIC) and its firmware, as examples of hardware devices with their own firmware."
    type: fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.9 Design for Recovery"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch09.html
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "a machine and its BIOS, or a network interface card (NIC) and its firmware"
    os_concepts: ["booting"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-13
    claim: "Building Secure and Reliable Systems says Google manages the firmware on its machines with the same systems and processes it uses to manage host software updates."
    type: org-fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.9 Design for Recovery"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch09.html
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260616012631/https://google.github.io/building-secure-and-reliable-systems/raw/ch09.html
    quote: "same systems and processes that we use to manage updates to our host software"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-14
    claim: "Building Secure and Reliable Systems says Google's automation securely distributes the intended state for all firmware as a package."
    type: org-fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.9 Design for Recovery"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch09.html
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260616012631/https://google.github.io/building-secure-and-reliable-systems/raw/ch09.html
    quote: "Automation securely distributes the intended state for all the firmware as a package"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-15
    claim: "Building Secure and Reliable Systems lists Arm and x86 CPUs, and UEFI and bare-metal firmware, among the environments where Google implements a cryptographic key management protocol."
    type: org-fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, ch.9 Design for Recovery"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch09.html
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260616012631/https://google.github.io/building-secure-and-reliable-systems/raw/ch09.html
    quote: "Arm and x86 CPUs, UEFI and bare-metal firmware"
    os_concepts: ["booting"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-16
    claim: "In an SRE book incident where automation sent machines to have their disks erased, the BIOS on the affected machines either halted or went into a constant reboot cycle."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.13 Emergency Response"
      url: https://sre.google/sre-book/emergency-response/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260915061328/https://sre.google/sre-book/emergency-response/
    quote: "the BIOS either halted or went into a constant reboot cycle"
    os_concepts: ["booting"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-17
    claim: "The SRE book recounts an automation bug after which Diskerase wiped the disks on all machines in Google's CDN."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.7 The Evolution of Automation at Google"
      url: https://sre.google/sre-book/automation-at-google/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260910213452/https://sre.google/sre-book/automation-at-google/
    quote: "the highly efficient Diskerase wiped the disks on all machines in our CDN"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-24
    claim: "Google's infrastructure security design overview says Google designs custom chips, including a hardware security chip called Titan."
    type: org-fact
    status: ai-checked
    source:
      title: "Google Cloud, Google infrastructure security design overview"
      url: https://docs.cloud.google.com/docs/security/infrastructure/design
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260923013749/https://docs.cloud.google.com/docs/security/infrastructure/design
    quote: "We also design custom chips, including a hardware security chip (called Titan"
    os_concepts: ["security"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-25
    claim: "Google's infrastructure security design overview says these chips let Google authenticate legitimate Google devices at the hardware level and serve as hardware roots of trust."
    type: org-fact
    status: ai-checked
    source:
      title: "Google Cloud, Google infrastructure security design overview"
      url: https://docs.cloud.google.com/docs/security/infrastructure/design
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260923013749/https://docs.cloud.google.com/docs/security/infrastructure/design
    quote: "legitimate Google devices at the hardware level and serve as hardware roots of trust"
    os_concepts: ["security"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
  - id: 05-26
    claim: "Google's infrastructure security design overview says Google servers use various technologies to make sure they boot the intended software stack."
    type: org-fact
    status: ai-checked
    source:
      title: "Google Cloud, Google infrastructure security design overview"
      url: https://docs.cloud.google.com/docs/security/infrastructure/design
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260923013749/https://docs.cloud.google.com/docs/security/infrastructure/design
    quote: "Google servers use various technologies to ensure that they boot the intended software stack."
    os_concepts: ["booting"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-05-author-check.md
      result: supported
---

# Firmware, BIOS and CPU platforms in Google's fleet

## Summary

Building Secure and Reliable Systems treats firmware as part of the fleet's managed state. Machines have a BIOS and NICs have their own firmware, and Google manages firmware with the same systems it uses for host software, distributing the intended firmware state as a package (05-12 to 05-14). The environments Google names include Arm and x86 CPUs and UEFI and bare-metal firmware (05-15). Google's infrastructure security design overview adds that Google designs custom chips, including the Titan hardware security chip, which authenticate Google devices at the hardware level and serve as hardware roots of trust, and that Google servers use various technologies to boot the intended software stack (05-24 to 05-26). Two SRE book incidents show automation reaching the hardware layer: BIOS halts or reboot loops, and Diskerase wiping the disks of every machine in Google's CDN (05-16, 05-17).

## Key points

- Firmware (BIOS, NIC firmware) is managed like software, as a package with an intended state. (05-12, 05-13, 05-14)
- CPU architectures named: Arm and x86. Firmware named: UEFI and bare metal. (05-15)
- Hardware root of trust: Google's custom Titan chip authenticates devices, and servers check that they boot the intended software stack. (05-24, 05-25, 05-26)
- Automation mistakes can reach disks and boot firmware. (05-16, 05-17)

## Sources and limits

Round 1 used only the three books on https://sre.google/books/. Round 2 adds current official pages: Google Cloud documentation and blog posts, Google's data center site, and, for practice hardware, the Debian installation guide and the minikube documentation. The SRE book page footer says copyright 2017 and the Workbook page footer says copyright 2018; the Building Secure and Reliable Systems pages show no date. Each claim describes what its source says at the time of that source. Quotes are kept short on purpose; open the source to read the full passage.
