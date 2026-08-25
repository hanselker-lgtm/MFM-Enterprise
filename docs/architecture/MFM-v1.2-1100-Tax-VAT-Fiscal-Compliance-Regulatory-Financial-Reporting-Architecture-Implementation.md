# MFM v1.2-1100 – Tax, VAT, Fiscal Compliance & Regulatory Financial Reporting Architecture Implementation

Version: 1.2

Document ID: MFM-v1.2-1100

Status: Tax, VAT, Fiscal Compliance & Regulatory Financial Reporting Implementation Baseline

---

# 1. Purpose

This document defines the Tax, VAT, Fiscal Compliance and Regulatory Financial Reporting architecture implementation baseline for MaritimForeningsManager (MFM) v1.2.

It extends:

- MFM v1.2-1030 – Membership Fees, Dues, Billing & Payment Architecture Implementation
- MFM v1.2-1040 – Accounting Integration, Financial Posting & Reconciliation Architecture Implementation
- MFM v1.2-1050 – Financial Reporting, Budgeting, Forecasting & Management Accounting Architecture Implementation
- MFM v1.2-1060 – Financial Controls, Approval Limits, Delegation & Segregation of Duties Architecture Implementation
- MFM v1.2-1070 – Procurement, Purchasing, Supplier & Expense Management Architecture Implementation
- MFM v1.2-1080 – Asset Management, Fixed Assets, Inventory & Depreciation Architecture Implementation
- MFM v1.2-1090 – Cash Management, Bank Accounts, Treasury & Liquidity Management Architecture Implementation

The purpose is to establish a controlled fiscal architecture for tax classification, VAT treatment, tax evidence, fiscal reporting, regulatory submissions, tax-period close and compliance monitoring.

The document establishes:

- Tax Architecture
- Fiscal Compliance
- Tax Authority
- Tax Registration
- Tax Identification
- Tax Jurisdiction
- Tax Residence
- VAT Registration
- VAT Status
- VAT Treatment
- VAT Codes
- VAT Rates
- VAT Categories
- VAT Exemptions
- Zero-Rated Transactions
- Outside-Scope Transactions
- Reverse Charge
- Input VAT
- Output VAT
- Recoverable VAT
- Non-Recoverable VAT
- VAT Evidence
- Tax Evidence
- Tax-Inclusive Amounts
- Tax-Exclusive Amounts
- Tax Calculation
- Tax Rounding
- Tax Date
- Supply Date
- Invoice Date
- Payment Date
- Tax Point
- Fiscal Periods
- VAT Periods
- Tax Period Close
- Tax Reconciliation
- VAT Reconciliation
- Tax Return Preparation
- VAT Return Preparation
- Regulatory Financial Reporting
- Tax Reporting
- Fiscal Reporting
- Regulatory Submission
- Submission Status
- Filing Deadlines
- Filing Extensions
- Payment Deadlines
- Tax Liabilities
- VAT Liabilities
- Tax Payments
- Tax Refunds
- Tax Adjustments
- Corrective Returns
- Credit Notes
- Debit Notes
- Tax Invoices
- Invoice Compliance
- Supplier Tax Information
- Customer Tax Information
- Member Tax Information
- Cross-Border Transactions
- EU Transactions
- International Transactions
- Import VAT
- Export Treatment
- Reverse Charge
- Tax Residency
- Withholding Tax
- Payroll Tax Boundary
- Tax Exempt Organizations
- Charitable / Non-Profit Tax Considerations
- Restricted Funding Tax Considerations
- Grants and Donations
- Sponsorship
- Membership Fees
- Event Revenue
- Sales of Goods
- Services
- Asset Disposals
- Procurement Tax Treatment
- Expense Tax Treatment
- Fixed Asset VAT
- Inventory VAT
- Tax Master Data
- Tax Rule Versioning
- Tax Configuration
- Tax Change Management
- Tax Audit Trail
- Tax Evidence Retention
- Tax Risk
- Compliance Monitoring
- Tax Exceptions
- Tax Incidents
- Regulatory Reporting Controls
- Security
- Privacy
- Recovery
- Migration
- Testing
- Definition of Ready / Done Gates

---

