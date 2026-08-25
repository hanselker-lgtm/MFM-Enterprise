# MFM v1.2-Steady-State-97
## Enterprise Data Architecture, Data Governance, Data Quality, Master Data, Metadata, Data Lifecycle & Data Assurance

**Version:** 1.2  
**Document ID:** MFM v1.2-Steady-State-97  
**Status:** Steady-State Enterprise Data Management Baseline  
**Lifecycle:** Post-Implementation / Steady-State Operation  
**Document Type:** Data Architecture / Data Governance / Data Quality / Master Data / Metadata / Data Lifecycle / Data Assurance Document  

---

# 1. Purpose

This document establishes the ninety-seventh document in the MFM v1.2 Steady-State series.

It follows MFM v1.2-Steady-State-96 – Enterprise Software Architecture, Application Architecture, API Governance, Integration Architecture & Application Lifecycle Assurance.

The purpose is to establish the permanent enterprise operating model for data architecture, data governance, data ownership, data stewardship, data domains, master data, reference data, metadata, data lineage, data quality, data classification, data lifecycle, data retention, data archival, data disposal, data integration, data standards, data controls, data exceptions, data remediation, data assurance, data metrics, dashboards, maturity and continual enterprise data management improvement.

The central objective is:

> **MFM must govern enterprise data as a strategic and controlled asset so that data remains accurate, complete, consistent, secure, traceable, available, appropriately retained and fit for business use.**

---

# 2. Scope

This document covers:

- Enterprise Data Architecture
- Data Governance
- Data Ownership
- Data Stewardship
- Data Domains
- Master Data
- Reference Data
- Metadata
- Data Lineage
- Data Quality
- Data Classification
- Data Lifecycle
- Data Retention
- Data Archival
- Data Disposal
- Data Integration
- Data Standards
- Data Controls
- Data Exceptions
- Data Remediation
- Data Assurance
- Data Metrics
- Data Dashboards
- Data Maturity
- Continual Enterprise Data Management Improvement

---

# 3. Data Governance Objective

The primary objective is:

> **Establish clear accountability, decision rights, standards and controls for enterprise data.**

# 4. Data Architecture Objective

The primary objective is:

> **Establish a coherent enterprise data architecture supporting business capabilities, applications, integrations, analytics, security and lifecycle requirements.**

# 5. Data Quality Objective

The primary objective is:

> **Ensure data is sufficiently accurate, complete, consistent, timely, valid, unique and fit for its intended purpose.**

# 6. Master Data Objective

The primary objective is:

> **Establish authoritative management of shared business entities and reduce duplication and inconsistency across systems.**

# 7. Metadata Objective

The primary objective is:

> **Provide sufficient information about data meaning, structure, ownership, lineage, classification and lifecycle to support reliable use and governance.**

# 8. Data Lifecycle Objective

The primary objective is:

> **Manage data from creation and acquisition through use, retention, archival and controlled disposal.**

# 9. Data Assurance Objective

The primary objective is:

> **Provide evidence that material data controls, quality requirements and governance obligations are operating effectively.**

# 10. Data Principles

Enterprise data should be:

```text
Accurate
Complete
Consistent
Timely
Valid
Unique where Required
Secure
Traceable
Available
Purpose-Fit
```

# 11. Data Governance Principles

Data governance should establish:

```text
Ownership
Stewardship
Standards
Decision Rights
Controls
Assurance
Improvement
```

# 12. Data Architecture Principles

Data architecture should promote:

```text
Common Meaning
Controlled Duplication
Interoperability
Traceability
Security
Scalability
Lifecycle Control
```

# 13. Data Lifecycle

The data lifecycle should integrate:

