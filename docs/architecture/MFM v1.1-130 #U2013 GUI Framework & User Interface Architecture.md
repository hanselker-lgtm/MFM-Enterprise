# MFM v1.1-130 – GUI Framework & User Interface Architecture

Version: 1.1

Document ID: MFM-v1.1-130

Status: Technical Implementation

---

# 1. Purpose

This document defines the graphical user interface (GUI) architecture for MaritimForeningsManager (MFM) v1.1.

The GUI shall provide a modern, intuitive and responsive desktop interface that supports the daily work of a small non-profit association.

The GUI is strictly separated from business logic.

Business rules remain exclusively within the Service Layer.

---

# 2. Design Objectives

The user interface shall be:

- Simple
- Consistent
- Fast
- Accessible
- Maintainable
- Responsive
- Easy to learn

The application is designed for volunteers and administrative users with varying levels of computer experience.

---

# 3. GUI Technology

Framework

```
PySide6 (Qt6)
```

Pattern

```
MVC (Model-View-Controller)
```

Extended by:

```
Service Layer

Repository Layer

Domain Model
```

The GUI never communicates directly with the database.

---

# 4. Overall GUI Architecture

```
Main Window

│

├── Ribbon/Menu

├── Navigation Panel

├── Workspace

├── Status Bar

└── Notification Area
```

Every screen is loaded dynamically inside the workspace.

---

# 5. Main Window

The Main Window contains:

- Application Menu
- Toolbar
- Navigation Tree
- Workspace Tabs
- Status Bar
- Notification Panel

Only one Main Window instance exists.

---

# 6. Navigation Structure

```
Dashboard

Membership

Accounting

Projects

Grants

Documents

Reports

Administration

Backup

Help
```

Modules become visible according to user permissions.

---

# 7. Workspace

The workspace supports:

- Single View
- Multiple Tabs
- Dialog Windows
- Floating Windows (future)

Every business screen is loaded into the workspace.

---

# 8. Menu Structure

```
File

Edit

View

Membership

Accounting

Projects

Grants

Documents

Reports

Administration

Tools

Help
```

Menu items are role-sensitive.

---

# 9. Toolbar

Common toolbar actions:

- New
- Edit
- Save
- Delete
- Refresh
- Search
- Print
- Export

Unavailable functions are disabled rather than hidden where appropriate.

---

# 10. Dashboard

The dashboard is displayed after login.

Widgets may include:

- Membership Summary
- Financial Overview
- Active Projects
- Grant Status
- Pending Tasks
- Recent Documents
- Upcoming Meetings
- Notifications

Widgets are configurable by role.

---

# 11. Standard Screen Layout

```
Toolbar

↓

Filter Panel

↓

Data Grid

↓

Detail Panel

↓

Status Information
```

This layout shall be reused throughout the application.

---

# 12. Data Grids

Every grid supports:

- Sorting
- Filtering
- Searching
- Pagination (optional)
- Export
- Column Selection

Large datasets shall use lazy loading.

---

# 13. Forms

All forms follow the same layout:

```
General Information

↓

Business Information

↓

Additional Information

↓

Audit Information
```

Mandatory fields are clearly indicated.

---

# 14. Dialog Windows

Standard dialogs include:

- Confirmation
- Information
- Warning
- Error
- Search
- File Selection
- Print Preview

Dialog behaviour shall be consistent.

---

# 15. Validation

Validation occurs in two stages.

GUI Validation

Examples:

- Empty fields
- Invalid dates
- Number formats

Service Validation

Examples:

- Business Rules
- Permissions
- Accounting Rules

Business validation always occurs in the Service Layer.

---

# 16. Search Framework

Global search supports:

- Members
- Projects
- Grants
- Documents
- Accounting Vouchers

Search results are grouped by module.

---

# 17. Status Bar

Displays:

- Logged-in User
- Current Role
- Database Status
- Backup Status
- Current Company
- Application Version

Optional indicators include online/offline status.

---

# 18. Notifications

Notification types:

Information

Warning

Error

Reminder

Examples:

- Membership Renewal Due
- Backup Failed
- Grant Deadline
- Missing Documents

Notifications never execute automatic business actions.

---

# 19. Themes

Supported themes:

Light

Dark (future)

High Contrast (future)

Theme settings are stored per user.

---

# 20. Accessibility

The GUI shall support:

- Keyboard Navigation
- Screen Scaling
- High DPI Displays
- Shortcut Keys
- Readable Fonts
- Colour Contrast

Accessibility is considered during every screen design.

---

# 21. Keyboard Shortcuts

Examples:

```
Ctrl + N

New

Ctrl + S

Save

Ctrl + P

Print

Ctrl + F

Search

Ctrl + E

Export

F5

Refresh

Esc

Cancel
```

Shortcut behaviour is consistent throughout the application.

---

# 22. Error Handling

Errors are presented using standard dialogs.

Technical details are written to logs.

Users receive:

- Clear description
- Suggested action
- Error reference number

Stack traces are never shown to normal users.

---

# 23. Screen Catalogue

The application contains dedicated screens for:

Membership

- Member List
- Member Details
- Membership Payments

Accounting

- Chart of Accounts
- Journal
- Voucher Entry
- Trial Balance
- Balance Sheet

Projects

- Project List
- Project Details
- Milestones
- Budget

Grants

- Funding Opportunities
- Applications
- Awards

Documents

- Document Browser
- Upload
- Version History

Reporting

- Dashboard
- Reports
- KPIs

Administration

- Users
- Roles
- Configuration

Backup

- Backup
- Restore
- Maintenance

---

# 24. Window Lifecycle

```
Application Start

↓

Login

↓

Dashboard

↓

Module Selection

↓

Business Screen

↓

Service Layer

↓

Repository

↓

Database

↓

GUI Refresh
```

The GUI always reflects committed business data.

---

# 25. GUI Development Standards

Every screen shall:

- Have one controller
- Have one UI definition
- Use Services only
- Avoid business logic
- Support validation
- Support localisation

Maximum recommended controller size:

300 source lines.

Large windows should be split into reusable components.

---

# 26. Future Enhancements

Future GUI improvements may include:

- Dockable Windows
- Ribbon Interface
- Touch Support
- Integrated Calendar
- Kanban Boards
- Drag-and-Drop Document Management
- Multi-monitor Support

These enhancements shall remain compatible with the established GUI architecture.

---

# 27. Summary

The GUI Framework & User Interface Architecture establishes a consistent, modular and user-friendly interface for MFM v1.1.

The design follows a strict separation between presentation, business logic and data access while providing a modern Windows desktop experience suitable for volunteer organisations and small maritime associations.

The framework ensures consistency across all modules and provides a solid foundation for future expansion without compromising maintainability or usability.

---

# Next Document

**MFM v1.1-140 – Membership Module Implementation**

---

# END OF DOCUMENT