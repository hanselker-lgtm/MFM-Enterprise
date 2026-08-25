# MFM v1.2-1080 – Asset Management, Fixed Assets, Inventory & Depreciation Architecture Implementation

Version: 1.2

Document ID: MFM-v1.2-1080

Status: Asset Management, Fixed Assets, Inventory & Depreciation Implementation Baseline

---

# 1. Purpose

This document defines the Asset Management, Fixed Assets, Inventory and Depreciation architecture implementation baseline for MaritimForeningsManager (MFM) v1.2.

It extends:

- MFM v1.2-1040 – Accounting Integration, Financial Posting & Reconciliation Architecture Implementation
- MFM v1.2-1050 – Financial Reporting, Budgeting, Forecasting & Management Accounting Architecture Implementation
- MFM v1.2-1060 – Financial Controls, Approval Limits, Delegation & Segregation of Duties Architecture Implementation
- MFM v1.2-1070 – Procurement, Purchasing, Supplier & Expense Management Architecture Implementation

The purpose is to establish a controlled lifecycle for organizational assets, fixed assets, inventory and related financial treatment.

The document establishes:

- Asset Management Architecture
- Asset Register
- Fixed Asset Register
- Asset Identification
- Asset Classification
- Asset Categories
- Asset Ownership
- Asset Custody
- Asset Location
- Asset Status
- Asset Lifecycle
- Asset Acquisition
- Capitalization
- Capitalization Thresholds
- Componentization
- Asset Cost
- Direct Acquisition Costs
- Installation Costs
- Initial Recognition
- Asset Transfers
- Asset Reassignment
- Asset Custody Changes
- Asset Location Changes
- Asset Maintenance References
- Asset Impairment
- Depreciation
- Depreciation Methods
- Useful Life
- Residual Value
- Depreciation Start Date
- Depreciation Period
- Depreciation Suspension
- Depreciation Adjustment
- Asset Revaluation Boundaries
- Asset Disposal
- Asset Sale
- Asset Retirement
- Asset Write-Off
- Asset Loss
- Asset Damage
- Asset Theft
- Inventory Management
- Stock Items
- Inventory Categories
- Stock Locations
- Stock Movements
- Stock Receipts
- Stock Issues
- Stock Adjustments
- Stock Counts
- Inventory Valuation
- Inventory Reconciliation
- Inventory Obsolescence
- Inventory Write-Down
- Consumables
- Spare Parts
- Equipment
- Tools
- Digital Assets
- Intangible Asset Boundaries
- Asset Documents
- Asset Evidence
- Asset Audit
- Physical Verification
- Asset Tagging
- Asset Security
- Custodian Responsibilities
- Asset Controls
- Asset Approval
- Disposal Approval
- Inventory Approval
- Financial Integration
- Accounting Core Integration
- Asset-to-Ledger Reconciliation
- Depreciation Posting
- Disposal Posting
- Inventory Posting
- Reporting
- Asset Register Reporting
- Depreciation Reporting
- Inventory Reporting
- Asset Utilization
- Asset Exceptions
- Asset Incidents
- Recovery
- Migration
- Testing
- Definition of Ready / Done Gates

---

# 2. Asset Authority Principle

Asset management must maintain controlled operational asset records while Accounting Core remains authoritative for financial ledger state.

```text
Acquisition
    |
    v
Asset / Inventory Record
    |
    +---- Physical / Operational Lifecycle
    |
    +---- Financial Classification
    |
    v
Accounting Core
    |
    v
Financial Reporting
```

---

# 3. Accounting Authority

> **Accounting Core remains the authoritative source for financial ledger state.**

---

# 4. Asset Register

The asset register is the operational authoritative record for managed organizational assets.

---

# 5. Fixed Asset Register

The fixed asset register identifies assets that meet the organization's capitalization and fixed-asset criteria.

---

# 6. Asset Identifier

Every managed asset should have a unique asset identifier.

---

# 7. Asset Tag

Physical assets may receive a physical asset tag.

---

# 8. Asset Tag Uniqueness

Asset tags must not be reused while historical traceability depends on them.

---

# 9. Asset Category

Assets may be classified into categories such as:

