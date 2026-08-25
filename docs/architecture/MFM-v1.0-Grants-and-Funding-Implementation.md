# MFM v1.0 GRANTS & FUNDING IMPLEMENTATION

## MaritimForeningsManager

**Version:** 1.0  
**Status:** Implementation Baseline  
**Architecture position:** Grants & Funding Layer  
**Predecessor:** MFM v1.0 Project & Budget Implementation

---

## Executive Summary

MFM v1.0 Grants & Funding provides a practical funding workflow for a small non-profit association. It connects funding opportunities, applications, awards, project funding, receipts, reporting obligations and accounting without creating a parallel financial ledger.

The core separation is:

```text
FUNDING PLANNING
      ↓
PROJECT FUNDING
      ↓
ACCOUNTING REALITY
```

The module SHALL remain understandable to volunteers, treasurers and board members.

---

# 1. Purpose
This document defines the concrete v1.0 implementation baseline for grants, public/private funding, applications, awards, funding commitments, receipts, project allocation, reporting obligations and accounting integration.

The module is deliberately designed for a small non-profit association. It is a funding-control layer, not a full grant-management enterprise platform.

## Implementation Record 1
**Object:** 1. Purpose
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 2. Governing Principle
> A funding record describes the external or internal financing commitment of a project; accounting remains the authoritative source for money actually received or spent.

The module SHALL connect funding planning with projects and accounting without creating a second financial ledger.

## Implementation Record 2
**Object:** 2. Governing Principle
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 3. Scope
Mandatory v1.0 capabilities:

```text
FUNDING SOURCES
FUNDERS
FUNDING OPPORTUNITIES
APPLICATIONS
AWARDS
COMMITMENTS
PAYMENT MILESTONES
RECEIPTS
PROJECT ALLOCATION
FUNDING CONDITIONS
DEADLINES
REPORTING OBLIGATIONS
FUNDING STATUS
ACCOUNTING LINKS
AUDIT
REPORTS
```

Out of scope for v1.0:

```text
automatic grant discovery
automatic application submission
bank API reconciliation
complex donor CRM
legal contract management
AI-controlled applications
```

## Implementation Record 3
**Object:** 3. Scope
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 4. Architecture Position
The grants module sits above the existing project and accounting layers:

```text
FUNDING OPPORTUNITY
        ↓
APPLICATION
        ↓
AWARD / COMMITMENT
        ↓
PROJECT FUNDING
        ↓
RECEIPT
        ↓
ACCOUNTING
        ↓
REPORTING
```

The module SHALL use ProjectService for project references and AccountingService for financial posting.

## Implementation Record 4
**Object:** 4. Architecture Position
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 5. Funding Source
A funding source identifies where financing originates.

Examples:

```text
FOUNDATION
PUBLIC_AUTHORITY
MUNICIPALITY
PRIVATE_DONOR
SPONSOR
MEMBER
ASSOCIATION_RESERVE
OTHER
```

Funding source types SHALL be configurable.

## Implementation Record 5
**Object:** 5. Funding Source
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 6. Funder
A funder is an organisation or party that may provide funding.

Minimum fields:

```text
id
name
source_type
contact_name
email
phone
address
active
created_at
updated_at
```

The system SHALL avoid storing unnecessary personal information.

## Implementation Record 6
**Object:** 6. Funder
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 7. Funding Opportunity
An opportunity represents a potential source of financing before an application is submitted.

Minimum:

```text
id
funder_id
name
deadline
status
description
website_or_reference
```

Recommended statuses:

```text
IDENTIFIED
ASSESSING
SUITABLE
NOT_SUITABLE
CLOSED
```

## Implementation Record 7
**Object:** 7. Funding Opportunity
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 8. Application
An application represents a concrete request for funding.

Minimum:

```text
id
funder_id
project_id
application_number
application_date
requested_amount_minor
status
decision_date
```

Recommended statuses:

```text
DRAFT
READY
SUBMITTED
UNDER_REVIEW
APPROVED
PARTIALLY_APPROVED
REJECTED
WITHDRAWN
CLOSED
```

## Implementation Record 8
**Object:** 8. Application
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 9. Application Principle
An application SHALL preserve the amount requested at submission.

Later changes SHALL be recorded as controlled amendments or new application versions.

The application record SHALL not be silently overwritten after submission.

## Implementation Record 9
**Object:** 9. Application Principle
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 10. Award
An award represents a funding decision.

Minimum:

```text
id
application_id
project_id
awarded_amount_minor
award_date
status
conditions
```

Statuses:

```text
OFFERED
ACCEPTED
DECLINED
ACTIVE
COMPLETED
CANCELLED
```

## Implementation Record 10
**Object:** 10. Award
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 11. Commitment
A commitment represents funding that the association can reasonably treat as committed according to its policy.

The system SHALL distinguish:

```text
REQUESTED
AWARDED
COMMITTED
RECEIVED
```

These are not interchangeable financial states.

## Implementation Record 11
**Object:** 11. Commitment
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 12. Funding Amounts
The module SHALL distinguish at least:

```text
requested_amount
awarded_amount
committed_amount
received_amount
spent_amount
remaining_amount
```

These values SHALL have clear definitions and SHALL not be manually duplicated when they can be derived.

## Implementation Record 12
**Object:** 12. Funding Amounts
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 13. Currency
v1.0 defaults to:

```text
DKK
```

The data model MAY retain currency codes for future multi-currency support.

Financial amounts SHALL use the same money representation as the accounting core.

## Implementation Record 13
**Object:** 13. Currency
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 14. Project Link
A funding application or award SHOULD reference a project when the funding is project-specific.

A funding record without a project MAY exist during early planning.

Once a project-specific award is accepted, the project link SHOULD normally be established.

## Implementation Record 14
**Object:** 14. Project Link
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 15. Project Funding Integration
The existing Project & Budget module remains authoritative for project-level funding summaries.

The grants module supplies detailed funding provenance:

```text
WHO
WHY
HOW MUCH
WHEN
UNDER WHICH CONDITIONS
```

The project module supplies the operational project view.

## Implementation Record 15
**Object:** 15. Project Funding Integration
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 16. Accounting Boundary
The grants module SHALL never directly insert accounting vouchers or voucher lines.

All actual money received SHALL pass through:

```text
AccountingService
```

The grants module may request a posting and retain the resulting accounting reference.

