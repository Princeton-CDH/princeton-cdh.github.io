---
title: "Sep 13 - Sep 24, 2021"
date: 2021-09-27
iteration_start: 2021-09-06
layout: iterationreport
slug: "27"
---

This iteration, we continued working on planned maintenance work and finishing the charter for the next year of work on the Geniza research partnership.

## Derrida's Margins

We completed revisions on three of the four dataset exports, and corrected one bug in the previous version of the data exports and one bug in the IIIF image endpoint handling.

## Geniza

We finally completed the script to merge documents, and fixed a bug that made it into production when part of the incompletely tested merge code was included in the last release. We also made progress on design work towards visual identity and color selection.

## Shakespeare and Company

We successsfully completed the migration to PUL infrastructure without hiccups, including switching the 100 years twitter bot cron job over to the new server. This update includes upgrades to python 3.6, Solr 8, and a switch from MySQL to Postgresql. Most crucially, this gets the code off of python 3.5 which has not been supported for nearly a year. Looking foward, we know have a path for testing and updating the application to newer versions of python, since the infrastructure on the PUL VMs is fully managed by our ansible deploy scripts.












