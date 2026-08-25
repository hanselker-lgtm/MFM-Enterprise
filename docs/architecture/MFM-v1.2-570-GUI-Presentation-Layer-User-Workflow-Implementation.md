# MFM v1.2-570 – GUI, Presentation Layer & User Workflow Implementation

Version: 1.2

Document ID: MFM-v1.2-570

Status: Implementation Execution Baseline

---

# 1. Purpose

This document defines the implementation baseline for the MFM graphical user interface, presentation layer and user workflow execution.

It follows:

- MFM v1.2-500 – Architecture Consolidation & Implementation Readiness
- MFM v1.2-510 – Implementation Backlog, Work Packages & Traceability
- MFM v1.2-520 – Implementation Execution, Coding Standards & Development Workflow
- MFM v1.2-530 – Database Implementation, Schema Evolution & Migration Execution
- MFM v1.2-540 – Security Hardening, Secrets Management & Access Control Execution
- MFM v1.2-550 – Core Services & Domain Logic Implementation
- MFM v1.2-560 – Repository, Persistence Services & Data Access Implementation

The purpose is to define how MFM presents business capabilities to users without moving business rules into the GUI.

The document establishes:

- Presentation Architecture
- Screen Structure
- Navigation
- User Workflows
- Forms
- Validation
- Authorization Presentation
- Error Handling
- Tables and Lists
- Search
- Dialogs
- Notifications
- Dashboard Presentation
- Reporting Interaction
- Accessibility
- User Feedback
- Unsaved Changes
- Concurrency
- Testing
- GUI Security
- Usability
- Implementation Standards

---

# 2. Scope

This document covers the MFM desktop presentation layer for:

- Authentication
- Dashboard
- Membership
- Accounting
- Projects
- Grants
- Documents
- Reporting
- Administration
- Backup and Maintenance
- Notifications
- Search
- System Status

The exact screen names may follow the existing MFM source tree.

---

# 3. Presentation Architectural Position

The presentation layer is responsible for:

- Display
- Input
- Navigation
- User Interaction
- Form State
- User Feedback
- Formatting

It is not responsible for authoritative business rules.

The standard flow is:

```text
User

↓

GUI

↓

Application Service

↓

Domain Logic

↓

Repository

↓

Database
```

---

# 4. GUI Responsibility Rule

The GUI may:

- Validate Obvious Input
- Display Allowed Actions
- Collect User Input
- Display Results
- Display Errors
- Request Confirmation

The GUI must not:

- Post Accounting Entries Directly
- Execute Business SQL
- Decide Financial Rules
- Bypass Authorization
- Create Parallel Business State

---

# 5. Presentation Technology

The implementation should follow the technology already established by the MFM implementation baseline.

The presentation layer should remain lightweight and appropriate for a Windows desktop application.

Avoid introducing a large web or enterprise frontend framework unless future requirements justify it.

---

# 6. Main Application Window

The main window provides:

```text
Application Header

Navigation

Workspace

Status Area
```

A conceptual layout:

```text
+------------------------------------------------------+
| MFM | Organization | User | Notifications            |
+--------------------+---------------------------------+
| Navigation          | Main Workspace                 |
|                     |                                 |
| Dashboard           |                                 |
| Members             |                                 |
| Accounting          |                                 |
| Projects            |                                 |
| Grants              |                                 |
| Documents           |                                 |
| Reports             |                                 |
| Administration      |                                 |
+--------------------+---------------------------------+
| Status / System Information                          |
+------------------------------------------------------+
```

---

# 7. Navigation

Navigation should expose only functionality relevant to the current user.

Unauthorized modules may be:

- Hidden
- Disabled
- Displayed with restricted state

However, hiding a menu item is not a security mechanism.

Authorization remains enforced by services.

---

# 8. Navigation Groups

A practical grouping may be:

```text
Home

Members

Finance

Projects

Grants

Documents

Reports

Administration
```

The exact labels may follow the existing UI implementation.

---

# 9. Current Context

The interface should clearly show the current location.

Example:

```text
Members
→ Member Details
```

This helps users understand where they are.

---

# 10. Breadcrumbs

