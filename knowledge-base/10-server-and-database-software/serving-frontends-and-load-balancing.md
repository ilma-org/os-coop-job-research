---
doc_type: topic-note
topic: 10-server-and-database-software
title: "Front ends, load balancing and overload handling"
updated: 2026-10-14
claims:
  - id: 10-01
    claim: "In a section headed \"Example: Google's frontend design\", Building Secure and Reliable Systems says Google Front End (GFE) serves as a frontend layer to most Google services, implemented as a microservice, so these services are not directly exposed to the internet."
    type: org-fact
    status: human-verified
    source:
      title: "Building Secure and Reliable Systems, Chapter 7"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch07.html
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260616012631/https://google.github.io/building-secure-and-reliable-systems/raw/ch07.html
    quote: "Google Front End (GFE) serves as a frontend layer to most Google services, implemented as a microservice, so these services aren’t directly exposed to the internet."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-nine14282-server-db-author-check-4.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-10-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 10-02
    claim: "In a section headed \"Example: Google's frontend design\", Building Secure and Reliable Systems says GFE also terminates traffic for incoming HTTP(S), TCP and TLS proxies, provides DDoS attack countermeasures, and routes and load balances traffic to Google Cloud services."
    type: org-fact
    status: human-verified
    source:
      title: "Building Secure and Reliable Systems, Chapter 7"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch07.html
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260616012631/https://google.github.io/building-secure-and-reliable-systems/raw/ch07.html
    quote: "GFE also terminates traffic for incoming HTTP(S), TCP, and TLS proxies; provides DDoS attack countermeasures; and routes and load balances traffic to Google Cloud services."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-nine14282-server-db-author-check-4.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-10-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 10-03
    claim: "In a section headed \"Example: Google's frontend design\", Building Secure and Reliable Systems says that if a service becomes overloaded, GFE can serve as a mitigation point by dropping or absorbing connections before the load reaches the backends."
    type: org-fact
    status: human-verified
    source:
      title: "Building Secure and Reliable Systems, Chapter 7"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch07.html
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260616012631/https://google.github.io/building-secure-and-reliable-systems/raw/ch07.html
    quote: "If a service becomes overloaded, GFE can serve as a mitigation point by dropping or absorbing connections before the load reaches the backends."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-nine14282-server-db-author-check-4.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-10-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 10-05
    claim: "Building Secure and Reliable Systems says load shedding is done by returning errors rather than serving requests, and throttling of clients by delaying responses until closer to the request deadline."
    type: fact
    status: human-verified
    source:
      title: "Building Secure and Reliable Systems, Chapter 8"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch08.html
      kind: official-doc
      accessed: 2026-10-12
      archive: https://web.archive.org/web/20260704103623/https://google.github.io/building-secure-and-reliable-systems/raw/ch08.html
    quote: "Load shedding is done by returning errors rather than serving requests. Throttling of clients is done by delaying responses until closer to the request deadline."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-server-db-author-check-2.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-10-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 10-06
    claim: "Building Secure and Reliable Systems says that when the load on a component starts to exceed its capacity, you want it to serve errors for all excessive requests rather than crash, because crashing makes all of the component's capacity unavailable, not just the capacity for the excess requests."
    type: fact
    status: human-verified
    source:
      title: "Building Secure and Reliable Systems, Chapter 8"
      url: https://google.github.io/building-secure-and-reliable-systems/raw/ch08.html
      kind: official-doc
      accessed: 2026-10-07
      archive: https://web.archive.org/web/20260704103623/https://google.github.io/building-secure-and-reliable-systems/raw/ch08.html
    quote: "When the load on a component starts to exceed its capacity, you want the component to serve errors for all excessive requests rather than crashing. Crashing makes all of the component’s capacity unavailable—not just the capacity for the excess requests."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-server-db-author-check-2.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-10-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 10-08
    claim: "The SRE Workbook says that, at the time it was written, GCLB (Google Cloud Load Balancer) did not use DNS load balancing, because DNS-based load balancing relies on client cooperation to properly expire and refetch DNS records."
    type: org-fact
    status: human-verified
    source:
      title: "The Site Reliability Workbook: Managing Load"
      url: https://sre.google/workbook/managing-load/
      kind: official-doc
      accessed: 2026-10-12
      archive: https://web.archive.org/web/20260909104922/https://sre.google/workbook/managing-load/
    quote: "We also discussed an endemic problem of this approach: it relies on client cooperation to properly expire and refetch DNS records. For this reason, GCLB does not use DNS load balancing."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-nine14282-server-db-author-check-5.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-10-reviewer-recheck-2.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
  - id: 10-09
    claim: "The SRE book says that no matter how efficient a load balancing policy is, eventually some part of a system will become overloaded, and that gracefully handling overload conditions is fundamental to running a reliable serving system."
    type: fact
    status: human-verified
    source:
      title: "Site Reliability Engineering (SRE book) - Handling Overload"
      url: https://sre.google/sre-book/handling-overload/
      kind: official-doc
      accessed: 2026-10-12
      archive: https://web.archive.org/web/20260927190503/https://sre.google/sre-book/handling-overload/
    quote: "But no matter how efficient your load balancing policy, eventually some part of your system will become overloaded. Gracefully handling overload conditions is fundamental to running a reliable serving system."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-12-nine14282-server-db-author-check-2.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-14-nacs-970-10-reviewer-recheck.md
      result: supported
    review:
      by: "@nacs-970"
      date: 2026-10-14
      result: pass
      opened_source: true
