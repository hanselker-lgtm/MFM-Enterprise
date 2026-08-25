# MFM v1.2-Steady-State-13
## Enterprise Data Management, Data Governance, Data Quality, Master Data, Metadata, Records, Information Lifecycle & Analytics Operations

**Version:** 1.2  
**Document ID:** MFM-v1.2-Steady-State-13  
**Status:** Steady-State Data Management Baseline  
**Lifecycle:** Post-Implementation / Steady-State Operation  
**Document Type:** Enterprise Data Management / Data Governance / Data Quality / Metadata / Records / Analytics Operations Document  

---

# 1. Purpose

This document establishes the thirteenth document in the MFM v1.2 Steady-State series.

It follows MFM v1.2-Steady-State-12 – Enterprise Application, Platform, Infrastructure, Cloud, Network, Endpoint, Database & Technical Operations Management.

The purpose of this document is to establish the permanent enterprise data-management operating model for MFM, covering data governance, ownership, data quality, master data, metadata, information lifecycle, records, data architecture, data integration, reporting, analytics and data assurance.

The central objective is:

> **MFM data must remain accurate, trustworthy, governed, protected, traceable, accessible to authorized users and fit for its intended business purpose throughout its lifecycle.**

---

# 2. Scope

This document covers:

- Enterprise Data Management
- Data Governance
- Data Ownership
- Data Stewardship
- Data Architecture
- Data Domains
- Data Classification
- Data Quality
- Data Quality Rules
- Data Quality Monitoring
- Master Data
- Reference Data
- Metadata
- Business Glossary
- Technical Metadata
- Data Lineage
- Data Catalog
- Data Integration
- Data Exchange
- Data Lifecycle
- Records Management
- Information Retention
- Information Disposal
- Data Access
- Data Sharing
- Data Protection
- Data Privacy Integration
- Data Security Integration
- Reporting
- Business Intelligence
- Analytics
- Data Products
- Data Reconciliation
- Data Controls
- Data Assurance
- Data Issues
- Data Remediation
- Data Metrics
- Data Maturity
- Continual Data Improvement

---

# 3. Data Management Objective

The primary objective is:

> **Ensure that MFM data is governed as an enterprise asset and remains fit for business, operational, regulatory, analytical and decision-making purposes.**

---

# 4. Data Principles

Data Management should be:

```text
Business-Aligned
Owned
Governed
Accurate
Complete
Consistent
Timely
Traceable
Protected
Accessible
Lifecycle-Aware
Continuously Improved
```

---

# 5. Data Operating Model

The data lifecycle should integrate:

```text
Create
 ↓
Capture
 ↓
Validate
 ↓
Store
 ↓
Use
 ↓
Share
 ↓
Retain
 ↓
Archive
 ↓
Dispose
```

---

# 6. Data Governance

Data Governance establishes accountability and decision rights for enterprise data.

---

# 7. Data Governance Authority

The Data Governance Authority should coordinate:

```text
Policies
Standards
Ownership
Quality
Metadata
Architecture
Issues
Assurance
Improvement
```

---

# 8. Data Ownership

Material data domains should have accountable Data Owners.

---

# 9. Data Owner Responsibilities

Data Owners should be accountable for:

```text
Definition
Quality
Access
Classification
Retention
Risk
Compliance
Lifecycle
```

within delegated authority.

---

# 10. Data Steward

Data Stewards support operational governance of data within assigned domains.

---

# 11. Data Steward Responsibilities

Data Stewards may manage:

```text
Data Quality
Definitions
Metadata
Issues
Validation
Data Rules
User Support
```

---

# 12. Data Domains

MFM data should be organized into logical domains where appropriate.

Examples may include:

```text
Member
Customer
Supplier
Financial
Asset
Service
Project
Employee
Operational
Reference
```

according to the actual MFM information model.

---

# 13. Data Domain Ownership

Each material data domain should have:

```text
Owner
Steward
Definition
Scope
Criticality
Quality Requirements
```

---

# 14. Data Classification

Data should be classified according to:

```text
Sensitivity
Confidentiality
Integrity
Availability
Privacy
Business Criticality
```

requirements.

---

# 15. Data Criticality

Critical data should be identified based on impact to:

```text
Operations
Finance
Compliance
Security
Reporting
Decision Making
Service Delivery
```

---

# 16. Data Asset

A Data Asset represents a governed collection of data used for a defined business or technical purpose.