Where screens become nested, breadcrumbs may be used.

Example:

```text
Projects
→ Álvur Restoration
→ Documents
→ Document Details
```

---

# 11. Authentication Screen

The login screen should contain:

- User Identifier
- Password
- Login Action
- Error Area

Optional:

- Show / Hide Password
- Organization Context
- Version Information

---

# 12. Login Workflow

```text
Enter Credentials

↓

Submit

↓

Authentication Service

↓

Success?

YES → Create Session → Dashboard

NO → Show Safe Error
```

---

# 13. Login Error

Use understandable feedback.

Example:

```text
The credentials could not be verified.
```

Do not expose technical authentication details.

---

# 14. Session State

After login, the GUI receives the authenticated user context.

The presentation layer may use this to:

- Show User Name
- Show Roles
- Display Authorized Navigation

It must not treat client-side state as the final authorization decision.

---

# 15. Logout Workflow

```text
User Selects Logout

↓

Confirm if required

↓

Security Service

↓

Session Invalidated

↓

Login Screen
```

---

# 16. Dashboard

The dashboard provides a concise operational overview.

Possible sections:

```text
Membership

Finance

Projects

Grants

Documents

Tasks

Notifications
```

The dashboard should not attempt to display every available metric.

---

# 17. Dashboard Principle

Dashboard values must have clear provenance.

Example:

```text
Actual Accounting Balance
Source: Accounting Core
```

---

# 18. Dashboard Financial Rule

Financial dashboard values must come from Accounting Core or approved Accounting Core query services.

The dashboard must never maintain its own authoritative balance.

---

# 19. Dashboard Cards

Cards may display:

```text
Active Members

Open Projects

Upcoming Grant Deadlines

Outstanding Tasks

Current Cash / Bank Position
```

Only authorized values should be shown.

---

# 20. Dashboard Refresh

Dashboard data may be:

- Loaded at Login
- Refreshed on Navigation
- Manually Refreshed

The refresh strategy should balance usability and performance.

---

# 21. Membership Screen

The membership workspace should support:

```text
Member List

Search

Filters

Create Member

Member Details

Edit

Status

History
```

---

# 22. Member List

The member list should display practical columns such as:

```text
Membership No.

Name

Status

Category

Contact Indicator
```

Avoid displaying unnecessary personal data.

---

# 23. Member Search

Search should support common user needs.

Example:

```text
Name

Membership Number

Email
```

Search should be tolerant of normal input variations where appropriate.

---

# 24. Member Filters

Possible filters:

```text
Active

Inactive

Suspended

Category
```

---

# 25. Member Create Workflow

```text
New Member

↓

Enter Information

↓

Validate

↓

Save

↓

Success Message

↓

Open Member
```

---

# 26. Member Form

Fields should be grouped logically.

Example:

```text
Identity

Contact

Membership

Administrative Information
```

---

# 27. Required Fields

Required fields should be clearly marked.

The GUI may provide immediate feedback.

The service remains authoritative for validation.

---

# 28. Member Edit

Editing follows:

```text
Open

↓

Edit

↓

Validate

↓

Save

↓

Audit

↓

Refresh
```

---

# 29. Unsaved Changes

If a user leaves a modified form:

```text
Unsaved Changes

Save

Discard

Cancel
```

Do not silently discard user input.

---

# 30. Membership Status Change

Status changes should use explicit actions.

Example:

```text
Change Status

↓

Select New Status

↓

Confirm

↓

MembershipService

↓

Result
```

Avoid free-text status editing.

---

# 31. Membership History

History should show:

```text
Date

Previous Status

New Status

Changed By
```

Where appropriate.

---

# 32. Accounting Workspace

The accounting workspace should provide controlled access to:

- Accounts
- Vouchers
- Ledger
- Periods
- Financial Reports

---

# 33. Accounting Navigation

A practical structure:

```text
Accounting

├── Overview
├── Vouchers
├── Accounts
├── Ledger
├── Periods
└── Reports
```

---

# 34. Voucher List

The voucher list may show:

```text
Voucher No.

Date

Description

Amount

Status
```

---

# 35. Voucher Creation

