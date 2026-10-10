---
doc_type: prompt-log
id: 2026-10-11-nacs-970-hard-skills-reviewer-recheck
author: "@nacs-970"
date: 2026-10-11
platform: Claude Code
model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
phase: exploration
role: reviewer-recheck
significant: false
significant_reason: null
purpose: Blind reviewer recheck of 30 claims in 02-hard-skills
pr: 27
claims: [02-01, 02-02, 02-03, 02-04, 02-05, 02-06, 02-07, 02-08, 02-09, 02-10, 02-11, 02-12, 02-13, 02-14, 02-15, 02-16, 02-17, 02-18, 02-19, 02-20, 02-21, 02-22, 02-23, 02-24, 02-25, 02-26, 02-27, 02-28, 02-29, 02-30]
redactions: 12
supporting_docs:
  - https://sre.google/prodcast/transcripts/sre-prodcast-03-10/
  - https://sre.google/static/pdf/LessonsLearnedFromTwoDecades.pdf
  - https://sre.google/static/pdf/TrainingSiteReliabilityEngineers.pdf
  - https://sre.google/workbook/canarying-releases/
  - https://sre.google/workbook/eliminating-toil/
  - https://sre.google/resources/practices-and-processes/sre-fundamentals-course/
  - https://sre.google/resources/practices-and-processes/slo-adoption-and-usage/
  - https://sre.google/prodcast/transcripts/sre-prodcast-04-02/
  - https://sre.google/resources/practices-and-processes/measuring-reliability/
  - https://sre.google/static/pdf/reliable_data_processing_with_minimal_toil.pdf
  - https://sre.google/workbook/data-processing/
  - https://sre.google/workbook/how-sre-relates/
  - https://sre.google/workbook/implementing-slos/
  - https://sre.google/resources/practices-and-processes/twenty-years-of-sre-lessons-learned/
  - https://sre.google/static/pdf/enterprise-roadmap-to-sre.pdf
  - https://google.github.io/building-secure-and-reliable-systems/raw/ch03.html
  - https://google.github.io/building-secure-and-reliable-systems/raw/ch05.html
  - https://sre.google/prodcast/transcripts/sre-prodcast-05-03/
  - https://google.github.io/building-secure-and-reliable-systems/raw/ch07.html
  - https://sre.google/static/pdf/IncidentManagementGuide.pdf
  - https://google.github.io/building-secure-and-reliable-systems/raw/ch04.html
  - https://sre.google/static/pdf/CaseStudiesInfrastructureChangeManagement.pdf
  - https://sre.google/workbook/managing-load/
---

## Turn 1 — user
You are an independent fact checker. You know nothing about any project; work only from this message.

INPUT FILE: [REDACTED:path]
It lists claims. Each has an ID, a CLAIM sentence and the source URL it cites.
OUTPUT FILE: [REDACTED:path]

Read ONLY the input file. Do not read, list or search any other file or directory except your own download directory (create a new empty directory under [REDACTED:path] named dl_sre-role and put every download there). Do not open any git repository.

TASK: for every claim, open its URL yourself (WebFetch, or curl then read the text; for PDFs use curl then pdftotext; run any Python you write with `python3 -I`). Find the passage that the claim rests on. Decide whether the PAGE ITSELF says what the CLAIM says. A claim is "supported" only if nothing in it goes beyond the page: check names, roles, numbers, scope words (such as "all", "always", "at Google"), tense, and who is speaking. If part of the claim is not on the page, say which part.

Write the output file with one block per claim, in input order, exactly in this shape (5 lines, then a blank line). First line of the file: `MODEL: <your model name and version>`.
ID: <id>
VERDICT: supported | partial | unsupported | unreachable
QUOTE: <one or two sentences copied exactly from the page that support the claim; if none, write none>
SOURCE_URL_OPENED: <the URL you actually read>
ISSUES: <each part of the claim the page does not say, or the wording that is stronger than the page; write none if there is none>

Do not guess. If you cannot open a URL, use `unreachable` and say why in ISSUES. Do not shorten or paraphrase the QUOTE. When finished, reply with one line: the output file path and the count of claims per verdict.

Content of the input file:

ID: 02-01
CLAIM: Cody Smith says Google SRE had a mission-control program where engineers from pure dev teams joined SRE for a six-month rotation.
URL: https://sre.google/prodcast/transcripts/sre-prodcast-03-10/