---

# 17. Data Inventory

The Data Inventory should identify material:

```text
Data Asset
Owner
Domain
System
Classification
Criticality
Lifecycle
```

---

# 18. Data Architecture

Data Architecture defines how data is structured, stored, integrated and used across MFM.

---

# 19. Data Architecture Principles

Data Architecture should promote:

```text
Consistency
Reuse
Traceability
Interoperability
Security
Scalability
Maintainability
```

---

# 20. Data Model

Material business data should have an appropriate logical representation.

---

# 21. Conceptual Data Model

The conceptual model should describe major business entities and relationships.

---

# 22. Logical Data Model

The logical model should define:

```text
Entities
Attributes
Relationships
Identifiers
Rules
```

where appropriate.

---

# 23. Physical Data Model

The physical model should describe implementation structures where required.

---

# 24. Data Relationship

Important relationships between data entities should be documented where necessary.

---

# 25. Master Data

Master Data represents core entities that are shared across processes and systems.

---

# 26. Master Data Candidates

Master data may include:

```text
Member
Customer
Supplier
Organization
Employee
Asset
Product
Service
```

where applicable.

---

# 27. Master Data Ownership

Each master-data domain should have an accountable owner.

---

# 28. Master Data Lifecycle

The baseline lifecycle is:

```text
Create
 ↓
Validate
 ↓
Approve
 ↓
Use
 ↓
Update
 ↓
Review
 ↓
Retire
```

---

# 29. Master Data Golden Record

Where appropriate, MFM should maintain an authoritative representation of important master-data entities.

---

# 30. Master Data Matching

Duplicate and conflicting master-data records should be identified and resolved.

---

# 31. Reference Data

Reference Data provides controlled values used consistently across systems and processes.

---

# 32. Reference Data Governance

Reference values should have:

```text
Owner
Definition
Allowed Values
Effective Date
Status
Review
```

where applicable.

---

# 33. Reference Data Change

Changes to critical reference data should be controlled and traceable.

---

# 34. Data Quality

Data Quality Management ensures that data remains fit for purpose.

---

# 35. Data Quality Dimensions

Data quality may be assessed through:

```text
Accuracy
Completeness
Consistency
Timeliness
Validity
Uniqueness
Integrity
```

as appropriate.

---

# 36. Data Quality Rule

A Data Quality Rule defines an expected condition for data.

---

# 37. Data Quality Rule Example

A rule may require:

```text
Mandatory Field Present
Valid Format
Valid Reference
Unique Identifier
Consistent Relationship
Current Value
```

where applicable.

---

# 38. Data Quality Threshold

Critical data should have defined acceptable quality thresholds.

---

# 39. Data Quality Monitoring

Quality should be monitored according to:

```text
Criticality
Risk
Usage
Regulatory Need
Business Importance
```

---

# 40. Data Quality Issue

A Data Quality Issue identifies a condition where data does not meet an approved quality requirement.

---

# 41. Data Quality Issue Lifecycle

```text
Detect
 ↓
Log
 ↓
Assess
 ↓
Assign
 ↓
Correct
 ↓
Validate
 ↓
Close
```

---

# 42. Data Quality Root Cause

Material data-quality issues should be investigated for underlying causes.

---

# 43. Data Quality Remediation

Remediation may address:

```text
Source
Process
Application
Integration
Rule
User Practice
Data Transformation
```

---

# 44. Data Validation

Critical data should be validated at appropriate points in its lifecycle.

---

# 45. Data Reconciliation

Important data should be reconciled where independent sources or processes require consistency.

---

# 46. Reconciliation Rule

A reconciliation should define:

```text
Source
Target
Expected Relationship
Frequency
Tolerance
Owner
Exception Handling
```

---

# 47. Reconciliation Exception

Exceptions should be:

```text
Recorded
Investigated
Resolved
Validated
```

where appropriate.

---

# 48. Metadata

Metadata provides context about data.

---

# 49. Business Metadata

Business metadata may include:

```text
Definition
Owner
Purpose
Business Rule
Classification
Criticality
```

---

# 50. Technical Metadata

Technical metadata may include:

```text
System
Table
Field
Type
Source
Transformation
Interface
```

---

# 51. Operational Metadata

Operational metadata may include:

```text
Refresh
Status
Load Time
Processing Result
Quality Status
Usage
```

---

# 52. Metadata Ownership

Material metadata should have accountable ownership.

---

