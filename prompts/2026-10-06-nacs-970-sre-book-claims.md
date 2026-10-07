---
doc_type: prompt-log
id: 2026-10-06-nacs-970-sre-book-claims
author: "@nacs-970"
date: 2026-10-06
platform: Claude Code
model: "Claude Sonnet 5.5 (claude-sonnet-5-5); advisor calls to Opus 5.5"
phase: exploration
role: research
significant: true
significant_reason: "Produced the 29 topic 07 claims from the Google SRE books that report section 9 relies on."
purpose: Research topic 07 claims from the Google SRE books for issue 12
pr: null
claims: [07-01, 07-02, 07-03, 07-04, 07-05, 07-06, 07-07, 07-08, 07-09, 07-10, 07-11, 07-12, 07-13, 07-14, 07-15, 07-16, 07-17, 07-18, 07-19, 07-20, 07-21, 07-22, 07-23, 07-24, 07-25, 07-26, 07-27, 07-28, 07-29]
redactions: 0
supporting_docs:
  - https://sre.google/books/
  - https://sre.google/sre-book/table-of-contents/
  - https://sre.google/workbook/table-of-contents/
  - https://sre.google/sre-book/automation-at-google/
  - https://sre.google/sre-book/effective-troubleshooting/
  - https://sre.google/sre-book/monitoring-distributed-systems/
  - https://sre.google/sre-book/production-environment/
  - https://sre.google/sre-book/release-engineering/
  - https://sre.google/sre-book/testing-reliability/
  - https://sre.google/workbook/configuration-specifics/
  - https://sre.google/workbook/simplicity/
  - https://google.github.io/building-secure-and-reliable-systems/raw/ch12.html
  - https://google.github.io/building-secure-and-reliable-systems/raw/ch13.html
  - https://google.github.io/building-secure-and-reliable-systems/raw/ch15.html
  - https://web.archive.org/web/20260910213452/https://sre.google/sre-book/automation-at-google/
  - https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
  - https://web.archive.org/web/20260912041941/https://sre.google/sre-book/release-engineering/
---

## Turn 1 — user
start research on 12, with https://sre.google/books/ as primarily source first

## Turn 1 — assistant
I've created the branch and saved all 16 chapters as plain text. Now I'll grep
them for mentions of languages, compilers, debuggers and profilers, and fetch
the BSRS book.

I've finished reading the sources. Next I'll check the Workbook and pull
Wayback archive links for the cited pages, then draft the claims, verifying
each quote against the saved page text.

Still waiting on the Wayback lookups. Meanwhile I'm collecting exact chapter
titles so the claim source titles are accurate.

Status: source search is complete across the SRE book, Workbook and BSRS
chapters. I found a useful debugging passage in BSRS ch.15. I'm reading it
now, then I'll write the notes.

Archive snapshots found. Each resolves with HTTP 200 and contains the quoted
sentences. Now I'm generating the three note files and updating index.md.

Now update index.md with the issue number, the note list and the gaps, then
run the lint.

Chapter titles for BSRS are correct. The Workbook chapter number was wrong in
my draft (ch.18 should be ch.15), so I'm fixing that and adding the Simplicity
IDE claim.

The fetch gap is closed — all BSRS TOC pages and SRE book part pages are
saved, with small files just being short part-divider pages, not failures. Now
rerunning the negative search across all 100+ files.

The old background Wayback job overwrote archive.json with failures. I'm
stopping it and rebuilding the file from the CDX records, then regenerating.

Research round 1 on issue #12 is written to disk on branch
07-dev-and-runtime-tools/sre-book-claims. It has 29 claims in three new notes,
all status: unverified, and python3 scripts/lint_front_matter.py passes with
0 errors. Nothing is staged or committed.

Note: languages-and-build-tools.md
Claims: 07-01 to 07-07
Content: Google's standard languages (C++, Java, Python, Go, JavaScript),
Blaze/Bazel, hermetic builds, and Python and shell in early automation
────────────────────────────────────────
Note: ide-and-compiler-feedback.md
Claims: 07-08 to 07-15, 07-29
Content: Compiler plug-ins, IDE and editor plug-ins, Pytype, IDEs named in the

Workbook
────────────────────────────────────────
Note: debugging-and-profiling.md
Claims: 07-16 to 07-28
Content: Profiling, Valgrind, the Google Sanitizers, the Go race detector,
logs

Of the 29 claims, 6 are org-fact (07-01, 03, 05, 06, 07, 16) and 23 are fact.
None is an assumption.

- Quotes: I took them from raw page HTML, not WebFetch summaries. A script
  confirmed each quote appears verbatim in the page text.
- Archive links: The 6 org-fact claims have Wayback snapshots found through
  the archive's CDX index. Each snapshot returns 200 and contains the quoted
  sentences.
- Gaps: index.md lists what the books don't cover, searched across 104 fetched
  pages.
  - No editor is named as an SRE tool. Vim appears once, as an attacker
    example.
  - strace, tcpdump, perf and pprof don't appear.
  - Google SRE job ads aren't covered, so the languages they require are still
    unknown.
- Date caveat: The SRE book page footer says copyright 2017. Those claims say
  what the book states, not current Google practice.

I also set issue: 12 in index.md and listed the notes there.

Next steps:
1. Author AI check: Nothing is fact-checked yet. Run it in a separate session
   with its own role: author-check prompt log, which would let claims reach
   ai-checked.
2. Prompt log: AGENTS.md requires one and none exists. This session produced
   the key claims, so it is probably significant: true, which puts it in the
   report appendix and counts toward the page cap. The session also contains
   the job, todo and milestone turns. Should I log the whole session or only
   the research turns? Either way I'll redact the home and scratchpad paths in
   the tool ledger.
3. Commits: I propose one commit per note file, one for index.md, and one for
   the prompt log, with .gitignore left out. Say yes and I'll commit.
4. Next sources: After the books, Google SRE job ads would cover the languages
   and tools gap.

## Tool-call ledger
- Read (1 file, path collapsed in export)
- Bash (1 command, collapsed in export)
- WebFetch https://sre.google/books/
- Read (1 file, path collapsed in export)
- WebFetch https://sre.google/books/
- Bash (1 command, collapsed in export)
- WebFetch https://sre.google/sre-book/table-of-contents/
- WebFetch https://sre.google/workbook/table-of-contents/
- advisor (Opus 5.5, no arguments)
- Bash (1 command, collapsed in export)
- Bash (5 commands, collapsed in export)
- Directory listing (1, path collapsed in export)
- Bash (5 commands, collapsed in export)
- Bash (6 commands, collapsed in export)
- Edit of a scratchpad file (1, +172 lines, path collapsed in export)
- Bash (5 commands, collapsed in export)
- Bash (1 command, collapsed in export)
- Write knowledge-base/07-dev-and-runtime-tools/index.md
- Bash (3 commands, collapsed in export)
- Bash (3 commands, collapsed in export)
- advisor (Opus 5.5, no arguments)
- Bash (3 commands, collapsed in export)
- Bash (5 commands, collapsed in export)
- Bash (2 commands, collapsed in export)
- Bash (1 command, collapsed in export)

The terminal export collapses shell commands, so their arguments are not listed. Ctrl+O in the live session shows them.
