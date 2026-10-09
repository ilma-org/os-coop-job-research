---
doc_type: topic-note
topic: 02-hard-skills
title: What Google looks for in an SRE
updated: '2026-10-07'
claims:
- id: 02-01
  claim: Cody Smith says Google SRE had a mission-control program where engineers from pure dev teams joined SRE for a six-month rotation.
  type: org-fact
  status: unverified
  source:
    title: 'Google SRE Prodcast transcript: Maglev: load balancing at Google with Cody Smith and Trisha Weir'
    url: https://sre.google/prodcast/transcripts/sre-prodcast-03-10/
    kind: other
    accessed: '2026-10-07'
    archive: https://web.archive.org/web/20260615075901/https://sre.google/prodcast/transcripts/sre-prodcast-03-10/
  quote: We had this mission-control program where engineers would come over from pure dev teams to join SRE for a rotation of six months.
  os_concepts: []
  pr: null
- id: 02-02
  claim: Google says unit tests have limited scope and do not fully replicate the runtime environment, which is why it advocates integration testing.
  type: org-fact
  status: unverified
  source:
    title: Lessons Learned from Two Decades of Site Reliability Engineering (Google SRE 20th anniversary PDF)
    url: https://sre.google/static/pdf/LessonsLearnedFromTwoDecades.pdf
    kind: official-doc
    accessed: '2026-10-07'
    archive: https://web.archive.org/web/20260908065110/https://sre.google/static/pdf/LessonsLearnedFromTwoDecades.pdf
  quote: Unit tests have intentionally limited scope, and are super helpful, but they also don't fully replicate the runtime environment and productionized demands that might exist.
  os_concepts: []
  pr: null
- id: 02-03
  claim: The report quotes Ben Treynor Sloss that an SRE's job is to apply software engineering skills to operations problems.
  type: org-fact
  status: unverified
  source:
    title: Training Site Reliability Engineers (O'Reilly report by Google authors, 2019/2020)
    url: https://sre.google/static/pdf/TrainingSiteReliabilityEngineers.pdf
    kind: official-doc
    accessed: '2026-10-07'
    archive: https://web.archive.org/web/20251123125903/https://sre.google/static/pdf/TrainingSiteReliabilityEngineers.pdf
  quote: an SRE’s job is to apply software engineering skills to operations problems.
  os_concepts: []
  pr: null
- id: 02-04
  claim: In Google's experience, a majority of incidents are triggered by binary or configuration pushes.
  type: org-fact
  status: unverified
  source:
    title: 'The Site Reliability Workbook: Canarying Releases'
    url: https://sre.google/workbook/canarying-releases/
    kind: official-doc
    accessed: '2026-10-07'
    archive: https://web.archive.org/web/20260919200604/https://sre.google/workbook/canarying-releases/
  quote: In Google’s experience, a majority of incidents are triggered by binary or configuration pushes
  os_concepts: []
  pr: null
- id: 02-05
  claim: Google limits the time SRE teams spend on operational work (toil and non-toil) to 50%.
  type: org-fact
  status: unverified
  source:
    title: 'The Site Reliability Workbook: Eliminating Toil'
    url: https://sre.google/workbook/eliminating-toil/
    kind: official-doc
    accessed: '2026-10-07'
    archive: https://web.archive.org/web/20260909103330/https://sre.google/workbook/eliminating-toil/
  quote: Google limits the time SRE teams spend on operational work (including both toil- and non-toil-intensive work) at 50%
  os_concepts: []
  pr: null
- id: 02-06
  claim: Many Google teams manage and configure services using version control and process organizational requests as pull requests, called changelists (CLs), which brings code review and continuous deployment to configuration changes.
  type: org-fact
  status: unverified
  source:
    title: 'The Site Reliability Workbook: Eliminating Toil'
    url: https://sre.google/workbook/eliminating-toil/
    kind: official-doc
    accessed: '2026-10-07'
    archive: https://web.archive.org/web/20260909103330/https://sre.google/workbook/eliminating-toil/
  quote: Many teams at Google manage and configure their services using version control, and process organizational requests in the form of pull requests (called changelists, or CLs).
  os_concepts: []
  pr: null
---

# What Google looks for in an SRE

Claims are listed newest source first. Everything here is `unverified`: an AI agent copied each quote from the source page; no human has checked it yet.

Source years in this note: 2025, 2020, 2019, 2018. A year is the publication or last-update year of the source, or the book edition year when the page gives none (SRE book 2016, Workbook 2018, Building Secure and Reliable Systems 2020).

## Claims at a glance

- `02-01` (org-fact): Cody Smith says Google SRE had a mission-control program where engineers from pure dev teams joined SRE for a six-month rotation.
- `02-02` (org-fact): Google says unit tests have limited scope and do not fully replicate the runtime environment, which is why it advocates integration testing.
- `02-03` (org-fact): The report quotes Ben Treynor Sloss that an SRE's job is to apply software engineering skills to operations problems.
- `02-04` (org-fact): In Google's experience, a majority of incidents are triggered by binary or configuration pushes.
- `02-05` (org-fact): Google limits the time SRE teams spend on operational work (toil and non-toil) to 50%.
- `02-06` (org-fact): Many Google teams manage and configure services using version control and process organizational requests as pull requests, called changelists (CLs), which brings code review and continuous deployment to configuration changes.

## Notes

- `org-fact` claims carry a Wayback Machine snapshot in `source.archive`. The exact quote was found in that snapshot on 2026-10-07.
- Podcast speakers are named in the claim. A speaker who is not a Google employee is not evidence about Google, so those claims are `fact`, not `org-fact`.
