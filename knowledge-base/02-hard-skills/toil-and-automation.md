---
doc_type: topic-note
topic: 02-hard-skills
title: Toil, automation and production changes
updated: '2026-10-07'
claims:
- id: 02-15
  claim: Google SRE says that had a global change been canaried with a progressive rollout strategy, the outage could have been curbed before it had global impact.
  type: org-fact
  status: unverified
  source:
    title: Google SRE lessons - key principles of site reliability engineering
    url: https://sre.google/resources/practices-and-processes/twenty-years-of-sre-lessons-learned/
    kind: official-doc
    accessed: '2026-10-07'
    archive: https://web.archive.org/web/20260917003110/https://sre.google/resources/practices-and-processes/twenty-years-of-sre-lessons-learned/
  quote: Had we canaried those global changes with a progressive rollout strategy, this outage could have been curbed before it had global impact.
  os_concepts: []
  pr: null
- id: 02-16
  claim: Google SRE says automating manual mitigations can reduce MTTR and that automated mitigation can come before root-causing.
  type: org-fact
  status: unverified
  source:
    title: Google SRE lessons - key principles of site reliability engineering
    url: https://sre.google/resources/practices-and-processes/twenty-years-of-sre-lessons-learned/
    kind: official-doc
    accessed: '2026-10-07'
    archive: https://web.archive.org/web/20260917003110/https://sre.google/resources/practices-and-processes/twenty-years-of-sre-lessons-learned/
  quote: Sometimes it is better to use an automated mitigation first and save the root-causing for after user impact has been avoided.
  os_concepts: []
  pr: null
- id: 02-17
  claim: The Enterprise Roadmap to SRE says that once toil overwhelms an SRE team, all other SRE activities grind to a halt.
  type: fact
  status: unverified
  source:
    title: Enterprise Roadmap to SRE (Google Cloud/SRE report)
    url: https://sre.google/static/pdf/enterprise-roadmap-to-sre.pdf
    kind: official-doc
    accessed: '2026-10-07'
    archive: https://web.archive.org/web/20260305034321/https://sre.google/static/pdf/enterprise-roadmap-to-sre.pdf
  quote: Once toil overwhelms your team, all the other SRE activities will grind to a halt.
  os_concepts: []
  pr: null
- id: 02-18
  claim: Google's Zero Touch Prod requires every production change to be made by automation, prevalidated by software, or triggered through an audited breakglass mechanism.
  type: org-fact
  status: unverified
  source:
    title: Building Secure and Reliable Systems, Chapter 3
    url: https://google.github.io/building-secure-and-reliable-systems/raw/ch03.html
    kind: official-doc
    accessed: '2026-10-07'
    archive: https://web.archive.org/web/20260224150156/https://google.github.io/building-secure-and-reliable-systems/raw/ch03.html
  quote: Zero Touch Prod is a project at Google that requires every change in production to be made by automation (instead of humans), prevalidated by software, or triggered through an audited breakglass mechanism
  os_concepts: []
  pr: null
- id: 02-19
  claim: Google estimates about 13% of all Google-evaluated outages could have been prevented or mitigated with Zero Touch Prod.
  type: org-fact
  status: unverified
  source:
    title: Building Secure and Reliable Systems, Chapter 3
    url: https://google.github.io/building-secure-and-reliable-systems/raw/ch03.html
    kind: official-doc
    accessed: '2026-10-07'
    archive: https://web.archive.org/web/20260224150156/https://google.github.io/building-secure-and-reliable-systems/raw/ch03.html
  quote: We estimate that ~13% of all Google-evaluated outages could have been prevented or mitigated with Zero Touch Prod.
  os_concepts: []
  pr: null
- id: 02-20
  claim: The SRE organization at Google is building on least privilege through automation, aiming for Zero Touch interfaces.
  type: org-fact
  status: unverified
  source:
    title: Building Secure and Reliable Systems, Chapter 5
    url: https://google.github.io/building-secure-and-reliable-systems/raw/ch05.html
    kind: official-doc
    accessed: '2026-10-07'
    archive: https://web.archive.org/web/20260616012631/https://google.github.io/building-secure-and-reliable-systems/raw/ch05.html
  quote: The SRE organization at Google is working to build upon the concept of least privilege through automation, with the goal of moving to what we call Zero Touch interfaces.
  os_concepts: []
  pr: null
- id: 02-21
  claim: Zero Touch interfaces aim to make Google safer and reduce outages by removing direct human access to production roles.
  type: org-fact
  status: unverified
  source:
    title: Building Secure and Reliable Systems, Chapter 5
    url: https://google.github.io/building-secure-and-reliable-systems/raw/ch05.html
    kind: official-doc
    accessed: '2026-10-07'
    archive: https://web.archive.org/web/20260616012631/https://google.github.io/building-secure-and-reliable-systems/raw/ch05.html
  quote: The specific goal of these interfaces—like Zero Touch Production (ZTP), described in Chapter 3, and Zero Touch Networking (ZTN)—is to make Google safer and reduce outages by removing direct human access to production roles.
  os_concepts: []
  pr: null
- id: 02-22
  claim: SRE as practiced at Google has a hard limit of 50% of a team member's time on toil.
  type: org-fact
  status: unverified
  source:
    title: 'The Site Reliability Workbook: How SRE Relates to DevOps'
    url: https://sre.google/workbook/how-sre-relates/
    kind: official-doc
    accessed: '2026-10-07'
    archive: https://web.archive.org/web/20260918074533/https://sre.google/workbook/how-sre-relates/
  quote: 'SRE as practiced in Google has a hard limit of how much time a team member can spend on toil, as opposed to engineering that produces lasting value: 50%.'
  os_concepts: []
  pr: null
---

# Toil, automation and production changes

Claims are listed newest source first. Everything here is `unverified`: an AI agent copied each quote from the source page; no human has checked it yet.

Source years in this note: 2025, 2022, 2020, 2018. A year is the publication or last-update year of the source, or the book edition year when the page gives none (SRE book 2016, Workbook 2018, Building Secure and Reliable Systems 2020).

## Claims at a glance

- `02-15` (org-fact): Google SRE says that had a global change been canaried with a progressive rollout strategy, the outage could have been curbed before it had global impact.
- `02-16` (org-fact): Google SRE says automating manual mitigations can reduce MTTR and that automated mitigation can come before root-causing.
- `02-17` (fact): The Enterprise Roadmap to SRE says that once toil overwhelms an SRE team, all other SRE activities grind to a halt.
- `02-18` (org-fact): Google's Zero Touch Prod requires every production change to be made by automation, prevalidated by software, or triggered through an audited breakglass mechanism.
- `02-19` (org-fact): Google estimates about 13% of all Google-evaluated outages could have been prevented or mitigated with Zero Touch Prod.
- `02-20` (org-fact): The SRE organization at Google is building on least privilege through automation, aiming for Zero Touch interfaces.
- `02-21` (org-fact): Zero Touch interfaces aim to make Google safer and reduce outages by removing direct human access to production roles.
- `02-22` (org-fact): SRE as practiced at Google has a hard limit of 50% of a team member's time on toil.

## Notes

- `org-fact` claims carry a Wayback Machine snapshot in `source.archive`. The exact quote was found in that snapshot on 2026-10-07.
- Podcast speakers are named in the claim. A speaker who is not a Google employee is not evidence about Google, so those claims are `fact`, not `org-fact`.
