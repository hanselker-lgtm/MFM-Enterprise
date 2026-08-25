# MFM v1.2-Steady-State-120
## Enterprise Data Architecture, Data Governance, Data Management, Data Quality, Data Security, Data Lifecycle & Data Assurance

**Version:** 1.2  
**Document ID:** MFM v1.2-Steady-State-120  
**Status:** Steady-State Enterprise Data Architecture & Data Management Baseline  
**Lifecycle:** Post-Implementation / Steady-State Operation  
**Document Type:** Data Architecture / Data Governance / Data Management / Data Quality / Data Security / Data Lifecycle / Data Assurance Document  

---

# 1. Purpose

This document establishes the one-hundred-and-twentieth document in the MFM v1.2 Steady-State series.

It follows MFM v1.2-Steady-State-119 – Enterprise Cloud Architecture, Cloud Governance, Cloud Security, Cloud Operations, Cloud FinOps, Cloud Resilience & Cloud Assurance.

The purpose is to establish the permanent enterprise operating model for data strategy, data governance, data ownership, data domains, data architecture, master data, reference data, metadata, data quality, data classification, data lineage, data integration, data platforms, databases, data lakes, data warehouses, analytics data, data retention, archival, deletion, data security, privacy integration, data access, data incidents, data risk, data compliance, data exceptions, remediation, data assurance, metrics, dashboards, maturity and continual enterprise data capability improvement.

The central objective is:

> **MFM must govern data as a strategic enterprise asset, ensuring that data is owned, understood, classified, protected, accurate, accessible to authorized users, traceable throughout its lifecycle and managed in accordance with business, security, privacy, regulatory and operational requirements.**

---

# 2. Scope

This document covers:

- Data Strategy
- Data Governance
- Data Ownership
- Data Domains
- Data Architecture
- Master Data
- Reference Data
- Metadata
- Data Quality
- Data Classification
- Data Lineage
- Data Integration
- Data Platforms
- Databases
- Data Lakes
- Data Warehouses
- Analytics Data
- Data Retention
- Data Archival
- Data Deletion
- Data Security
- Privacy Integration
- Data Access
- Data Incidents
- Data Risk
- Data Compliance
- Data Exceptions
- Data Remediation
- Data Assurance
- Data Metrics
- Data Dashboards
- Data Maturity
- Continual Enterprise Data Capability Improvement

---

# 3. Data Governance Objective

The primary objective is:

> **Establish clear authority, ownership, accountability, standards, controls and assurance for enterprise data throughout its lifecycle.**

# 4. Data Architecture Objective

The primary objective is:

> **Provide a coherent enterprise data architecture that supports business processes, applications, analytics, integration, security, privacy, interoperability and long-term information value.**

# 5. Data Quality Objective

The primary objective is:

> **Ensure that material data is sufficiently accurate, complete, consistent, timely, valid, unique and fit for its intended purpose.**

# 6. Data Security Objective

The primary objective is:

> **Protect data against unauthorized access, alteration, disclosure, loss, destruction and misuse throughout its lifecycle.**

# 7. Data Lifecycle Objective

The primary objective is:

> **Govern data from creation and acquisition through use, sharing, retention, archival and secure deletion.**

# 8. Data Assurance Objective

The primary objective is:

> **Provide evidence that data governance, quality, security, lifecycle and management controls operate effectively.**

# 9. Data Principles

Data should be:

```text
Owned
Defined
Classified
Accurate
Complete
Consistent
Timely
Secure
Traceable
Lifecycle-Controlled
```

# 10. Data Governance Principles

Data governance should be:

```text
Accountable
Business-Aligned
Domain-Based
Risk-Based
Evidence-Based
Continuously Improved
```

# 11. Data Security Principles

Data security should be:

```text
Risk-Based
Least-Privilege
Need-to-Know
Classified
Encrypted where Required
Monitored
Auditable
```

# 12. Data Quality Principles

Data quality should be:

```text
Measured
Purpose-Driven
Owned
Monitored
Remediated
Continuously Improved
```

# 13. Data Lifecycle

Data management should integrate:

```text
Create / Acquire
 ↓
Classify
 ↓
Store
 ↓
Process
 ↓
Use
 ↓
Share
 ↓
Retain
 ↓
Archive
 ↓
Delete / Dispose
```

