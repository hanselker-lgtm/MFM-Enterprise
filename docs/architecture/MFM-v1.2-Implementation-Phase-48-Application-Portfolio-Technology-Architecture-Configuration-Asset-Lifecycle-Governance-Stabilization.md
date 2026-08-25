# MFM v1.2-Implementation-Phase-48
## Application Portfolio, Technology Architecture, Configuration, Asset & Lifecycle Governance Stabilization

**Version:** 1.2  
**Document ID:** MFM-v1.2-Implementation-Phase-48  
**Status:** Implementation Phase Baseline  
**Phase:** Application Portfolio, Technology Architecture, Configuration, Asset & Lifecycle Governance Stabilization  
**Document Type:** Implementation Execution Document  

---

# 1. Purpose

This document defines the forty-eighth implementation phase following MFM v1.2-Implementation-Phase-47 – Data Governance, Data Quality, Information Lifecycle, Master Data & Data Protection Stabilization.

The purpose of this phase is to establish a controlled governance capability for applications, technology platforms, configuration items, assets, dependencies and technology lifecycles.

The central objective is:

> **MFM must maintain a reliable, governed and decision-ready view of its application and technology estate, including ownership, configuration, dependencies, lifecycle, technical debt, obsolescence and strategic fit.**

---

# 2. Scope

This phase covers:

- Application Portfolio Management
- Technology Portfolio Management
- Architecture Governance
- Configuration Management
- Asset Management
- CMDB Governance
- Dependency Mapping
- Application Lifecycle
- Technology Lifecycle
- Obsolescence Management
- Technical Debt
- Configuration Quality
- Asset Ownership
- Technology Governance Quality Gates

---

# 3. Portfolio Governance Authority

Portfolio Governance coordinates:

```text
Applications
Technology
Architecture
Configuration
Assets
Dependencies
Lifecycle
Obsolescence
Technical Debt
Portfolio Decisions
```

It does not replace:

```text
Service Ownership
Security Authority
Data Governance
Financial Management
Vendor Management
Project Governance
Change Management
Operations
```

---

# 4. Portfolio Governance Principles

Portfolio governance should be:

```text
Business-Aligned
Lifecycle-Aware
Evidence-Based
Owner-Driven
Dependency-Aware
Risk-Based
Financially Transparent
Strategically Coherent
Continuously Reviewed
```

---

# 5. Application

An application is a software capability supporting one or more business, service or operational functions.

---

# 6. Application Ownership

Each material application should have an accountable business or service owner and an appropriate technical owner.

---

# 7. Application Portfolio

The application portfolio should provide visibility into:

```text
Application
Purpose
Owner
Users
Services
Technology
Cost
Risk
Lifecycle
Status
```

---

# 8. Application Classification

Applications may be classified according to:

```text
Business Criticality
Service Criticality
Risk
Data Sensitivity
Strategic Importance
Lifecycle
```

---

# 9. Application Criticality

Criticality should reflect the consequences of application failure or unavailability.

---

# 10. Application Business Value

Applications should be assessed for:

```text
Business Value
User Value
Operational Value
Strategic Value
```

---

# 11. Application Health

Application health may consider:

```text
Availability
Performance
Security
Maintainability
Supportability
Data Quality
User Experience
```

---

# 12. Application Lifecycle

The baseline lifecycle is:

```text
Idea
 ↓
Evaluate
 ↓
Acquire / Build
 ↓
Implement
 ↓
Operate
 ↓
Maintain
 ↓
Modernize
 ↓
Retire
```

---

# 13. Application Lifecycle Ownership

Each material lifecycle stage should have an accountable owner.

---

# 14. Application Introduction

New applications should be assessed for:

```text
Business Need
Architecture
Security
Data
Cost
Support
Continuity
Integration
```

---

# 15. Application Rationalization

Applications should periodically be evaluated for:

```text
Retain
Invest
Modernize
Consolidate
Replace
Retire
```

---

# 16. Application Duplication

