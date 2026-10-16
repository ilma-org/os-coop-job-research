---
doc_type: topic-note
topic: 12-organization-and-working-environment
title: "Google services, customers and the origin of SRE"
updated: 2026-10-16
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
  - id: 12-49
    claim: "Google's own company story page says the Google story begins in 1995 at Stanford University."
    type: org-fact
    status: ai-checked
    source:
      title: "How we started and where we are today - Google - About Google"
      url: https://about.google/company-info/our-story/
      kind: official-doc
      accessed: 2026-10-16
      archive: https://web.archive.org/web/20261010142916/https://about.google/company-info/our-story/
    quote: "The Google story begins in 1995 at Stanford University."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-16-nacs-970-12-company-internship-author-check.md
      result: supported
  - id: 12-50
    claim: "Google's own company story page says Google Inc. was officially born in August 1998, after Sun co-founder Andy Bechtolsheim wrote Larry Page and Sergey Brin a check for $100,000."
    type: org-fact
    status: ai-checked
    source:
      title: "How we started and where we are today - Google - About Google"
      url: https://about.google/company-info/our-story/
      kind: official-doc
      accessed: 2026-10-16
      archive: https://web.archive.org/web/20261010142916/https://about.google/company-info/our-story/
    quote: "In August 1998, Sun co-founder Andy Bechtolsheim wrote Larry and Sergey a check for $100,000, and Google Inc. was officially born."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-16-nacs-970-12-company-internship-author-check.md
      result: supported
  - id: 12-51
    claim: "Google's own company story page says Google moved to its current headquarters, the Googleplex, in Mountain View, California."
    type: org-fact
    status: ai-checked
    source:
      title: "How we started and where we are today - Google - About Google"
      url: https://about.google/company-info/our-story/
      kind: official-doc
      accessed: 2026-10-16
      archive: https://web.archive.org/web/20261010142916/https://about.google/company-info/our-story/
    quote: "Google outgrew the garage and eventually moved to its current headquarters (a.k.a.“The Googleplex”) in Mountain View, California."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-16-nacs-970-12-company-internship-author-check.md
      result: supported
  - id: 12-52
    claim: "Google's own company story page says Google makes hundreds of products used by billions of people, from YouTube and Android to Gmail and Google Search."
    type: org-fact
    status: ai-checked
    source:
      title: "How we started and where we are today - Google - About Google"
      url: https://about.google/company-info/our-story/
      kind: official-doc
      accessed: 2026-10-16
      archive: https://web.archive.org/web/20261010142916/https://about.google/company-info/our-story/
    quote: "Today, Google makes hundreds of products used by billions of people across the globe, from YouTube and Android to Gmail and, of course, Google Search."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-16-nacs-970-12-company-internship-author-check.md
      result: supported
  - id: 12-53
    claim: "Alphabet's June 2026 investor presentation, published on Google's blog, says annual revenue more than doubled from 2020 to 2025, to over $400 billion."
    type: org-fact
    status: ai-checked
    source:
      title: "Alphabet investor presentation: June 2026"
      url: https://blog.google/alphabet/investor-presentation-june-2026/
      kind: official-doc
      accessed: 2026-10-16
      archive: https://web.archive.org/web/20261011170255/https://blog.google/alphabet/investor-presentation-june-2026/
    quote: "From 2020 to 2025, our annual revenue more than doubled to over $400 billion."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-16-nacs-970-12-company-internship-author-check.md
      result: supported
  - id: 12-54
    claim: "Alphabet's June 2026 investor presentation says first-quarter 2026 revenue reached nearly $110 billion, up 22% year over year."
    type: org-fact
    status: ai-checked
    source:
      title: "Alphabet investor presentation: June 2026"
      url: https://blog.google/alphabet/investor-presentation-june-2026/
      kind: official-doc
      accessed: 2026-10-16
      archive: https://web.archive.org/web/20261011170255/https://blog.google/alphabet/investor-presentation-june-2026/
    quote: "In the first quarter of 2026, our momentum has continued as revenue reached nearly $110 billion, up 22% year-over-year."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-16-nacs-970-12-company-internship-author-check.md
      result: supported
  - id: 12-55
    claim: "Alphabet's June 2026 investor presentation says Gemini now powers all of Google's 13 products that have over a billion users, including five that have over 3 billion users."
    type: org-fact
    status: ai-checked
    source:
      title: "Alphabet investor presentation: June 2026"
      url: https://blog.google/alphabet/investor-presentation-june-2026/
      kind: official-doc
      accessed: 2026-10-16
      archive: https://web.archive.org/web/20261011170255/https://blog.google/alphabet/investor-presentation-june-2026/
    quote: "Gemini is now powering all of our 13 products that have over a billion users, including five that surpass 3 billion users."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-16-nacs-970-12-company-internship-author-check.md
      result: supported
  - id: 12-56
    claim: "A May 2023 Google Workspace blog post says three billion users and 9 million paying customers use Google Workspace. The figure is from 2023, not current."
    type: org-fact
    status: ai-checked
    source:
      title: "Build workflows across Google Workspace to connect user experiences across apps (blog post, May 2023)"
      url: https://workspace.google.com/blog/product-announcements/workflows-across-workspace
      kind: official-doc
      accessed: 2026-10-16
      archive: https://web.archive.org/web/20260927101804/https://workspace.google.com/blog/product-announcements/workflows-across-workspace
    quote: "Three billion users and 9 million paying customers use Google Workspace to connect, create, and collaborate."
    os_concepts: []
    pr: null
    ai_check:
      platform: Claude Code
      model: "Claude Sonnet 5.5 (claude-sonnet-5-5)"
      prompt_log: prompts/2026-10-16-nacs-970-12-company-internship-author-check.md
      result: supported
