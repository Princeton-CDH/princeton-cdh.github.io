---
title: "Oct 4 - Oct 15, 2022"
date: 2022-10-18
iteration_start: 2022-10-03
layout: iterationreport
slug: "18"
---

Another high point iteration, as we made the final push to finish work
for the CDH/Geniza Research Partnership. For development, we closed **18 points** across 31 issues, resulting in a rolling velocity of **18.67** (_exactly_ the same as last iteration). 
Design also had a big push, closing **14 points** across 9 issues. 

## Geniza

We released v4.9 of Princeton Geniza Project mid-iteration. This was a major update
which included the long-awaited transcription migration from TEI to the new W3C 
annotation format, and rolled out the new transcription editor tool, annotorious-tahqiq. This includes full functionality needed to add, edit, and delete transcriptions 
with support for right-to-left text, as well as a new automated backup that 
synchronizes transcription content to a GitHub repository, with co-author commits
to track contributions. As part of this release, we also loaded a number
of new images from Bodleian and JRL collections. After the release went out,
we started tackling bugs with the editor not found in testing and finishing
the remaining committed functionality for the CDH/PGP charter, prioritizing
search improvements for sunsetting PGPv3 and CSV exports for data publication,
with a smaller amount of effort going to localization functionality.

## Lenape Timetree

We made significant progress on sitemap and wireframe designs for this project,
making a big push to get things ready for development while design is paused 
for a month.

## Demos

* [PGP transcription export](https://github.com/princetongenizalab/pgp-text) — browse the transcription content synchronized from the application, in annotation format and compiled into html and text 

{{< figure src="featured_pgp_transcription_editor.png" caption="Screenshot of transcription editor on the Princeton Geniza Project site">}}

{{< figure src="https://user-images.githubusercontent.com/7234006/194160646-e55abbcb-ef27-4482-b204-c19536d28091.gif" caption="Screen capture showing transcription with tahqiq">}}









