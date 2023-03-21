---
title: "Feb 27 - Mar 10, 2023"
date: 2023-03-13
iteration_start: 2023-02-27
layout: iterationreport
slug: "13"
---

In this iteration, PPA 3.9 was released, which includes a major improvement to search functionality so that similar works or reprints are clustered by default (the relevant functionality was tested and accepted the previous iteration). On the Lenape Timetree project, major design issues were accomplished for tag and leaf interactions. We also completed the first-pass implementation on the active leaf styles, hover interactions for corresponding leaf and labels, and url behavior that makes it possible to bookmark the tree with a specific leaf showing.  We also contributed to some small bugfixes and a major indexing speed improvement for the Geniza project — work that was previously left  in-progress, and benefited from a recent discovery made while working on PPA that made it possible to optimize the database queries used for bulk indexing (indexing all Geniza documents went from somewhere around 20-30 minutes to \~2 minutes.)

Our rolling development velocity is stable, at **7 points**, but this is due to the large number of points closed in the previous iteration when we completed the PPA search clustering functionality. We only completed **4 points** of development work in the current iteration. The design velocity is on an upward trend, with two very productive iterations in a row, reflecting the substantial amount of design progress on the Lenape Timetree project in recent weeks.

## Demos

{{< figure src="featured-lenape-active-leaf-style.png" caption="Screenshot of the Lenape Timetree showing active leaf style">}}