## Implementation Record 16
**Object:** 16. Accounting Boundary
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 17. Receipt
A receipt record represents funding actually received.

Minimum:

```text
id
award_id
project_id
receipt_date
amount_minor
payment_reference
status
accounting_voucher_id
```

A receipt is not considered financially completed until the accounting transaction is successfully posted where posting is required.

## Implementation Record 17
**Object:** 17. Receipt
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 18. Receipt Status
Recommended:

```text
EXPECTED
RECEIVED
POSTED
REVERSED
```

`RECEIVED` describes operational knowledge; `POSTED` confirms accounting integration.

## Implementation Record 18
**Object:** 18. Receipt Status
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 19. Partial Receipt
An award may be received in multiple instalments.

Example:

```text
Award = 100,000
Receipt 1 = 40,000
Receipt 2 = 60,000
```

The total received SHALL equal the sum of valid receipt records.

## Implementation Record 19
**Object:** 19. Partial Receipt
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 20. Over-Receipt
A receipt that causes received funding to exceed the relevant committed or awarded amount SHALL trigger a warning or controlled rejection according to configuration.

The system SHALL never silently hide the difference.

## Implementation Record 20
**Object:** 20. Over-Receipt
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 21. Funding Milestones
Some awards are paid against milestones.

A milestone MAY contain:

```text
id
award_id
description
due_date
expected_amount_minor
status
received_amount_minor
```

Statuses:

```text
PLANNED
READY
SUBMITTED
APPROVED
PAID
CANCELLED
```

## Implementation Record 21
**Object:** 21. Funding Milestones
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 22. Funding Conditions
Funding conditions are requirements attached to an award.

Examples:

```text
co-financing required
completion report
specific spending categories
deadline
documentation
public acknowledgement
```

v1.0 stores conditions as structured notes and deadlines; a full contract-management engine is out of scope.

## Implementation Record 22
**Object:** 22. Funding Conditions
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 23. Co-Financing
A funding source may require own contribution.

Example:

```text
Project budget = 200,000
Grant = 150,000
Own contribution = 50,000
```

The system SHOULD show the co-financing gap clearly.

## Implementation Record 23
**Object:** 23. Co-Financing
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 24. Co-Financing Calculation
Basic calculation:

```text
required_total
-
external_funding
=
own_contribution
```

The result is planning information and does not itself create an accounting transaction.

## Implementation Record 24
**Object:** 24. Co-Financing Calculation
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 25. Funding Coverage
Funding coverage:

```text
confirmed funding / project budget × 100
```

If the budget is zero, display:

```text
N/A
```

and never divide by zero.

## Implementation Record 25
**Object:** 25. Funding Coverage
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 26. Funding Gap
Funding gap:

```text
project budget
-
confirmed funding
```

A negative result indicates funding above the current planned budget and SHALL be shown explicitly.

## Implementation Record 26
**Object:** 26. Funding Gap
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 27. Deadline Management
Applications and reporting obligations SHALL support dates.

The module SHOULD provide:

```text
application deadline
decision date
award start
award end
receipt deadline
report deadline
```

## Implementation Record 27
**Object:** 27. Deadline Management
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 28. Deadline Status
Recommended derived states:

```text
UPCOMING
DUE_SOON
OVERDUE
COMPLETED
CANCELLED
```

Derived status SHALL not overwrite the underlying obligation state.

## Implementation Record 28
**Object:** 28. Deadline Status
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 29. Reminder Principle
The system MAY highlight upcoming deadlines.

v1.0 SHALL not automatically submit applications or reports.

Human confirmation remains mandatory.

## Implementation Record 29
**Object:** 29. Reminder Principle
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 30. Reporting Obligation
An award may require one or more reports.

Minimum:

```text
id
award_id
name
due_date
status
description
document_id
submitted_date
```

Statuses:

```text
PLANNED
IN_PROGRESS
READY
SUBMITTED
ACCEPTED
OVERDUE
WAIVED
```

## Implementation Record 30
**Object:** 30. Reporting Obligation
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 31. Reporting Evidence
A report obligation MAY link to a document.

The grant module stores the reference; the document module stores the physical file.

## Implementation Record 31
**Object:** 31. Reporting Evidence
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 32. Document Boundary
Do not duplicate files inside the grants module.

Use:

```text
document_id
```

or the existing document reference mechanism.

## Implementation Record 32
**Object:** 32. Document Boundary
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 33. Application Documents
Typical linked documents:

```text
application
budget
quotes
project description
board decision
award letter
conditions
progress report
final report
```

The document module remains authoritative for files.

## Implementation Record 33
**Object:** 33. Application Documents
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 34. Application Approval
Submission of an application SHALL require appropriate authority.

Recommended permission:

```text
SUBMIT_FUNDING_APPLICATION
```

Draft preparation does not require submission authority.

## Implementation Record 34
**Object:** 34. Application Approval
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 35. Award Acceptance
Accepting an award is a governance action.

Recommended permission:

```text
ACCEPT_FUNDING_AWARD
```

The action SHALL be audited.

## Implementation Record 35
**Object:** 35. Award Acceptance
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 36. Funding Roles
Recommended permissions:

```text
VIEW_FUNDING
CREATE_FUNDING
EDIT_FUNDING
SUBMIT_FUNDING_APPLICATION
ACCEPT_FUNDING_AWARD
REGISTER_FUNDING_RECEIPT
MANAGE_FUNDING_REPORTS
EXPORT_FUNDING_REPORTS
```

A treasurer or board member may receive only the permissions appropriate to the association's policy.

## Implementation Record 36
**Object:** 36. Funding Roles
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 37. Separation of Duties
The person preparing an application need not be the person approving its submission.

The person registering a receipt need not have permission to alter the underlying award.

The system SHALL support separation without forcing a complex enterprise workflow.

## Implementation Record 37
**Object:** 37. Separation of Duties
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 38. Funding GUI
Minimum screens:

```text
Funding Dashboard
Funder Register
Opportunity Register
Application List
Application Detail
Award Detail
Receipt Register
Reporting Obligations
Funding Reports
```

## Implementation Record 38
**Object:** 38. Funding GUI
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 39. Funding Dashboard
Recommended indicators:

```text
active applications
applications awaiting decision
awards active
awarded amount
received amount
funding gap
upcoming deadlines
overdue reports
```

## Implementation Record 39
**Object:** 39. Funding Dashboard
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 40. Funder Register
Search by:

```text
name
type
active
```

The register SHALL support deactivation without deleting historical relationships.

## Implementation Record 40
**Object:** 40. Funder Register
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 41. Opportunity Register
Show:

```text
funder
opportunity
deadline
status
estimated amount
suitability
```

This is an internal planning tool.

## Implementation Record 41
**Object:** 41. Opportunity Register
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 42. Application Detail
Show:

```text
funder
project
requested amount
application date
status
decision
documents
conditions
history
```

## Implementation Record 42
**Object:** 42. Application Detail
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 43. Award Detail
Show:

```text
application
project
awarded amount
conditions
milestones
receipts
reporting obligations
accounting references
```

## Implementation Record 43
**Object:** 43. Award Detail
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 44. Receipt Entry
Receipt form:

```text
award
project
date
amount
reference
payment method
```

Validation SHALL occur before financial posting.

## Implementation Record 44
**Object:** 44. Receipt Entry
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 45. Receipt Accounting Flow
```text
Receipt Entry
   ↓
Validate
   ↓
Authorise
   ↓
AccountingService
   ↓
Voucher Posted
   ↓
Receipt = POSTED
   ↓
Audit
```

## Implementation Record 45
**Object:** 45. Receipt Accounting Flow
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 46. Accounting Example
A grant receipt may result in:

```text
Debit Bank
Credit Grant Income
```

The actual accounts SHALL come from configured accounting mappings.

No account numbers shall be hard-coded.

## Implementation Record 46
**Object:** 46. Accounting Example
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 47. Deferred/Restricted Funding Boundary
Some funding may have accounting treatment different from ordinary income.

MFM v1.0 SHALL permit the configured accounting policy to determine the posting.

The grants module SHALL not invent accounting treatment.

## Implementation Record 47
**Object:** 47. Deferred/Restricted Funding Boundary
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 48. Restricted Funding
A funding award may be operationally restricted to a project or purpose.

The restriction SHALL be represented in the funding record.

Actual accounting classification remains an accounting policy decision.

## Implementation Record 48
**Object:** 48. Restricted Funding
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 49. Funding Allocation
A receipt may be allocated to one project.

If one receipt covers multiple projects, the application MAY support controlled allocation lines.

For a small association, single-project receipts are preferred where possible.

## Implementation Record 49
**Object:** 49. Funding Allocation
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 50. Multi-Project Receipt
Optional allocation table:

```text
funding_receipt_allocations
receipt_id
project_id
amount_minor
```

The allocation total SHALL equal the receipt amount.

## Implementation Record 50
**Object:** 50. Multi-Project Receipt
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 51. Funding Allocation Validation
Reject:

```text
allocation < 0
allocation total > receipt
unknown project
closed project without authorised reopening
```

## Implementation Record 51
**Object:** 51. Funding Allocation Validation
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 52. Accounting Reference
Once a receipt is posted, store:

```text
accounting_voucher_id
```

This provides traceability from:

```text
award → receipt → voucher
```

## Implementation Record 52
**Object:** 52. Accounting Reference
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 53. Reversal
A reversed receipt SHALL preserve the original receipt.

Do not delete it.

A controlled reversal or accounting correction SHALL be recorded.

## Implementation Record 53
**Object:** 53. Reversal
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 54. Reversal Permission
Recommended:

```text
REVERSE_FUNDING_RECEIPT
```

The action requires audit and, where appropriate, treasurer authority.

## Implementation Record 54
**Object:** 54. Reversal Permission
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 55. Funding Status Model
At the overall funding level:

```text
PLANNED
APPLIED
AWARDED
COMMITTED
PARTIALLY_RECEIVED
RECEIVED
COMPLETED
CANCELLED
```

Status transitions SHALL be validated.

## Implementation Record 55
**Object:** 55. Funding Status Model
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 56. Status Transitions
Baseline:

```text
PLANNED → APPLIED
APPLIED → AWARDED
APPLIED → REJECTED
AWARDED → COMMITTED
COMMITTED → PARTIALLY_RECEIVED
COMMITTED → RECEIVED
RECEIVED → COMPLETED
```

Cancellation is permitted only through controlled transitions.

## Implementation Record 56
**Object:** 56. Status Transitions
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 57. Invalid Transition
The service SHALL reject invalid transitions and explain the reason in user-friendly language.

## Implementation Record 57
**Object:** 57. Invalid Transition
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 58. Funding History
Material events SHALL remain visible:

```text
application submitted
award received
award accepted
receipt registered
receipt posted
report submitted
award completed
```

## Implementation Record 58
**Object:** 58. Funding History
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 59. Audit Events
Minimum:

```text
FUNDER_CREATED
FUNDER_UPDATED
OPPORTUNITY_CREATED
APPLICATION_CREATED
APPLICATION_SUBMITTED
APPLICATION_DECIDED
AWARD_CREATED
AWARD_ACCEPTED
FUNDING_RECEIPT_CREATED
FUNDING_RECEIPT_POSTED
FUNDING_RECEIPT_REVERSED
REPORT_OBLIGATION_CREATED
REPORT_SUBMITTED
FUNDING_STATUS_CHANGED
FUNDING_REPORT_EXPORTED
```

## Implementation Record 59
**Object:** 59. Audit Events
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 60. Database Tables
Recommended:

```text
funders
funding_opportunities
funding_applications
funding_awards
funding_milestones
funding_receipts
funding_receipt_allocations
funding_reporting_obligations
```

## Implementation Record 60
**Object:** 60. Database Tables
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 61. Funders Table
```text
id
name
source_type
contact_name
email
phone
address
active
created_at
updated_at
```

## Implementation Record 61
**Object:** 61. Funders Table
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 62. Opportunities Table
```text
id
funder_id
name
description
deadline
estimated_amount_minor
status
reference
created_at
updated_at
```

## Implementation Record 62
**Object:** 62. Opportunities Table
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 63. Applications Table
```text
id
application_number
funder_id
project_id
opportunity_id
application_date
requested_amount_minor
status
decision_date
decision_amount_minor
description
created_at
updated_at
```

## Implementation Record 63
**Object:** 63. Applications Table
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 64. Awards Table
```text
id
application_id
project_id
award_date
awarded_amount_minor
committed_amount_minor
status
conditions
start_date
end_date
created_at
updated_at
```

