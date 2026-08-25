# MFM v1.2-Implementation-Phase-101
## Data Governance, Data Architecture, Master Data, Data Quality, Metadata, Information Lifecycle & Data Assurance Stabilization

**Version:** 1.2  
**Document ID:** MFM-v1.2-Implementation-Phase-101  
**Status:** Implementation Phase Baseline  
**Phase:** Data Governance, Data Architecture, Master Data, Data Quality, Metadata, Information Lifecycle & Data Assurance Stabilization  
**Document Type:** Implementation Execution Document  

---

# 1. Purpose

This document defines the one-hundred-and-first implementation phase following MFM v1.2-Implementation-Phase-100 – Enterprise Architecture, Technology Portfolio, Application Lifecycle, Infrastructure, Configuration, Asset & Technical Debt Stabilization.

The purpose of this phase is to establish a controlled enterprise data governance capability covering data ownership, data stewardship, data architecture, data domains, master data, reference data, data quality, data quality rules, data profiling, data lineage, metadata governance, data catalog, information lifecycle, data retention, data classification, data access, data sharing, data integration, data synchronization, data reconciliation, data issue management and data assurance.

The central objective is:

> **MFM must ensure that critical data is owned, understood, classified, governed, sufficiently accurate, traceable, appropriately protected and usable throughout its lifecycle.**

---

# 2. Scope

This phase covers:

- Enterprise Data Governance
- Data Ownership
- Data Stewardship
- Data Architecture
- Data Domains
- Master Data
- Reference Data
- Data Quality
- Data Quality Rules
- Data Profiling
- Data Lineage
- Metadata Governance
- Data Catalog
- Information Lifecycle
- Data Retention
- Data Classification
- Data Access
- Data Sharing
- Data Integration
- Data Synchronization
- Data Reconciliation
- Data Issue Management
- Data Assurance
- Data Governance Quality Gates

---

# 3. Data Governance Authority

Data Governance coordinates:

```text
Data Ownership
Data Stewardship
Data Architecture
Master Data
Reference Data
Quality
Metadata
Lineage
Lifecycle
Access
Sharing
Integration
Reconciliation
Assurance
```

It does not replace:

```text
Business Ownership
Security Governance
Privacy Governance
Records Governance
Application Ownership
Service Management
Enterprise Architecture
```

---

# 4. Data Governance Principles

Data governance should be:

```text
Business-Aligned
Accountable
Traceable
Consistent
Risk-Based
Quality-Oriented
Lifecycle-Aware
Secure
Privacy-Aware
Evidence-Based
```

---

# 5. Data Governance Objective

The primary objective is:

> **Ensure that data supporting MFM services, processes, decisions, reporting and obligations remains sufficiently accurate, complete, consistent, available, understandable, protected and traceable for its intended use.**

---

# 6. Data

Data is a recorded representation of information or facts used by MFM processes, services, systems and decisions.

---

# 7. Information

Information is data interpreted and used within a defined context.

---

# 8. Data Owner

A data owner is accountable for the business meaning, use, quality expectations, access requirements and governance of a defined data domain or dataset.

---

# 9. Data Steward

A data steward supports operational governance of data quality, definitions, metadata, issues and lifecycle requirements.

---

# 10. Data Custodian

A data custodian manages technical handling and protection of data on behalf of the accountable owner.

---

# 11. Data Domain

A data domain groups related data according to a coherent business subject.

---

# 12. Data Domain Register

The register should identify:

```text
Domain
Owner
Steward
Purpose
Criticality
Systems
Classification
Quality
Status
```

---

# 13. Critical Data

Critical data is data whose loss, corruption, unavailability or misuse could materially affect organizational objectives, services, compliance or decisions.

---

# 14. Critical Data Register

The register should identify:

```text
Dataset
Domain
Owner
Criticality
Classification
System
Quality
Retention
Access
Status
```

---

# 15. Data Architecture

Data architecture defines the structure, relationships, movement and governance of data across MFM.

---

# 16. Data Architecture Domains

Data architecture should consider:

```text
Data Domains
Data Models
Master Data
Reference Data
Metadata
Lineage
Integration
Storage
Access
Lifecycle
```

---

# 17. Conceptual Data Model

The conceptual model describes important business concepts and their relationships without prescribing implementation detail.

---

# 18. Logical Data Model

The logical model defines structured relationships, attributes and business rules independent of a specific physical implementation.

---

# 19. Physical Data Model

The physical model describes implementation-specific structures used by databases, applications or data platforms.

---

