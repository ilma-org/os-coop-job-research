---
doc_type: prompt-log
id: 2026-10-16-nacs-970-12-company-internship-author-check
author: "@nacs-970"
date: 2026-10-16
platform: Claude Code
model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
phase: exploration
role: author-check
significant: false
significant_reason: null
purpose: Blind author check of 17 claims in 12-organization-and-working-environment
pr: null
claims: [12-35, 12-36, 12-37, 12-38, 12-40, 12-42, 12-44, 12-46, 12-48, 12-49, 12-50, 12-51, 12-52, 12-53, 12-54, 12-55, 12-56]
redactions: 4
supporting_docs:
  - https://www.google.com/about/careers/applications/jobs/results/100028133205254854-software-engineering-site-reliability-engineering-bsms-intern-2027
  - https://web.archive.org/web/20260922191313/https://www.google.com/about/careers/applications/jobs/results/100028133205254854-software-engineering-site-reliability-engineering-bsms-intern-2027
  - https://www.google.com/about/careers/applications/students/
  - https://web.archive.org/web/20261009220028/https://www.google.com/about/careers/applications/students/
  - https://about.google/company-info/our-story/
  - https://web.archive.org/web/20261010142916/https://about.google/company-info/our-story/
  - https://blog.google/alphabet/investor-presentation-june-2026/
  - https://web.archive.org/web/20261011170255/https://blog.google/alphabet/investor-presentation-june-2026/
  - https://workspace.google.com/blog/product-announcements/workflows-across-workspace
  - https://web.archive.org/web/20260927101804/https://workspace.google.com/blog/product-announcements/workflows-across-workspace
---

## Turn 1 — user
Read the file [REDACTED:path]/input_internships-and-job-opportunities.txt and follow its instructions exactly. Read no other file on this machine.

Content of the input file:

You are an independent fact checker. You have no other context.

For each claim below, open its source URL yourself (WebFetch or curl) and decide whether the page supports the claim. Do not read any other file on this machine except this one. Do not look for other sources. Do not guess: if you cannot open a URL, say so.

For each claim, output exactly these five lines:
ID: <id>
VERDICT: supported | partial | unsupported
QUOTE: <one or two sentences copied verbatim from the page that best support the claim. Confirm in code that it is an exact substring of the page text.>
ARCHIVE: loads+quote-present | loads+quote-missing | fails | not-given   (only when an archive URL is listed)
ISSUES: <any wording in the claim that goes beyond what the page says, or: none>

Start your report with one line: MODEL: <your model name and exact model ID as given in your system prompt>.
Write the complete report to [REDACTED:path]/report_internships-and-job-opportunities.md and also return the same text as your final answer.

CLAIMS

ID: 12-35
CLAIM: The posting for Google's 2027 SRE internship in London says Google offers a range of internships in either Software Engineering or Site-Reliability Engineering in London.
URL: https://www.google.com/about/careers/applications/jobs/results/100028133205254854-software-engineering-site-reliability-engineering-bsms-intern-2027
ARCHIVE URL: https://web.archive.org/web/20260922191313/https://www.google.com/about/careers/applications/jobs/results/100028133205254854-software-engineering-site-reliability-engineering-bsms-intern-2027

ID: 12-36
CLAIM: The London 2027 SRE internship posting says the internship is intended for students in their penultimate or final year of an accredited full-time Bachelors or Masters degree program located in the EMEA region, and that participation requires being located in the UK for the duration of the program.
URL: https://www.google.com/about/careers/applications/jobs/results/100028133205254854-software-engineering-site-reliability-engineering-bsms-intern-2027
ARCHIVE URL: https://web.archive.org/web/20260922191313/https://www.google.com/about/careers/applications/jobs/results/100028133205254854-software-engineering-site-reliability-engineering-bsms-intern-2027

ID: 12-37
CLAIM: The London 2027 SRE internship posting says interns must be available to work full-time for a minimum of 13 weeks over Summer 2027, starting in May, June or July.
URL: https://www.google.com/about/careers/applications/jobs/results/100028133205254854-software-engineering-site-reliability-engineering-bsms-intern-2027
ARCHIVE URL: https://web.archive.org/web/20260922191313/https://www.google.com/about/careers/applications/jobs/results/100028133205254854-software-engineering-site-reliability-engineering-bsms-intern-2027