```text
Buildings

Vessels

Vehicles

Machinery

Equipment

Tools

IT Equipment

Furniture

Navigation Equipment

Workshop Equipment

Other Approved Asset
```

---

# 10. Asset Classification

Classification must support operational and financial reporting.

---

# 11. Asset Description

The asset record should contain a clear description sufficient for identification.

---

# 12. Asset Serial Number

Where available, manufacturer serial numbers should be retained.

---

# 13. Manufacturer

Manufacturer information may be recorded where relevant.

---

# 14. Model

Model information may be recorded where relevant.

---

# 15. Acquisition Date

The acquisition date must be recorded where known.

---

# 16. In-Service Date

The date an asset becomes available for intended use must be distinguished from acquisition date where relevant.

---

# 17. Asset Owner

An accountable organizational owner must be identified.

---

# 18. Asset Custodian

A custodian may be responsible for day-to-day physical control of an asset.

---

# 19. Custodian vs Owner

Custody does not necessarily imply financial ownership.

---

# 20. Asset Location

The operational location of an asset should be recorded.

---

# 21. Location History

Material asset location changes should be traceable.

---

# 22. Asset Status

Possible asset states include:

```text
Planned

Ordered

Received

In Service

Under Maintenance

Temporarily Unavailable

Transferred

Disposed

Retired

Lost

Stolen
```

---

# 23. Asset Lifecycle

The asset lifecycle may follow:

```text
Need

↓

Procurement

↓

Receipt

↓

Recognition

↓

In Service

↓

Maintenance / Transfer

↓

Review

↓

Disposal / Retirement
```

---

# 24. Asset Acquisition

Asset acquisition may originate from:

```text
Purchase

Donation

Grant

Transfer

Construction

Internal Development
```

where applicable.

---

# 25. Acquisition Source

The acquisition source must be recorded.

---

# 26. Purchase Reference

Purchased assets should reference the relevant procurement transaction.

---

# 27. Supplier Reference

Where applicable, the asset should reference the supplier.

---

# 28. Invoice Reference

Capitalized assets should retain the relevant supplier invoice or accounting reference.

---

# 29. Acquisition Cost

Acquisition cost must follow applicable accounting policy.

---

# 30. Direct Acquisition Costs

Direct costs required to acquire and prepare an asset for intended use may be included where accounting policy permits.

---

# 31. Installation Costs

Installation costs may form part of asset cost where applicable.

---

# 32. Testing / Commissioning Costs

Testing and commissioning costs may be capitalized where permitted by accounting policy.

---

# 33. Non-Capitalizable Costs

Costs that do not meet capitalization criteria must remain expenses where required.

---

# 34. Capitalization Threshold

The organization may define a capitalization threshold.

---

# 35. Threshold Governance

Capitalization thresholds must be controlled and effective-dated.

---

# 36. Threshold Application

Thresholds must not be manipulated through artificial splitting of asset components or invoices.

---

# 37. Componentization

Material assets may be divided into significant components where different useful lives or accounting treatment apply.

---

# 38. Component Identifier

Each component should be traceable to the parent asset.

---

# 39. Component Lifecycle

Components may have separate:

```text
Useful Life

Depreciation

Replacement

Disposal
```

where required.

---

# 40. Asset Bundle

Several items may be treated as one asset where accounting policy permits.

---

# 41. Bundle Traceability

Bundled assets must remain physically and financially traceable.

---

# 42. Donated Asset

Donated assets require controlled valuation and recognition according to accounting policy.

---

# 43. Grant-Funded Asset

Grant-funded assets must retain funding-source information where required.

---

# 44. Restricted Funding

Assets acquired using restricted funding must comply with applicable restrictions.

---

# 45. Asset Funding Source

The asset record may identify:

```text
Unrestricted Funds

Grant

Donation

Sponsor

Project

Other Restricted Source
```

---

# 46. Asset Approval

Capital acquisitions must follow MFM v1.2-1060 approval rules.

---

# 47. Capital Commitment

Approved capital purchases may create commitments before recognition.

---

# 48. Asset Receipt

Physical receipt should be confirmed before the asset is placed into operational service.

---

# 49. Asset Acceptance

An authorized person may confirm that an acquired asset meets required specifications.

