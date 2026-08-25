# MFM v1.0 MEMBERSHIP & MEMBER MANAGEMENT

## MaritimForeningsManager — Medlemsadministration, medlemskaber og kontingentstyring

**Version:** 1.0  
**Status:** Development Baseline  
**Parent:** MFM v1.0 Accounting Core  
**Purpose:** Define the complete membership and member-management module for an almennyttig association

---

# 1. Purpose

The Membership & Member Management module provides the association with a simple and reliable way to manage:

- members;
- membership status;
- membership types;
- membership periods;
- contact information;
- membership fees;
- payments;
- outstanding balances;
- member history;
- member communication data;
- membership reports.

The module SHALL remain separate from the accounting ledger while providing controlled integration with the Accounting Core.

---

# 2. Core Principle

> **A member record describes a person and their relationship with the association; the accounting ledger records the financial consequences of that relationship.**

The member database SHALL therefore not become a second accounting system.

---

# 3. Architectural Position

```text
MEMBER
   ↓
MEMBERSHIP
   ↓
MEMBERSHIP FEE
   ↓
CHARGE / PAYMENT
   ↓
ACCOUNTING SERVICE
   ↓
ACCOUNTING LEDGER
```

The Membership module owns membership information.

The Accounting Core owns financial truth.

---

# 4. Scope

The module SHALL support:

1. Member registration
2. Member editing
3. Member search
4. Member status
5. Membership types
6. Membership periods
7. Membership fees
8. Fee status
9. Payment registration
10. Member history
11. Membership reports
12. Controlled accounting integration
13. Data export
14. Audit trail
15. Privacy controls

---

# 5. Out of Scope

MFM v1.0 shall not attempt to become:

- a general CRM;
- a marketing automation system;
- a mass-mailing platform;
- a social network;
- a payment gateway;
- a banking platform.

Communication and payment integrations MAY be added later.

---

# 6. Member Entity

A member is a person or, where specifically required, another membership entity.

Minimum member information:

```text
member_number
first_name
last_name
address
postal_code
city
phone
email
join_date
leave_date
status
notes
```

Only information required by the association SHALL be collected.

---

# 7. Member Number

Every member SHALL have a unique member number.

Example:

```text
M00001
M00002
M00003
```

The exact numbering scheme SHALL be configurable.

Member numbers SHALL not be reused for another member after a historical member record has existed.

---

# 8. Member Status

Recommended states:

```text
PENDING
ACTIVE
INACTIVE
LEFT
```

## PENDING

Registration has started but membership is not yet active.

## ACTIVE

Member currently belongs to the association.

## INACTIVE

Membership temporarily inactive without historical deletion.

## LEFT

Member has left the association.

---

# 9. Status Transitions

```text
PENDING
   ↓
ACTIVE
   ↓
INACTIVE
   ↓
ACTIVE

ACTIVE
   ↓
LEFT
```

The application SHALL preserve historical status changes.

---

# 10. Member Creation

Member creation SHALL require:

- first name;
- last name;
- member number;
- status.

Additional information MAY be added later.

The system SHALL prevent duplicate member numbers.

---

# 11. Member Editing

Active member data MAY be edited by authorised users.

Material changes SHOULD create an audit event.

Examples:

```text
ADDRESS_CHANGED
EMAIL_CHANGED
PHONE_CHANGED
STATUS_CHANGED
MEMBERSHIP_CHANGED
```

---

# 12. Member Deletion

Members with historical activity SHALL not be physically deleted through ordinary application functions.

Instead:

```text
ACTIVE → LEFT
```

This preserves:

- historical membership;
- fee history;
- accounting references;
- auditability.

---

# 13. Membership Entity

A membership represents the member's relationship with the association.

A member MAY have more than one historical membership record.

Fields include:

```text
member_id
membership_type
start_date
end_date
status
notes
```

---

# 14. Membership Types

Membership types SHALL be configurable.

Examples:

```text
ORDINARY
FAMILY
STUDENT
HONORARY
SUPPORTER
LIFE_MEMBER
```

The association MAY define its own categories.

---

# 15. Membership Type Configuration

A future configurable membership-type table SHOULD contain:

```text
name
description
default_fee
active
```

Membership type SHALL not be hard-coded into application logic.

---

# 16. Membership Period

A membership period defines:

```text
start_date
end_date
```

A typical annual membership might be:

```text
01-01-2027
31-12-2027
```

The system SHALL support different periods where needed.

---

# 17. Membership Fee

A membership fee is the financial obligation associated with a membership.

Fields:

