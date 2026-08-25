# MFM v1.2-Implementation-Phase-36
## Enterprise Architecture Portfolio, Capability Management, Application Portfolio & Technology Lifecycle Stabilization

**Version:** 1.2  
**Document ID:** MFM-v1.2-Implementation-Phase-36  
**Status:** Implementation Phase Baseline  
**Phase:** Enterprise Architecture Portfolio, Capability Management, Application Portfolio & Technology Lifecycle Stabilization  
**Document Type:** Implementation Execution Document  

---

# 1. Purpose

This document defines the thirty-sixth implementation phase following MFM v1.2-Implementation-Phase-35 – Vendor, Supplier, Third-Party Governance, Contract Lifecycle & Supply-Chain Assurance Stabilization.

The purpose of this phase is to establish the enterprise architecture portfolio, business capability management, application portfolio, technology portfolio and technology lifecycle baseline for MFM.

The central objective is:

> **MFM must maintain a governed view of business capabilities, applications, technologies, architecture standards, lifecycle states, dependencies, technical debt and investment priorities so that architecture decisions remain traceable, risk-aware and aligned with organizational objectives.**

---

# 2. Scope

This phase covers:

- Enterprise capability management
- Business capability mapping
- Application portfolio governance
- Technology portfolio governance
- Application ownership
- Technology ownership
- Lifecycle states
- Obsolescence management
- Technical debt portfolio
- Architecture standards
- Reference architectures
- Architecture exceptions
- Portfolio rationalization
- Investment prioritization
- Technology roadmaps
- Capability / application / technology dependency mapping
- Architecture quality gates

---

# 3. Enterprise Architecture Authority

Enterprise Architecture coordinates:

```text
Business Capabilities
Application Portfolio
Technology Portfolio
Architecture Standards
Reference Architectures
Lifecycle Management
Technical Debt
Dependencies
Architecture Exceptions
Investment Alignment
Technology Roadmaps
Portfolio Rationalization
Architecture Assurance
```

It does not replace:

```text
Business Ownership
Product Ownership
Security Authority
Privacy Authority
Financial Authority
Risk Authority
Operational Authority
```

---

# 4. Architecture Governance Principles

MFM architecture governance should be:

```text
Business-Aligned
Capability-Driven
Lifecycle-Aware
Risk-Based
Standards-Based
Traceable
Evidence-Based
Investment-Aware
Sustainable
```

---

# 5. Business Capability

A business capability describes what the organization must be able to do, independent of a specific implementation.

---

# 6. Capability Map

MFM should maintain a governed capability map.

A capability record may contain:

```text
Capability ID
Name
Description
Owner
Importance
Maturity
Strategic Relevance
Applications
Processes
Data
Technology
Risks
```

---

# 7. Capability Ownership

Each material capability should have an accountable owner.

---

# 8. Capability Hierarchy

Capabilities may be organized into:

```text
Enterprise
Domain
Sub-Domain
Capability
Sub-Capability
```

The hierarchy should remain stable enough to support portfolio analysis.

---

# 9. Capability Maturity

A baseline maturity scale may be:

```text
1 – Initial
2 – Developing
3 – Defined
4 – Managed
5 – Optimized
```

---

# 10. Capability Assessment

Capability assessment should consider:

```text
Business Value
Performance
Risk
Maturity
Cost
Strategic Importance
```

---

# 11. Capability Gap

A capability gap exists when the current capability does not sufficiently support the required objective.

---

# 12. Capability Improvement

Capability improvement may involve:

```text
Process Change
Application Change
Technology Change
People / Skills
Data
Governance
```

---

# 13. Capability Investment

Investment decisions should consider capability importance and expected business value.

---

# 14. Capability Dependency

Capabilities may depend on:

```text
Other Capabilities
Processes
Applications
Data
Technology
Suppliers
```

---

# 15. Capability Risk

Material capability risks should link to the enterprise risk register.

---

# 16. Application Portfolio

MFM should maintain an application portfolio.