## Implementation Record 64
**Object:** 64. Awards Table
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 65. Milestones Table
```text
id
award_id
description
due_date
expected_amount_minor
status
created_at
updated_at
```

## Implementation Record 65
**Object:** 65. Milestones Table
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 66. Receipts Table
```text
id
award_id
project_id
receipt_date
amount_minor
payment_method
payment_reference
status
accounting_voucher_id
created_at
updated_at
```

## Implementation Record 66
**Object:** 66. Receipts Table
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 67. Receipt Allocations Table
```text
id
receipt_id
project_id
amount_minor
created_at
```

## Implementation Record 67
**Object:** 67. Receipt Allocations Table
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 68. Reporting Obligations Table
```text
id
award_id
name
description
due_date
status
document_id
submitted_date
created_at
updated_at
```

## Implementation Record 68
**Object:** 68. Reporting Obligations Table
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 69. Foreign Keys
Enforce:

```text
funding_opportunities.funder_id → funders.id
applications.funder_id → funders.id
applications.project_id → projects.id
applications.opportunity_id → funding_opportunities.id
awards.application_id → funding_applications.id
awards.project_id → projects.id
milestones.award_id → awards.id
receipts.award_id → awards.id
receipts.project_id → projects.id
receipt_allocations.receipt_id → receipts.id
receipt_allocations.project_id → projects.id
reporting_obligations.award_id → awards.id
```

## Implementation Record 69
**Object:** 69. Foreign Keys
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 70. Indexes
Recommended:

```text
funders.name
opportunities.deadline
applications.application_number
applications.status
applications.project_id
awards.project_id
awards.status
receipts.award_id
receipts.receipt_date
reporting_obligations.due_date
reporting_obligations.status
```

## Implementation Record 70
**Object:** 70. Indexes
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 71. Unique Constraints
Recommended:

```text
application_number UNIQUE
```

Funder names should not necessarily be unique because duplicate names may legitimately exist across jurisdictions or entities.

## Implementation Record 71
**Object:** 71. Unique Constraints
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 72. Application Number
Application numbers SHALL be generated by the service layer.

Example:

```text
F-2026-001
F-2026-002
```

Once submitted, the application number SHALL remain stable.

## Implementation Record 72
**Object:** 72. Application Number
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 73. Funding Service
Recommended API:

```text
create_funder()
create_opportunity()
create_application()
submit_application()
record_decision()
create_award()
accept_award()
update_award()
```

## Implementation Record 73
**Object:** 73. Funding Service
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 74. Receipt Service
Recommended API:

```text
register_receipt()
post_receipt()
reverse_receipt()
get_award_balance()
get_project_funding()
```

## Implementation Record 74
**Object:** 74. Receipt Service
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 75. Reporting Service
Recommended:

```text
create_reporting_obligation()
update_reporting_status()
mark_submitted()
list_due()
list_overdue()
```

## Implementation Record 75
**Object:** 75. Reporting Service
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 76. Funding Finance Service
Read-oriented calculations:

```text
get_requested_total()
get_awarded_total()
get_committed_total()
get_received_total()
get_remaining_award()
get_project_funding_gap()
```

## Implementation Record 76
**Object:** 76. Funding Finance Service
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 77. Derived Totals
Totals SHOULD be derived from authoritative records.

Do not allow users to manually edit:

```text
received_total
remaining_total
```

when these can be calculated from receipts.

## Implementation Record 77
**Object:** 77. Derived Totals
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 78. Award Remaining
Basic calculation:

```text
awarded amount
-
valid posted receipts
=
remaining award
```

Reversed receipts are excluded.

## Implementation Record 78
**Object:** 78. Award Remaining
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 79. Committed Remaining
Where commitment is distinct:

```text
committed amount
-
valid receipts
=
unreceived committed funding
```

## Implementation Record 79
**Object:** 79. Committed Remaining
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 80. Application Success
A report MAY calculate:

```text
approved applications / decided applications
```

Only completed decisions should enter the denominator.

## Implementation Record 80
**Object:** 80. Application Success
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 81. Funding Pipeline
The dashboard MAY show:

```text
requested
probability-adjusted optional forecast
awarded
committed
received
```

Probability-adjusted values are planning estimates and SHALL never enter accounting.

## Implementation Record 81
**Object:** 81. Funding Pipeline
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 82. Pipeline Forecast
A simple optional forecast:

```text
requested amount × configured probability
```

This is advisory only.

## Implementation Record 82
**Object:** 82. Pipeline Forecast
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 83. Probability Governance
Probability values SHALL be user-configured or explicitly entered.

AI may suggest a probability but SHALL not silently change it.

## Implementation Record 83
**Object:** 83. Probability Governance
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 84. Funding Risk
Funding risk indicators may include:

```text
deadline risk
decision risk
funding gap
condition risk
reporting risk
receipt delay
```

These are informational.

## Implementation Record 84
**Object:** 84. Funding Risk
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 85. Funding Health
Optional:

```text
GREEN
AMBER
RED
```

based on configured rules.

Health SHALL not automatically change funding status.

## Implementation Record 85
**Object:** 85. Funding Health
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 86. Funding Conditions
A condition may include:

```text
name
description
due_date
status
evidence_document_id
```

For v1.0, a simple condition table is sufficient if needed.

## Implementation Record 86
**Object:** 86. Funding Conditions
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 87. Condition Compliance
Statuses:

```text
OPEN
IN_PROGRESS
FULFILLED
WAIVED
OVERDUE
```

A condition marked fulfilled SHOULD have evidence where appropriate.

## Implementation Record 87
**Object:** 87. Condition Compliance
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 88. Grant Reporting
The module SHOULD provide a report obligation list sorted by:

```text
due date
status
project
funder
```

## Implementation Record 88
**Object:** 88. Grant Reporting
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 89. Final Report
At award completion, the system MAY show a checklist:

```text
funding received
project actuals reconciled
report submitted
conditions fulfilled
documents linked
```

## Implementation Record 89
**Object:** 89. Final Report
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 90. Award Closure
Closing an award SHALL not delete:

```text
application
award
receipts
reports
audit
```

It merely marks the funding relationship complete.

## Implementation Record 90
**Object:** 90. Award Closure
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 91. Application Rejection
A rejected application remains historical.

Record:

```text
decision date
decision status
decision note
```

The request amount remains available for reporting.

## Implementation Record 91
**Object:** 91. Application Rejection
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 92. Partial Approval
If requested:

```text
100,000
```

and awarded:

```text
70,000
```

the system SHALL preserve both values.

## Implementation Record 92
**Object:** 92. Partial Approval
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 93. Application Amendment
Material application changes after submission SHOULD be versioned.

At minimum record:

```text
old value
new value
reason
actor
timestamp
```

## Implementation Record 93
**Object:** 93. Application Amendment
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 94. Award Amendment
Changes to an active award SHALL be controlled.

Examples:

```text
amount change
period change
condition change
project change
```

All material changes SHALL be audited.

## Implementation Record 94
**Object:** 94. Award Amendment
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 95. Project Change
Moving an award from one project to another is a material action.

It SHALL require explicit authority and audit.

## Implementation Record 95
**Object:** 95. Project Change
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 96. Project Closure Check
A project should not be closed while active funding obligations remain without a warning.

The user may proceed only under the association's configured policy.

## Implementation Record 96
**Object:** 96. Project Closure Check
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 97. Funding and Budget Integration
Project budget provides:

```text
planned cost
```

Funding provides:

```text
planned/confirmed financing
```

Together they support:

```text
funding gap
```

## Implementation Record 97
**Object:** 97. Funding and Budget Integration
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 98. Funding vs Actual
The project report may compare:

```text
budget
confirmed funding
received funding
actual expense
```

This is a planning and reporting view.

## Implementation Record 98
**Object:** 98. Funding vs Actual
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 99. Funding Sustainability
A project can be:

```text
fully funded
partially funded
unfunded
```

based on confirmed funding versus budget.

## Implementation Record 99
**Object:** 99. Funding Sustainability
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 100. Funding Safety Rule
The system SHALL not assume that an application will be approved.

Only awarded/committed values enter confirmed funding calculations.

## Implementation Record 100
**Object:** 100. Funding Safety Rule
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 101. Requested vs Confirmed
Requested funding SHALL be clearly separated from confirmed funding in all reports.

## Implementation Record 101
**Object:** 101. Requested vs Confirmed
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 102. Received vs Confirmed
A project may have:

```text
confirmed = 100,000
received = 40,000
```

The remaining 60,000 is expected but not yet cash received.

## Implementation Record 102
**Object:** 102. Received vs Confirmed
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 103. Cash Visibility
Treasurer views should distinguish:

```text
committed funding
cash received
```

This supports liquidity awareness without duplicating the cash ledger.

## Implementation Record 103
**Object:** 103. Cash Visibility
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 104. Accounting Integration Test
For a posted receipt:

```text
grant receipt
=
accounting transaction
=
project funding received
```

All three references SHALL remain traceable.

## Implementation Record 104
**Object:** 104. Accounting Integration Test
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 105. Accounting Failure
If posting fails:

```text
receipt SHALL NOT become POSTED
```

The transaction SHALL be rolled back or remain clearly uncommitted.

## Implementation Record 105
**Object:** 105. Accounting Failure
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 106. Retry Safety
Retrying a receipt post SHALL not create duplicate accounting vouchers.

Use existing accounting references and idempotency checks.

## Implementation Record 106
**Object:** 106. Retry Safety
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 107. Reconciliation
Funding reconciliation SHALL compare:

```text
award totals
+
receipt totals
+
accounting postings
```

and identify discrepancies.

## Implementation Record 107
**Object:** 107. Reconciliation
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 108. Reconciliation Status
Recommended:

```text
RECONCILED
WARNING
ERROR
```

An ERROR status should prevent unsafe automatic financial actions.

## Implementation Record 108
**Object:** 108. Reconciliation Status
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 109. Reconciliation Report
Show:

```text
award
awarded
received records
accounting posted
difference
status
```

## Implementation Record 109
**Object:** 109. Reconciliation Report
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 110. Negative Test — Duplicate Application
Attempt to create the same application number twice.

Expected:

```text
REJECTED
```

## Implementation Record 110
**Object:** 110. Negative Test — Duplicate Application
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 111. Negative Test — Receipt Too Large
Award:

```text
100,000
```

Receipt:

```text
120,000
```

Expected:

```text
warning or controlled rejection
```

No silent overstatement of award receipt.

## Implementation Record 111
**Object:** 111. Negative Test — Receipt Too Large
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 112. Negative Test — Invalid Receipt
Receipt with:

```text
amount <= 0
```

Expected:

```text
REJECTED
```

## Implementation Record 112
**Object:** 112. Negative Test — Invalid Receipt
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 113. Negative Test — Missing Project
Project-specific award without a valid project reference SHALL be rejected where the policy requires project linkage.

## Implementation Record 113
**Object:** 113. Negative Test — Missing Project
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 114. Negative Test — Unauthorised Submission
User without `SUBMIT_FUNDING_APPLICATION` attempts submission.

Expected:

```text
DENIED
```

## Implementation Record 114
**Object:** 114. Negative Test — Unauthorised Submission
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 115. Negative Test — Unauthorised Acceptance
User without `ACCEPT_FUNDING_AWARD` attempts acceptance.

Expected:

```text
DENIED
```

## Implementation Record 115
**Object:** 115. Negative Test — Unauthorised Acceptance
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 116. Negative Test — Accounting Failure
Receipt registration succeeds only if the financial transaction completes according to the configured accounting policy.

A failed posting SHALL not be reported as posted.

## Implementation Record 116
**Object:** 116. Negative Test — Accounting Failure
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 117. Negative Test — Duplicate Posting
Repeat the same posting request.

Expected:

```text
one accounting transaction
one posted receipt
```

## Implementation Record 117
**Object:** 117. Negative Test — Duplicate Posting
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 118. Negative Test — Closed Award
Attempt new receipt on a closed award.

Expected:

```text
REJECTED
```

unless a controlled reopening is performed.

## Implementation Record 118
**Object:** 118. Negative Test — Closed Award
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 119. Negative Test — Closed Project
Attempt to allocate a new project receipt to a closed project.

Expected:

```text
REJECTED
```

unless authorised reopening is performed.

## Implementation Record 119
**Object:** 119. Negative Test — Closed Project
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 120. Negative Test — Missing Report
Close an award with an overdue mandatory report.

Expected:

```text
warning
```

or controlled rejection according to configuration.