# 2. Fiscal Authority Principle

MFM must support fiscal classification and reporting while preserving Accounting Core as the authoritative source for financial ledger state.

```text
Business Transaction
        |
        v
Tax Classification
        |
        v
Tax / VAT Calculation
        |
        v
Accounting Core
        |
        +---- Tax Reconciliation
        |
        +---- Tax Reporting
        |
        v
Regulatory Submission
```

---

# 3. Accounting Authority

> **Accounting Core remains the authoritative source for financial ledger state.**

---

# 4. Tax Authority

Applicable tax authorities and official fiscal requirements determine the legal treatment of tax matters.

---

# 5. Legal Compliance Boundary

MFM provides systems support for tax and fiscal compliance but does not independently determine legal tax obligations without approved rules or professional interpretation.

---

# 6. Tax Jurisdiction

Every tax-relevant transaction should be associated with the applicable tax jurisdiction where required.

---

# 7. Tax Registration

The organization may maintain records of relevant tax registrations.

---

# 8. Tax Registration Record

A registration record may include:

```text
Authority

Registration Number

Jurisdiction

Effective Date

Expiry / End Date

Status
```

---

# 9. Tax Identification Number

Tax identifiers must be stored securely and used consistently.

---

# 10. VAT Registration

Where applicable, VAT registration details must be maintained.

---

# 11. VAT Registration Status

Possible states include:

```text
Not Registered

Pending

Registered

Suspended

Cancelled
```

---

# 12. VAT Registration Scope

VAT registration may apply to defined activities, jurisdictions or periods.

---

# 13. Tax Residence

The organization's tax residence should be defined where relevant.

---

# 14. Tax Classification

Transactions should be classified according to approved tax rules.

---

# 15. Tax Code

Every tax-relevant transaction should use an approved tax code where applicable.

---

# 16. Tax Code Definition

A tax code should define:

```text
Tax Type

Rate

Jurisdiction

Treatment

Effective Date

Reporting Category
```

---

# 17. VAT Code

VAT codes identify approved VAT treatment.

---

# 18. VAT Rate

VAT rates must be controlled and effective-dated.

---

# 19. VAT Category

VAT categories may include:

```text
Standard

Reduced

Zero Rated

Exempt

Outside Scope

Reverse Charge
```

subject to applicable law.

---

# 20. Rate Versioning

Changes to tax rates must not overwrite historical rates applicable to closed periods.

---

# 21. Tax Rule Versioning

Material tax-rule changes must be versioned or effective-dated.

---

# 22. Historical Tax Integrity

Historical transactions must retain the tax treatment applicable at the time of the transaction.

---

# 23. Tax Calculation

Tax calculations must use approved tax rules and rounding policies.

---

# 24. Tax-Inclusive Amount

A tax-inclusive amount includes the applicable tax.

---

# 25. Tax-Exclusive Amount

A tax-exclusive amount excludes the applicable tax.

---

# 26. Tax Amount

Tax amount is calculated according to the applicable rate and taxable base.

---

# 27. Taxable Base

The taxable base must be identifiable for tax-relevant transactions.

---

# 28. Tax Rounding

Tax rounding must follow a documented rule.

---

# 29. Rounding Consistency

The same approved rounding methodology must be applied consistently within a reporting context.

---

# 30. Tax Date

Tax reporting may depend on a defined tax date.

---

# 31. Supply Date

The supply date may determine the applicable tax treatment where required.

---

# 32. Invoice Date

Invoice date must be retained for tax evidence and reporting.

---

# 33. Payment Date

Payment date may be relevant to specific tax treatments or reporting schemes.

---

# 34. Tax Point

Where applicable, the tax point determines the period in which tax becomes reportable.

---

# 35. Fiscal Period

Tax reporting periods must be explicitly defined.

---

# 36. VAT Period

VAT periods must align with the applicable registration and reporting requirements.

---

# 37. Tax Period Status

Possible states include:

```text
Open

Under Review

Prepared

Approved

Submitted

Closed

Corrected
```

---

# 38. Tax Period Close

Tax periods should be closed only after required reconciliation and review.

---

# 39. Tax Period Reopening

Reopening a closed tax period requires controlled authority.