# 14. Data Governance

Data governance should establish:

```text
Authority
Ownership
Domains
Standards
Policies
Quality
Security
Privacy
Lifecycle
Risk
Assurance
Improvement
```

# 15. Data Authority

Data authority should define who may:

```text
Approve Data Strategy
Approve Data Architecture
Approve Data Standards
Approve Data Classification
Approve Material Data Sharing
Approve Material Exceptions
Accept Data Risk
```

# 16. Data Ownership

Material data domains should have accountable owners for:

```text
Business Meaning
Quality
Access
Security
Lifecycle
Compliance
Risk
```

# 17. Data Stewardship

Data stewards should support:

```text
Definitions
Quality
Metadata
Lineage
Issue Management
Access Governance
```

# 18. Data Domains

Enterprise data should be organized into meaningful domains according to business capabilities.

Examples may include:

```text
Customer
Supplier
Employee
Finance
Operations
Asset
Product
Service
Regulatory
Reference
```

# 19. Data Domain Governance

Each material domain should have:

```text
Owner
Steward
Definitions
Critical Data Elements
Quality Rules
Classification
Lifecycle
Access Model
```

# 20. Data Architecture

Data architecture should align with:

```text
Enterprise Architecture
Business Architecture
Application Architecture
Integration Architecture
Security Architecture
Cloud Architecture
Infrastructure Architecture
```

# 21. Data Architecture Principles

Data architecture should support:

```text
Interoperability
Reuse
Scalability
Security
Traceability
Resilience
Lifecycle Management
```

# 22. Data Models

Material data models should be governed for:

```text
Purpose
Ownership
Version
Relationships
Definitions
Constraints
Lifecycle
```

# 23. Conceptual Data Model

Enterprise-level conceptual models should describe important business concepts and relationships.

# 24. Logical Data Model

Logical models should define relevant structures independent of implementation where appropriate.

# 25. Physical Data Model

Physical models should reflect actual implementation requirements.

# 26. Canonical Data Models

Where integration requires consistent representations, canonical models may be established.

# 27. Master Data

Master data represents authoritative core business entities.

Examples may include:

```text
Customer
Supplier
Employee
Asset
Product
Organization
```

# 28. Master Data Governance

Master data should have:

```text
Authoritative Source
Owner
Steward
Definition
Quality Rules
Lifecycle
```

# 29. Golden Record

Where appropriate, a trusted representation of a material master-data entity should be maintained.

# 30. Reference Data

Reference data should provide controlled values such as:

```text
Country
Currency
Status
Category
Classification
Code
```

# 31. Reference Data Governance

Reference data should be:

```text
Defined
Versioned
Owned
Controlled
Published
Reviewed
```

# 32. Metadata

Metadata should describe data meaning, structure, ownership, sensitivity, lineage and lifecycle where appropriate.

# 33. Business Metadata

Business metadata should define:

```text
Business Term
Meaning
Owner
Domain
Usage
Criticality
```

# 34. Technical Metadata

Technical metadata may include:

```text
System
Table
Column
Type
Source
Destination
Transformation
```

# 35. Operational Metadata

Operational metadata may include:

```text
Load Time
Refresh Status
Processing Status
Usage
Quality Status
```

# 36. Data Catalog

A data catalog should provide discoverability for material data assets.

Catalog information may include:

```text
Asset
Owner
Description
Classification
Source
Lineage
Quality
Access
Lifecycle
```

# 37. Data Discovery

Authorized users should be able to discover relevant data while respecting classification and access controls.

# 38. Data Classification

Data should be classified according to:

```text
Sensitivity
Business Impact
Security
Privacy
Regulatory Requirements
```

# 39. Classification Levels

Organizations may use an approved classification model such as:

```text
Public
Internal
Confidential
Restricted
```

# 40. Classification Ownership

Data owners should be accountable for appropriate classification.

# 41. Data Handling

Handling requirements should reflect classification and risk.

# 42. Data Access

Access should be governed by:

```text
Business Need
Need-to-Know
Least Privilege
Data Classification
Role
Risk
```

# 43. Data Access Approval

Sensitive data access should require appropriate authorization.

# 44. Data Access Reviews