Workflow:

```text
New Voucher

↓

Header

↓

Voucher Lines

↓

Validate

↓

Review

↓

Post / Save Draft
```

---

# 36. Voucher Header

Typical information:

```text
Voucher Number

Date

Description

Reference
```

---

# 37. Voucher Lines

Each line may contain:

```text
Account

Description

Debit

Credit

Project / Reference where applicable
```

---

# 38. Voucher Balance Display

The form should display:

```text
Total Debit

Total Credit

Difference
```

Example:

```text
Debit: 5,000.00

Credit: 5,000.00

Difference: 0.00
```

---

# 39. Posting Control

The Post action should be enabled only when the form appears valid.

However, the service must perform the final validation.

---

# 40. Posting Confirmation

For posting, a confirmation may display:

```text
Post this voucher?

This action will create an accounting entry.
```

---

# 41. Accounting Error

Example:

```text
The voucher cannot be posted because the accounting period is closed.
```

Do not display raw database or stack-trace errors.

---

# 42. Voucher Reversal

The GUI should provide an explicit reversal action.

It should show:

- Original Voucher
- Reversal Date
- Reason
- Confirmation

---

# 43. Closed Period

If a period is closed:

```text
Posting → Disabled / Rejected

Reversal → Controlled Workflow
```

The GUI should communicate the reason.

---

# 44. Project Workspace

The project workspace should support:

```text
Project List

Project Details

Tasks

Milestones

Budget Planning

Documents

Financial Overview
```

---

# 45. Project List

Columns may include:

```text
Project

Status

Start

End

Responsible

Budget
```

---

# 46. Project Details

Project details may contain:

```text
Overview

Objectives

Responsible

Dates

Status

Budget

Tasks

Documents
```

---

# 47. Project Creation

Workflow:

```text
New Project

↓

Enter Details

↓

Validate

↓

Create

↓

Open Project Workspace
```

---

# 48. Project Status

Use explicit actions:

```text
Start Project

Complete Project

Archive Project
```

rather than unrestricted text editing.

---

# 49. Project Budget

The budget screen may show:

```text
Budget

Forecast

Actual

Variance
```

The actual value must originate from Accounting Core.

---

# 50. Project Financial Provenance

A financial display should make clear:

```text
Budget
→ Project Planning

Actual
→ Accounting Core

Variance
→ Derived
```

---

# 51. Project Tasks

Tasks may show:

```text
Task

Responsible

Due Date

Status

Priority
```

---

# 52. Task Workflow

```text
Create

↓

Assign

↓

Work

↓

Complete

```

The workflow should remain lightweight.

---

# 53. Grant Workspace

The grant workspace should support:

```text
Grant List

Applications

Deadlines

Awards

Reporting

Documents
```

---

# 54. Grant List

Columns may include:

```text
Grant

Provider

Deadline

Status

Requested

Awarded
```

---

# 55. Grant Application Workflow

```text
Identify

↓

Plan

↓

Draft

↓

Review

↓

Submit

↓

Record Result
```

---

# 56. Grant Submission

Submission should require explicit confirmation.

Example:

```text
Submit Application?

After submission the status will change to Submitted.
```

---

# 57. Grant Deadline Display

Upcoming deadlines should be visually clear.

Possible states:

```text
Normal

Approaching

Due Soon

Overdue
```

The exact visual styling should remain accessible and understandable.

---

# 58. Grant Award

When an award is recorded:

```text
Record Award

↓

Validate

↓

Save

↓

Link to Project if applicable

↓

Notify if configured
```

---

# 59. Grant Financial Display

The GUI may show:

```text
Requested

Awarded

Planned Spend

Actual Spend
```

Actual Spend is derived from Accounting Core.

---

# 60. Document Workspace

The document workspace should provide:

```text
Document List

Search

Upload

Metadata

Versions

Archive

Retention
```

---

# 61. Document List

Typical columns:

```text
Name

Category

Version

Related Entity

Date

Status
```

---

# 62. Document Upload Workflow

```text
Upload

↓

Select File

↓

Validate

↓

Enter Metadata

↓

Confirm

↓

Store

↓

Result
```

