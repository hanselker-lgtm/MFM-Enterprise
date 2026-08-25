# MFM v1.0 MEMBERSHIP & MEMBER MANAGEMENT IMPLEMENTATION

## MaritimForeningsManager — Konkret implementeringsgrundlag for medlemmer, medlemsstatus, kontingenter, betalinger og regnskabsintegration

**Version:** 1.0  
**Status:** Implementation Baseline  
**Parent:** MFM v1.0 Accounting Core Implementation  
**Purpose:** Provide a simple, secure and auditable membership subsystem for a non-profit association

---

# 1. Purpose

This document defines the concrete implementation baseline for the MFM membership module.

The module SHALL manage:

```text
MEMBERS
MEMBERSHIP TYPES
MEMBERSHIP STATUS
MEMBERSHIP PERIODS
MEMBERSHIP FEES
PAYMENTS
MEMBER COMMUNICATION DATA
MEMBER HISTORY
ACCOUNTING INTEGRATION
AUDIT
```

The design SHALL remain proportionate to a small non-profit association.

---

# 2. Membership Principle

> **The member register is the authoritative source for who belongs to the association; accounting remains the authoritative source for money.**

Membership and accounting SHALL therefore be integrated but not merged into one data model.

---

# 3. Scope

Mandatory v1.0:

```text
Member register
Membership types
Membership status
Membership periods
Membership fee definitions
Member fee generation
Payment registration
Payment allocation
Outstanding fees
Member balance
Membership reports
Accounting integration
Audit
```

Optional later:

```text
online self-service
automatic payment gateways
SMS
mass email
QR payment
MobilePay API
advanced CRM
```

---

# 4. Membership Architecture

```text
MEMBER
   ↓
MEMBERSHIP
   ↓
FEE
   ↓
PAYMENT
   ↓
ACCOUNTING
   ↓
AUDIT
```

---

# 5. Security Architecture

```text
USER
 ↓
SECURITY CONTEXT
 ↓
MEMBERSHIP SERVICE
 ↓
MEMBERSHIP REPOSITORY
 ↓
DATABASE
 ↓
AUDIT
```

---

# 6. Member Entity

Minimum:

```text
id
member_number
first_name
last_name
status
created_at
updated_at
```

Recommended:

```text
address
postal_code
city
country
phone
email
notes
```

---

# 7. Member Number

Member number SHALL be unique.

Example:

```text
0001
0002
0003
```

The number SHALL remain stable during the member's lifetime.

---

# 8. Member Number Reuse

A former member's number SHOULD NOT be reassigned.

Historical references must remain unambiguous.

---

# 9. Name

Minimum:

```text
first_name
last_name
```

Names SHALL be stored as data fields, not one combined authoritative field.

---

# 10. Address

Address fields SHOULD be separated:

```text
address
postal_code
city
country
```

---

# 11. Contact Information

Optional:

```text
phone
email
```

Contact data SHALL be treated as personal data.

---

# 12. Member Status

Recommended:

```text
ACTIVE
INACTIVE
FORMER
DECEASED
```

The exact status vocabulary MAY be adjusted by the association.

---

# 13. Active Member

An active member is currently entitled to membership benefits according to the association's rules.

---

# 14. Inactive Member

An inactive member record is retained but is not currently an active membership.

---

# 15. Former Member

A former member has ended their membership.

Historical financial and membership records SHALL remain.

---

# 16. No Physical Deletion

A member with historical activity SHALL not be physically deleted.

---

# 17. Member Archiving

Former members MAY be archived from ordinary lists while remaining available for authorised historical reporting.

---

# 18. Membership Type

A membership type defines the category of membership.

Examples:

```text
ORDINARY
FAMILY
STUDENT
HONORARY
SUPPORTER
```

The association defines the actual categories.

---

# 19. Membership Type Entity

Minimum:

```text
id
name
description
active
```

Recommended:

```text
default_fee
account_id
```

---

# 20. Membership Type Fee

The default fee is a configuration value.

It SHALL not overwrite historical fees already generated.

---

# 21. Membership Period

A membership record SHALL identify a period.

Minimum:

```text
id
member_id
membership_type_id
start_date
end_date
status
```

---

# 22. Membership History

A member MAY have multiple historical memberships.

Example:

```text
2024 ordinary
2025 ordinary
2026 supporter
```

History SHALL remain traceable.

---

# 23. Overlapping Memberships

The service SHOULD prevent accidental overlapping active memberships unless the association explicitly permits them.

---

# 24. Membership Renewal

Renewal SHOULD create a new membership period or extend an existing period according to the chosen model.

Historical information SHALL not be lost.

---

# 25. Membership Status Derivation

The application MAY derive current membership from:

```text
active membership
+
date
```

rather than relying only on a manually maintained flag.

---

# 26. Membership Service

Recommended API:

```text
create_member()
update_member()
deactivate_member()
reactivate_member()
create_membership()
renew_membership()
end_membership()
get_member()
list_members()
```

---

# 27. Member Creation

Create operation:

```text
validate data
 ↓
allocate member number
 ↓
create member
 ↓
audit
```

---

# 28. Member Number Allocation

Allocation SHALL be transactional.

It SHALL not depend solely on the visible GUI list.

---

# 29. Duplicate Member Detection

The application SHOULD warn about likely duplicates using combinations such as:

```text
name
email
phone
```

A warning SHALL not automatically reject a legitimate member.

---

# 30. Duplicate Detection Principle

The user remains responsible for confirming whether two similar records are actually the same person.

---

# 31. Member Edit

Authorised users MAY edit contact information.

Material changes SHOULD be audited.

---

# 32. Membership Administrator Permission

Recommended permissions:

```text
VIEW_MEMBERS
CREATE_MEMBER
EDIT_MEMBER
MANAGE_MEMBERSHIP
MANAGE_MEMBERSHIP_FEES
REGISTER_MEMBER_PAYMENT
VIEW_MEMBER_BALANCE
EXPORT_MEMBER_DATA
```

---

# 33. Membership Role

The existing:

```text
MEMBER_ADMIN
```

role SHOULD receive the normal membership permissions.

---

# 34. Treasurer Integration

The treasurer MAY receive:

```text
VIEW_MEMBER_BALANCE
REGISTER_MEMBER_PAYMENT
```

without necessarily receiving full member administration rights.

---

# 35. Member Privacy

Users SHALL only see member data necessary for their role.

---

# 36. Personal Data Minimisation

MFM SHALL not require unnecessary personal information.

---

# 37. Optional Fields

The following SHOULD remain optional:

```text
phone
email
address
notes
```

unless the association has a specific operational requirement.

---

# 38. Email Validation

Email format validation SHOULD be basic and practical.

It SHALL not reject unusual but technically valid addresses unnecessarily.

---

# 39. Phone Validation

Phone numbers SHALL not be forced into a single country-specific format unless required.

---

# 40. Membership Fee

A fee record represents an amount owed for membership.

Minimum:

```text
id
member_id
membership_id
fee_date
due_date
amount
status
```

---

# 41. Fee Status

Recommended:

```text
OPEN
PARTIALLY_PAID
PAID
CANCELLED
```

---

# 42. Fee Amount

Fee amounts SHALL use the same authoritative money representation as accounting.

Recommended:

```text
integer minor units
```

---

# 43. Fee Currency

v1.0 default:

```text
DKK
```

---

# 44. Fee Generation

The system MAY generate a fee from:

```text
membership type
membership period
fee schedule
```

---

# 45. Historical Fee

Once a fee is generated, its amount SHALL not silently change because the membership type's default fee changes.

---

# 46. Fee Adjustment

A fee adjustment SHALL be a controlled operation.

It SHALL be audited.

---

# 47. Fee Cancellation

Cancelling an unpaid fee SHALL require appropriate authority.

The reason SHALL be recorded.

---

# 48. Fee Deletion

A fee with financial history SHALL not be physically deleted.

Use cancellation or adjustment.

---

# 49. Due Date

The fee SHALL have a due date where the association uses payment deadlines.

---

# 50. Payment

A payment represents money received from a member.

Minimum:

```text
id
member_id
payment_date
amount
payment_method
reference
status
```

---

# 51. Payment Method

Recommended:

```text
BANK
CASH
CARD
OTHER
```

Additional methods can be configured.

---

# 52. Payment Reference

Reference MAY contain:

```text
bank reference
receipt number
manual reference
```

Do not store unnecessary sensitive payment information.

---

# 53. Payment Allocation

A payment SHOULD be allocated to one or more open membership fees.

---

# 54. Allocation Example

Fee:

```text
500 DKK
```

Payment:

```text
500 DKK
```

Allocation:

```text
500 → fee
```

Status:

```text
PAID
```

---

# 55. Partial Payment

Fee:

```text
500
```

Payment:

```text
300
```

Status:

```text
PARTIALLY_PAID
```

Outstanding:

```text
200
```

---

# 56. Multiple Fee Allocation

A payment MAY cover multiple fees.

Example:

```text
Fee 2026 = 500
Fee 2027 = 500
Payment = 1,000
```

Allocation:

```text
500 → 2026
500 → 2027
```

---

# 57. Payment Allocation Table

Recommended:

```text
payment_allocations
```

Fields:

```text
id
payment_id
fee_id
amount
created_at
```

---

# 58. Allocation Rule

Total allocation SHALL not exceed:

```text
payment amount
```

nor:

```text
fee outstanding amount
```

---

# 59. Unallocated Payment

A payment MAY temporarily remain:

```text
UNALLOCATED
```

when the member or fee cannot yet be identified.

---

# 60. Unallocated Payment Governance

Unallocated money SHALL not be silently assigned to a member.

It requires review.

---

# 61. Payment Status

Recommended:

```text
UNALLOCATED
PARTIALLY_ALLOCATED
ALLOCATED
REVERSED
```

---

# 62. Payment Reversal

A payment reversal SHALL not delete the original payment.

It creates a controlled reversal record.

---

# 63. Payment Reversal Reason

Required:

```text
reason
actor
timestamp
```

---

# 64. Payment Audit

Payment creation, allocation and reversal SHALL be auditable.

---

# 65. Accounting Integration

Membership financial activity SHALL integrate with the accounting core.

The membership module SHALL not maintain a second independent accounting ledger.

---

# 66. Accounting Flow

```text
MEMBERSHIP FEE
      ↓
MEMBERSHIP RECEIVABLE / FEE RECORD
      ↓
PAYMENT
      ↓
ACCOUNTING SERVICE
      ↓
BANK / CASH
```

The exact accounting treatment depends on the association's bookkeeping policy.

---

# 67. Cash-Basis Simplicity

For a simple association, membership income may be recognised when payment is received.

The implementation SHALL support the association's chosen accounting policy.

---

# 68. Receivable Model

If the association tracks unpaid membership fees as receivables:

```text
Fee generated
 ↓
Receivable
 ↓
Payment
 ↓
Receivable cleared
```

This can be enabled without changing the member model.

---

# 69. Accounting Boundary

MembershipService requests accounting operations through:

```text
AccountingService
```

It SHALL not insert voucher lines directly.

---

# 70. Payment Accounting Example

For a cash-style model:

```text
Debit Bank
Credit Membership Income
```

For a receivable model:

```text
Fee:
Debit Receivable
Credit Membership Income

Payment:
Debit Bank
Credit Receivable
```

The selected policy SHALL be documented in the association's accounting setup.

