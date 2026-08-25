# MFM v1.1-170 – Grants & Funding Module Implementation

Version: 1.1

Document ID: MFM-v1.1-170

Status: Technical Implementation

---

# 1. Purpose

The Grants & Funding Module manages the complete lifecycle of external funding opportunities within MaritimForeningsManager (MFM) v1.1.

The module supports the planning, application, administration and reporting of grants while ensuring that financial accounting remains exclusively within the Accounting Module.

The module is intended for non-profit organizations that depend on public grants, private foundations, sponsors and donations.

---

# 2. Responsibilities

The Grants & Funding Module manages:

- Funding Opportunities
- Grant Applications
- Sponsors
- Foundations
- Public Funding
- Award Decisions
- Funding Agreements
- Reporting Obligations
- Grant Documents
- Grant Status

The module does not perform financial bookkeeping.

---

# 3. Architectural Principles

The module follows these principles:

- One Grant Record
- One Grant Owner
- One Application History
- One Reporting History
- Multiple Project References
- Accounting remains the financial authority

Grant administration and accounting are separate responsibilities.

---

# 4. Module Architecture

```
Grant GUI

↓

Grant Controller

↓

Grant Service

↓

Grant Repository

↓

SQLite Database
```

All business rules are implemented in the Grant Service.

---

# 5. Core Entities

```
Grant

FundingProgramme

FundingOrganisation

GrantApplication

GrantAward

GrantAgreement

GrantReport

GrantMilestone

GrantContact

GrantDocument
```

Each entity has a single responsibility.

---

# 6. Grant Lifecycle

```
Opportunity Identified

↓

Planning

↓

Application

↓

Submitted

↓

Evaluation

↓

Approved / Rejected

↓

Agreement

↓

Active

↓

Reporting

↓

Completed

↓

Archived
```

Every state transition is recorded.

---

# 7. Funding Opportunity

Each funding opportunity contains:

```
Opportunity Number

Programme Name

Funding Organisation

Description

Funding Area

Opening Date

Closing Date

Maximum Grant

Website

Status

Notes
```

Funding opportunities may exist without an application.

---

# 8. Grant Application

Application information includes:

```
Application Number

Application Date

Requested Amount

Project

Applicant

Status

Responsible User

Summary

Attachments
```

Applications remain editable until submission.

---

# 9. Award Information

Award records include:

```
Award Number

Decision Date

Approved Amount

Funding Percentage

Conditions

Reporting Requirements

Payment Schedule

Reference Number
```

Award amounts are informational.

Financial postings are performed by Accounting.

---

# 10. Funding Organisations

The module stores information about:

- Government Agencies
- Municipalities
- Foundations
- Companies
- Sponsors
- Private Donors
- EU Programmes

Each organisation may provide multiple funding opportunities.

---

# 11. Agreements

Funding agreements include:

```
Agreement Number

Signing Date

Valid From

Valid To

Conditions

Termination Clause

Reporting Schedule
```

Signed agreements are archived as documents.

---

# 12. Reporting Obligations

Each grant may define:

- Interim Report
- Financial Report
- Final Report
- Progress Report
- Activity Report

Deadlines are monitored.

---

# 13. Grant Milestones

Milestones include:

```
Milestone

Description

Due Date

Completion Date

Status

Responsible Person
```

Milestones support compliance monitoring.

---

# 14. Contacts

Each funding organisation may contain:

- Contact Person
- Email
- Telephone
- Address
- Position
- Preferred Communication Method

Communication history is maintained.

---

# 15. Project Integration

One grant may support:

- One Project
- Multiple Projects

One project may receive funding from:

- Multiple Grants

Relationships are managed through references.

---

# 16. Accounting Integration

Accounting responsibilities include:

- Grant Income
- Grant Payments
- Project Expenses
- Financial Statements

The Grant Module never stores accounting balances.

Instead, it references accounting transactions when needed.

---

# 17. Document Integration

Documents linked to grants include:

- Applications
- Agreements
- Budgets
- Approval Letters
- Reports
- Correspondence
- Supporting Documentation

Physical files remain under Document Service ownership.

---

# 18. Reporting

Standard reports include:

- Active Grants
- Submitted Applications
- Awarded Grants
- Rejected Applications
- Funding by Organisation
- Reporting Deadlines
- Grant Portfolio
- Project Funding Overview

Reports are read-only.

---

# 19. Dashboard Integration

Dashboard widgets may include:

- Open Funding Opportunities
- Upcoming Deadlines
- Pending Reports
- Active Grants
- Recently Awarded Grants
- Funding Pipeline

Widgets display operational information only.

---

# 20. Search & Filtering

Search criteria include:

- Grant Number
- Programme
- Funding Organisation
- Status
- Project
- Date Range
- Responsible User
- Funding Type

Combined filtering is supported.

---

# 21. Security

Permissions include:

- View Grants
- Create Applications
- Edit Applications
- Submit Applications
- Register Awards
- Create Reports
- Archive Grants
- Export Data

Access is role-based.

---

# 22. Audit

The following actions are audited:

- Grant Created
- Application Submitted
- Award Registered
- Agreement Updated
- Report Submitted
- Status Changed
- Document Added
- Archive
- Restore

Audit history is immutable.

---

# 23. User Interface

Primary screens:

- Funding Opportunities
- Grant Overview
- Application Details
- Award Details
- Reporting
- Funding Organisations
- Contacts
- Documents

Secondary dialogs:

- New Opportunity
- New Application
- Register Award
- Add Reporting Deadline
- Close Grant

The interface follows the common MFM GUI framework.

---

# 24. Validation Rules

Examples:

- Grant Number must be unique.
- Closing Date must be after Opening Date.
- Requested Amount must be positive.
- Approved Amount cannot exceed programme limits unless overridden.
- Reporting Deadlines must be chronological.
- Funding Organisation must exist.

Validation occurs in the Service Layer.

---

# 25. Future Enhancements

Future versions may support:

- Online Grant Portals
- Automatic Deadline Reminders
- AI-assisted Funding Opportunity Matching
- Electronic Application Submission
- Digital Signature Support
- Integration with National Grant Portals
- Grant Performance Analytics

These enhancements shall remain compatible with the established architecture.

---

# 26. Governance

The Grants & Funding Module is responsible for administrative management of funding activities.

It shall never replace:

- Accounting
- Project Management
- Document Management

Instead, it coordinates information between these modules through the Service Layer while maintaining clear ownership of grant-related business data.

---

# 27. Summary

The Grants & Funding Module provides comprehensive administration of funding opportunities, grant applications, awards, agreements and reporting obligations.

It integrates seamlessly with the Project, Accounting, Document and Reporting modules while preserving the MFM architectural principle that financial transactions remain exclusively within the Accounting Module.

The module enables non-profit organisations to manage complex funding activities in a structured, auditable and maintainable manner.

---

# Next Document

**MFM v1.1-180 – Document & Archive Module Implementation**

---

# END OF DOCUMENT