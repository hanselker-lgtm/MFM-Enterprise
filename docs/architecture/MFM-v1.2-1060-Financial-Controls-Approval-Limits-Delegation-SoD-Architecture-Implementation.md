# MFM v1.2-1060 – Financial Controls, Approval Limits, Delegation & Segregation of Duties Architecture Implementation

Version: 1.2

Document ID: MFM-v1.2-1060

Status: Financial Controls, Approval Limits, Delegation & Segregation of Duties Implementation Baseline

---

# 1. Purpose

This document defines the Financial Controls, Approval Limits, Delegation and Segregation of Duties architecture implementation baseline for MaritimForeningsManager (MFM) v1.2.

It extends:

- MFM v1.2-1000 – Identity, Authentication, Authorization & Access Management Architecture Implementation
- MFM v1.2-1010 – Organization, Membership, Roles & Organizational Structure Architecture Implementation
- MFM v1.2-1030 – Membership Fees, Dues, Billing & Payment Architecture Implementation
- MFM v1.2-1040 – Accounting Integration, Financial Posting & Reconciliation Architecture Implementation
- MFM v1.2-1050 – Financial Reporting, Budgeting, Forecasting & Management Accounting Architecture Implementation

The purpose is to establish a controlled financial authorization framework that prevents unauthorized financial actions, supports approval thresholds, separates incompatible duties and provides complete accountability for financial decisions.

The document establishes:

- Financial Control Architecture
- Control Objectives
- Preventive Controls
- Detective Controls
- Corrective Controls
- Approval Authority
- Approval Limits
- Delegation
- Delegation Periods
- Delegation Scope
- Segregation of Duties
- Incompatible Duties
- Maker / Checker Controls
- Four-Eyes Principle
- Financial Roles
- Financial Permissions
- Transaction Approval
- Budget Approval
- Payment Approval
- Refund Approval
- Write-Off Approval
- Adjustment Approval
- Journal Approval
- Purchase Approval
- Commitment Approval
- Contract Approval
- Bank Payment Approval
- Cash Handling Controls
- Expense Claims
- Reimbursement Approval
- Exception Approval
- Emergency Approval
- Temporary Access
- Approval Escalation
- Approval Substitution
- Approval Routing
- Approval Evidence
- Approval Expiry
- Approval Revocation
- Threshold Management
- Multi-Level Approval
- Parallel Approval
- Sequential Approval
- Conditional Approval
- Conflict of Interest
- Self-Approval Prevention
- Related-Party Controls
- Financial Monitoring
- Control Testing
- Control Evidence
- Control Exceptions
- Control Deficiencies
- Remediation
- Financial Audit
- Management Review
- Access Review
- Delegation Review
- Periodic Certification
- Financial Incident Management
- Recovery
- Migration
- Testing
- Definition of Ready / Done Gates

---

# 2. Financial Control Authority Principle

Financial controls must protect the integrity of financial decisions and transactions without creating a competing accounting authority.

```text
Financial Request
        |
        v
Authorization Rules
        |
        v
Approval Routing
        |
        v
Authorized Decision
        |
        v
Accounting / Operational Processing
        |
        v
Reconciliation & Review
```

---

# 3. Control Authority

> **Financial control rules govern who may initiate, approve, execute, review and correct financial actions; Accounting Core remains authoritative for ledger state.**

---

# 4. Control Objective

Every material financial action must be:

```text
Authorized

Traceable

Appropriately Approved

Executed by an Authorized Actor

Reconciled

Reviewable
```

---

# 5. Preventive Control

A preventive control stops an unauthorized or invalid financial action before execution.

---

# 6. Detective Control

A detective control identifies an unauthorized, incorrect or anomalous action after or during processing.

---

# 7. Corrective Control

A corrective control restores the intended state through an authorized remediation process.

---

# 8. Control Ownership

Every material financial control must have an accountable owner.

---

# 9. Control Definition

A control definition should specify:

```text
Purpose

Risk

Trigger

Owner

Frequency

Evidence

Expected Result

Exception Handling
```