Sensitive or privileged data access should be periodically reviewed.

# 45. Data Sharing

Material data sharing should have:

```text
Purpose
Owner
Recipient
Data Scope
Classification
Security
Legal / Contractual Basis where Required
Retention
```

# 46. External Data Sharing

External sharing should be risk-assessed and appropriately authorized.

# 47. Data Contracts

Where appropriate, data producers and consumers should use defined data contracts covering:

```text
Schema
Meaning
Quality
Availability
Version
Change
```

# 48. Data Integration

Data integration should be:

```text
Controlled
Traceable
Secure
Observable
Recoverable
```

# 49. Integration Patterns

Appropriate patterns may include:

```text
API
Event
Batch
Streaming
File Transfer
Replication
```

# 50. Data Transformation

Material transformations should be documented and traceable.

# 51. Data Lineage

Lineage should identify material relationships from:

```text
Source
 ↓
Ingestion
 ↓
Transformation
 ↓
Storage
 ↓
Processing
 ↓
Consumption
```

# 52. Business Lineage

Business lineage should explain how important data supports business processes and decisions.

# 53. Technical Lineage

Technical lineage should identify systems, datasets and transformations.

# 54. Lineage Criticality

Lineage requirements should be prioritized according to:

```text
Business Criticality
Regulatory Importance
Risk
Data Sensitivity
```

# 55. Data Platforms

Data platforms should be governed according to their purpose.

Examples may include:

```text
Operational Databases
Data Warehouses
Data Lakes
Lakehouses
Analytics Platforms
Integration Platforms
```

# 56. Database Governance

Databases should have:

```text
Owner
Purpose
Classification
Availability
Backup
Recovery
Security
Lifecycle
```

# 57. Data Warehouse

Data warehouses should have controlled:

```text
Data Sources
Transformation
Quality
Access
Performance
Retention
```

# 58. Data Lake

Data lakes should have controls for:

```text
Zones
Metadata
Classification
Access
Retention
Quality
Lifecycle
```

# 59. Analytics Data

Analytics data should remain traceable to authoritative sources where material.

# 60. Data Processing

Data processing should have:

```text
Owner
Purpose
Source
Transformation
Destination
Security
Monitoring
```

# 61. Data Quality

Material data quality should be measured against defined requirements.

# 62. Data Quality Dimensions

Quality may include:

```text
Accuracy
Completeness
Consistency
Timeliness
Validity
Uniqueness
Integrity
```

# 63. Critical Data Elements

Critical data elements should be identified according to business importance.

# 64. Data Quality Rules

Quality rules should define measurable expectations.

# 65. Data Quality Monitoring

Quality should be monitored using appropriate controls and metrics.

# 66. Data Quality Issues

Quality issues should be:

```text
Logged
Prioritized
Assigned
Investigated
Remediated
Validated
```

# 67. Data Quality Root Cause

Root-cause analysis should consider:

```text
Source
Process
Application
Integration
Transformation
Human Input
Governance
```

# 68. Data Quality Thresholds

Material quality thresholds should be defined for critical data.

# 69. Data Validation

Validation should occur at appropriate points such as:

```text
Capture
Ingestion
Transformation
Publication
Consumption
```

# 70. Data Reconciliation

Material datasets should be reconciled where appropriate.

# 71. Data Security

Data security should protect:

```text
Confidentiality
Integrity
Availability
```

# 72. Encryption at Rest

Sensitive data should use appropriate encryption at rest.

# 73. Encryption in Transit

Sensitive data should use appropriate encryption in transit.

# 74. Data Masking

Sensitive data may be masked or anonymized for lower-risk environments.

# 75. Tokenization

Tokenization may be used where appropriate to reduce exposure of sensitive values.

# 76. Non-Production Data

Production data should not be copied into non-production environments without appropriate authorization and protection.

# 77. Data Loss Prevention

Where appropriate, data-loss-prevention controls should detect and reduce unauthorized data disclosure.

# 78. Data Access Logging

Material access to sensitive data should be logged according to risk and requirements.

# 79. Data Monitoring

Monitoring should identify relevant:

```text
Unauthorized Access
Unusual Usage
Bulk Extraction
Data Movement
Quality Failures
Processing Failures
```

