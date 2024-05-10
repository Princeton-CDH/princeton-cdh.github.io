---
title: "Aug 23 - Sep 3, 2021"
date: 2021-09-07
iteration_start: 2021-08-23
layout: iterationreport
slug: "07"
---

Completed points for this iteration are quite low (only **2 points**). This brings our rolling velocity down to **6**, which is the lowest it's been in quite some time. This is likely due to the focus on maintenance work and chartering the next year of the Princeton Geniza Project; we also have some in-progress work on revised data exports for Derrida's Margins that have not been completed.

## CDH web

We released version 3.4 with the enhancements as planned in the charter, most notably a new site search. One new feature was completed this iteration, revising the home page to call attention to important information (about CDH and consults). We also fixed a small bug impacting the staff and executive committee pages.

## Geniza

We released version 0.5 with high priority fixes and improvements that had been identified by the project team to help with ongoing data work. In progress work on a script to merge documents, which has been through multiple rounds of testing, was temporarily put in the ice box to prioritize work on the Geniza charter for the next year. We did also start work more seriously on frontend development and inftrastructure and visual design.

## Derrida

Maintenance work is ongoing; we successfully set up continuous integration on GitHub Actions, to aid us in testing the remaining development (since Travis-CI is no longer reliable). We made progress on the data export scripts, but none of the issues were completed.

## Shakespeare and Company Project

We made progress on maintenance work to migrate the application from the current host into PUL infrastructure, which includes a python version upgrade, new version of Solr, and switch from MySQL to Postgresql. The site is successfully running in the new QA environment, so after a bit more testing to confirm functionality and migrated data, we should be able to proceed and schedule a production migration.

## Demos

{{< figure src="featured-cdhweb-homepage.png" caption="Screenshot of the CDH home page showing the newly implemented design featuring the About page and Consultations">}}









