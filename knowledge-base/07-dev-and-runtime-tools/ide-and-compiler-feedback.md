---
doc_type: topic-note
topic: 07-dev-and-runtime-tools
title: "IDEs, editors and compiler feedback"
updated: 2026-10-06
claims:
  - id: 07-08
    claim: "Compiler plug-ins such as Error Prone for Java and Tsetse for TypeScript can prohibit risky code patterns at compile time."
    type: fact
    status: unverified
    source:
      title: "Building Secure and Reliable Systems, ch.12 Writing Code"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch12.html
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "Plug-ins for popular compilers, such as Error Prone for Java and Tsetse for TypeScript, can prohibit risky code patterns."
    os_concepts: []
    pr: null
  - id: 07-09
    claim: "The authors of Building Secure and Reliable Systems report that compiler errors give faster feedback than opt-in tools such as linters or checks at code review time."
    type: fact
    status: unverified
    source:
      title: "Building Secure and Reliable Systems, ch.12 Writing Code"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch12.html
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "Our experience has shown that compiler errors provide immediate and actionable feedback. Tools running on an opt-in basis (like linters) or at code review time provide feedback much later."
    os_concepts: []
    pr: null
  - id: 07-10
    claim: "Building Secure and Reliable Systems names IDE plug-ins that underline problematic code as a fast feedback mechanism for developers."
    type: fact
    status: unverified
    source:
      title: "Building Secure and Reliable Systems, ch.12 Writing Code"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch12.html
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "It’s much easier to equip developers with compiler errors or faster feedback mechanisms like IDE plug-ins that underline problematic code."
    os_concepts: []
    pr: null
  - id: 07-11
    claim: "Building Secure and Reliable Systems recommends adding stricter type-checking extensions to languages that use dynamic or weak typing by default."
    type: fact
    status: unverified
    source:
      title: "Building Secure and Reliable Systems, ch.12 Writing Code"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch12.html
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "If you want to use languages that have dynamic type checking or weak typing by default, we recommend using extensions like the following to improve the reliability of your code."
    os_concepts: []
    pr: null
  - id: 07-12
    claim: "Building Secure and Reliable Systems lists Pytype as one of its recommended type-checking extensions, for Python."
    type: fact
    status: unverified
    source:
      title: "Building Secure and Reliable Systems, ch.12 Writing Code"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch12.html
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "Pytype for Python"
    os_concepts: []
    pr: null
  - id: 07-13
    claim: "Popular IDEs such as CLion provide first-class integration with the Google Sanitizers."
    type: fact
    status: unverified
    source:
      title: "Building Secure and Reliable Systems, ch.12 Writing Code"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch12.html
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "Popular IDEs like CLion also provide first-class integration with Google Sanitizers."
    os_concepts: []
    pr: null
  - id: 07-14
    claim: "The SRE Workbook lists linters, debuggers, formatters and IDE integration as tooling that supports configuration files."
    type: fact
    status: unverified
    source:
      title: "The Site Reliability Workbook, ch.15 Configuration Specifics"
      url: https://sre.google/workbook/configuration-specifics/
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "Support configuration health, engineer confidence, and productivity via tooling for managing the config files (linters, debuggers, formatters, IDE integration, etc.)."
    os_concepts: []
    pr: null
  - id: 07-15
    claim: "The SRE Workbook suggests investigating whether an editor plug-in can integrate style and lint tools for configuration files into your workflow."
    type: fact
    status: unverified
    source:
      title: "The Site Reliability Workbook, ch.15 Configuration Specifics"
      url: https://sre.google/workbook/configuration-specifics/
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "Consider how you will enforce style and lint your configurations, and investigate if there’s an editor plug-in that integrates these tools into your workflow."
    os_concepts: []
    pr: null
  - id: 07-29
    claim: "The SRE Workbook says code-complexity measurement tools exist for a number of IDEs, including Visual Studio, Eclipse and IntelliJ."
    type: fact
    status: unverified
    source:
      title: "The Site Reliability Workbook, ch.7 Simplicity"
      url: https://sre.google/workbook/simplicity/
      kind: official-doc
      accessed: 2026-10-06
      archive: null
    quote: "The software community is actually quite good at measuring code complexity, and there are measurement tools for a number of integrated development environments (including Visual Studio, Eclipse, and IntelliJ)."
    os_concepts: []
    pr: null
---

# IDEs, editors and compiler feedback

What the books say about IDE plug-ins, editor plug-ins and compiler checks. No book names an editor as an SRE tool. Vim appears in one passage of BSRS ch.5 as an attacker example, not as a tool. See `index.md` for the gaps.
