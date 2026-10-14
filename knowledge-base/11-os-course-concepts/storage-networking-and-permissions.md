---
doc_type: topic-note
topic: 11-os-course-concepts
title: "File I/O, networking and permissions in SRE troubleshooting"
updated: 2026-10-10
claims:
  - id: 11-08
    claim: "A successful Linux write() return does not guarantee that the data has been committed to disk."
    type: fact
    status: human-verified
    source:
      title: "Linux man-pages: write(2)"
      url: https://man7.org/linux/man-pages/man2/write.2.html
      kind: official-doc
      accessed: 2026-10-10
      archive: null
    quote: "A successful return from write () does not make any guarantee that data has been committed to disk."
    os_concepts: ["file systems", "I/O", "system calls", "durability"]
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
  - id: 11-09
    claim: "Linux fsync() blocks until the storage device reports that the transfer has completed."
    type: fact
    status: human-verified
    source:
      title: "Linux man-pages: fsync(2)"
      url: https://man7.org/linux/man-pages/man2/fsync.2.html
      kind: official-doc
      accessed: 2026-10-10
      archive: null
    quote: "The call blocks until the device reports that the transfer has completed."
    os_concepts: ["file systems", "I/O", "blocking", "durability"]
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
  - id: 11-10
    claim: "Linux puts file data into the page cache when reading it to avoid expensive disk access on subsequent reads."
    type: fact
    status: human-verified
    source:
      title: "Linux Kernel documentation: Concepts overview, Page cache"
      url: https://docs.kernel.org/admin-guide/mm/concepts.html
      kind: official-doc
      accessed: 2026-10-10
      archive: null
    quote: "Whenever a file is read, the data is put into the page cache to avoid expensive disk access on the subsequent reads."
    os_concepts: ["page cache", "memory management", "file systems", "I/O"]
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
  - id: 11-11
    claim: "Linux's BSD-compatible sockets provide an interface between user processes and kernel network protocol stacks."
    type: fact
    status: human-verified
    source:
      title: "Linux man-pages: socket(7)"
      url: https://man7.org/linux/man-pages/man7/socket.7.html
      kind: official-doc
      accessed: 2026-10-10
      archive: null
    quote: "The BSD compatible sockets are the uniform interface between the user process and the network protocol stacks in the kernel."
    os_concepts: ["networking", "sockets", "user space and kernel space"]
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
  - id: 11-12
    claim: "TCP delivers data in order and retransmits lost packets."
    type: fact
    status: human-verified
    source:
      title: "Linux man-pages: tcp(7)"
      url: https://man7.org/linux/man-pages/man7/tcp.7.html
      kind: official-doc
      accessed: 2026-10-10
      archive: null
    quote: "TCP guarantees that the data arrives in order and retransmits lost packets."
    os_concepts: ["networking", "TCP", "retransmission"]
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
  - id: 11-13
    claim: "During Linux path resolution, lack of search permission on the current lookup directory returns EACCES (Permission denied)."
    type: fact
    status: human-verified
    source:
      title: "Linux man-pages: path_resolution(7)"
      url: https://man7.org/linux/man-pages/man7/path_resolution.7.html
      kind: official-doc
      accessed: 2026-10-10
      archive: null
    quote: "If the process does not have search permission on the current lookup directory, an EACCES error is returned (\"Permission denied\")."
    os_concepts: ["file systems", "permissions", "security", "path resolution"]
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
  - id: 11-14
    claim: "Recommended SRE course connection: for a service that writes persistent data, distinguish successful write() calls, cache activity and completed synchronization when investigating latency or crash recovery. Relate the workload's durability requirements to filesystem and I/O concepts; do not assume that a successful write alone proves durable storage."
    type: assumption
    status: unverified
    os_concepts: ["file systems", "I/O", "page cache", "durability"]
    pr: null
  - id: 11-15
    claim: "Recommended SRE course connection: investigate a failed or slow service connection through its process socket and TCP behavior, and investigate file-access failures through directory search permissions. Use these as testable hypotheses rather than assigning every timeout to the network or broadening permissions without diagnosing the failure."
    type: assumption
    status: unverified
    os_concepts: ["networking", "sockets", "TCP", "permissions", "security"]
    pr: null
---

## Summary

Linux distinguishes a successful write from data committed to disk, while fsync waits for the device to report completion and file reads use the page cache (11-08 to 11-10). Sockets connect user processes to kernel network stacks, TCP retransmits lost packets, and directory search permissions affect path resolution (11-11 to 11-13). The proposed SRE applications relate these facts to storage durability, connection failures and access errors, and are recorded as assumptions (11-14, 11-15).

## Key points

- A successful write does not establish disk persistence; fsync blocks until the device reports completion. (11-08, 11-09)
- File reads populate the page cache to avoid expensive disk access on later reads. (11-10)
- Sockets form the user-process interface to kernel networking; TCP delivers data in order and retransmits lost packets. (11-11, 11-12)
- Missing directory search permission can produce EACCES during path resolution. (11-13)
- Recommended connection: investigate write completion, cache behavior and synchronization in storage-latency or recovery exercises. (11-14)
- Recommended connection: use socket, TCP and directory-permission observations as hypotheses when investigating connection or file-access failures. (11-15)

## Proposed connection to SRE work

| OS concept | Published mechanism | Recommended analysis exercise | Claim IDs |
|---|---|---|---|
| File systems, I/O and durability | write success and fsync completion describe different guarantees. | Relate persistent-data requirements to observed writes and synchronization. | 11-08, 11-09, 11-14 |
| Memory and storage interaction | File reads use the page cache. | Include cache behavior in storage-latency hypotheses. | 11-10, 11-14 |
| Networking | Processes use sockets; TCP retransmits lost packets. | Examine socket and TCP observations for a slow or failed connection. | 11-11, 11-12, 11-15 |
| Security and permissions | Directory search permission is checked during path resolution. | Diagnose file-access failure before changing permissions. | 11-13, 11-15 |

The exercises are recommendations recorded as assumptions. Each factual mechanism has one cited primary source; the write, fsync and page-cache references describe complementary parts of the storage path rather than proving a particular application's durability design.