---

# Front ends, load balancing and overload handling

## Summary

In an example section on Google's frontend design, Building Secure and Reliable Systems says Google Front End (GFE) is a frontend layer to most Google services that terminates traffic, provides DDoS countermeasures, and routes and load balances traffic to Google Cloud services (10-01, 10-02), and that it can drop or absorb connections when a service is overloaded (10-03). The same book says a component should serve errors for excessive requests rather than crash (10-06) and describes load shedding and client throttling (10-05). The SRE Workbook says that, at the time it was written, Google Cloud Load Balancer (GCLB) did not use DNS load balancing because DNS-based load balancing relies on client cooperation (10-08), and the SRE book says some part of a system will eventually become overloaded however efficient its load balancing policy is (10-09). Each claim rests on one source; no second source was compared, and this note has no claim yet on web and application servers such as Apache or Nginx.

## Key points

- In a section headed "Example: Google's frontend design", Building Secure and Reliable Systems says GFE serves as a frontend layer to most Google services, so they are not directly exposed to the internet (10-01).
- The same example section says GFE terminates HTTP(S), TCP and TLS proxy traffic, provides DDoS countermeasures, and routes and load balances traffic to Google Cloud services (10-02).
- The same example section says that if a service becomes overloaded, GFE can drop or absorb connections before the load reaches the backends (10-03).
- The same book says a component under too much load should serve errors rather than crash, because crashing removes all of its capacity (10-06).
- The same book says load shedding returns errors rather than serving requests, and throttling delays responses until closer to the request deadline (10-05).
- The SRE Workbook says that, at the time it was written, Google Cloud Load Balancer (GCLB) did not use DNS load balancing because it relies on client cooperation to expire and refetch DNS records (10-08).
- The SRE book says gracefully handling overload is fundamental to running a reliable serving system (10-09).

Claims are listed newest source first. Each claim's `status` in the front matter says how far it has been checked.

Source years in this note: 2020, 2018, 2016. A year is the publication or last-update year of the source, or the book edition year when the page gives none (SRE book 2016, Workbook 2018, Building Secure and Reliable Systems 2020).

## Claims at a glance

- `10-01` (org-fact): In a section headed "Example: Google's frontend design", Building Secure and Reliable Systems says Google Front End (GFE) serves as a frontend layer to most Google services, implemented as a microservice, so these services are not directly exposed to the internet.
- `10-02` (org-fact): In a section headed "Example: Google's frontend design", Building Secure and Reliable Systems says GFE also terminates traffic for incoming HTTP(S), TCP and TLS proxies, provides DDoS attack countermeasures, and routes and load balances traffic to Google Cloud services.
- `10-03` (org-fact): In a section headed "Example: Google's frontend design", Building Secure and Reliable Systems says that if a service becomes overloaded, GFE can serve as a mitigation point by dropping or absorbing connections before the load reaches the backends.
- `10-05` (fact): Building Secure and Reliable Systems says load shedding is done by returning errors rather than serving requests, and throttling of clients by delaying responses until closer to the request deadline.
- `10-06` (fact): Building Secure and Reliable Systems says that when the load on a component starts to exceed its capacity, you want it to serve errors for all excessive requests rather than crash, because crashing makes all of the component's capacity unavailable, not just the capacity for the excess requests.
- `10-08` (org-fact): The SRE Workbook says that, at the time it was written, GCLB (Google Cloud Load Balancer) did not use DNS load balancing, because DNS-based load balancing relies on client cooperation to properly expire and refetch DNS records.
- `10-09` (fact): The SRE book says that no matter how efficient a load balancing policy is, eventually some part of a system will become overloaded, and that gracefully handling overload conditions is fundamental to running a reliable serving system.

## Notes

- `org-fact` claims carry a Wayback Machine snapshot in `source.archive`. The exact quote was found in that snapshot on the claim's `source.accessed` date.
- Podcast speakers are named in the claim. A speaker who is not a Google employee is not evidence about Google, so those claims are `fact`, not `org-fact`.
- `10-01` to `10-03` come from a section of Building Secure and Reliable Systems headed "Example: Google's frontend design". They describe Google's design as the book's example.
