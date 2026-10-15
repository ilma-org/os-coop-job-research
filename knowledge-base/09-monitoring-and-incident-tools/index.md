---
doc_type: topic-index
topic: 09-monitoring-and-incident-tools
title: Monitoring and incident tools
assignment_section: "4.4"
report_sections: [9]
owner: "@nacs-970"
issue: 14
updated: 2026-10-14
---

# Monitoring and incident tools

Assignment 4.4: system monitoring tools. Core SRE area.

## Scope

- Metrics, logging and tracing (observability) tools
- Alerting and on-call tools
- Incident management and post-incident review practice

## Notes in this directory

The owner organizes notes (`topic-note` files) here. List them below as they are added.

<!-- notes:start -->
- [metrics-logging-and-tracing.md](metrics-logging-and-tracing.md): Metrics, logging and tracing tools in Google's SRE books. 16 claims (09-01 to 09-10, 09-21 to 09-26): 16 ai-checked.
- [incident-response-and-postmortems.md](incident-response-and-postmortems.md): Incident response and postmortem practice in Google's SRE books. 15 claims (09-11 to 09-20, 09-41 to 09-45): 15 ai-checked.
- [alerting-and-on-call.md](alerting-and-on-call.md): Alerting, paging and on-call tools in Google's SRE books. 15 claims (09-27 to 09-40, 09-46): 15 ai-checked.
<!-- notes:end -->

## Sources covered so far

Round 1 uses only the SRE book and the Workbook on https://sre.google/books/. Chapters cited by claims: SRE book ch.6, 10, 11, 12, 14, 15, 16, 31 and appendix D; Workbook ch.4, 5, 8, 9, 10. For the gap search below, 21 pages were fetched as plain text and searched for tool names: 14 SRE book pages and 7 Workbook pages on monitoring, alerting, on-call, incidents and postmortems.

## Not found yet

These items from the scope are missing from the 21 pages searched. They need other published sources, such as Google SRE job ads or tool documentation, or must be marked `assumption`.

- None of the 21 pages names Zipkin, Jaeger, OpenTelemetry, Splunk, Elasticsearch, Kibana, Datadog, Nagios, Graphite, Opsgenie, ServiceNow, Stackdriver or Google Cloud Monitoring. OpenCensus appears only in a footnote of Workbook ch.4.
- Tracing: Dapper is the only tracing tool named, and the books describe no trace-analysis workflow.
- No source says which monitoring, paging or incident tools Google SRE uses today. The SRE book page footer says copyright 2017 and the Workbook footer says 2018, so claims about Google describe what the books say, not current practice.
- Prometheus and Grafana appear in the 21 pages only as open source examples, not as tools used inside Google.
- PagerDuty appears only in one case study written by a PagerDuty author, so it is evidence about PagerDuty, not Google.
