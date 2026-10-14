---
doc_type: topic-note
topic: 03-soft-skills
title: "Blameless culture, psychological safety and working with product teams"
updated: 2026-10-14
claims:
  - id: 03-09
    claim: "A Google SRE article on product-focused reliability says that to obtain product and user information, SRE needs to work with product managers and UX researchers, who define the product and its features using frameworks such as Jobs to be Done and Google's Critical User Journeys."
    type: org-fact
    status: ai-checked
    source:
      title: "Google SRE - Product SRE, improving reliability of services"
      url: https://sre.google/resources/practices-and-processes/product-focused-reliability-for-sre/
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260828005315/https://sre.google/resources/practices-and-processes/product-focused-reliability-for-sre/
    quote: "To obtain product and user information, SRE needs to work with product managers and UX researchers, who define the product and features based on frameworks like Jobs to be Done [1,5] and Google's Critical User Journeys (CUJs) [2], which identify the end user's goals and desired outcomes."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check-2.md
      result: supported
  - id: 03-10
    claim: "On Google's SRE Prodcast, Steph Hippo says that when she first got to SRE at Google, all incident command was still done on IRC, and as a junior SRE she could just follow along with outages her team was not responsible for."
    type: org-fact
    status: ai-checked
    source:
      title: "Google SRE Prodcast transcript: The One With Stephanie Hippo and Observability"
      url: https://sre.google/prodcast/transcripts/sre-prodcast-05-01/
      kind: other
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260306061602/https://sre.google/prodcast/transcripts/sre-prodcast-05-01/
    quote: "One of the things that I really loved about my time at Google, when I first got to SRE, all the incident command was still done on IRC. And I could, as a junior SRE, just follow along, outages that my team wasn't responsible for."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check-2.md
      result: supported
  - id: 03-12
    claim: "The Google SRE report Anatomy of an Incident quotes a definition of psychological safety as a belief that one will not be punished or humiliated for speaking up with ideas, questions, concerns or mistakes."
    type: fact
    status: ai-checked
    source:
      title: "Anatomy of an Incident (Google SRE report)"
      url: https://sre.google/static/pdf/Anatomy_Of_An_Incident.pdf
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260910212000/https://sre.google/static/pdf/Anatomy_Of_An_Incident.pdf
    quote: "Psychological safety is a belief that one will not be punished or humiliated for speaking up with ideas, questions, concerns, or mistakes."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check-2.md
      result: supported
  - id: 03-13
    claim: "The report Enterprise Roadmap to SRE says the team must feel psychologically safe when put in the high-pressure position of control over major systems, and must be able to say no to peers and leaders without fear of retribution."
    type: fact
    status: ai-checked
    source:
      title: "Enterprise Roadmap to SRE (Google Cloud/SRE report)"
      url: https://sre.google/static/pdf/enterprise-roadmap-to-sre.pdf
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260305034321/https://sre.google/static/pdf/enterprise-roadmap-to-sre.pdf
    quote: "The team must feel psychologically safe when they’re put in the high-pressure position of control over major systems. They must be able to say “no” to their peers and leaders without fear of retribution."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check-2.md
      result: supported
  - id: 03-14
    claim: "The report Enterprise Roadmap to SRE says citing 'human error' when humans make mistakes has been shown to be somewhat meaningless and not an effective way to improve a system, and that SRE instead promotes blamelessness."
    type: fact
    status: ai-checked
    source:
      title: "Enterprise Roadmap to SRE (Google Cloud/SRE report)"
      url: https://sre.google/static/pdf/enterprise-roadmap-to-sre.pdf
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260305034321/https://sre.google/static/pdf/enterprise-roadmap-to-sre.pdf
    quote: "Often, when mistakes are made by humans, it can be tempting to cite “human error,” but this has been shown to be somewhat meaningless and not an effective way to improve a system. Instead, SRE promotes blamelessness."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check-2.md
      result: supported
  - id: 03-15
    claim: "In its section on remediating and learning from incidents, Google's Incident Management Guide calls open and blameless postmortem writing the most effective tool Google has found for that purpose."
    type: org-fact
    status: ai-checked
    source:
      title: "Google SRE: Incident Management Guide (PDF)"
      url: https://sre.google/static/pdf/IncidentManagementGuide.pdf
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260702124541/https://sre.google/static/pdf/IncidentManagementGuide.pdf
    quote: "The most effective tool we have found for achieving that is through open and blameless postmortem writing."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check-2.md
      result: supported
  - id: 03-16
    claim: "Google's Incident Management Guide says regular practice such as Wheel of Misfortune exercises can keep knowledge up to date and gives less experienced on-callers an opportunity to develop their skills in a safe environment."
    type: fact
    status: ai-checked
    source:
      title: "Google SRE: Incident Management Guide (PDF)"
      url: https://sre.google/static/pdf/IncidentManagementGuide.pdf
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260702124541/https://sre.google/static/pdf/IncidentManagementGuide.pdf
    quote: "Regular practice through activities such as \"Wheel of Misfortune'' exercises can keep this knowledge up to date, as well as providing an opportunity for less experienced oncallers to develop their skills in a safe environment."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-soft-skills-author-check-2.md
      result: supported