---

# 63. Upload Progress

For larger files, the UI may display progress.

The user should receive clear feedback if storage fails.

---

# 64. Document Metadata

Metadata may include:

```text
Title

Category

Description

Related Member / Project / Grant

Retention

Status
```

---

# 65. Document Version Workflow

```text
Open Document

↓

New Version

↓

Select File

↓

Validate

↓

Save Version
```

Previous versions remain preserved according to policy.

---

# 66. Document Hold

A held document should clearly display:

```text
Retention Hold Active
```

Deletion controls should be unavailable or rejected.

---

# 67. Document Archive

Archiving should clearly distinguish:

```text
Active

Archived
```

Archived documents remain searchable where policy permits.

---

# 68. Reporting Workspace

Reports should be organized by business area.

Example:

```text
Accounting Reports

Membership Reports

Project Reports

Grant Reports

Document Reports
```

---

# 69. Report Generation

Workflow:

```text
Select Report

↓

Select Filters

↓

Generate

↓

Preview

↓

Export
```

---

# 70. Report Filters

Filters should be understandable.

Examples:

```text
Date From

Date To

Project

Grant

Member Status
```

---

# 71. Report Provenance

Important reports should identify their source.

Example:

```text
Financial Report

Source:
Accounting Core

Period:
01-01-2026 to 31-12-2026
```

---

# 72. Report Export

Supported formats should follow the established MFM implementation.

Possible:

```text
PDF

Excel

CSV
```

Export must respect authorization.

---

# 73. Administration Workspace

Administration should be restricted to authorized users.

Possible sections:

```text
Users

Roles

Permissions

Organization

Configuration

Backup

Maintenance

Diagnostics
```

---

# 74. User Administration

The UI should support:

```text
Create User

Disable User

Assign Role

Review Access
```

---

# 75. Role Administration

Role editing should show:

```text
Role Name

Permissions

Users Assigned
```

Changes require appropriate authorization.

---

# 76. Configuration

Configuration screens should group settings.

Example:

```text
Organization

Accounting

Membership

Notifications

Documents

System
```

---

# 77. Sensitive Configuration

Secrets must not be displayed in plaintext.

The UI may show:

```text
Credential Configured
```

instead of the actual credential.

---

# 78. Backup Screen

The backup screen may show:

```text
Last Backup

Backup Status

Backup Location

Verification Status

Create Backup

Restore
```

---

# 79. Restore UI

Restore must be clearly marked as a high-risk operation.

The confirmation should state:

```text
Restore will replace the current application database.

A current backup should exist before continuing.
```

---

# 80. Maintenance Screen

Maintenance may provide:

```text
Database Integrity Check

Backup Verification

Database Information

Migration Status

Log Diagnostics
```

---

# 81. Notifications

Notifications should appear in:

- Header
- Notification Center
- Relevant Workflow Screen

They should not overwhelm users.

---

# 82. Notification Severity

Use clear categories:

```text
Information

Warning

Action Required

Critical
```

---

# 83. Notification Action

Where appropriate:

```text
Notification

↓

Open Related Record
```

Example:

```text
Grant deadline approaching

→ Open Grant
```

---

# 84. Error Presentation

Errors should be:

- Clear
- Specific
- Actionable
- Non-Technical

Example:

```text
This member number is already in use.
```

---

# 85. Validation Presentation

Inline validation should identify the affected field.

Example:

```text
Membership Number
[ 12345 ]

This number already exists.
```

---

# 86. Form Validation Timing

Validation may occur:

- On Field Exit
- On Save
- On Submit

Critical business validation always occurs in the service.

---

# 87. Confirmation Dialogs

Confirmation should be used for destructive or significant actions.

Examples:

- Delete
- Archive
- Post
- Reverse
- Restore
- Disable User

Do not require confirmation for every harmless action.

---

# 88. Destructive Action Design

Destructive actions should be visually and semantically distinct.

The user should understand:

```text
What will happen?

Which record?

Can it be undone?
```

---

# 89. Delete Policy

Where business history must be preserved, prefer:

```text
Archive

Deactivate

Cancel
```

over physical deletion.

