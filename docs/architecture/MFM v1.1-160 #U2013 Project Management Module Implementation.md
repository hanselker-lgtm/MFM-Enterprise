# MFM v1.1-160 – Project Management Module Implementation

Version: 1.1

Document ID: MFM-v1.1-160

Status: Technical Implementation

---

# 1. Purpose

The Project Management Module provides structured planning, execution and follow-up of projects within MaritimForeningsManager (MFM) v1.1.

The module supports both small operational activities and larger multi-year initiatives undertaken by a non-profit association.

Projects serve as organizational and reporting entities.

They are **not** financial ledgers.

Financial transactions remain exclusively within the Accounting Module.

---

# 2. Responsibilities

The Project Management Module manages:

- Projects
- Activities
- Milestones
- Tasks
- Budgets (Planning)
- Resources
- Participants
- Project Documents
- Project Status
- Progress Reporting

---

# 3. Architectural Principles

The module follows these principles:

- One project owner
- One project manager
- One project record
- One planning budget
- Multiple accounting references
- Complete auditability

Project planning and financial accounting remain separated.

---

# 4. Module Architecture

```
Project GUI

↓

Project Controller

↓

Project Service

↓

Project Repository

↓

SQLite Database
```

Business rules reside exclusively in the Project Service.

---

# 5. Core Entities

```
Project

ProjectCategory

ProjectStatus

ProjectMilestone

ProjectTask

ProjectParticipant

ProjectBudget

ProjectRisk

ProjectDocument

ProjectActivity
```

Each entity has a clearly defined purpose.

---

# 6. Project Lifecycle

```
Idea

↓

Proposal

↓

Approved

↓

Planning

↓

Active

↓

Completed

↓

Archived
```

Archived projects remain searchable.

---

# 7. Project Record

Every project contains:

```
Project Number

Project Name

Short Description

Detailed Description

Category

Status

Start Date

End Date

Project Manager

Responsible Board Member

Priority

Notes
```

Project numbers are automatically assigned.

---

# 8. Project Categories

Examples:

- Vessel Restoration
- Museum Activities
- Educational Activities
- Public Events
- Maintenance
- Administration
- Research
- Heritage Preservation

Categories are configurable.

---

# 9. Project Status

Supported status values:

- Proposed
- Approved
- Planning
- Active
- On Hold
- Completed
- Cancelled
- Archived

Status changes are recorded automatically.

---

# 10. Project Budget

The Project Budget represents the planned financial framework.

It contains:

```
Expected Income

Expected Expenses

Expected Grants

Expected Donations

Expected Own Contribution

Budget Notes
```

The budget is used for planning only.

Actual financial figures originate from the Accounting Module.

---

# 11. Milestones

Each milestone includes:

```
Title

Description

Responsible Person

Due Date

Completion Date

Status

Comments
```

Milestones support progress monitoring.

---

# 12. Project Tasks

Tasks contain:

```
Task Number

Title

Description

Assigned User

Priority

Start Date

Due Date

Status

Estimated Hours

Actual Hours
```

Tasks are independent of accounting activities.

---

# 13. Participants

Participants may include:

- Board Members
- Volunteers
- Members
- External Partners
- Contractors

Participant roles are configurable.

---

# 14. Risk Register

Projects may contain identified risks.

Each risk includes:

```
Description

Probability

Impact

Risk Level

Mitigation Plan

Responsible Person

Status
```

Risk management supports project governance.

---

# 15. Resource Planning

Projects may allocate:

- Volunteers
- Equipment
- Meeting Rooms
- Vessels
- Vehicles
- Materials

Resource planning is informational.

---

# 16. Timeline

Projects provide a visual timeline showing:

- Start Date
- Milestones
- Deadlines
- Completion Date

Future versions may include Gantt chart visualization.

---

# 17. Document Integration

Projects may reference:

- Applications
- Drawings
- Contracts
- Meeting Minutes
- Technical Reports
- Photographs
- Permits

Documents remain managed by the Document Service.

---

# 18. Accounting Integration

Projects may be referenced by accounting entries.

Examples:

```
Expense Voucher

↓

Project Reference

↓

Accounting Ledger
```

The Project Module does not calculate financial balances.

Financial reporting is obtained from the Accounting Module.

---

# 19. Grant Integration

Projects may be linked to:

- Funding Opportunities
- Grant Applications
- Award Decisions
- Grant Reports

One project may receive funding from multiple grants.

One grant may support multiple projects where permitted by funding conditions.

---

# 20. Reporting

Standard reports include:

- Active Projects
- Completed Projects
- Milestone Status
- Budget Overview
- Progress Report
- Resource Allocation
- Risk Register
- Grant Connections

Reports are generated from current project data.

---

# 21. Search & Filtering

Projects may be searched by:

- Project Number
- Name
- Category
- Status
- Manager
- Date Range
- Grant
- Participant

Combined filters are supported.

---

# 22. Security

Permissions include:

- View Projects
- Create Projects
- Edit Projects
- Archive Projects
- Manage Milestones
- Manage Tasks
- Export Projects

Project Managers have delegated authority within assigned projects.

---

# 23. Audit

The following actions are audited:

- Project Created
- Project Updated
- Status Changed
- Budget Updated
- Milestone Added
- Task Assigned
- Participant Added
- Archive
- Restore

Audit history is immutable.

---

# 24. User Interface

Primary screens:

- Project Overview
- Project Details
- Timeline
- Milestones
- Tasks
- Budget
- Risks
- Participants
- Documents

Secondary dialogs:

- New Project
- New Milestone
- New Task
- Assign Participant
- Close Project

The interface follows the standard MFM GUI framework.

---

# 25. Validation Rules

Examples:

- Project Number must be unique.
- End Date cannot precede Start Date.
- Project Manager must exist.
- Category must exist.
- Status transitions must follow defined workflow.
- Budget values cannot be negative unless explicitly permitted.

Business validation occurs in the Service Layer.

---

# 26. Future Enhancements

Future releases may support:

- Gantt Charts
- Kanban Boards
- Resource Calendars
- Dependency Management
- Critical Path Analysis
- Volunteer Scheduling
- Mobile Project Dashboard
- GIS/Location Support

These enhancements shall remain compatible with the existing Project Service architecture.

---

# 27. Summary

The Project Management Module provides structured planning and execution support for projects undertaken by the association.

It manages project information, milestones, tasks, participants, planning budgets and risks while integrating seamlessly with the Accounting, Grant, Document and Reporting modules.

The architecture preserves the fundamental MFM principle that project planning and operational management remain separate from financial bookkeeping, ensuring a clear separation of responsibilities and a single authoritative financial ledger.

---

# Next Document

**MFM v1.1-170 – Grants & Funding Module Implementation**

---

# END OF DOCUMENT