---

# 71. Payment Posting

A payment that creates an accounting transaction SHALL use the normal:

```text
validate
authorise
post
audit
```

workflow.

---

# 72. Payment Idempotency

A payment SHALL not create duplicate accounting entries because the user clicks Save twice.

---

# 73. Payment Reference Uniqueness

Where reliable bank references exist, the system SHOULD warn about duplicate references.

It SHALL not assume every duplicate reference is an error.

---

# 74. Receipt

MFM MAY generate a payment receipt.

Minimum:

```text
member
date
amount
reference
payment method
```

---

# 75. Receipt Number

Receipt numbers SHOULD be unique if formal receipts are used.

---

# 76. Receipt Audit

Generating a formal receipt MAY be audited.

---

# 77. Member Balance

Member balance:

```text
fees
-
allocated payments
```

depending on the accounting model.

---

# 78. Positive Balance

A member may have:

```text
credit balance
```

if payments exceed currently allocated fees.

The system SHALL not silently convert this into a new fee.

---

# 79. Credit Handling

A credit may be:

```text
UNALLOCATED CREDIT
```

until allocated or refunded according to association policy.

---

# 80. Refund

Refund capability is optional for v1.0.

If implemented, it SHALL require:

```text
REFUND_MEMBER_PAYMENT
```

permission and audit.

---

# 81. Outstanding Fees

The application SHOULD provide:

```text
all open fees
overdue fees
partially paid fees
```

---

# 82. Overdue

A fee is overdue when:

```text
due_date < current_date
```

and:

```text
outstanding > 0
```

---

# 83. Reminder List

MFM SHOULD provide a list of members requiring payment reminder.

---

# 84. Reminder Generation

The system MAY generate:

```text
payment reminder
```

but SHALL not automatically send it without an appropriate user action in v1.0.

---

# 85. Communication Log

Optional table:

```text
member_communications
```

can record:

```text
date
member
type
subject
status
```

---

# 86. Communication Scope

v1.0 does not require a full CRM.

---

# 87. Membership Reports

Minimum:

```text
Member Register
Active Members
Former Members
Membership by Type
Fees Outstanding
Paid Fees
Member Balance
Payment Register
```

---

# 88. Member Register

Columns:

```text
member number
name
membership type
status
contact
membership dates
```

---

# 89. Active Member Report

Filter:

```text
active membership
```

---

# 90. Former Member Report

Filter:

```text
former
```

or historical ended memberships.

---

# 91. Membership Type Report

Show counts:

```text
ordinary
family
student
supporter
```

according to configured types.

---

# 92. Fee Report

Show:

```text
member
fee
due date
amount
paid
outstanding
status
```

---

# 93. Payment Report

Show:

```text
date
member
amount
method
reference
allocation
```

---

# 94. Member Balance Report

Show:

```text
member
fees
payments
outstanding
credit
```

---

# 95. Membership Dashboard

Useful indicators:

```text
Active Members
New Members
Former Members
Outstanding Fees
Overdue Fees
Payments This Period
```

---

# 96. Dashboard Security

Member financial data SHALL only be visible to authorised users.

---

# 97. Membership GUI

Minimum screens:

```text
Member List
Member Detail
Membership History
Fee List
Payment Entry
Outstanding Fees
Membership Reports
```

---

# 98. Member List

Search by:

```text
member number
name
email
phone
```

---

# 99. Member Detail

Sections:

```text
Identity
Contact
Current Membership
Membership History
Fees
Payments
Notes
```

---

# 100. Member History

History SHOULD show:

```text
membership
start
end
type
status
```

---

# 101. Fee Entry

Fee form:

```text
member
membership
date
due date
amount
description
```

---

# 102. Payment Entry

Payment form:

```text
member
date
amount
method
reference
fees to allocate
```

---

# 103. Payment Entry Validation

Check:

```text
member exists
amount > 0
date valid
allocation <= payment
```

---

# 104. Membership Type Administration

Administrators SHOULD be able to:

```text
create type
edit type
deactivate type
set default fee
```

---

# 105. Membership Type Deactivation

Deactivating a type SHALL not alter historical memberships.

---

# 106. Fee Schedule

For v1.0, a simple annual default fee is sufficient.

Future versions may support:

```text
monthly
quarterly
custom periods
```

---

# 107. Annual Fee Generation

The system MAY generate fees for active memberships for the selected year.

---

# 108. Fee Generation Safety

Repeated generation SHALL not duplicate fees.

The system SHALL check whether the fee already exists.

---

# 109. Fee Generation Transaction

```text
BEGIN
 ↓
identify active memberships
 ↓
check existing fee
 ↓
create missing fee
 ↓
audit
 ↓
COMMIT
```

---

# 110. Fee Generation Permission

Require:

```text
MANAGE_MEMBERSHIP_FEES
```

---

# 111. Fee Generation Preview

Before committing mass fee generation, the GUI SHOULD display:

```text
members affected
total amount
already generated
new fees
```

---

# 112. Mass Operation Safety

Mass generation SHALL require confirmation.

---

# 113. Mass Update

MFM v1.0 SHOULD avoid mass editing personal data unless specifically needed.

---

# 114. Membership Renewal

Renewal SHOULD provide:

```text
old membership
new period
new type if changed
fee
```

---

# 115. Renewal Safety

Renewal SHALL not accidentally create duplicate overlapping membership periods.

---

# 116. Membership End

Ending membership SHALL record:

```text
end date
reason
actor
```

Reason may be optional according to association policy.

---

# 117. Membership Reinstatement

A former member may be reinstated through a new membership period.

History remains intact.

---

# 118. Member Merge

Member merge is not mandatory for v1.0.

If implemented later, it requires exceptional controls because financial history is involved.

---