```text
Create / Acquire
 ↓
Classify
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

# 14. Data Governance Model

The governance model should define:

```text
Data Owner
Data Steward
Data Custodian
Data Consumer
Governance Authority
```

# 15. Data Owner

A data owner should be accountable for the business use, quality expectations, access requirements and lifecycle decisions for a defined data domain or dataset.

# 16. Data Steward

A data steward should support:

```text
Definitions
Quality
Standards
Issue Management
Metadata
Lineage
```

within the assigned domain.

# 17. Data Custodian

A data custodian should implement appropriate technical controls for storage, protection, access, backup and operational handling.

# 18. Data Consumer

Data consumers should use data according to:

```text
Purpose
Authorization
Classification
Usage Rules
```

# 19. Data Domains

Enterprise data should be organized into meaningful domains.

Examples may include:

```text
Customer
Supplier
Employee
Finance
Product
Asset
Service
Location
Reference
```

# 20. Domain Ownership

Each material data domain should have accountable ownership.

# 21. Data Domain Standards

Each domain should establish appropriate:

```text
Definitions
Ownership
Quality Rules
Classification
Lifecycle
Access
```

# 22. Data Inventory

Material datasets should be registered in an authoritative data inventory.

# 23. Dataset Attributes

Where appropriate:

```text
Dataset
Owner
Steward
Purpose
System
Classification
Criticality
Retention
Location
Dependencies
```

# 24. Data Classification

Data should be classified according to sensitivity, criticality, regulatory requirements and business value.

# 25. Classification Categories

Where appropriate, organizations may define categories such as:

```text
Public
Internal
Confidential
Restricted
```

# 26. Classification Ownership

Classification should have accountable ownership and review.

# 27. Sensitive Data

Sensitive or regulated data should receive enhanced controls according to applicable requirements.

# 28. Personal Data

Personal data should be governed according to applicable privacy and data-protection requirements.

# 29. Data Access

Access should follow:

```text
Least Privilege
Need-to-Know
Purpose Limitation
Authorization
Logging
```

# 30. Data Sharing

Data sharing should define:

```text
Purpose
Source
Recipient
Data
Authorization
Security
Retention
```

requirements.

# 31. Master Data

Master data represents shared business entities requiring consistent enterprise treatment.

# 32. Master Data Domains

Material master data may include:

```text
Customer
Supplier
Employee
Product
Asset
Location
Organization
```

where applicable.

# 33. Master Data Ownership

Each master data domain should have accountable ownership.

# 34. Master Data Record

Master records should have defined:

```text
Identifier
Attributes
Source
Owner
Status
Lifecycle
```

# 35. Golden Record

Where appropriate, a trusted authoritative representation should be established for shared master entities.

# 36. Master Data Matching

Duplicate master records should be identified and resolved according to defined rules.

# 37. Master Data Synchronization

Master data synchronization between systems should be controlled and monitored.

# 38. Reference Data

Reference data provides standardized values used consistently across systems.

# 39. Reference Data Governance

Reference data should have:

```text
Owner
Definition
Allowed Values
Effective Date
Version
Retirement
```

# 40. Metadata

Metadata should describe relevant:

```text
Meaning
Structure
Owner
Source
Classification
Lineage
Lifecycle
```

information.

# 41. Business Metadata

Business metadata should explain data meaning and business context.

# 42. Technical Metadata

Technical metadata may include:

```text
Tables
Columns
Types
Interfaces
Systems
Storage
```

# 43. Operational Metadata

Operational metadata may include:

```text
Refresh
Processing
Availability
Usage
Quality
Execution
```

information.

# 44. Metadata Ownership

Material metadata should have defined ownership and stewardship.

# 45. Data Lineage

Data lineage should identify relevant movement and transformation from source to consumption.

# 46. Lineage Scope

Critical data should have sufficient lineage across:

```text
Source
Integration
Transformation
Storage
Reporting
Consumption
```

# 47. Lineage Use

Lineage should support:

```text
Impact Analysis
Incident Investigation
Compliance
Audit
Data Quality
Change
```

# 48. Data Quality

Data quality should be managed according to intended business use.

# 49. Data Quality Dimensions

Assess relevant:

```text
Accuracy
Completeness
Consistency
Timeliness
Validity
Uniqueness
Integrity
```

# 50. Data Quality Rules

Material datasets should have defined quality rules where appropriate.

# 51. Data Quality Thresholds

Quality thresholds should be defined according to:

```text
Business Need
Risk
Criticality
Regulation
```

# 52. Data Quality Monitoring

Material data quality should be monitored using appropriate measures.

# 53. Data Quality Issues

Issues should be:

```text
Detected
Logged
Classified
Assigned
Remediated
Validated
Closed
```

# 54. Data Quality Root Cause

Recurring data quality problems should identify underlying causes where practical.

# 55. Data Quality Remediation

Remediation should address:

```text
Source
Process
Application
Integration
User
Control
```

causes where applicable.

# 56. Data Quality Exceptions

Exceptions should be:

```text
Risk-Assessed
Approved
Time-Bounded
Reviewed
```

# 57. Data Standards

Enterprise data standards should define approved conventions for relevant:

```text
Names
Identifiers
Codes
Dates
Units
Formats
Values
```

# 58. Data Identifiers

Material entities should use controlled and sufficiently unique identifiers.

# 59. Data Definitions

Business-critical terms should have approved definitions.

# 60. Data Dictionary

The enterprise data dictionary should provide authoritative definitions for material data elements.

# 61. Data Contracts

Where appropriate, data exchanges should use controlled data contracts defining:

```text
Structure
Meaning
Quality
Version
Ownership
```

# 62. Data Integration

Data integration should support controlled movement and transformation of data between systems.

# 63. Integration Controls

Material data integration should consider:

```text
Validation
Security
Error Handling
Reconciliation
Lineage
Monitoring
```

# 64. Data Reconciliation

Material data transfers should use reconciliation where required to confirm completeness and integrity.

# 65. Data Transformation

Transformations should be documented and traceable where material.

# 66. Data Storage

Data storage should align with:

```text
Classification
Performance
Availability
Security
Retention
Cost
```

requirements.

# 67. Data Backup

Critical data should be backed up according to applicable recovery requirements.

# 68. Data Recovery

Recovery procedures should be tested according to data criticality.

# 69. Data Retention

Retention periods should be defined according to:

```text
Business Need
Legal Requirement
Regulatory Requirement
Contract
Risk
```

# 70. Retention Ownership

Retention requirements should have accountable ownership.

# 71. Legal Hold

Where applicable, legal holds should suspend normal disposal for affected data.

# 72. Data Archival

Data requiring long-term retention should be archived using controlled processes.

# 73. Archive Integrity

Archived data should maintain appropriate:

```text
Integrity
Accessibility
Traceability
Retention
Protection
```

# 74. Data Disposal

Data should be disposed of securely when retention requirements expire and no hold applies.

# 75. Disposal Evidence

Material data disposal should provide appropriate evidence.

# 76. Data Access Reviews

Access to sensitive or critical data should be reviewed according to risk and policy.

# 77. Data Usage Monitoring

Where appropriate, data usage should be monitored for:

```text
Unauthorized Access
Unexpected Consumption
Sensitive Data Exposure
Policy Violations
```

# 78. Data Security Coordination

Data governance should integrate with:

```text
Cybersecurity
Identity
Privacy
Application Security
Infrastructure Security
```

# 79. Data Privacy Coordination

Data governance should coordinate with privacy requirements concerning:

```text
Purpose
Minimization
Access
Retention
Rights
Protection
```

# 80. Data Architecture Coordination

Data architecture should integrate with:

```text
Application Architecture
Integration Architecture
Enterprise Architecture
Analytics
Cloud
Security
```

# 81. Data Consumer Management

Material data consumers should understand:

```text
Purpose
Definitions
Quality
Access
Restrictions
```

# 82. Data Product Governance

Where data products exist, each should have:

```text
Owner
Purpose
Consumers
Quality Expectations
Interface
Lifecycle
```

# 83. Data Reporting

Data reporting should use governed definitions and authoritative sources where required.

# 84. Data Analytics

Analytics should identify:

```text
Source
Definition
Transformation
Refresh
Quality
```

where material.

# 85. Data Assurance

Assurance may include:

```text
Data Quality Reviews
Lineage Reviews
Access Reviews
Retention Reviews
Master Data Reviews
Metadata Reviews
Internal Audit
Independent Assurance
```

# 86. Data Findings

Findings may identify weaknesses in:

```text
Ownership
Definitions
Quality
Lineage
Classification
Access
Retention
Integration
Master Data
Metadata
```

# 87. Data Evidence

Evidence should support:

```text
Ownership
Definitions
Quality
Access
Lineage
Retention
Disposal
Remediation
```

# 88. Data Exceptions

Exceptions should identify:

```text
Requirement
Deviation
Reason
Risk
Compensating Control
Approval
Expiry
Review
```

# 89. Data Remediation

Remediation should identify:

```text
Finding
Root Cause
Action
Owner
Due Date
Evidence
Validation
```

# 90. Data Metrics

Metrics may include:

```text
Data Quality Score
Completeness
Accuracy
Timeliness
Duplicate Rate
Critical Data Defects
Master Data Duplicate Rate
Metadata Coverage
Lineage Coverage
Data Owner Coverage
Data Steward Coverage
Retention Compliance
Data Disposal Completion
Access Review Completion
```

# 91. Data Dashboard

May include:

```text
Data Domains
Critical Datasets
Quality
Master Data
Metadata
Lineage
Classification
Access
Retention
Archival
Disposal
Findings
Remediation
```

# 92. Daily Review

Where appropriate:

```text
Critical Data Quality Failures
Critical Data Integration Failures
Sensitive Data Events
Critical Data Availability
```

# 93. Weekly Review

May consider:

```text
Data Quality Trends
Integration Failures
Master Data Issues
Metadata Gaps
Lineage Gaps
Open Remediation
```

# 94. Monthly Review

May consider:

```text
Data Quality
Critical Datasets
Master Data
Metadata
Lineage
Retention
Access Reviews
Data Issues
```

# 95. Quarterly Review

May consider:

```text
Data Strategy
Data Architecture
Data Domains
Quality
Master Data
Metadata
Lineage
Privacy
Security
Retention
Assurance
Maturity
```

# 96. Annual Review

May consider:

```text
Data Strategy
Architecture
Governance
Ownership
Quality
Master Data
Reference Data
Metadata
Lineage
Lifecycle
Retention
Archival
Disposal
Security
Privacy
Assurance
Maturity
Improvement
```

# 97. Data Maturity

Enterprise data management maturity should be periodically assessed.

# 98. Maturity Dimensions

Assess:

```text
Governance
Strategy
Ownership
Stewardship
Domains
Inventory
Classification
Access
Sharing
Master Data
Reference Data
Metadata
Lineage
Quality
Standards
Identifiers
Definitions
Dictionary
Contracts
Integration
Reconciliation
Transformation
Storage
Backup
Recovery
Retention
Legal Hold
Archival
Disposal
Security
Privacy
Consumers
Data Products
Reporting
Analytics
Exceptions
Remediation
Assurance
Metrics
Improvement
```

# 99. Maturity Levels

```text
1 – Initial
2 – Repeatable
3 – Defined
4 – Managed
5 – Optimized
```

# 100. Data Governance Quality Gate

```text
Domain
 ↓