# 80. Data Incidents

Data incidents may include:

```text
Unauthorized Disclosure
Unauthorized Access
Data Corruption
Data Loss
Data Destruction
Integrity Failure
Privacy Incident
Availability Failure
```

# 81. Data Incident Response

Response should integrate:

```text
Detect
 ↓
Triage
 ↓
Contain
 ↓
Investigate
 ↓
Recover
 ↓
Validate
 ↓
Notify where Required
 ↓
Learn
```

# 82. Data Recovery

Recovery should consider:

```text
Backup
Replication
RTO
RPO
Integrity
Dependencies
```

# 83. Data Backup

Critical data should have backup arrangements aligned with business requirements.

# 84. Data Restore Testing

Critical data recovery should be tested periodically according to risk.

# 85. Data Retention

Retention should be based on:

```text
Business Need
Legal Requirements
Regulatory Requirements
Contractual Requirements
Risk
```

# 86. Retention Rules

Material data classes should have defined retention rules where required.

# 87. Data Archival

Data requiring long-term retention should be archived using controlled mechanisms.

# 88. Archive Access

Archived data should retain appropriate:

```text
Security
Integrity
Metadata
Ownership
Retrievability
```

# 89. Secure Deletion

Data should be securely deleted when retention requirements expire and deletion is authorized.

# 90. Deletion Evidence

Material deletion should be traceable where required.

# 91. Data Lifecycle Exceptions

Exceptions to retention or deletion requirements should be formally governed.

# 92. Privacy Integration

Data governance should integrate with applicable privacy and data-protection requirements.

# 93. Privacy by Design

Material data architectures and processing should consider privacy requirements from design onward.

# 94. Personal Data

Personal data should be identified and handled according to applicable requirements.

# 95. Data Processing Records

Where required, material processing activities should be documented and governed.

# 96. Data Subject Requirements

Where applicable, data processes should support authorized data-subject rights and obligations.

# 97. Data Compliance

Data management should comply with applicable:

```text
Policies
Standards
Contracts
Legal Requirements
Regulatory Requirements
Privacy Requirements
```

# 98. Data Compliance Monitoring

Compliance should be periodically assessed according to risk.

# 99. Data Risk

Data risks should be:

```text
Identified
Assessed
Owned
Treated
Monitored
Reported
```

# 100. Data Risk Factors

Assessment may consider:

```text
Sensitivity
Criticality
Volume
Exposure
Quality
Availability
Integrity
Privacy
Regulatory Impact
```

# 101. Data Exceptions

Exceptions should identify:

```text
Requirement
Deviation
Reason
Risk
Compensating Control
Owner
Approval
Expiry
Review
```

# 102. Data Remediation

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

# 103. Data Assurance

Assurance may include:

```text
Data Governance Reviews
Architecture Reviews
Data Quality Reviews
Classification Reviews
Access Reviews
Lineage Reviews
Data Security Reviews
Retention Reviews
Privacy Reviews
Backup / Recovery Tests
Supplier Reviews
Internal Audit
Independent Assurance
```

# 104. Data Evidence

Evidence should support:

```text
Governance
Ownership
Domains
Definitions
Metadata
Classification
Access
Sharing
Integration
Lineage
Quality
Security
Backup
Recovery
Retention
Archival
Deletion
Privacy
Risk
Compliance
Exceptions
Remediation
Assurance
```

# 105. Data Metrics

Metrics may include:

```text
Data Domain Ownership Coverage
Data Stewardship Coverage
Data Catalog Coverage
Critical Data Element Coverage
Metadata Completeness
Business Definition Coverage
Technical Metadata Coverage
Data Classification Coverage
Sensitive Data Identification Coverage
Data Quality Score
Accuracy
Completeness
Consistency
Timeliness
Validity
Uniqueness
Data Quality Issue Volume
Data Quality Remediation Time
Data Lineage Coverage
Critical Data Lineage Coverage
Data Access Review Completion
Sensitive Data Access Review Completion
Data Sharing Review Completion
Encryption Coverage
Data Loss Prevention Coverage
Production Data in Non-Production Findings
Data Incident Volume
Data Loss Events
Data Integrity Events
Backup Success Rate
Restore Test Success
RTO Achievement
RPO Achievement
Retention Compliance
Deletion Compliance
Archive Integrity
Privacy Compliance
Data Risk Exposure
Exception Age
Remediation Completion
Data Assurance Findings
```