# 53. Business Glossary

The Business Glossary should define important business terms consistently.

---

# 54. Glossary Term

A glossary term should identify:

```text
Term
Definition
Owner
Domain
Status
Related Terms
```

---

# 55. Definition Governance

Material business definitions should be approved by appropriate domain authority.

---

# 56. Data Catalog

A Data Catalog should provide discoverability of governed data assets where appropriate.

---

# 57. Data Catalog Content

May include:

```text
Data Asset
Definition
Owner
Source
Classification
Quality
Lineage
Access
```

---

# 58. Data Lineage

Data lineage describes how data moves and transforms from source to destination.

---

# 59. Lineage Scope

Critical lineage may cover:

```text
Source
Extraction
Transformation
Integration
Storage
Reporting
Analytics
```

---

# 60. Lineage Value

Lineage supports:

```text
Impact Analysis
Troubleshooting
Audit
Compliance
Data Quality
Reporting Trust
```

---

# 61. Data Integration

Data integration should provide controlled movement and transformation of information.

---

# 62. Data Interface

A data interface should define:

```text
Source
Target
Data
Format
Frequency
Owner
Security
Failure Handling
```

---

# 63. Data Exchange

Data exchanges should use approved mechanisms.

---

# 64. Data Transformation

Material transformations should be documented and traceable.

---

# 65. Data Mapping

Mappings should identify relationships between source and target fields where necessary.

---

# 66. Data Migration

Data migrations should be planned, tested, reconciled and validated.

---

# 67. Migration Readiness

Migration readiness should consider:

```text
Scope
Quality
Mapping
Security
Privacy
Validation
Rollback
```

---

# 68. Migration Validation

Migration validation should confirm:

```text
Completeness
Accuracy
Relationships
Totals
Critical Records
```

as appropriate.

---

# 69. Data Lifecycle Management

Data should be governed from creation to disposal.

---

# 70. Data Retention

Retention periods should reflect:

```text
Business Need
Legal
Regulatory
Contractual
Operational
Privacy
```

requirements.

---

# 71. Data Archiving

Archived data should remain:

```text
Protected
Retrievable
Traceable
Readable
```

for the required retention period.

---

# 72. Data Disposal

Data disposal should be authorized and performed securely.

---

# 73. Disposal Evidence

Material disposal should produce appropriate evidence.

---

# 74. Records Management

Records Management ensures that required evidence of business activity is retained and controlled.

---

# 75. Record

A record is information retained as evidence of an activity, decision, transaction or obligation.

---

# 76. Records Classification

Records should be classified according to applicable:

```text
Business
Legal
Regulatory
Privacy
Confidentiality
```

requirements.

---

# 77. Records Retention

Retention schedules should define:

```text
Record Type
Retention Period
Owner
Disposition
```

---

# 78. Legal Hold

Where applicable, disposal should be suspended when information is subject to legal or regulatory preservation requirements.

---

# 79. Information Access

Access to data should be governed by:

```text
Need
Role
Sensitivity
Purpose
Authority
```

---

# 80. Data Sharing

Data sharing should be:

```text
Authorized
Purpose-Limited
Secure
Traceable
Appropriate
```

---

# 81. Data Sharing Agreement

Material external sharing should be governed by appropriate agreements or documented authority.

---

# 82. Data Protection Integration

Data Management must integrate with Privacy and Data Protection requirements.

---

# 83. Personal Data

Personal data should be handled according to applicable privacy requirements.

---

# 84. Sensitive Data

Sensitive data should receive enhanced protection according to classification and risk.

---

# 85. Data Security Integration

Data Management must integrate with cybersecurity controls for:

```text
Access
Encryption
Monitoring
Backup
Recovery
Disposal
```

---

# 86. Data Access Review

Access to critical or sensitive data should be periodically reviewed.

---

# 87. Data Usage Monitoring

Where appropriate, material data usage should be monitored for abnormal or unauthorized activity.

---

# 88. Reporting

Reporting should use governed data sources where possible.

---

# 89. Management Reporting

Management reports should have:

```text
Owner
Definition
Source
Frequency
Validation
```

where appropriate.

---

# 90. Business Intelligence

Business Intelligence should transform governed data into useful management information.

---

# 91. BI Dataset

Material BI datasets should identify:

```text
Owner
Source
Refresh
Definitions
Quality
Users
```

---

# 92. Analytics

Analytics should use appropriate governed data and documented assumptions.