---

# 17. Application Record

An application record should contain where applicable:

```text
Application ID
Name
Purpose
Owner
Business Capability
Process
Technology
Criticality
Lifecycle
Cost
Risk
Dependencies
Vendor
Status
```

---

# 18. Application Ownership

Each material application should have an accountable owner.

---

# 19. Application Classification

Applications may be classified by:

```text
Business Criticality
Strategic Importance
Technical Risk
Data Sensitivity
Lifecycle State
```

---

# 20. Application Lifecycle

A baseline lifecycle is:

```text
Proposed
Planned
Development
Pilot
Production
Maintenance
Retirement Planned
Retired
```

---

# 21. Application Lifecycle Governance

Lifecycle transitions should be controlled and recorded.

---

# 22. Application Criticality

Criticality should reflect impact on:

```text
Business
Finance
Security
Privacy
Continuity
Compliance
```

---

# 23. Application Dependency

Applications should be mapped to relevant:

```text
Applications
Services
Data
Infrastructure
Vendors
Processes
Capabilities
```

---

# 24. Application Portfolio Health

Portfolio health should consider:

```text
Lifecycle
Risk
Cost
Performance
Security
Technical Debt
Business Fit
```

---

# 25. Application Rationalization

Applications should periodically be evaluated for:

```text
Invest
Maintain
Modernize
Consolidate
Replace
Retire
```

---

# 26. Duplicate Capability

Where multiple applications provide substantially overlapping capabilities, consolidation should be considered.

---

# 27. Application Technical Debt

Application technical debt should be recorded where material.

---

# 28. Application Obsolescence

Obsolete or unsupported applications should have remediation or retirement plans.

---

# 29. Technology Portfolio

MFM should maintain a technology portfolio.

---

# 30. Technology Record

A technology record may contain:

```text
Technology ID
Name
Category
Version
Owner
Applications
Lifecycle
Support Status
Risk
Vendor
Cost
Dependencies
```

---

# 31. Technology Ownership

Material technologies should have accountable owners.

---

# 32. Technology Categories

Examples:

```text
Operating System
Database
Runtime
Framework
Library
Cloud Service
Infrastructure
Security Technology
Integration Technology
Development Tool
```

---

# 33. Technology Lifecycle

A baseline lifecycle is:

```text
Candidate
Approved
Standard
Restricted
Deprecated
Unsupported
Retired
```

---

# 34. Technology Standard

Approved technology standards should identify:

```text
Technology
Version
Approved Use
Owner
Review Date
```

---

# 35. Technology Exception

Use of non-standard technology should require an architecture exception where applicable.

---

# 36. Architecture Standards

Architecture standards should define preferred approaches for:

```text
Application
Data
Integration
Security
Infrastructure
Deployment
Observability
```

---

# 37. Reference Architecture

Reference architectures should provide reusable target patterns.

---

# 38. Reference Architecture Components

A reference architecture may define:

```text
Principles
Components
Interfaces
Patterns
Constraints
Security Requirements
Operational Requirements
```

---

# 39. Architecture Principle

Architecture principles should guide design decisions.

Examples:

```text
Reuse Before Build
Secure by Design
Data Ownership
Least Privilege
API-First where Appropriate
Observable by Design
Lifecycle Awareness
```

---

# 40. Architecture Decision Record

Material architecture decisions should be documented.

An ADR should contain:

```text
Decision
Context
Options
Rationale
Consequences
Date
Owner
Status
```

---

# 41. Architecture Decision Lifecycle

A decision may be:

```text
Proposed
Accepted
Superseded
Rejected
Retired
```

---

# 42. Architecture Exception

Exceptions to approved standards should be:

```text
Documented
Risk-Assessed
Approved
Time-Bounded where Appropriate
Reviewed
```

---

# 43. Architecture Exception Record

An exception should contain:

```text
Exception ID
Standard
Deviation
Reason
Risk
Compensating Control
Approver
Expiry / Review
Status
```

---

# 44. Architecture Review

