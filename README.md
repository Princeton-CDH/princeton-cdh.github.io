# Dev/Design @ CDH

This repository is used for automated reporting on development work and for maintenance of dev/design documentation and reporting site for the Center for Digital Humanities at Princeton Development and Design Team.

[![github pages](https://github.com/Princeton-CDH/princeton-cdh.github.io/workflows/github%20pages/badge.svg)](https://princeton-cdh.github.io/)

## reporting

GitHub Actions are used to collect data on releases (via repository tags) and issues closed, with points and velocity (based on GitHub and ZenHub APIs). The data files created by these scripts are used for reporting in the Hugo site.

## hugo site

The dev/design site is generated with [Hugo](https://gohugo.io/) using the [Docsy](https://www.docsy.dev/) theme. The Hugo site is automatically compiled from the `main` branch and published to `gh-pages`.

## setup

When checking out for local development, make sure you have
the docsy theme via git submodule:

```
git submodule update --init --recursive
```

Install npm dependencies:

```
npm install
```

## Creating iteration reports

Update iteration definitions as needed in `iterations.json` if you need to add the dates for the next iteration (although these will likely be populated ahead of time now that we are using that data file for quarterly development shcedule). 

Pull the latest changes from GitHub to get data added by the issue collection and iteration summary GitHub Action scripts, which run on Saturdays.

Create a new iteration report using the iteration report page bundle archetype with the filename for the post you want to create. By convention, use isodates for iteration reports. To autogenerate for the current date, use this command:

```
hugo new --kind iteration-report blog/iteration-reports/`date +'%Y-%m-%d'`
```

The iteration report archetype assumes it is run on the first day of the new iteration; previous iteration start is calculated accordingly, and should be edited when necessary. Make sure the `iteration_start` date matches the iteration start value in the iterations summary data file.

Edit the new post to add content and any demo or featured content, then commit and push to GitHub to publish.


## Creating quarterly dev schedule

Create a new post with layout *quarterlyschedule* and configure
date range start and end in page parameters.

Edit `iterations.json` data file to add the dates for all iterations during the time period you want to cover.

For each iteration, add:
- projects: the list of projects projected to be active that iteration
- partial: optional, list of projects that are in planning or wrap up phases
- notes: optional; dictionary with list of notes per project for display in the schedule; when two notes are displayed, the second will be displayed 
the second week of the iteration

Be sure to add project colors and partial colors to `_quarterly_schedule.scss` when you add new projects to the schedule.