---

# 90. Loading State

Long-running operations should display:

```text
Loading...

Processing...

Generating...

Restoring...
```

The user should not be left wondering whether the application has stopped responding.

---

# 91. Progress

For operations with measurable progress:

```text
0%

25%

50%

75%

100%
```

For operations without measurable progress, use an indeterminate progress indicator.

---

# 92. Success Feedback

After a successful operation, provide concise feedback.

Example:

```text
Member saved successfully.
```

Avoid excessive confirmation dialogs.

---

# 93. Empty States

Empty lists should explain what the user can do.

Example:

```text
No projects found.

Create a new project or change your filters.
```

---

# 94. Search Empty State

If filters produce no results:

```text
No members match the selected criteria.
```

Offer an easy way to clear filters.

---

# 95. Table Design

Tables should support:

- Sorting
- Filtering where useful
- Selection
- Double-click / Open
- Appropriate Column Widths

Avoid excessive columns.

---

# 96. Table Performance

Large datasets should use paginated or controlled loading.

Do not load thousands of records unnecessarily.

---

# 97. Keyboard Navigation

Common operations should support keyboard use where practical.

Examples:

```text
Tab

Enter

Escape

Ctrl+S
```

---

# 98. Accessibility

The GUI should provide:

- Readable Text
- Clear Labels
- Logical Focus
- Keyboard Access
- Sufficient Contrast
- Non-Color-Only Indicators

---

# 99. Color Usage

Color may reinforce status but must not be the only indication.

Example:

```text
Warning

[Icon] Warning
```

rather than relying only on yellow color.

---

# 100. Localization

The application should keep user-visible strings centralized where practical.

This makes future language support easier.

---

# 101. Date Display

Dates should be displayed according to the organization's locale.

The underlying stored representation remains standardized.

---

# 102. Number Display

Numbers should use consistent locale-aware formatting.

---

# 103. Currency Display

Currency values should clearly identify the currency.

Example:

```text
DKK 12,500.00
```

The actual formatting follows the organization's locale settings.

---

# 104. Accounting Display

Financial screens should distinguish:

```text
Draft

Posted

Reversed

Closed
```

Status should be visible without relying only on color.

---

# 105. User Permissions in GUI

The UI may:

```text
Hide unavailable action

Disable unavailable action

Show restricted state
```

But the service must still enforce permission.

---

# 106. Unauthorized Action

If a user attempts an unauthorized action:

```text
You do not have permission to perform this action.
```

Do not expose internal permission identifiers unless useful to administrators.

---

# 107. Session Expiration UI

If the session expires:

```text
Your session has expired.

Please sign in again.
```

Unsaved work should be handled carefully where practical.

---

# 108. Concurrency Conflict UI

Example:

```text
This record has been changed by another user.

Reload the record before saving.
```

Do not silently overwrite.

---

# 109. Offline / Database Unavailable

If the database becomes unavailable:

```text
The application cannot currently access the database.

Your data has not been changed.
```

The application should not pretend that a save succeeded.

---

# 110. Service Error Mapping

The presentation layer should map service errors to appropriate messages.

Example:

```text
DuplicateMemberError

↓

"This membership number is already in use."
```

---

# 111. Technical Error Handling

Unexpected technical errors should:

- Log Technical Detail
- Show Safe User Message
- Provide Correlation ID where useful

Example:

```text
An unexpected error occurred.

Reference:
MFM-8F31A2
```

---

# 112. User Workflow Consistency

Similar actions should behave similarly.

For example:

```text
New

Edit

Save

Cancel

Archive
```

should use consistent patterns across modules.

---

# 113. Form Layout Consistency

Forms should use consistent:

- Labels
- Required Indicators
- Button Placement
- Error Presentation
- Save / Cancel Behavior

---

# 114. Navigation State

The application should preserve useful navigation context.

Example:

```text
Project List

↓

Project

↓

Task

↓

Back

→ Project
```

---

# 115. Modal Dialog Use

Dialogs should be used for focused tasks.

Avoid deeply nested modal dialogs that make navigation confusing.

---

# 116. Main Workspace Principle