# 20. Data Model Governance

Material data models should have:

```text
Owner
Version
Purpose
Scope
Approval
Dependencies
Review
Status
```

---

# 21. Data Entity

A data entity represents a defined business object or concept.

---

# 22. Data Attribute

A data attribute describes a property of a data entity.

---

# 23. Data Definition

A data definition establishes the agreed meaning of a data element.

---

# 24. Business Glossary

The business glossary provides governed definitions for important business terms and data concepts.

---

# 25. Glossary Governance

Glossary terms should have:

```text
Term
Definition
Owner
Steward
Domain
Status
Review
```

---

# 26. Master Data

Master data represents stable, shared business entities used across multiple processes or systems.

---

# 27. Master Data Domains

Examples may include:

```text
Members
Organizations
Suppliers
Projects
Grants
Accounts
Assets
Services
```

according to MFM scope.

---

# 28. Master Data Ownership

Each material master data domain should have an accountable owner.

---

# 29. Master Data Record

A master record should have:

```text
Unique Identifier
Definition
Owner
Source
Status
Lifecycle
Quality
```

---

# 30. Golden Record

Where appropriate, a golden record represents the trusted consolidated version of a master entity.

---

# 31. Master Data Matching

Matching rules should identify records representing the same business entity.

---

# 32. Duplicate Management

Potential duplicates should be:

```text
Detected
Reviewed
Merged
Rejected
Tracked
```

as appropriate.

---

# 33. Reference Data

Reference data provides controlled values used to classify, interpret or validate other data.

---

# 34. Reference Data Register

The register should identify:

```text
Reference Set
Owner
Values
Meaning
Version
Effective Date
Status
```

---

# 35. Reference Data Change

Changes to controlled reference values should be governed and traceable.

---

# 36. Data Quality

Data quality is the degree to which data is fit for its intended use.

---

# 37. Data Quality Dimensions

Relevant dimensions may include:

```text
Accuracy
Completeness
Consistency
Timeliness
Validity
Uniqueness
Integrity
Availability
```

---

# 38. Data Quality Rule

A data quality rule defines an expected condition that data should satisfy.

---

# 39. Data Quality Rule Record

The record should identify:

```text
Rule
Dataset
Dimension
Threshold
Owner
Frequency
Result
Status
```

---

# 40. Data Profiling

Data profiling examines data characteristics to identify:

```text
Patterns
Missing Values
Duplicates
Outliers
Invalid Values
Relationships
```

---

# 41. Data Quality Baseline

A baseline establishes the measured quality state against which improvement can be assessed.

---

# 42. Data Quality Threshold

A threshold defines an acceptable or escalation level for a data quality measure.

---

# 43. Data Quality Issue

A data quality issue identifies data that fails an agreed quality requirement.

---

# 44. Data Issue Lifecycle

A baseline lifecycle is:

```text
Detect
 ↓
Register
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

# 45. Data Issue Record

The record should identify:

```text
Issue
Dataset
Cause
Impact
Owner
Action
Due Date
Evidence
Status
```

---

# 46. Root Cause Analysis

Material recurring data quality issues should be assessed for underlying causes.

---

# 47. Data Quality Remediation

Remediation may include:

```text
Correction
Validation
Process Change
System Change
Rule Change
Training
Migration
```

---

# 48. Data Lineage

Data lineage describes the movement and transformation of data through relevant systems and processes.

---

# 49. Lineage Scope

Material lineage should cover, where appropriate:

```text
Source
Transformation
Integration
Storage
Use
Reporting
```

---

# 50. Lineage Record

A lineage record should identify:

```text
Source
Target
Transformation
Owner
Process
System
Status
```

---

# 51. Critical Data Lineage

Critical datasets should have sufficient lineage to support:

```text
Impact Analysis
Troubleshooting
Audit
Reporting
Privacy
Recovery
```

---

# 52. Metadata

Metadata is structured information describing data, its meaning, context, ownership, lifecycle and use.

---

# 53. Metadata Governance

Metadata governance should define:

```text
Required Metadata
Ownership
Standards
Quality
Lifecycle
Access
Review
```

---

# 54. Technical Metadata

Technical metadata may include:

```text
System
Table
Field
Format
Type
Source
Location
```

---

# 55. Business Metadata

Business metadata may include:

```text
Definition
Owner
Purpose
Domain
Classification
Criticality
```

---

# 56. Operational Metadata

Operational metadata may include:

```text
Refresh
Processing
Status
Quality
Usage
Last Update
```

---

# 57. Data Catalog

The data catalog provides a governed inventory of relevant datasets and metadata.

---

# 58. Catalog Record

A catalog record may identify:

```text
Dataset
Description
Owner
Steward
Source
Classification
Quality
Lineage
Lifecycle
```

---

# 59. Catalog Search

Users should be able to locate relevant governed data according to authorized access.

---

# 60. Data Classification

Data should be classified according to sensitivity, criticality, regulatory requirements and intended use.

---

# 61. Classification Levels

MFM may use an approved classification model such as:

```text
Public
Internal
Confidential
Restricted
```

where appropriate.

---

# 62. Classification Ownership

Data owners are accountable for appropriate classification of their governed data.

---

# 63. Classification Review

Classification should be reviewed when:

```text
Use Changes
Sensitivity Changes
Regulation Changes
Data Is Combined
Lifecycle Changes
```

---

# 64. Data Access

Data access should follow:

```text
Need
Authorization
Purpose
Classification
Security
Privacy
```

requirements.

---

# 65. Data Access Review

Access to critical or sensitive data should be periodically reviewed.

---

# 66. Data Sharing

Data sharing should be governed by:

```text
Purpose
Authority
Recipient
Data
Security
Privacy
Contract
Retention
```

where applicable.

---

# 67. Data Sharing Agreement

Material external or controlled sharing should have documented requirements where appropriate.

---

# 68. Data Integration

Data integration connects data across systems or services.

---

# 69. Integration Pattern

Integration may use:

```text
API
Event
Message
File
Database
Workflow
```

according to architecture standards.

---

# 70. Data Synchronization

Synchronization maintains intended consistency of data across systems.

---

# 71. Synchronization Rules

Rules should define:

```text
Source
Target
Frequency
Direction
Conflict
Validation
Error Handling
```

---

# 72. Data Reconciliation

Reconciliation compares data between sources to identify unexpected differences.

---

# 73. Reconciliation Rule

A reconciliation rule should define:

```text
Source
Target
Population
Comparison
Tolerance
Frequency
Owner
Action
```

---

# 74. Reconciliation Exception

Unexpected differences should generate controlled exceptions and investigation where material.

---

# 75. Data Migration

Data migration transfers data between systems, structures or platforms.

---

# 76. Migration Governance

Migration should address:

```text
Scope
Mapping
Quality
Lineage
Transformation
Validation
Reconciliation
Retention
Security
```

---

# 77. Migration Validation

Migration should validate:

```text
Completeness
Accuracy
Integrity
Relationships
Business Meaning
```

---

# 78. Data Retention

Data retention defines how long data should be maintained according to business, legal, regulatory and operational requirements.

---

# 79. Retention Ownership

Retention requirements should have accountable ownership and align with records and information governance.

---

# 80. Data Disposal

Data disposal should be authorized and performed according to applicable retention, legal hold, security and privacy requirements.

---

# 81. Data Lifecycle

A baseline lifecycle is:

```text
Create
 ↓
Capture
 ↓
Use
 ↓
Share
 ↓
Store
 ↓
Retain
 ↓
Archive
 ↓