Duplicate or overlapping capabilities should be identified.

---

# 17. Application Consolidation

Consolidation opportunities should consider:

```text
Cost
Risk
Complexity
User Impact
Migration
Strategic Fit
```

---

# 18. Application Retirement

Retirement should address:

```text
Users
Data
Integrations
Contracts
Licenses
Infrastructure
Access
Documentation
```

---

# 19. Retirement Verification

Retirement should verify that:

```text
Access Removed
Data Handled
Dependencies Removed
Licenses Closed
Infrastructure Released
Records Retained
```

where applicable.

---

# 20. Technology Portfolio

The technology portfolio should provide visibility into:

```text
Platform
Technology
Version
Owner
Usage
Criticality
Lifecycle
Cost
Risk
```

---

# 21. Technology Classification

Technology may be classified by:

```text
Platform
Infrastructure
Database
Network
Security
Integration
Cloud
Endpoint
```

---

# 22. Technology Standards

Approved technology standards should define preferred technologies and versions.

---

# 23. Technology Exception

Technology outside approved standards should be:

```text
Identified
Risk-Assessed
Approved
Tracked
Reviewed
```

---

# 24. Architecture Governance

Architecture governance should assess:

```text
Strategic Fit
Standards
Dependencies
Security
Data
Integration
Lifecycle
Cost
```

---

# 25. Architecture Decision

Material technology decisions should have documented rationale where appropriate.

---

# 26. Architecture Decision Record

An ADR may contain:

```text
Context
Decision
Options
Rationale
Consequences
Owner
Date
Status
```

---

# 27. Configuration Management

Configuration Management maintains controlled information about configuration items and their relationships.

---

# 28. Configuration Item

A Configuration Item (CI) may include:

```text
Application
Server
Database
Network Device
Cloud Resource
Integration
Service
```

---

# 29. CI Ownership

Material CIs should have accountable ownership.

---

# 30. CI Attributes

A CI record may include:

```text
Identifier
Type
Owner
Status
Version
Location
Environment
Dependencies
Lifecycle
```

---

# 31. CMDB

The CMDB should provide a controlled repository of configuration information and relationships where applicable.

---

# 32. CMDB Scope

CMDB scope should prioritize:

```text
Critical Services
Critical Applications
Material Infrastructure
Important Dependencies
```

---

# 33. Configuration Relationships

Relationships may include:

```text
Depends On
Runs On
Connects To
Supports
Hosted By
Uses
```

---

# 34. Dependency Mapping

Dependency maps should connect:

```text
Business Service
 ↓
Application
 ↓
Technology
 ↓
Infrastructure
 ↓
Supplier
```

where relevant.

---

# 35. Dependency Accuracy

Material dependencies should be periodically validated.

---

# 36. Configuration Baseline

Approved configuration states should be identifiable.

---

# 37. Configuration Drift

Drift from approved configuration should be detected and assessed.

---

# 38. Configuration Change

Material CI changes should integrate with change governance.

---

# 39. Configuration History

Material configuration history should be retained sufficiently to support:

```text
Investigation
Audit
Recovery
Change Analysis
```

---

# 40. Asset Management

Asset Management governs physical and logical technology assets through their lifecycle.

---

# 41. Asset Types

Assets may include:

```text
Hardware
Software
Licenses
Cloud Resources
Devices
Infrastructure
```

---

# 42. Asset Ownership

Material assets should have identifiable ownership.

---

# 43. Asset Acquisition

Acquisition should connect:

```text
Requirement
Approval
Procurement
Receipt
Registration
```

---

# 44. Asset Registration

Assets should be registered with sufficient identifiers and ownership.

---

# 45. Asset Location

Where relevant, asset location should be maintained.

---

# 46. Asset Status

Asset status may include:

```text
Planned
Ordered
Active
In Maintenance
Retired
Disposed
```

---

# 47. Asset Lifecycle

The asset lifecycle is:

```text
Plan
 ↓
Acquire
 ↓
Receive
 ↓
Deploy
 ↓
Operate
 ↓
Maintain
 ↓
Retire
 ↓
Dispose
```

---

# 48. Asset Disposal

Disposal should consider:

```text
Data
Security
Environmental
Financial
Records
```

requirements.

---

# 49. Software Licensing

Software licenses should be tracked against:

```text
Entitlement
Usage
Contract
Cost
Expiry
```

where applicable.

---

# 50. License Compliance

License compliance should be monitored for material software.

---

# 51. License Optimization

Optimization should identify:

```text
Unused
Underused
Duplicate
Over-Licensed
```

licenses where relevant.

---

# 52. Technology Lifecycle

Technology lifecycle management should identify:

```text
Current
Preferred
Aging
End-of-Support
End-of-Life
Retired
```

states.

---

# 53. End-of-Support

End-of-support technologies should be identified before support termination.

---

# 54. End-of-Life

End-of-life technologies should have approved remediation or retirement plans.

---

# 55. Obsolescence

Obsolescence risk may arise from:

```text
Unsupported Version
Vendor Exit
Security Weakness
Skills Scarcity
Integration Constraint
Performance Limitation
```

---

# 56. Obsolescence Register

The register should identify:

```text
Technology
Version
Owner
Risk
End Date
Action
Status
```

---

# 57. Technical Debt

Technical debt represents accumulated cost or risk resulting from technology or design decisions that require future remediation.

---

# 58. Technical Debt Categories

Categories may include:

```text
Architecture
Code
Infrastructure
Security
Data
Integration
Documentation
```

---

# 59. Technical Debt Assessment

Technical debt should consider:

```text
Impact
Risk
Cost
Urgency
Dependencies
```

---

# 60. Technical Debt Register

The register should identify:

```text
Debt
Asset / Application
Impact
Risk
Owner
Remediation
Due Date
Status
```

---

# 61. Technical Debt Prioritization

Prioritization should consider:

```text
Business Impact
Security
Operational Risk
Cost
Lifecycle
Strategic Fit
```

---

# 62. Portfolio Cost

Portfolio economics should connect:

```text
Application
Technology
Service
Vendor
License
Infrastructure
```

costs.

---

# 63. Portfolio Risk

Portfolio risk should consider:

```text
Criticality
Obsolescence
Security
Dependency
Vendor
Continuity
```

---

# 64. Portfolio Strategic Fit

Technology should be assessed against approved strategic direction.

---

# 65. Portfolio Review

Material portfolios should be reviewed periodically.

---

# 66. Portfolio Decision

Portfolio decisions may include:

```text
Invest
Maintain
Modernize
Consolidate
Migrate
Replace
Retire
```

---

# 67. Portfolio Decision Evidence

Material decisions should be supported by:

```text
Value
Cost
Risk
Lifecycle
Architecture
Dependencies
```

---

# 68. Application Modernization

Modernization should assess:

```text
Business Need
Architecture
Technology
Data
Integration
Security
Cost
```

---

# 69. Migration Planning

Migration should consider:

```text
Dependencies
Data
Users
Testing
Continuity
Rollback
```

---

# 70. Migration Readiness

Migration should not proceed until required dependencies and recovery measures are sufficiently prepared.

---

# 71. Technology Standardization

Standardization should reduce:

```text
Complexity
Cost
Risk
Skill Fragmentation
```

where appropriate.

---

# 72. Technology Exceptions

Exceptions should have:

```text
Owner
Reason
Risk
Approval
Expiry / Review
```

---

# 73. Configuration Data Quality

CMDB and asset information should be assessed for:

```text
Completeness
Accuracy
Currency
Consistency
Relationship Integrity
```

---

# 74. Configuration Reconciliation

Configuration information should be reconciled against authoritative sources where possible.

---

# 75. Discovery

Automated discovery may be used to identify technology assets and configuration information.

---

# 76. Discovery Validation

Discovered information should be validated before becoming authoritative where required.

---

# 77. Configuration Compliance

Material configuration items should be assessed against approved baselines.