```text
membership_id
financial_year
amount
due_date
status
voucher_id
```

Fee status:

```text
OPEN
PARTIAL
PAID
CANCELLED
```

---

# 18. Fee Lifecycle

```text
MEMBERSHIP ACTIVE
       ↓
FEE CREATED
       ↓
OPEN
       ↓
PAYMENT
       ↓
PARTIAL / PAID
```

If cancelled:

```text
OPEN
 ↓
CANCELLED
```

---

# 19. Fee Generation

The system SHOULD support generation of annual fees.

Example:

```text
Select financial year
        ↓
Find active members
        ↓
Determine membership type
        ↓
Determine applicable fee
        ↓
Create fee records
        ↓
Review
        ↓
Post financial consequences
```

Fee generation SHALL not blindly create duplicates.

---

# 20. Duplicate Fee Prevention

The application SHALL detect an existing fee for:

```text
member
+
membership
+
financial year
```

If an equivalent fee already exists, the system SHALL not silently create another.

---

# 21. Fee Adjustment

If a member receives a reduced or special fee:

```text
STANDARD FEE
      ↓
ADJUSTMENT
      ↓
FINAL FEE
```

The reason SHOULD be recorded.

---

# 22. Fee Cancellation

A fee MAY be cancelled by an authorised user.

Cancellation SHALL record:

- user;
- timestamp;
- reason.

If the fee has already generated accounting entries, the accounting effect SHALL be corrected through the Accounting Core.

---

# 23. Payment Registration

A payment SHALL be registered against the member fee.

Example:

```text
Fee       500
Payment   500
Status    PAID
```

Partial payment:

```text
Fee       500
Payment   300
Outstanding 200
Status    PARTIAL
```

---

# 24. Accounting Integration

Membership SHALL not directly write financial ledger records.

Instead:

```text
MembershipService
       ↓
AccountingService
       ↓
Accounting Core
```

This preserves one financial truth.

---

# 25. Fee Accounting Example

Where the association uses receivables:

```text
Debit  Membership Receivable
Credit Membership Income
```

Payment:

```text
Debit  Bank
Credit Membership Receivable
```

Exact account numbers SHALL be configurable.

---

# 26. Alternative Simple Accounting

For associations that recognise membership income directly on payment, the accounting workflow MAY instead be:

```text
Debit  Bank
Credit Membership Income
```

The selected accounting method SHALL be explicitly configured.

---

# 27. Fee Status Calculation

The system SHALL determine:

```text
TOTAL CHARGED
-
TOTAL PAID
=
OUTSTANDING
```

The outstanding amount SHALL never be inferred merely from a visual status field.

---

# 28. Payment Matching

Payments MAY be matched by:

- member number;
- reference;
- amount;
- date;
- description.

Automatic matching SHOULD initially produce suggestions.

---

# 29. Bank Integration

If bank import is implemented:

```text
BANK TRANSACTION
       ↓
MATCH MEMBER FEE
       ↓
USER REVIEW
       ↓
REGISTER PAYMENT
       ↓
ACCOUNTING
```

No payment SHALL be silently assigned to the wrong member.

---

# 30. Member Search

Search SHALL support:

- member number;
- first name;
- last name;
- email;
- phone;
- status.

Search SHOULD tolerate ordinary partial text.

---

# 31. Member List

Recommended columns:

```text
Member No.
Name
Membership
Status
Email
Phone
Fee Status
```

The list SHOULD support filtering.

---

# 32. Member Details

The member detail view SHOULD contain:

```text
PERSONAL INFORMATION
MEMBERSHIP
FEES
PAYMENTS
DOCUMENTS
HISTORY
```

Financial information SHALL be read from authoritative fee/accounting data.

---

# 33. Member History

History SHOULD show:

```text
JOINED
MEMBERSHIP CHANGED
ADDRESS CHANGED
FEE CREATED
PAYMENT REGISTERED
STATUS CHANGED
LEFT
```

Material events SHALL be auditable.

---

# 34. Contact Information

The module MAY store:

```text
address
postal code
city
phone
email
```

The association SHOULD avoid collecting unnecessary personal information.

---

# 35. Email

Email addresses SHALL be validated for basic syntax.

The application SHALL not assume that an email is valid merely because it contains `@`.

---

# 36. Communication

MFM v1.0 MAY provide export of member contact lists.

Direct mass-mailing SHALL remain optional.

---

# 37. Member Documents

Documents MAY be linked to a member.

Examples:

```text
membership application
correspondence
consent
other association documents
```

Documents SHALL follow the Document Foundation rules.

---

# 38. Privacy

