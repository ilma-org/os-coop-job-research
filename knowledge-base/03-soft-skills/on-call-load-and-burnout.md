---
doc_type: topic-note
topic: 03-soft-skills
title: "On-call load, stress and burnout"
updated: 2026-10-12
claims:
  - id: 03-17
    claim: "Google SRE's lessons-learned article says that to keep your cool during a high-risk, high-stress situation, it is important to practice recovery mechanisms and mitigations beforehand."
    type: org-fact
    status: ai-checked
    source:
      title: "Google SRE lessons - key principles of site reliability engineering"
      url: https://sre.google/resources/practices-and-processes/twenty-years-of-sre-lessons-learned/
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260917003110/https://sre.google/resources/practices-and-processes/twenty-years-of-sre-lessons-learned/
    quote: "To keep your cool during a high-risk and high-stress situation, it's important to practice recovery mechanisms and mitigations beforehand and verify that:"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check-2.md
      result: supported
  - id: 03-18
    claim: "On Google's SRE Prodcast, Steve McGhee recalls a method that teams or individuals could opt in to: first a text, then something else, and if they did not respond 90 seconds later, Telebot would wake them up."
    type: org-fact
    status: ai-checked
    source:
      title: "Google SRE Prodcast transcript: Special Episode: You Missed a Page from Telebot"
      url: https://sre.google/prodcast/transcripts/sre-prodcast-03-14/
      kind: other
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260413021633/https://sre.google/prodcast/transcripts/sre-prodcast-03-14/
    quote: "And there was a method that teams could opt in to using it, or individuals could opt in to using it, saying like, first send me a text, then send me a thing. And then 90 seconds later, if I don't respond, then sic the Telebot on me and wake me up."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check-2.md
      result: supported
  - id: 03-19
    claim: "A Google SRE article on heroism defines heroism as when there is a systemic problem or gap in a system and an individual decides to fill that gap."
    type: fact
    status: ai-checked
    source:
      title: "Why heroism is bad, and what we can do to stop it"
      url: https://sre.google/resources/practices-and-processes/no-heroes/
      kind: official-doc
      accessed: 2026-10-07
      archive: null
    quote: "When there's a systemic problem or gap in a system, and an individual decides to fill that gap."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check.md
      result: supported
  - id: 03-20
    claim: "A Google SRE article on heroism says heroism should not be planned for or relied on in the long term; if you commit to an SLO, you should be able to meet it without any heroes."
    type: fact
    status: ai-checked
    source:
      title: "Why heroism is bad, and what we can do to stop it"
      url: https://sre.google/resources/practices-and-processes/no-heroes/
      kind: official-doc
      accessed: 2026-10-07
      archive: null
    quote: "But heroism shouldn't be something you plan for or rely on in the long term. If you're committing to an SLO, you should be able to meet the SLO without any heroes."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check.md
      result: supported
  - id: 03-21
    claim: "A Google SRE article on heroism says on-call, when done right, does not require constant heroism."
    type: fact
    status: ai-checked
    source:
      title: "Why heroism is bad, and what we can do to stop it"
      url: https://sre.google/resources/practices-and-processes/no-heroes/
      kind: official-doc
      accessed: 2026-10-07
      archive: null
    quote: "On-call, when done right, does not require constant heroism."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check.md
      result: supported
  - id: 03-22
    claim: "On Google's SRE Prodcast, Vrai Stacey recalls a team with a three-minute SLO: after being paged, they were expected to be in front of a computer fixing the problem within three minutes."
    type: org-fact
    status: ai-checked
    source:
      title: "Google SRE Prodcast transcript: Incident Response with Sarah Butt and Vrai Stacey"
      url: https://sre.google/prodcast/transcripts/sre-prodcast-03-06/
      kind: other
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260510204843/https://sre.google/prodcast/transcripts/sre-prodcast-03-06/
    quote: "And we had a three-minute SLO. So we were expected from having been paged to be in front of a computer fixing a problem within three minutes."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check-2.md
      result: supported
  - id: 03-23
    claim: "The Google SRE report Anatomy of an Incident says lack of accountability, poor communications, missing hierarchy and freelancing/heroes can lengthen resolution times, add stress for on-callers and responders, and impact customers."
    type: fact
    status: ai-checked
    source:
      title: "Anatomy of an Incident (Google SRE report)"
      url: https://sre.google/static/pdf/Anatomy_Of_An_Incident.pdf
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260910212000/https://sre.google/static/pdf/Anatomy_Of_An_Incident.pdf
    quote: "lack of accountability, poor communications, missing hierarchy, and freelancing/heroes can result in longer resolution times, add additional stress for the on-callers and responders, and impact your customers."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check-2.md
      result: supported
  - id: 03-24
    claim: "The Google SRE report Anatomy of an Incident says it can be challenging and expensive to find SREs with the right mix of skills to respond to incidents, so you don't want to burn them out by designating them solely to incident response."
    type: fact
    status: ai-checked
    source:
      title: "Anatomy of an Incident (Google SRE report)"
      url: https://sre.google/static/pdf/Anatomy_Of_An_Incident.pdf
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260910212000/https://sre.google/static/pdf/Anatomy_Of_An_Incident.pdf
    quote: "It can be challenging and expensive to find site reliability engineers (SREs) with the right mix of skills to respond to incidents, so you don’t want to burn them out by designating them solely to incident response."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check-2.md
      result: supported
  - id: 03-25
    claim: "The report Training Site Reliability Engineers says too much on-call can burn SREs out, while too little can cause them to lose familiarity with the service and troubleshooting processes."
    type: org-fact
    status: ai-checked
    source:
      title: "Training Site Reliability Engineers (O'Reilly report by Google authors, 2019/2020)"
      url: https://sre.google/static/pdf/TrainingSiteReliabilityEngineers.pdf
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20251123125903/https://sre.google/static/pdf/TrainingSiteReliabilityEngineers.pdf
    quote: "Too much on-call, however, can burn them out. Too little, on the other hand, can cause them to lose familiarity with the service and troubleshooting processes."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check-2.md
      result: supported
