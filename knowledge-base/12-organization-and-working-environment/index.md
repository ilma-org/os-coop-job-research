---
doc_type: topic-index
topic: 12-organization-and-working-environment
title: Organization and working environment (Google)
assignment_section: "4.7"
report_sections: [5]
owner: "@Bximai"
issue: 17
updated: 2026-10-14
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
- [google-services-and-customers.md](google-services-and-customers.md): Google services, customers and the origin of SRE. 6 claims (12-01 to 12-04, 12-06, 12-34): 6 ai-checked.
- [sre-organization-at-google.md](sre-organization-at-google.md): How SRE is organized at Google. 11 claims (12-07 to 12-17): 11 ai-checked.
- [working-environment-and-culture.md](working-environment-and-culture.md): SRE working environment and culture at Google. 12 claims (12-18 to 12-29): 12 ai-checked.
- [internships-and-job-opportunities.md](internships-and-job-opportunities.md): Internships and job opportunities at Google. 4 claims (12-30 to 12-33): 4 ai-checked.
<!-- notes:end -->

## Sources covered so far

Round 1 used only the three books on https://sre.google/books/: Site Reliability Engineering, The Site Reliability Workbook, and Building Secure and Reliable Systems. 86 book pages (36 from the SRE book, 25 from the Workbook, 25 from Building Secure and Reliable Systems) and the books and careers pages of sre.google were fetched as plain text and searched for organization, culture, team, on-call, training, hiring and intern terms. Chapters cited by claims: SRE book Preface, ch.1, 3, 11, 31; Workbook ch.1, 8, 17, 20; Building Secure and Reliable Systems ch.19, 21.

Computing infrastructure and technologies at Google (datacenters, Borg, Linux, tools) are covered by topics 04, 05, 06 and 07, so this topic does not repeat them.

## Not found yet

These items have no opened source that `scripts/add_claim.py` has checked. Do not put them in the report as facts.

- Company background: founding year, founders, headquarters, parent company (Alphabet), employee count, revenue. The books do not give them. Try official Google pages such as about.google or Alphabet investor pages.
- A current list of Google products and customer segments. The books name products only as examples, some under old names (Google Apps for Work).
- Google's AI and data activities. Not searched in this round.
- Offices and locations of SRE teams, working hours, and remote or hybrid work policy.
- An SRE internship or student program at Google, its eligibility and how to apply. The books mention interns only in two case studies (12-32, 12-33). Try Google's careers pages and current job ads.
- Current Google SRE job openings. The sre.google careers page links to Google careers but is not one of the books, so it was not used in this round.
- Size of the Google SRE organization.