Member data SHALL be protected by role permissions.

Recommended:

```text
READ MEMBER DATA
EDIT MEMBER DATA
VIEW MEMBER FINANCIAL STATUS
EXPORT MEMBER DATA
ADMINISTER MEMBER DATA
```

These permissions MAY be mapped to existing roles.

---

# 39. Financial Privacy

Not every user who can view a member should automatically see:

- outstanding fees;
- payment history;
- financial notes.

Financial membership data SHALL therefore be separately permissioned where practical.

---

# 40. Data Export

Member export SHOULD support:

```text
CSV
XLSX
```

Exports SHOULD include only fields selected by the user.

Sensitive fields SHOULD require appropriate permission.

---

# 41. Audit Trail

Material membership events SHOULD create audit events.

Examples:

```text
MEMBER_CREATED
MEMBER_UPDATED
MEMBER_DEACTIVATED
MEMBER_STATUS_CHANGED
MEMBERSHIP_CREATED
MEMBERSHIP_CHANGED
FEE_CREATED
FEE_ADJUSTED
FEE_CANCELLED
PAYMENT_REGISTERED
```

---

# 42. Membership Service

Recommended service methods:

```text
create_member()
update_member()
get_member()
search_members()
change_status()
create_membership()
end_membership()
create_fee()
generate_fees()
adjust_fee()
cancel_fee()
register_payment()
get_fee_status()
get_member_history()
```

---

# 43. Member Repository

`MemberRepository` SHALL handle persistence for:

- members;
- memberships;
- membership fees;
- member queries.

It SHALL not contain GUI code.

---

# 44. Membership Business Rules

The service layer SHALL enforce:

- unique member number;
- valid membership status;
- valid membership dates;
- valid fee amount;
- duplicate fee prevention;
- authorised changes;
- controlled cancellation;
- payment limits.

---

# 45. Payment Validation

A payment SHALL not exceed the outstanding fee without explicit handling.

If:

```text
Payment > Outstanding
```

the system SHALL:

- warn;
- require clarification;
- or record an unapplied amount according to configured policy.

It SHALL not silently discard the difference.

---

# 46. Overpayment

Future support MAY provide:

```text
UNAPPLIED PAYMENT
```

which can later be allocated.

The first implementation MAY require manual resolution.

---

# 47. Refund

Refunds SHALL be treated as controlled financial transactions.

A refund SHALL:

- identify the original payment;
- record amount;
- record reason;
- use AccountingService;
- create audit event.

---

# 48. Membership Renewal

Renewal SHALL normally create a new membership period or extend the existing membership according to the configured model.

Historical information SHALL remain available.

---

# 49. Annual Fee Process

Recommended annual workflow:

```text
1. Verify membership types
2. Verify fee rates
3. Review active members
4. Generate proposed fees
5. Review exceptions
6. Confirm
7. Create fees
8. Create accounting consequences
9. Audit
10. Report
```

---

# 50. Fee Preview

Before final generation, the application SHOULD show:

```text
Member
Membership Type
Standard Fee
Adjustment
Final Fee
```

This provides a human control point.

---

# 51. Fee Generation Authority

Automatic fee generation SHALL not silently alter association fee policy.

Fee rates SHALL come from configured data approved by authorised users.

---

# 52. Membership Type Changes

Changing membership type SHALL not rewrite historical membership records.

Instead:

```text
OLD MEMBERSHIP
      ↓
END
      ↓
NEW MEMBERSHIP
```

This preserves history.

---

# 53. Member Leaving

When a member leaves:

```text
status = LEFT
leave_date = date
```

Outstanding financial obligations SHALL remain visible according to accounting policy.

The system SHALL not automatically cancel debt merely because membership ended.

---

# 54. Rejoining

A former member may rejoin.

The application SHOULD preserve the original member number where association policy permits.

A new membership period SHALL be created.

---

# 55. Duplicate Person Detection

The system SHOULD warn about possible duplicate members based on combinations such as:

- name;
- email;
- phone;
- address.

It SHALL not automatically merge records.

---

# 56. Merge

Member merge MAY be implemented later.

If implemented, it SHALL:

- require administrator authority;
- preserve audit;
- preserve financial history;
- retain a reference to the source member;
- never silently destroy accounting history.

---

# 57. Membership Reports

Minimum reports:

1. Member list
2. Active members
3. New members
4. Members who left
5. Membership by type
6. Fee status
7. Outstanding fees
8. Payments
9. Membership history

---

# 58. Annual Membership Report

The annual report SHOULD show:

```text
Opening members
+
New members
-
Members leaving
=
Closing members
```

---

# 59. Fee Report

The fee report SHOULD show:

```text
Member
Fee
Paid
Outstanding
Status
```

Filters:

```text
financial year
membership type
status
```

---

# 60. Member Statistics

Dashboard MAY show:

```text
TOTAL MEMBERS
ACTIVE MEMBERS
NEW THIS YEAR
LEFT THIS YEAR
OPEN FEES
OUTSTANDING AMOUNT
```

---

# 61. Membership GUI

Recommended navigation:

```text
Members
 ├── Member List
 ├── New Member
 ├── Membership Types
 ├── Fees
 └── Reports
```

---

# 62. Member Entry Screen

Recommended:

```text
Member Number
First Name
Last Name
Address
Postal Code
City
Phone
Email
Join Date
Status
Notes
```

Save SHALL validate required fields.

---

# 63. Membership Screen

Show:

```text
Membership Type
Start
End
Status
Fee
History
```

---

# 64. Fee Screen

Show:

```text
Member
Financial Year
Amount
Due Date
Paid
Outstanding
Status
```

Actions:

```text
Create
Adjust
Cancel
Register Payment
View Accounting
```

---

# 65. Member-to-Accounting Link

The member interface MAY provide:

```text
View fee
 ↓
View related voucher
 ↓
View ledger entry
```

The accounting record remains authoritative.

---

# 66. Membership-to-Project Separation

Membership SHALL remain independent of project accounting.

A member MAY be:

- a volunteer;
- project responsible;
- donor;
- board member;

without changing the membership accounting model.

---

# 67. Volunteer Information

Volunteer management is outside the minimum membership model.

Optional future fields MAY include:

```text
volunteer
skills
availability
```

These SHALL not be introduced into v1.0 unless required.

---

# 68. Board Roles

Board membership MAY be represented as a separate association role rather than changing membership type.

This avoids mixing governance and membership.

---

# 69. Data Validation

Minimum:

```text
member number required
first name required
last name required
status valid
join date valid
leave date >= join date
fee amount >= 0
payment amount > 0
financial year valid
```

---

# 70. Negative Testing

```text
Duplicate member number → BLOCK
Missing name → BLOCK
Invalid status → BLOCK
Invalid date range → BLOCK
Duplicate annual fee → BLOCK
Negative fee → BLOCK
Negative payment → BLOCK
Unauthorised fee cancellation → BLOCK
Unauthorised member export → BLOCK
Payment exceeds fee → WARN / CONTROL
Delete historical member → BLOCK
Change historical membership silently → BLOCK
Change fee policy without authority → BLOCK
Assign payment to invalid member → BLOCK
Database failure during payment → ROLLBACK
Audit failure during material change → ROLLBACK
```

---

# 71. Acceptance Test — Create Member

Input valid member.

Expected:

```text
member created
member number unique
audit event created
```

---

# 72. Acceptance Test — Duplicate Member

Create member using existing member number.

Expected:

```text
creation rejected
```

---

# 73. Acceptance Test — Membership

Create:

```text
Member = M00001
Type = ORDINARY
Start = 2027-01-01
End = 2027-12-31
```

Expected:

```text
membership active
```

---

# 74. Acceptance Test — Annual Fee

Generate annual fee.

Expected:

```text
one fee
correct amount
correct financial year
status OPEN
```

Running generation again SHALL not silently create a duplicate.

---

# 75. Acceptance Test — Payment

Fee:

```text
500
```

Payment:

```text
500
```

Expected:

```text
PAID
Outstanding = 0
Accounting transaction exists
Audit event exists
```

---

# 76. Acceptance Test — Partial Payment

Fee:

```text
500
```

Payment:

```text
300
```

Expected:

```text
PARTIAL
Outstanding = 200
```

---

# 77. Acceptance Test — Member Leaving

Change:

```text
ACTIVE → LEFT
```

Expected:

```text
leave date recorded
membership history preserved
financial history preserved
audit event exists
```

---

# 78. Acceptance Test — Rejoin

Former member rejoins.

Expected:

```text
historical membership retained
new membership period created
member number preserved where permitted
```

---

# 79. Acceptance Test — Export

Authorised user exports member list.

Expected:

```text
file generated
selected fields included
no unauthorised fields
```

---

# 80. Service Integration

The target architecture is:

```text
Member GUI
     ↓
MembershipService
     ↓
MemberRepository
     ↓
Database
```

For accounting:

```text
MembershipService
     ↓
AccountingService
     ↓
AccountingRepository
     ↓
Database
```

---

