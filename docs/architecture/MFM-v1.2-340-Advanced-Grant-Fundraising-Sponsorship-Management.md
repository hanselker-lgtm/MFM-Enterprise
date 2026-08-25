# MFM v1.2-340 – Advanced Grant, Fundraising & Sponsorship Management

Version: 1.2

Document ID: MFM-v1.2-340

Status: Functional Expansion

---

# 1. Purpose

This document defines the Advanced Grant, Fundraising & Sponsorship Management capabilities introduced in MaritimForeningsManager (MFM) v1.2.

The purpose is to extend the Grants & Funding Module into a structured funding-management environment covering external grants, sponsorships, donations, fundraising activities and related compliance.

The module remains an administrative and planning module.

The Accounting Core remains the sole authoritative financial ledger.

---

# 2. Objectives

The expanded module shall support:

- Advanced Grant Pipeline Management
- Funding Opportunity Management
- Grant Application Management
- Sponsorship Management
- Donation Campaigns
- Fundraising Activities
- Funding Targets
- Commitment Tracking
- Reporting Obligations
- Funding Relationships
- Funding Portfolio Analysis

---

# 3. Architectural Principles

The following principles remain mandatory:

- Grants own grant-administration data.
- Fundraising owns fundraising planning and campaign data.
- Sponsorships own sponsor relationship data.
- Accounting owns all actual financial transactions.
- Projects own project planning information.
- Documents own physical files.
- Reporting consumes authoritative data and remains read-only.

No fundraising or grant component may create a parallel financial ledger.

---

# 4. Expanded Funding Architecture

```text
Funding Opportunity

        ↓

Funding Assessment

        ↓

Application / Sponsorship Proposal

        ↓

Submission

        ↓

Decision

        ↓

Award / Commitment

        ↓

Project Delivery

        ↓

Reporting

        ↓

Completion / Archive
```

Every stage is traceable.

---

# 5. Funding Pipeline

The funding pipeline provides a consolidated overview of potential funding.

Pipeline stages include:

- Identified
- Assessed
- Qualified
- Preparing
- Submitted
- Under Review
- Approved
- Rejected
- Withdrawn
- Completed

Pipeline status is administrative information and does not represent accounting balances.

---

# 6. Funding Opportunity

Each opportunity may contain:

- Opportunity Number
- Programme
- Funding Organisation
- Funding Type
- Description
- Eligibility
- Opening Date
- Closing Date
- Maximum Funding
- Expected Decision Date
- Website Reference
- Responsible User
- Related Project
- Notes

---

# 7. Opportunity Assessment

Before an application is created, an opportunity may be assessed.

Assessment criteria may include:

- Strategic Fit
- Eligibility
- Funding Potential
- Project Readiness
- Time Requirement
- Co-Funding Requirement
- Reporting Burden
- Probability of Success

Assessment scores are configurable.

---

# 8. Application Management

Applications contain:

- Application Number
- Funding Opportunity
- Funding Organisation
- Project
- Requested Amount
- Own Contribution
- Co-Funding
- Submission Date
- Decision Date
- Responsible User
- Status
- Notes

Applications may contain multiple versions of supporting documents.

---

# 9. Application Workflow

```text
Draft

↓

Internal Review

↓

Board Approval (where required)

↓

Submitted

↓

Under Review

↓

Approved / Rejected

↓

Agreement

↓

Active

↓

Completed
```

Workflow transitions are audited.

---

# 10. Internal Approval

Applications may require internal approval before submission.

Approval records include:

- Submitted For Approval
- Reviewer
- Decision
- Decision Date
- Comments

Approval is an organizational decision and does not create an accounting transaction.

---

# 11. Grant Awards

Award records contain:

- Award Number
- Application
- Approved Amount
- Award Date
- Agreement Date
- Conditions
- Payment Schedule
- Reporting Requirements
- Funding Period
- Responsible User

Approved amounts are administrative award information.

Actual receipts remain Accounting transactions.

---

# 12. Sponsorship Management

The module introduces structured sponsorship management.

Sponsors may include:

- Companies
- Local Businesses
- Foundations
- Private Supporters
- Strategic Partners

Sponsor records may contain:

- Organisation Name
- Contact Person
- Contact Details
- Sponsor Category
- Relationship Owner
- Sponsorship Status
- Agreement Dates
- Notes

---

# 13. Sponsorship Proposals

Each sponsorship proposal may contain:

- Proposal Number
- Sponsor
- Project
- Sponsorship Type
- Requested Contribution
- Benefits Offered
- Validity Period
- Responsible User
- Status

Sponsorship proposals are planning records.

Financial contributions are posted by Accounting after receipt or other approved financial recognition.

---

# 14. Sponsorship Agreements

Agreements may define:

- Sponsor
- Project
- Agreement Date
- Start Date
- End Date
- Contribution Terms
- Visibility Rights
- Branding Rights
- Deliverables
- Renewal Terms
- Reporting Requirements

Signed agreements are stored through the Document Service.

---

# 15. Fundraising Campaigns

Fundraising campaigns may be created for:

- Vessel Restoration
- Equipment Purchase
- Educational Activities
- Events
- Preservation Projects
- Emergency Repairs

Campaign records include:

- Campaign Number
- Name
- Objective
- Target Amount
- Start Date
- End Date
- Responsible User
- Status
- Related Project

The target is a planning value.

Actual donations remain Accounting data.

---

# 16. Campaign Lifecycle

```text
Concept

↓

Planning

↓

Approved

↓

Active

↓

Target Reached / End Date

↓

Completed

↓

Archived
```

Campaign transitions are audited.

---

# 17. Donation Administration

The module may register donation-related administrative information such as:

- Campaign
- Donor Reference
- Donation Date
- Communication
- Acknowledgement Status
- Donor Consent

The financial amount and accounting treatment remain authoritative in Accounting.

Where a donation is posted financially, the fundraising record references the corresponding accounting transaction rather than duplicating it.

---

# 18. Donor Relationships

Donor relationship records may include:

- Individual
- Organisation
- Anonymous Donor
- Sponsor
- Previous Supporter

Relationship history may include:

- Contact
- Campaign Participation
- Acknowledgement
- Correspondence
- Consent

Sensitive personal information is permission controlled.

---

# 19. Fundraising Targets

Targets may be defined at:

- Campaign Level
- Project Level
- Annual Level

Examples:

```text
Campaign Target

↓

100,000 DKK
```

Target progress is calculated from authoritative financial information where available.

The fundraising module does not maintain a second ledger.

---

# 20. Funding Commitments

Administrative commitments may include:

- Expected Grant
- Sponsorship Commitment
- Pledged Donation
- Co-Funding Commitment

Each commitment includes:

- Source
- Expected Amount
- Date
- Status
- Responsible User
- Related Project

A commitment is not treated as an accounting transaction unless and until Accounting records the relevant financial event.

---

# 21. Co-Funding Management

Projects may identify:

- Grant Funding
- Sponsorship
- Donations
- Own Contribution
- Volunteer Contribution
- In-Kind Contribution

Financial amounts are reconciled with Accounting where actual transactions exist.

Non-financial contributions remain operational records.

---

# 22. Funding Portfolio

The funding portfolio provides an overview of:

- Funding Pipeline
- Applications
- Awards
- Sponsorships
- Campaigns
- Commitments
- Reporting Deadlines
- Project Funding Sources

Portfolio information is read-only from the Reporting perspective.

---

# 23. Funding Dashboard

New dashboard widgets include:

- Open Opportunities
- Applications in Progress
- Pending Decisions
- Awarded Funding
- Sponsorship Pipeline
- Active Campaigns
- Campaign Progress
- Upcoming Grant Reports
- Funding Deadlines

Financial figures displayed on dashboards originate from Accounting where they represent actual financial activity.

---

# 24. Deadline Management

The module tracks:

- Application Deadlines
- Decision Dates
- Agreement Deadlines
- Reporting Deadlines
- Payment Milestones
- Campaign End Dates
- Sponsorship Renewal Dates

Deadline reminders are configurable.

---

# 25. Notification Workflow

Example:

```text
Deadline Approaching

↓

Notification Service

↓

Responsible User

↓

Review

↓

Action

↓

Audit
```

Notifications do not automatically submit applications or create financial transactions.

---

# 26. Document Integration

Funding-related documents may include:

- Funding Guidelines
- Applications
- Budgets
- Board Approvals
- Grant Agreements
- Sponsorship Agreements
- Donation Campaign Material
- Approval Letters
- Grant Reports
- Correspondence

All physical files remain under Document Service ownership.

---

# 27. Project Integration

Funding records may reference one or more projects.

Examples:

```text
Restoration Project

├── Grant Application
├── Foundation Award
├── Sponsor Agreement
└── Fundraising Campaign
```