The main workspace should prioritize the user's task.

Avoid displaying unnecessary technical information.

---

# 117. Administration Diagnostics

Technical diagnostic information should be separated from normal business screens.

---

# 118. Audit Visibility

Authorized administrators may view relevant audit information.

Ordinary users should not automatically see all security or administrative audit events.

---

# 119. GUI Logging

GUI logging should focus on:

- Navigation Errors
- Unexpected Exceptions
- Integration Problems
- Technical Failures

Do not log sensitive form contents unnecessarily.

---

# 120. GUI Testing

Presentation testing should cover:

- Navigation
- Form Validation
- Authorization Presentation
- Save / Cancel
- Error Messages
- Table Operations
- Dialogs
- Keyboard Use
- Session Expiration

---

# 121. Authentication UI Tests

Minimum:

```text
Valid Login

Invalid Login

Disabled User

Logout

Session Expiration
```

---

# 122. Membership UI Tests

Minimum:

```text
List

Search

Create

Edit

Status

History

Authorization
```

---

# 123. Accounting UI Tests

Minimum:

```text
Voucher

Balance

Draft

Post

Closed Period

Reverse

Reports
```

---

# 124. Project UI Tests

Minimum:

```text
Create

Edit

Status

Task

Milestone

Budget

Financial Actual
```

---

# 125. Grant UI Tests

Minimum:

```text
List

Application

Submission

Deadline

Award

Project Link
```

---

# 126. Document UI Tests

Minimum:

```text
Upload

Metadata

Version

Hold

Archive

Open

Delete Restriction
```

---

# 127. Administration UI Tests

Minimum:

```text
User

Role

Configuration

Backup

Restore

Maintenance
```

---

# 128. Reporting UI Tests

Minimum:

```text
Select Report

Filter

Generate

Preview

Export

Authorization
```

---

# 129. GUI Integration Testing

Important workflows should be tested end-to-end:

```text
GUI

↓

Service

↓

Repository

↓

Database

↓

Result
```

---

# 130. GUI Security Testing

Test:

- Unauthorized Menu Access
- Unauthorized Service Action
- Privileged Action
- Session Expiration
- Export Permissions
- Document Permissions

---

# 131. GUI Performance

The GUI should remain responsive for normal operations.

Heavy tasks should use controlled background processing.

---

# 132. Startup

Startup should:

```text
Load Configuration

↓

Check Database

↓

Check Schema

↓

Authenticate

↓

Load Workspace
```

The exact sequence follows the security and migration implementation.

---

# 133. Startup Failure

If startup cannot safely continue:

```text
Show Clear Error

↓

Log Technical Detail

↓

Do Not Enter Partial Operational State
```

---

# 134. Shutdown

Application shutdown should:

- Save Required State
- Close Resources
- End Session where appropriate
- Close Database Connections
- Stop Background Jobs Safely

---

# 135. Unsaved Form Recovery

Where practical, important forms may warn before shutdown.

Do not silently discard important accounting or administrative input.

---

# 136. Accounting UX Principle

Accounting workflows should favor:

```text
Clarity

Verification

Traceability

```

over speed at the expense of financial correctness.

---

# 137. Membership UX Principle

Membership workflows should favor:

```text
Simple Data Entry

Searchability

Clear Status

History
```

---

# 138. Project UX Principle

Project workflows should favor:

```text
Overview

Tasks

Milestones

Budget Planning

Actuals
```

---

# 139. Grant UX Principle

Grant workflows should favor:

```text
Deadline Awareness

Application Progress

Documents

Award Tracking

Reporting
```

---

# 140. Document UX Principle

Document workflows should favor:

```text
Findability

Version Clarity

Retention Awareness

Safe Access
```

---

# 141. Reporting UX Principle

Reports should answer a user question directly.

Avoid reports that expose raw database structures rather than meaningful information.

---

# 142. Dashboard UX Principle

The dashboard should answer:

```text
What needs attention?

What changed?

What is important now?
```

---

# 143. Administration UX Principle

Administrative operations should clearly distinguish:

```text
Normal

Sensitive

Destructive

Recovery
```

operations.

---

