---
title: "Mar 15 — 29, 2021"
date: 2021-03-29
iteration_start: 2021-03-15
layout: iterationreport
slug: "29"
aliases:
  - /blog/2021/03/march-29-2021/
---

The points and total number of issues closed for the last iteration is quite high — 42 points total, 25 for cdhweb and 17 for geniza, which results in a rolling velocity of 27. I'd like to think this is a sign that we're gaining momentum on geniza work, but suspect that the high numbers are due to work that rolled over from the last iteration and a significant push to finish cdhweb 3.0.

## Princeton Geniza Project
We're continuing to make progress on building out the database and importing existing data. New features include a document suppression feature, automatic tracking of historic shelfmarks, and a "needs review" field where content editors can add notes about problems or questions in the data that are used to create a queue of records with problems to be addressed.  We also finished testing on data import issues from previous iterations, most notably preliminary document & fragment import.

## CDH Website
We completed features related to blog migration and managing site menus and navigation via wagtail, and resolved a number of longstanding bugs that are no longer an issue now that the site is on wagtail instead of mezzanine. There are only a few small issues rolling over for final testing and review before the 3.0 release can be created and deployed production.

## Demos
{{< figure src="geniza-awaiting-review.png" caption="Screenshot of Geniza admin interface with new awaiting review feature">}}
{{< figure src="cdhweb-wagtail-recents.png" caption="Screenshot of cdhweb wagtail interface showing recent edits, based on page history events">}}
{{< figure src="featured-cdhweb-page-history.png" caption="Screenshot of cdhweb wagtail interface showing page history with migration event">}}