---

# 50. Asset Commissioning

Commissioning establishes that the asset is ready for intended use.

---

# 51. In-Service Recognition

The accounting recognition point must follow Accounting Core policy.

---

# 52. Depreciation

Depreciation allocates the depreciable amount over the asset's useful life according to accounting policy.

---

# 53. Depreciable Amount

Depreciable amount may be:

```text
Cost - Residual Value
```

subject to applicable accounting policy.

---

# 54. Useful Life

Useful life must be defined or estimated according to accounting policy.

---

# 55. Useful Life Governance

Useful-life rules should be controlled and documented.

---

# 56. Depreciation Method

Supported methods may include:

```text
Straight-Line

Declining Balance

Units of Production
```

where applicable.

---

# 57. Method Authority

Depreciation method selection must follow Accounting Core policy.

---

# 58. Depreciation Start

Depreciation begins according to the approved recognition and in-service rules.

---

# 59. Depreciation Frequency

Depreciation may be calculated monthly or according to the accounting calendar.

---

# 60. Depreciation Period

The depreciation period must be traceable to the asset's useful life.

---

# 61. Residual Value

Residual value must be defined where applicable.

---

# 62. Depreciation Adjustment

Changes to useful life, residual value or method must be controlled.

---

# 63. Depreciation Recalculation

A material change may require recalculation according to accounting policy.

---

# 64. Depreciation Suspension

Suspension of depreciation may only occur where accounting policy permits it.

---

# 65. Depreciation Posting

Depreciation postings must be generated or approved through Accounting Core.

---

# 66. Depreciation Traceability

Each depreciation result must be traceable to the relevant asset and accounting period.

---

# 67. Accumulated Depreciation

Accumulated depreciation must be maintained through the authoritative accounting model.

---

# 68. Net Book Value

Net book value is derived from cost, accumulated depreciation and applicable adjustments.

---

# 69. Net Book Value Authority

Authoritative net book value must come from Accounting Core or an approved reconciled asset-accounting model.

---

# 70. Impairment

Assets may require impairment assessment when indicators exist.

---

# 71. Impairment Indicator

Indicators may include:

```text
Damage

Obsolescence

Loss of Function

Reduced Use

Market Decline

Other Material Indicator
```

---

# 72. Impairment Assessment

Impairment assessments must follow accounting policy.

---

# 73. Impairment Approval

Material impairment decisions may require financial approval.

---

# 74. Impairment Posting

Impairment effects must be posted through Accounting Core.

---

# 75. Revaluation

Asset revaluation is permitted only where explicitly supported by the applicable accounting framework and organizational policy.

---

# 76. Revaluation Authority

MFM must not independently create authoritative revaluation accounting.

---

# 77. Asset Transfer

Assets may be transferred between:

```text
Locations

Departments

Projects

Custodians

Organizational Units
```

---

# 78. Transfer Approval

Material transfers may require approval.

---

# 79. Transfer Date

The effective transfer date must be recorded.

---

# 80. Transfer History

Asset transfer history must remain reconstructable.

---

# 81. Custody Change

Changes in custodian must be recorded.

---

# 82. Custody Acknowledgement

The receiving custodian may be required to acknowledge custody.

---

# 83. Asset Location Change

Physical location changes should be recorded promptly.

---

# 84. Maintenance Reference

Maintenance records may reference the asset identifier.

---

# 85. Maintenance vs Asset Accounting

Maintenance activity does not automatically change asset accounting treatment.

---

# 86. Capital Improvement

Material improvements may require separate capitalization assessment.

---

# 87. Improvement Link

Capital improvements should reference the parent asset.

---

# 88. Replacement Component

A replacement component may require derecognition of an old component and recognition of a new component according to accounting policy.

---

# 89. Asset Disposal

Disposal ends the organization's controlled asset lifecycle.

---

# 90. Disposal Types

Possible disposal outcomes include:

```text
Sale

Donation

Scrapping

Recycling

Transfer

Retirement

Loss
```

---

# 91. Disposal Approval

Disposal must follow approved authority.

---

# 92. Disposal Evidence

Disposal should retain:

```text
Reason

Date

Approver

Method

Recipient / Buyer

Value
```