---

# 78. Service Mapping

Service maps should connect technical dependencies to business services.

---

# 79. Impact Analysis

Dependency information should support:

```text
Incident
Change
Problem
Continuity
Risk
Architecture
```

analysis.

---

# 80. Change Impact

Before material changes, affected dependencies should be assessed.

---

# 81. Incident Impact

Incident analysis should use configuration and dependency information where available.

---

# 82. Problem Analysis

Recurring failures should consider underlying configuration and architecture dependencies.

---

# 83. Continuity Integration

Recovery plans should use accurate dependency information.

---

# 84. Security Integration

Security controls should consider:

```text
Asset
Configuration
Identity
Dependency
Exposure
```

---

# 85. Data Governance Integration

Application and technology metadata should identify relevant data dependencies.

---

# 86. Vendor Integration

Material vendor dependencies should be represented in relevant portfolio and configuration records.

---

# 87. Financial Integration

Portfolio records should connect to relevant:

```text
Budget
Actual
Forecast
Contract
License
Service Cost
```

data.

---

# 88. Portfolio Dashboards

An application portfolio dashboard may show:

```text
Applications
Criticality
Lifecycle
Cost
Risk
Strategic Fit
Technical Debt
```

---

# 89. Technology Dashboard

A technology dashboard may show:

```text
Platforms
Versions
Lifecycle
Obsolescence
Standards
Exceptions
Risk
```

---

# 90. Configuration Dashboard

A CMDB dashboard may show:

```text
CIs
Ownership
Completeness
Accuracy
Relationships
Drift
```

---

# 91. Asset Dashboard

An asset dashboard may show:

```text
Assets
Lifecycle
Location
Ownership
Warranty
Licenses
Retirement
```

---

# 92. Portfolio Metrics

Metrics may include:

```text
Application Count
Technology Count
Lifecycle Coverage
Obsolescence Exposure
Technical Debt
CMDB Accuracy
Asset Ownership
License Utilization
```

---

# 93. Portfolio KPIs

KPIs should measure portfolio outcomes rather than inventory volume alone.

---

# 94. Portfolio Risk Indicators

Indicators may include:

```text
Unsupported Technology
Critical Dependencies
High Technical Debt
Unowned Assets
Configuration Drift
License Risk
```

---

# 95. Portfolio Review

Portfolio reviews should assess:

```text
Value
Cost
Risk
Lifecycle
Architecture
Dependencies
```

---

# 96. Application Review

Application owners should periodically review:

```text
Business Value
Health
Users
Cost
Risk
Lifecycle
```

---

# 97. Technology Review

Technology owners should review:

```text
Version
Support
Security
Cost
Usage
Strategic Fit
```

---

# 98. Configuration Review

Configuration owners should review:

```text
Ownership
Accuracy
Relationships
Drift
Lifecycle
```

---

# 99. Asset Review

Asset owners should review:

```text
Ownership
Location
Status
Lifecycle
Cost
Security
```

---

# 100. Portfolio Improvement

Improvement should address:

```text
Duplication
Obsolescence
Technical Debt
Cost
Risk
Complexity
```

---

# 101. Application Portfolio Register

The register should identify:

```text
Application
Owner
Purpose
Criticality
Cost
Risk
Lifecycle
Strategic Fit
Status
```

---

# 102. Technology Portfolio Register

The register should identify:

```text
Technology
Version
Owner
Standard
Lifecycle
Cost
Risk
Status
```

---

# 103. Configuration Register

The register should identify:

```text
CI
Type
Owner
Version
Environment
Dependencies
Lifecycle
Status
```

---

# 104. Asset Register

The register should identify:

```text
Asset
Type
Owner
Location
Status
Cost
Lifecycle
Security
```

---

# 105. Dependency Register

The register should identify:

```text
Source
Dependency
Target
Relationship
Criticality
Owner
Status
```

---

# 106. Technology Exception Register

The register should identify:

```text
Exception
Technology
Reason
Risk
Approval
Expiry
Status
```

