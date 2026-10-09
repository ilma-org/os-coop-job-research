---
doc_type: topic-index
topic: 06-system-architecture-infrastructure
title: System architecture and infrastructure
assignment_section: "4.3"
report_sections: [8]
owner: "@csinside"
issue: 11
updated: 2026-10-08
---

# System architecture and infrastructure

Assignment Appendix E. Architecture and infrastructure an SRE encounters.

## Scope

- Client-server, web, application and database server tiers
- Cloud infrastructure, virtual machines, hypervisors
- Containers and container orchestration
- Distributed and clustered systems
- Backup and disaster recovery systems

## Notes in this directory

The owner organizes notes (`topic-note` files) here. List them below as they are added.

<!-- notes:start -->
- [request-path-and-load-balancing.md](request-path-and-load-balancing.md): Client-server request path, RPC and load balancing. 9 claims (06-01 to 06-08, 06-26): 9 unverified.
- [cluster-management-containers-vms.md](cluster-management-containers-vms.md): Cluster management, containers and virtual machines. 9 claims (06-09 to 06-15, 06-27 to 06-28): 9 unverified.
- [storage-consensus-and-recovery.md](storage-consensus-and-recovery.md): Distributed storage, consensus, backups and disaster recovery. 10 claims (06-16 to 06-25): 10 unverified.
<!-- notes:end -->

## Sources covered so far

Round 1 used only the three books on https://sre.google/books/. Chapters cited by claims: SRE book ch.2, 23, 26; Workbook ch.6, 9, 11; Building Secure and Reliable Systems ch.8, 16. The same 79-page plain-text search as topic 04 was used, with architecture terms (load balancing, Borg, Kubernetes, virtual machine, backup, replication, failure domain, NAS).

Round 2 added current official pages: the Cloud Load Balancing documentation for Application Load Balancers and a 2017 Google Cloud Blog post on Google's KVM hypervisor.

## Not found yet

These items still have no opened source. Do not put them in the report as facts.

- The current hypervisor setup. The KVM claims (06-27, 06-28) date from 2017.
- A current, archived source for Maglev. The Maglev claim (06-07) comes from the 2018 Workbook; the current Network Load Balancer page that names Maglev has no Wayback snapshot with that text yet.
- Web, application and database server software such as Apache, Nginx or MySQL. Topic 10 covers server and database software.
- IoT infrastructure, and edge computing beyond racks of proxy/cache machines in colos (05-11).
- GPU and TPU servers inside Google's own production; only Google Cloud offerings are covered (05-32, 05-33).