Dispose
```

---

# 82. Data Lifecycle Review

Material datasets should be reviewed for:

```text
Purpose
Quality
Access
Retention
Risk
```

---

# 83. Data Access Logging

Access to sensitive or critical data should be logged where required by risk or governance.

---

# 84. Data Usage

Material data use should remain aligned with:

```text
Purpose
Authorization
Policy
Contract
Privacy
```

requirements.

---

# 85. Data Quality Monitoring

Data quality monitoring should evaluate defined rules at appropriate frequencies.

---

# 86. Data Quality Dashboard

A dashboard may show:

```text
Quality
Failures
Trends
Critical Datasets
Open Issues
```

---

# 87. Data Governance Metrics

Metrics may include:

```text
Data Domains
Owned Datasets
Stewardship Coverage
```

---

# 88. Data Quality Metrics

Metrics may include:

```text
Accuracy
Completeness
Consistency
Timeliness
Validity
Uniqueness
```

---

# 89. Metadata Metrics

Metrics may include:

```text
Catalog Coverage
Metadata Completeness
Glossary Coverage
Lineage Coverage
```

---

# 90. Master Data Metrics

Metrics may include:

```text
Duplicate Rate
Master Record Quality
Matching Accuracy
Reference Data Currency
```

---

# 91. Data Integration Metrics

Metrics may include:

```text
Synchronization Success
Reconciliation Exceptions
Integration Failures
```

---

# 92. Data Issue Metrics

Metrics may include:

```text
Open Issues
High-Risk Issues
Overdue Issues
Mean Resolution Time
Recurrence
```

---

# 93. Data Assurance Metrics

Metrics may include:

```text
Assurance Coverage
Quality Evidence
Control Testing
Open Findings
```

---

# 94. Data Risk Indicators

Indicators may include:

```text
Critical Dataset Without Owner
Critical Dataset Without Lineage
Repeated Quality Failure
Unresolved Reconciliation Difference
Unclassified Sensitive Data
Stale Reference Data
Unmanaged Master Duplicate
```

---

# 95. Data Governance Dashboard

A dashboard may show:

```text
Domains
Owners
Quality
Metadata
Lineage
Issues
```

---

# 96. Master Data Dashboard

A dashboard may show:

```text
Master Domains
Quality
Duplicates
Exceptions
```

---

# 97. Data Quality Dashboard

A dashboard may show:

```text
Quality Dimensions
Rules
Failures
Trends
Remediation
```

---

# 98. Metadata Dashboard

A dashboard may show:

```text
Catalog
Metadata
Glossary
Lineage
Coverage
```

---

# 99. Data Assurance Dashboard

A dashboard may show:

```text
Controls
Evidence
Issues
Findings
Remediation
```

---

# 100. Data Governance Maturity

Data governance maturity should be reviewed periodically.

---

# 101. Maturity Dimensions

Assess:

```text
Governance
Ownership
Architecture
Master Data
Reference Data
Quality
Metadata
Lineage
Lifecycle
Access
Integration
Assurance
```

---

# 102. Maturity Levels

A baseline model is:

```text
1 – Initial
2 – Repeatable
3 – Defined
4 – Managed
5 – Optimized
```

---

# 103. Data Ownership Gate

Data governance passes when:

```text
Domain
 ↓
Dataset
 ↓
Owner
 ↓
Steward
 ↓
Purpose
 ↓
Classification
```

is defined.

---

# 104. Data Architecture Gate

Data architecture passes when:

```text
Entity
 ↓
Definition
 ↓
Model
 ↓
Source
 ↓
Target
 ↓
Lineage
```

is understood.

---

# 105. Master Data Gate

Master data governance passes when:

```text
Entity
 ↓
Identifier
 ↓
Source
 ↓
Matching
 ↓
Quality
 ↓
Lifecycle
```

is controlled.

---

# 106. Data Quality Gate

Data quality passes when:

```text
Dataset
 ↓
Dimension
 ↓
Rule
 ↓
Threshold
 ↓
Measurement
 ↓
Issue
 ↓
Remediation
```

is controlled.

---

# 107. Metadata Gate

Metadata governance passes when:

```text
Dataset
 ↓
Definition
 ↓
Owner
 ↓
Classification
 ↓
Lineage
 ↓
Lifecycle
```

is sufficiently documented.

---

# 108. Data Lifecycle Gate

Data lifecycle governance passes when:

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

# 109. Data Integration Gate

Data integration passes when:

```text
Source
 ↓
Transformation
 ↓
Transfer
 ↓
Validation
 ↓
Target
 ↓
Reconciliation
```

is controlled.

---

# 110. Data Assurance Gate

Data assurance passes when:

```text
Requirement
 ↓
Rule / Control
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

# 111. Definition of Ready

A data governance work item is Ready when:

- The data domain, dataset or data requirement is identified.
- Ownership is established.
- Business purpose and intended use are understood.
- Classification and criticality are known or ready for assessment.
- Relevant quality, metadata, lineage, lifecycle and access requirements are identified.
- Dependencies and affected systems are understood.
- Evidence and assurance requirements are defined.

---

# 112. Definition of Done

A data governance work item is Done when:

```text
Data Defined
        ↓
Owner Established
        ↓
Classification Established
        ↓
Quality Rules Defined
        ↓
Metadata Captured
        ↓
Lineage Established
        ↓
Lifecycle Controlled
        ↓
Access / Sharing Controlled
        ↓
Evidence Captured
        ↓
Assurance Passed
```

---

# 113. Final Data Governance Principle

> **Critical data must have accountable ownership, clear meaning, appropriate classification and controlled lifecycle management.**

---

# 114. Final Data Quality Principle

> **Data quality must be measured against defined requirements and material deficiencies must be owned, remediated and verified.**

---

# 115. Final Master Data Principle

> **Shared master data must have controlled identity, ownership, matching, lifecycle and quality so that different processes do not create conflicting versions of core entities.**

