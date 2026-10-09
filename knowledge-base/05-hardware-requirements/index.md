---
doc_type: topic-index
topic: 05-hardware-requirements
title: Hardware requirements
assignment_section: "4.3"
report_sections: [7]
owner: "@csinside"
issue: 10
updated: 2026-10-09
---

# Hardware requirements

What hardware and infrastructure the operating systems run on.

## Scope

- Server and cloud instance hardware (CPU architecture, memory, storage, network)
- Engineer workstation requirements
- Network and storage hardware an SRE meets
- Hardware for hands-on practice before applying

## Notes in this directory

The owner organizes notes (`topic-note` files) here. List them below as they are added.

<!-- notes:start -->
- [datacenter-hardware.md](datacenter-hardware.md): Google datacenter hardware, network and storage. 14 claims (05-01 to 05-11, 05-22 to 05-23, 05-36): 12 ai-checked, 2 unverified.
- [firmware-and-cpu-platforms.md](firmware-and-cpu-platforms.md): Firmware, BIOS and CPU platforms in Google's fleet. 9 claims (05-12 to 05-17, 05-24 to 05-26): 9 ai-checked.
- [sizing-and-practice-hardware.md](sizing-and-practice-hardware.md): Machine sizing numbers and hardware for practice. 6 claims (05-18 to 05-21, 05-34 to 05-35): 5 ai-checked, 1 unverified.
- [google-cloud-instance-hardware.md](google-cloud-instance-hardware.md): CPU platforms and accelerators on Google Cloud. 7 claims (05-27 to 05-33): 5 ai-checked, 2 unverified.
<!-- notes:end -->

## Sources covered so far

Round 1 used only the three books on https://sre.google/books/. Chapters cited by claims: SRE book ch.2, 7, 13, 20; Workbook ch.10, 12; Building Secure and Reliable Systems ch.9. The same 79-page plain-text search as topic 04 was used, with hardware terms (CPU, RAM, disk, SSD, rack, switch, firmware, BIOS, x86, Arm).

Round 2 added current official pages: the Google infrastructure security design overview, the Google Data Centers site, the Compute Engine CPU platform and GPU documentation, the Cloud TPU introduction, the Debian installation guide (hardware requirements) and the minikube documentation.

## Not found yet

These items still have no opened source. Do not put them in the report as facts.

- CPU models, memory sizes and disk sizes of Google's internal production machines. The Workbook numbers (05-18, 05-19) are exercise assumptions, and the Google Cloud pages (05-27 to 05-33) describe customer instances.
- Hardware requirements for an SRE's own workstation.
- Hardware for student practice: 05-21 stays an assumption, now based on cited minimums (05-34, 05-35).