---

# 40. VAT Output Tax

Output VAT represents VAT charged on taxable sales or supplies.

---

# 41. VAT Input Tax

Input VAT represents VAT incurred on eligible purchases or expenses.

---

# 42. Recoverable VAT

Recoverable VAT must follow applicable legal and organizational rules.

---

# 43. Non-Recoverable VAT

Non-recoverable VAT must be treated according to approved accounting policy.

---

# 44. VAT Exemption

VAT-exempt transactions must use an approved exemption classification.

---

# 45. Zero-Rated Transaction

Zero-rated transactions must remain distinguishable from exempt transactions.

---

# 46. Outside-Scope Transaction

Outside-scope transactions must remain distinguishable from zero-rated and exempt transactions.

---

# 47. Reverse Charge

Reverse-charge transactions must be separately identifiable where applicable.

---

# 48. Reverse-Charge Evidence

Required evidence must be retained.

---

# 49. VAT Evidence

VAT evidence may include:

```text
Tax Invoice

Credit Note

Debit Note

Receipt

Import Document

Export Evidence

Customer / Supplier Tax Identifier
```

where applicable.

---

# 50. Tax Invoice

Tax invoices must contain required fiscal information according to applicable rules.

---

# 51. Invoice Compliance

Invoices should be validated for required tax information before final processing where appropriate.

---

# 52. Credit Note

Credit notes must reference the original transaction where required.

---

# 53. Debit Note

Debit notes must be linked to the underlying transaction where required.

---

# 54. Tax Adjustment

Tax adjustments must be authorized and traceable.

---

# 55. Corrective Return

A corrective tax return may be required when a submitted return contains a material error.

---

# 56. Corrective Return Authority

Corrective filings require defined approval authority.

---

# 57. VAT Reconciliation

VAT balances must reconcile between transaction-level records, Accounting Core and the relevant VAT reporting model.

---

# 58. Tax Reconciliation

Tax balances must reconcile to the authoritative accounting data.

---

# 59. Reconciliation Frequency

Tax reconciliation should occur before each required tax filing and according to internal control requirements.

---

# 60. Reconciliation Exception

Differences must be investigated and documented.

---

# 61. Tax Return Preparation

Tax returns should be generated from controlled, reconciled tax data.

---

# 62. VAT Return Preparation

VAT returns must identify:

```text
Reporting Period

Taxable Sales

Output VAT

Taxable Purchases

Input VAT

Adjustments

Net VAT
```

where applicable.

---

# 63. Return Review

Tax returns require review before submission.

---

# 64. Return Approval

Formal tax filings require defined approval authority.

---

# 65. Regulatory Submission

Regulatory submissions must use authorized submission channels.

---

# 66. Submission Status

Possible states:

```text
Draft

Prepared

Reviewed

Approved

Submitted

Accepted

Rejected

Corrected
```

---

# 67. Submission Evidence

Submission evidence should include:

```text
Return

Submission Date

Submitter

Reference

Status

Response
```

where available.

---

# 68. Filing Deadline

Each regulatory filing must have a known deadline.

---

# 69. Deadline Monitoring

Upcoming filing deadlines should be monitored.

---

# 70. Filing Extension

An extension may be recorded where legally available and approved.

---

# 71. Extension Evidence

Extension evidence must be retained.

---

# 72. Payment Deadline

Tax liabilities must be scheduled for payment according to applicable deadlines.

---

# 73. Tax Liability

Tax liabilities should be visible in financial reporting.

---

# 74. VAT Liability

VAT payable should reconcile to Accounting Core.

---

# 75. Tax Payment

Tax payments must follow approved payment authority.

---

# 76. Tax Refund

Tax refunds must be reconciled to the underlying tax position.

---

# 77. Refund Tracking

Expected tax refunds should be monitored until receipt or resolution.

---

# 78. Tax Adjustment Approval

Material tax adjustments require approval.

---

# 79. Supplier Tax Information

Supplier records may include:

```text
Tax Identifier

VAT Number

Tax Residence

Tax Classification
```

where applicable.

---

# 80. Customer Tax Information

Customer records may include relevant tax identifiers and classifications.