ID: 02-02
CLAIM: Google says unit tests have limited scope and do not fully replicate the runtime environment, which is why it advocates integration testing.
URL: https://sre.google/static/pdf/LessonsLearnedFromTwoDecades.pdf

ID: 02-03
CLAIM: The report quotes Ben Treynor Sloss that an SRE's job is to apply software engineering skills to operations problems.
URL: https://sre.google/static/pdf/TrainingSiteReliabilityEngineers.pdf

ID: 02-04
CLAIM: In Google's experience, a majority of incidents are triggered by binary or configuration pushes.
URL: https://sre.google/workbook/canarying-releases/

ID: 02-05
CLAIM: Google limits the time SRE teams spend on operational work (toil and non-toil) to 50%.
URL: https://sre.google/workbook/eliminating-toil/

ID: 02-06
CLAIM: Many Google teams manage and configure services using version control and process organizational requests as pull requests, called changelists (CLs), which brings code review and continuous deployment to internal service configuration changes.
URL: https://sre.google/workbook/eliminating-toil/

## Turn 1 — assistant
MODEL: Claude Sonnet 5.5 (claude-sonnet-5-5)
ID: 02-01
VERDICT: supported
QUOTE: CODY SMITH: ... We had this mission-control program where engineers would come over from pure dev teams to join SRE for a rotation of six months. And then if that had worked out well, they might stay.
SOURCE_URL_OPENED: https://sre.google/prodcast/transcripts/sre-prodcast-03-10/
ISSUES: none (the speaker label is CODY SMITH; the episode is titled "Maglev: load balancing at Google with Cody Smith and Trisha Weir"; the page says "we had", past tense, matching the claim)