---

# 116. Final Metadata Principle

> **Important data must be understandable through governed definitions, metadata, ownership, classification and lineage.**

---

# 117. Final Lineage Principle

> **Material data flows must be sufficiently traceable to support impact analysis, reporting, troubleshooting, assurance, privacy and recovery.**

---

# 118. Final Lifecycle Principle

> **Data must be governed from creation through use, sharing, retention, archiving and authorized disposal.**

---

# 119. Final Integration Principle

> **Data Governance must integrate with Enterprise Architecture, Business Process, Applications, Security, Privacy, Records, Service Management, Reporting, Finance, Membership, Projects, Grants and Enterprise Assurance.**

---

# 120. Final Assurance Principle

> **Data assurance must provide evidence-based confidence that critical data is sufficiently accurate, complete, consistent, protected, traceable and fit for intended use.**

---

# 121. Final Implementation Principle

> **MFM should govern data through a controlled lifecycle connecting ownership, architecture, master data, reference data, quality, metadata, lineage, classification, access, sharing, integration, reconciliation, retention and assurance.**

---

# 122. Summary

MFM v1.2-Implementation-Phase-101 establishes the Data Governance, Data Architecture, Master Data, Data Quality, Metadata, Information Lifecycle and Data Assurance Stabilization baseline.

It defines:

- Enterprise Data Governance
- Data Ownership / Stewardship / Custodianship
- Data Domains / Domain Registers
- Critical Data / Critical Data Registers
- Data Architecture
- Conceptual / Logical / Physical Data Models
- Data Model Governance
- Data Entities / Attributes / Definitions
- Business Glossary / Glossary Governance
- Master Data / Master Data Domains / Ownership
- Master Data Records / Golden Records
- Matching / Duplicate Management
- Reference Data / Reference Data Registers / Change Governance
- Data Quality / Quality Dimensions / Quality Rules
- Data Profiling / Quality Baselines / Thresholds
- Data Quality Issues / Issue Lifecycle / Root Cause / Remediation
- Data Lineage / Lineage Records / Critical Data Lineage
- Metadata Governance / Technical / Business / Operational Metadata
- Data Catalog / Catalog Records / Catalog Search
- Data Classification / Classification Levels / Reviews
- Data Access / Access Reviews
- Data Sharing / Data Sharing Agreements
- Data Integration / Integration Patterns
- Data Synchronization / Synchronization Rules
- Data Reconciliation / Reconciliation Rules / Exceptions
- Data Migration / Migration Governance / Validation
- Data Retention / Disposal / Lifecycle
- Data Access Logging / Data Usage Governance
- Data Quality Monitoring
- Data Domain / Critical Data / Master Data / Reference Data / Quality / Issue / Lineage / Metadata / Catalog / Reconciliation / Assurance Registers
- Data Governance / Quality / Metadata / Master Data / Integration / Issue / Assurance Metrics
- Data Risk Indicators
- Data Governance / Master Data / Quality / Metadata / Assurance Dashboards
- Data Governance Maturity
- Data Ownership / Architecture / Master Data / Quality / Metadata / Lifecycle / Integration / Assurance Quality Gates
- Definition of Ready
- Definition of Done

---

# 123. Next Implementation Phase

The next document shall be:

**MFM v1.2-Implementation-Phase-102 – Integration Governance, API Management, Event Architecture, Interoperability, Workflow Orchestration & Integration Assurance Stabilization**

It shall establish the controlled implementation and validation of:

- Integration governance
- API management
- API lifecycle
- API standards
- Event architecture
- Event contracts
- Messaging
- Integration patterns
- Interoperability
- Data exchange
- Workflow orchestration
- Integration security
- API identity
- API authorization
- Integration monitoring
- Integration error handling
- Retry / recovery
- Integration testing
- Interface contracts
- Integration dependency management
- Integration assurance
- Integration quality gates

---

# 124. Document Control