---

# 107. Obsolescence Register

The register should identify:

```text
Technology
Version
End Date
Risk
Owner
Action
Status
```

---

# 108. Technical Debt Register

The register should identify:

```text
Debt
Application / Technology
Risk
Impact
Owner
Remediation
Due Date
Status
```

---

# 109. Configuration Quality Register

The register should identify:

```text
CI
Quality Dimension
Expected
Actual
Variance
Owner
Action
Status
```

---

# 110. Portfolio Maturity

Application and technology governance maturity should be reviewed periodically.

---

# 111. Portfolio Maturity Dimensions

Assess:

```text
Application Portfolio
Technology Portfolio
Architecture
Configuration
Assets
Dependencies
Lifecycle
Obsolescence
Technical Debt
Financial Visibility
```

---

# 112. Portfolio Maturity Levels

A baseline model is:

```text
1 – Initial
2 – Repeatable
3 – Defined
4 – Managed
5 – Optimized
```

---

# 113. Portfolio Governance Quality Gate

Governance passes when:

```text
Application Ownership         ✓
Technology Ownership          ✓
Portfolio Visibility          ✓
Architecture Governance      ✓
Configuration Governance     ✓
Asset Governance             ✓
Dependency Mapping            ✓
Lifecycle Management          ✓
Obsolescence Management      ✓
Technical Debt                ✓
Financial Visibility          ✓
Risk Visibility               ✓
Evidence                      ✓
```

---

# 114. Application Portfolio Gate

Application portfolio governance passes when:

- Applications have owners.
- Business purpose is known.
- Criticality is assessed.
- Lifecycle is known.
- Cost and risk are visible.
- Rationalization is periodically performed.

---

# 115. Configuration Quality Gate

Configuration governance passes when:

```text
CI
 ↓
Owner
 ↓
Attributes
 ↓
Relationships
 ↓
Lifecycle
 ↓
Validation
 ↓
Quality
```

is controlled.

---

# 116. Asset Lifecycle Gate

Asset governance passes when:

```text
Acquire
 ↓
Register
 ↓
Deploy
 ↓
Operate
 ↓
Maintain
 ↓
Retire
 ↓
Dispose
```

is traceable.

---

# 117. Obsolescence Gate

Obsolescence governance passes when:

- End-of-support dates are known.
- Risks are assessed.
- Remediation is planned.
- Exceptions are governed.
- Retirement or modernization is tracked.

---

# 118. Technical Debt Gate

Technical debt governance passes when:

- Debt is identified.
- Impact and risk are assessed.
- Ownership exists.
- Remediation is prioritized.
- Progress is measured.

---

# 119. Definition of Ready

A portfolio work item is Ready when:

- Application, technology or asset is identified.
- Owner is assigned.
- Business purpose is known.
- Lifecycle status is known.
- Dependencies are identified.
- Cost and risk considerations are available.

---

# 120. Definition of Done

A portfolio work item is Done when:

```text
Asset / Application Identified
        ↓
Owner Assigned
        ↓
Classification Completed
        ↓
Dependencies Mapped
        ↓
Lifecycle Established
        ↓
Risk / Cost Assessed
        ↓
Governance Evidence Available
        ↓
Portfolio Governance Gate Passed
```

---

# 121. Final Portfolio Principle

> **MFM must maintain a decision-ready view of the application and technology estate, not merely an inventory.**

---

# 122. Final Ownership Principle

> **Every material application, technology platform, configuration item and asset must have clear accountability.**

---

# 123. Final Lifecycle Principle

> **Technology must be actively governed from introduction through operation, modernization and retirement.**

---

# 124. Final Configuration Principle

> **Configuration information is valuable only when it is sufficiently accurate, current and connected through meaningful relationships.**

---

# 125. Final Dependency Principle

> **Dependency visibility is essential for safe change, incident analysis, continuity, security and architecture decisions.**

---

# 126. Final Obsolescence Principle

