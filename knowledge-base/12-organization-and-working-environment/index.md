---
doc_type: topic-index
topic: 12-organization-and-working-environment
title: Organization and working environment (Google)
assignment_section: "4.7"
report_sections: [5]
owner: "@Bximai"
issue: 17
updated: 2026-10-16
---

# Organization and working environment

Assignment Appendix G. Target company: **Google** (SRE). Do not claim what Google uses without reliable published evidence (Google job ads, Google's SRE books, official Google pages), and archive every source. Anything about Google's internal environment that no published source states is labeled as an assumption.

## Scope

- Organization background, products and services, customers
- Technologies and IT/software/data/AI activities
- Computing infrastructure where publicly available
- Working environment or culture where reliable information exists
- Existing or previous internship, COOP or job opportunities

## Notes in this directory

The owner organizes notes (`topic-note` files) here. List them below as they are added.

<!-- notes:start -->
- [google-services-and-customers.md](google-services-and-customers.md): Google services, customers and the origin of SRE. 14 claims (12-01 to 12-04, 12-06, 12-34, 12-49 to 12-56): 8 ai-checked, 6 human-verified.
- [sre-organization-at-google.md](sre-organization-at-google.md): How SRE is organized at Google. 11 claims (12-07 to 12-17): 11 human-verified.
- [working-environment-and-culture.md](working-environment-and-culture.md): SRE working environment and culture at Google. 12 claims (12-18 to 12-29): 12 human-verified.
- [internships-and-job-opportunities.md](internships-and-job-opportunities.md): Internships and job opportunities at Google. 13 claims (12-30 to 12-33, 12-35 to 12-38, 12-40, 12-42, 12-44, 12-46, 12-48): 9 ai-checked, 4 human-verified.
<!-- notes:end -->

## Sources covered so far

Round 1 used only the three books on https://sre.google/books/: Site Reliability Engineering, The Site Reliability Workbook, and Building Secure and Reliable Systems. 86 book pages (36 from the SRE book, 25 from the Workbook, 25 from Building Secure and Reliable Systems) and the books and careers pages of sre.google were fetched as plain text and searched for organization, culture, team, on-call, training, hiring and intern terms. Chapters cited by claims: SRE book Preface, ch.1, 3, 11, 31; Workbook ch.1, 8, 17, 20; Building Secure and Reliable Systems ch.19, 21.

Computing infrastructure and technologies at Google (datacenters, Borg, Linux, tools) are covered by topics 04, 05, 06 and 07, so this topic does not repeat them.

## Not found yet

These items have no opened source that `scripts/add_claim.py` has checked. Do not put them in the report as facts.

- A current list of Google products and customer segments. The books name products only as examples, some under old names (Google Apps for Work).
- Google's AI and data activities. Not searched in this round.
- Offices and locations of SRE teams, working hours, and remote or hybrid work policy.
- A total count of Google's business customers. The only figure found is for Workspace alone, from May 2023 (12-56).
- An SRE internship for students outside the EMEA region. The 2027 posting found (12-35 to 12-48) is limited to students in EMEA.
- Employee count and the number of SRE staff. Not searched in this round.