---

# 81. Member Tax Information

Member tax information must be collected only where required and must be protected.

---

# 82. Tax Data Minimization

Tax identifiers and related personal information must be limited to legitimate requirements.

---

# 83. Cross-Border Transaction

Cross-border transactions must be separately identifiable where tax treatment differs.

---

# 84. EU Transaction

EU transactions may require specific VAT classification and reporting.

---

# 85. International Transaction

Non-EU international transactions may require separate tax treatment.

---

# 86. Import VAT

Import VAT must be supported by appropriate import evidence.

---

# 87. Export Treatment

Export transactions must retain evidence supporting the applicable treatment.

---

# 88. Cross-Border Evidence

Cross-border tax evidence must be retained according to applicable requirements.

---

# 89. Withholding Tax

Where applicable, withholding tax must be separately identified and controlled.

---

# 90. Withholding Tax Boundary

Withholding tax functionality must be enabled only where required by applicable rules.

---

# 91. Payroll Tax Boundary

Payroll taxes belong to the applicable payroll / employment tax process and must integrate with Accounting Core where relevant.

---

# 92. Tax-Exempt Organization

An organization may have special tax treatment that must be documented and governed.

---

# 93. Non-Profit Tax Considerations

Non-profit or charitable status does not automatically imply that every transaction is tax-exempt.

---

# 94. Activity-Based Tax Treatment

Tax treatment may depend on the nature of the activity rather than the organization's general status.

---

# 95. Membership Fees

Membership fees must be assigned the approved tax treatment applicable to the specific membership activity.

---

# 96. Donation

Donations must be distinguished from taxable sales or consideration where required.

---

# 97. Grant

Grants must be classified according to their legal and fiscal nature.

---

# 98. Sponsorship

Sponsorship revenue may require different treatment from donations or grants depending on the underlying obligations.

---

# 99. Event Revenue

Event revenue must be classified according to the nature of the event and applicable tax rules.

---

# 100. Sale of Goods

Sales of goods require the appropriate tax classification.

---

# 101. Services

Services require the appropriate tax classification and place-of-supply treatment where relevant.

---

# 102. Asset Disposal Tax

Disposal of assets may create tax or VAT consequences that must be separately evaluated.

---

# 103. Procurement Tax Treatment

Procurement transactions must preserve the applicable supplier tax treatment.

---

# 104. Expense Tax Treatment

Expense transactions must identify recoverable and non-recoverable tax where required.

---

# 105. Fixed Asset VAT

VAT on fixed-asset acquisitions must follow applicable recovery rules.

---

# 106. Inventory VAT

VAT on inventory purchases must follow applicable treatment.

---

# 107. Tax Master Data

Tax master data should include:

```text
Tax Codes

Rates

Categories

Jurisdictions

Exemptions

Effective Dates
```

---

# 108. Tax Configuration Ownership

Tax configuration requires a defined owner.

---

# 109. Tax Configuration Change

Changes to tax configuration must be controlled.

---

# 110. Tax Change Approval

Material tax-rule or tax-code changes require approval.

---

# 111. Tax Change Effective Date

Changes must specify when the new treatment becomes effective.

---

# 112. Tax Change Testing

Tax configuration changes must be tested before production use where practical.

---

# 113. Tax Change Audit

Tax configuration changes must be auditable.

---

# 114. Tax Override

Manual tax overrides must be restricted and auditable.

---

# 115. Tax Override Reason

An override should record the reason.

---

# 116. Tax Override Approval

Material overrides may require approval.

---

# 117. Tax Exception

Tax exceptions may include:

```text
Missing Tax Code

Invalid Rate

Unexpected Tax Treatment

Missing Evidence

Reconciliation Difference

Late Filing Risk
```

---

# 118. Tax Exception Owner

Material tax exceptions must have an owner.

---

# 119. Tax Compliance Monitoring

Compliance monitoring may include:

```text
Upcoming Filings

Open Reconciliations

Tax Exceptions

Rate Changes

Missing Evidence

Unusual Tax Results
```

---

# 120. Tax Risk

Tax risk may arise from:

```text
Incorrect Classification

Incorrect Rate

Missing Evidence

Late Filing

Late Payment

Incorrect Recovery

Cross-Border Error

Unauthorized Override
```

---

# 121. Tax Risk Assessment

Material tax risks should be assessed and monitored.

---

# 122. Compliance Calendar

MFM may maintain a fiscal compliance calendar.

---

# 123. Compliance Calendar Content

A compliance item may contain:

```text
Authority

Requirement

Period

Due Date

Owner

Status

Evidence
```

---

# 124. Filing Responsibility

Every required filing must have an accountable owner.

---

# 125. Filing Backup

A backup responsible person may be designated where operationally necessary.

---

# 126. Filing Escalation

Approaching or missed deadlines must trigger escalation according to policy.

---

# 127. Missed Filing

A missed filing must be treated as a compliance incident.

---

# 128. Late Filing

Late filing evidence and corrective action must be retained.

---

# 129. Tax Audit

Tax authorities may request records, explanations or supporting evidence.

---

# 130. Tax Audit Request

Audit requests should be registered and assigned.

---

# 131. Tax Audit Evidence

Evidence provided to authorities must be traceable.

---

# 132. Tax Audit Response

Responses must follow approved governance.

---

# 133. Tax Audit Findings

Findings should be recorded and assigned for remediation.

---

# 134. Tax Dispute

Tax disputes require controlled legal or financial handling.

---

# 135. Tax Advice Boundary

Where tax interpretation is uncertain, qualified professional advice may be required.

---

# 136. Regulatory Financial Reporting

MFM may support reports required by regulators or authorities.

---

# 137. Regulatory Report Definition

A regulatory report must specify:

```text
Authority

Purpose

Period

Data Source

Calculation Rules

Submission Channel

Deadline
```

---

# 138. Regulatory Report Source

Regulatory financial reports must derive from controlled and reconciled data.

---

# 139. Regulatory Report Reconciliation

Reported values must reconcile to Accounting Core or approved source records.

---

# 140. Regulatory Report Certification

Material regulatory reports may require certification before submission.

---

# 141. Regulatory Report Version

Submitted reports must retain a version or immutable copy.

---

# 142. Regulatory Correction

Corrected regulatory reports must retain the relationship to the original submission.

---

# 143. Submission Archive

Submission records and responses must be archived according to retention requirements.

---

# 144. Tax Evidence Retention

Tax evidence must be retained according to applicable legal and records-management requirements.

---

# 145. Evidence Integrity

Retained tax evidence must be protected against unauthorized alteration.

---

# 146. Evidence Retrieval

Authorized users must be able to retrieve evidence for audit and compliance purposes.

---

# 147. Tax Data Security

Tax data must follow MFM security architecture.

---

# 148. Tax Privacy

Tax identifiers and personal tax information require appropriate privacy controls.

---

# 149. Tax Access

Access should follow role, organizational scope and legitimate business need.

---

# 150. Tax Export

Tax data exports must be controlled and auditable where required.

---

# 151. Tax Incident

Examples include:

```text
Incorrect Filing

Missed Deadline

Wrong Tax Rate

Unauthorized Override

Missing Evidence

Tax Data Exposure

Incorrect VAT Reconciliation
```

---

# 152. Incorrect Filing Incident

Assess the filing, determine materiality and initiate correction according to applicable rules.

---

# 153. Missed Deadline Incident

Escalate immediately and document corrective action.

---

# 154. Wrong Tax Rate Incident

Identify affected transactions and determine whether corrections are required.

---

# 155. Unauthorized Override Incident

Investigate the actor, rule, transactions and financial impact.

---

# 156. Missing Evidence Incident

Identify affected transactions and recover or reconstruct evidence where legally permissible.

---

# 157. Tax Data Exposure Incident

Contain access and follow MFM security and privacy incident procedures.

---

# 158. VAT Reconciliation Incident

Investigate differences between transaction tax data, Accounting Core and the reporting return.

---

# 159. Recovery

Tax configuration, tax-period status, filings and evidence must be recoverable.

---

# 160. Recovery Integrity

Recovery must not duplicate tax calculations, submissions or payment records.

---

# 161. Filing Recovery

Submitted returns must remain distinguishable from drafts after recovery.

