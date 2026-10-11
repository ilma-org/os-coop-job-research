---
doc_type: topic-index
topic: 11-os-course-concepts
title: Operating Systems course concepts
assignment_section: "4.5"
report_sections: [10]
owner: "@TonCS05"
issue: 16
updated: 2026-10-11
---

# Operating Systems course concepts

Connect the SRE job to OS concepts from the course. Feeds the relationship visualization.

## Scope

- Chain in the form: Job -> OS -> hardware -> software/tools -> OS concepts, as in the assignment examples
- Processes, threads and scheduling
- Memory management and virtual memory
- File systems and I/O
- Virtualization, containers and resource isolation
- Networking, security and permissions
- Distributed-system failure detection and recovery

## Notes in this directory

The owner organizes notes (`topic-note` files) here. List them below as they are added.

<!-- notes:start -->
- [processes-and-memory.md](processes-and-memory.md): Processes, threads, scheduling and virtual memory for SRE. 14 claims (11-01 to 11-07, 11-24 to 11-30): 10 ai-checked, 4 unverified.
- [storage-networking-and-permissions.md](storage-networking-and-permissions.md): File I/O, networking and permissions in SRE troubleshooting. 8 claims (11-08 to 11-15): 6 ai-checked, 2 unverified.
- [containers-and-resource-isolation.md](containers-and-resource-isolation.md): Virtualization, containers and resource isolation for SRE. 8 claims (11-16 to 11-23): 6 ai-checked, 2 unverified.
- [distributed-failure-detection-and-recovery.md](distributed-failure-detection-and-recovery.md): Distributed failure detection and recovery for SRE. 3 claims (11-31 to 11-33): 2 ai-checked, 1 unverified.
<!-- notes:end -->

## Research coverage

The notes connect processes and scheduling, virtual memory, file I/O,
networking, permissions, virtualization, resource isolation and distributed recovery to
proposed SRE analysis exercises. Facts cite Linux man-pages, Linux Kernel, Zephyr,
Kubernetes, Docker, QEMU and the SRE book. The complete workload chain and
recommended applications are explicitly recorded as assumptions.

## Course alignment

Eight locally supplied slide PDFs were inspected on 2026-10-11. References use
PDF page order; the slide files are not stored in this repository.

| Lecture file | PDF pages | Connection |
|---|---|---|
| `ch2_operating-systemstructures.pdf` | 4–6, 13, 21–23, 54–56 | System calls, I/O, protection and troubleshooting; 11-03 to 11-05, 11-08 to 11-17. |
| `ch3_processes.pdf`; `ch4_cpuscheduling_forstudents.pdf` | Chapter 3: 8, 13–17, 50–55; chapter 4: 6–9, 29 | Processes, sockets and proposed scheduling investigation; 11-01, 11-11, 11-28, 11-30. |
| `ch7_memorymanagement_forstudent.pdf`; `ch8_virtualmemory.pdf` | Chapter 7: 8–9, 20–29; chapter 8: 5, 9, 13–21 | Address translation, demand paging and fault investigation; 11-24 to 11-27, 11-29. |
| `ch9_distributedsystems.pdf` | 17–21 | Failure detection and recovery examples; 11-31 to 11-33. |

Containers and resource limits extend the resource-allocation and protection
concepts; the supplied slides do not teach these tools in detail. This selection
connects relevant concepts without covering every lecture chapter.

## Not found yet

- The supplied slides have an AI inspection only; a human should confirm the
  course mapping before using it in the report.
- The complete proposed workload chain is not established as Google's actual
  infrastructure. No claim in these notes asserts that Google deploys this
  combination of tools or follows the recommended exercises.
- These notes do not cover synchronization algorithms, deadlock handling or
  specific page-replacement algorithms. Additional claims would be needed if
  the report uses those concepts.
- Human verification and the reviewer's separate recheck remain pending.
