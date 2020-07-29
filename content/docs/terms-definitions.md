---
title: "Terms & Definitions"
---


<!-- note: may want to use headings and anchor links like  -->

Workflow
: In the context of a CDH project, a workflow is a combination of a particular task or function with the tools, approach, and best practices used to accomplish that task.

Workflows are documented in the early stages of a project’s charter process. They are usually based on a combination of the accumulated experience of the project’s current team with the accumulated experience of the CDH across all its other projects.

Workflows may originate from past templates and experience or may be created collaboratively by the Project Manager and Project Director. The Project Manager has the authority and obligation to periodically review the project’s workflows and assess what is working or needs improvement; workflows should be updated so that they are best serving the needs of the project team. The Technical Lead is available to consult on workflows, especially to offer lessons learned from the CDH’s experience with other projects.

Protocol
: Protocols are special workflows used to make decisions about project data - for example, how to attribute authorship to a document, or when to assess that two records are really describing the same item and should be merged.

Protocols usually take the form of a Google Doc stored in the project’s Shared Drive. They usually list out the steps to take when someone is working with the data and encounters a particular problem or situation. Protocols can be greatly enhanced by screenshots or screen-capture video that guides the reader in following the steps of the protocol.

Protocols are usually formed by the Project Manager and Project Director in tandem and circulated to anyone who works with the data so that they can refer to documentation when editing or encoding data. The Technical Lead may consult on protocols to offer advice on how to resolve tough decisions, or recommend software that could aid in tasks like deduplication or data enrichment. Protocols can be drafted by the Project Manager and circulated to the entire Project Team for comment before being stored in the Team Drive.

Proof of Concept
: In software development, a proof-of-concept is a small, incomplete implementation used to test whether an approach is feasible or has practical potential. It is used to prove that a concept is worth pursuing, and can be used as a basis for testing and refining the approach.

Working on a proof-of-concept is different from working on a project in its later stages. At this stage, there is less of a focus on durable solutions and more of a focus on tackling key questions. Work done on the proof-of-concept may form the basis of the next stage in the project development, or it may be discarded entirely. There may be multiple different proof-of-concepts or prototypes, depending on the questions that need to be answered. The project team may implement the proof-of-concept using tools or techniques they would not use for the “final”, production version, knowing that this work will ultimately not be used: the purpose is to build something functional enough to test the concept or approach.

To use an example, the project team might be considering using a new database software to store the project data because the Technical Lead identified it as a promising solution. The proof-of-concept will be built atop the new database software, including:
- translating the project’s data model into the language of the new database
- building a basic backend so team members can add project data to the database
- building a basic frontend that shows off the data in the database

For each of these tasks, the proof-of-concept will try to answer the questions - “could this work? if so, how?” The proof-of-concept will be tested by various constituencies to answer these questions, and the lessons learned incorporated in the next version of the project.

Prototype
: A prototype is an early version of a product that can be used to test a concept or process. A proof of concept is a prototype, but not all prototypes are proofs of concept. For example, a hand-drawn or printed paper prototype can be used for usability testing on a proposed interface. Similarly, a visual prototype conveying the look and feel of an interface without any functionality can be used for usability testing and demonstration purposes.

Alpha
: An alpha version of a product is an early functional prototype used for internal testing with the intent of refining and developing further. It might be incomplete, unstable, or have flaws.

Beta
: A beta version of a product is more mature than an alpha. It should have most of the expected functionality and be close to a complete product, although it may still be incomplete and have flaws. It can be used for testing and soliciting feedback either with a select group of people or with the general public, with the intent of refining for a release.

Backend / Frontend
: These two terms are used frequently in the software development industry to refer to different parts of an application or program, but are hard to define precisely. Most often, a project’s “frontend” means the part that “end users” will interact with; for a website, this is the general public. The “backend” can refer to parts of the product that only certain users will see (like an interface for editing the project database) but it can also refer to parts of the product that users won’t see at all (like code that runs on a server to generate a webpage).

At the CDH, we usually use “frontend” to refer to the public-facing parts of a project, like pages on a website focused at other researchers or the general public. We usually use “backend” to refer to parts of a project that store and operate on the project data, like a non-public administrative interface used by project team members.

Design Review
: Design review is a workflow where the Project Director and the Developers discuss the UX Designer’s designs, with the goal of reaching agreement and signing off on a single version that the Developers will implement.

A Github issue is first created to track the progress of a particular design, often corresponding to a single page or feature. The Designer uses design software (e.g. Figma) to create and publish designs, often creating multiple versions at once so that the project team has options to select from. When the design is ready for review, the Designer moves the Github issue to the “review/QA” ZenHub pipeline and asks for review from the Project Director and other team members.

Primary review is conducted by the Project Director, with the Developers and the PM also contributing to the discussion. Developers may comment on the feasibility of the design or possible implementations. All team members respond with their feedback and questions or concerns via GitHub comments on the issue so that the discussion is stored at a particular URL. Once agreement is reached, the issue is closed and moved to the “completed” ZenHub pipeline - it is ready to implement. If agreement is not reached the UX Designer works to determine what revisions are needed to be made and will address the issues. At this stage the UX Designer moves the issue back into the “in progress” ZenHub pipeline before re-delivering for design review.

Design Testing
: Design testing is a workflow where the UX Designer compares parts of the project to the design specifications to identify any inconsistencies or errors in the implementation. The goal is to have a usable and functioning version of the design that preserves the intentions of the designer.

Developers implement the design specified in a design tool or handoff tool (Figma, Zeplin). When the design is ready to be tested, it’s moved to the “review/QA” ZenHub pipeline. The tester visits the QA environment (usually a special non-public version of a project), compares the implementation with the designs specified in the tool, and leaves comments or questions based on their experience.