# 119. Member Import

CSV/XLSX import is optional.

If implemented, import SHALL use validation and preview.

---

# 120. Import Principle

Import SHALL never directly bypass:

```text
MemberService
```

or audit controls.

---

# 121. Member Export

Export MAY be provided for authorised users.

Permission:

```text
EXPORT_MEMBER_DATA
```

---

# 122. Export Privacy

Exports containing personal data SHALL be treated as controlled outputs.

---

# 123. GDPR-Oriented Principle

MFM SHALL support practical data minimisation, access control and retention without turning v1.0 into a compliance management system.

---

# 124. Data Retention

Financial records SHALL be retained according to applicable accounting requirements.

Membership contact records may have different retention needs.

---

# 125. Former Member Data

Former members SHALL remain identifiable where necessary for historical financial accountability.

---

# 126. Personal Data Anonymisation

Anonymisation must not destroy accounting integrity.

A future privacy workflow may anonymise non-required contact fields while retaining legally necessary financial references.

---

# 127. Notes

Member notes SHOULD be used sparingly.

Sensitive personal information should not be stored in free-text fields unless necessary.

---

# 128. Security

Membership operations require authentication.

---

# 129. Authorisation

Examples:

```text
VIEW_MEMBERS
CREATE_MEMBER
EDIT_MEMBER
MANAGE_MEMBERSHIP
REGISTER_MEMBER_PAYMENT
VIEW_MEMBER_BALANCE
EXPORT_MEMBER_DATA
```

---

# 130. Service-Level Enforcement

The service SHALL check permissions.

The GUI alone SHALL not provide the security boundary.

---

# 131. Audit Events

Minimum:

```text
MEMBER_CREATED
MEMBER_UPDATED
MEMBER_DEACTIVATED
MEMBERSHIP_CREATED
MEMBERSHIP_RENEWED
MEMBERSHIP_ENDED
FEE_CREATED
FEE_CANCELLED
PAYMENT_CREATED
PAYMENT_ALLOCATED
PAYMENT_REVERSED
MEMBER_DATA_EXPORTED
```

---

# 132. Audit Actor

Every material operation SHALL record the authenticated actor.

---

# 133. Audit Old/New State

For important changes, audit SHOULD record meaningful old/new values.

Do not duplicate unnecessary personal data.

---

# 134. Membership Database Tables

Recommended:

```text
members
membership_types
memberships
membership_fees
payments
payment_allocations
```

Optional:

```text
member_communications
```

---

# 135. Members Table

Conceptual:

```text
id
member_number
first_name
last_name
address
postal_code
city
country
phone
email
status
notes
created_at
updated_at
```

---

# 136. Membership Types Table

```text
id
name
description
default_fee_minor
active
created_at
updated_at
```

---

# 137. Memberships Table

```text
id
member_id
membership_type_id
start_date
end_date
status
created_at
updated_at
```

---

# 138. Membership Fees Table

```text
id
member_id
membership_id
fee_date
due_date
amount_minor
status
description
created_at
updated_at
```

---

# 139. Payments Table

```text
id
member_id
payment_date
amount_minor
payment_method
reference
status
created_by
created_at
```

---

# 140. Payment Allocations Table

```text
id
payment_id
fee_id
amount_minor
created_at
```

---

# 141. Foreign Keys

Enforce relationships:

```text
membership.member_id → members.id
membership.membership_type_id → membership_types.id
fee.member_id → members.id
fee.membership_id → memberships.id
payment.member_id → members.id
allocation.payment_id → payments.id
allocation.fee_id → membership_fees.id
```

---

# 142. Indexes

Recommended:

```text
members.member_number
members.last_name
members.email
members.status
memberships.member_id
memberships.start_date
memberships.end_date
membership_fees.member_id
membership_fees.status
membership_fees.due_date
payments.member_id
payments.payment_date
payment_allocations.payment_id
payment_allocations.fee_id
```

---

# 143. Unique Constraints

Recommended:

```text
member_number UNIQUE
membership_type.name UNIQUE
```

Payment references should not necessarily be globally unique because external references can repeat.

---

# 144. Date Validation

Membership:

```text
start_date <= end_date
```

where end date exists.

---

# 145. Fee Validation

```text
amount > 0
due_date valid
member exists
membership exists
```

---

# 146. Payment Validation

```text
amount > 0
member exists
date valid
```

---

# 147. Allocation Validation

```text
amount > 0
payment exists
fee exists
allocation <= payment remaining
allocation <= fee outstanding
```

---

# 148. Membership Overlap Validation

The service SHOULD detect:

```text
same member
same active period
```

and reject or warn according to policy.

---

# 149. Fee Uniqueness

A fee generation key MAY use:

```text
membership_id
fee period
fee type
```

to prevent duplicate annual fees.

---

# 150. Payment Idempotency Key

Where available, a stable external reference MAY be stored for duplicate detection.

---

# 151. Member Repository

Recommended:

```text
get_by_id()
get_by_number()
search()
create()
update()
update_status()
```

---

# 152. Membership Repository

Recommended:

```text
create()
get_current()
list_history()
update()
end()
```

---

# 153. Fee Repository

Recommended:

```text
create()
get_open()
get_overdue()
get_by_member()
update_status()
```

---

# 154. Payment Repository

Recommended:

```text
create()
get_by_id()
list_by_member()
create_allocation()
reverse()
```

---

# 155. Membership Service API

Recommended:

```text
create_member()
update_member()
create_membership()
renew_membership()
end_membership()
generate_fees()
```

---

# 156. Payment Service API

A dedicated service MAY be used:

```text
register_payment()
allocate_payment()
reverse_payment()
get_member_balance()
```

---

# 157. Membership Accounting Integration API

Conceptually:

```text
record_membership_income()
record_membership_receivable()
record_membership_payment()
```

The implementation SHALL delegate to `AccountingService`.

---

# 158. Payment Transaction

```text
BEGIN
 ↓
validate payment
 ↓
validate allocation
 ↓
save payment
 ↓
save allocations
 ↓
create accounting transaction if required
 ↓
audit
 ↓
COMMIT
```

---

# 159. Payment Failure

If accounting posting fails:

```text
ROLLBACK payment
ROLLBACK allocations
```

No half-created financial payment SHALL remain.

---

# 160. Fee Generation Failure

If one fee fails during a controlled batch operation, the system SHALL either:

```text
rollback entire batch
```

or use an explicitly designed per-member transaction model.

The chosen behaviour SHALL be visible to the administrator.

---

# 161. Recommended Batch Model

For a small association:

```text
preview
 ↓
confirm
 ↓
single transaction
```

is acceptable for annual fee generation.

---

# 162. Membership Reports and Accounting

Membership fee totals SHOULD reconcile with accounting transactions according to the chosen accounting policy.

---

# 163. Reconciliation Test

For a cash-basis model:

```text
member payments
=
membership income postings
```

for the selected period, excluding documented adjustments.

---

# 164. Receivable Test

For a receivable model:

```text
open fees
-
allocated payments
=
outstanding receivables
```

---

# 165. Member Balance Test

For each member:

```text
sum fees
-
sum allocations
=
outstanding
```

with credit handled explicitly.

---

# 166. Membership Scenario 1

```text
Create member
 ↓
Create membership
 ↓
Generate fee
 ↓
Register payment
 ↓
Allocate payment
```

Expected:

```text
fee = PAID
member balance = 0
accounting transaction exists
audit exists
```

---

# 167. Membership Scenario 2

```text
Fee 500
Payment 300
```

Expected:

```text
PARTIALLY_PAID
Outstanding 200
```

---

# 168. Membership Scenario 3

```text
Fee 500
Payment 500
```

Expected:

```text
PAID
Outstanding 0
```

---

# 169. Membership Scenario 4

```text
Fee 500
Payment 600
```

Expected:

```text
Fee PAID
Credit 100 or unallocated 100
```

according to configured policy.

---

# 170. Membership Scenario 5

```text
Duplicate annual fee generation
```

Expected:

```text
no duplicate fee
```

---

# 171. Membership Scenario 6

```text
Former member
 ↓
attempt new fee without active membership
```

Expected:

```text
controlled rejection
```

unless the user first creates a new membership period.

---

# 172. Membership Scenario 7

```text
Disabled membership type
 ↓
attempt new membership
```

Expected:

```text
rejected
```

Historical memberships remain.

---

# 173. Membership Scenario 8

```text
Payment allocation > payment
```

Expected:

```text
rejected
```

---

# 174. Membership Scenario 9

```text
Payment allocation > fee outstanding
```

Expected:

```text
rejected
```

---

# 175. Membership Scenario 10

```text
Payment created
 ↓
Accounting posting fails
```

Expected:

```text
transaction rollback
```

---

# 176. Membership Security Test

Read-only user attempts:

```text
CREATE_MEMBER
```

Expected:

```text
DENIED
```

---

# 177. Membership Payment Security Test

User without:

```text
REGISTER_MEMBER_PAYMENT
```

attempts payment.

Expected:

```text
DENIED
```

---

# 178. Membership Export Security Test

User without:

```text
EXPORT_MEMBER_DATA
```

attempts export.

Expected:

```text
DENIED
```

---

# 179. Audit Test

Create member.

Expected:

```text
MEMBER_CREATED
```

---

# 180. Payment Audit Test

Register payment.

Expected:

```text
PAYMENT_CREATED
PAYMENT_ALLOCATED
```

and accounting audit where applicable.

---

# 181. Data Integrity Test

Delete member with historical payment.

Expected:

```text
DENIED
```

or controlled archival only.

---

# 182. Membership Performance

For a normal association, member search and member list should remain responsive.

Indexes SHALL support:

```text
member number
name
email
status
```

---

# 183. Test Dataset

Recommended test data:

```text
1,000 members
10 membership types
5 years history
5,000 fees
5,000 payments
```

These are test volumes, not system limits.

---

# 184. Membership Dashboard Metrics

Recommended:

```text
active member count
new members this year
former members
open fees
overdue fees
income this year
```

---

# 185. Membership Dashboard Integrity

Dashboard figures SHALL use the same service/repository queries as reports.

---

# 186. No Duplicate Logic

Do not implement one calculation for:

```text
member balance
```

and another different calculation for the dashboard.

Use a shared service.

---

# 187. Membership Export

Export SHOULD support:

```text
CSV
XLSX
```

where appropriate.

---

# 188. Payment Receipt Export

Payment receipt MAY support:

```text
PDF
```

if the document layer is available.

---

# 189. Communication Integration

Future email functionality SHALL obtain member recipients from the membership service.

---

# 190. Communication Security

Bulk communication SHALL require explicit user action.

AI SHALL not automatically send messages to all members.

---

# 191. AI Boundary

Future AI MAY:

```text
identify overdue patterns
suggest reminders
detect duplicate members
summarise membership trends
```

It SHALL not:

```text
change member status autonomously
delete members
send mass messages without authorisation
create accounting postings without authorisation
```

---

# 192. Autonomous Safety

AI recommendations follow:

```text
INTELLIGENCE
 ↓
RECOMMENDATION
 ↓
AUTHORISATION
 ↓
EXECUTION
```

---

# 193. Membership Circuit Breaker

If membership-to-accounting reconciliation fails:

```text
stop automatic posting
```

and require review.

---

# 194. Membership Safe State

If member data is readable but accounting is unavailable:

```text
read-only member functions may continue
financial write operations stop
```

where technically safe.

---

# 195. Payment Safe State

If accounting cannot accept a payment transaction:

```text
payment remains uncommitted
```

rather than appearing paid without accounting support.

---

# 196. Recovery

After failure:

```text
verify payment
verify accounting
verify audit
```

before retrying.

---

# 197. Retry Safety

Retrying a failed payment operation SHALL not duplicate:

```text
payment
allocation
accounting voucher
```

---

# 198. Membership Migration

Existing member data imports SHALL map:

```text
old member id
→
new member record
```

without losing historical references.

---

# 199. Legacy Member Numbers

If importing an existing register, legacy member numbers SHOULD be retained where practical.

---

# 200. Import Validation

Before import:

```text
preview
duplicate detection
required fields
format validation
```

---

# 201. Import Commit

Import SHALL be transactional.

---

# 202. Import Audit

Import SHALL record:

```text
actor
date
source
number of records
result
```

---

# 203. Membership Configuration

Configuration MAY include:

```text
default membership type
default fee
default due date offset
member number format
```

---

# 204. Configuration Authority

Only authorised administrators should change membership configuration.

---

# 205. Configuration Audit

Material configuration changes SHALL be audited.

---

# 206. Membership Governance

The association decides:

```text
who may create members
who may change membership
who may register payments
who may export data
```

MFM enforces those decisions technically.

---

# 207. No Autonomous Authority

MFM SHALL not grant membership administration rights based on usage patterns.

---

# 208. Membership Closure

When a membership ends:

```text
historical fees remain
payments remain
accounting remains
```

Only current entitlement changes.

---

# 209. Membership Reactivation

Reactivation should create a new period unless the existing period is merely temporarily inactive by policy.

---

# 210. Historical Accuracy

Reports for a past date SHALL use the membership state applicable to that date where the required historical model is available.

---

# 211. Membership as-of Reporting

A future enhancement may provide:

```text
active members as of date
```

using membership periods.

---

# 212. Current Member Query

Current membership:

```text
start_date <= today
AND
(end_date IS NULL OR end_date >= today)
AND
status = ACTIVE
```

subject to the association's policy.

---

# 213. Overdue Query

```text
status IN (OPEN, PARTIALLY_PAID)
AND due_date < today
```

---

# 214. Member Balance Query

Aggregate:

```text
fees
-
allocations
```

per member.

---

# 215. Membership Count

Count distinct members with an active current membership.

---

# 216. Fee Generation Query

Select eligible memberships:

```text
active
+
period applicable
+
no existing fee
```

---

# 217. Payment Allocation UI

The GUI SHOULD show:

```text
payment amount
allocated amount
remaining
```

before save.

---

# 218. Fee Allocation UI

For each selected fee:

```text
fee amount
already paid
outstanding
allocation
```

---

# 219. Payment Validation Display

Example:

```text
Payment:       1,000.00
Allocated:       800.00
Remaining:       200.00
```

---

# 220. Membership Error Messages

Use clear messages:

```text
Member number already exists.
Membership period overlaps an existing active membership.
Fee has already been generated.
Payment exceeds outstanding amount.
You do not have permission to register payments.
```

---

# 221. Technical Error Separation

Do not show:

```text
SQLITE FOREIGN KEY constraint failed
```

to ordinary users.

Log technical details separately.

---

# 222. Membership Tests

Tests SHALL cover:

```text
member creation
member update
membership creation
renewal
fee generation
payment
allocation
balance
accounting integration
security
audit
```

---

# 223. Acceptance Criteria

Membership implementation is accepted when:

```text
member can be created
member can be searched
membership can be created
membership history works
fees can be generated
duplicate fees are prevented
payments can be registered
payments can be allocated
member balance is correct
accounting integration works
audit works
permissions work
```

---

# 224. Release Blockers

Release SHALL be blocked by:

```text
duplicate member numbers
duplicate fees
payment without accounting where accounting is required
incorrect member balance
unauthorised payment registration
loss of historical membership
loss of financial history
uncontrolled personal-data export
```

---

# 225. Implementation Order

Implement:

```text
1. members table
2. membership types
3. memberships
4. member repository
5. membership repository
6. MemberService
7. membership GUI
8. fees
9. payments
10. allocations
11. AccountingService integration
12. reports
13. audit
14. tests
```

---

# 226. First Membership Milestone

```text
Create member
 ↓
Create membership
 ↓
View member
 ↓
View membership history
```

---

# 227. Second Membership Milestone

```text
Generate fee
 ↓
View outstanding fee
```

---

# 228. Third Membership Milestone

```text
Register payment
 ↓
Allocate payment
 ↓
Accounting transaction
 ↓
Member balance = 0
```

---

# 229. Fourth Membership Milestone

Add:

```text
reports
exports
reminder list
dashboard
```

---

# 230. Integration Test

Complete end-to-end:

```text
Create member
 ↓
Create membership
 ↓
Generate annual fee
 ↓
Register payment
 ↓
Allocate payment
 ↓
Post accounting transaction
 ↓
View member balance
 ↓
View accounting report
 ↓
View audit
```

Expected:

```text
membership
+
payment
+
accounting
+
audit
```

remain consistent.

---

# 231. Example Membership Chart

The membership module should not assume a fixed account structure.

Instead configuration may map:

```text
membership income → selected income account
bank/cash → selected asset account
receivable → selected receivable account
```

---

# 232. Accounting Mapping

Membership configuration MAY contain:

```text
membership_income_account_id
receivable_account_id
```

Bank/cash account is selected from the payment method or payment setup.

---

# 233. Mapping Validation

Before financial posting:

```text
required account mapping exists
account active
account type appropriate
```

---

# 234. Missing Mapping

If mapping is missing:

```text
financial operation denied
```

rather than posting to a guessed account.

---

# 235. Payment Method Mapping

Example:

```text
BANK → bank account
CASH → cash account
```

---

# 236. No Hard-Coded Account Numbers

Code SHALL not assume:

```text
1000 = Bank
4000 = Membership
```

as universal values.

Those are configuration examples only.

---

# 237. Membership Configuration Repository

Recommended:

```text
MembershipConfigurationRepository
```

or use existing application configuration.

---

# 238. Membership Service Dependency

Conceptually:

```text
MembershipService
 ↓
SecurityContext
 ↓
MembershipRepository
 ↓
AccountingService
 ↓
AuditService
```

---

# 239. Payment Service Dependency

```text
PaymentService
 ↓
SecurityContext
 ↓
PaymentRepository
 ↓
AccountingService
 ↓
AuditService
```

---

# 240. Circular Dependency Avoidance

AccountingService SHALL not depend on MembershipService.

Instead:

```text
MembershipService → AccountingService
```

This keeps accounting as the financial core.

---

# 241. Event Alternative

A future event mechanism MAY notify membership of accounting results.

Not required for v1.0.

---

# 242. Database Transaction Boundary

Membership and accounting changes that represent one financial event SHALL be atomic where the database architecture supports it.

---

# 243. Cross-Service Transaction

Preferred:

```text
PaymentService
 ↓
AccountingService
 ↓
same transaction context
```

rather than two independent commits.

---

# 244. Cross-Service Failure

If payment is saved but accounting fails:

```text
ROLLBACK
```

---

# 245. Audit Failure

If mandatory audit fails:

```text
ROLLBACK
```

for material operations.

---

# 246. Membership Data Integrity

Foreign keys SHALL be enabled.

---

# 247. SQLite Foreign Keys

Application startup SHALL explicitly enable SQLite foreign key enforcement for each connection.

---

# 248. Transaction Isolation

The existing database foundation SHALL provide appropriate transaction handling.

---

# 249. Test Isolation

Membership tests SHALL use an isolated test database.

---

# 250. Seed Membership Types

Test/initial configuration may seed:

```text
Ordinary
Family
Supporter
```

but production defaults SHALL remain configurable.

---

# 251. No Mandatory Member Type

The system SHALL not force an association to use a specific membership taxonomy.

---

# 252. Member Search

Search SHOULD be case-insensitive and accent-tolerant where practical.

---

# 253. Danish Characters

The system SHALL correctly support:

```text
Æ
Ø
Å
```

and other Unicode characters.

---

# 254. Sorting

Member lists SHOULD sort by:

```text
last name
first name
member number
```

as appropriate.

---

# 255. Member Number Display

Member numbers SHOULD be displayed consistently with leading zeros if configured.

---

# 256. Member Form Usability

The member form SHOULD minimise duplicate entry.

---

# 257. Required Member Fields

At minimum:

```text
first name
last name
```

Member number is generated.

---

# 258. Membership Required

A member record MAY exist without active membership.

This supports former and pending members.

---

# 259. Pending Membership

A future status:

```text
PENDING
```

may be added if applications are introduced.

Not required for v1.0.

---

# 260. Membership Application

Not required for v1.0.

---

# 261. Member Communication Preferences

Future:

```text
email consent
postal preference
```

may be added according to the association's needs and applicable requirements.

---

# 262. Notes Security

Notes are personal data and SHALL be protected like other member fields.

---

# 263. Audit Privacy

Audit should identify the action without unnecessarily copying full member records.

---

# 264. Export Audit

Example:

```text
MEMBER_DATA_EXPORTED
actor = admin
scope = active members
timestamp
```

---

# 265. Report Export

Financial member reports may contain both personal and financial data.

They require appropriate permissions.

---

# 266. Membership Backup

Member data SHALL be included in normal application backups.

---

# 267. Restore Test

After restore:

```text
member count
membership history
fees
payments
allocations
```

SHALL be verified.

---

# 268. Migration Test

Database migrations SHALL preserve:

```text
member IDs
membership IDs
fee IDs
payment IDs
```

where possible.

---

# 269. Versioning

Schema changes SHALL be handled by the existing migration framework.

---

# 270. No Manual SQL

Administrators SHALL not need to edit membership tables manually.

---

# 271. Administrative Recovery

If a member record becomes inconsistent, a controlled repair process SHALL be preferred over direct database editing.

---

# 272. Membership Integrity Check

A diagnostic function MAY check:

```text
membership references valid member
fee references valid membership
payment allocations valid
allocation totals valid
```

---

# 273. Integrity Failure

Detected corruption SHALL:

```text
flag record
prevent unsafe financial action
provide diagnostic information
```

---

# 274. Membership Health Check

The application MAY show:

```text
Membership data: OK
Fee allocations: OK
Accounting integration: OK
```

---

# 275. Health Check Security

Detailed diagnostics SHALL be restricted to administrators.

---

# 276. Membership Acceptance Report

The module SHOULD be able to produce:

```text
member count
active count
fee total
payment total
outstanding total
```

for a selected period.

---

# 277. Reconciliation Acceptance

For the same period:

```text
membership payment total
```

SHOULD reconcile to:

```text
membership-related accounting postings
```

according to policy.

---

# 278. Accounting Source of Truth

If a discrepancy exists:

```text
Accounting
```

remains the authoritative financial ledger.

Membership records must be corrected through controlled operations.

---

# 279. Membership Source of Truth

For membership status:

```text
MembershipService / membership records
```

remain authoritative.

---

# 280. Clear Boundary

```text
WHO IS A MEMBER?
→ MEMBERSHIP

HOW MUCH MONEY WAS POSTED?
→ ACCOUNTING

WHICH PAYMENT BELONGS TO WHICH FEE?
→ PAYMENT ALLOCATION
```