Material architecture changes should receive appropriate architecture review.

---

# 45. Architecture Review Inputs

Review may consider:

```text
Business Fit
Security
Privacy
Data
Integration
Performance
Cost
Operational Impact
Lifecycle
Risk
```

---

# 46. Architecture Quality

Architecture quality should consider:

```text
Maintainability
Scalability
Security
Resilience
Observability
Interoperability
Cost
Lifecycle
```

---

# 47. Technical Debt

Technical debt represents known compromises or accumulated engineering obligations that may create future cost or risk.

---

# 48. Technical Debt Register

A technical debt record should contain:

```text
Debt ID
Component
Description
Cause
Impact
Risk
Cost
Priority
Owner
Treatment
Target Date
Status
```

---

# 49. Technical Debt Classification

Debt may be classified as:

```text
Architecture
Code
Data
Infrastructure
Security
Integration
Documentation
Operational
```

---

# 50. Technical Debt Priority

Priority should reflect:

```text
Risk
Business Impact
Cost
Urgency
Dependency
```

---

# 51. Technical Debt Treatment

Treatments may include:

```text
Refactor
Replace
Upgrade
Simplify
Document
Accept
Retire
```

---

# 52. Technical Debt Aging

Long-lived technical debt should receive periodic review.

---

# 53. Technology Obsolescence

Technology approaching end-of-support should be identified early.

---

# 54. End-of-Support

Where support dates are known, they should be recorded.

---

# 55. Obsolescence Risk

Obsolescence risk should consider:

```text
Security
Availability
Compatibility
Supportability
Cost
Skills
```

---

# 56. Technology Roadmap

MFM should maintain technology roadmaps where appropriate.

---

# 57. Roadmap Horizon

Roadmaps may distinguish:

```text
Current
Near-Term
Mid-Term
Target
```

---

# 58. Roadmap Dependency

Roadmap items should identify dependencies and sequencing.

---

# 59. Roadmap Assumptions

Material assumptions should be recorded.

---

# 60. Portfolio Investment

Architecture portfolio decisions should connect to investment governance.

---

# 61. Investment Criteria

Potential criteria include:

```text
Strategic Value
Business Capability
Risk Reduction
Compliance
Security
Cost
Operational Benefit
Technical Sustainability
```

---

# 62. Portfolio Prioritization

Initiatives may be prioritized according to approved organizational criteria.

---

# 63. Portfolio Balance

Portfolio decisions should consider balance between:

```text
Run
Improve
Transform
```

where applicable.

---

# 64. Application Investment

Application investment should consider:

```text
Business Fit
Lifecycle
Cost
Risk
Strategic Relevance
```

---

# 65. Technology Investment

Technology investment should consider:

```text
Supportability
Security
Scalability
Cost
Strategic Fit
```

---

# 66. Capability-to-Application Mapping

Capabilities should map to supporting applications where practical.

---

# 67. Application-to-Technology Mapping

Applications should map to supporting technologies.

---

# 68. Technology-to-Vendor Mapping

Technologies should map to vendors where applicable.

---

# 69. Capability-to-Process Mapping

Capabilities should map to relevant business processes.

---

# 70. Process-to-Application Mapping

Business processes should map to supporting applications.

---

# 71. Data-to-Application Mapping

Important data domains should map to applications responsible for processing them.

---

# 72. Dependency Graph

MFM should support a dependency view connecting:

```text
Capability
 ↓
Process
 ↓
Application
 ↓
Technology
 ↓
Vendor
```

and, where relevant:

```text
Data
Infrastructure
Security Control
```

---

# 73. Impact Analysis

Dependency mapping should support impact analysis for:

```text
Change
Failure
Retirement
Migration
Incident
Security Event
Vendor Exit
```

---

# 74. Architecture Risk

Architecture risks should connect to the enterprise risk register.

---

# 75. Architecture Compliance

Architecture implementations should be assessed against approved standards.

---

# 76. Architecture Compliance Assessment