---

# 93. Analytical Model

Material analytical models should identify:

```text
Purpose
Data
Method
Owner
Version
Validation
```

---

# 94. Data Product

A Data Product is a governed data output designed for defined consumers and outcomes.

---

# 95. Data Product Ownership

Data Products should have accountable owners.

---

# 96. Data Product Lifecycle

```text
Identify Need
 ↓
Design
 ↓
Build
 ↓
Validate
 ↓
Publish
 ↓
Monitor
 ↓
Improve
 ↓
Retire
```

---

# 97. Reporting Definitions

Important metrics and measures should use consistent definitions.

---

# 98. Metric Governance

A material metric should have:

```text
Name
Definition
Owner
Formula
Source
Frequency
```

where appropriate.

---

# 99. Data Reuse

Existing governed data should be reused where appropriate rather than creating unnecessary duplicate sources.

---

# 100. Data Duplication

Material duplication should be identified and managed where it creates:

```text
Quality Risk
Cost
Confusion
Security Risk
Maintenance
```

---

# 101. Data Issue Management

Data issues should be managed through a controlled lifecycle.

---

# 102. Data Issue Classification

Issues may be classified as:

```text
Critical
High
Medium
Low
Observation
```

according to impact and governance requirements.

---

# 103. Data Issue Ownership

Material data issues should have accountable owners.

---

# 104. Data Issue Escalation

Issues should be escalated when they exceed defined:

```text
Risk
Quality
Compliance
Business Impact
```

thresholds.

---

# 105. Data Remediation

Remediation should address both:

```text
Immediate Correction
Root Cause
```

where appropriate.

---

# 106. Data Control Framework

Data controls should address:

```text
Quality
Access
Integrity
Retention
Lineage
Reconciliation
Change
```

---

# 107. Data Control Ownership

Material data controls should have accountable owners.

---

# 108. Data Control Testing

Controls should be tested according to:

```text
Risk
Criticality
Change
History
```

---

# 109. Data Control Evidence

Control execution should produce appropriate evidence.

---

# 110. Data Assurance

Data Assurance provides confidence that governed data remains fit for purpose.

---

# 111. Assurance Activities

May include:

```text
Quality Testing
Reconciliation
Metadata Review
Lineage Review
Access Review
Data Audit
Control Testing
```

---

# 112. Data Finding

A Data Finding identifies a material weakness in data governance, quality, protection, lifecycle or control.

---

# 113. Data Remediation Plan

A remediation plan should identify:

```text
Finding
Cause
Risk
Action
Owner
Due Date
Evidence
Validation
```

---

# 114. Data Exception

A data exception should identify:

```text
Requirement
Deviation
Reason
Risk
Compensating Measure
Owner
Approval
Expiry
```

---

# 115. Data Metrics

Metrics may include:

```text
Quality Score
Completeness
Accuracy
Duplicate Rate
Timeliness
Reconciliation Exceptions
Metadata Coverage
Lineage Coverage
Critical Data Issue Aging
```

---

# 116. Data Dashboard

May include:

```text
Data Quality
Critical Issues
Master Data
Metadata
Lineage
Access
Retention
Reporting
Analytics
```

---

# 117. Data Review Cadence

Data reviews should occur according to:

```text
Criticality
Risk
Usage
Regulatory Need
Change
```

---

# 118. Data Governance Review

A governance review may assess:

```text
Ownership
Quality
Issues
Definitions
Metadata
Access
Lifecycle
Assurance
```

---

# 119. Data Quality Review

Quality reviews should assess trends, exceptions and root causes.

---

# 120. Data Domain Review

Material domains should periodically review:

```text
Definitions
Ownership
Quality
Lifecycle
Risks
Issues
```

---

# 121. Data Maturity

Data Management maturity should be periodically assessed.

---

# 122. Maturity Dimensions

Assess:

```text
Governance
Ownership
Architecture
Quality
Master Data
Reference Data
Metadata
Lineage
Lifecycle
Records
Integration
Reporting
Analytics
Assurance
Improvement
```

---

# 123. Maturity Levels

A baseline model is:

```text
1 – Initial
2 – Repeatable
3 – Defined
4 – Managed
5 – Optimized
```

---

# 124. Data Governance Quality Gate

Data Governance passes when:

```text
Domain
 ↓
Owner
 ↓
Definition
 ↓
Rule
 ↓
Quality
 ↓
Issue Management
 ↓
Assurance
```