## Implementation Record 120
**Object:** 120. Negative Test — Missing Report
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 121. Scenario 1 — Successful Grant
```text
Opportunity
 ↓
Application 100,000
 ↓
Award 100,000
 ↓
Receipt 100,000
 ↓
Accounting
 ↓
Project funding 100,000
```

Expected:

```text
received = 100,000
remaining award = 0
reconciled = true
```

## Implementation Record 121
**Object:** 121. Scenario 1 — Successful Grant
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 122. Scenario 2 — Partial Grant
```text
Award = 100,000
Receipt = 40,000
```

Expected:

```text
received = 40,000
remaining = 60,000
status = PARTIALLY_RECEIVED
```

## Implementation Record 122
**Object:** 122. Scenario 2 — Partial Grant
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 123. Scenario 3 — Multiple Instalments
```text
Award = 100,000
Receipt 1 = 30,000
Receipt 2 = 30,000
Receipt 3 = 40,000
```

Expected:

```text
received = 100,000
remaining = 0
```

## Implementation Record 123
**Object:** 123. Scenario 3 — Multiple Instalments
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 124. Scenario 4 — Partial Approval
```text
Requested = 150,000
Awarded = 100,000
```

Expected:

```text
requested remains 150,000
confirmed award = 100,000
```

## Implementation Record 124
**Object:** 124. Scenario 4 — Partial Approval
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 125. Scenario 5 — Funding Gap
```text
Project budget = 200,000
Confirmed funding = 150,000
```

Expected:

```text
funding gap = 50,000
```

## Implementation Record 125
**Object:** 125. Scenario 5 — Funding Gap
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 126. Scenario 6 — Reporting Obligation
```text
Award accepted
 ↓
Create final report obligation
 ↓
Attach document
 ↓
Submit
 ↓
Mark accepted
```

Expected full history and audit.

## Implementation Record 126
**Object:** 126. Scenario 6 — Reporting Obligation
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 127. Scenario 7 — Rejected Application
Application is rejected.

Expected:

```text
application retained
decision recorded
no award created
no confirmed funding
```

## Implementation Record 127
**Object:** 127. Scenario 7 — Rejected Application
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 128. Scenario 8 — Award Reversal
A posted receipt is reversed.

Expected:

```text
original receipt retained
reversal recorded
accounting correction exists
received total recalculated
```

## Implementation Record 128
**Object:** 128. Scenario 8 — Award Reversal
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 129. Scenario 9 — Project Integration
```text
Award 80,000
Project budget 100,000
Receipt 50,000
```

Expected:

```text
project confirmed funding = 80,000
project received funding = 50,000
funding gap = 20,000
cash received = 50,000
```

## Implementation Record 129
**Object:** 129. Scenario 9 — Project Integration
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 130. Scenario 10 — Audit
Create application, submit, award, receive payment and close.

Expected audit chain:

```text
APPLICATION_CREATED
APPLICATION_SUBMITTED
AWARD_CREATED
AWARD_ACCEPTED
FUNDING_RECEIPT_CREATED
FUNDING_RECEIPT_POSTED
AWARD_COMPLETED
```

## Implementation Record 130
**Object:** 130. Scenario 10 — Audit
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 131. Security
The grants module SHALL use the existing authentication and SecurityContext.

No grant operation may bypass the service-level permission check.

## Implementation Record 131
**Object:** 131. Security
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 132. Export Security
Funding exports may contain:

```text
funder data
application amounts
project data
bank/payment references
```

Therefore export permission is mandatory.

## Implementation Record 132
**Object:** 132. Export Security
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 133. Export Audit
Material funding exports SHOULD generate:

```text
FUNDING_REPORT_EXPORTED
```

with actor, timestamp and scope.

## Implementation Record 133
**Object:** 133. Export Audit
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 134. Privacy
Funder contact data may be personal data.

The system SHALL minimise storage and restrict access appropriately.

## Implementation Record 134
**Object:** 134. Privacy
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 135. No Sensitive Payment Data
Do not store:

```text
card numbers
bank login credentials
security codes
```

The module only stores references needed for reconciliation.

## Implementation Record 135
**Object:** 135. No Sensitive Payment Data
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 136. Backup
Funding data SHALL be included in normal MFM backups.

## Implementation Record 136
**Object:** 136. Backup
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 137. Restore
Restore verification SHALL confirm:

```text
funders
applications
awards
receipts
reports
project links
accounting references
audit
```

## Implementation Record 137
**Object:** 137. Restore
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 138. Migration
Schema migrations SHALL preserve identifiers and financial references.

## Implementation Record 138
**Object:** 138. Migration
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 139. Import
CSV/XLSX import is optional.

If implemented, it SHALL follow:

```text
preview
validate
confirm
commit
audit
```

## Implementation Record 139
**Object:** 139. Import
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 140. No Direct SQL
Administrators SHALL not need to edit grant tables manually.

## Implementation Record 140
**Object:** 140. No Direct SQL
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 141. Repository Layer
Recommended:

```text
FunderRepository
FundingOpportunityRepository
FundingApplicationRepository
FundingAwardRepository
FundingReceiptRepository
FundingReportingRepository
```

## Implementation Record 141
**Object:** 141. Repository Layer
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 142. Service Layer
Recommended:

```text
FundingService
FundingReceiptService
FundingReportingService
FundingFinanceService
```

## Implementation Record 142
**Object:** 142. Service Layer
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 143. Dependency Structure
```text
GUI
 ↓
FundingService
 ↓
Repositories
 ↓
Database

FundingReceiptService
 ↓
AccountingService
 ↓
AuditService
```

## Implementation Record 143
**Object:** 143. Dependency Structure
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 144. Circular Dependency Avoidance
AccountingService SHALL not depend on FundingService.

The direction remains:

```text
Funding → Accounting
```

## Implementation Record 144
**Object:** 144. Circular Dependency Avoidance
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 145. Transaction Boundary
Receipt posting SHALL be atomic with the related grant receipt state wherever supported by the database architecture.

## Implementation Record 145
**Object:** 145. Transaction Boundary
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 146. Receipt Transaction
```text
BEGIN
 ↓
validate award
 ↓
validate receipt
 ↓
create receipt
 ↓
post accounting
 ↓
store voucher reference
 ↓
audit
 ↓
COMMIT
```

## Implementation Record 146
**Object:** 146. Receipt Transaction
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 147. Receipt Failure
If accounting or audit fails:

```text
ROLLBACK
```

No receipt should appear as successfully posted.