---

# 10. Control Frequency

Controls may operate:

```text
Per Transaction

Daily

Weekly

Monthly

Quarterly

Annually

Event-Driven
```

---

# 11. Control Evidence

Financial controls must produce sufficient evidence to demonstrate execution.

---

# 12. Evidence Integrity

Control evidence must be protected against unauthorized alteration.

---

# 13. Approval Authority

Approval authority defines who may authorize a financial action.

---

# 14. Approval Limit

An approval limit defines the maximum financial authority available to a role or person under defined conditions.

---

# 15. Approval Scope

Approval authority must specify:

```text
Amount

Currency

Transaction Type

Organization

Project

Funding Source

Period
```

where applicable.

---

# 16. Approval Currency

Approval limits must define how foreign-currency transactions are treated.

---

# 17. Approval Conversion

Currency conversion for approval thresholds must follow a documented rule.

---

# 18. Threshold Basis

Thresholds may be based on:

```text
Gross Amount

Net Amount

Tax-Inclusive Amount

Tax-Exclusive Amount
```

according to policy.

---

# 19. Threshold Ownership

Approval thresholds require accountable financial ownership.

---

# 20. Threshold Versioning

Changes to approval thresholds must be versioned or effective-dated.

---

# 21. Threshold Historical Integrity

Historical approval decisions must remain interpretable using the rules applicable at the time.

---

# 22. Approval Levels

A financial approval model may include:

```text
Level 1

Level 2

Level 3

Executive / Board
```

according to organizational policy.

---

# 23. Multi-Level Approval

Higher-value or higher-risk transactions may require multiple approval levels.

---

# 24. Sequential Approval

Sequential approval requires one approval stage to complete before the next.

---

# 25. Parallel Approval

Parallel approval allows multiple required approvers to act independently before completion.

---

# 26. Conditional Approval

Approval routing may depend on:

```text
Amount

Category

Risk

Project

Funding Source

Transaction Type
```

---

# 27. Approval Completion

A transaction is approved only when all required approvals have been completed.

---

# 28. Approval Rejection

A rejection must record the decision and reason where required.

---

# 29. Approval Withdrawal

An approver may withdraw approval only where the workflow explicitly permits it.

---

# 30. Approval Expiry

Approvals may expire after a defined period.

---

# 31. Approval Revalidation

Material changes after approval may require reapproval.

---

# 32. Approval Change Trigger

Examples include:

```text
Amount Changed

Supplier Changed

Funding Source Changed

Account Changed

Project Changed

Scope Changed
```

---

# 33. Approval Evidence

Approval evidence should contain:

```text
Approver

Timestamp

Decision

Transaction

Approval Rule

Comments
```

where applicable.

---

# 34. Approval Audit

Approval actions must be auditable.

---

# 35. Maker / Checker

The maker / checker principle separates transaction creation from approval or review.

---

# 36. Four-Eyes Principle

Material financial actions may require two independent persons to complete the process.

---

# 37. Self-Approval Prevention

A user must not approve their own transaction where self-approval is prohibited.

---

# 38. Self-Approval Detection

The system should detect prohibited self-approval attempts.

---

# 39. Self-Approval Override

Any exceptional override must require explicit authority and audit evidence.

---

# 40. Segregation of Duties

Segregation of duties separates incompatible financial responsibilities.

---

# 41. Incompatible Duties

Examples may include:

```text
Create Payment

Approve Payment

Execute Payment

Reconcile Payment
```

---

# 42. Accounting Incompatibility

Other incompatible combinations may include:

```text
Create Journal

Approve Journal

Review Reconciliation
```

---

# 43. Refund Incompatibility

Where risk requires it:

```text
Create Refund

Approve Refund

Execute Refund

Reconcile Refund
```

should be separated.

---

# 44. Vendor Incompatibility

Where procurement is supported:

```text
Create Supplier

Approve Supplier

Create Purchase

Approve Purchase

Pay Supplier
```

may require separation.

---

# 45. Budget Incompatibility

Where appropriate:

```text
Create Budget

Approve Budget

Certify Budget
```

should be separated.

---

# 46. Delegation

Delegation transfers defined approval authority temporarily or permanently according to policy.

---

# 47. Delegation Scope

A delegation must define its scope.

---

# 48. Delegation Start

A delegation must have a start date.

---

# 49. Delegation End

A temporary delegation must have an end date.

---

# 50. Delegation Reason

Delegation should have a reason where required.

---

# 51. Delegation Owner

The delegating authority remains accountable according to policy unless responsibility is formally transferred.

---

# 52. Delegation Acceptance

Delegated authority may require acceptance by the delegate.

---

# 53. Delegation Limits

A delegate must not receive broader authority than the defined delegation.

---

# 54. Delegation Inheritance

Delegated authority must not automatically create further delegation rights.

---

# 55. Sub-Delegation

Sub-delegation is prohibited unless explicitly permitted.

---

# 56. Delegation Expiry

Expired delegations must no longer authorize financial actions.

---

# 57. Delegation Revocation

Delegations must be revocable.

---

# 58. Delegation Audit

Delegation creation, modification and revocation must be auditable.

---

# 59. Emergency Delegation

Emergency delegation may be permitted under controlled circumstances.

---

# 60. Emergency Delegation Duration

Emergency delegations should be time-limited.

---

# 61. Emergency Delegation Review

Emergency delegations require retrospective review.

---

# 62. Temporary Financial Access

Temporary financial permissions must have explicit expiry.

---

# 63. Access Expiry

Expired temporary access must be automatically disabled where technically possible.

---

# 64. Approval Routing

The approval engine determines the required approval path.

---

# 65. Routing Inputs

Routing may use:

```text
Transaction Type

Amount

Organization

Project

Account

Funding Source

Risk

Requester
```

---

# 66. Routing Determinism

For the same rule set and transaction state, routing should produce deterministic results.

---

# 67. Routing Version

Approval routing rules must be versioned or effective-dated.

---

# 68. Historical Routing

Historical approvals must remain interpretable using the routing rules applicable at the time.

---

# 69. Approval Candidate

An approval candidate must satisfy all required role, scope and authority conditions.

---

# 70. Approval Conflict

The system should identify when a candidate has an incompatible duty.

---

# 71. Approval Fallback

Fallback approvers must be explicitly defined.

---

# 72. No Uncontrolled Fallback

The system must not automatically select an arbitrary administrator as a fallback approver.

---

# 73. Escalation

Unresolved approvals may be escalated according to policy.

---

# 74. Escalation Trigger

Triggers may include:

```text
Age

Amount

Risk

Deadline

Criticality
```

---

# 75. Escalation Owner

Escalation ownership must be defined.

---

# 76. Approval Reminder

Approval reminders may be sent according to notification policy.

---

# 77. Reminder Frequency

Reminder frequency must be controlled.

---

# 78. Approval Fatigue

The approval process should avoid unnecessary approvals while preserving required financial control.

---

# 79. Transaction Approval

Transactions requiring approval must not be executed before approval completion.

---

# 80. Payment Approval

Payments above defined thresholds may require approval.

---

# 81. Bank Payment Approval

Bank payments should follow defined approval limits and maker/checker controls.

---

# 82. Cash Payment Approval

Cash payments must follow approved cash-handling authority.

---

# 83. Refund Approval

Refunds must follow defined approval thresholds.

---

# 84. Write-Off Approval

Write-offs must require approval according to amount and financial risk.

---

# 85. Adjustment Approval

Financial adjustments must follow defined approval rules.

---

# 86. Journal Approval

Manual or material journals may require independent approval.

---

# 87. Purchase Approval

Purchases may require approval before commitment.

---

# 88. Commitment Approval

Financial commitments should be controlled before an obligation is created.

---

# 89. Contract Approval

Financial contracts should follow defined authorization levels.

---

# 90. Expense Claim Approval

Expense claims require review and approval according to policy.

---

# 91. Reimbursement Approval

Reimbursements must verify:

```text
Claimant

Amount

Evidence

Purpose

Eligibility

Approval
```

---

# 92. Related-Party Transaction

Related-party transactions require additional controls where applicable.

---

# 93. Conflict of Interest

Users must not participate in financial approval where a conflict of interest prevents impartial decision-making.

---

# 94. Conflict Declaration

Conflicts may require explicit declaration.

---

# 95. Conflict Escalation

Declared conflicts must be routed according to policy.

---

# 96. Financial Role

Financial roles may include:

```text
Requester

Budget Owner

Approver

Treasurer

Bookkeeper

Payment Executor

Reconciler

Reviewer

Auditor
```

---

# 97. Role Separation

Roles must be designed to prevent prohibited combinations of duties.

---

# 98. Permission vs Authority

Having a technical permission does not automatically establish financial approval authority.

---

# 99. Authority Source

Financial authority should originate from approved organizational and financial governance.

---

# 100. Organizational Scope

Approval authority may be restricted by organizational unit.

---

# 101. Project Scope

Approval authority may be restricted by project.

---

# 102. Funding Scope

Approval authority may be restricted by funding source.

---

# 103. Account Scope

Approval authority may be restricted by account category.

---

# 104. Transaction Scope

Approval authority may be limited to defined transaction types.

---

# 105. Period Scope

Approval authority may be restricted to defined financial periods.

---

# 106. Board / Executive Approval

Material financial decisions may require board or executive approval.

---

# 107. Board Approval Evidence

Board-level financial approvals should retain appropriate evidence.

---

# 108. Approval Minutes

Where governance requires formal minutes, the approval should be traceable to the relevant meeting record.

---

# 109. Written Resolution

Written financial resolutions may be used where permitted.

---

# 110. Resolution Traceability

Resolutions must link to the approved financial action.

---

# 111. Budget Approval

Budget approval should confirm:

```text
Amount

Period

Scope

Funding

Owner
```

where applicable.

---

# 112. Budget Change Approval

Changes to an approved budget may require reapproval based on defined thresholds.

---

# 113. Forecast Approval

Formal forecasts may require management approval.

---

# 114. Financial Report Certification

Formal financial reports may require independent review or certification.

---

# 115. Certification Independence

Certification should be performed by an appropriately independent person where required.

---

# 116. Control Review

Financial controls should be reviewed periodically.

---

# 117. Control Testing

Controls should be tested according to risk and frequency.

---

# 118. Test Evidence

Control test results must be retained.

---

# 119. Control Failure

A failed control must create an exception or remediation process.

---

# 120. Control Exception

An exception represents a deviation from the defined control.

---

# 121. Exception Classification

Exceptions may be:

```text
Low

Medium

High

Critical
```

---

# 122. Control Deficiency

A control deficiency indicates that a control does not adequately address its intended risk.

---

# 123. Material Control Deficiency

Material deficiencies require escalation according to financial governance.

---

# 124. Remediation

Control deficiencies require corrective action.

---

# 125. Remediation Owner

Every remediation action must have an owner.

---

# 126. Remediation Due Date

Material remediation should have a due date.

---

# 127. Remediation Verification

Completed remediation must be independently verified where required.

---

# 128. Compensating Control

Where a control is temporarily unavailable, an approved compensating control may be used.

---

# 129. Compensating Control Duration

Compensating controls should be time-limited.

---

# 130. Compensating Control Evidence

Use of a compensating control must be documented.

---

# 131. Financial Monitoring

Financial controls should be monitored through:

```text
Approval Exceptions

Self-Approval Attempts

Threshold Breaches

Expired Delegations

Unusual Adjustments

Failed Reconciliations

Emergency Access
```

---

# 132. Threshold Monitoring

Threshold breaches must be visible to authorized financial personnel.

---

# 133. Unusual Transaction Monitoring

Material or unusual financial activity may require review.

---

# 134. Approval Analytics

Management may monitor:

```text
Approval Volume

Approval Time

Rejection Rate

Escalation Rate

Delegation Usage
```

---