is controlled.

---

# 125. Data Quality Quality Gate

Data Quality passes when:

```text
Requirement
 ↓
Rule
 ↓
Measurement
 ↓
Issue
 ↓
Remediation
 ↓
Validation
```

is traceable.

---

# 126. Master Data Quality Gate

Master Data Management passes when:

```text
Entity
 ↓
Create
 ↓
Validate
 ↓
Approve
 ↓
Use
 ↓
Review
 ↓
Retire
```

is controlled.

---

# 127. Metadata Quality Gate

Metadata Management passes when:

```text
Asset
 ↓
Definition
 ↓
Owner
 ↓
Metadata
 ↓
Review
 ↓
Update
```

is traceable.

---

# 128. Lineage Quality Gate

Data Lineage passes when:

```text
Source
 ↓
Transformation
 ↓
Storage
 ↓
Report / Analytics
 ↓
Consumer
```

is traceable.

---

# 129. Records Quality Gate

Records Management passes when:

```text
Record
 ↓
Classify
 ↓
Retain
 ↓
Protect
 ↓
Retrieve
 ↓
Dispose
```

is controlled.

---

# 130. Data Lifecycle Quality Gate

Data Lifecycle Management passes when:

```text
Create
 ↓
Use
 ↓
Share
 ↓
Retain
 ↓
Archive
 ↓
Dispose
```

is governed.

---

# 131. Analytics Quality Gate

Analytics Management passes when:

```text
Purpose
 ↓
Data
 ↓
Method
 ↓
Validation
 ↓
Result
 ↓
Owner
```

is controlled.

---

# 132. Data Assurance Quality Gate

Data Assurance passes when:

```text
Requirement
 ↓
Control
 ↓
Test
 ↓
Evidence
 ↓
Finding
 ↓
Remediation
 ↓
Verification
```

is traceable.

---

# 133. Definition of Ready

A data-management work item is Ready when:

- The data domain, asset, quality issue, master-data entity, metadata item, lineage requirement, record, report, analytical product or lifecycle action is clearly identified.
- Ownership, criticality and business purpose are known.
- Quality, security, privacy, retention, acceptance and evidence requirements are defined.

---

# 134. Definition of Done

A data-management work item is Done when:

```text
Requirement Identified
        ↓
Owner Assigned
        ↓
Data Action Implemented
        ↓
Quality / Security / Privacy Validated
        ↓
Metadata / Lineage Updated Where Required
        ↓
Evidence Captured
        ↓
Issues / Exceptions Addressed
        ↓
Outcome Accepted
```

---

# 135. Final Data Principle

> **MFM data must be treated as an enterprise asset with accountable ownership and controlled lifecycle management.**

---

# 136. Final Quality Principle

> **Data used for material business, financial, operational, regulatory or analytical purposes must be fit for its intended purpose and supported by appropriate quality controls.**

---

# 137. Final Master Data Principle

> **Core business entities must have authoritative definitions, controlled creation, appropriate validation and managed lifecycle.**

---

# 138. Final Metadata Principle

> **Important data must remain understandable through accurate business, technical and operational metadata.**

---

# 139. Final Lineage Principle

> **Critical data used for decisions, reporting and compliance must be traceable from source through transformation to consumer where appropriate.**

---

# 140. Final Records Principle

> **Required records must remain protected, retrievable and retained for the appropriate period before controlled disposal.**

---

# 141. Final Access Principle

> **Data access must be authorized according to legitimate purpose, role, sensitivity and applicable security and privacy requirements.**

---

# 142. Final Analytics Principle

> **Analytics and reporting must use governed data, consistent definitions and documented methods so that results can be trusted and understood.**

---

# 143. Final Assurance Principle

> **Material data controls must be tested and supported by evidence demonstrating continuing effectiveness.**

---

# 144. Final Improvement Principle

> **Data quality issues, reporting discrepancies, audit findings and user feedback must continuously improve MFM data management.**

---

# 145. Final Integration Principle

> **Data Management must integrate with Cybersecurity, Privacy, Service Management, Technical Operations, Risk, Compliance, Financial Operations, Architecture, Supplier Management and Business Continuity.**

---

# 146. Final Steady-State Data Principle

> **MFM data must remain accurate, trustworthy, governed, protected, traceable, accessible to authorized users and fit for its intended business purpose throughout its lifecycle.**

---

# 147. Summary