**Document:** MFM v1.2-Implementation-Phase-101  
**Version:** 1.2  
**Status:** Implementation Phase Baseline  
**Previous Document:** MFM v1.2-Implementation-Phase-100  
**Next Document:** MFM v1.2-Implementation-Phase-102  
**Primary Transition:** Enterprise Architecture / Technology Portfolio / Application Lifecycle / Infrastructure / Configuration / Asset / Technical Debt → Data Governance / Data Architecture / Master Data / Data Quality / Metadata / Information Lifecycle / Data Assurance  
**Security Authority:** Security Core  
**Financial Authority:** Accounting Core  
**Membership Authority:** Membership Core  
**Project Authority:** Project Core  
**Grant Authority:** Grant Core  
**Document Authority:** Document Core  
**Reporting Authority:** Reporting Core  
**Workflow Authority:** Workflow Core  
**Integration Authority:** Integration Core  
**Data Quality Authority:** Data Quality / Integrity Control  
**Performance Authority:** Performance / Capacity Engineering  
**UX Authority:** User Experience / Accessibility / Human Factors  
**Assurance Authority:** Security Verification / Privacy / Compliance Assurance  
**Operational Authority:** Service Management / Operational Governance  
**Production Authority:** Production Readiness / Release Acceptance  
**Improvement Authority:** Continuous Improvement / Production Optimization  
**Architecture Authority:** Architecture Governance / Long-Term Evolution  
**Data Authority:** Enterprise Data Governance / Data Stewardship  
**Integration Authority:** Integration Governance / API & Interoperability  
**Process Authority:** Business Process Governance / BPM / Orchestration  
**Security Authority:** Enterprise Security Architecture / Zero Trust / Threat Management / Security Operations  
**Privacy Authority:** Privacy / Information Rights / Records Compliance / Data Protection  
**Financial Authority:** Financial Governance / Accounting / Internal Controls / Fiscal Compliance  
**Risk Authority:** Enterprise Risk Management / Business Risk / Control Assurance / Resilience Governance  
**Compliance Authority:** Enterprise Compliance Management / Regulatory Obligations / Policy Governance / Compliance Monitoring  
**Third-Party Authority:** Vendor / Supplier / Contract / Supply-Chain Governance  
**Architecture Portfolio Authority:** Enterprise Architecture / Capability / Application / Technology Portfolio Governance  
**Service Authority:** Enterprise Service Management / IT Operations / Service Catalog / SLA / Operational Performance  
**Configuration Authority:** Configuration Management / Asset Management / CMDB / Dependency Governance  
**Monitoring Authority:** Monitoring / Event Management / Observability / Alerting / Operational Telemetry  
**Incident Authority:** Incident / Major Incident / Problem / Root Cause / Operational Recovery Governance  
**Change Authority:** Change Enablement / Release / Deployment / CI/CD Governance  
**Service Level Authority:** Service Level Management / SLA / OLA / Operational Assurance  
**Financial Management Authority:** IT Financial Management / Cost Transparency / Budgeting / Chargeback / Technology Economics  
**Third-Party Authority:** Vendor / Supplier / Contract / Procurement / Third-Party Service Governance  
**Resilience Authority:** Business Continuity / Disaster Recovery / Resilience / Crisis Management / Operational Recovery  
**Security Operations Authority:** Information Security Operations / Identity / Access / Vulnerability / Security Monitoring  
**Data Governance Authority:** Enterprise Data Governance / Data Quality / Information Lifecycle / Master Data / Data Protection  
**Portfolio Governance Authority:** Application Portfolio / Technology Architecture / Configuration / Asset / Lifecycle Governance  
**Integration Governance Authority:** Enterprise Integration / API Management / Workflow Orchestration / Interoperability  
**Process Governance Authority:** Business Process Management / Process Automation / Case Management / Operational Workflow  
**Service Management Authority:** Enterprise Service Management / Service Catalog / SLA / Request / Incident / Problem / Operational Support  
**Financial Governance Authority:** Financial Management / Budgeting / Cost Control / Accounting / Procurement / Financial Assurance  
**Membership Governance Authority:** Membership / Member Experience / Communications / Engagement / Relationship Management  
**Project Governance Authority:** Project & Portfolio Management / Planning / Resource / Milestone / Delivery / Project Assurance  
**Grant Governance Authority:** Grant Management / Funding Lifecycle / Eligibility / Application / Award / Compliance / Grant Assurance  
**Document Governance Authority:** Document & Records Management / Information Lifecycle / Filing / Retention / Search / Archiving / Records Assurance  
**Procurement Governance Authority:** Procurement / Supplier / Contract / Vendor Lifecycle / Third-Party Risk / Supply-Chain Assurance  
**Enterprise Assurance Authority:** Risk / Compliance / Internal Control / Audit / Policy / Enterprise Assurance  
**Configuration Governance Authority:** Configuration Management / Asset Management / CMDB / Dependency Mapping / Technology Lifecycle Assurance  
**Principle:** MFM must ensure that critical data is owned, understood, classified, governed, sufficiently accurate, traceable, appropriately protected and usable throughout its lifecycle
