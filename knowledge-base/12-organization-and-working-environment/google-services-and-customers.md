---
doc_type: topic-note
topic: 12-organization-and-working-environment
title: "Google services, customers and the origin of SRE"
updated: 2026-10-14
claims:
  - id: 12-01
    claim: "The SRE book preface says Google SREs operate services such as planet-scale storage, email for hundreds of millions of users, and web search, which is where Google began."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Preface"
      url: https://sre.google/sre-book/preface/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20260807210643/https://sre.google/sre-book/preface/
    quote: "Finally, SREs are focused on operating services built atop our distributed computing systems, whether those services are planet-scale storage, email for hundreds of millions of users, or where Google began, web search."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-15-nine14282-12-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-15
      result: pass
      opened_source: true
  - id: 12-02
    claim: "The SRE book preface says the \"site\" in SRE first meant keeping the google.com website running, and that SRE now also runs services that are not websites, from internal infrastructure such as Bigtable to Google Cloud Platform for external developers."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, Preface"
      url: https://sre.google/sre-book/preface/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20260807210643/https://sre.google/sre-book/preface/
    quote: "The “site” in our name originally referred to SRE’s role in keeping the google.com website running, though we now run many more services, many of which aren’t themselves websites—from internal infrastructure such as Bigtable to products for external developers such as the Google Cloud Platform."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-15-nine14282-12-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-15
      result: pass
      opened_source: true
  - id: 12-03
    claim: "In the SRE book introduction, Benjamin Treynor Sloss writes that when he joined Google in 2003 he was tasked with running a \"Production Team\" of seven engineers."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, ch.1 Introduction"
      url: https://sre.google/sre-book/introduction/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20260919013803/https://sre.google/sre-book/introduction/
    quote: "When I joined Google in 2003 and was tasked with running a \"Production Team\" of seven engineers, my entire life up to that point had been software engineering."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-15-nine14282-12-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-15
      result: pass
      opened_source: true
  - id: 12-04
    claim: "The SRE book names Search, Ads, Gmail and Photos as Google services whose place on the risk continuum Google analyzes when setting reliability targets."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, ch.3 Embracing Risk"
      url: https://sre.google/sre-book/embracing-risk/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20260919013748/https://sre.google/sre-book/embracing-risk/
    quote: "where on the (nonlinear) risk continuum we should place Search, Ads, Gmail, or Photos"
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-15-nine14282-12-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-15
      result: pass
      opened_source: true
  - id: 12-06
    claim: "The SRE book says Google acquired YouTube and that in 2006 YouTube was focused on consumers."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, ch.3 Embracing Risk"
      url: https://sre.google/sre-book/embracing-risk/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20260919013748/https://sre.google/sre-book/embracing-risk/
    quote: "When Google acquired YouTube, we had to decide on the appropriate availability target for the website. In 2006, YouTube was focused on consumers and was in a very different phase of its business lifecycle than Google was at the time."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-15-nine14282-12-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-15
      result: pass
      opened_source: true
  - id: 12-34
    claim: "The SRE book says the majority of Google Apps for Work users are enterprises, which depend on its services such as Gmail, Calendar, Drive and Docs for their employees' daily work."
    type: org-fact
    status: human-verified
    source:
      title: "Site Reliability Engineering, ch.3 Embracing Risk"
      url: https://sre.google/sre-book/embracing-risk/
      kind: official-doc
      accessed: 2026-10-14
      archive: https://web.archive.org/web/20260919013748/https://sre.google/sre-book/embracing-risk/
    quote: "The majority of its users are enterprise users, some large and some small. These enterprises depend on Google Apps for Work services (e.g., Gmail, Calendar, Drive, Docs) to provide tools that enable their employees to perform their daily work."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code (desktop app)
      model: "Claude Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-14-Bximai-12-author-check-2.md
      result: supported
    ai_recheck:
      platform: Claude Code
      model: "Opus 5.5 (claude-opus-5-5)"
      prompt_log: prompts/2026-10-15-nine14282-12-reviewer-recheck.md
      result: supported
    review:
      by: "@Nine14282"
      date: 2026-10-15
      result: pass
      opened_source: true
---

# Google services, customers and the origin of SRE

## Summary

The Google SRE books describe the services Google SREs run: web search, where Google began, email for hundreds of millions of users, planet-scale storage, internal infrastructure such as Bigtable, and Google Cloud Platform for external developers. The SRE book names Search, Ads, Gmail and Photos as services it weighs for risk, and separates enterprise customers of Google Apps for Work from YouTube's consumer audience in 2006. SRE at Google began in 2003 with a "Production Team" of seven engineers. Product names such as Google Apps for Work are as the books give them and may not be current names. The books give no company history, revenue or customer counts beyond these examples.

## Key points

- SREs run Google's user services (web search, email, storage) and services that are not websites, such as Bigtable and Google Cloud Platform. (12-01, 12-02)
- SRE at Google started in 2003, when Benjamin Treynor Sloss took over a seven-engineer "Production Team". (12-03)
- Google weighs reliability risk per service, naming Search, Ads, Gmail and Photos. (12-04)
- Customers range from enterprises using Google Apps for Work (Gmail, Calendar, Drive, Docs) to consumers of YouTube, which Google acquired. (12-06, 12-34)
