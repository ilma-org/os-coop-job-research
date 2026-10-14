---
doc_type: topic-note
topic: 03-soft-skills
title: "Teamwork, incident collaboration, design documents and approvals"
updated: 2026-10-14
claims:
  - id: 03-26
    claim: "On Google's SRE Prodcast, Adam Kramer says that if they are paged for a completely specious thing, the attitude is 'please don't page us for that next time', but people should feel free to page them with new problems rather than let a problem sit and simmer."
    type: fact
    status: ai-checked
    source:
      title: "Google SRE Prodcast transcript: Adam Kramer"
      url: https://sre.google/prodcast/transcripts/sre-prodcast-06-09/
      kind: other
      accessed: 2026-10-07
      archive: null
    quote: "The attitude is if we're paged for a completely specious thing, the attitude is please don't page us for that next time, but feel free to page us with new problems, because don't let the problem sit and simmer if you don't know what to do."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check.md
      result: supported
  - id: 03-27
    claim: "On Google's SRE Prodcast, Vrai Stacey says their team always adopted the view that if the on-caller needs your help, you drop what you are doing and help the on-caller."
    type: org-fact
    status: ai-checked
    source:
      title: "Google SRE Prodcast transcript: Incident Response with Sarah Butt and Vrai Stacey"
      url: https://sre.google/prodcast/transcripts/sre-prodcast-03-06/
      kind: other
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260510204843/https://sre.google/prodcast/transcripts/sre-prodcast-03-06/
    quote: "And we always adopted a view that if the on-caller needs your help, you drop what you're doing and help the on-caller."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check.md
      result: supported
  - id: 03-28
    claim: "In a section headed \"Example: Google Design Document\", Building Secure and Reliable Systems says Google uses a design document template to guide new feature design and to collect feedback from stakeholders before starting an engineering project."
    type: org-fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, Chapter 4"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch04.html
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260606131700/https://google.github.io/building-secure-and-reliable-systems/raw/ch04.html
    quote: "Google uses a design document template to guide new feature design and to collect feedback from stakeholders before starting an engineering project."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-nine14282-soft-skills-author-check-3.md
      result: supported
  - id: 03-29
    claim: "Google's Incident Management Guide says blameless postmortems are one of the core tenets of SRE culture, and that it is important to remember everyone involved in an incident had good intentions."
    type: fact
    status: ai-checked
    source:
      title: "Google SRE: Incident Management Guide (PDF)"
      url: https://sre.google/static/pdf/IncidentManagementGuide.pdf
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260702124541/https://sre.google/static/pdf/IncidentManagementGuide.pdf
    quote: "One of the core tenets of SRE’s culture is that postmortems should be blameless. It’s important to remember that everyone involved in the incident had good intentions."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check.md
      result: supported
  - id: 03-30
    claim: "Google's Incident Management Guide says blaming individuals for unintended consequences during the response does not aid learning, so the focus is instead on improving systems, procedures and training to make them more resilient."
    type: fact
    status: ai-checked
    source:
      title: "Google SRE: Incident Management Guide (PDF)"
      url: https://sre.google/static/pdf/IncidentManagementGuide.pdf
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260702124541/https://sre.google/static/pdf/IncidentManagementGuide.pdf
    quote: "Blaming individuals for unintended consequences during the response, does not aid the learning process so instead, we focus on how we can improve our systems, procedures, and training to make them more resilient."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check.md
      result: supported
  - id: 03-31
    claim: "One of the lessons in Lessons Learned from Two Decades of Site Reliability Engineering says teams expected to use Google Hangouts and Google Meet to manage an incident, and that relying on these Google services when 350M users were logged out of their devices and services was, in retrospect, kind of a bad call."
    type: org-fact
    status: ai-checked
    source:
      title: "Lessons Learned from Two Decades of Site Reliability Engineering (Google SRE 20th anniversary PDF)"
      url: https://sre.google/static/pdf/LessonsLearnedFromTwoDecades.pdf
      kind: official-doc
      accessed: 2026-10-12
      archive: https://web.archive.org/web/20260908065110/https://sre.google/static/pdf/LessonsLearnedFromTwoDecades.pdf
    quote: "Teams were expecting to be able to use Google Hangouts and Google Meet to manage the incident. But when 350M users were logged out of their devices and services... relying on these Google services was, in retrospect, kind of a bad call."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check-2.md
      result: supported
  - id: 03-33
    claim: "Building Secure and Reliable Systems says social pressure around approvals may also lead to bad decisions."
    type: fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, Chapter 5"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch05.html
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260616012631/https://google.github.io/building-secure-and-reliable-systems/raw/ch05.html
    quote: "Social pressure around approvals may also lead to bad decisions."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-nine14282-soft-skills-author-check-3.md
      result: supported
  - id: 03-34
    claim: "Building Secure and Reliable Systems advises making sure the technology and social dynamics allow someone to say no before building a multi-party authorization system; otherwise the system is of little value."
    type: fact
    status: ai-checked
    source:
      title: "Building Secure and Reliable Systems, Chapter 5"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch05.html
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260616012631/https://google.github.io/building-secure-and-reliable-systems/raw/ch05.html
    quote: "Before building a multi-party authorization system, make sure the technology and social dynamics allow someone to say no. Otherwise, the system is of little value."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check.md
      result: supported
