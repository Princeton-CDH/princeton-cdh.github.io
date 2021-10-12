---
title: "Workflows"
---

## Communication

### Tools
Project teams communicate primarily over Slack, using a channel in the CDH @ Princeton workspace. Project team members can be added to the CDH slack as single-channel guests so that they don’t have additional noise from other CDH channels. The Project may also maintain its own Slack workspace separate from CDH.

### Workflow
These types of conversations normally happen on Slack.

- polling the team for advice on how to handle some part of the project data
- notifying the team that work is starting to implement a feature of the project
- checking whether an observed phenomenon is a bug
- reporting on what team members accomplished during the day
- asking team members to review or test a feature or design
- thanking and appreciating team members

These types of conversations normally require further documentation, such as email or google doc.

- notifying project team members of absence or vacation
- creating or modifying a project workflow
- forming an agenda for a meeting and circulating it for comment
- reviewing or testing a feature or design and leaving comments

### Best Practices

- customize your notifications settings so you aren’t bombarded by messages
- use “do not disturb” mode when you don’t wish to be notified
- use DMs for private conversations, including group DMs
- use threads to keep conversations together
- use tacos to show your appreciation for project team members
- set your status to show what you’re working on and if you’re available

## File Storage

### Tools
Files are stored in a Google Shared Drive. Adding files to any folder in the drive automatically makes them available to all users who are members of the drive.

### Workflow
These types of files are normally stored in Google Drive.

- meeting agendas (in a “meeting notes” folder)
- charter documentation (in a “charter planning notes & docs” folder)
- design files and assets (usually in a “design” folder)
- data work protocols and checklists (usually in a “data work” folder)
- written content and images to be used directly on a website
- written content and images to be distributed for publicity purposes
- old versions of any of the above (usually in an “archive” folder)

### Best Practices

- name files including a date, like “2020-06-30 design issues”, so they are findable
- use the search function to find documents you’re looking for more easily
- store files in the team drive rather than your personal drive
- use document headings so that the “document map” function works

## Meetings

### Tools
Meetings are conducted via Zoom. Meeting agendas are written as Google Docs and stored in the project’s Team Drive (see “File Storage” above).

### Workflow & Best Practices
Meeting norms for each project are established in documentation stored in the project's Google Drive.

## Project Management

### Tools
Project teams track tasks on an Asana board in the CDH @ Princeton workspace.

### Workflow
Asana tasks are used to track:

- action items identified in meetings
- preparation of agendas for meetings
- communications and publicity work
- editorial workflow for written website content or publicity materials
- software releases, via a release checklist managed by CDH Lead Developer
- data work (if helpful)

## Data Work

### Tools
The CDH usually customizes an interface for project team members to use to edit and update project data. This may take the form of a spreadsheet, or it may be an interface to a relational database.

### Workflow
Any members of the project team who are working with the data (sometimes called “encoders”) use the project’s protocols to encode the data.

### Best Practices
The best practices for working with project data are codified as protocols and stored in the project’s Google Drive.

## Development

### Tools
The project’s code is hosted on GitHub in a public repository under the [Princeton-CDH organization](https://github.com/princeton-cdh). GitHub offers a wide range of functionality related to the project’s code. The project also uses [ZenHub](https://app.zenhub.com/), which adds a layer of agile project management tooling on top of GitHub.

### Workflow
The project team splits development up into two-week “iterations”; at the end of each iteration the completed features from that iteration are released and become public. Each iteration begins with a planning meeting of the dev & design team at which the team also reflects on the previous iteration.

Individual features and tasks are tracked using GitHub issues. Often, issues are written in the form of agile “user stories” - for example, “As a content editor, I want to select featured essays to show on the site home page so I can provide pathways into the content for non-academic users.” Some issues may not take the form of user stories - they may document bugs discovered in the project, or “chores” (one-off tasks that are necessary to support other work).

The dev & design team estimates the relative complexity of features in “points” to get a rough idea of how much work can be accomplished in a single iteration. GitHub does not natively provide features to track these points, so ZenHub is used to organize issues in terms of points and iterations.

ZenHub organizes dev and design issues using kanban-style boards; as issues are worked on they move through a pipeline of different stages from development to review to testing:

- an issue starts in the “icebox”, a place for work that isn’t ready to start yet
- issues that are ready to be worked on in the current iteration are in the “backlog”
- developers claim (assign) issues in the backlog and move them to “in progress”
- when a feature’s code and any visual changes have been reviewed it goes to “development complete”
- when a feature is ready to be tested it is delivered with notes and moved to “QA”
- if the feature doesn’t pass testing it moves back to “in progress” for further work
- if it does pass testing, it is closed and automatically moved to “completed”

The Project Manager uses GitHub and ZenHub extensively to participate in testing of issues and to get a sense of what the dev & design team is actively working on and has completed. These tools offer a variety of reporting functions to get a better picture of how the team works together to author source code.

Developers submitting code that introduces visual or behavioral changes also participate in the visual review process. If automated software (Percy) detects that the code introduces desired visual changes, the UX designer reviews these changes. If the changes were unintentional, the developer revises the code to prevent introducing visual or behavioral regressions.

## UX Design

### Tools
CDH projects may use [Figma](https://www.figma.com/) to create and store designs and possibly also [Zeplin](https://zeplin.io/) for "handing off" designs to developers. The visual review process may use [Percy](https://percy.io). Design tasks are tracked on GitHub/ZenHub as issues, in a similar manner to features in development.

### Workflow
The UX Designer collaborates with the dev team in two-week “iterations”. At the end of each iteration, design tasks that are completed and have passed the review stage will be ready for implementation in the upcoming iteration. During iterations the UX Designer also focuses on designing/researching/testing for long-term design goals for the project (within the scope of the project grant cycle).

Design tasks are tracked using GitHub issues with the label “Design”. Often, design issues are written in the following form (focused on user goals and actions) - for example, “Design a way for the user to access all the essays that an issue contains so they can read them.” Other design issues include “Design chores”, which often entail updating the designs or some type of cleanup. Design chores are neither estimated nor reviewed. 

Each design issue is estimated for its relative complexity in “points” to get a rough idea of how much work can be accomplished in a single iteration. 

As design issues are worked on they move through a pipeline of different stages from design to review:

- a design issue starts in the “icebox”
- issues that are ready to be worked on in the current iteration are in the “backlog”
- once the UX Designer has started to work on an issue they move it from the backlog to “in progress”
- when a feature is ready to be reviewed it is delivered with notes and moved to “QA”
- if the design issue doesn’t pass the review the UX Designer works to identify and address what revisions it will need, - where it moves back to “in progress” for further work
- if it does pass the review, it is closed and automatically moved to “completed”.

The UX designer also participates in review of visual and behavioral changes introduced by developers. When a pull request is opened that introduced visual changes, the UX designer uses Percy to comment on the changes or request further work. This ensures that only code implementing desired visual changes is merged.