ID: 12-38
CLAIM: The London 2027 SRE internship posting asks applicants to complete the application before 23 October 2026 and says applications are reviewed on a rolling basis.
URL: https://www.google.com/about/careers/applications/jobs/results/100028133205254854-software-engineering-site-reliability-engineering-bsms-intern-2027
ARCHIVE URL: https://web.archive.org/web/20260922191313/https://www.google.com/about/careers/applications/jobs/results/100028133205254854-software-engineering-site-reliability-engineering-bsms-intern-2027

ID: 12-40
CLAIM: The London 2027 SRE internship posting says individuals applying for this position will not be eligible for immigration sponsorship.
URL: https://www.google.com/about/careers/applications/jobs/results/100028133205254854-software-engineering-site-reliability-engineering-bsms-intern-2027
ARCHIVE URL: https://web.archive.org/web/20260922191313/https://www.google.com/about/careers/applications/jobs/results/100028133205254854-software-engineering-site-reliability-engineering-bsms-intern-2027

ID: 12-42
CLAIM: The London 2027 SRE internship posting says that to start an application you need an updated CV or resume and a current unofficial or official transcript in English.
URL: https://www.google.com/about/careers/applications/jobs/results/100028133205254854-software-engineering-site-reliability-engineering-bsms-intern-2027
ARCHIVE URL: https://web.archive.org/web/20260922191313/https://www.google.com/about/careers/applications/jobs/results/100028133205254854-software-engineering-site-reliability-engineering-bsms-intern-2027

ID: 12-44
CLAIM: The London 2027 SRE internship posting says the Site Reliability intern works on software development projects that keep business-critical systems running, from code-level troubleshooting of traffic anomalies and service maintenance to monitoring, alerts and building new automation infrastructure.
URL: https://www.google.com/about/careers/applications/jobs/results/100028133205254854-software-engineering-site-reliability-engineering-bsms-intern-2027
ARCHIVE URL: https://web.archive.org/web/20260922191313/https://www.google.com/about/careers/applications/jobs/results/100028133205254854-software-engineering-site-reliability-engineering-bsms-intern-2027

ID: 12-46
CLAIM: The London 2027 SRE internship posting lists Unix/Linux among the preferred areas of practical or internship experience, together with AI/ML, infrastructure and web application development.
URL: https://www.google.com/about/careers/applications/jobs/results/100028133205254854-software-engineering-site-reliability-engineering-bsms-intern-2027
ARCHIVE URL: https://web.archive.org/web/20260922191313/https://www.google.com/about/careers/applications/jobs/results/100028133205254854-software-engineering-site-reliability-engineering-bsms-intern-2027

ID: 12-48
CLAIM: Google's careers site has a Students section whose menu lists Internships, Early career, Apprenticeships and Build your future.
URL: https://www.google.com/about/careers/applications/students/
ARCHIVE URL: https://web.archive.org/web/20261009220028/https://www.google.com/about/careers/applications/students/

## Turn 1 — assistant
MODEL: Sonnet 5.5, claude-sonnet-5-5

ID: 12-35
VERDICT: supported
QUOTE: We offer a range of internships in either Software Engineering or Site-Reliability Engineering in London.
ARCHIVE: loads+quote-present
ISSUES: none. The posting is a combined "Software Engineering, Site Reliability Engineering BS/MS Intern, 2027" posting, not an SRE-only one. "SRE internship" in the claim is shorthand for that.

ID: 12-36
VERDICT: supported
QUOTE: This internship is intended for students enrolled in their penultimate/final year of education in an accredited full-time Bachelors or Masters degree program located in the EMEA region. Participation in the internship program requires that you are located in the UK for the duration of the internship program.
ARCHIVE: loads+quote-present
ISSUES: none

ID: 12-37
VERDICT: supported
QUOTE: Interns will be required to be available to work full-time for a minimum of 13 weeks over the Summer 2027 (starting in May, June or July) for the duration of the program.
ARCHIVE: loads+quote-present
ISSUES: none

