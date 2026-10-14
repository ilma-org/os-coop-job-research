---
doc_type: topic-note
topic: 03-soft-skills
title: "Incident command, communication and persuasion"
updated: 2026-10-14
claims:
  - id: 03-01
    claim: "Google SRE's lessons-learned article advises ensuring you have non-dependent backup communication channels and that you have tested them."
    type: org-fact
    status: ai-checked
    source:
      title: "Google SRE lessons - key principles of site reliability engineering"
      url: https://sre.google/resources/practices-and-processes/twenty-years-of-sre-lessons-learned/
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260917003110/https://sre.google/resources/practices-and-processes/twenty-years-of-sre-lessons-learned/
    quote: "Ensure that you have non-dependent backup communication channels, and that you have tested them."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-03-reviewer-recheck.md
      result: supported
  - id: 03-02
    claim: "On Google's SRE Prodcast, Peter Pellerzi says that when something goes wrong, all of their data centers have very specific protocols, for example immediately opening a common video chat that anybody who wants to can join."
    type: org-fact
    status: ai-checked
    source:
      title: "Google SRE Prodcast transcript: The One With Data Centers and Peter Pellerzi"
      url: https://sre.google/prodcast/transcripts/sre-prodcast-04-02/
      kind: other
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260413020631/https://sre.google/prodcast/transcripts/sre-prodcast-04-02/
    quote: "When something goes wrong on this proverbial Saturday at 2 o'clock or 1:00 AM in the morning, we have very specific protocols at all of our data centers. So, for example, we open up a video chat immediately, a common video chat between anybody who wants to get on."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-03-reviewer-recheck.md
      result: supported
  - id: 03-03
    claim: "Google's Incident Management Guide says incident roles do not follow reporting chains and are instead based on knowledge and incident context."
    type: org-fact
    status: ai-checked
    source:
      title: "Google SRE: Incident Management Guide (PDF)"
      url: https://sre.google/static/pdf/IncidentManagementGuide.pdf
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260702124541/https://sre.google/static/pdf/IncidentManagementGuide.pdf
    quote: "Incident roles do not follow reporting chains and instead are based on knowledge and incident context."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-03-reviewer-recheck.md
      result: supported
  - id: 03-04
    claim: "Lessons Learned from Two Decades of Site Reliability Engineering says Google SRE learned the hard way that during an incident it should monitor and evaluate the severity of the situation and choose a mitigation path whose riskiness is appropriate for that severity."
    type: org-fact
    status: ai-checked
    source:
      title: "Lessons Learned from Two Decades of Site Reliability Engineering (Google SRE 20th anniversary PDF)"
      url: https://sre.google/static/pdf/LessonsLearnedFromTwoDecades.pdf
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260908065110/https://sre.google/static/pdf/LessonsLearnedFromTwoDecades.pdf
    quote: "We learned the hard way that during an incident, we should monitor and evaluate the severity of the situation and choose a mitigation path whose riskiness is appropriate for that severity."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-03-reviewer-recheck.md
      result: supported
  - id: 03-05
    claim: "Building Secure and Reliable Systems says Google has codified crisis response into a program called Incident Management at Google (IMAG), a standard, consistent way to handle all types of incidents."
    type: org-fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, Chapter 1"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch01.html
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260616012620/https://google.github.io/building-secure-and-reliable-systems/raw/ch01.html
    quote: "Google has codified crisis response into a program called Incident Management at Google (IMAG), which establishes a standard, consistent way to handle all types of incidents, from system outages to natural disasters, and organize an effective response."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-03-reviewer-recheck.md
      result: supported
  - id: 03-06
    claim: "The report Training Site Reliability Engineers says blameless postmortems help find root causes, and that when blaming is involved people tend to sweep things under the rug, which hinders finding the underlying causes and indirectly allows the same incident to happen again."
    type: org-fact
    status: ai-checked
    source:
      title: "Training Site Reliability Engineers (O'Reilly report by Google authors, 2019/2020)"
      url: https://sre.google/static/pdf/TrainingSiteReliabilityEngineers.pdf
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20251123125903/https://sre.google/static/pdf/TrainingSiteReliabilityEngineers.pdf
    quote: "Blameless postmortems help you to find root causes. If blaming is involved, people tend to sweep things under the rug, which hinders finding out the underlying causes, thereby indirectly allowing the same incident to happen again."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-03-reviewer-recheck.md
      result: supported
  - id: 03-07
    claim: "The report Training Site Reliability Engineers says that through interviews with different teams its authors found communication, agreement and trust are paramount to healthy SRE-developer relationships, and that the best functioning teams are those where it is barely known who is an SRE and who is a developer."
    type: org-fact
    status: ai-checked
    source:
      title: "Training Site Reliability Engineers (O'Reilly report by Google authors, 2019/2020)"
      url: https://sre.google/static/pdf/TrainingSiteReliabilityEngineers.pdf
      kind: official-doc
      accessed: 2026-10-12
      archive: https://web.archive.org/web/20251123125903/https://sre.google/static/pdf/TrainingSiteReliabilityEngineers.pdf
    quote: "Through interviews with different teams, we’ve found that communication, agreement, and trust are paramount to healthy SRE–developer relationships, and the best functioning teams are those in which it’s barely known who is an SRE and who is a developer"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check-2.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-03-reviewer-recheck.md
      result: supported
  - id: 03-08
    claim: "The Site Reliability Workbook gives, as an example, a first-person account by John Looney: an objective cost/benefit analysis showing the problem was costing Google $1,000 per hour convinced the devs to fix the problem with Looney's patch."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook: Eliminating Toil"
      url: https://sre.google/workbook/eliminating-toil/
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260909103330/https://sre.google/workbook/eliminating-toil/
    quote: "My objective cost/benefit analysis showing that the problem was costing Google $1,000 per hour convinced the devs to fix the problem with my patch."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-nine14282-soft-skills-author-check-3.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-03-reviewer-recheck.md
      result: supported