Owner
 ↓
Steward
 ↓
Definition
 ↓
Classification
 ↓
Quality
 ↓
Lifecycle
 ↓
Assurance
```

must be controlled.

# 101. Data Quality Quality Gate

```text
Rule
 ↓
Threshold
 ↓
Measure
 ↓
Detect
 ↓
Issue
 ↓
Remediate
 ↓
Validate
```

must be controlled.

# 102. Master Data Quality Gate

```text
Entity
 ↓
Identifier
 ↓
Authoritative Source
 ↓
Match
 ↓
Validate
 ↓
Synchronize
 ↓
Monitor
```

must be controlled.

# 103. Metadata Quality Gate

```text
Meaning
 ↓
Structure
 ↓
Owner
 ↓
Source
 ↓
Lineage
 ↓
Lifecycle
 ↓
Review
```

must be controlled.

# 104. Data Lifecycle Quality Gate

```text
Create / Acquire
 ↓
Classify
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

must be controlled.

# 105. Data Assurance Quality Gate

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
Validation
```

must be traceable.

# 106. Definition of Ready

A data domain, dataset, data quality rule, master data object, metadata record, lineage model, data contract, lifecycle decision, exception, remediation or assurance review is Ready when purpose, owner, steward, scope, classification, requirements, dependencies, quality expectations, lifecycle, access requirements, decision authority and acceptance criteria are defined.

# 107. Definition of Done

A data-management work item is Done when:

```text
Requirement Identified
        ↓