where applicable.

---

# 93. Asset Sale

Asset sales must be processed through controlled financial and accounting procedures.

---

# 94. Disposal Proceeds

Sale proceeds must reconcile to Accounting Core.

---

# 95. Gain / Loss on Disposal

Any accounting gain or loss must be determined through the authoritative accounting process.

---

# 96. Asset Retirement

Retired assets must be removed from active operational inventory while preserving historical records.

---

# 97. Asset Write-Off

Write-offs require controlled approval.

---

# 98. Asset Loss

Lost assets must be recorded as incidents and assessed for accounting impact.

---

# 99. Asset Theft

Theft must trigger security, incident and financial processes as appropriate.

---

# 100. Asset Damage

Material damage must be documented and assessed.

---

# 101. Physical Verification

Assets should be physically verified according to risk and policy.

---

# 102. Verification Frequency

Verification may be:

```text
Annual

Periodic

Risk-Based

Event-Driven
```

---

# 103. Verification Evidence

Verification should record:

```text
Asset

Location

Condition

Custodian

Verification Date

Result
```

---

# 104. Missing Asset

A missing asset creates an exception requiring investigation.

---

# 105. Asset Count

Physical asset counts should reconcile operational records with actual assets.

---

# 106. Asset Condition

Condition may be classified as:

```text
New

Good

Fair

Poor

Unserviceable
```

---

# 107. Asset Utilization

Management may track utilization where useful.

---

# 108. Underutilized Asset

Underutilized assets may be reviewed for reassignment, disposal or other action.

---

# 109. Inventory

Inventory represents controlled stock held for operational use, resale or other approved purposes.

---

# 110. Inventory Item

Each controlled stock item should have a unique item definition.

---

# 111. Stock Keeping Unit

Where appropriate, an inventory item may have a SKU or internal stock code.

---

# 112. Inventory Category

Categories may include:

```text
Consumables

Spare Parts

Materials

Merchandise

Supplies

Other Stock
```

---

# 113. Stock Location

Inventory may be held in one or more stock locations.

---

# 114. Stock Quantity

Quantity must be maintained using controlled stock movements.

---

# 115. Stock Movement

Stock movements may include:

```text
Receipt

Issue

Transfer

Adjustment

Return

Disposal
```

---

# 116. Stock Receipt

Receipt increases recorded stock quantity.

---

# 117. Stock Issue

Issue reduces recorded stock quantity.

---

# 118. Stock Transfer

Transfers move stock between controlled locations.

---

# 119. Stock Return

Returns restore stock according to defined rules.

---

# 120. Stock Adjustment

Adjustments require reason and authorization.

---

# 121. Inventory Count

Physical counts compare recorded and actual stock.

---

# 122. Inventory Count Frequency

Counts may be:

```text
Annual

Periodic

Cycle Count

Risk-Based
```

---

# 123. Count Variance

Differences between physical and recorded quantities must be investigated.

---

# 124. Inventory Valuation

Inventory valuation must follow approved accounting policy.

---

# 125. Valuation Method

Methods may include:

```text
FIFO

Weighted Average

Specific Identification
```

where applicable.

---

# 126. Valuation Authority

Authoritative inventory valuation belongs to Accounting Core or the approved accounting model.

---

# 127. Inventory Write-Down

Obsolete, damaged or unsellable inventory may require write-down.

---

# 128. Obsolescence

Inventory obsolescence should be monitored.

---

# 129. Slow-Moving Inventory

Slow-moving inventory may be reported for management review.

---

# 130. Inventory Disposal

Disposed inventory must be removed from operational stock and treated financially according to policy.

---

# 131. Consumables

Consumables may be expensed when used or treated according to accounting policy.

---

# 132. Spare Parts

Spare parts may be inventory or capitalized components depending on their nature and accounting treatment.

---

# 133. Tools

Tools may be treated as inventory or fixed assets according to policy and capitalization criteria.

---

# 134. Equipment

Equipment classification must follow asset and capitalization rules.

---

# 135. Digital Assets

Digital assets may include:

```text
Software Licenses

Digital Equipment

Other Controlled Digital Resources
```

---

# 136. Intangible Asset Boundary