ID: 12-38
VERDICT: supported
QUOTE: Please complete your application before 23rd October 2026. We encourage you to apply as early as possible as we review applications on a rolling basis.
ARCHIVE: loads+quote-present
ISSUES: none. The page writes "23rd October 2026" and the claim writes "23 October 2026", which is the same date.

ID: 12-40
VERDICT: supported
QUOTE: Individuals applying for this position will not be eligible for immigration sponsorship.
ARCHIVE: loads+quote-present
ISSUES: none

ID: 12-42
VERDICT: supported
QUOTE: To start the application process, you will need an updated CV or resume and a current unofficial or official transcript in English.
ARCHIVE: loads+quote-present
ISSUES: none

ID: 12-44
VERDICT: supported
QUOTE: You will work on software development projects to keep important business-critical systems up and running, from code-level troubleshooting of traffic anomalies to maintenance of our services; from monitoring and alerts to building new automation infrastructure.
ARCHIVE: loads+quote-present
ISSUES: none. The sentence sits under the "Site Reliability Intern:" heading, so attributing it to the Site Reliability intern is correct. "Service maintenance" in the claim paraphrases "maintenance of our services".

ID: 12-46
VERDICT: supported
QUOTE: Relevant practical or internship experience with one or more of the following: AI/ML, infrastructure, web application development, Unix/Linux, mobile application development, distributed and parallel systems, machine learning, information retrieval, natural language processing, networking, developing large software systems, or security software development.
ARCHIVE: loads+quote-present
ISSUES: The line is under "Preferred qualifications" in the combined SWE/SRE posting, so it is not SRE-specific. The list has eight more items than the four the claim names, but the claim does not say the list is exhaustive. The four named items appear in the page's own order (AI/ML, infrastructure, web application development, Unix/Linux), so that part is accurate.

ID: 12-48
VERDICT: supported
QUOTE: Students Internships Early career Apprenticeships Build your future Applying to Google
ARCHIVE: loads+quote-present
ISSUES: The Students menu has a fifth entry, "Applying to Google", that the claim does not name. The claim does not say the list is complete, so this is a minor omission only. The static HTML of this page holds only the navigation (about 1.8k characters of text, no body content), so only the menu text could be checked, which is all the claim asserts.

## Turn 2 — user
Read the file [REDACTED:path]/input_google-services-and-customers.txt and follow its instructions exactly. Read no other file on this machine.

Content of the input file:

You are an independent fact checker. You have no other context.

For each claim below, open its source URL yourself (WebFetch or curl) and decide whether the page supports the claim. Do not read any other file on this machine except this one. Do not look for other sources. Do not guess: if you cannot open a URL, say so.

For each claim, output exactly these five lines:
ID: <id>
VERDICT: supported | partial | unsupported
QUOTE: <one or two sentences copied verbatim from the page that best support the claim. Confirm in code that it is an exact substring of the page text.>
ARCHIVE: loads+quote-present | loads+quote-missing | fails | not-given   (only when an archive URL is listed)
ISSUES: <any wording in the claim that goes beyond what the page says, or: none>

Start your report with one line: MODEL: <your model name and exact model ID as given in your system prompt>.
Write the complete report to [REDACTED:path]/report_google-services-and-customers.md and also return the same text as your final answer.

CLAIMS

ID: 12-49
CLAIM: Google's own company story page says the Google story begins in 1995 at Stanford University.
URL: https://about.google/company-info/our-story/
ARCHIVE URL: https://web.archive.org/web/20261010142916/https://about.google/company-info/our-story/

ID: 12-50
CLAIM: Google's own company story page says Google Inc. was officially born in August 1998, after Sun co-founder Andy Bechtolsheim wrote Larry Page and Sergey Brin a check for $100,000.
URL: https://about.google/company-info/our-story/
ARCHIVE URL: https://web.archive.org/web/20261010142916/https://about.google/company-info/our-story/

ID: 12-51
CLAIM: Google's own company story page says Google moved to its current headquarters, the Googleplex, in Mountain View, California.
URL: https://about.google/company-info/our-story/
ARCHIVE URL: https://web.archive.org/web/20261010142916/https://about.google/company-info/our-story/