If the design implementation is deemed acceptable by the tester, the issue is closed and moved to the “completed” pipeline in ZenHub. If the tester has questions or something doesn’t look right, they respond to the issue with comments and a Developer will address the issue. Developers may move the issue back into the “in progress” ZenHub pipeline to make further changes before re-delivering for testing.

Acceptance Testing
: Acceptance testing is a workflow where the Project Manager (and potentially also the Project Director) review new functionality that has been deployed to a testing environment and determine if it is acceptable. The goal is to ensure that the version of the project that is deployed matches the vision of the project team.

Developers implement the feature described in a GitHub issue (often a user story) and add testing notes to the issue describing how to verify that it works as intended. When the issue is ready to be tested, it’s moved to the “review/QA” ZenHub pipeline. The tester visits the QA environment (usually a special non-public version of a project), follows the testing script written in the issue, and leaves comments or questions based on their experience.

If the feature works as intended and is deemed acceptable by the tester, the issue is closed and moved to the “completed” pipeline in ZenHub. If the tester has questions or something doesn’t look right, they respond to the issue with comments and a Developer will address the issue. Developers may move the issue back into the “in progress” ZenHub pipeline to make further changes before re-delivering for testing.

Code Review
: Code Review is a workflow where Developers submit code to be reviewed by other Developers. The goals are to catch potential bugs early in the process, and help Developers gain familiarity with each other’s independent work.

Developers implement the feature described in a GitHub issue (often a user story) with one or several changes in a new git branch. While code is being written, the issue is moved to the “in progress” pipeline in ZenHub. Eventually, the code is published to GitHub and a pull request (PR) is created so that other Developers can review the code before merging it into the main codebase. GitHub offers built-in functionality for requesting code reviews and for leaving review comments and assessments.

Reviewers can either accept the code for inclusion or request further changes. In some cases, a developer may submit code as a “draft” pull request to indicate that it is ready for review but shouldn’t be included in the codebase in its current state. If the code passes review, it is merged into the main codebase and the issue is moved into the “development complete” pipeline in ZenHub.

All of the terms below aim to enable the user to reach their goals within the context of project goals.

Web Accessibility
: It is the practice of making websites usable by as many people as possible regardless of their abilities or circumstances. It is addressed by ensuring that individuals with accessibility needs can also use the website and benefit from it. Examples of accessibility needs are various kinds of vision impairment and motor impairment, and may be temporary or permanent. Designing and developing with respect to accessibility principles usually also benefits other groups of users, such as those with slow network connections.

User Experience Design (UX)
: It is the umbrella term that encompasses the practices below. UX is a concept which refers to everything that affects the user’s experience with the software.

Information Architecture (IA)
: It entails organizing, structuring, and labeling information in the entire software in usable and systemic ways. It directly contributes to the creation of a sitemap (a diagram that shows a list of website pages often in a hierarchical manner), and a site flow diagram (shows how the pages of a website are connected and how users can navigate through information – uses the sitemap as its base).
It encompasses:
- organization schemes (how information is categorized and structured)
- labeling systems (how information is represented)
- navigation systems (how users browse and move through information)
- search systems (how users look for information)

User Interface Design (UI)
: It entails the visual organization of information through grids, spacing, font styles (i.e. font weight, size, and leading/line-height), button styles, colors, etc. Its primary goal is to make it easier for users to read, understand and process information. Many of its aspects affect accessibility and are therefore created with respect to accessibility requirements. This is different from Graphic Design, which focuses on the creation of visual work mainly for print media. (Not Graphic Design)

Interaction Design (IxD)
: It is the practice of designing with respect to the context within which users interact with the software. On a higher level it’s about the cycle of user’s actions and software’s responses to those actions, i.e a conversation between the two. Many of its aspects affect accessibility and are created with respect to accessibility requirements. IxD is an ongoing aspect throughout the course of a project, but it is even more focused on during the IA and UI processes.

It can be thought of as having five dimensions:
1.  words/language
2. visual representations, e.g. icons and typography
3. physical objects/space, e.g the device and the setting through which the user will interact with the software
4. time, e.g. the motion and/or sounds used as forms of feedback in the user’s interactions with the software, or designing with clear goals for the amount of time the user spends interacting with the software or each of its pieces.
5. behaviors, how the previous dimensions define the user-software interactions.

Visual Design
: It entails the creation of illustrations, icons, and other types of graphics for software. Its goals often include communicating to the user through visual storytelling as well as determining the brand/identity of the software. Some of its aspects affect accessibility and are therefore created with respect to accessibility requirements. This is different from Graphic Design, which focuses on the creation of visual work mainly for print media.  (Not Graphic Design)

User Experience Research (UX Research)
: It is about understanding the goals and scoping of projects, and how and if users’ needs and goals align with project goals. It is often conducted through interviews, observations, surveys, etc.
: Also known as “user research”

Usability Testing
: Its goal is to test with a representative user whether and how usable a design is;  tests may be conducted on a concept in the form of a sketch, prototype, or working software. It is conducted by observing representative users attempt to interact with the artifact (sketch, prototype, or software) and complete the tasks designed for them.

Note:
Many of the decisions in IA, UI, IxD, and Visual Design require UX research and/or usability testing, either to determine a direction or to confirm a solution. Usability testing is more often valuable, because showing participants an artifact brings up new questions and ideas rather than conversing only through questions.
Many of the decisions in the categories above depend on the data available, how it is structured, and Project Director research goals for the data.
Knowledge about the structure of data, the goals of the project and its data, as well as UX Research all help determine site flows/user flows.
Many of the terms above are interdependent.
“Experience Design” and “Interaction Design” are often applied beyond software-focused projects or human-machine interactions, and are often applied to human-human and machine-machine interactions.