Intangible asset recognition must follow applicable accounting policy.

---

# 137. Software Costs

Software-related costs must be classified according to the applicable accounting treatment.

---

# 138. Asset Documents

Asset records may reference:

```text
Invoices

Warranties

Manuals

Certificates

Inspection Records

Photos

Disposal Documents
```

---

# 139. Asset Evidence

Evidence must be retained according to records-management requirements.

---

# 140. Warranty

Warranty information may include:

```text
Start Date

End Date

Provider

Coverage
```

---

# 141. Inspection

Assets subject to inspection should reference inspection records.

---

# 142. Certification

Where an asset requires certification, certificate validity should be monitored.

---

# 143. Expired Certification

Expired certification should trigger an appropriate operational alert.

---

# 144. Asset Security

Assets must be protected against unauthorized removal, misuse or loss.

---

# 145. High-Value Asset

High-value assets may require enhanced custody and monitoring.

---

# 146. Portable Asset

Portable assets may require additional tracking.

---

# 147. Asset Loan

Asset loans to members, volunteers, employees or third parties must be documented.

---

# 148. Loan Record

A loan may include:

```text
Asset

Borrower

Start Date

Expected Return

Actual Return

Condition
```

---

# 149. Loan Approval

Asset loans may require approval according to policy.

---

# 150. Overdue Asset Loan

Overdue loans should generate an exception or reminder.

---

# 151. Asset Incident

Examples include:

```text
Missing

Stolen

Damaged

Mislocated

Unauthorized Transfer
```

---

# 152. Incident Investigation

Material asset incidents must be investigated.

---

# 153. Financial Impact

Incidents must be assessed for potential financial impact.

---

# 154. Accounting Integration

Asset financial events must integrate with Accounting Core.

---

# 155. Acquisition Posting

Capitalized acquisition transactions must reconcile to Accounting Core.

---

# 156. Depreciation Posting

Depreciation must reconcile to accounting journal entries.

---

# 157. Impairment Posting

Impairment must reconcile to Accounting Core.

---

# 158. Disposal Posting

Disposals must reconcile to accounting entries and proceeds.

---

# 159. Inventory Posting

Inventory movements affecting accounting must reconcile to Accounting Core.

---

# 160. Inventory Adjustment Posting

Material stock adjustments with financial effect must be posted through the authoritative accounting process.

---

# 161. Asset-to-Ledger Reconciliation

The asset register should reconcile to the fixed-asset balances in Accounting Core.

---

# 162. Reconciliation Frequency

Asset-to-ledger reconciliation should occur according to financial close and risk requirements.

---

# 163. Reconciliation Exception

Differences must be investigated and resolved through controlled processes.

---

# 164. Control Totals

Reconciliation may use:

```text
Asset Count

Gross Cost

Accumulated Depreciation

Net Book Value

Additions

Disposals
```

---

# 165. Inventory Reconciliation

Inventory records should reconcile to accounting inventory balances where applicable.

---

# 166. Inventory Control Totals

Control totals may include:

```text
Quantity

Value

Receipts

Issues

Adjustments
```

---

# 167. Financial Reporting

Asset reporting may include:

```text
Gross Cost

Accumulated Depreciation

Net Book Value

Additions

Disposals

Impairments
```

---

# 168. Depreciation Reporting

Reports may include:

```text
Current Period

Year-to-Date

Accumulated

Forecast
```

---

# 169. Inventory Reporting

Reports may include:

```text
On Hand

Value

Slow Moving

Obsolete

Variance
```

---

# 170. Asset Register Reporting

Reports may include:

```text
Asset ID

Category

Location

Custodian

Status

Cost

Net Book Value
```

---

# 171. Asset Utilization Reporting

Management may analyze utilization by asset category or project.

---

# 172. Capital Expenditure Reporting

Capital expenditure reports may show:

```text
Approved

Committed

Actual

Forecast

Remaining
```

---

# 173. Disposal Reporting

Disposal reports may include:

```text
Assets Disposed

Proceeds

Book Value

Gain / Loss
```

---

# 174. Asset Dashboard

A management dashboard may show:

```text
Asset Count

Asset Value

Depreciation

Upcoming Reviews

Missing Assets

Inventory Exceptions
```