Results may be:

```text
Compliant
Partially Compliant
Non-Compliant
Exception Approved
Not Assessed
```

---

# 77. Architecture Evidence

Evidence may include:

```text
Architecture Diagram
ADR
Review
Test Result
Exception
Implementation Record
```

---

# 78. Architecture Repository

Architecture artifacts should be stored in a controlled repository.

---

# 79. Architecture Artifact Metadata

Artifacts should identify:

```text
Owner
Version
Status
Date
Scope
Review Date
```

---

# 80. Architecture Artifact Lifecycle

Artifacts may progress through:

```text
Draft
Review
Approved
Published
Superseded
Archived
```

---

# 81. Architecture Knowledge

Architecture knowledge should be reusable across projects and changes.

---

# 82. Architecture Change Management

Material architecture changes should be linked to change-management records.

---

# 83. Architecture and Security

Architecture reviews should consider:

```text
Identity
Access
Encryption
Network
Logging
Threats
```

where applicable.

---

# 84. Architecture and Privacy

Architecture reviews should consider:

```text
Data Flows
Purpose
Minimization
Retention
Access
```

where personal information is involved.

---

# 85. Architecture and Finance

Architecture decisions should consider:

```text
Capital Cost
Operating Cost
Lifecycle Cost
Financial Risk
```

where relevant.

---

# 86. Architecture and Operations

Architecture should support:

```text
Monitoring
Support
Backup
Recovery
Deployment
Incident Response
```

---

# 87. Architecture and Continuity

Critical architecture should support defined continuity and recovery requirements.

---

# 88. Architecture and Compliance

Architecture should incorporate applicable compliance requirements.

---

# 89. Portfolio Reporting

Management reporting may include:

```text
Application Health
Technology Health
Technical Debt
Obsolescence
Architecture Exceptions
Capability Gaps
Investment
Roadmap
```

---

# 90. Portfolio Dashboard

The portfolio dashboard should provide management visibility of architecture health and change.

---

# 91. Portfolio Metrics

Metrics may include:

```text
Applications by Lifecycle
Unsupported Technologies
Technical Debt Aging
Architecture Exceptions
Capability Coverage
Portfolio Cost
Retirement Progress
Modernization Progress
```

---

# 92. Application Review Calendar

Application reviews should be scheduled according to criticality and risk.

---

# 93. Technology Review Calendar

Technology standards and lifecycle states should be reviewed periodically.

---

# 94. Architecture Governance Review

Periodic governance should assess:

```text
Capability Map
Application Portfolio
Technology Portfolio
Standards
Exceptions
Technical Debt
Roadmaps
Dependencies
```

---

# 95. Portfolio Governance Register

The register should identify:

```text
Portfolio Item
Owner
Lifecycle
Risk
Decision
Review
Status
```

---

# 96. Architecture Exception Register

Material exceptions should contain:

```text
Exception
Standard
Risk
Owner
Approver
Compensating Control
Expiry / Review
Status
```

---

# 97. Technical Debt Register

Material technical debt should contain:

```text
Debt
Component
Risk
Impact
Owner
Treatment
Priority
Target
Status
```

---

# 98. Technology Lifecycle Register

The register should identify:

```text
Technology
Version
Lifecycle
Support
Owner
Applications
Risk
Target Action
```

---

# 99. Capability Register

The capability register should identify:

```text
Capability
Owner
Maturity
Strategic Relevance
Applications
Processes
Risk
Improvement
```

---

# 100. Portfolio Maturity

Architecture portfolio maturity should be reviewed periodically.

---

# 101. Portfolio Maturity Dimensions

Assess:

```text
Capability Management
Application Management
Technology Management
Standards
Dependencies
Technical Debt
Roadmaps
Investment
Assurance
```

---

# 102. Portfolio Maturity Levels

A baseline model is:

```text
1 – Initial
2 – Repeatable
3 – Defined
4 – Managed
5 – Optimized
```

---

# 103. Enterprise Architecture Quality Gate