Owner Assigned
        ↓
Data Governance / Architecture / Quality / Lifecycle Action Completed
        ↓
Business / Security / Privacy / Technical / Risk Validation Completed where Required
        ↓
Data / Metadata / Lineage / Inventory Records Updated
        ↓
Evidence Captured
        ↓
Findings / Exceptions Addressed
        ↓
Outcome Accepted
```

# 108. Final Data Governance Principle

> **MFM must govern enterprise data as a strategic and controlled asset so that data remains accurate, complete, consistent, secure, traceable, available, appropriately retained and fit for business use.**

# 109. Final Ownership Principle

> **Every material data domain and critical dataset must have clear accountable ownership and appropriate stewardship.**

# 110. Final Quality Principle

> **Data quality requirements must be defined according to business purpose, risk and criticality and continuously monitored where material.**

# 111. Final Master Data Principle

> **Shared business entities must have authoritative ownership and controlled synchronization to reduce duplication and inconsistent information.**

# 112. Final Metadata Principle

> **Material data must have sufficient metadata to explain its meaning, structure, ownership, source, classification, lineage and lifecycle.**

# 113. Final Lineage Principle

> **Critical data must have sufficient lineage to support impact analysis, operational investigation, compliance, audit and change management.**

# 114. Final Lifecycle Principle

> **Data must be managed throughout its lifecycle, including retention, archival and secure disposal when requirements expire.**

# 115. Final Security Principle

> **Data access and sharing must be controlled according to sensitivity, purpose, authorization, risk and applicable legal or regulatory requirements.**

# 116. Final Assurance Principle

> **Material data governance and quality controls must be supported by reliable evidence and periodically assessed through risk-based assurance.**

# 117. Final Improvement Principle

> **Data quality issues, lineage gaps, master data problems, metadata deficiencies and assurance findings must continuously improve MFM's enterprise data capability.**

# 118. Final Integration Principle

> **Data Management must integrate with Enterprise Architecture, Application Architecture, Integration Architecture, Service Management, IT Operations, Configuration Management, Asset Management, Cybersecurity, Identity, Privacy, Finance, Procurement, Suppliers, Risk, Compliance, Legal and Business Continuity.**

# 119. Final Steady-State Data Principle

> **MFM must govern enterprise data as a strategic and controlled asset so that data remains accurate, complete, consistent, secure, traceable, available, appropriately retained and fit for business use.**

# 120. Summary

MFM v1.2-Steady-State-97 establishes the permanent Enterprise Data Management baseline.

It defines:

- Data Architecture / Data Governance / Data Ownership / Data Stewardship
- Data Domains / Data Inventory / Dataset Attributes
- Data Classification / Sensitive Data / Personal Data
- Data Access / Data Sharing
- Master Data / Master Data Domains / Ownership / Records / Golden Records
- Master Data Matching / Synchronization
- Reference Data Governance
- Metadata / Business / Technical / Operational Metadata
- Metadata Ownership
- Data Lineage / Lineage Scope / Lineage Use
- Data Quality / Quality Dimensions / Rules / Thresholds / Monitoring
- Data Quality Issues / Root Cause / Remediation / Exceptions
- Data Standards / Identifiers / Definitions / Data Dictionary / Data Contracts
- Data Integration / Validation / Reconciliation / Transformation
- Data Storage / Backup / Recovery
- Data Retention / Legal Hold / Archival / Disposal / Disposal Evidence
- Data Access Reviews / Usage Monitoring
- Data Security / Privacy / Architecture Coordination
- Data Consumers / Data Products / Reporting / Analytics
- Data Assurance / Findings / Evidence / Exceptions / Remediation
- Data Metrics / Data Dashboard
- Daily / Weekly / Monthly / Quarterly / Annual Reviews
- Data Maturity
- Data Governance / Quality / Master Data / Metadata / Lifecycle / Assurance Quality Gates
- Definition of Ready
- Definition of Done

# 121. Next Document

**MFM v1.2-Steady-State-98 – Enterprise Data Security, Privacy, Information Classification, Records Management, Data Protection & Privacy Assurance**

It shall establish the permanent enterprise operating model for information classification, data protection, privacy governance, personal data management, records management, information handling, data access, privacy rights coordination, retention, legal holds, secure disposal, data loss prevention, information protection, privacy risk, records assurance, findings, exceptions, remediation, privacy metrics, dashboards, maturity and continual enterprise information protection and privacy improvement supporting MFM.

# 122. Document Control

**Document:** MFM v1.2-Steady-State-97  
**Version:** 1.2  
**Status:** Steady-State Enterprise Data Management Baseline  
**Previous Document:** MFM v1.2-Steady-State-96  
**Next Document:** MFM v1.2-Steady-State-98  
**Lifecycle:** Steady-State Operation  
**Data Authority:** Enterprise Data Management  
**Data Architecture Authority:** Data Architecture  
**Data Governance Authority:** Data Governance  
**Data Quality Authority:** Data Quality Management  
**Master Data Authority:** Master Data Management  
**Metadata Authority:** Metadata Management  
**Lineage Authority:** Data Lineage Management  
**Service Authority:** Enterprise Service Management  
**Application Authority:** Enterprise Application Management  
**Architecture Authority:** Enterprise Architecture  
**Operations Authority:** Enterprise IT Operations  
**Configuration Authority:** Configuration Management  
**Asset Authority:** Enterprise Asset Management  
**Security Authority:** Cybersecurity / Information Security  
**Identity Authority:** Identity and Access Management  
**Privacy Authority:** Privacy / Data Protection  
**Finance Authority:** Finance / IT Financial Management  
**Procurement Authority:** Procurement / Sourcing  
**Supplier Authority:** Supplier / Third-Party Management  
**Risk Authority:** Enterprise Risk Management  
**Compliance Authority:** Enterprise Compliance  
**Legal Authority:** Legal / Regulatory Affairs  
**Continuity Authority:** Business Continuity / Operational Resilience  
**Project Authority:** Project / Portfolio Management  
**Assurance Authority:** Data Assurance / Internal Audit / Independent Assurance  
**Improvement Authority:** Continual Enterprise Data Management Improvement  

**Principle:** MFM must govern enterprise data as a strategic and controlled asset so that data remains accurate, complete, consistent, secure, traceable, available, appropriately retained and fit for business use.