# 135. Approval Time

Approval-time metrics should distinguish normal processing from escalated cases.

---

# 136. Delegation Analytics

Delegation reporting may identify:

```text
Active Delegations

Expired Delegations

Emergency Delegations

High-Risk Delegations
```

---

# 137. SoD Monitoring

Segregation-of-duties conflicts should be periodically evaluated.

---

# 138. SoD Conflict

A conflict exists when one actor has incompatible authority combinations.

---

# 139. SoD Exception

Exceptions to segregation rules require explicit approval.

---

# 140. SoD Exception Expiry

SoD exceptions must have an expiry date.

---

# 141. SoD Exception Review

Exceptions should be reviewed periodically.

---

# 142. Access Review

Financial permissions should be reviewed periodically.

---

# 143. Access Review Scope

Review may cover:

```text
Financial Roles

Approval Limits

Delegations

Temporary Access

Privileged Access
```

---

# 144. Access Certification

Managers or designated authorities may certify continued access.

---

# 145. Access Revocation

Unnecessary financial access must be revoked promptly.

---

# 146. Role Change

Organizational changes must trigger review of financial authority.

---

# 147. Employment / Membership End

When a user's authorized role ends, financial authority must be removed according to policy.

---

# 148. Leave of Absence

Temporary absence may trigger delegation or suspension of approval authority.

---

# 149. Approval Continuity

Business continuity must not result in uncontrolled financial authority.

---

# 150. Approval Outage

If the approval system is unavailable, emergency procedures must be explicit.

---

# 151. Emergency Financial Process

Emergency financial actions must use predefined emergency authority.

---

# 152. Emergency Evidence

Emergency transactions require enhanced documentation.

---

# 153. Post-Emergency Review

Emergency financial actions must be reviewed after normal operations resume.

---

# 154. No Emergency Bypass

Emergency procedures must not become a routine bypass for normal controls.

---

# 155. Manual Approval

Manual approvals may be used only through controlled procedures.

---

# 156. Manual Approval Evidence

Manual approval should capture:

```text
Approver

Date

Transaction

Decision

Reason

Evidence
```

---

# 157. Electronic Approval

Electronic approvals should provide non-repudiable or strongly attributable evidence appropriate to risk.

---

# 158. Approval Authentication

Material approvals may require reauthentication or step-up authentication.

---

# 159. Approval Session

Approval sessions must be protected against unauthorized reuse.

---

# 160. Approval Notification

Approvers should receive sufficient transaction context to make an informed decision.

---

# 161. Approval Data Minimization

Approval interfaces should expose only necessary information.

---

# 162. Approval Link Security

Approval links must be authenticated and bound to the intended action where applicable.

---

# 163. Expired Approval Link

Expired approval links must not authorize transactions.

---

# 164. Approval Delegation Conflict

A delegate must not approve a transaction when another incompatible role conflict exists.

---

# 165. Approval Reassignment

Reassignment must be authorized and auditable.

---

# 166. Approval Cancellation

Cancelled transactions must no longer be approvable.

---

# 167. Approval Amendment

Materially amended transactions require revalidation.

---

# 168. Approval Replay

A previous approval must not automatically apply to a materially changed transaction.

---

# 169. Approval Idempotency

Repeated approval requests must not create multiple approval effects.

---

# 170. Approval Event

Approval actions may generate events such as:

```text
ApprovalRequested

ApprovalGranted

ApprovalRejected

ApprovalExpired

ApprovalEscalated

ApprovalRevoked
```

---

# 171. Approval Event Governance

Approval events follow MFM v1.2-920.

---

# 172. Workflow Governance

Approval workflows follow MFM v1.2-930.

---

# 173. Rules Governance

Approval rules follow MFM v1.2-940.

---

# 174. Identity Governance

Financial authorization follows MFM v1.2-1000.

---

# 175. Audit Governance

Financial approval evidence follows applicable audit and records-management architecture.

---

# 176. Financial Incident

Examples include:

```text
Unauthorized Payment

Self-Approval

Expired Delegation Used

Threshold Bypass

Unauthorized Refund

Unauthorized Write-Off

SoD Violation

Approval Fraud
```

---

# 177. Unauthorized Payment Incident

Contain the transaction, determine accounting impact and initiate controlled remediation.

---

# 178. Self-Approval Incident

Investigate the approval path and verify whether the transaction was otherwise authorized.

---

# 179. Expired Delegation Incident

Determine whether the action occurred after authority expiry and escalate according to policy.

---

# 180. Threshold Bypass Incident

Identify why routing failed and assess all affected transactions.

---

# 181. Unauthorized Refund Incident

Contain refund processing, reconcile financial effects and investigate access.

---

# 182. Unauthorized Write-Off Incident

Review the write-off authority and correct financial consequences through Accounting Core.

---

# 183. SoD Violation Incident

Identify incompatible access and determine whether financial exposure exists.

---

# 184. Approval Fraud Incident

Escalate through security and financial incident processes.

---

# 185. Financial Recovery

Approval state and control evidence must be recoverable.

---

# 186. Recovery Integrity

Recovery must not create duplicate approvals or bypass required controls.

---

# 187. Recovery Revalidation

In-flight financial actions may require revalidation after recovery.

---

# 188. Delegation Recovery

Active delegations must be restored with correct effective dates.

---

# 189. Approval Queue Recovery

Pending approval requests must retain their transaction and routing context.

---

# 190. Migration

Migration must preserve:

```text
Approval History

Delegations

Approval Limits

Role Assignments

Control Exceptions

Certification Evidence
```

where required.

---

# 191. Migration Authority Validation

Migrated approval authority must be validated against current organizational structure.

---

# 192. Migration Expired Authority

Expired historical authority must not become active through migration.

---

# 193. Migration Delegation Validation

Delegations must retain correct start and end dates.

---

# 194. Financial Control Testing

Test:

```text
Approval Limits

Routing

Self-Approval Prevention

Delegation

SoD

Escalation

Revocation
```

---

# 195. Threshold Testing

Test:

```text
Below Threshold

At Threshold

Above Threshold

Multiple Thresholds

Currency Conversion
```

---

# 196. Delegation Testing

Test:

```text
Active

Expired

Revoked

Future-Dated

Emergency
```

---

# 197. SoD Testing

Test prohibited role combinations and approved exceptions.

---

# 198. Approval Workflow Testing

Test:

```text
Sequential

Parallel

Conditional

Rejected

Expired

Escalated

Cancelled
```

---

# 199. Security Testing

Test:

```text
Authentication

Authorization

Step-Up Authentication

Privileged Access

Approval Link Security
```

---

# 200. Audit Testing

Verify approval, delegation and control events are complete and attributable.

---

# 201. Control Definition of Ready

A financial control is Ready when:

- Risk Defined
- Control Objective Defined
- Owner Defined
- Frequency Defined
- Evidence Defined
- Exception Path Defined

---

# 202. Control Definition of Done

A financial control is Done when:

- Control Implemented
- Positive Case Tested
- Failure Case Tested
- Evidence Verified
- Exception Handling Tested
- Ownership Confirmed

---

# 203. Approval Definition of Ready

An approval process is Ready when:

- Transaction Type Defined
- Threshold Defined
- Approvers Defined
- Routing Defined
- SoD Rules Defined
- Escalation Defined
- Evidence Defined

---

# 204. Approval Definition of Done

An approval process is Done when:

- Normal Approval Tested
- Rejection Tested
- Escalation Tested
- Expiry Tested
- Self-Approval Tested
- Delegation Tested
- Audit Verified

---

# 205. Delegation Definition of Ready

Delegation is Ready when:

- Delegator Defined
- Delegate Defined
- Scope Defined
- Start Defined
- End Defined
- Limits Defined
- Revocation Defined

---

# 206. Delegation Definition of Done

Delegation is Done when:

- Activation Tested
- Expiry Tested
- Revocation Tested
- Scope Tested
- Audit Verified

---

# 207. SoD Definition of Ready

