---
doc_type: topic-note
topic: 07-dev-and-runtime-tools
title: "Languages, runtimes and build tools in Google's SRE books"
updated: 2026-10-06
claims:
  - id: 07-01
    claim: "The SRE book says Google's build tool Blaze builds binaries from what Google calls its standard languages: C++, Java, Python, Go and JavaScript."
    type: org-fact
    status: unverified
    source:
      title: "Site Reliability Engineering, ch.8 Release Engineering"
      url: https://sre.google/sre-book/release-engineering/
      kind: official-doc
      accessed: 2026-10-06
      archive: https://web.archive.org/web/20260912041941/https://sre.google/sre-book/release-engineering/
    quote: "It supports building binaries from a range of languages, including our standard languages of C++, Java, Python, Go, and JavaScript."
    os_concepts: []
    pr: null
  - id: 07-02
    claim: "The SRE book says its build tool Blaze has been open sourced as Bazel."
    type: fact
    status: unverified
    source:
      title: "Site Reliability Engineering, ch.8 Release Engineering"
      url: https://sre.google/sre-book/release-engineering/
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "Blaze has been open sourced as Bazel."
    os_concepts: []
    pr: null
  - id: 07-03
    claim: "The SRE book says Google's builds are hermetic: they depend on known versions of build tools such as compilers, not on software installed on the build machine."
    type: org-fact
    status: unverified
    source:
      title: "Site Reliability Engineering, ch.8 Release Engineering"
      url: https://sre.google/sre-book/release-engineering/
      kind: official-doc
      accessed: 2026-10-06
      archive: https://web.archive.org/web/20260912041941/https://sre.google/sre-book/release-engineering/
    quote: "Our builds are hermetic, meaning that they are insensitive to the libraries and other software installed on the build machine. Instead, builds depend on known versions of build tools, such as compilers, and dependencies, such as libraries."
    os_concepts: []
    pr: null
  - id: 07-04
    claim: "Bazel builds a dependency graph of a project and rebuilds only the part of the software that depends on a changed file."
    type: fact
    status: unverified
    source:
      title: "Site Reliability Engineering, ch.17 Testing for Reliability"
      url: https://sre.google/sre-book/testing-reliability/
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "Bazel creates dependency graphs for software projects. When a change is made to a file, Bazel only rebuilds the part of the software that depends on that file."
    os_concepts: []
    pr: null
  - id: 07-05
    claim: "Google's early cluster-configuration shell scripts were brittle and did not scale with the number of people or cluster permutations."
    type: org-fact
    status: unverified
    source:
      title: "Site Reliability Engineering, ch.7 The Evolution of Automation at Google"
      url: https://sre.google/sre-book/automation-at-google/
      kind: official-doc
      accessed: 2026-10-06
      archive: https://web.archive.org/web/20260910213452/https://sre.google/sre-book/automation-at-google/
    quote: "The creative—though brittle—shell scripts we used to configure clusters were neither scaling to the number of people who wanted to make changes nor to the sheer number of cluster permutations that needed to be built."
    os_concepts: []
    pr: null
  - id: 07-06
    claim: "Google SRE extended the Python unit test framework into Prodtest, which unit-tests real-world services."
    type: org-fact
    status: unverified
    source:
      title: "Site Reliability Engineering, ch.7 The Evolution of Automation at Google"
      url: https://sre.google/sre-book/automation-at-google/
      kind: official-doc
      accessed: 2026-10-06
      archive: https://web.archive.org/web/20260910213452/https://sre.google/sre-book/automation-at-google/
    quote: "We extended the Python unit test framework to allow for unit testing of real-world services."
    os_concepts: []
    pr: null
  - id: 07-07
    claim: "Google's early production automation consisted of simple Python scripts."
    type: org-fact
    status: unverified
    source:
      title: "Site Reliability Engineering, ch.7 The Evolution of Automation at Google"
      url: https://sre.google/sre-book/automation-at-google/
      kind: official-doc
      accessed: 2026-10-06
      archive: https://web.archive.org/web/20260910213452/https://sre.google/sre-book/automation-at-google/
    quote: "Initially automation consisted of simple Python scripts for operations such as the following:"
    os_concepts: []
    pr: null
---

# Languages, runtimes and build tools in Google's SRE books

Evidence on which languages and build tools Google's SRE books name. The SRE book text is dated (page footer: copyright 2017), so claims describe what the book says, not Google today. Shell and Python evidence comes from the book's history of Google's automation.