## Implementation Record 147
**Object:** 147. Receipt Failure
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 148. Reporting Transaction
Changing a reporting obligation status SHALL be transactional and audited.

## Implementation Record 148
**Object:** 148. Reporting Transaction
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 149. Application Submission Transaction
Submission SHALL:

```text
validate
 ↓
change status
 ↓
record submission date
 ↓
audit
 ↓
commit
```

## Implementation Record 149
**Object:** 149. Application Submission Transaction
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 150. Award Acceptance Transaction
Acceptance SHALL:

```text
validate
 ↓
change status
 ↓
create/update project funding relationship
 ↓
audit
 ↓
commit
```

## Implementation Record 150
**Object:** 150. Award Acceptance Transaction
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 151. Award Acceptance Safety
Acceptance SHALL not create cash or accounting entries merely because an award was accepted.

Only actual financial events create financial postings.

## Implementation Record 151
**Object:** 151. Award Acceptance Safety
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 152. Funding Forecast
Forecast may distinguish:

```text
requested
probability-adjusted
awarded
committed
received
```

The forecast is non-financial ledger data.

## Implementation Record 152
**Object:** 152. Funding Forecast
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 153. AI Boundary
AI MAY:

```text
identify suitable opportunities
summarise funder requirements
draft application outlines
detect deadline risk
forecast funding gaps
identify reporting obligations
```

AI SHALL NOT:

```text
submit applications
accept awards
change funding commitments
post receipts
reverse payments
```

without explicit authorised human action.

## Implementation Record 153
**Object:** 153. AI Boundary
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 154. AI Workflow
```text
INTELLIGENCE
 ↓
RECOMMENDATION
 ↓
HUMAN REVIEW
 ↓
AUTHORISATION
 ↓
EXECUTION
```

## Implementation Record 154
**Object:** 154. AI Workflow
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 155. Autonomous Safety
Any future automation SHALL stop when:

```text
funding identity is uncertain
accounting mapping is missing
award amount conflicts
project is closed
authorisation is missing
reconciliation fails
```

## Implementation Record 155
**Object:** 155. Autonomous Safety
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 156. Funding Circuit Breaker
If a funding receipt cannot be reconciled with its award and accounting record, automatic processing SHALL stop.

## Implementation Record 156
**Object:** 156. Funding Circuit Breaker
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 157. Safe State
In a funding integrity failure:

```text
read-only reporting
+
diagnostics
```

may continue, while financial writes are blocked.

## Implementation Record 157
**Object:** 157. Safe State
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 158. Recovery
Recovery SHALL verify:

```text
award
receipt
accounting voucher
project funding
audit
```

before retrying.

## Implementation Record 158
**Object:** 158. Recovery
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 159. Idempotency
Operations such as:

```text
submit_application
accept_award
post_receipt
submit_report
```

must be safe against repeated user actions.

## Implementation Record 159
**Object:** 159. Idempotency
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 160. No Duplicate Receipt
A receipt with an existing accounting voucher reference SHALL not be posted again.

## Implementation Record 160
**Object:** 160. No Duplicate Receipt
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 161. Project Funding Reconciliation
For each project:

```text
confirmed grant funding
=
sum active awards linked to project
```

subject to approved adjustments.

## Implementation Record 161
**Object:** 161. Project Funding Reconciliation
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 162. Received Funding Reconciliation
For each project:

```text
received funding
=
sum valid posted funding receipts
```

## Implementation Record 162
**Object:** 162. Received Funding Reconciliation
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 163. Accounting Reconciliation
For each posted receipt:

```text
grant receipt amount
=
accounting transaction amount
```

unless an explicitly configured multi-line accounting treatment applies.

## Implementation Record 163
**Object:** 163. Accounting Reconciliation
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 164. Funding Report
Minimum report:

```text
Funder
Application
Award
Project
Awarded
Received
Remaining
Status
```

## Implementation Record 164
**Object:** 164. Funding Report
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 165. Application Pipeline Report
Show:

```text
draft
submitted
under review
approved
rejected
requested amount
awarded amount
```

## Implementation Record 165
**Object:** 165. Application Pipeline Report
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 166. Deadline Report
Show:

```text
deadline
days remaining
project
funder
status
```

## Implementation Record 166
**Object:** 166. Deadline Report
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 167. Reporting Obligation Report
Show:

```text
report
award
project
due date
status
document
```

## Implementation Record 167
**Object:** 167. Reporting Obligation Report
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 168. Funding Reconciliation Report
Show:

```text
award
awarded
received
accounting
difference
status
```

## Implementation Record 168
**Object:** 168. Funding Reconciliation Report
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 169. Project Funding Summary
Show:

```text
project budget
confirmed funding
received funding
funding gap
```

This report should use the project module as the presentation layer where practical.

## Implementation Record 169
**Object:** 169. Project Funding Summary
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 170. Board Funding Summary
A board-level report SHOULD show:

```text
applications
awards
total awarded
total received
projects at funding risk
upcoming deadlines
```

without exposing unnecessary personal data.

## Implementation Record 170
**Object:** 170. Board Funding Summary
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 171. Treasurer Funding Summary
The treasurer may require:

```text
receipts
accounting vouchers
bank references
reconciliation
```

## Implementation Record 171
**Object:** 171. Treasurer Funding Summary
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 172. Project Manager Funding Summary
The project manager may require:

```text
confirmed funding
received funding
funding gap
conditions
deadlines
```

without unrestricted accounting administration.

## Implementation Record 172
**Object:** 172. Project Manager Funding Summary
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 173. Funding Dashboard Simplicity
The dashboard SHALL remain usable by volunteers and board members.

Avoid enterprise-style workflow complexity unless it has a concrete association use case.

## Implementation Record 173
**Object:** 173. Funding Dashboard Simplicity
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 174. Configuration
Configuration MAY include:

```text
application_number_prefix
deadline_warning_days
funding_warning_threshold
default_currency
```

## Implementation Record 174
**Object:** 174. Configuration
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 175. No Hard-Coded Funding Policy
Do not hard-code:

```text
maximum grant size
approval threshold
required co-financing
```

These are association policy/configuration.

## Implementation Record 175
**Object:** 175. No Hard-Coded Funding Policy
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 176. Approval Thresholds
A future configuration may require board approval above a specified amount.

The grants module SHALL not assume a universal threshold.

