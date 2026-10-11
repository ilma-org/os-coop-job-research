---
doc_type: topic-note
topic: 11-os-course-concepts
title: "Processes, threads, scheduling and virtual memory for SRE"
updated: 2026-10-11
claims:
  - id: 11-01
    claim: "The Linux scheduler selects which runnable thread executes on the CPU next."
    type: fact
    status: human-verified
    source:
      title: "Linux man-pages: sched(7)"
      url: https://man7.org/linux/man-pages/man7/sched.7.html
      kind: official-doc
      accessed: 2026-10-10
      archive: null
    quote: "The scheduler is the kernel component that decides which runnable thread will be executed by the CPU next."
    os_concepts: ["processes", "threads", "CPU scheduling"]
    pr: null
    ai_check:
      platform: Codex
      model: "gpt-6.1-sol"
      prompt_log: prompts/2026-10-10-TonCS05-11-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-11-reviewer-recheck-2.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-11
      result: pass
      opened_source: true
  - id: 11-02
    claim: "POSIX threads in one process share global memory, including data and heap segments, while each thread has its own stack."
    type: fact
    status: human-verified
    source:
      title: "Linux man-pages: pthreads(7)"
      url: https://man7.org/linux/man-pages/man7/pthreads.7.html
      kind: official-doc
      accessed: 2026-10-10
      archive: null
    quote: "These threads share the same global memory (data and heap segments), but each thread has its own stack (automatic variables)."
    os_concepts: ["processes", "threads", "memory management"]
    pr: null
    ai_check:
      platform: Codex
      model: "gpt-6.1-sol"
      prompt_log: prompts/2026-10-10-TonCS05-11-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-11-reviewer-recheck-2.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-11
      result: pass
      opened_source: true
  - id: 11-03
    claim: "On Linux, SIGKILL and SIGSTOP cannot be caught, blocked or ignored."
    type: fact
    status: human-verified
    source:
      title: "Linux man-pages: signal(7)"
      url: https://man7.org/linux/man-pages/man7/signal.7.html
      kind: official-doc
      accessed: 2026-10-10
      archive: null
    quote: "The signals SIGKILL and SIGSTOP cannot be caught, blocked, or ignored."
    os_concepts: ["process lifecycle", "signals"]
    pr: null
    ai_check:
      platform: Codex
      model: "gpt-6.1-sol"
      prompt_log: prompts/2026-10-10-TonCS05-11-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-11-reviewer-recheck-2.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-11
      result: pass
      opened_source: true
  - id: 11-04
    claim: "The mmap() system call creates a mapping in the calling process's virtual address space."
    type: fact
    status: human-verified
    source:
      title: "Linux man-pages: mmap(2)"
      url: https://man7.org/linux/man-pages/man2/mmap.2.html
      kind: official-doc
      accessed: 2026-10-10
      archive: null
    quote: "mmap () creates a new mapping in the virtual address space of the calling process."
    os_concepts: ["virtual memory", "address spaces", "system calls"]
    pr: null
    ai_check:
      platform: Codex
      model: "gpt-6.1-sol"
      prompt_log: prompts/2026-10-10-TonCS05-11-author-check-2.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-11-nacs-970-11-reviewer-recheck-2.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-11
      result: pass
      opened_source: true
  - id: 11-05
    claim: "The SRE book's troubleshooting guidance notes that diagnosis may require analyzing system logs across one or several processes."
    type: fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Chapter 12: Effective Troubleshooting"
      url: https://sre.google/sre-book/effective-troubleshooting/
      kind: official-doc
      accessed: 2026-10-10
      archive: null
    quote: "You may need to analyze system logs across one or many processes."
    os_concepts: ["processes", "observability", "troubleshooting"]
    pr: null
    ai_check:
      platform: Codex
      model: "gpt-6.1-sol"
      prompt_log: prompts/2026-10-10-TonCS05-11-author-check.md
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
  - id: 11-06
    claim: "Recommended SRE course connection: for a slow multithreaded service, examine runnable threads and CPU scheduling alongside latency measurements; for a restart, examine process logs and signals before assigning a cause. This is a proposed analysis exercise, not evidence of a particular company's workflow."
    type: assumption
    status: unverified
    os_concepts: ["processes", "threads", "CPU scheduling", "signals"]
    pr: null
  - id: 11-07
    claim: "Recommended SRE course connection: compare a service's virtual mappings with its resident memory measurements, and relate shared heap data and per-thread stacks to memory demand. Treat these observations as diagnostic evidence rather than assuming that a large virtual address space proves a memory leak."
    type: assumption
    status: unverified
    os_concepts: ["virtual memory", "address spaces", "threads", "memory management"]
    pr: null
  - id: 11-24
    claim: "Page tables translate virtual addresses used by the CPU into physical addresses on the memory bus."
    type: fact
    status: human-verified
    source:
      title: "Linux Kernel documentation: Page Tables"
      url: https://docs.kernel.org/mm/page_tables.html
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "Page tables map virtual addresses as seen by the CPU into physical addresses as seen on the external memory bus."
    os_concepts: ["virtual memory", "paging", "page tables", "address translation"]
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
  - id: 11-25
    claim: "Demand paging brings data into physical memory only as required by the current execution context."
    type: fact
    status: human-verified
    source:
      title: "Zephyr Project documentation: Demand Paging"
      url: https://docs.zephyrproject.org/latest/kernel/memory_management/demand_paging.html
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "Demand paging provides a mechanism where data is only brought into physical memory as required by current execution context."
    os_concepts: ["virtual memory", "demand paging"]
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
  - id: 11-26
    claim: "On Linux, getrusage() reports major page faults as faults whose servicing required I/O activity."
    type: fact
    status: human-verified
    source:
      title: "Linux man-pages: getrusage(2), published by Debian"
      url: https://manpages.debian.org/testing/manpages-dev/getrusage.2.en.html
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "The number of page faults serviced that required I/O activity."
    os_concepts: ["virtual memory", "page faults", "I/O"]
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
  - id: 11-27
    claim: "When allocation triggers direct reclaim at the minimum free-page watermark, Linux stalls the allocation until enough pages are reclaimed to satisfy it."
    type: fact
    status: human-verified
    source:
      title: "Linux Kernel documentation: Concepts overview, Reclaim"
      url: https://docs.kernel.org/admin-guide/mm/concepts.html
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "In this case allocation is stalled until enough memory pages are reclaimed to satisfy the request."
    os_concepts: ["memory management", "memory pressure", "page reclaim"]
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
  - id: 11-28
    claim: "Linux scheduler-statistics counters accumulate rather than representing only the latest observation interval."
    type: fact
    status: ai-checked
    source:
      title: "Linux Kernel documentation: Scheduler Statistics"
      url: https://docs.kernel.org/scheduler/sched-stats.html
      kind: official-doc
      accessed: 2026-10-11
      archive: null
    quote: "These fields are counters, and only increment."
    os_concepts: ["CPU scheduling", "monitoring"]
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
  - id: 11-29
    claim: "Recommended course connection: use the lecture model of address translation and demand paging to interpret virtual mappings, resident memory and changes in major-fault counts; consider reclaim-related allocation stalls when testing a memory-pressure hypothesis. This is a proposed SRE analysis exercise, not proof that every page fault indicates exhaustion or failure."
    type: assumption
    status: unverified
    os_concepts: ["virtual memory", "demand paging", "page faults", "memory pressure"]
    pr: null
  - id: 11-30
    claim: "Recommended course connection: distinguish ready-queue waiting from waiting for an event, and use the lecture discussion of context switches and scheduling criteria to frame a slow-service investigation. Compare CPU execution, waiting observations and request latency over the same interval; use changes in cumulative counters, and do not equate CPU execution time with end-to-end response time."
    type: assumption
    status: unverified
    os_concepts: ["process states", "ready queue", "CPU scheduling", "context switches", "response time"]
    pr: null