---

# 162. Tax Configuration Recovery

Tax rates and rules must retain correct historical effective dates after recovery.

---

# 163. Migration

Migration must preserve:

```text
Tax Codes

Historical Rates

Tax Classifications

Tax Periods

VAT Returns

Tax Reconciliations

Submission References

Tax Evidence
```

where required.

---

# 164. Migration Historical Integrity

Historical transactions must retain their original tax treatment.

---

# 165. Migration Reconciliation

Migrated tax balances must reconcile to Accounting Core.

---

# 166. Tax Testing

Test:

```text
Tax Codes

Rates

Tax Calculation

Rounding

Exemptions

Zero Rating

Outside Scope

Reverse Charge
```

---

# 167. VAT Testing

Test:

```text
Input VAT

Output VAT

Recoverable VAT

Non-Recoverable VAT

VAT Reconciliation

VAT Return
```

---

# 168. Filing Testing

Test:

```text
Draft

Review

Approval

Submission

Response

Correction
```

---

# 169. Cross-Border Testing

Test applicable:

```text
EU Transactions

International Transactions

Imports

Exports

Reverse Charge
```

---

# 170. Tax Security Testing

Test:

```text
Tax Configuration Access

Tax Data Access

Override Access

Export

Submission Authority
```

---

# 171. Tax Definition of Ready

Tax capability is Ready when:

- Tax Jurisdictions Defined
- Tax Codes Defined
- Rates Defined
- Tax Treatment Defined
- Effective Dates Defined
- Accounting Integration Defined
- Filing Requirements Defined
- Ownership Defined

---

# 172. Tax Definition of Done

Tax capability is Done when:

- Tax Calculation Tested
- VAT Tested
- Reconciliation Verified
- Filing Tested
- Security Tested
- Audit Evidence Verified

---

# 173. VAT Definition of Ready

VAT capability is Ready when:

- Registration Status Defined
- VAT Codes Defined
- Rates Defined
- Exemptions Defined
- Reverse Charge Defined
- Reporting Period Defined
- Reconciliation Defined

---

# 174. VAT Definition of Done

VAT capability is Done when:

- Input VAT Tested
- Output VAT Tested
- Recovery Tested
- Reconciliation Tested
- Return Tested
- Correction Tested
- Audit Verified

---

# 175. Regulatory Reporting Definition of Ready

Regulatory reporting is Ready when:

- Authority Defined
- Report Definition Defined
- Source Data Defined
- Calculation Rules Defined
- Deadline Defined
- Approval Defined
- Submission Channel Defined

---

# 176. Regulatory Reporting Definition of Done

Regulatory reporting is Done when:

- Report Generated
- Reconciled
- Reviewed
- Approved
- Submitted
- Submission Evidence Stored
- Correction Path Tested

---

# 177. Final Fiscal Principle

> **MFM must classify, calculate, reconcile and report tax information using approved fiscal rules while preserving Accounting Core as the authoritative financial ledger.**

---

# 178. Final VAT Principle

> **VAT treatment must distinguish taxable, zero-rated, exempt, outside-scope and reverse-charge transactions and must retain the evidence necessary to support the applied treatment.**

---

# 179. Final Historical Tax Principle

> **Tax rates, tax codes and tax rules must be effective-dated so that historical transactions retain the treatment applicable at the time.**

---

# 180. Final Reconciliation Principle

> **Tax and VAT reports must reconcile to Accounting Core and material differences must remain visible as controlled exceptions.**

---

# 181. Final Filing Principle

> **Every required fiscal or regulatory filing must have an owner, deadline, approval path, submission evidence and correction process.**

---

# 182. Final Evidence Principle

> **Tax evidence must be complete, protected, retrievable and traceable to the underlying transaction and filing.**

---

# 183. Final Override Principle

> **Manual tax overrides must be exceptional, justified, authorized and fully auditable.**

---

# 184. Final Privacy Principle

> **Tax identifiers and personal tax information must be exposed only to authorized users with a legitimate business need.**

---

# 185. Final Governance Principle

> **Every fiscal process must have defined ownership, authoritative sources, approved tax rules, effective dates, reconciliation, evidence, security and compliance monitoring.**