Architecture governance passes when:

```text
Capability Map               ✓
Capability Ownership         ✓
Application Portfolio        ✓
Application Ownership        ✓
Technology Portfolio         ✓
Technology Ownership         ✓
Lifecycle States             ✓
Obsolescence                 ✓
Technical Debt               ✓
Architecture Standards       ✓
Reference Architectures      ✓
Architecture Decisions       ✓
Architecture Exceptions      ✓
Dependency Mapping            ✓
Portfolio Rationalization    ✓
Investment Alignment         ✓
Technology Roadmaps          ✓
Architecture Assurance       ✓
```

---

# 104. Capability Gate

Capability management passes when:

- Material capabilities are identified.
- Owners are assigned.
- Maturity is assessed.
- Gaps are visible.
- Supporting applications and processes are mapped.
- Risks are linked.

---

# 105. Application Portfolio Gate

Application portfolio governance passes when:

```text
Application
 ↓
Owner
 ↓
Capability
 ↓
Process
 ↓
Technology
 ↓
Lifecycle
 ↓
Risk
```

can be traced for material applications.

---

# 106. Technology Lifecycle Gate

Technology governance passes when:

- Technology owners exist.
- Lifecycle states are defined.
- Support status is known.
- Obsolescence risk is assessed.
- Exceptions are governed.
- Roadmaps exist where required.

---

# 107. Technical Debt Gate

Technical debt governance passes when:

- Material debt is recorded.
- Risk and impact are assessed.
- Owners exist.
- Priorities are established.
- Treatment is tracked.

---

# 108. Architecture Decision Gate

Architecture decision governance passes when:

- Material decisions are documented.
- Alternatives are considered where appropriate.
- Rationale is recorded.
- Consequences are understood.
- Decision status is controlled.

---

# 109. Portfolio Rationalization Gate

Rationalization passes when portfolio items can be evaluated against:

```text
Business Value
Cost
Risk
Lifecycle
Strategic Fit
```

and a governed decision is recorded.

---

# 110. Dependency Gate

Dependency governance passes when critical relationships between:

```text
Capabilities
Processes
Applications
Data
Technology
Vendors
Infrastructure
```

can be identified where required.

---

# 111. Roadmap Gate

Technology roadmaps pass when:

```text
Current State
Target State
Transition
Dependencies
Assumptions
Timing
Ownership
```

are sufficiently defined.

---

# 112. Definition of Ready

An architecture portfolio work item is Ready when:

- Business objective is identified.
- Capability impact is known.
- Application / technology impact is understood.
- Ownership is assigned.
- Risk is assessed.
- Standards are identified.
- Dependencies are known.
- Decision criteria are defined.

---

# 113. Definition of Done

An architecture portfolio work item is Done when:

```text
Objective Defined
        ↓
Capability Impact Assessed
        ↓
Application / Technology Impact Assessed
        ↓
Standards Evaluated
        ↓
Dependencies Mapped
        ↓
Risk Assessed
        ↓
Architecture Decision Completed
        ↓
Portfolio Updated
        ↓
Lifecycle / Roadmap Updated
        ↓
Evidence Available
        ↓
Architecture Governance Gate Passed
```

---

# 114. Final Capability Principle

> **Architecture must begin with what the organization needs to be capable of doing, not with a specific technology product.**

---

# 115. Final Portfolio Principle

> **Every material application and technology should have an owner, a known purpose, a lifecycle state and a current risk profile.**

---

# 116. Final Lifecycle Principle

> **Technology and applications must be actively governed throughout their lifecycle rather than only at implementation.**

---

# 117. Final Obsolescence Principle

> **End-of-support and obsolete technologies must be identified early enough to permit controlled remediation, migration or retirement.**

---

# 118. Final Technical-Debt Principle

> **Technical debt must be visible as a managed portfolio of risk and future work rather than hidden inside implementation decisions.**

---

# 119. Final Standards Principle

> **Architecture standards should provide repeatable patterns while allowing controlled, evidence-based exceptions where justified.**

