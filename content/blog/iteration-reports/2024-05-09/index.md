---
title: "Apr 29 - May 8, 2024"
date: 2024-05-09
iteration_start: 2024-04-29
layout: iterationreport
hideDesignVelocity: true  # control visibility of design chart
slug: "09"
---

This marked the second iteration of the new RSE team cycle, with a 8 day development sprint, followed by 2 days of R&D. The RSE team was focused on the PPA, as well as wrapping up some maintenance issues that carried over from last sprint. 

### Releases

The team wrapped up two major releases this week. We started the iteration with the release of the Wagtail upgrade for CDH web ahead of the technical phase of the website redesign. And we closed the iteration with the release of version 1.6 and 1.6.1 of Shakespeare and Company, which closed out a cluster of issues around improving data imports and exports.

The Springload redesign is moving forward with the implementation of the website redesign: https://github.com/springload/cdh-web/ 

#### PPA

For the main PPA application, the focus this iteration was on the integration with EEBO and addressing the shift in Gale's approach to serving images. Both are underway and moving forward smoothly.  

For the NLP project, worked continued on assessing and preparing the corpus for analysis, as well as initial planning for the creating of annotations. Laure completed the evaluation of the existing OCR, with a recommendation to re-OCR the text from Gale. The resulting data on detected languages also proved useful as a way to filter pages and to identify where the OCR error rate is likely high. 

### Aerial Archival Photography

We continue to make progress with assessing the work completed by Microsoft. We have a copy of the package developed for Prof. Kreike's data. Next iteration we will have a call with the Microsoft to clarify any questions / procedures and attempt to run the package on Princeton hardware.

### Maintenace Projects

We continue to support and consult on the Geniza project, particularly around issues of search and solr. 

The bug with Ansible Tower was addressed by PUL, which clears the way to set up the deploy of our major web applications (CDH Web, Geniza, S&Co) through this interface. This will improve our workflow for collaborating with external partners and contractors.

The issues with timeouts continues, and PUL has added datadog to the production applications so that we can get better visibility on what is happening. 

And in preparation for next week, the VMs for the Derrida Archive are ready to go.

### Writing

The long-awaited article-proofs arrived for the Shakespeare and Company cluster, which Rebecca was able to review, as well as finalize the corresponding replication code. In addition, she submitted the "Trust Your Code" article for publication; and submitted to the DH Mini Conference on Simulating Risk.

### Upcoming Priorities

Looking ahead, we will be focused next on completing the archive of Derrida's Margins (ahead of the server being shut down), interfacing with Microsoft regarding their object detection pipeline, completing the itegration with EEBO data on PPA, and determining the work plan for identifying poems in the PPA data. We are also ramping up our preparations for the London RSE site visits and the DARIAH conference.

## Demos

Interactive figures for the Shakespeare and Company article: https://viz.shakespeareandco.princeton.edu/
