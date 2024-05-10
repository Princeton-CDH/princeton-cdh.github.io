---
title: "Oct 31 - Nov 11, 2022"
date: 2022-11-14
iteration_start: 2022-10-31
layout: iterationreport
slug: "14"
---

The points completed in the last iteration are low due to staffing
and the fact that our work has been focused on migrations and bug fixes.
Our rolling velocity is **7.3**, but that may be artificially inflated
by the high point total three iterations ago when we were closing out
the official charter period for the Geniza project.

## PPA

We've made substantial progress on the PPA migration, as evidenced by the
number of closed issues. We've figured out and resolved several problems,
so now it's just a matter of getting everything setup on the new production
server.  We're hopeful that we'll be able to complete the migration this iteration.

## Geniza

We released a hotfix (version 4.10.1) because we discovered a high priority
bug that needed to be corrected quickly. The script that runs as a cron job to
export annotations and transcription content to GitHub for a versioned backup
was broken by a scenario we didn't consider or encounter in testing: deleting
an annotation and then deleting (in this case via merge) the document it belonged to.
We were able to resolve this, along with a fix for a sorting regression in v4.10.
We're continuing to make progress on the data export work for dataset publication,
and supporting the project under the CDH warranty.