---

# 175. Data Freshness

Asset and inventory dashboards should show data freshness where relevant.

---

# 176. Asset Security and Privacy

Asset records may contain information about custodians, locations and organizational activities.

---

# 177. Access Control

Asset information must follow MFM v1.2-1000 authorization rules.

---

# 178. Location Sensitivity

Sensitive asset locations should be restricted where necessary.

---

# 179. Export Security

Asset exports must be authorized and protected.

---

# 180. Audit Trail

Material asset changes must be auditable.

---

# 181. Audit Events

Audit events may include:

```text
Created

Classified

Capitalized

Transferred

Reassigned

Adjusted

Impaired

Disposed

Written Off
```

---

# 182. Inventory Audit

Inventory adjustments and count results must be auditable.

---

# 183. Disposal Audit

Disposals must retain evidence of authorization and execution.

---

# 184. Control Review

Asset and inventory controls should be reviewed periodically.

---

# 185. Asset Incident Escalation

Material asset incidents should be escalated according to risk.

---

# 186. Fraud Monitoring

Monitoring may identify:

```text
Repeated Inventory Adjustments

Missing Assets

Unauthorized Transfers

Unusual Disposals

Duplicate Asset Records
```

---

# 187. Recovery

Asset and inventory records must be recoverable.

---

# 188. Recovery Integrity

Recovery must not duplicate asset creation, inventory movements or financial postings.

---

# 189. Migration

Migration must preserve:

```text
Asset IDs

Historical Cost

Accumulated Depreciation

Useful Life

Acquisition Date

Disposal History

Inventory History
```

where required.

---

# 190. Migration Reconciliation

Migrated asset and inventory balances must reconcile to Accounting Core.

---

# 191. Migration Validation

Validate:

```text
Asset Count

Gross Cost

Accumulated Depreciation

Net Book Value

Inventory Quantity

Inventory Value
```

---

# 192. Asset Testing

Test:

```text
Create

Classify

Capitalize

Transfer

Depreciate

Impair

Dispose
```

---

# 193. Depreciation Testing

Test:

```text
Useful Life

Residual Value

Start Date

Method

Period

Adjustment
```

---

# 194. Inventory Testing

Test:

```text
Receipt

Issue

Transfer

Adjustment

Count

Variance
```

---

# 195. Reconciliation Testing

Test:

```text
Asset Register ↔ Accounting Core

Inventory ↔ Accounting Core

Depreciation ↔ Journal

Disposal ↔ Accounting
```

---

# 196. Security Testing

Test:

```text
Asset Access

Custodian Access

Location Access

Disposal Authorization

Export
```

---

# 197. Asset Definition of Ready

Asset management is Ready when:

- Asset Model Defined
- Classification Defined
- Ownership Defined
- Lifecycle Defined
- Capitalization Rules Defined
- Accounting Integration Defined
- Security Defined

---

# 198. Asset Definition of Done

Asset management is Done when:

- Acquisition Tested
- Capitalization Tested
- Transfer Tested
- Depreciation Tested
- Disposal Tested
- Reconciliation Verified
- Audit Verified

---

# 199. Inventory Definition of Ready

Inventory management is Ready when:

- Item Model Defined
- Locations Defined
- Movement Rules Defined
- Valuation Defined
- Count Rules Defined
- Accounting Integration Defined

---

# 200. Inventory Definition of Done

Inventory management is Done when:

- Receipt Tested
- Issue Tested
- Transfer Tested
- Adjustment Tested
- Count Tested
- Valuation Tested
- Reconciliation Verified
- Audit Verified

---

# 201. Final Asset Principle

> **Every controlled organizational asset must have a unique identity, accountable ownership or custody, defined lifecycle and sufficient evidence to support operational and financial traceability.**

---

# 202. Final Capitalization Principle

> **Capitalization must follow approved accounting criteria and must not be manipulated through artificial transaction splitting or classification.**

---

# 203. Final Depreciation Principle

> **Depreciation must follow the authoritative accounting policy for useful life, residual value, method and recognition timing.**

---

# 204. Final Disposal Principle