# 144. GUI Anti-Patterns

Avoid:

### Business Logic in Event Handlers

### Direct SQL in Screens

### Hidden Automatic Posting

### Silent Data Loss

### Excessive Dialogs

### Huge Data Tables

### Technical Error Messages

### Parallel Financial Calculations

---

# 145. Presentation Component Structure

A practical component structure may be:

```text
src/
└── gui/
    ├── main_window
    ├── dashboard
    ├── members
    ├── accounting
    ├── projects
    ├── grants
    ├── documents
    ├── reports
    └── administration
```

The exact directory structure must follow the actual MFM source tree.

---

# 146. Screen Responsibility

Each screen should have a clear responsibility.

Example:

```text
MemberListScreen
→ Find and open members

MemberDetailsScreen
→ View and edit one member
```

---

# 147. Controller / View Model

Where appropriate, screens may use a controller or view-model layer.

This helps prevent event handlers from becoming large.

---

# 148. GUI State

GUI state may contain:

- Current Filter
- Selected Record
- Form Values
- Loading State
- Error State

Business truth remains in domain services and persistence.

---

# 149. GUI State Synchronization

After a successful save:

```text
Save

↓

Reload / Update View

↓

Display Current State
```

Avoid relying on stale local form state.

---

# 150. Refresh

Refresh should retrieve current data from the appropriate service.

---

# 151. Bulk User Actions

Bulk actions may be provided where useful.

Examples:

```text
Archive Selected Members
Export Selected Records
```

Bulk actions require:

- Authorization
- Validation
- Confirmation
- Result Summary

---

# 152. Bulk Result

Example:

```text
25 records selected

23 completed

2 failed

View details
```

---

# 153. Error Summary

For multi-item operations, errors should identify affected records without exposing unnecessary technical details.

---

# 154. User Workflow Definition of Ready

A workflow is Ready when:

- User Goal Is Clear
- Screen Flow Is Defined
- Authorization Is Defined
- Validation Is Defined
- Error States Are Defined
- Success State Is Defined
- Data Source Is Known

---

# 155. User Workflow Definition of Done

A workflow is Done when:

- Screens Implemented
- Navigation Works
- Service Integration Works
- Authorization Works
- Validation Works
- Error Handling Works
- Tests Pass
- Accessibility Reviewed

---

# 156. Presentation Release Gate

Before release:

```text
Navigation

Authentication

Authorization

Forms

Validation

Error Handling

Accounting UX

Reports

Exports

Accessibility

Performance

Regression
```

must be reviewed.

---

# 157. Traceability

Presentation changes should trace:

```text
Requirement

↓

Workflow

↓

Screen

↓

Service

↓

Repository

↓

Test

↓

Release
```

---

# 158. Small-Association Principle

MFM GUI implementation should remain simple and understandable.

Do not introduce:

- Complex SPA Architecture
- Microfrontend Architecture
- Enterprise Workflow Engines
- Excessive Client State Management

unless future scale requires it.

---

# 159. Final Presentation Principle

The GUI is the user's working surface.

It should be:

```text
Clear

Predictable

Accessible

Secure

Responsive
```

while keeping business authority in the application services and domain model.

---

# 160. Final Financial Presentation Principle

The GUI must never create a parallel financial truth.

Financial values displayed in:

- Accounting
- Projects
- Grants
- Reports
- Dashboards

must trace back to Accounting Core where they represent actual financial transactions.

---

# 161. Summary

MFM v1.2-570 establishes the GUI, presentation layer and user workflow implementation baseline.

It defines:

- Main Window
- Navigation
- Authentication
- Dashboard
- Membership
- Accounting
- Projects
- Grants
- Documents
- Reporting
- Administration
- Notifications
- Validation
- Error Handling
- Accessibility
- Concurrency
- GUI Testing
- Security
- Usability

The fundamental architectural rule remains:

> **The GUI presents and initiates business operations; it does not own business truth.**

And:

> **Accounting Core remains the sole authoritative financial ledger.**

---

# 162. Next Document

**MFM v1.2-580 – Reporting, Dashboard & Read-Model Implementation**

---

# END OF DOCUMENT
