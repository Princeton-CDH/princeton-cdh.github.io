# Dev/Design @ CDH

This repository is used for automated reporting on development work and for maintenance of dev/design documentation and reporting site for the Center for Digital Humanities at Princeton Development and Design Team.

[![github pages](https://github.com/Princeton-CDH/princeton-cdh.github.io/workflows/github%20pages/badge.svg)](https://princeton-cdh.github.io/)

## reporting

GitHub Actions are used to collect data on releases (via repository tags) and issues closed, with points and velocity (based on GitHub and ZenHub APIs). The data files created by these scripts are used for reporting in the Hugo site.

## hugo site

The dev/design site is generated with [Hugo](https://gohugo.io/) using the [Docsy](https://www.docsy.dev/) theme.

Because GitHub currently only supports publishing User and Organization sites from `master`, development on the site and scripts should be done on `develop`. The Hugo site is automatically compiled and published from the `develop` branch and published to `master`.


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

And run locally:

```
hugo server -D
```

## Creating iteration reports

First, edit the iteration definition file `iterations.json` to add the dates for the next iteration. Push the change to github to trigger the iteration summary GitHub Action to run.

Then create a new iteration report using the iteration report page bundle archetype with the filename for the post you want to create. By convention, use isodates for iteration reports. To autogenerate for the current date, use this command:

```
hugo new --kind iteration-report blog/iteration-reports/`date +'%Y-%m-%d'`
```

The iteration report archetype assumes it is run on the first day of the new iteration; previous iteration start is calculated accordingly, and should be edited when necessary. Make sure the `iteration_start` date matches the iteration start value in the iterations summary data file.

Edit the new post to add content and any demo or featured content, then commit and push to GitHub to publish.