Project ownership remains unchanged.

---

# 28. Accounting Integration

Accounting remains the authoritative source for:

- Grant Receipts
- Sponsorship Income
- Donations
- Project Expenses
- Co-Funding Transactions

The Funding Module may:

- Request accounting references
- Display approved financial information
- Compare planning values with actual accounting data
- Link funding records to accounting transactions

The Funding Module may not directly create journal entries.

---

# 29. Reporting

Standard reports include:

- Funding Pipeline
- Grant Application Status
- Grant Awards
- Sponsorship Portfolio
- Fundraising Campaigns
- Funding Commitments
- Reporting Deadlines
- Funding by Project
- Funding Source Overview
- Campaign Progress

Financial reports continue to originate from Accounting.

---

# 30. Security

Permissions include:

- View Funding
- Create Opportunities
- Create Applications
- Approve Applications
- Register Awards
- Manage Sponsors
- Manage Campaigns
- Manage Commitments
- Export Funding Data
- Archive Funding Records

Sensitive donor and sponsor information is restricted by role.

---

# 31. Audit

The following actions are audited:

- Opportunity Created
- Opportunity Assessed
- Application Created
- Application Submitted
- Application Approved
- Award Registered
- Sponsor Created
- Sponsorship Agreement Registered
- Campaign Created
- Campaign Approved
- Commitment Updated
- Funding Record Archived

Audit records remain immutable.

---

# 32. Data Validation

Examples:

- Funding Opportunity Number must be unique.
- Application Number must be unique.
- Campaign Number must be unique.
- Closing Date cannot precede Opening Date.
- Requested Amount cannot be negative.
- Target Amount cannot be negative.
- Related Project must exist where required.
- Responsible User must be active.
- Sponsorship Agreement dates must be valid.
- Reporting deadlines must be within the relevant funding period where applicable.

Business validation occurs in the Service Layer.

---

# 33. Board Governance

Where organizational policy requires board approval, the module shall support:

- Approval Request
- Review
- Decision
- Decision Date
- Decision Maker
- Decision Notes
- Supporting Documents

The approval record documents governance but does not replace formal meeting minutes or board records.

---

# 34. Transparency & Donor Stewardship

The module supports structured follow-up with funders and donors.

Examples:

- Thank-you communication
- Funding acknowledgement
- Sponsor deliverables
- Reporting submissions
- Renewal discussions
- Relationship history

The purpose is to improve continuity and accountability in funding relationships.

---

# 35. GDPR & Personal Data

Where donor or sponsor records contain personal data, the system shall support:

- Data Minimization
- Purpose Limitation
- Access Control
- Consent Records where required
- Retention Rules
- Auditability
- Controlled Export

The module shall not collect personal information that is not operationally required.

---

# 36. Future Enhancements

Future releases may support:

- Online Donation Forms
- Payment Provider Integration
- Crowdfunding Integration
- Automated Sponsor Renewals
- Funding Opportunity Web Monitoring
- AI-assisted Opportunity Matching
- Grant Application Templates
- Digital Signature Integration
- Donor Relationship Scoring
- Automated Funder Reporting Packages

External integrations remain optional and shall pass through controlled service interfaces.

---

# 37. Governance

The Advanced Grant, Fundraising & Sponsorship Module shall remain subordinate to the established MFM domain ownership model.

It shall never:

- Create a parallel financial ledger
- Store duplicate accounting balances
- Replace Project Management
- Replace Document Management
- Modify Accounting records directly
- Bypass Security or Audit services

This governance rule is mandatory.

---

# 38. Summary

The Advanced Grant, Fundraising & Sponsorship Management expansion provides a comprehensive funding-management environment for MFM v1.2.

It extends the existing Grants & Funding capabilities into a unified environment for:

- Grant Applications
- Funding Opportunities
- Sponsorships
- Fundraising Campaigns
- Donations
- Commitments
- Funding Relationships
- Reporting Obligations

The expansion is specifically designed to support the realities of small non-profit and maritime heritage organizations that rely on a combination of grants, sponsors, donations and volunteer contributions.

Most importantly, the expansion preserves the central MFM architectural principle:

> **Planning, funding administration and fundraising may reference and report financial information, but Accounting Core remains the only authoritative financial ledger.**

---

# Next Document

**MFM v1.2-350 – Advanced Document Intelligence, OCR & Digital Archive**

---

# END OF DOCUMENT