---

## Summary

Linux scheduling selects runnable threads, POSIX threads share global memory while retaining separate stacks, and signal handling has explicit limits (11-01 to 11-03). Memory mapping operates in a process's virtual address space, and the SRE troubleshooting guidance discusses examining logs across processes (11-04, 11-05). The proposed SRE applications connect these mechanisms to investigating slow services, restarts and memory demand; these applications are recommendations recorded as assumptions (11-06, 11-07). Page-table translation, demand paging, major faults requiring I/O and direct-reclaim stalls deepen the memory connection (11-24 to 11-27). Cumulative scheduler counters and two further proposed exercises connect observation intervals with course concepts (11-28 to 11-30).

## Key points

- CPU scheduling concerns which runnable thread executes next; threads share data and heap segments but have individual stacks. (11-01, 11-02)
- SIGKILL and SIGSTOP cannot be caught, blocked or ignored; virtual-memory mappings belong to the calling process's virtual address space. (11-03, 11-04)
- Troubleshooting guidance explicitly allows for analyzing logs from multiple processes. (11-05)
- Recommended connection: use scheduling, thread and signal concepts to form hypotheses about service latency and restarts. (11-06)
- Recommended connection: compare virtual mappings with resident memory observations when investigating memory demand. (11-07)
- Page tables translate virtual to physical addresses; demand paging brings data into physical memory as needed. (11-24, 11-25)
- Major faults require I/O; direct reclaim can stall an allocation. (11-26, 11-27)
- Scheduler counters accumulate; proposed exercises compare changes and interpret observations through the course models. (11-28 to 11-30)

## Proposed connection to SRE work

| OS concept | Published mechanism | Recommended analysis exercise | Claim IDs |
|---|---|---|---|
| Processes, threads and scheduling | The scheduler selects a runnable thread; threads share global memory and have separate stacks. | Relate observed CPU activity and runnable threads to service latency. | 11-01, 11-02, 11-06 |
| Process lifecycle and signals | SIGKILL and SIGSTOP cannot be intercepted. | Examine signals and process logs when explaining a restart. | 11-03, 11-05, 11-06 |
| Virtual memory | mmap creates mappings within a process's virtual address space. | Compare mappings with resident-memory measurements before forming a memory-leak hypothesis. | 11-04, 11-07 |

The exercises in the final column are assumptions, not verified workplace requirements. Each factual mechanism has one cited primary source. The SRE book provides the troubleshooting context; the Linux manuals provide the operating-system mechanisms.

## Additional course connections

| Lecture concepts | Proposed SRE investigation | Claim IDs |
|---|---|---|
| Address translation, demand paging and page faults | Compare virtual mappings, resident memory, fault-count changes and allocation stalls before assigning a memory-pressure cause. | 11-24 to 11-27, 11-29 |
| Ready/wait states, context switches and scheduling criteria | Compare CPU execution, waiting and request latency over one interval; use changes in cumulative counters. | 11-01, 11-28, 11-30 |

These investigations are assumptions. Zephyr supplies the general demand-paging definition, rather than evidence of a Linux or Google deployment; Linux references supply the translation, fault, reclaim and counter mechanisms.