ID: 12-52
CLAIM: Google's own company story page says Google makes hundreds of products used by billions of people, from YouTube and Android to Gmail and Google Search.
URL: https://about.google/company-info/our-story/
ARCHIVE URL: https://web.archive.org/web/20261010142916/https://about.google/company-info/our-story/

ID: 12-53
CLAIM: Alphabet's June 2026 investor presentation, published on Google's blog, says annual revenue more than doubled from 2020 to 2025, to over $400 billion.
URL: https://blog.google/alphabet/investor-presentation-june-2026/
ARCHIVE URL: https://web.archive.org/web/20261011170255/https://blog.google/alphabet/investor-presentation-june-2026/

ID: 12-54
CLAIM: Alphabet's June 2026 investor presentation says first-quarter 2026 revenue reached nearly $110 billion, up 22% year over year.
URL: https://blog.google/alphabet/investor-presentation-june-2026/
ARCHIVE URL: https://web.archive.org/web/20261011170255/https://blog.google/alphabet/investor-presentation-june-2026/

ID: 12-55
CLAIM: Alphabet's June 2026 investor presentation says Gemini now powers all of Google's 13 products that have over a billion users, including five that have over 3 billion users.
URL: https://blog.google/alphabet/investor-presentation-june-2026/
ARCHIVE URL: https://web.archive.org/web/20261011170255/https://blog.google/alphabet/investor-presentation-june-2026/

ID: 12-56
CLAIM: A May 2023 Google Workspace blog post says three billion users and 9 million paying customers use Google Workspace. The figure is from 2023, not current.
URL: https://workspace.google.com/blog/product-announcements/workflows-across-workspace
ARCHIVE URL: https://web.archive.org/web/20260927101804/https://workspace.google.com/blog/product-announcements/workflows-across-workspace

## Turn 2 — assistant
MODEL: Claude Sonnet 5.5 (claude-sonnet-5-5)

ID: 12-49
VERDICT: supported
QUOTE: The Google story begins in 1995 at Stanford University.
ARCHIVE: loads+quote-present
ISSUES: none

ID: 12-50
VERDICT: supported
QUOTE: In August 1998, Sun co-founder Andy Bechtolsheim wrote Larry and Sergey a check for $100,000, and Google Inc. was officially born.
ARCHIVE: loads+quote-present
ISSUES: none

ID: 12-51
VERDICT: supported
QUOTE: Google outgrew the garage and eventually moved to its current headquarters (a.k.a.“The Googleplex”) in Mountain View, California.
ARCHIVE: loads+quote-present
ISSUES: none

ID: 12-52
VERDICT: supported
QUOTE: Today, Google makes hundreds of products used by billions of people across the globe, from YouTube and Android to Gmail and, of course, Google Search.
ARCHIVE: loads+quote-present
ISSUES: none

ID: 12-53
VERDICT: supported
QUOTE: From 2020 to 2025, our annual revenue more than doubled to over $400 billion.
ARCHIVE: loads+quote-present
ISSUES: none

ID: 12-54
VERDICT: supported
QUOTE: In the first quarter of 2026, our momentum has continued as revenue reached nearly $110 billion, up 22% year-over-year.
ARCHIVE: loads+quote-present
ISSUES: none

ID: 12-55
VERDICT: supported
QUOTE: Gemini is now powering all of our 13 products that have over a billion users, including five that surpass 3 billion users.
ARCHIVE: loads+quote-present
ISSUES: none

ID: 12-56
VERDICT: supported
QUOTE: Three billion users and 9 million paying customers use Google Workspace to connect, create, and collaborate.
ARCHIVE: loads+quote-present
ISSUES: none (the page is dated May 2023. The live page text shows "May 16, 2023". The archived copy and the page's datePublished metadata show May 15, 2023.)

## Tool-call ledger
- Bash: python3 .agents/skills/agent-fact-check/scripts/blind_check.py prepare 2 note(s)
- Fresh agent context (blind check of internships-and-job-opportunities.md): its tool calls are not visible to this session
- Fresh agent context (blind check of google-services-and-customers.md): its tool calls are not visible to this session
- Bash: python3 .agents/skills/agent-fact-check/scripts/blind_check.py finish
