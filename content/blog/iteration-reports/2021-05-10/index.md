---
title: "May 10, 2021"
date: 2021-05-10
iteration_start: 2021-04-26
layout: iterationreport
---

This iteration we closed 10 development points for a rolling velocity of 8. Our primary focus was on Princeton Geniza Project, but we did a small amount of planned work on the CDH website, ansible deploy scripts, and a very small amount of unplanned work on Shakespeare and Company Project to fix a time-sensitive bug.

## Princeton Geniza Project
Accepted development work consists of a preliminary document detail page for the public site and admin editing enhancements, including a footnote count for the source list in admin, a way to edit and link to documents on the fragment edit view, and a certainty flag for TextBlocks to handle potential joins.

Completed design work includes a decision on document titles for detail pages as well as search and browse, revisions to the document detail page based on the initial implementation, and completed wireframes for sort and filter on search for all screens.

## CDH Website

We completed planned maintenance and released version 3.0.2 — this update removes all mezzanine dependencies and resets database migrations, making it possible for the site to finally be upgraded to newer versions of django and wagtail. This also resolved a bug in the 3.0 release.

## Shakespeare and Company Project

The bugfix release was a small change to address a limitation on the 100 years twitter code  — it did not handle subscriptions and renewals with no known duration, as revealed by a tweet on Monday. The bugfix was out in time to handle the next occurrence on Friday.

## Demos
{{< figure src="featured-geniza-document-detail.png" caption="Screenshot of preliminary document detail page for Princeton Geniza Project">}}