# 81. Transactional Payment Flow

```text
BEGIN
 ↓
Validate member
 ↓
Validate fee
 ↓
Validate payment
 ↓
Update fee status
 ↓
Create accounting transaction
 ↓
Create audit event
 ↓
COMMIT
```

Failure SHALL rollback all related changes.

---

# 82. Membership Configuration

Association settings SHOULD include:

```text
default membership year
default fee
default due date
membership number prefix
```

These SHALL be configurable.

---

# 83. Data Migration

If existing member data exists in Excel or another system:

```text
IMPORT
 ↓
VALIDATE
 ↓
DUPLICATE CHECK
 ↓
PREVIEW
 ↓
USER CONFIRM
 ↓
CREATE
 ↓
AUDIT
```

No direct database import without validation.

---

# 84. Import Mapping

Possible columns:

```text
Member Number
First Name
Last Name
Address
Postal Code
City
Phone
Email
Membership Type
Status
```

The import process SHALL report rejected rows.

---

# 85. Import Error Report

Example:

```text
Row 12
Error: duplicate member number

Row 24
Error: missing last name
```

The user SHALL be able to correct the source and retry.

---

# 86. Privacy and Retention

Member data SHALL only be retained according to the association's legitimate requirements and applicable rules.

The application SHOULD support controlled anonymisation or deactivation where required.

Financial records that must remain for accounting purposes SHALL not be destroyed merely because a member leaves.

---

# 87. Backup

Member data SHALL be included in the standard MFM database backup.

Documents linked to members SHALL be included in the document backup.

---

# 88. Performance

The module SHALL support normal association membership volumes without specialised infrastructure.

Indexed search SHALL be used for member number and common lookup fields.

---

# 89. Integration with Dashboard

Dashboard membership metrics SHALL derive from the membership service.

Example:

```text
Active members = COUNT(active membership)
Open fees = COUNT(open fees)
Outstanding = SUM(outstanding)
```

---

# 90. Reporting Integrity

Membership reports SHALL use the membership database.

Financial reports SHALL use the Accounting Core.

Where a report combines both:

```text
Membership data → MembershipService
Financial data   → AccountingService
```

The report layer SHALL combine the results.

---

# 91. Error Handling

User-facing errors SHALL be understandable.

Examples:

```text
"Member number already exists."
"Membership fee already exists for this year."
"The selected membership is inactive."
"The payment exceeds the outstanding amount."
"You do not have permission to perform this action."
```

Technical exceptions SHALL be logged separately.

---

# 92. Security

Member data SHALL be accessible only to authorised users.

Exports SHALL require appropriate permission.

Administrative membership functions SHALL be protected.

---

# 93. Maintainability

Membership business rules SHALL reside in:

```text
membership_service.py
```

not in:

```text
members.py
```

The GUI SHALL present and collect information.

---

# 94. Suggested Files

```text
src/
├── models/
│   ├── member.py
│   ├── membership.py
│   └── membership_fee.py
│
├── repositories/
│   ├── member_repository.py
│   └── membership_repository.py
│
├── services/
│   ├── member_service.py
│   └── membership_service.py
│
└── gui/
    ├── members.py
    ├── membership.py
    └── membership_fees.py
```

Existing files MAY be reused if they meet the architecture baseline.

---

# 95. Development Sequence

```text
1. Member model
2. Membership model
3. Fee model
4. Repository
5. Member service
6. Membership service
7. Validation
8. Fee generation
9. Payment integration
10. Audit integration
11. Member GUI
12. Fee GUI
13. Reports
14. Import/export
15. Tests
```

---

# 96. Definition of Done

Membership & Member Management v1.0 is complete when:

- members can be created;
- members can be edited;
- member numbers are unique;
- members can be deactivated;
- membership history is preserved;
- membership types work;
- membership periods work;
- annual fees work;
- duplicate fees are prevented;
- payments work;
- partial payments work;
- accounting integration works;
- member reports work;
- fee reports work;
- export works;
- audit works;
- permissions work;
- negative tests pass.

---

# 97. Relationship to Previous Baselines

```text
MFM Architecture Baseline
          ↓
Database Foundation
          ↓
Accounting Core
          ↓
Membership & Member Management
```

Membership uses the database foundation.

Membership uses the Accounting Core for financial consequences.

Membership does not replace either.

---

# 98. Final Governing Principle

> **The membership system shall make it easy to manage people and their relationship with the association while keeping financial truth in the accounting core and historical truth in the audit trail.**

# END OF MFM v1.0 MEMBERSHIP & MEMBER MANAGEMENT
