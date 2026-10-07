---
doc_type: topic-index
topic: 07-dev-and-runtime-tools
title: Development and runtime tools
assignment_section: "4.4"
report_sections: [9]
owner: "@nacs-970"
issue: 12
updated: 2026-10-06
---

# Development and runtime tools

Assignment 4.4: development tools and programming and runtime environments.

## Scope

- Editors, IDEs and compilers used by SREs
- Programming and runtime environments (for example Python, Go, shell)
- Debugging and profiling tools

## Notes in this directory

The owner organizes notes (`topic-note` files) here. List them below as they are added.

- [languages-and-build-tools.md](languages-and-build-tools.md): languages, shell, Python and the Blaze/Bazel build tool (07-01 to 07-07)
- [ide-and-compiler-feedback.md](ide-and-compiler-feedback.md): IDE and editor plug-ins, compiler checks, type-checking extensions (07-08 to 07-15, 07-29)
- [debugging-and-profiling.md](debugging-and-profiling.md): profilers, Valgrind, sanitizers, Go race detector, logs (07-16 to 07-28)

## Sources covered so far

Round 1 uses only the three books on https://sre.google/books/. Chapters cited by claims: SRE book ch.2, 6, 7, 8, 12, 17; Workbook ch.7, 15; Building Secure and Reliable Systems ch.12, 13, 15. For the gap search below, 104 pages were fetched as plain text and searched for tool names: 45 SRE book pages (all 34 chapters, the part pages and the appendices), all 24 Workbook pages, and the 35 pages in the Building Secure and Reliable Systems table of contents.

## Not found yet

These items from the scope are missing from the three books. They need other published sources, such as Google SRE job ads, or must be marked `assumption`.

- No editor is named as used by SREs. Emacs and VS Code do not appear in any fetched chapter. Vim appears in one passage of BSRS ch.5, as an attacker example (bypassing command-history logging), not as an SRE tool.
- IDEs appear by name only in claim 07-29 (Visual Studio, Eclipse, IntelliJ), as hosts for code-complexity tools. No book says which IDE SREs use.
- No command-line debugger or tracer is named as an SRE tool. `strace`, `tcpdump`, `perf` and `pprof` do not appear. GDB appears twice in BSRS, in ch.12 as a comparison for how hard a checker finding is to understand and in ch.15 to say that "debugger" there means a person.
- Rust does not appear in any fetched chapter.
- No source states which languages Google SRE job ads require. That needs the Google careers pages.
- The SRE book page footer says copyright 2017. Claims about Google describe what the book says, not current practice.
