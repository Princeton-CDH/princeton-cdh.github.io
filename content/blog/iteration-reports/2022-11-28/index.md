---
title: "Nov 14 - Nov 25, 2022"
date: 2022-11-28
iteration_start: 2022-11-14
layout: iterationreport
slug: "28"
---

We completed a couple of major things before the Thanksgiving holiday — completed the PPA migration to PUL infrastructure, and completed the dataset export work for PGP. We 
completed **12** development points for a rolling velocity of **5.33** - the low velocity is due to the number of chores required to complete the PPA migration.  We also finally completed the charter for the Lenape Timetree project, and will be circulating it to project stakeholders soon.

## Princeton Prosody Archive

We completed the last few steps for the migration, released version **3.8.1** and switched the production site over so it is running on PUL infrastructure. We've already completed some initial upgrades (python version) that are easier to manage now, and are circling back to in-progress that wasn't completed when PPA was in active development in August.

## Princeton Geniza Project

We released version **4.11** with a few search improvements needed to decommission PGPv3 and completed work on dataset exports which will be the basis for published datasets from the project data. We also setup Zenodo sync for the codebase, registering a DOI and adding a citation file to make the code more citable. 

We also have a large number of old issues that were closed thanks to some work from PGP project managers going through and reviewing — some of them have already been addressed, others are duplicates, and others are no longer priorities.

## Demos

{{< figure src="featured_pgp-metadata-flatviewer.png" caption="Princeton Geniza Project [documents data export displayed in Flat GitHub's Flat viewer](https://flatgithub.com/princetongenizalab/pgp-metadata?filename=data%2Fdocuments.csv&sha=549836002cd41abf84e61829439b7b4bf3505af0).">}}

{{< figure src="pgp-metadata-commits.png" caption="Princeton Geniza Project metadata repository showing [commit history with co-author information](https://github.com/princetongenizalab/pgp-metadata/commits/main)." >}}

{{< figure src="pgp-description-bigram-search.png" caption="Princeton Geniza Project search showing [partial word searching on document descriptions](https://geniza.princeton.edu/en/documents/?q=al-fad)." >}}