---

# Blameless culture, psychological safety and working with product teams

## Summary

In its section on learning from incidents, Google's Incident Management Guide calls open and blameless postmortem writing the most effective tool Google has found for that purpose (03-15), and the report Enterprise Roadmap to SRE says SRE promotes blamelessness instead of citing human error (03-14). On psychological safety, the report Anatomy of an Incident quotes a definition (03-12), and Enterprise Roadmap to SRE says a team in control of major systems must feel psychologically safe and be able to say no to peers and leaders without fear of retribution (03-13). A Prodcast speaker recalls following along with outages on IRC as a junior SRE (03-10), and the guide says Wheel of Misfortune practice can keep knowledge up to date (03-16). A Google SRE article on working with product managers and UX researchers (03-09) is also kept here. Each claim rests on one source; no second source was compared, and this note has no claim yet from a source outside Google.

## Key points

- In its section on learning from incidents, Google's Incident Management Guide calls open and blameless postmortem writing the most effective tool Google has found for that purpose (03-15).
- The report Enterprise Roadmap to SRE says citing human error is somewhat meaningless and not an effective way to improve a system, and that SRE promotes blamelessness instead (03-14).
- The Google SRE report Anatomy of an Incident quotes a definition of psychological safety as a belief that one will not be punished or humiliated for speaking up (03-12).
- The report Enterprise Roadmap to SRE says a team in control of major systems must feel psychologically safe and be able to say no without fear of retribution (03-13).
- Google's Incident Management Guide says Wheel of Misfortune exercises can keep knowledge up to date and let less experienced on-callers develop their skills in a safe environment (03-16).
- On Google's SRE Prodcast, Steph Hippo says that as a junior SRE she could follow along on IRC with outages her team was not responsible for (03-10).
- A Google SRE article on product-focused reliability says SRE needs to work with product managers and UX researchers to obtain product and user information (03-09).

Claims are listed newest source first. Each claim's `status` in the front matter says how far it has been checked.

Source years in this note: 2025, 2024, 2022, 2020. A year is the publication or last-update year of the source, or the book edition year when the page gives none (SRE book 2016, Workbook 2018, Building Secure and Reliable Systems 2020).

## Claims at a glance

- `03-09` (org-fact): A Google SRE article on product-focused reliability says that to obtain product and user information, SRE needs to work with product managers and UX researchers, who define the product and its features using frameworks such as Jobs to be Done and Google's Critical User Journeys.
- `03-10` (org-fact): On Google's SRE Prodcast, Steph Hippo says that when she first got to SRE at Google, all incident command was still done on IRC, and as a junior SRE she could just follow along with outages her team was not responsible for.
- `03-12` (fact): The Google SRE report Anatomy of an Incident quotes a definition of psychological safety as a belief that one will not be punished or humiliated for speaking up with ideas, questions, concerns or mistakes.
- `03-13` (fact): The report Enterprise Roadmap to SRE says the team must feel psychologically safe when put in the high-pressure position of control over major systems, and must be able to say no to peers and leaders without fear of retribution.
- `03-14` (fact): The report Enterprise Roadmap to SRE says citing 'human error' when humans make mistakes has been shown to be somewhat meaningless and not an effective way to improve a system, and that SRE instead promotes blamelessness.
- `03-15` (org-fact): In its section on remediating and learning from incidents, Google's Incident Management Guide calls open and blameless postmortem writing the most effective tool Google has found for that purpose.
- `03-16` (fact): Google's Incident Management Guide says regular practice such as Wheel of Misfortune exercises can keep knowledge up to date and gives less experienced on-callers an opportunity to develop their skills in a safe environment.

## Notes

- `org-fact` claims carry a Wayback Machine snapshot in `source.archive`. The exact quote was found in that snapshot on the claim's `source.accessed` date.
- Podcast speakers are named in the claim. A speaker who is not a Google employee is not evidence about Google, so those claims are `fact`, not `org-fact`.
- `03-15` names the guide's section on learning from incidents. The stored quote says only "for achieving that"; the section heading and the sentences before the quote say what "that" is.
- `03-10` is one speaker's account of their own early time in Google SRE, not a statement of general SRE practice.
