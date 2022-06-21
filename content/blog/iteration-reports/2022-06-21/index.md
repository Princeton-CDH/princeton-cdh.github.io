---
title: "Jun 7 - Jun 18, 2022"
date: 2022-06-21
iteration_start: 2022-06-06
layout: iterationreport
slug: "21"
---

This iteration our primary focus was on Princeton Geniza Project, but we did close a few more issues related to the upcoming Startwords issue 3.  Our development velocity is on an upward trend — we closed **21** development points (16 issues), which gives us a rolling velocity of **13.7**.

## Princeton Geniza Project

This iteration we released version 4.5, which adds several features related to document date functionality: calendar conversion in admin for simple cases with Anno Mundi and Hijri calendars, improved date display on document details, and sorting and filtering search results by date. We also rolled out the new "related documents" page, improved image credits display for JTS content, and fixed a bug with handling Heidelberg IIIF. This update required a supporting release of `djiffy`, to add support for displaying Creative Commons licenses in addition to rightstatements.org licenses. Several features for the new image+transcription panel viewer were tested but not released; they won't go out until we have a full replacement for the current display, hopefully in the next release.

## Startwords

We finished work on the new authors list page, adjusted the footer to add a link to the authors page, and completed a few other small style-related changes.

## Demos

{{< figure src="featured_geniza_datesortfilter.png" caption="Screenshot of Princeton Geniza Project search page with document date filter and sort options.">}}

{{< figure src="startwords-authors.png" caption="Screenshot of Startwords author list page.">}}









