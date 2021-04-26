---
title: "April 26, 2021"
date: 2021-04-26
iteration_start: 2021-04-12
layout: iterationreport
---

This iteration we closed 11 development points for a rolling velocity of 19, still coming down from the massive number of points closed three iterations ago.

## Princeton Geniza Project
We made more improvements to the data import, fixing Language+Script mapping based on the new display names and resolving all previously unhandled languages, and most notably parsing history input information (names and dates) into structured django log entries to preserve the known edit history of PGP documents. We also completed preliminary work on footnote models for linking scholarship records to documents.

For design, wireframes for cluster view browse and search results pages for all screens (desktop, tablet, mobile) were all completed.

## CDH Website
We fixed a couple more bugs in the 3.0 version and released a planned 3.0.1 cleanup release to remove exodus code specific to the shift to wagtail. This is a necessary step to removing mezzanine, which will finally let us upgrade to newer versions of Dljango and python. 


## Demos
{{< figure src="featured-pgp-change-history.png" caption="Screenshot of change history for a test imported document showing historic changes">}}

{{< figure src="pgp-first-last-edits.png" caption="Screenshot of earliest and most recent changes for a test import document, shown on the document dit form">}}






