---
title: "User Stories"
---

## User stories should:

- describe something a particular kind of user (as recognizable to the software) can do in the application and why
- describe features at a granular level (e.g., could be implemented in a day or less)
- be something technical and non-technical team members can understand and agree on
- not be too specific about implementation details (leave room for developers to make technical decisions)
- provide user motivation or value for the feature (may influence development choices)
- should be testable (when a developer completes a feature and delivers it for testing, the project team member will test that feature to see if it works as expected)

## User story template:

> As a user (**WHO** - specify type of user within the system if appropriate), I want to do X (**WHAT** - feature or functionality) so that Y (**WHY** - rationale or motivation).

Users in this context are intended to be users as the software can recognize them - e.g., anonymous user vs. logged in user, admin vs. blog editor or content editor.  Unless otherwise specified, it will generally be assumed that users with more permissions can do everything an anonymous or generic user can do.  If there are multiple types of users in a system, the terminology should be agreed upon and defined.

User scenarios or case studies referencing particular kinds of personas (researchers, students, general public, etc) are valuable and may well feed into development user stories, but they generally provide a different level of specificity than what is needed for development work.

## Administrative User Stories

Describing administrative functionality is just as important as public-facing user functionality.  Articulating administrative needs will help the development team to build something that is more efficient and easy to use.

Some features may have two related stories - the public facing story and the admin functionality that supports it.  For example:
- As a user, I want to read blog posts so I can keep up to date on project news.
- As a blog editor, I want to create and update blog posts so I can post news for users.

### Types of admin users

It may be useful to articulate groups of admin users based on what they need to do with the data and what permissions they should have.  For example, a content site could have:
- Blog authors, who can contribute blog posts but not edit other content
- Content editors, who can manage blog posts and other site content
- Admins, who can manage blog posts, content, users, etc.

In an admin site for managing data, we might have something like a data entry user or data curator.

Any custom admin user terms should be defined so that everyone reading the user stories understands which kinds of users are meant.

The development team can help create and set permissions for admin user groups when implementing the admin interface.

### Django Admin interface

Django comes with an easy-to customize admin interface for database content.  The development team may be able to make suggestions based on our understanding of the database, but knowing what you need to accomplish will help.  Here are some features to keep in mind when thinking through admin needs:
- What fields or data should display when listing all data for a particular kind of item (e.g. book or person)
- What fields should be searchable by default in the admin interface?
- What fields would be useful for filtering a list of items?
- When editing items, should related items be grouped or displayed together?
- Do any fields need a special lookup from a different system? (e.g., VIAF or Geonames)
- Would it be useful to have some fields editable on the item list view for batch editing?

* * * 

For a critical discussion of user stories, see [Best Practices?](https://cdh.princeton.edu/updates/2019/07/29/best-practices/) by Rebecca Sutton Koeser and [“Meta!Meta!Meta! A Speculative Design Brief for the Digital Humanities” by Anne Burdick](http://visiblelanguagejournal.com/issue/172).