Segregation of duties is Ready when:

- Incompatible Duties Identified
- Roles Mapped
- Exceptions Defined
- Review Frequency Defined
- Escalation Defined

---

# 208. SoD Definition of Done

Segregation of duties is Done when:

- Conflicts Detected
- Prohibited Actions Blocked
- Exceptions Tested
- Periodic Review Tested
- Audit Verified

---

# 209. Final Control Principle

> **Every material financial action must be subject to an appropriate control proportional to its value, risk and organizational impact.**

---

# 210. Final Approval Principle

> **No transaction requiring approval may be executed until all mandatory approvals have been completed under the applicable approval rules.**

---

# 211. Final Delegation Principle

> **Delegated authority must be explicit, scoped, time-bound where appropriate, non-transferrable unless permitted and fully auditable.**

---

# 212. Final Segregation Principle

> **No individual should control incompatible stages of a material financial process where segregation of duties is required.**

---

# 213. Final Threshold Principle

> **Approval thresholds must be deterministic, effective-dated, scope-aware and resistant to circumvention through transaction splitting or other manipulation.**

---

# 214. Final Reapproval Principle

> **Material changes to an approved transaction invalidate the approval to the extent defined by policy and must trigger revalidation or reapproval.**

---

# 215. Final Emergency Principle

> **Emergency financial procedures may preserve continuity but must never become an uncontrolled bypass of normal financial governance.**

---

# 216. Final Audit Principle

> **Every approval, delegation, exception and control action must remain attributable and reconstructable.**

---

# 217. Final Accounting Principle

> **Financial controls govern authorization and execution; Accounting Core remains the authoritative source of financial ledger truth.**

---

# 218. Final Governance Principle

> **Every financial control and approval mechanism must have an owner, defined authority, effective dates, scope, evidence, exception handling and periodic review.**

---

# 219. Summary

MFM v1.2-1060 establishes the Financial Controls, Approval Limits, Delegation and Segregation of Duties architecture implementation baseline.

It defines:

- Financial Control Architecture
- Preventive, Detective and Corrective Controls
- Control Objectives
- Control Ownership
- Control Evidence
- Approval Authority
- Approval Limits
- Approval Scope
- Currency Treatment
- Threshold Basis
- Threshold Versioning
- Multi-Level Approval
- Sequential Approval
- Parallel Approval
- Conditional Approval
- Approval Completion
- Approval Rejection
- Approval Expiry
- Approval Revalidation
- Approval Evidence
- Maker / Checker
- Four-Eyes Principle
- Self-Approval Prevention
- Segregation of Duties
- Incompatible Duties
- Payment Approval
- Refund Approval
- Write-Off Approval
- Adjustment Approval
- Journal Approval
- Purchase Approval
- Commitment Approval
- Contract Approval
- Expense Claim Approval
- Reimbursement Approval
- Related-Party Controls
- Conflict of Interest
- Financial Roles
- Financial Permission Boundaries
- Organizational Scope
- Project Scope
- Funding Scope
- Board / Executive Approval
- Budget Approval
- Forecast Approval
- Report Certification
- Delegation
- Delegation Scope
- Delegation Start / End
- Delegation Acceptance
- Delegation Limits
- Sub-Delegation
- Delegation Expiry
- Delegation Revocation
- Emergency Delegation
- Temporary Financial Access
- Approval Routing
- Routing Versioning
- Approval Candidates
- Approval Conflicts
- Fallback Approvers
- Escalation
- Approval Reminders
- Threshold Monitoring
- Approval Analytics
- Delegation Analytics
- SoD Monitoring
- SoD Exceptions
- Access Review
- Access Certification
- Financial Authority Changes
- Emergency Financial Processes
- Manual Approval
- Electronic Approval
- Approval Authentication
- Approval Security
- Approval Events
- Financial Incidents
- Recovery
- Migration
- Financial Control Testing
- Approval Testing
- Delegation Testing
- SoD Testing
- Definition of Ready / Done Gates

The central architectural rules remain:

> **Every material financial action must be subject to an appropriate control proportional to its value, risk and organizational impact.**

> **No transaction requiring approval may be executed until all mandatory approvals have been completed under the applicable approval rules.**

> **Delegated authority must be explicit, scoped, time-bound where appropriate, non-transferrable unless permitted and fully auditable.**

> **No individual should control incompatible stages of a material financial process where segregation of duties is required.**

> **Financial controls govern authorization and execution; Accounting Core remains the authoritative source of financial ledger truth.**

---

# 220. MFM Financial Control Architecture Baseline

MFM v1.2-1060 establishes the controlled authorization foundation for financial approvals, delegations, thresholds, segregation of duties, control monitoring and financial governance.

Future financial-control work should reference this document together with:

- MFM v1.2-730 – Architecture Governance, Decision Records & Strategic Change Control Implementation
- MFM v1.2-740 – Enterprise Integration, Interoperability & External Ecosystem Implementation
- MFM v1.2-750 – Data Exchange, Master Data & Cross-Domain Information Governance Implementation
- MFM v1.2-760 – Information Security Architecture, Zero-Trust Controls & Cyber Resilience Implementation
- MFM v1.2-770 – Privacy Architecture, Data Protection & Personal Information Lifecycle Implementation
- MFM v1.2-780 – Application Architecture, Modular Design & Internal Service Boundary Implementation
- MFM v1.2-800 – Reporting, Analytics, Business Intelligence & Management Information Architecture Implementation
- MFM v1.2-810 – Integration Testing, Quality Assurance & End-to-End Validation Architecture Implementation
- MFM v1.2-840 – Observability, Monitoring, Logging, Alerting & Operational Intelligence Architecture Implementation
- MFM v1.2-850 – Business Continuity, Disaster Recovery, Backup & Resilience Architecture Implementation
- MFM v1.2-860 – Capacity Planning, Performance Engineering & Scalability Architecture Implementation
- MFM v1.2-870 – Configuration Management, Environment Management & Feature Flag Architecture Implementation
- MFM v1.2-880 – Security Operations, Vulnerability Management, Threat Detection & Incident Response Architecture Implementation
- MFM v1.2-890 – Data Lifecycle, Archiving, Retention, Disposal & Records Management Architecture Implementation
- MFM v1.2-900 – Enterprise Data Governance, Data Quality & Information Stewardship Architecture Implementation
- MFM v1.2-910 – API Governance, Service Contracts, Versioning & Integration Interface Architecture Implementation
- MFM v1.2-920 – Event-Driven Architecture, Messaging, Queues & Asynchronous Processing Architecture Implementation
- MFM v1.2-930 – Workflow Orchestration, Business Process Automation & State Machine Architecture Implementation
- MFM v1.2-940 – Rules Engine, Decision Management & Business Rules Architecture Implementation
- MFM v1.2-950 – Document & Content Management, Document Services, Templates & Digital Records Architecture Implementation
- MFM v1.2-960 – Notification, Communication, Messaging & User Engagement Architecture Implementation
- MFM v1.2-970 – Search, Discovery, Indexing & Information Retrieval Architecture Implementation
- MFM v1.2-980 – User Experience, Accessibility, Interaction & Frontend Architecture Implementation
- MFM v1.2-990 – Mobile, Offline, Synchronization & Multi-Device Architecture Implementation
- MFM v1.2-1000 – Identity, Authentication, Authorization & Access Management Architecture Implementation
- MFM v1.2-1010 – Organization, Membership, Roles & Organizational Structure Architecture Implementation
- MFM v1.2-1020 – Membership Lifecycle, Enrollment, Renewal & Retention Architecture Implementation
- MFM v1.2-1030 – Membership Fees, Dues, Billing & Payment Architecture Implementation
- MFM v1.2-1040 – Accounting Integration, Financial Posting & Reconciliation Architecture Implementation
- MFM v1.2-1050 – Financial Reporting, Budgeting, Forecasting & Management Accounting Architecture Implementation

---

# END OF DOCUMENT