---

# Google services, customers and the origin of SRE

## Summary

The Google SRE books describe the services Google SREs run: web search, where Google began, email for hundreds of millions of users, planet-scale storage, internal infrastructure such as Bigtable, and Google Cloud Platform for external developers. The SRE book names Search, Ads, Gmail and Photos as services it weighs for risk, and separates enterprise customers of Google Apps for Work from YouTube's consumer audience in 2006. SRE at Google began in 2003 with a "Production Team" of seven engineers. Product names such as Google Apps for Work are as the books give them and may not be current names. Google's own company page and Alphabet's June 2026 investor presentation add the company's start in 1995 and incorporation in 1998, its Mountain View headquarters, annual revenue above $400 billion in 2025, and user counts (12-49 to 12-56). None of the sources we read gives a total customer count. The only figure is a May 2023 Google Workspace post that gives 9 million paying customers for Workspace alone.

## Key points

- SREs run Google's user services (web search, email, storage) and services that are not websites, such as Bigtable and Google Cloud Platform. (12-01, 12-02)
- SRE at Google started in 2003, when Benjamin Treynor Sloss took over a seven-engineer "Production Team". (12-03)
- Google weighs reliability risk per service, naming Search, Ads, Gmail and Photos. (12-04)
- Customers range from enterprises using Google Apps for Work (Gmail, Calendar, Drive, Docs) to consumers of YouTube, which Google acquired. (12-06, 12-34)
- Google's story starts in 1995 at Stanford University, and Google Inc. was officially born in August 1998; its headquarters is the Googleplex in Mountain View, California. (12-49, 12-50, 12-51)
- Google makes hundreds of products used by billions of people. (12-52)
- Alphabet's annual revenue more than doubled from 2020 to 2025, to over $400 billion, and first-quarter 2026 revenue was nearly $110 billion. (12-53, 12-54)
- Thirteen Google products have over a billion users, five of them over 3 billion. (12-55)
- A May 2023 post says Google Workspace has three billion users and 9 million paying customers; this is not a current figure. (12-56)
