---
doc_type: topic-index
topic: 08-devops-iac-cicd-tools
title: DevOps, infrastructure-as-code and CI/CD tools
assignment_section: "4.4"
report_sections: [9]
owner: "@nacs-970"
issue: 13
updated: 2026-10-09
---

# DevOps, infrastructure-as-code and CI/CD tools

Assignment 4.4: system and DevOps tools.

## Scope

- Git and version control workflow
- Docker, Kubernetes, SSH, shell scripting, Bash
- CI/CD tools
- Infrastructure-as-code and configuration management tools

## Notes in this directory

The owner organizes notes (`topic-note` files) here. List them below as they are added.

<!-- notes:start -->
- [release-engineering-and-ci-cd.md](release-engineering-and-ci-cd.md): Release engineering and CI/CD in Google's SRE books. 17 claims (08-01 to 08-16, 08-34): 17 ai-checked.
- [configuration-and-infrastructure-as-code.md](configuration-and-infrastructure-as-code.md): Configuration management and infrastructure-as-code in Google's SRE books. 10 claims (08-17 to 08-24, 08-35 to 08-36): 10 ai-checked.
- [containers-kubernetes-ssh-and-shell.md](containers-kubernetes-ssh-and-shell.md): Containers, Kubernetes, SSH and shell in Google's SRE books. 9 claims (08-25 to 08-33): 9 ai-checked.
<!-- notes:end -->

## Sources covered so far

Round 1 uses only the three books on https://sre.google/books/. Chapters cited by claims: SRE book ch.2, 7, 8; Workbook ch.8, 9, 14, 15, 16, 21; Building Secure and Reliable Systems ch.9, 14. For the gap search below, 106 pages were fetched as plain text and searched for tool names: 74 pages on sre.google (the SRE book and the Workbook: chapters, parts and appendices) and 32 pages from the Building Secure and Reliable Systems table of contents.

## Not found yet

These items from the scope are missing from the three books. They need other published sources, such as Google SRE job ads, or must be marked `assumption`.

- No fetched page names Ansible, Mercurial, Perforce, Travis CI, CircleCI, Google Cloud Build, GitHub Actions, Argo, TeamCity or Bamboo.
- No source says which Git hosting, CI/CD, infrastructure-as-code or container tools Google SRE uses today. The SRE book page footer says copyright 2017 and the Workbook footer says 2018, so claims about Google describe what the books say, not current practice.
- Docker appears on only 3 of the 106 pages. Claim 08-28 uses the one incident case study that names DockerHub. No page describes how SREs use Docker day to day.
- Shell scripts appear as something Google moved away from (08-31) and Bash appears once (08-32). No page was found that says SREs must write shell or Bash scripts. That needs Google SRE job ads.
- The books give no comparison of Terraform, Deployment Manager and Cloud Formation, and no guidance on choosing an infrastructure-as-code tool.
