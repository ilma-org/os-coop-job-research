---
doc_type: topic-index
topic: 04-operating-systems
title: Operating systems required or recommended
assignment_section: "4.3"
report_sections: [6]
owner: "@csinside"
issue: 9
updated: 2026-10-09
---

# Operating systems required or recommended

Not only which OS is used, but why it is appropriate and how it is configured.

## Scope

- Which operating systems an SRE works with, and why they fit
- Distributions and kernel features relevant to the work
- How the OS is configured and operated in production
- Workstation OS versus server OS

## Notes in this directory

The owner organizes notes (`topic-note` files) here. List them below as they are added.

<!-- notes:start -->
- [linux-in-google-production.md](linux-in-google-production.md): Linux and the cluster operating system in Google production. 15 claims (04-01 to 04-08, 04-26 to 04-32): 15 ai-checked.
- [kernel-updates-and-os-logs.md](kernel-updates-and-os-logs.md): Kernel updates, live patching and OS logs in Google production. 7 claims (04-09 to 04-14, 04-43): 7 ai-checked.
- [isolation-and-resource-limits.md](isolation-and-resource-limits.md): Process isolation, sandboxing and OS resource limits. 18 claims (04-15 to 04-21, 04-33 to 04-41, 04-56 to 04-57): 18 ai-checked.
- [workstations-and-servers.md](workstations-and-servers.md): Engineer workstations versus production servers. 12 claims (04-22 to 04-25, 04-44 to 04-51): 11 ai-checked, 1 unverified.
- [google-cloud-container-os.md](google-cloud-container-os.md): Container-Optimized OS on Google Cloud. 4 claims (04-52 to 04-55): 4 ai-checked.
<!-- notes:end -->

## Sources covered so far

Round 1 used only the three books on https://sre.google/books/. Chapters cited by claims: SRE book ch.2, 6, 7, 22; Workbook ch.7; Building Secure and Reliable Systems ch.7, 8, 9, 14, 15, 16. To find them, 79 chapter pages were fetched as plain text and searched for OS terms (Linux, kernel, operating system, system call, container, workstation): the 34 SRE book chapters and two of its appendices, the 21 Workbook chapters, and the 22 Building Secure and Reliable Systems chapters. A second search of the same pages found no mention of a distribution name (Ubuntu, Red Hat, gLinux, Goobuntu), cgroups, namespaces, systemd, journald, gVisor, Container-Optimized OS or a hypervisor.

Round 2 added sources outside the books for the gaps round 1 left: the Google Cloud Blog post on gLinux (2022), the Google Cloud pages "What are containers?" and "Containers at Google", the GKE Sandbox and Container-Optimized OS documentation, the Linux kernel documentation on Control Group v2 and Livepatch, the gVisor documentation, and Marc Merlin's USENIX LISA '13 paper (a Google engineer).

## Not found yet

These items still have no opened source that `scripts/add_claim.py` can check. Do not put them in the report as facts.

- Which OS Google's SREs use on their own workstations. Google runs many OS platforms, one of them Linux (04-44), so 04-25 stays an assumption.
- The name and version of Google's current server distribution, and whether the internal distribution in Building Secure and Reliable Systems (04-02) is the Debian Testing based one in the 2013 paper (04-28).
- Which kernel features Borg uses for containers. The Borg paper (EuroSys 2015) is a PDF, which the quote checker cannot read, and the ACM Queue article "Borg, Omega, and Kubernetes" refuses the checker's requests (HTTP 403).
- Why Google chose Linux for its production servers. For desktops, 04-49 gives the reason for Debian only.
- Whether the "ksplice" in Building Secure and Reliable Systems is the Oracle Ksplice product.
- Which Google services run in gVisor, for example App Engine. Google lists an application kernel such as gVisor among its isolation techniques (04-57) but does not name the services.
- Linux knowledge asked for in current Google SRE job ads. Topics 01 and 02 may cover this.
