---
doc_type: topic-note
topic: 06-system-architecture-infrastructure
title: "Client-server request path, RPC and load balancing"
updated: 2026-10-09
claims:
  - id: 06-01
    claim: "The SRE book defines a server as a piece of software that implements a service."
    type: fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "A piece of software that implements a service"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-02
    claim: "The SRE book says that, in traditional terms, a server's frontend is called the client and its backend is called the server."
    type: fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: null
    quote: "the frontend is called the client and the backend is called the server"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-03
    claim: "In the SRE book's example request, the user's DNS request ultimately ends up at Google's DNS server, which talks to GSLB (the Global Software Load Balancer)."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "This request ultimately ends up at Google’s DNS server, which talks to GSLB."
    os_concepts: ["networking"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-04
    claim: "The SRE book describes the Google Frontend (GFE) as a reverse proxy that terminates the TCP connection."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "is a reverse proxy that terminates the TCP connection"
    os_concepts: ["networking"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-05
    claim: "The SRE book says Google's services communicate using a Remote Procedure Call (RPC) infrastructure named Stubby."
    type: org-fact
    status: ai-checked
    source:
      title: "Site Reliability Engineering, ch.2 The Production Environment at Google, from the Viewpoint of an SRE"
      url: https://sre.google/sre-book/production-environment/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260911034439/https://sre.google/sre-book/production-environment/
    quote: "All of Google’s services communicate using a Remote Procedure Call (RPC) infrastructure named Stubby"
    os_concepts: ["networking"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-06
    claim: "The SRE Workbook says Google Cloud Load Balancer (GCLB) does not use DNS load balancing and uses anycast instead."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.11 Managing Load"
      url: https://sre.google/workbook/managing-load/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260909104922/https://sre.google/workbook/managing-load/
    quote: "GCLB does not use DNS load balancing. Instead, we use anycast"
    os_concepts: ["networking"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-07
    claim: "The SRE Workbook says Google implements stabilized anycast using Maglev, its custom load balancer."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.11 Managing Load"
      url: https://sre.google/workbook/managing-load/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260909104922/https://sre.google/workbook/managing-load/
    quote: "Google implements stabilized anycast using Maglev, our custom load balancer."
    os_concepts: ["networking"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-08
    claim: "The SRE Workbook says GCLB is the externalization of one of Google's internally developed global load balancing systems."
    type: org-fact
    status: ai-checked
    source:
      title: "The Site Reliability Workbook, ch.11 Managing Load"
      url: https://sre.google/workbook/managing-load/
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260909104922/https://sre.google/workbook/managing-load/
    quote: "the externalization of one of our internally developed global load balancing systems"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
  - id: 06-26
    claim: "Cloud Load Balancing documentation says external Application Load Balancers are implemented using Google Front Ends (GFEs) or managed proxies."
    type: org-fact
    status: ai-checked
    source:
      title: "Cloud Load Balancing documentation, Application Load Balancer overview"
      url: https://docs.cloud.google.com/load-balancing/docs/application-load-balancer
      kind: official-doc
      accessed: 2026-10-08
      archive: https://web.archive.org/web/20260927102916/https://docs.cloud.google.com/load-balancing/docs/application-load-balancer
    quote: "External Application Load Balancers are implemented using Google Front Ends (GFEs) or managed proxies."
    os_concepts: ["networking"]
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-09-csinside-06-author-check.md
      result: supported
---

# Client-server request path, RPC and load balancing

## Summary

The SRE book separates software from hardware: a server is a piece of software that implements a service, and in traditional terms a frontend is the client and a backend is the server (06-01, 06-02). In its example request, the user's DNS request reaches Google's DNS server and GSLB, the Google Frontend (GFE) reverse proxy terminates the TCP connection, and Google's services talk to each other over the Stubby RPC infrastructure (06-03 to 06-05). The SRE Workbook adds that Google Cloud Load Balancer uses anycast instead of DNS load balancing, stabilized by Google's Maglev load balancer, and that it is an externalized internal Google system (06-06 to 06-08). Current Google Cloud documentation confirms that GFEs are still in use: external Application Load Balancers are implemented with GFEs or managed proxies (06-26).

## Key points

- "Server" means software, not a machine; frontend and backend map to client and server. (06-01, 06-02)
- Request path: DNS and GSLB, then the GFE reverse proxy, then RPCs between services over Stubby. (06-03, 06-04, 06-05)
- Google Cloud Load Balancer uses anycast and Maglev, and grew out of an internal Google system. (06-06, 06-07, 06-08)
- Today's external Application Load Balancers on Google Cloud still run on GFEs or managed proxies. (06-26)

## Sources and limits

Round 1 used only the three books on https://sre.google/books/. Round 2 adds current official pages: Google Cloud documentation and blog posts, Google's data center site, and, for practice hardware, the Debian installation guide and the minikube documentation. The SRE book page footer says copyright 2017 and the Workbook page footer says copyright 2018; the Building Secure and Reliable Systems pages show no date. Each claim describes what its source says at the time of that source. Quotes are kept short on purpose; open the source to read the full passage.
