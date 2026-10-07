---
doc_type: topic-note
topic: 07-dev-and-runtime-tools
title: "Debugging and profiling tools"
updated: 2026-10-06
claims:
  - id: 07-16
    claim: "The SRE book says every Google server runs an HTTP server that exposes diagnostics and statistics for a given task, to support dashboards, monitoring and debugging."
    type: org-fact
    status: unverified
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-06
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "To facilitate dashboards, monitoring, and debugging, every server has an HTTP server that provides diagnostics and statistics for a given task."
    os_concepts: []
    pr: null
  - id: 07-17
    claim: "Text logs suit real-time debugging, while structured binary logs let teams build tools for deeper retrospective analysis."
    type: fact
    status: unverified
    source:
      title: "Site Reliability Engineering, ch.12 Effective Troubleshooting"
      url: https://sre.google/sre-book/effective-troubleshooting/
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "Text logs are very helpful for reactive debugging in real time, while storing logs in a structured binary format can make it possible to build tools to conduct retrospective analysis with much more information."
    os_concepts: []
    pr: null
  - id: 07-18
    claim: "In the SRE book's troubleshooting chapter, profiling the server is the step that shows where CPU time is being used."
    type: fact
    status: unverified
    source:
      title: "Site Reliability Engineering, ch.12 Effective Troubleshooting"
      url: https://sre.google/sre-book/effective-troubleshooting/
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "Where in the server is the CPU time being used? Profiling the server shows it’s sorting entries in logs checkpointed to disk."
    os_concepts: ["processes and CPU scheduling"]
    pr: null
  - id: 07-19
    claim: "The authors of Building Secure and Reliable Systems describe a slow web server where a profiler showed that logging all input to disk and calling sync caused the delay, not the backends."
    type: fact
    status: unverified
    source:
      title: "Building Secure and Reliable Systems, ch.15 Investigating Systems"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch15.html
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "We assumed the problem lay in the backends, but a profiler showed that the practice of logging every possible scrap of input to disk and then calling sync was causing vast amounts of delay."
    os_concepts: ["file systems and I/O"]
    pr: null
  - id: 07-20
    claim: "The SRE book counts interfaces such as the Java Virtual Machine Profiling Interface as a source of white-box monitoring metrics."
    type: fact
    status: unverified
    source:
      title: "Site Reliability Engineering, ch.6 Monitoring Distributed Systems"
      url: https://sre.google/sre-book/monitoring-distributed-systems/
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "Monitoring based on metrics exposed by the internals of the system, including logs, interfaces like the Java Virtual Machine Profiling Interface, or an HTTP handler that emits internal statistics."
    os_concepts: []
    pr: null
  - id: 07-21
    claim: "Valgrind runs a user's binary in a virtual machine, so developers can catch memory errors without recompiling their code."
    type: fact
    status: unverified
    source:
      title: "Building Secure and Reliable Systems, ch.12 Writing Code"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch12.html
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "Valgrind has the benefit of providing a virtual machine that interprets a user’s binary, so users don’t need to recompile their code to use it."
    os_concepts: ["memory management"]
    pr: null
  - id: 07-22
    claim: "AddressSanitizer (ASan) detects memory errors such as buffer overflows, use after free and incorrect initialization order."
    type: fact
    status: unverified
    source:
      title: "Building Secure and Reliable Systems, ch.12 Writing Code"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch12.html
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "AddressSanitizer (ASan) detects memory errors (buffer overflows, use after free, incorrect initialization order)."
    os_concepts: ["memory management"]
    pr: null
  - id: 07-23
    claim: "ThreadSanitizer (TSan) detects data races and deadlocks."
    type: fact
    status: unverified
    source:
      title: "Building Secure and Reliable Systems, ch.12 Writing Code"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch12.html
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "ThreadSanitizer (TSan) detects data races and deadlocks."
    os_concepts: ["threads and concurrency", "deadlock"]
    pr: null
  - id: 07-24
    claim: "The Google Sanitizers suite runs up to 10 times faster than Valgrind."
    type: fact
    status: unverified
    source:
      title: "Building Secure and Reliable Systems, ch.12 Writing Code"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch12.html
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "The main advantage of the Google Sanitizers suite is speed: it’s up to 10 times faster than Valgrind."
    os_concepts: []
    pr: null
  - id: 07-25
    claim: "Go can still suffer data races even though it disallows the memory corruption typical of C++, and the Go Race Detector finds them."
    type: fact
    status: unverified
    source:
      title: "Building Secure and Reliable Systems, ch.12 Writing Code"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch12.html
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "While Go is designed to disallow memory corruption issues typical to C++, it may still suffer from data race conditions. Go Race Detector can detect these conditions."
    os_concepts: ["threads and concurrency"]
    pr: null
  - id: 07-26
    claim: "The Google Sanitizers began in the LLVM compiler infrastructure and are now also supported by GCC and other compilers."
    type: fact
    status: unverified
    source:
      title: "Building Secure and Reliable Systems, ch.13 Testing Code"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch13.html
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "They were initially developed as part of the LLVM compiler infrastructure to capture common programming mistakes, and are now supported by GCC and other compilers, as well."
    os_concepts: []
    pr: null
  - id: 07-27
    claim: "Sanitizer-instrumented binaries can be orders of magnitude slower, so many projects run sanitizer pipelines in CI/CD less often, for example nightly."
    type: fact
    status: unverified
    source:
      title: "Building Secure and Reliable Systems, ch.13 Testing Code"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch13.html
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "This feedback comes at a performance cost: the compiler-instrumented binaries can be orders of magnitude slower than the native binaries. As a result, many projects are adding sanitizer-enhanced pipelines to their existing CI/CD systems, but running those pipelines less frequently—for example, nightly."
    os_concepts: []
    pr: null
  - id: 07-28
    claim: "Performance profilers and code coverage report generators are the best-known types of dynamic program analysis."
    type: fact
    status: unverified
    source:
      title: "Building Secure and Reliable Systems, ch.13 Testing Code"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch13.html
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "Performance profilers (which are used to find performance issues in programs) and code coverage report generators are the best-known types of dynamic analysis."
    os_concepts: []
    pr: null
---

# Debugging and profiling tools

Debugging and profiling tools named in the books. Claim 07-17 is general advice on logs from the SRE book's troubleshooting chapter. Claim 07-18 comes from that chapter's worked example. The sanitizer and Valgrind claims describe C/C++ tools in a Google-authored book; they do not show that Google SRE uses them day to day.