> **End-of-support and end-of-life exposure must be identified early enough to allow controlled remediation or retirement.**

---

# 127. Final Technical Debt Principle

> **Technical debt must be treated as a managed risk and investment decision rather than an invisible engineering backlog.**

---

# 128. Final Financial Principle

> **Portfolio decisions must consider total lifecycle cost, service value, risk and strategic fit.**

---

# 129. Final Integration Principle

> **Application, technology, configuration and asset governance must integrate with service management, security, data, finance, vendors, projects, change, continuity and enterprise architecture.**

---

# 130. Final Implementation Principle

> **MFM should operate an evidence-based technology portfolio capability that connects applications, architecture, configuration, assets, dependencies, lifecycle, cost, risk and strategic direction into one governed decision model.**

---

# 131. Summary

MFM v1.2-Implementation-Phase-48 establishes the Application Portfolio, Technology Architecture, Configuration, Asset and Lifecycle Governance Stabilization baseline.

It defines:

- Portfolio Governance Authority
- Application Portfolio Management
- Application Ownership / Criticality / Business Value / Health
- Application Lifecycle
- Application Introduction / Rationalization / Duplication / Consolidation / Retirement
- Retirement Verification
- Technology Portfolio Management
- Technology Classification / Standards / Exceptions
- Architecture Governance
- Architecture Decisions / ADRs
- Configuration Management
- Configuration Items / Ownership / Attributes
- CMDB Governance
- Configuration Relationships
- Dependency Mapping / Validation
- Configuration Baselines / Drift / History
- Asset Management
- Asset Types / Ownership / Acquisition / Registration / Location / Status
- Asset Lifecycle / Disposal
- Software Licensing / Compliance / Optimization
- Technology Lifecycle
- End-of-Support / End-of-Life / Obsolescence
- Obsolescence Register
- Technical Debt / Categories / Assessment / Prioritization
- Portfolio Cost / Risk / Strategic Fit
- Portfolio Review / Decisions / Evidence
- Application Modernization / Migration Planning / Readiness
- Technology Standardization / Exceptions
- Configuration Data Quality / Reconciliation / Discovery
- Configuration Compliance
- Service Mapping
- Impact Analysis
- Change / Incident / Problem / Continuity Integration
- Security / Data / Vendor / Financial Integration
- Portfolio / Technology / Configuration / Asset Dashboards
- Portfolio Metrics / KPIs / Risk Indicators
- Application / Technology / Configuration / Asset Reviews
- Portfolio Improvement
- Application / Technology / Configuration / Asset / Dependency / Exception / Obsolescence / Technical Debt / Configuration Quality Registers
- Portfolio Maturity
- Portfolio Governance / Application / Configuration / Asset / Obsolescence / Technical Debt Quality Gates
- Definition of Ready
- Definition of Done

---

# 132. Next Implementation Phase

The next document shall be:

**MFM v1.2-Implementation-Phase-49 – Enterprise Integration, API Management, Workflow Orchestration & Interoperability Stabilization**

It shall establish the controlled implementation and validation of:

- Enterprise integration
- API governance
- Interface management
- Workflow orchestration
- Event-driven integration
- Integration security
- Data exchange
- Integration monitoring
- API lifecycle
- Integration testing
- Failure handling
- Interoperability governance
- Integration quality gates

---

# 133. Document Control

**Document:** MFM v1.2-Implementation-Phase-48  
**Version:** 1.2  
**Status:** Implementation Phase Baseline  
**Previous Document:** MFM v1.2-Implementation-Phase-47  
**Next Document:** MFM v1.2-Implementation-Phase-49  
**Primary Transition:** Data Governance / Data Quality / Information Lifecycle / Master Data / Data Protection → Application Portfolio / Technology Architecture / Configuration / Asset / Lifecycle Governance  
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
**Principle:** MFM must maintain a governed, accurate and decision-ready view of applications, technology, configuration items, assets and dependencies throughout their lifecycle, integrating cost, risk, architecture, security, service and strategic considerations
