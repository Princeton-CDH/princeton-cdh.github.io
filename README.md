# Dev/Design @ CDH

This repository is used for automated reporting on development work and for maintenance of dev/design documentation and reporting site for the Center for Digital Humanities at Princeton Development and Design Team.

## reporting

GitHub Actions are used to collect data on releases (via repository tags) and issues closed, with points and velocity (based on GitHub and ZenHub APIs). The data files created by these scripts are used for reporting in the Hugo site.

## hugo site

The dev/design site is generated with [Hugo](https://gohugo.io/) using the [Docsy](https://www.docsy.dev/) theme.

Because GitHub currently only supports publishing User and Organization sites from `master`, development on the site and scripts should be done on `develop`. The Hugo site is automatically compiled and published from the `develop` branch and published to `master`.

To add a new iteration report, create a new post under `content/blog/iteration-reports` with `layout: iterationreport` and configure an `iteration_start` date that matches the iteration start value in the iterations summary data file.


## setup

When checking out for local development, make sure you have
the docsy theme via git submodule:

```
git submodule update --init --recursive
```

Install npm dependencies:

```
npm install
``






