---
title: "March 15, 2021"
date: 2021-03-15
iteration_start: 2021-03-01
layout: iterationreport
---

Rolling velocity for this iteration increased from about 10 points to about 15 points, largely due to a substantial chunk of CDH website user stories that completed the testing process together after multiple iterations.

## CDH Website
This iteration we completed testing on a large set of issues that have been rolling over through multiple iterations, including major changes to:
- Events
- People & Profiles
- Project, Grants, and Grant Memberships

Work is still in progress on content management updates for Blog Posts, the last major module to migrate as part of the v3.0 update.

## Princeton Geniza Project
This iteration we completed the admin management interface for Documents, the primary model in the Geniza database. In addition, we added new functionality to track where and how often languages & scripts are used by Documents, including provision for probable or uncertain language identification.

To support upcoming functionality for de-merging composite documents, we added an option to "clone" Documents with a record of the process stored in the database. We also experimented with clustering tags assigned to documents in order to start finding patterns in the data.

On the design side, we completed revisions to the sitemap diagram and created a low-fidelity mockup of the public view for Documents to spark discussion on content structure and hierarchy.

Four user stories related to the interface and data import process for Fragments are still in-progress.

## Demos
{{< figure src="featured-geniza-tagnetwork-detail.png" caption="Visualization of tag network generated from Geniza document tags">}}
{{< figure src="geniza-document-admin.png" caption="Screenshot of administrative interface for Geniza document database">}}