# 106. Data Dashboard

May include:

```text
Data Governance
Data Domains
Ownership
Catalog
Metadata
Classification
Access
Sharing
Lineage
Quality
Security
Privacy
Backup
Recovery
Retention
Archival
Deletion
Incidents
Risk
Compliance
Assurance
Improvement
```

# 107. Daily Review

Where appropriate:

```text
Critical Data Quality Failures
Data Processing Failures
Sensitive Data Security Alerts
Data Access Anomalies
Data Integration Failures
Critical Backup Failures
```

# 108. Weekly Review

May consider:

```text
Data Quality Trends
Data Incidents
Integration Failures
Access Changes
Lineage Issues
Backup Health
Open Remediation
```

# 109. Monthly Review

May consider:

```text
Data Governance
Domains
Ownership
Catalog
Metadata
Classification
Access
Sharing
Lineage
Quality
Security
Privacy
Backup
Recovery
Retention
Risk
Compliance
Assurance
```

# 110. Quarterly Review

May consider:

```text
Data Strategy
Architecture
Governance
Domain Ownership
Master Data
Reference Data
Metadata
Quality
Lineage
Security
Privacy
Lifecycle
Supplier Risk
Compliance
Assurance
Maturity
```

# 111. Annual Review

May consider:

```text
Data Strategy
Operating Model
Governance
Architecture
Domains
Master Data
Reference Data
Metadata
Catalog
Classification
Access
Sharing
Integration
Lineage
Data Platforms
Databases
Warehouses
Lakes
Analytics
Quality
Security
Privacy
Backup
Recovery
Retention
Archival
Deletion
Risk
Compliance
Exceptions
Remediation
Assurance
Maturity
Improvement
```

# 112. Data Maturity

Data capability maturity should be periodically assessed.

# 113. Maturity Dimensions

Assess:

```text
Governance
Strategy
Authority
Ownership
Stewardship
Data Domains
Domain Governance
Architecture
Data Models
Conceptual Models
Logical Models
Physical Models
Canonical Models
Master Data
Golden Records
Reference Data
Metadata
Business Metadata
Technical Metadata
Operational Metadata
Data Catalog
Data Discovery
Classification
Handling
Access
Access Approval
Access Reviews
Data Sharing
External Sharing
Data Contracts
Integration
Integration Patterns
Transformation
Lineage
Business Lineage
Technical Lineage
Data Platforms
Database Governance
Data Warehouses
Data Lakes
Analytics Data
Data Processing
Data Quality
Quality Dimensions
Critical Data Elements
Quality Rules
Quality Monitoring
Quality Issues
Root Cause
Thresholds
Validation
Reconciliation
Data Security
Encryption
Masking
Tokenization
Non-Production Data
DLP
Access Logging
Monitoring
Data Incidents
Incident Response
Recovery
Backup
Restore Testing
Retention
Archival
Archive Access
Secure Deletion
Privacy
Personal Data
Processing Records
Data Subject Requirements
Compliance
Risk
Exceptions
Remediation
Assurance
Evidence
Metrics
Improvement
```

# 114. Maturity Levels

```text
1 – Initial
2 – Repeatable
3 – Defined
4 – Managed
5 – Optimized
```

# 115. Data Architecture Quality Gate

```text
Business Requirement
 ↓
Data Requirement
 ↓
Ownership
 ↓
Classification
 ↓
Architecture
 ↓
Security
 ↓
Quality
 ↓
Lineage
 ↓
Lifecycle
 ↓
Assurance
```

must be controlled.

# 116. Data Access Quality Gate

```text
Business Need
 ↓
Data Classification
 ↓
Identity
 ↓
Permission
 ↓
Approval
 ↓
Provision
 ↓
Monitor
 ↓
Review
```

must be controlled.

# 117. Data Sharing Quality Gate

```text
Purpose
 ↓
Owner
 ↓
Recipient
 ↓
Data Scope
 ↓
Classification
 ↓
Security / Privacy
 ↓
Authorization
 ↓
Retention
 ↓
Evidence
```

must be controlled.