---

# On-call load, stress and burnout

## Summary

A Google SRE article on heroism says heroism should not be planned for or relied on in the long term, and that on-call done right does not require constant heroism (03-19, 03-20, 03-21). The report Anatomy of an Incident says lack of accountability, poor communications, missing hierarchy and freelancing/heroes can add stress for on-callers (03-23) and that SREs should not be burned out by designating them solely to incident response (03-24), and the report Training Site Reliability Engineers says too much on-call can burn SREs out while too little can cause them to lose familiarity with the service (03-25). Google SRE's lessons say it is important to practice recovery mechanisms and mitigations beforehand to keep your cool under stress (03-17). Prodcast speakers recall paging expectations: an opt-in method where Telebot woke people who did not respond within 90 seconds (03-18) and a team with a three-minute SLO to be at a computer fixing the problem (03-22). Each claim rests on one source; no second source was compared, and this note has no claim yet on on-call shift length or page volume.

## Key points

- A Google SRE article on heroism defines heroism as an individual filling a systemic gap in a system (03-19).
- The same article says heroism should not be planned for or relied on in the long term, and that an SLO you commit to should be met without heroes (03-20).
- The same article says on-call, when done right, does not require constant heroism (03-21).
- The Google SRE report Anatomy of an Incident says lack of accountability, poor communications, missing hierarchy and freelancing can add stress for on-callers and responders (03-23).
- The same report says SREs with the right skills are challenging and expensive to find, so you don't want to burn them out by designating them solely to incident response (03-24).
- The report Training Site Reliability Engineers says too much on-call can burn SREs out, while too little can cause them to lose familiarity with the service (03-25).
- Google SRE's lessons-learned article says it is important to practice recovery mechanisms and mitigations beforehand to keep your cool in a high-stress situation (03-17).
- On Google's SRE Prodcast, Steve McGhee recalls an opt-in method: a text, then something else, and if there was no response 90 seconds later, Telebot would wake them up (03-18).
- On Google's SRE Prodcast, Vrai Stacey recalls a team with a three-minute SLO for being in front of a computer fixing the problem after a page (03-22).

Claims are listed newest source first. Each claim's `status` in the front matter says how far it has been checked.

Source years in this note: 2025, 2024, 2022, 2019. A year is the publication or last-update year of the source, or the book edition year when the page gives none (SRE book 2016, Workbook 2018, Building Secure and Reliable Systems 2020).

## Claims at a glance

- `03-17` (org-fact): Google SRE's lessons-learned article says that to keep your cool during a high-risk, high-stress situation, it is important to practice recovery mechanisms and mitigations beforehand.
- `03-18` (org-fact): On Google's SRE Prodcast, Steve McGhee recalls a method that teams or individuals could opt in to: first a text, then something else, and if they did not respond 90 seconds later, Telebot would wake them up.
- `03-19` (fact): A Google SRE article on heroism defines heroism as when there is a systemic problem or gap in a system and an individual decides to fill that gap.
- `03-20` (fact): A Google SRE article on heroism says heroism should not be planned for or relied on in the long term; if you commit to an SLO, you should be able to meet it without any heroes.
- `03-21` (fact): A Google SRE article on heroism says on-call, when done right, does not require constant heroism.
- `03-22` (org-fact): On Google's SRE Prodcast, Vrai Stacey recalls a team with a three-minute SLO: after being paged, they were expected to be in front of a computer fixing the problem within three minutes.
- `03-23` (fact): The Google SRE report Anatomy of an Incident says lack of accountability, poor communications, missing hierarchy and freelancing/heroes can lengthen resolution times, add stress for on-callers and responders, and impact customers.
- `03-24` (fact): The Google SRE report Anatomy of an Incident says it can be challenging and expensive to find SREs with the right mix of skills to respond to incidents, so you don't want to burn them out by designating them solely to incident response.
- `03-25` (org-fact): The report Training Site Reliability Engineers says too much on-call can burn SREs out, while too little can cause them to lose familiarity with the service and troubleshooting processes.

## Notes

- `org-fact` claims carry a Wayback Machine snapshot in `source.archive`. The exact quote was found in that snapshot on the claim's `source.accessed` date.
- Podcast speakers are named in the claim. A speaker who is not a Google employee is not evidence about Google, so those claims are `fact`, not `org-fact`.