---

# 120. Final Decision Principle

> **Material architecture decisions must preserve context, alternatives, rationale and consequences so that future decisions remain understandable.**

---

# 121. Final Dependency Principle

> **Critical dependencies between capabilities, processes, applications, data, technologies and suppliers must be visible enough to support impact analysis.**

---

# 122. Final Investment Principle

> **Architecture investment should prioritize business value, risk reduction, strategic relevance and sustainable lifecycle economics.**

---

# 123. Final Roadmap Principle

> **Technology roadmaps must describe a governed transition from the current state toward an approved target state, including dependencies and assumptions.**

---

# 124. Final Implementation Principle

> **MFM should manage enterprise architecture as an integrated portfolio of capabilities, applications, technologies, dependencies, standards, technical debt and investment decisions aligned with organizational objectives.**

---

# 125. Summary

MFM v1.2-Implementation-Phase-36 establishes the Enterprise Architecture Portfolio, Capability Management, Application Portfolio and Technology Lifecycle Stabilization baseline.

It defines:

- Enterprise Architecture Authority
- Architecture Governance Principles
- Business Capability Management
- Capability Map / Ownership / Hierarchy
- Capability Maturity / Assessment / Gaps / Improvement
- Capability Investment / Dependencies / Risk
- Application Portfolio
- Application Records / Ownership / Classification
- Application Lifecycle
- Application Criticality / Dependencies / Portfolio Health
- Application Rationalization
- Application Technical Debt / Obsolescence
- Technology Portfolio
- Technology Records / Ownership / Categories
- Technology Lifecycle / Standards / Exceptions
- Architecture Standards
- Reference Architectures
- Architecture Principles
- Architecture Decision Records
- Architecture Decision Lifecycle
- Architecture Exceptions
- Architecture Review / Quality
- Technical Debt Register / Classification / Priority / Treatment / Aging
- Technology Obsolescence / End-of-Support / Risk
- Technology Roadmaps
- Portfolio Investment / Prioritization / Balance
- Capability / Application / Technology / Vendor / Process / Data Mapping
- Dependency Graph / Impact Analysis
- Architecture Risk / Compliance / Evidence / Repository
- Architecture Change Management
- Security / Privacy / Finance / Operations / Continuity / Compliance Architecture Integration
- Portfolio Reporting / Dashboards / Metrics
- Application / Technology Review Calendars
- Portfolio / Exception / Technical Debt / Technology Lifecycle / Capability Registers
- Portfolio Maturity
- Enterprise Architecture / Capability / Application / Technology Lifecycle / Technical Debt / Decision / Rationalization / Dependency / Roadmap Quality Gates
- Definition of Ready
- Definition of Done

---

# 126. Next Implementation Phase

The next document shall be:

**MFM v1.2-Implementation-Phase-37 – Enterprise Service Management, IT Operations, Service Catalog, SLA & Operational Performance Stabilization**

It shall establish the controlled implementation and validation of:

- Enterprise service management
- Service portfolio
- Service catalog
- Service ownership
- Service lifecycle
- Service-level management
- Operational performance
- Incident / request / problem integration
- Availability management
- Capacity management
- Service continuity
- Operational knowledge
- Service reporting
- Service quality gates

---

# 127. Document Control

**Document:** MFM v1.2-Implementation-Phase-36  
**Version:** 1.2  
**Status:** Implementation Phase Baseline  
**Previous Document:** MFM v1.2-Implementation-Phase-35  
**Next Document:** MFM v1.2-Implementation-Phase-37  
**Primary Transition:** Vendor / Supplier / Third-Party Governance / Contract Lifecycle / Supply-Chain Assurance → Enterprise Architecture Portfolio / Capability Management / Application Portfolio / Technology Lifecycle  
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
**Principle:** MFM must maintain a governed architectural portfolio connecting business capabilities to applications, data, technologies, vendors, lifecycle states, technical debt, risks, standards and investment decisions