# 118. Data Quality Quality Gate

```text
Requirement
 ↓
Rule
 ↓
Measure
 ↓
Issue
 ↓
Root Cause
 ↓
Remediation
 ↓
Validation
 ↓
Monitor
```

must be controlled.

# 119. Data Lifecycle Quality Gate

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
Delete
 ↓
Evidence
```

must be controlled.

# 120. Data Recovery Quality Gate

```text
Failure
 ↓
Assess
 ↓
Recover
 ↓
Validate Integrity
 ↓
Validate RTO / RPO
 ↓
Communicate
 ↓
Review
```

must be controlled.

# 121. Data Assurance Quality Gate

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

# 122. Definition of Ready

A data architecture, data domain, master-data object, reference-data set, data asset, data model, data integration, data-sharing arrangement, quality rule, classification, access model, retention rule, archival arrangement, deletion process, exception, remediation or assurance review is Ready when purpose, owner, scope, classification, dependencies, business requirements, security and privacy requirements, lifecycle requirements, risk, approval authority and acceptance criteria are defined.

# 123. Definition of Done

A data work item is Done when:

```text
Requirement / Data Event Identified
        ↓
Owner Assigned
        ↓
Data Action Completed
        ↓
Quality / Security / Privacy / Lifecycle Validation Completed where Required
        ↓
Data / Metadata / Lineage / Access / Catalog / Quality Records Updated
        ↓
Evidence Captured
        ↓
Findings / Exceptions Addressed
        ↓