> **Asset disposal, retirement, loss and write-off must preserve historical asset records and reconcile all financial effects to Accounting Core.**

---

# 205. Final Inventory Principle

> **Inventory quantities and values must be supported by controlled stock movements, physical verification and reconciliation to the authoritative accounting model where financially relevant.**

---

# 206. Final Custody Principle

> **Operational custody and financial ownership are distinct responsibilities and must remain separately identifiable.**

---

# 207. Final Security Principle

> **High-value, portable or sensitive assets require controls proportional to their physical, operational and financial risk.**

---

# 208. Final Reconciliation Principle

> **The asset register and inventory records must be capable of reconciliation to authoritative financial balances and must expose differences as controlled exceptions.**

---

# 209. Final Governance Principle

> **Every asset and inventory process must have defined ownership, classification, approval, evidence, accounting treatment, security, reconciliation and lifecycle controls.**

---

# 210. Summary

MFM v1.2-1080 establishes the Asset Management, Fixed Assets, Inventory and Depreciation architecture implementation baseline.

It defines:

- Asset Register
- Fixed Asset Register
- Asset Identification
- Asset Tagging
- Asset Categories
- Asset Classification
- Asset Ownership
- Asset Custody
- Asset Location
- Asset Status
- Asset Lifecycle
- Acquisition
- Capitalization
- Capitalization Thresholds
- Componentization
- Asset Bundles
- Acquisition Costs
- Installation and Commissioning Costs
- Donated Assets
- Grant-Funded Assets
- Restricted Funding
- Asset Approval
- Asset Receipt
- Asset Acceptance
- Asset Commissioning
- In-Service Recognition
- Depreciation
- Useful Life
- Residual Value
- Depreciation Methods
- Depreciation Start
- Depreciation Period
- Depreciation Adjustments
- Impairment
- Revaluation Boundaries
- Asset Transfers
- Custody Changes
- Location Changes
- Maintenance References
- Capital Improvements
- Replacement Components
- Asset Disposal
- Asset Sales
- Asset Retirement
- Write-Offs
- Loss
- Theft
- Damage
- Physical Verification
- Asset Counts
- Asset Condition
- Asset Utilization
- Inventory Items
- Stock Keeping Units
- Inventory Categories
- Stock Locations
- Stock Movements
- Receipts
- Issues
- Transfers
- Returns
- Stock Adjustments
- Inventory Counts
- Inventory Valuation
- Inventory Write-Down
- Obsolescence
- Consumables
- Spare Parts
- Tools
- Equipment
- Digital Assets
- Intangible Asset Boundaries
- Asset Documents
- Warranty and Certification
- Asset Loans
- Asset Incidents
- Accounting Integration
- Acquisition Posting
- Depreciation Posting
- Impairment Posting
- Disposal Posting
- Inventory Posting
- Asset-to-Ledger Reconciliation
- Inventory Reconciliation
- Control Totals
- Asset Reporting
- Depreciation Reporting
- Inventory Reporting
- Capital Expenditure Reporting
- Disposal Reporting
- Asset Dashboards
- Asset Security
- Audit Trail
- Fraud Monitoring
- Recovery
- Migration
- Testing
- Definition of Ready / Done Gates

The central architectural rules remain:

> **Every controlled organizational asset must have a unique identity, accountable ownership or custody, defined lifecycle and sufficient evidence to support operational and financial traceability.**

> **Capitalization must follow approved accounting criteria and must not be manipulated through artificial transaction splitting or classification.**

> **Depreciation must follow the authoritative accounting policy for useful life, residual value, method and recognition timing.**

> **Asset disposal, retirement, loss and write-off must preserve historical asset records and reconcile all financial effects to Accounting Core.**

> **Inventory quantities and values must be supported by controlled stock movements, physical verification and reconciliation to the authoritative accounting model where financially relevant.**

> **Operational custody and financial ownership are distinct responsibilities and must remain separately identifiable.**

---

# 211. MFM Asset & Inventory Management Architecture Baseline

MFM v1.2-1080 establishes the controlled asset foundation for fixed assets, inventory, depreciation, custody, physical verification, disposal and financial reconciliation.

Future asset and inventory work should reference this document together with:

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

---

# END OF DOCUMENT