## Implementation Record 176
**Object:** 176. Approval Thresholds
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 177. Funding Governance
The association decides:

```text
who may apply
who may submit
who may accept
who may register receipts
who may reverse receipts
```

MFM enforces the resulting permissions.

## Implementation Record 177
**Object:** 177. Funding Governance
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 178. Board Decision Reference
An application or award MAY reference a board decision or meeting record through the document/reference layer.

## Implementation Record 178
**Object:** 178. Board Decision Reference
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 179. No Governance by Software
MFM shall support governance but shall not invent the association's authority structure.

## Implementation Record 179
**Object:** 179. No Governance by Software
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 180. Testing
Tests SHALL cover:

```text
funder
opportunity
application
submission
decision
award
acceptance
receipt
posting
reversal
reporting
reconciliation
security
audit
```

## Implementation Record 180
**Object:** 180. Testing
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 181. Acceptance Criteria
The module is accepted when:

```text
funders can be maintained
applications can be created
applications can be submitted
awards can be recorded
project funding is linked
receipts can be registered
receipts can be posted
accounting references are retained
reporting obligations work
reconciliation works
security works
audit works
```

## Implementation Record 181
**Object:** 181. Acceptance Criteria
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 182. Release Blockers
Release SHALL be blocked by:

```text
duplicate application numbers
receipt without award when required
receipt posted without accounting reference
incorrect project funding total
unauthorised award acceptance
duplicate accounting posting
loss of award history
missing audit
```

## Implementation Record 182
**Object:** 182. Release Blockers
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 183. Implementation Order
Implement:

```text
1. funders
2. opportunities
3. applications
4. awards
5. reporting obligations
6. receipts
7. repositories
8. services
9. accounting integration
10. GUI
11. reports
12. audit
13. tests
```

## Implementation Record 183
**Object:** 183. Implementation Order
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 184. First Milestone
```text
Create funder
 ↓
Create opportunity
 ↓
Create application
 ↓
View application
```

## Implementation Record 184
**Object:** 184. First Milestone
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 185. Second Milestone
```text
Submit application
 ↓
Record decision
 ↓
Create award
 ↓
Accept award
```

## Implementation Record 185
**Object:** 185. Second Milestone
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 186. Third Milestone
```text
Register receipt
 ↓
Post accounting
 ↓
Link voucher
 ↓
Update project funding
```

## Implementation Record 186
**Object:** 186. Third Milestone
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 187. Fourth Milestone
```text
Create reporting obligation
 ↓
Attach document
 ↓
Submit report
 ↓
Close award
```

## Implementation Record 187
**Object:** 187. Fourth Milestone
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 188. End-to-End Scenario
```text
Project budget = 200,000
Application = 150,000
Award = 150,000
Receipt 1 = 75,000
Receipt 2 = 75,000
```

Expected:

```text
confirmed funding = 150,000
received funding = 150,000
funding gap = 50,000
award remaining = 0
accounting receipts = 150,000
```

## Implementation Record 188
**Object:** 188. End-to-End Scenario
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 189. Final Architecture
```text
                 GOVERNANCE
                     ↓
              FUNDING OPPORTUNITY
                     ↓
                  APPLICATION
                     ↓
                 AWARD
                     ↓
            PROJECT FUNDING
                     ↓
                  RECEIPT
                     ↓
              ACCOUNTING CORE
                     ↓
                   AUDIT

          REPORTING / DOCUMENTS
                 ↘   ↓   ↙
                  PROJECT
```

## Implementation Record 189
**Object:** 189. Final Architecture
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 190. Final Rules
```text
RULE 1
Requested funding is not confirmed funding.

RULE 2
Awarded funding is not cash received.

RULE 3
Actual cash remains an accounting concern.

RULE 4
A funding receipt must be traceable to its award.

RULE 5
A posted receipt must be traceable to accounting.

RULE 6
Project funding must reconcile to award/receipt records.

RULE 7
Historical applications and awards are never silently deleted.

RULE 8
Submission and award acceptance require authority.

RULE 9
AI may recommend but may not create financial authority.

RULE 10
Funding integrity failures enter a safe state.

RULE 11
Documents are referenced, not duplicated.

RULE 12
The implementation remains proportionate to a small non-profit association.
```

## Implementation Record 190
**Object:** 190. Final Rules
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 191. Next Layer
The next implementation layer should be:

```text
MFM v1.0 Document & Archive Implementation
```

It will connect:

```text
DOCUMENTS
+
PROJECTS
+
MEMBERS
+
ACCOUNTING
+
GRANTS
+
AUDIT
```

and provide a practical central document structure for invoices, grant applications, award letters, minutes, receipts, restoration documentation and other association records.

## Implementation Record 191
**Object:** 191. Next Layer
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.

# 192. Governing Principle
> **MFM shall make funding easy to follow from opportunity to application, from award to receipt, and from receipt to accounting and project impact, while preserving human authority and avoiding a second financial ledger.**

## Implementation Record 192
**Object:** 192. Governing Principle
**Layer:** Funding / Project / Accounting Integration
**Authority:** Human-authorised operation
**Audit:** Required for material state changes
**Failure mode:** Preserve historical state and prevent unsafe financial completion
**Lifecycle:** Draft → Validate → Authorise → Execute → Audit
**Acceptance:** Behaviour must be deterministic, traceable and reversible where financially appropriate.


# 193. Final Acceptance Checklist

```text
[ ] Funder register implemented
[ ] Opportunity register implemented
[ ] Application lifecycle implemented
[ ] Application submission authority implemented
[ ] Award lifecycle implemented
[ ] Award acceptance authority implemented
[ ] Project linkage implemented
[ ] Receipt registration implemented
[ ] Accounting integration implemented
[ ] Receipt idempotency implemented
[ ] Receipt reversal implemented
[ ] Reporting obligations implemented
[ ] Document references implemented
[ ] Funding reconciliation implemented
[ ] Project funding reconciliation implemented
[ ] Security permissions implemented
[ ] Audit events implemented
[ ] Negative tests implemented
[ ] Recovery tests implemented
[ ] Board report implemented
[ ] Treasurer report implemented
```

# 194. Release Decision

The Grants & Funding module may enter MFM v1.0 release only when all mandatory acceptance criteria are passed and no release blocker remains.

The implementation SHALL favour correctness and traceability over automation.

# END OF MFM v1.0 GRANTS & FUNDING IMPLEMENTATION