Outcome Accepted
```

# 124. Final Data Governance Principle

> **MFM must govern data as a strategic enterprise asset, ensuring that data is owned, understood, classified, protected, accurate, accessible to authorized users, traceable throughout its lifecycle and managed in accordance with business, security, privacy, regulatory and operational requirements.**

# 125. Final Ownership Principle

> **Every material data domain and critical data asset must have clear accountability for business meaning, quality, access, security, lifecycle and risk.**

# 126. Final Quality Principle

> **Material data must be sufficiently accurate, complete, consistent, timely, valid, unique and fit for its intended purpose, with measurable quality rules and accountable remediation.**

# 127. Final Classification Principle

> **Data classification must reflect sensitivity, business impact, security, privacy and regulatory requirements and must drive appropriate handling controls.**

# 128. Final Access Principle

> **Data access must be based on legitimate business need, need-to-know, least privilege, classification and risk, with appropriate approval and periodic review.**

# 129. Final Lineage Principle

> **Material data must be sufficiently traceable from source through transformation and storage to business consumption to support trust, impact analysis, compliance and assurance.**

# 130. Final Lifecycle Principle

> **Data must be governed from creation and acquisition through use, sharing, retention, archival and secure deletion.**

# 131. Final Security Principle

> **Data security must protect confidentiality, integrity and availability through appropriate access control, encryption, monitoring, segregation and lifecycle controls.**

# 132. Final Privacy Principle

> **Where personal data is processed, data architecture and management must incorporate applicable privacy and data-protection requirements throughout the data lifecycle.**

# 133. Final Assurance Principle

> **Material data controls and data assets must be supported by reliable evidence and periodically assessed through risk-based assurance.**

# 134. Final Improvement Principle

> **Data quality issues, security incidents, access findings, lineage gaps, lifecycle failures, privacy findings and assurance results must continuously improve MFM's data capability.**

# 135. Final Integration Principle

> **Data Architecture and Data Management must integrate with Enterprise Architecture, Applications, Integration, Identity, Network, Infrastructure, Cloud, Cybersecurity, IT Service Management, Finance, Privacy, Risk, Compliance, Legal, Suppliers and Business Continuity.**

# 136. Final Steady-State Data Principle

> **MFM must govern data as a strategic enterprise asset, ensuring that data is owned, understood, classified, protected, accurate, accessible to authorized users, traceable throughout its lifecycle and managed in accordance with business, security, privacy, regulatory and operational requirements.**

# 137. Summary

MFM v1.2-Steady-State-120 establishes the permanent Enterprise Data Architecture and Data Management baseline.

It defines:

- Data Strategy / Governance / Authority / Ownership / Stewardship
- Data Domains / Domain Governance
- Data Architecture / Conceptual / Logical / Physical / Canonical Models
- Master Data / Golden Records
- Reference Data
- Metadata / Business / Technical / Operational Metadata
- Data Catalog / Data Discovery
- Data Classification / Handling
- Data Access / Approval / Reviews
- Data Sharing / External Sharing / Data Contracts
- Data Integration / Integration Patterns / Transformation
- Business and Technical Data Lineage
- Data Platforms / Databases / Warehouses / Lakes / Analytics
- Data Processing
- Data Quality / Quality Dimensions / Critical Data Elements / Rules
- Quality Monitoring / Issues / Root Cause / Thresholds / Validation / Reconciliation
- Data Security / Encryption / Masking / Tokenization
- Non-Production Data / DLP / Access Logging / Monitoring
- Data Incidents / Incident Response
- Data Recovery / Backup / Restore Testing
- Data Retention / Archival / Archive Access / Secure Deletion
- Privacy Integration / Privacy by Design / Personal Data
- Data Processing Records / Data Subject Requirements
- Data Compliance / Risk / Exceptions / Remediation
- Data Assurance / Evidence
- Data Metrics / Data Dashboard
- Daily / Weekly / Monthly / Quarterly / Annual Reviews
- Data Maturity
- Data Architecture / Access / Sharing / Quality / Lifecycle / Recovery / Assurance Quality Gates
- Definition of Ready
- Definition of Done

# 138. Next Document

**MFM v1.2-Steady-State-121 – Enterprise Application Architecture, Application Portfolio, Application Lifecycle, Integration, API Management, Application Security & Application Assurance**

It shall establish the permanent enterprise operating model for application strategy, application governance, application ownership, application portfolio management, application architecture, application lifecycle, application standards, application integration, APIs, application dependencies, application environments, application deployment, application monitoring, application performance, application security, application vulnerability management, application incidents, application changes, application releases, application resilience, application continuity, application suppliers, application compliance, application exceptions, remediation, application assurance, metrics, dashboards, maturity and continual enterprise application capability improvement supporting MFM.

# 139. Document Control

**Document:** MFM v1.2-Steady-State-120  
**Version:** 1.2  
**Status:** Steady-State Enterprise Data Architecture & Data Management Baseline  
**Previous Document:** MFM v1.2-Steady-State-119  
**Next Document:** MFM v1.2-Steady-State-121  
**Lifecycle:** Steady-State Operation  
**Data Governance Authority:** Enterprise Data Management  
**Data Architecture Authority:** Enterprise Data Architecture  
**Data Domain Authority:** Data Domain Owners  
**Data Stewardship Authority:** Data Stewardship  
**Data Quality Authority:** Data Quality Management  
**Metadata Authority:** Metadata / Data Catalog Management  
**Data Lineage Authority:** Data Lineage Management  
**Data Security Authority:** Data Security Architecture  
**Privacy Authority:** Privacy / Data Protection Governance  
**Data Platform Authority:** Data Platform Management  
**Database Authority:** Database Management  
**Integration Authority:** Enterprise Integration Architecture  
**Identity Authority:** Identity and Access Management  
**Cybersecurity Authority:** Enterprise Cybersecurity  
**Application Authority:** Enterprise Application Architecture  
**Network Authority:** Enterprise Network Architecture  
**Infrastructure Authority:** Enterprise Infrastructure Architecture  
**Cloud Authority:** Enterprise Cloud Architecture  
**Service Authority:** Enterprise IT Service Management  
**Configuration Authority:** Configuration Management  
**Asset Authority:** Enterprise Asset Management  
**Supplier Authority:** Supplier / Third-Party Management  
**Risk Authority:** Enterprise Risk Management  
**Compliance Authority:** Enterprise Compliance  
**Legal Authority:** Legal / Regulatory Affairs  
**Continuity Authority:** Business Continuity / Operational Resilience  
**Assurance Authority:** Data Assurance / Internal Audit / Independent Assurance  
**Improvement Authority:** Continual Enterprise Data Capability Improvement  

**Principle:** MFM must govern data as a strategic enterprise asset, ensuring that data is owned, understood, classified, protected, accurate, accessible to authorized users, traceable throughout its lifecycle and managed in accordance with business, security, privacy, regulatory and operational requirements.