---

# Teamwork, incident collaboration, design documents and approvals

## Summary

On Google's SRE Prodcast, Adam Kramer says people should feel free to page them with new problems (03-26), and Vrai Stacey says their team always adopted the view that you drop what you are doing to help an on-caller who needs it (03-27). Google's Incident Management Guide calls blameless postmortems one of the core tenets of SRE culture (03-29) and says blaming individuals does not aid learning (03-30). Building Secure and Reliable Systems gives Google's design document template, which collects stakeholder feedback, as an example (03-28), and says social pressure around approvals may lead to bad decisions (03-33) and that a multi-party authorization system is of little value unless the technology and social dynamics allow someone to say no (03-34). One of the lessons in Lessons Learned from Two Decades of Site Reliability Engineering says relying on Google Hangouts and Google Meet during an incident that logged out 350M users was, in retrospect, kind of a bad call (03-31). Each claim rests on one source; no second source was compared, and this note has no claim yet on presentation skills, time management or English and other language skills.

## Key points

- On Google's SRE Prodcast, Adam Kramer says that, apart from specious pages, people should feel free to page them with new problems rather than let a problem sit and simmer (03-26).
- On Google's SRE Prodcast, Vrai Stacey says their team always adopted the view that you drop what you are doing to help an on-caller who needs it (03-27).
- Google's Incident Management Guide says blameless postmortems are one of the core tenets of SRE culture (03-29).
- The same guide says blaming individuals does not aid learning, so the focus is on improving systems, procedures and training (03-30).
- In a section headed "Example: Google Design Document", Building Secure and Reliable Systems says Google uses a design document template to collect feedback from stakeholders before an engineering project starts (03-28).
- The same book says social pressure around approvals may lead to bad decisions (03-33), and that a multi-party authorization system is of little value unless someone can say no (03-34).
- One of the lessons in Lessons Learned from Two Decades of Site Reliability Engineering says relying on Google Hangouts and Google Meet when 350M users were logged out was, in retrospect, kind of a bad call (03-31).

Claims are listed newest source first. Each claim's `status` in the front matter says how far it has been checked.

Source years in this note: 2026, 2024, 2020. A year is the publication or last-update year of the source, or the book edition year when the page gives none (SRE book 2016, Workbook 2018, Building Secure and Reliable Systems 2020).

## Claims at a glance

- `03-26` (fact): On Google's SRE Prodcast, Adam Kramer says that if they are paged for a completely specious thing, the attitude is 'please don't page us for that next time', but people should feel free to page them with new problems rather than let a problem sit and simmer.
- `03-27` (org-fact): On Google's SRE Prodcast, Vrai Stacey says their team always adopted the view that if the on-caller needs your help, you drop what you are doing and help the on-caller.
- `03-28` (org-fact): In a section headed "Example: Google Design Document", Building Secure and Reliable Systems says Google uses a design document template to guide new feature design and to collect feedback from stakeholders before starting an engineering project.
- `03-29` (fact): Google's Incident Management Guide says blameless postmortems are one of the core tenets of SRE culture, and that it is important to remember everyone involved in an incident had good intentions.
- `03-30` (fact): Google's Incident Management Guide says blaming individuals for unintended consequences during the response does not aid learning, so the focus is instead on improving systems, procedures and training to make them more resilient.
- `03-31` (org-fact): One of the lessons in Lessons Learned from Two Decades of Site Reliability Engineering says teams expected to use Google Hangouts and Google Meet to manage an incident, and that relying on these Google services when 350M users were logged out of their devices and services was, in retrospect, kind of a bad call.
- `03-33` (fact): Building Secure and Reliable Systems says social pressure around approvals may also lead to bad decisions.
- `03-34` (fact): Building Secure and Reliable Systems advises making sure the technology and social dynamics allow someone to say no before building a multi-party authorization system; otherwise the system is of little value.

## Notes

- `org-fact` claims carry a Wayback Machine snapshot in `source.archive`. The exact quote was found in that snapshot on the claim's `source.accessed` date.
- Podcast speakers are named in the claim. A speaker who is not a Google employee is not evidence about Google, so those claims are `fact`, not `org-fact`.
- `03-26` is a `fact`: the Wayback Machine has no snapshot of the transcript, so it cannot be an `org-fact`, and the claim says nothing about Google beyond where it was said.
- `03-26` and `03-27` are each one speaker's account of their own team, not a statement of general SRE practice.