---

# 186. Summary

MFM v1.2-1100 establishes the Tax, VAT, Fiscal Compliance and Regulatory Financial Reporting architecture implementation baseline.

It defines:

- Tax Architecture
- Fiscal Compliance
- Tax Registration
- Tax Identification
- Tax Jurisdiction
- Tax Residence
- VAT Registration
- VAT Status
- Tax Classification
- Tax Codes
- VAT Codes
- Tax Rates
- VAT Categories
- Tax Rule Versioning
- Historical Tax Integrity
- Tax Calculation
- Taxable Base
- Tax Rounding
- Tax Date
- Supply Date
- Invoice Date
- Payment Date
- Tax Point
- Fiscal Periods
- VAT Periods
- Tax Period Status
- Tax Period Close
- Output VAT
- Input VAT
- Recoverable VAT
- Non-Recoverable VAT
- VAT Exemptions
- Zero-Rated Transactions
- Outside-Scope Transactions
- Reverse Charge
- Tax and VAT Evidence
- Tax Invoices
- Credit Notes
- Debit Notes
- Tax Adjustments
- Corrective Returns
- VAT Reconciliation
- Tax Reconciliation
- Tax Return Preparation
- VAT Return Preparation
- Return Review and Approval
- Regulatory Submission
- Submission Status
- Filing Deadlines
- Filing Extensions
- Payment Deadlines
- Tax Liabilities
- VAT Liabilities
- Tax Payments
- Tax Refunds
- Supplier Tax Information
- Customer Tax Information
- Member Tax Information
- Cross-Border Transactions
- EU Transactions
- International Transactions
- Import VAT
- Export Treatment
- Withholding Tax Boundary
- Payroll Tax Boundary
- Tax-Exempt Organizations
- Non-Profit Tax Considerations
- Membership Fees
- Donations
- Grants
- Sponsorship
- Event Revenue
- Sales of Goods
- Services
- Asset Disposal Tax
- Procurement Tax Treatment
- Expense Tax Treatment
- Fixed Asset VAT
- Inventory VAT
- Tax Master Data
- Tax Configuration
- Tax Change Management
- Tax Overrides
- Tax Exceptions
- Tax Compliance Monitoring
- Compliance Calendar
- Filing Responsibility
- Filing Escalation
- Tax Audits
- Tax Audit Evidence
- Tax Disputes
- Regulatory Financial Reporting
- Regulatory Report Certification
- Submission Archives
- Tax Evidence Retention
- Tax Security
- Tax Privacy
- Tax Incidents
- Recovery
- Migration
- Tax / VAT / Filing / Cross-Border / Security Testing
- Definition of Ready / Done Gates

The central architectural rules remain:

> **MFM must classify, calculate, reconcile and report tax information using approved fiscal rules while preserving Accounting Core as the authoritative financial ledger.**

> **VAT treatment must distinguish taxable, zero-rated, exempt, outside-scope and reverse-charge transactions and must retain the evidence necessary to support the applied treatment.**

> **Tax rates, tax codes and tax rules must be effective-dated so that historical transactions retain the treatment applicable at the time.**

> **Tax and VAT reports must reconcile to Accounting Core and material differences must remain visible as controlled exceptions.**

> **Every required fiscal or regulatory filing must have an owner, deadline, approval path, submission evidence and correction process.**

---

# 187. MFM Tax & Fiscal Compliance Architecture Baseline

MFM v1.2-1100 establishes the controlled fiscal foundation for tax classification, VAT processing, tax reconciliation, regulatory reporting, filing management, fiscal evidence and compliance monitoring.

Future tax and fiscal work should reference this document together with:

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
- MFM v1.2-1060 – Financial Controls, Approval Limits, Delegation & Segregation of Duties Architecture Implementation
- MFM v1.2-1070 – Procurement, Purchasing, Supplier & Expense Management Architecture Implementation
- MFM v1.2-1080 – Asset Management, Fixed Assets, Inventory & Depreciation Architecture Implementation
- MFM v1.2-1090 – Cash Management, Bank Accounts, Treasury & Liquidity Management Architecture Implementation

---

# END OF DOCUMENT