ID: 02-02
VERDICT: supported
QUOTE: Unit tests have intentionally limited scope, and are super helpful, but they also don't fully replicate the runtime environment and productionized demands that might exist. For this reason, we are big advocates of integration testing!
SOURCE_URL_OPENED: https://sre.google/static/pdf/LessonsLearnedFromTwoDecades.pdf
ISSUES: none (the PDF is the Google SRE team's own publication; the claim drops the word "intentionally" and the phrase "and productionized demands that might exist", which does not change the meaning)

ID: 02-03
VERDICT: supported
QUOTE: According to Ben Treynor Sloss, vice president of 24x7 at Google, “an SRE’s job is to apply software engineering skills to operations problems.
SOURCE_URL_OPENED: https://sre.google/static/pdf/TrainingSiteReliabilityEngineers.pdf
ISSUES: none (the PDF is the O'Reilly report "Training Site Reliability Engineers"; the quote appears in the section "Skills That Support a Career Shift Toward SRE")

ID: 02-04
VERDICT: supported
QUOTE: In Google’s experience, a majority of incidents are triggered by binary or configuration pushes (see Results of Postmortem Analysis ).
SOURCE_URL_OPENED: https://sre.google/workbook/canarying-releases/
ISSUES: none

ID: 02-05
VERDICT: supported
QUOTE: Google limits the time SRE teams spend on operational work (including both toil- and non-toil-intensive work) at 50% (for more context on why, see Chapter 5 in our first book).
SOURCE_URL_OPENED: https://sre.google/workbook/eliminating-toil/
ISSUES: none (the claim's "toil and non-toil" is a compression of "both toil- and non-toil-intensive work"; same meaning)

ID: 02-06
VERDICT: supported
QUOTE: Many teams at Google manage and configure their services using version control, and process organizational requests in the form of pull requests (called changelists , or CLs). This approach requires little or no involvement from the service’s team, but gives us the benefits of code review and continuous deployment processes to validate, test, and deploy internal service configuration changes.
SOURCE_URL_OPENED: https://sre.google/workbook/eliminating-toil/
ISSUES: none (the claim's "brings code review and continuous deployment" paraphrases "gives us the benefits of code review and continuous deployment processes")

## Turn 2 — user
You are an independent fact checker. You know nothing about any project; work only from this message.

INPUT FILE: [REDACTED:path]
It lists claims. Each has an ID, a CLAIM sentence and the source URL it cites.
OUTPUT FILE: [REDACTED:path]

Read ONLY the input file. Do not read, list or search any other file or directory except your own download directory (create a new empty directory under [REDACTED:path] named dl_slos and put every download there). Do not open any git repository.

TASK: for every claim, open its URL yourself (WebFetch, or curl then read the text; for PDFs use curl then pdftotext; run any Python you write with `python3 -I`). Find the passage that the claim rests on. Decide whether the PAGE ITSELF says what the CLAIM says. A claim is "supported" only if nothing in it goes beyond the page: check names, roles, numbers, scope words (such as "all", "always", "at Google"), tense, and who is speaking. If part of the claim is not on the page, say which part.

Write the output file with one block per claim, in input order, exactly in this shape (5 lines, then a blank line). First line of the file: `MODEL: <your model name and version>`.
ID: <id>
VERDICT: supported | partial | unsupported | unreachable
QUOTE: <one or two sentences copied exactly from the page that support the claim; if none, write none>
SOURCE_URL_OPENED: <the URL you actually read>
ISSUES: <each part of the claim the page does not say, or the wording that is stronger than the page; write none if there is none>

Do not guess. If you cannot open a URL, use `unreachable` and say why in ISSUES. Do not shorten or paraphrase the QUOTE. When finished, reply with one line: the output file path and the count of claims per verdict.

Content of the input file:

ID: 02-07
CLAIM: The SRE Fundamentals with Google course covers identifying key metrics, building SLOs and alerts, and systems design including single points of failure, performance and capacity planning.
URL: https://sre.google/resources/practices-and-processes/sre-fundamentals-course/

ID: 02-08
CLAIM: A report says SLOs are reliability targets measured by SLIs, and measurable SLOs eliminate conflicts around change management and event handling.
URL: https://sre.google/resources/practices-and-processes/slo-adoption-and-usage/

ID: 02-09
CLAIM: Peter Pellerzi, who works on Google data center infrastructure, says the metric they look at is availability, with a target of five nines.
URL: https://sre.google/prodcast/transcripts/sre-prodcast-04-02/

ID: 02-10
CLAIM: The talk defines an SLI as time series data showing how good the level of service is, often from logs or sampled counters.
URL: https://sre.google/resources/practices-and-processes/measuring-reliability/

ID: 02-11
CLAIM: Data processing can be declared reliable if well-reasoned SLOs are met; the freshness SLO asks whether the job completed in time and measures how long we can wait for the data to be available.
URL: https://sre.google/static/pdf/reliable_data_processing_with_minimal_toil.pdf

ID: 02-12
CLAIM: The Workbook says each alert condition should have a playbook entry describing the steps to recovery, and that Google finds it useful to link this documentation in alert messages sent to on-call engineers.
URL: https://sre.google/workbook/data-processing/

ID: 02-13
CLAIM: SRE is a term and job role coined by Ben Treynor Sloss, a VP of engineering at Google.
URL: https://sre.google/workbook/how-sre-relates/

ID: 02-14
CLAIM: At Google, a well-thought-out and adopted SLO is key to making data-informed decisions about the opportunity cost of reliability work and how to prioritize it.
URL: https://sre.google/workbook/implementing-slos/

## Turn 2 — assistant
MODEL: Claude Sonnet 5.5 (claude-sonnet-5-5)
ID: 02-07
VERDICT: supported
QUOTE: Learn to identify key metrics, build effective SLOs, and create alerts to maintain performance standards. Dive into Systems Design by developing systems from product specifications, assessing single points of failure, and understanding performance and capacity planning.
SOURCE_URL_OPENED: https://sre.google/resources/practices-and-processes/sre-fundamentals-course/
ISSUES: none

ID: 02-08
VERDICT: supported
QUOTE: To realize the full benefits of SRE, organizations need well-thought out reliability targets known as service level objectives (SLOs) that are measured by service level indicators (SLIs), a quantitative measure of an aspect of the service. As examined in this report, these measurable goals set forth in an organization’s SLOs eliminate the conflicts inherent in change management and event handling that cause the pace of innovation to slow and business to suffer.
SOURCE_URL_OPENED: https://sre.google/resources/practices-and-processes/slo-adoption-and-usage/
ISSUES: none

ID: 02-09
VERDICT: supported
QUOTE: So what's of concern, the metric that we look at is availability, 99.999, whatever, five nines of availability. That's our target.
SOURCE_URL_OPENED: https://sre.google/prodcast/transcripts/sre-prodcast-04-02/
ISSUES: none. The page names the guest as Peter Pellerzi (Distinguished Engineer, Google), assigned to the construction team that builds the physical data center infrastructure, so the description matches. He states the five nines target himself, in the first person plural ("our target").

ID: 02-10
VERDICT: supported
QUOTE: Service Level Indicator (SLI) Time series data which can tell us how good the level of service is. Often from logs or sampled counters.
SOURCE_URL_OPENED: https://sre.google/resources/practices-and-processes/measuring-reliability/
ISSUES: none. Minor wording note: the slide sits under "The SLO Model Recap" heading and says "can tell us how good", while the claim says "showing how good". This is a fair paraphrase.

ID: 02-11
VERDICT: supported
QUOTE: To apply an SRE approach, we can declare data processing to be reliable if well-reasoned SLOs are met. The freshness SLO ("Did the job complete in time?") is fairly straightforward to measure: it is a measure of how long we can wait for the data to be available.
SOURCE_URL_OPENED: https://sre.google/static/pdf/reliable_data_processing_with_minimal_toil.pdf
ISSUES: none

ID: 02-12
VERDICT: supported
QUOTE: Each alert condition in your system should have a corresponding playbook entry that describes the steps to recovery. At Google, we find it useful to link this documentation in any alert messages sent to on-call engineers.
SOURCE_URL_OPENED: https://sre.google/workbook/data-processing/
ISSUES: none. The page is Workbook Chapter 13 (Data Processing Pipelines), section "Playbook entries".

ID: 02-13
VERDICT: supported
QUOTE: Site Reliability Engineering (SRE) is a term (and associated job role) coined by Ben Treynor Sloss, a VP of engineering at Google.
SOURCE_URL_OPENED: https://sre.google/workbook/how-sre-relates/
ISSUES: none

ID: 02-14
VERDICT: supported
QUOTE: At Google, we’ve learned that a well-thought-out and adopted SLO is key to making data-informed decisions about the opportunity cost of reliability work, and to determining how to appropriately prioritize that work.
SOURCE_URL_OPENED: https://sre.google/workbook/implementing-slos/
ISSUES: none

## Turn 3 — user
You are an independent fact checker. You know nothing about any project; work only from this message.

INPUT FILE: [REDACTED:path]
It lists claims. Each has an ID, a CLAIM sentence and the source URL it cites.
OUTPUT FILE: [REDACTED:path]

Read ONLY the input file. Do not read, list or search any other file or directory except your own download directory (create a new empty directory under [REDACTED:path] named dl_toil and put every download there). Do not open any git repository.

TASK: for every claim, open its URL yourself (WebFetch, or curl then read the text; for PDFs use curl then pdftotext; run any Python you write with `python3 -I`). Find the passage that the claim rests on. Decide whether the PAGE ITSELF says what the CLAIM says. A claim is "supported" only if nothing in it goes beyond the page: check names, roles, numbers, scope words (such as "all", "always", "at Google"), tense, and who is speaking. If part of the claim is not on the page, say which part.

Write the output file with one block per claim, in input order, exactly in this shape (5 lines, then a blank line). First line of the file: `MODEL: <your model name and version>`.
ID: <id>
VERDICT: supported | partial | unsupported | unreachable
QUOTE: <one or two sentences copied exactly from the page that support the claim; if none, write none>
SOURCE_URL_OPENED: <the URL you actually read>
ISSUES: <each part of the claim the page does not say, or the wording that is stronger than the page; write none if there is none>

Do not guess. If you cannot open a URL, use `unreachable` and say why in ISSUES. Do not shorten or paraphrase the QUOTE. When finished, reply with one line: the output file path and the count of claims per verdict.

Content of the input file:

ID: 02-15
CLAIM: Google SRE describes a YouTube outage in which a caching config change fully hobbled the service for 13 minutes, and says canarying those global changes with a progressive rollout could have curbed it before it had global impact.
URL: https://sre.google/resources/practices-and-processes/twenty-years-of-sre-lessons-learned/

ID: 02-16
CLAIM: Google SRE says it is sometimes better to use an automated mitigation first and save root-causing for after user impact has been avoided.
URL: https://sre.google/resources/practices-and-processes/twenty-years-of-sre-lessons-learned/

ID: 02-17
CLAIM: The Enterprise Roadmap to SRE says that once toil overwhelms an SRE team, all other SRE activities grind to a halt.
URL: https://sre.google/static/pdf/enterprise-roadmap-to-sre.pdf

ID: 02-18
CLAIM: Google's Zero Touch Prod requires every production change to be made by automation, prevalidated by software, or triggered through an audited breakglass mechanism.
URL: https://google.github.io/building-secure-and-reliable-systems/raw/ch03.html

ID: 02-19
CLAIM: Google estimates about 13% of all Google-evaluated outages could have been prevented or mitigated with Zero Touch Prod.
URL: https://google.github.io/building-secure-and-reliable-systems/raw/ch03.html

ID: 02-20
CLAIM: The SRE organization at Google is working to build on least privilege through automation, aiming for Zero Touch interfaces.
URL: https://google.github.io/building-secure-and-reliable-systems/raw/ch05.html

ID: 02-21
CLAIM: Zero Touch interfaces aim to make Google safer and reduce outages by removing direct human access to production roles.
URL: https://google.github.io/building-secure-and-reliable-systems/raw/ch05.html

ID: 02-22
CLAIM: SRE as practiced at Google has a hard limit of 50% of a team member's time on toil.
URL: https://sre.google/workbook/how-sre-relates/

## Turn 3 — assistant
MODEL: Claude Sonnet 5.5 (claude-sonnet-5-5)
ID: 02-15
VERDICT: supported
QUOTE: Turns out, caching was a pretty critical feature for YouTube, and the config change had some unintended consequences that fully hobbled the service for 13 minutes. Had we canaried those global changes with a progressive rollout strategy, this outage could have been curbed before it had global impact.
SOURCE_URL_OPENED: https://sre.google/resources/practices-and-processes/twenty-years-of-sre-lessons-learned/
ISSUES: none (the page's intro separately calls the 2016 YouTube incident a fifteen-minute global outage from a bug in the distributed memory caching system; the 13-minute caching configuration change is the "Canary all changes" lesson and is described as such in the claim)

ID: 02-16
VERDICT: supported
QUOTE: Sometimes it is better to use an automated mitigation first and save the root-causing for after user impact has been avoided.
SOURCE_URL_OPENED: https://sre.google/resources/practices-and-processes/twenty-years-of-sre-lessons-learned/
ISSUES: none

ID: 02-17
VERDICT: supported
QUOTE: Once toil overwhelms your team, all the other SRE activities will grind to a halt.
SOURCE_URL_OPENED: https://sre.google/static/pdf/enterprise-roadmap-to-sre.pdf
ISSUES: none (the PDF is "Enterprise Roadmap to SRE" by James Brookbank and Steve McGhee; the claim rephrases "your team" as "an SRE team" and "will grind" as "grind", which does not change the meaning)

ID: 02-18
VERDICT: supported
QUOTE: Zero Touch Prod is a project at Google that requires every change in production to be made by automation (instead of humans), prevalidated by software, or triggered through an audited breakglass mechanism.
SOURCE_URL_OPENED: https://google.github.io/building-secure-and-reliable-systems/raw/ch03.html
ISSUES: none

ID: 02-19
VERDICT: supported
QUOTE: We estimate that ~13% of all Google-evaluated outages could have been prevented or mitigated with Zero Touch Prod.
SOURCE_URL_OPENED: https://google.github.io/building-secure-and-reliable-systems/raw/ch03.html
ISSUES: none (claim says "about 13%" for the page's "~13%"; the estimate is the authors' own, which the claim attributes to Google)

ID: 02-20
VERDICT: supported
QUOTE: The SRE organization at Google is working to build upon the concept of least privilege through automation, with the goal of moving to what we call Zero Touch interfaces.
SOURCE_URL_OPENED: https://google.github.io/building-secure-and-reliable-systems/raw/ch05.html
ISSUES: none

ID: 02-21
VERDICT: supported
QUOTE: The specific goal of these interfaces—like Zero Touch Production (ZTP), described in Chapter 3, and Zero Touch Networking (ZTN)—is to make Google safer and reduce outages by removing direct human access to production roles.
SOURCE_URL_OPENED: https://google.github.io/building-secure-and-reliable-systems/raw/ch05.html
ISSUES: none (the page adds that humans keep indirect access through tooling and automation; the claim does not contradict this)

ID: 02-22
VERDICT: supported
QUOTE: SRE as practiced in Google has a hard limit of how much time a team member can spend on toil, as opposed to engineering that produces lasting value: 50%.
SOURCE_URL_OPENED: https://sre.google/workbook/how-sre-relates/
ISSUES: none (the page notes many people think of the limit as a cap, and says it is more useful to think of it as a guarantee; the claim's "hard limit of 50%" matches the page)

## Turn 4 — user
You are an independent fact checker. You know nothing about any project; work only from this message.

INPUT FILE: [REDACTED:path]
It lists claims. Each has an ID, a CLAIM sentence and the source URL it cites.
OUTPUT FILE: [REDACTED:path]

Read ONLY the input file. Do not read, list or search any other file or directory except your own download directory (create a new empty directory under [REDACTED:path] named dl_trouble and put every download there). Do not open any git repository.

TASK: for every claim, open its URL yourself (WebFetch, or curl then read the text; for PDFs use curl then pdftotext; run any Python you write with `python3 -I`). Find the passage that the claim rests on. Decide whether the PAGE ITSELF says what the CLAIM says. A claim is "supported" only if nothing in it goes beyond the page: check names, roles, numbers, scope words (such as "all", "always", "at Google"), tense, and who is speaking. If part of the claim is not on the page, say which part.

Write the output file with one block per claim, in input order, exactly in this shape (5 lines, then a blank line). First line of the file: `MODEL: <your model name and version>`.
ID: <id>
VERDICT: supported | partial | unsupported | unreachable
QUOTE: <one or two sentences copied exactly from the page that support the claim; if none, write none>
SOURCE_URL_OPENED: <the URL you actually read>
ISSUES: <each part of the claim the page does not say, or the wording that is stronger than the page; write none if there is none>

Do not guess. If you cannot open a URL, use `unreachable` and say why in ISSUES. Do not shorten or paraphrase the QUOTE. When finished, reply with one line: the output file path and the count of claims per verdict.

Content of the input file:

ID: 02-23
CLAIM: Heather Adkins says insider-threat controls and mistake prevention often have very similar solutions.
URL: https://sre.google/prodcast/transcripts/sre-prodcast-05-03/

ID: 02-24
CLAIM: Building Secure and Reliable Systems says global load balancing helps move traffic between GFE and backends, and gives the example that Google can redirect traffic during a datacenter outage, reducing mitigation time.
URL: https://google.github.io/building-secure-and-reliable-systems/raw/ch07.html

ID: 02-25
CLAIM: Unchecked recurring outages increase operational toil and can exhaust error budgets, erode user trust and hurt revenue.
URL: https://sre.google/static/pdf/IncidentManagementGuide.pdf

ID: 02-26
CLAIM: Resilience testing checks a system survives faults, latency or disruptions, while recovery testing checks it can return to a stable state after a full shutdown.
URL: https://sre.google/static/pdf/LessonsLearnedFromTwoDecades.pdf

ID: 02-27
CLAIM: Building Secure and Reliable Systems asks what the SLOs are for metrics such as uptime or 95th- and 99th-percentile response latency, and how the system responds under load above a certain threshold.
URL: https://google.github.io/building-secure-and-reliable-systems/raw/ch04.html

ID: 02-28
CLAIM: In a Google case study (the Steamroller project), new memory limits for Borg jobs did not account for small RAM spikes, so Borg immediately killed tasks that went over them even slightly, causing localized service disruptions and latency.
URL: https://sre.google/static/pdf/CaseStudiesInfrastructureChangeManagement.pdf

ID: 02-29
CLAIM: Google's Disaster Recovery Testing (DiRT) frequently simulates regional outages against pipelines that depend on a datacenter.
URL: https://sre.google/workbook/data-processing/

ID: 02-30
CLAIM: Google announces IPs via BGP from multiple points in its network and relies on BGP routing to deliver packets to the closest frontend location that can terminate a TCP session.
URL: https://sre.google/workbook/managing-load/

## Turn 4 — assistant
MODEL: Claude Sonnet 5.5 (claude-sonnet-5-5)
ID: 02-23
VERDICT: supported
QUOTE: And if you think about, how do I keep an employee from doing something malicious, or how do I keep an employee from making a mistake, the solutions are often very similar.
SOURCE_URL_OPENED: https://sre.google/prodcast/transcripts/sre-prodcast-05-03/
ISSUES: none. The speaker is HEATHER ADKINS in the transcript (she leads Google's Office of Cybersecurity Resilience). The page says "insider threat" in the preceding sentence ("a lot of the work we'd done on insider threat from a cybersecurity perspective matched almost perfectly with how SRE was thinking about reliability"); "insider-threat controls" in the claim is a light paraphrase of "keep an employee from doing something malicious".

ID: 02-24
VERDICT: supported
QUOTE: Global load balancing helps move traffic between GFE and backends. For example, we can redirect traffic during a datacenter outage, reducing mitigation time.
SOURCE_URL_OPENED: https://google.github.io/building-secure-and-reliable-systems/raw/ch07.html
ISSUES: none. The page says "we" (the book's authors, describing Google's frontend design); the claim's "Google can redirect traffic" matches that context.

ID: 02-25
VERDICT: supported
QUOTE: Left unchecked, outages tend to regularly resurface and accumulate over time. This increases the operational toil for the team and can lead to expended error budgets, eroded user trust, and impacted revenue.
SOURCE_URL_OPENED: https://sre.google/static/pdf/IncidentManagementGuide.pdf
ISSUES: none material. Wording differences only: the claim says "exhaust error budgets" and "hurt revenue" where the page says "expended error budgets" and "impacted revenue"; "can" correctly applies to the last three effects, and the page states the toil increase without "can" as the claim does.

ID: 02-26
VERDICT: supported
QUOTE: While resilience testing verifies that your service or system could survive in the event of faults, latency, or disruptions, recovery testing verifies that your service can transition back to homeostasis after a full shutdown.
SOURCE_URL_OPENED: https://sre.google/static/pdf/LessonsLearnedFromTwoDecades.pdf
ISSUES: none material. The claim renders "homeostasis" as "a stable state", a paraphrase.

ID: 02-27
VERDICT: supported
QUOTE: What are the service level objectives (SLOs) for metrics such as uptime or 95th-percentile and 99th-percentile response latency? How does the system respond under load above a certain threshold?
SOURCE_URL_OPENED: https://google.github.io/building-secure-and-reliable-systems/raw/ch04.html
ISSUES: none. The page poses these as example questions under "Nonfunctional Requirements", which matches "asks".

ID: 02-28
VERDICT: supported
QUOTE: The team used this as the new baseline measurement for each Borg job to be applied after restarting the jobs but did not take into account the small spikes in RAM usage. Therefore, if any tasks went over their new memory limits, even by a small amount, Borg killed them immediately, causing localized service disruptions and latency.
SOURCE_URL_OPENED: https://sre.google/static/pdf/CaseStudiesInfrastructureChangeManagement.pdf
ISSUES: none material. The page says the Steamroller team's baseline measurement (a 90-day usage period, 100th percentile for RAM) did not account for small RAM spikes; the claim says the "new memory limits" did not account for them, which is a faithful compression. The document is a Google SRE report ("Case Studies in Infrastructure Change Management", Wendy Look and Mark Dallman), Case Study 1: Moonshot.

ID: 02-29
VERDICT: supported
QUOTE: For example, many pipelines at Google depend on the availability of the datacenter where they run. Our Disaster Recovery Testing (DiRT) frequently targets these systems, simulating a regional outage.
SOURCE_URL_OPENED: https://sre.google/workbook/data-processing/
ISSUES: none.

ID: 02-30
VERDICT: supported
QUOTE: Google announces IPs via Border Gateway Protocol (BGP) from multiple points in our network. We rely on the BGP routing mesh to deliver packets from a user to the closest frontend location that can terminate a transmission control protocol (TCP) session.
SOURCE_URL_OPENED: https://sre.google/workbook/managing-load/
ISSUES: none. The claim abbreviates "Border Gateway Protocol" and "transmission control protocol" to BGP and TCP, and says "BGP routing" for "the BGP routing mesh".

## Tool-call ledger
- Bash: python3 -I (extract each claim's text and source URL from the four notes at the PR head into one input file per note; the stored quotes are never written)
- Fresh agent context (blind recheck of sre-role-and-skills.md): its tool calls are not visible to this session
- Note: this checker could not write its report file and returned the report text as its final message; the text was saved unchanged to the report file named above
- Fresh agent context (blind recheck of slos-error-budgets-and-monitoring.md): its tool calls are not visible to this session
- Note: this checker could not write its report file and returned the report text as its final message; the text was saved unchanged to the report file named above
- Fresh agent context (blind recheck of toil-and-automation.md): its tool calls are not visible to this session
- Fresh agent context (blind recheck of troubleshooting-and-systems-knowledge.md): its tool calls are not visible to this session
- Bash: python3 -I (compare each checker QUOTE with the stored quote; the stored quotes were never shown to a checker)