---

# Incident command, communication and persuasion

## Summary

Building Secure and Reliable Systems says Google has codified crisis response into Incident Management at Google (IMAG) (03-05), and Google's Incident Management Guide says incident roles are based on knowledge and incident context rather than reporting chains (03-03). Google SRE's lessons advise keeping tested, non-dependent backup communication channels (03-01) and choosing a mitigation whose riskiness fits the severity (03-04), and a Prodcast speaker says their data centers open a common video chat when something goes wrong (03-02). The report Training Site Reliability Engineers says that when blaming is involved, people tend to sweep things under the rug (03-06) and that communication, agreement and trust are paramount to healthy SRE-developer relationships (03-07). The Site Reliability Workbook gives, as an example, a first-person account of how a cost/benefit analysis convinced developers to fix a problem (03-08). Each claim rests on one source; no second source was compared, and this note has no claim yet on handoffs between on-call shifts.

## Key points

- Building Secure and Reliable Systems says Google has codified crisis response into Incident Management at Google (IMAG), a standard way to handle all types of incidents (03-05).
- Google's Incident Management Guide says incident roles are based on knowledge and incident context, not reporting chains (03-03).
- Google SRE's lessons-learned article advises having non-dependent backup communication channels and testing them (03-01).
- Lessons Learned from Two Decades of Site Reliability Engineering says Google SRE learned to evaluate an incident's severity and choose a mitigation path whose riskiness fits it (03-04).
- On Google's SRE Prodcast, Peter Pellerzi says their data centers have specific protocols when something goes wrong, for example a common video chat anybody can join (03-02).
- The report Training Site Reliability Engineers says that when blaming is involved people tend to sweep things under the rug, which hinders finding the underlying causes (03-06).
- The same report says communication, agreement and trust are paramount to healthy SRE-developer relationships (03-07).
- The Site Reliability Workbook gives, as an example, a first-person account in which a cost/benefit analysis showing a problem cost Google $1,000 per hour convinced the devs to fix it (03-08).

Claims are listed newest source first. Each claim's `status` in the front matter says how far it has been checked.

Source years in this note: 2025, 2020, 2019, 2018. A year is the publication or last-update year of the source, or the book edition year when the page gives none (SRE book 2016, Workbook 2018, Building Secure and Reliable Systems 2020).

## Claims at a glance

- `03-01` (org-fact): Google SRE's lessons-learned article advises ensuring you have non-dependent backup communication channels and that you have tested them.
- `03-02` (org-fact): On Google's SRE Prodcast, Peter Pellerzi says that when something goes wrong, all of their data centers have very specific protocols, for example immediately opening a common video chat that anybody who wants to can join.
- `03-03` (org-fact): Google's Incident Management Guide says incident roles do not follow reporting chains and are instead based on knowledge and incident context.
- `03-04` (org-fact): Lessons Learned from Two Decades of Site Reliability Engineering says Google SRE learned the hard way that during an incident it should monitor and evaluate the severity of the situation and choose a mitigation path whose riskiness is appropriate for that severity.
- `03-05` (org-fact): Building Secure and Reliable Systems says Google has codified crisis response into a program called Incident Management at Google (IMAG), a standard, consistent way to handle all types of incidents.
- `03-06` (org-fact): The report Training Site Reliability Engineers says blameless postmortems help find root causes, and that when blaming is involved people tend to sweep things under the rug, which hinders finding the underlying causes and indirectly allows the same incident to happen again.
- `03-07` (org-fact): The report Training Site Reliability Engineers says that through interviews with different teams its authors found communication, agreement and trust are paramount to healthy SRE-developer relationships, and that the best functioning teams are those where it is barely known who is an SRE and who is a developer.
- `03-08` (org-fact): The Site Reliability Workbook gives, as an example, a first-person account by John Looney: an objective cost/benefit analysis showing the problem was costing Google $1,000 per hour convinced the devs to fix the problem with Looney's patch.

## Notes

- `org-fact` claims carry a Wayback Machine snapshot in `source.archive`. The exact quote was found in that snapshot on the claim's `source.accessed` date.
- Podcast speakers are named in the claim. A speaker who is not a Google employee is not evidence about Google, so those claims are `fact`, not `org-fact`.
- `03-02` is one speaker's account of the data centers they work with, not a statement of general SRE practice.
- `03-08` comes from a sidebar headed "Example: Manual Response to Toil". It is one engineer's account, not general guidance.