MFM v1.2-Steady-State-13 establishes the permanent Enterprise Data Management baseline.

It defines:

- Enterprise Data Management / Data Governance
- Data Governance Authority
- Data Ownership / Data Stewardship
- Data Domains / Domain Ownership
- Data Classification / Criticality
- Data Inventory / Data Assets
- Data Architecture / Conceptual / Logical / Physical Data Models
- Master Data / Master Data Ownership / Lifecycle
- Golden Records / Matching
- Reference Data / Reference Data Governance
- Data Quality / Quality Dimensions / Rules / Thresholds / Monitoring
- Data Quality Issues / Root Cause / Remediation
- Data Validation / Reconciliation / Exceptions
- Business / Technical / Operational Metadata
- Business Glossary / Definition Governance
- Data Catalog
- Data Lineage
- Data Integration / Data Exchange / Transformation / Mapping
- Data Migration / Migration Readiness / Validation
- Data Lifecycle / Retention / Archiving / Disposal
- Records Management / Classification / Retention / Legal Hold
- Data Access / Data Sharing / Data Sharing Agreements
- Privacy / Data Protection Integration
- Data Security Integration
- Data Access Reviews / Data Usage Monitoring
- Reporting / Management Reporting / Business Intelligence
- BI Datasets / Analytics / Analytical Models
- Data Products / Data Product Lifecycle
- Metric Governance
- Data Reuse / Data Duplication
- Data Issue Management / Classification / Ownership / Escalation
- Data Control Framework / Ownership / Testing / Evidence
- Data Assurance / Findings / Remediation / Exceptions
- Data Metrics / Dashboards
- Data Review Cadence / Governance Reviews / Quality Reviews / Domain Reviews
- Data Maturity
- Data Governance / Quality / Master Data / Metadata / Lineage / Records / Lifecycle / Analytics / Assurance Quality Gates
- Definition of Ready
- Definition of Done

---

# 148. Next Document

The next document shall be:

**MFM v1.2-Steady-State-14 – Enterprise Privacy, Data Protection, Information Rights, Consent, Personal Data Governance & Privacy Operations**

It shall establish the permanent enterprise privacy and personal-data governance operating model supporting MFM.

---

# 149. Document Control

**Document:** MFM v1.2-Steady-State-13  
**Version:** 1.2  
**Status:** Steady-State Data Management Baseline  
**Previous Document:** MFM v1.2-Steady-State-12  
**Next Document:** MFM v1.2-Steady-State-14  
**Lifecycle:** Steady-State Operation  
**Primary Transition:** Enterprise Application / Platform / Infrastructure / Cloud / Network / Endpoint / Database / Technical Operations → Enterprise Data Management / Data Governance / Data Quality / Master Data / Metadata / Records / Information Lifecycle / Analytics  
**Data Governance Authority:** Enterprise Data Governance / Data Management  
**Data Ownership Authority:** Data Owners / Domain Owners  
**Data Stewardship Authority:** Data Stewards / Data Quality Management  
**Data Architecture Authority:** Enterprise Data Architecture  
**Data Quality Authority:** Data Quality Management  
**Master Data Authority:** Master Data Management  
**Metadata Authority:** Metadata / Data Catalog Governance  
**Records Authority:** Records Management / Information Lifecycle Management  
**Analytics Authority:** Business Intelligence / Analytics / Data Products  
**Security Authority:** Cybersecurity / Information Security / Data Security  
**Privacy Authority:** Privacy / Information Rights / Data Protection  
**Service Authority:** Enterprise Service Management / ITSM  
**Technical Authority:** Enterprise Technical Operations / Application / Platform / Infrastructure / Database  
**Risk Authority:** Enterprise Risk Management  
**Compliance Authority:** Enterprise Compliance / Regulatory Obligations  
**Continuity Authority:** Business Continuity / Disaster Recovery / Operational Resilience  
**Architecture Authority:** Enterprise Architecture / Data Architecture / Solution Architecture  
**Supplier Authority:** Vendor / Supplier / Contract Governance  
**Financial Authority:** Financial Operations / Financial Data Governance  
**Assurance Authority:** Enterprise Assurance / Data Assurance / Audit  
**Improvement Authority:** Data Continual Improvement / Data Quality Improvement  
**Principle:** MFM data must remain accurate, trustworthy, governed, protected, traceable, accessible to authorized users and fit for its intended business purpose throughout its lifecycle.