---

# 281. Governance

The association defines membership policy.

MFM implements it.

---

# 282. Policy Examples

The association decides:

```text
annual fee
due date
membership categories
renewal policy
former member handling
payment methods
```

---

# 283. No Embedded Policy

Do not hard-code:

```text
annual fee = 500
```

or:

```text
renewal date = January 1
```

into business logic.

---

# 284. Configuration Example

```text
membership_type = Ordinary
default_fee = 500.00
due_days = 30
```

These are configuration values.

---

# 285. Future Pricing

Future versions may support:

```text
age-based fees
family discounts
campaign discounts
prorating
```

without redesigning the core member entity.

---

# 286. Discount Boundary

Discounts are not required for v1.0.

---

# 287. Fee Calculation Service

If fee calculation becomes complex, use:

```text
MembershipFeeService
```

rather than embedding rules in GUI code.

---

# 288. Fee Calculation Principle

```text
INPUT
membership
period
configuration
 ↓
FEE CALCULATION
 ↓
EXPLICIT RESULT
```

---

# 289. No Hidden Fee Changes

The generated fee SHALL show its calculated basis where practical.

---

# 290. Fee Description

Example:

```text
Membership fee 2026 — Ordinary membership
```

---

# 291. Payment Description

Example:

```text
Membership payment — member 0042
```

The accounting description SHALL avoid unnecessary personal details.

---

# 292. Accounting Privacy

Where possible, accounting descriptions should use:

```text
member number
```

rather than full name.

---

# 293. Receipt Privacy

Receipts may contain the member's name because they are delivered to the member.

---

# 294. Audit Privacy

Audit should use member ID/number where possible.

---

# 295. Membership Reports and GDPR

Export screens SHOULD clearly indicate when personal data is included.

---

# 296. Export Confirmation

For broad member exports, the GUI SHOULD request confirmation.

---

# 297. Security Boundary

The membership module SHALL not bypass:

```text
SecurityContext
```

for background operations.

---

# 298. Scheduled Operations

Future automatic fee generation SHALL run as an explicitly authorised system operation with audit.

It SHALL not invent authority.

---

# 299. Future Automation

Possible:

```text
annual fee generation
overdue reminder preparation
membership expiry report
```

Human approval remains appropriate for v1.0.

---

# 300. AI Membership Analysis

AI MAY analyse:

```text
member trends
renewal rates
fee collection
```

but recommendations remain advisory.

---

# 301. AI Safety

AI SHALL not:

```text
delete member
cancel fee
reverse payment
change membership status
```

without explicit authorised execution.

---

# 302. Failure Handling

If membership database is unavailable:

```text
membership write operations stop
```

---

# 303. Read-Only Degradation

If technically possible, safe read-only reporting may continue from available data.

---

# 304. Accounting Failure

If accounting is unavailable:

```text
payment financial completion stops
```

---

# 305. Retry

Retry shall use idempotent operation checks.

---

# 306. Duplicate Prevention

Before creating:

```text
fee
payment
allocation
```

the service SHALL check relevant existing state.

---

# 307. Transaction Recovery

After an interrupted transaction, database recovery SHALL leave either:

```text
complete transaction
```

or:

```text
no transaction
```

not an ambiguous half-state.

---

# 308. Membership Test Matrix

| Area | Test |
|---|---|
| Member | Create/update/search |
| Membership | Create/renew/end |
| Fee | Generate/cancel |
| Payment | Create/allocate/reverse |
| Accounting | Posting/reconciliation |
| Security | Permission enforcement |
| Audit | Event creation |
| Integrity | Foreign keys/duplicates |
| Recovery | Rollback/retry |

---

# 309. Definition of Done

The membership module is complete when:

```text
MEMBERS
+
MEMBERSHIPS
+
FEES
+
PAYMENTS
+
ALLOCATIONS
+
ACCOUNTING
+
SECURITY
+
AUDIT
+
REPORTS
+
TESTS
```

work together.

---

# 310. Final Membership Architecture

```text
                         SECURITY
                            ↓
USER → MEMBERSHIP GUI → MembershipService
                            ↓
                    ┌───────┴────────┐
                    ↓                ↓
              Membership DB     AccountingService
                    ↓                ↓
                 REPORTS          AUDIT
                    ↑                ↑
                    └──── Payments ──┘
```

---

# 311. Final Membership Rules

```text
RULE 1
Member numbers are unique and historically stable.

RULE 2
Historical members are not physically deleted.

RULE 3
Membership periods preserve history.

RULE 4
Generated fees retain their historical amount.

RULE 5
Payments cannot exceed their own amount or allocated fee balance.

RULE 6
Membership financial transactions use AccountingService.

RULE 7
Membership services enforce permissions.

RULE 8
Material member and payment changes are auditable.

RULE 9
Duplicate fee generation is prevented.

RULE 10
Financial failures roll back membership payment transactions.

RULE 11
Personal data exports require explicit authority.

RULE 12
The module remains proportionate to a small non-profit association.
```

---

# 312. Next Implementation Layer

The next concrete implementation file SHALL be:

```text
MFM v1.0 PROJECT & BUDGET IMPLEMENTATION
```

It will connect:

```text
PROJECTS
+
BUDGETS
+
PROJECT EXPENSES
+
ACCOUNTING
+
DOCUMENTS
```

using the existing:

```text
Database Foundation
Security
Audit
Accounting Core
Membership
```

---

# 313. Final Governing Principle

> **MFM shall make it simple to know who belongs to the association, what each member owes, what has been paid, and how every financial consequence is connected to the accounting record without duplicating financial truth.**

# END OF MFM v1.0 MEMBERSHIP & MEMBER MANAGEMENT IMPLEMENTATION
