# MFM v1.2-330 – Advanced Project, Resource & Maintenance Management

Version: 1.2

Document ID: MFM-v1.2-330

Status: Functional Expansion

---

# 1. Purpose

This document defines the Advanced Project, Resource & Maintenance Management capabilities introduced in MaritimForeningsManager (MFM) v1.2.

The purpose is to transform the Project Module from a traditional project register into a complete planning environment capable of managing restoration projects, maintenance activities, volunteers, resources, vessels, facilities and organizational work.

The module remains a planning and operational management module.

Financial transactions remain exclusively within the Accounting Core.

---

# 2. Objectives

The module expansion introduces:

- Advanced Project Planning
- Work Breakdown Structures (WBS)
- Task Management
- Resource Planning
- Volunteer Assignment
- Equipment Planning
- Vessel Maintenance
- Preventive Maintenance
- Risk Management
- Project Analytics

---

# 3. Architectural Principles

The Project Module owns:

- Projects
- Tasks
- Milestones
- Resources
- Maintenance Plans
- Risk Registers
- Schedules

The Project Module never owns:

- Accounting Transactions
- Payments
- Financial Ledger
- Bank Information

Actual costs always originate from the Accounting Core.

---

# 4. Expanded Project Architecture

```
Project

↓

Work Packages

↓

Tasks

↓

Resources

↓

Schedule

↓

Progress

↓

Reports
```

Each layer is independently manageable.

---

# 5. Project Lifecycle

```
Idea

↓

Proposal

↓

Planning

↓

Approved

↓

Active

↓

Completed

↓

Archived
```

Every state transition is audited.

---

# 6. Work Breakdown Structure (WBS)

Projects may be divided into:

```
Project

↓

Phase

↓

Work Package

↓

Task

↓

Subtask
```

Unlimited hierarchy depth is supported where practical.

---

# 7. Task Management

Each task contains:

- Task ID
- Title
- Description
- Responsible Person
- Priority
- Status
- Planned Start
- Planned Finish
- Actual Start
- Actual Finish
- Dependencies

Tasks support detailed operational planning.

---

# 8. Task Status

Supported statuses:

- Planned
- Ready
- In Progress
- Waiting
- Blocked
- Completed
- Cancelled

Status changes generate audit events.

---

# 9. Resource Management

Resources include:

- Volunteers
- Employees (future)
- Contractors
- Equipment
- Facilities
- Boats
- Vehicles

Resources may participate in multiple projects.

---

# 10. Volunteer Assignment

Volunteer assignments include:

- Assigned Project
- Assigned Task
- Role
- Availability
- Hours Planned
- Hours Performed
- Comments

Volunteer information is synchronized with the Membership Module.

---

# 11. Equipment Register

Equipment examples:

- Power Tools
- Safety Equipment
- Workshop Equipment
- Navigation Equipment
- Lifting Equipment
- Museum Equipment

Equipment records include maintenance schedules.

---

# 12. Vessel Maintenance

The module supports maintenance planning for vessels.

Maintenance categories:

- Hull
- Deck
- Engine
- Electrical
- Rigging
- Interior
- Safety Equipment
- Navigation Equipment

Maintenance history is permanently retained.

---

# 13. Preventive Maintenance

Maintenance intervals may be based upon:

- Calendar
- Running Hours
- Operating Seasons
- Inspection Results

Preventive maintenance reduces unexpected failures.

---

# 14. Maintenance Work Orders

Each work order includes:

- Work Order Number
- Asset
- Description
- Priority
- Assigned Personnel
- Planned Date
- Completion Date
- Related Documents

Financial costs originate from Accounting.

---

# 15. Risk Management

Each project maintains a risk register.

Each risk records:

- Description
- Probability
- Impact
- Mitigation
- Responsible Person
- Status

Risk assessments support project planning.

---

# 16. Dependencies

Task relationships include:

- Finish-to-Start
- Start-to-Start
- Finish-to-Finish
- Milestone Dependencies

Dependency validation prevents scheduling conflicts.

---

# 17. Project Dashboard

New dashboard widgets include:

- Active Projects
- Delayed Tasks
- Upcoming Milestones
- Maintenance Due
- Volunteer Availability
- Equipment Utilization
- High Risks

Dashboard information is refreshed dynamically.

---

# 18. Project Calendar

Calendar views support:

- Daily
- Weekly
- Monthly
- Timeline
- Gantt View (future)

Calendar integrates with milestones and maintenance plans.

---

# 19. Resource Utilization

Resource analysis includes:

- Assignment Load
- Availability
- Planned Hours
- Completed Hours
- Equipment Usage
- Maintenance Conflicts

Utilization assists operational planning.

---

# 20. Project Reporting

New reports include:

- Project Status Report
- Task Progress Report
- Maintenance Overview
- Volunteer Allocation
- Equipment Usage
- Risk Register
- Milestone Progress
- Resource Forecast

Financial reporting continues to use Accounting data.

---

# 21. Security

Permissions include:

- Create Projects
- Modify Projects
- Assign Resources
- Schedule Maintenance
- Close Projects
- Archive Projects
- Export Reports

Project permissions remain role-based.

---

# 22. Audit

The following actions are audited:

- Project Created
- Task Created
- Task Completed
- Resource Assigned
- Maintenance Planned
- Maintenance Completed
- Risk Updated
- Project Archived

Audit records remain immutable.

---

# 23. Integration

The Project Module integrates with:

### Membership

Volunteer assignments

Skills

Availability

### Accounting

Budget monitoring

Actual expenditures

Financial summaries

### Documents

Technical drawings

Maintenance manuals

Photographs

Inspection reports

### Reporting

Project KPIs

Maintenance statistics

Resource utilization

The Project Module remains the owner of planning information only.

---

# 24. Future Enhancements

Future releases may support:

- Interactive Gantt Charts
- Critical Path Analysis
- Mobile Maintenance App
- QR-coded Equipment Tracking
- GIS Asset Mapping
- Predictive Maintenance
- IoT Sensor Integration
- AI-assisted Scheduling

These enhancements preserve the planning-focused architecture established in this document.

---

# 25. Governance

Projects remain operational planning entities.

The module shall never:

- Create accounting transactions
- Register payments
- Modify member records
- Store duplicate documents

All integrations occur through the established Service Layer.

---

# 26. Summary

The Advanced Project, Resource & Maintenance Management expansion significantly extends the operational capabilities of MFM by introducing structured project planning, preventive maintenance, resource management and risk control.

The architecture is particularly suited to maritime heritage organizations managing vessel restoration, museum operations, volunteer activities and long-term preservation projects while preserving the fundamental MFM principle that operational planning and financial accounting remain separate but tightly integrated.

---

# Next Document

**MFM v1.2-340 – Advanced Grant, Fundraising & Sponsorship Management**

---

# END OF DOCUMENT