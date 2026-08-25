# MFM v1.2-Steady-State-30
## Enterprise Application Management, Software Lifecycle, Development, Testing, DevSecOps, Release Engineering & Application Governance

**Version:** 1.2  
**Document ID:** MFM-v1.2-Steady-State-30  
**Status:** Steady-State Enterprise Application & Software Engineering Baseline  
**Lifecycle:** Post-Implementation / Steady-State Operation  
**Document Type:** Application Management / Software Lifecycle / Development / Testing / DevSecOps / Release Engineering / Application Governance Document  

---

# 1. Purpose

This document establishes the thirtieth document in the MFM v1.2 Steady-State series.

It follows MFM v1.2-Steady-State-29 – Enterprise Service Management, IT Service Operations, Service Desk, Incident, Problem, Change & Configuration Management.

The purpose of this document is to establish the permanent enterprise operating model for application governance, software development, application lifecycle management, software architecture, engineering standards, testing, quality assurance, DevSecOps, source-code management, build management, release engineering, deployment, application security, technical debt, application support and application retirement.

The central objective is:

> **MFM applications must be designed, developed, tested, secured, released, operated, maintained and retired through controlled, traceable and continuously improving lifecycle processes.**

---

# 2. Scope

This document covers:

- Application Governance
- Application Portfolio Management
- Application Ownership
- Application Lifecycle Management
- Software Development Lifecycle
- Software Engineering Governance
- Development Standards
- Coding Standards
- Architecture Alignment
- Solution Design
- Source Code Management
- Repository Governance
- Branching Strategy
- Code Review
- Build Management
- Build Automation
- Continuous Integration
- Continuous Delivery
- DevSecOps
- Application Security
- Secure Coding
- Dependency Management
- Vulnerability Management
- Software Composition
- Secrets Management
- Environment Management
- Development Environments
- Test Environments
- Production Environments
- Test Strategy
- Test Planning
- Unit Testing
- Integration Testing
- System Testing
- Regression Testing
- Performance Testing
- Security Testing
- User Acceptance Testing
- Test Evidence
- Defect Management
- Quality Gates
- Release Engineering
- Release Planning
- Deployment
- Rollback
- Application Configuration
- Application Data
- Database Change
- API Governance
- Integration Management
- Application Monitoring
- Application Observability
- Application Support
- Technical Debt
- Application Risk
- Application Resilience
- Application Continuity
- Application Documentation
- Knowledge Transfer
- Software Licensing
- Open Source Governance
- Application Vendor Management
- Application Findings
- Application Exceptions
- Application Remediation
- Application Metrics
- Application Dashboards
- Application Assurance
- Application Maturity
- Application Retirement
- Continual Application Improvement

---

# 3. Application Governance Objective

The primary objective is:

> **Ensure that applications remain aligned with business requirements, architecture, security, operational needs, risk and lifecycle expectations throughout their existence.**

---

# 4. Software Engineering Objective

The primary software engineering objective is:

> **Develop and maintain reliable, secure, maintainable and supportable software through disciplined engineering practices.**

---

# 5. Application Lifecycle

The application lifecycle should integrate:

```text
Plan
 ↓
Design
 ↓
Develop
 ↓
Build
 ↓
Test
 ↓
Secure
 ↓
Release
 ↓
Deploy
 ↓
Operate
 ↓
Maintain
 ↓
Improve
 ↓
Retire
```

---

# 6. Application Governance Principles

Application Management should be:

```text
Business-Aligned
Architecture-Aligned
Secure
Tested
Traceable
Maintainable
Observable
Recoverable
Supportable
Continuously Improved
```

---

# 7. Software Engineering Principles

Software Engineering should be:

```text
Controlled
Automated Where Appropriate
Peer-Reviewed
Testable
Secure by Design
Version-Controlled
Reproducible
Evidence-Based
Maintainable
```

---

# 8. Application Ownership

Every material application should have an accountable Application Owner.

---

# 9. Application Owner Responsibilities

Application Owners should be accountable for:

```text
Purpose
Business Value
Lifecycle
Risk
Security
Performance
Support
Dependencies
Continuity
Technical Debt
Retirement
```

---

# 10. Application Portfolio

The Application Portfolio should provide an authoritative view of material applications.

---

# 11. Application Record

An application record may include:

```text
Application ID
Name
Purpose
Owner
Business Capability
Criticality
Environment
Technology
Dependencies
Data Classification
Supplier
Lifecycle Status
Support Model
```

---

# 12. Application Classification

Applications should be classified according to:

```text
Business Criticality
Data Sensitivity
Security
Availability
Recovery
Regulatory
Integration
User Dependency
```

---

# 13. Application Lifecycle Status

Lifecycle status may include:

```text
Planned
In Development
Test
Production
Maintenance
Deprecated
Retired
```

---

# 14. Application Dependencies

Material dependencies should be mapped to:

```text
Services
Applications
APIs
Databases
Infrastructure
Identity
Security Services
Suppliers
Data
```

---

# 15. Software Development Lifecycle

The SDLC should define controlled progression through:

```text
Requirement
 ↓
Design
 ↓
Development
 ↓
Testing
 ↓
Approval
 ↓
Release
 ↓
Deployment
 ↓
Operation
```

---

# 16. Requirements

Software requirements should be:

```text
Clear
Traceable
Prioritized
Testable
Approved
```

---

# 17. Requirement Traceability

Material requirements should be traceable through:

```text
Requirement
 ↓
Design
 ↓
Code
 ↓
Test
 ↓
Release
```

where appropriate.

---

# 18. Software Architecture

Application architecture should align with approved enterprise and solution architecture principles.

---

# 19. Architecture Review

Material applications and significant changes should undergo appropriate architecture review.

---

# 20. Solution Design

Solution designs should address:

```text
Business
Application
Data
Integration
Security
Infrastructure
Operations
Continuity
```

where relevant.

---

# 21. Development Standards

Development teams should follow approved engineering standards.

---

# 22. Coding Standards

Coding standards should promote:

```text
Readability
Consistency
Maintainability
Security
Testability
Performance
```

---

# 23. Source Code Management

Source code should be stored in approved version-control repositories.

---

# 24. Repository Governance

Repositories should have appropriate:

```text
Ownership
Access Control
Branch Protection
Auditability
Backup
Retention
```

---

# 25. Branching Strategy

Branching strategies should be defined according to application and delivery requirements.

---

# 26. Code Review

Material code changes should undergo appropriate peer review before integration.

---

# 27. Code Review Criteria

Reviews should consider:

```text
Correctness
Security
Quality
Maintainability
Testing
Standards
Dependencies
```

---

# 28. Build Management

Build processes should be controlled and reproducible.

---

# 29. Build Automation

Build automation should be used where appropriate to reduce manual error and improve consistency.

---

# 30. Continuous Integration

CI should validate integrated software changes through automated checks where practical.

---

# 31. Continuous Delivery

CD should support controlled and repeatable delivery of approved software.

---

# 32. DevSecOps

Security should be integrated into software development and delivery rather than treated solely as a final-stage activity.

---

# 33. Secure Development

Secure development should consider:

```text
Threats
Authentication
Authorization
Input Validation
Secrets
Encryption
Logging
Dependencies
Error Handling
```

---

# 34. Secure Coding

Developers should follow approved secure-coding practices appropriate to the technology.

---

# 35. Dependency Management

Software dependencies should be identified, maintained and monitored.

---

# 36. Vulnerability Management

Application vulnerabilities should be:

```text
Identified
Assessed
Prioritized
Remediated
Validated
Tracked
```

---

# 37. Software Composition

Third-party and open-source components should be governed according to security, licensing and lifecycle requirements.

---

# 38. Secrets Management

Application secrets should not be embedded in source code and should use approved secret-management mechanisms where available.

---

# 39. Environment Management

Development, test and production environments should be appropriately separated and controlled.

---

# 40. Development Environment

Development environments should support safe and controlled software creation without inappropriate production exposure.

---

# 41. Test Environment

Test environments should be sufficiently representative to provide meaningful validation.

---

# 42. Production Environment

Production environments should be protected through appropriate access, change, monitoring and operational controls.

---

# 43. Test Strategy

Each material application should have an appropriate test strategy.

---

# 44. Test Planning

Test planning should identify:

```text
Scope
Objectives
Requirements
Test Types
Data
Environment
Roles
Entry Criteria
Exit Criteria
Evidence
```

---

# 45. Unit Testing

Unit tests should validate individual software components where appropriate.

---

# 46. Integration Testing

Integration tests should validate interactions between components, applications, APIs, services and data stores.

---

# 47. System Testing

System testing should validate end-to-end application behavior against defined requirements.

---

# 48. Regression Testing

Regression testing should confirm that changes have not introduced unacceptable unintended effects.

---

# 49. Performance Testing

Performance testing should be used where service performance or scalability is material.

---

# 50. Security Testing

Security testing should be performed according to application risk and requirements.

---

# 51. User Acceptance Testing

Where appropriate, business users should validate that the application meets intended business requirements.

---

# 52. Test Data

Test data should be managed to protect confidentiality, privacy and integrity.

---

# 53. Test Evidence

Test evidence should demonstrate:

```text
Test
Expected Result
Actual Result
Status
Evidence
Defects
Approval
```

---

# 54. Test Defects

Defects should be recorded, prioritized, assigned and tracked through resolution.

---

# 55. Defect Severity

Severity should consider:

```text
Impact
Criticality
Security
Data
Users
Business Function
```

---

# 56. Defect Closure

Defects should be validated before closure where appropriate.

---

# 57. Quality Gates

Software should pass defined quality gates before progression between lifecycle stages.

---

# 58. Development Quality Gate

Development passes when:

```text
Requirement
 ↓
Code
 ↓
Review
 ↓
Build
 ↓
Automated Checks
```

is controlled.

---

# 59. Test Quality Gate

Testing passes when:

```text
Scope
 ↓
Test
 ↓
Evidence
 ↓
Defect Assessment
 ↓
Exit Criteria
```

is satisfied.

---

# 60. Security Quality Gate

Security passes when:

```text
Threat
 ↓
Control
 ↓
Test
 ↓
Finding
 ↓
Remediation / Acceptance
```

is controlled.

---

# 61. Release Quality Gate

Release passes when:

```text
Build
 ↓
Test
 ↓
Security
 ↓
Approval
 ↓
Release Package
```

is complete.

---

# 62. Deployment Quality Gate

Deployment passes when:

```text
Approved Release
 ↓
Deployment
 ↓
Validation
 ↓
Monitoring
 ↓
Acceptance
```

is complete.

---

# 63. Release Engineering

Release Engineering should ensure software releases are reproducible, controlled and traceable.

---

# 64. Release Planning

Release planning should consider:

```text
Scope
Dependencies
Risk
Testing
Security
Change
Support
Communication
Rollback
```

---

# 65. Release Package

A release package may include:

```text
Version
Build
Artifacts
Configuration
Database Changes
Release Notes
Deployment Instructions
Rollback
Evidence
```

---

# 66. Release Versioning

Applications should use an appropriate versioning strategy to identify released software.

---

# 67. Release Approval

Releases require appropriate approval based on risk and governance.

---

# 68. Deployment

Deployments should use controlled and repeatable procedures.

---

# 69. Deployment Automation

Automation should be used where appropriate to improve consistency and reduce deployment risk.

---

# 70. Rollback

Material deployments should have rollback or recovery arrangements appropriate to risk.

---

# 71. Database Change

Database changes should be controlled, tested and traceable.

---

# 72. Application Configuration

Application configuration should be managed separately from code where appropriate and remain controlled and traceable.

---

# 73. API Governance

Material APIs should have:

```text
Owner
Purpose
Version
Authentication
Authorization
Documentation
Monitoring
Lifecycle
```

defined where applicable.

---

# 74. Integration Management

Application integrations should be documented and governed according to criticality and risk.

---

# 75. Application Monitoring

Critical applications should have monitoring appropriate to:

```text
Availability
Performance
Errors
Security
Dependencies
Business Transactions
```

---

# 76. Application Observability

Application observability should provide sufficient information to support:

```text
Detection
Diagnosis
Performance Analysis
Incident Response
Capacity Planning
Recovery
```

---

# 77. Application Logging

Application logs should be appropriately:

```text
Generated
Protected
Retained
Monitored
Reviewed
```

according to requirements.

---

# 78. Application Support

Applications should have defined support arrangements.

---

# 79. Support Model

Support models should define:

```text
Support Owner
Support Hours
Escalation
Knowledge
SLA
Dependencies
Supplier
```

---

# 80. Technical Debt

Technical debt should be identified, assessed and managed.

---

# 81. Technical Debt Register

Material technical debt should be recorded with:

```text
Item
Impact
Risk
Owner
Priority
Remediation
Target
```

---

# 82. Application Risk

Application risk should integrate with Enterprise Risk Management.

---

# 83. Application Risk Assessment

Consider:

```text
Business
Security
Privacy
Technology
Availability
Continuity
Supplier
Compliance
Technical Debt
```

---

# 84. Application Resilience

Critical applications should have appropriate resilience and recovery arrangements.

---

# 85. Application Continuity

Application continuity should align with approved service RTO, RPO and MBCO requirements.

---

# 86. Application Documentation

Critical applications should have sufficient documentation to support:

```text
Development
Support
Operations
Security
Recovery
Change
Retirement
```

---

# 87. Knowledge Transfer

Critical application knowledge should not depend solely on one individual where this creates material operational risk.

---

# 88. Software Licensing

Software licenses should be identified and managed according to applicable requirements.

---

# 89. Open Source Governance

Open-source components should be assessed for:

```text
License
Security
Maintenance
Provenance
Usage
Risk
```

where applicable.

---

# 90. Application Vendor Management

Vendor-supported applications should integrate with Supplier Management and Contract Management.

---

# 91. Vendor Application Performance

Vendor applications should be assessed against agreed:

```text
Support
Availability
Security
Performance
Updates
Incident Response
```

where applicable.

---

# 92. Application Findings

An Application Finding identifies a weakness in application governance, engineering, testing, security, operations or lifecycle management.

---

# 93. Application Exception

An application exception should identify:

```text
Requirement
Deviation
Reason
Risk
Compensating Control
Approval
Expiry
```

---

# 94. Application Remediation

Remediation should identify:

```text
Finding
Cause
Action
Owner
Due Date
Evidence
Validation
```

---

# 95. Application Metrics

Metrics may include:

```text
Release Frequency
Change Failure
Defect Density
Test Coverage
Vulnerability Aging
Build Success
Deployment Success
Availability
Performance
Technical Debt
Support Volume
```

---

# 96. Application Dashboard

May include:

```text
Application Portfolio
Lifecycle
Releases
Quality
Security
Performance
Availability
Technical Debt
Risks
Findings
```

---

# 97. Application Review Cadence

Application reviews should occur according to:

```text
Criticality
Risk
Lifecycle
Change
Business Need
```

---

# 98. Daily Application Review

Where appropriate, operational reviews may consider:

```text
Critical Application Health
Deployment Issues
Security Alerts
Performance
Major Errors
```

---

# 99. Weekly Application Review

A weekly review may consider:

```text
Release Pipeline
Defects
Vulnerabilities
Technical Debt
Support Issues
Application Risks
```

---

# 100. Monthly Application Review

A monthly review may consider:

```text
Application Portfolio
Releases
Quality
Security
Performance
Technical Debt
Support
Supplier Performance
```

---

# 101. Quarterly Application Review

A quarterly review may consider:

```text
Application Strategy
Lifecycle
Architecture
Technology Risk
Security
Continuity
Vendor Dependency
Maturity
```

---

# 102. Annual Application Review

An annual review may consider:

```text
Portfolio
Business Value
Technology Lifecycle
Architecture
Risk
Security
Continuity
Technical Debt
Retirement
Maturity
```

---

# 103. Application Maturity

Application Management maturity should be periodically assessed.

---

# 104. Maturity Dimensions

Assess:

```text
Governance
Portfolio
Lifecycle
Requirements
Architecture
Development
Source Control
Build
Testing
Security
DevSecOps
Release
Deployment
Configuration
Integration
Monitoring
Support
Technical Debt
Documentation
Licensing
Assurance
Improvement
```

---

# 105. Maturity Levels

A baseline model is:

```text
1 – Initial
2 – Repeatable
3 – Defined
4 – Managed
5 – Optimized
```

---

# 106. Application Governance Quality Gate

Application Governance passes when:

```text
Authority
 ↓
Ownership
 ↓
Classification
 ↓
Lifecycle
 ↓
Risk
 ↓
Review
```

is controlled.

---

# 107. Requirements Quality Gate

Requirements pass when:

```text
Need
 ↓
Requirement
 ↓
Acceptance Criteria
 ↓
Traceability
 ↓
Approval
```

is controlled.

---

# 108. Development Quality Gate

Development passes when:

```text
Design
 ↓
Code
 ↓
Review
 ↓
Build
 ↓
Automated Validation
```

is controlled.

---

# 109. Test Quality Gate

Testing passes when:

```text
Requirement
 ↓
Test
 ↓
Evidence
 ↓
Defect
 ↓
Exit Criteria
```

is traceable.

---

# 110. Security Quality Gate

Application Security passes when:

```text
Threat
 ↓
Security Requirement
 ↓
Control
 ↓
Test
 ↓
Finding
 ↓
Remediation / Acceptance
```

is controlled.

---

# 111. Release Quality Gate

Release Engineering passes when:

```text
Build
 ↓
Test
 ↓
Security
 ↓
Approval
 ↓
Artifact
 ↓
Release
```

is traceable.

---

# 112. Deployment Quality Gate

Deployment passes when:

```text
Release
 ↓
Deploy
 ↓
Validate
 ↓
Monitor
 ↓
Accept / Rollback
```

is controlled.

---

# 113. Application Operations Quality Gate

Application Operations passes when:

```text
Service
 ↓
Monitoring
 ↓
Support
 ↓
Incident
 ↓
Problem
 ↓
Improvement
```

is controlled.

---

# 114. Application Retirement Quality Gate

Application Retirement passes when:

```text
Decision
 ↓
Dependency Review
 ↓
Data
 ↓
Access
 ↓
Migration
 ↓
Decommission
 ↓
Evidence
```

is controlled.

---

# 115. Application Assurance Quality Gate

Application Assurance passes when:

```text
Requirement
 ↓
Control
 ↓
Evidence
 ↓
Assessment
 ↓
Finding
 ↓
Remediation
 ↓
Validation
```

is traceable.

---

# 116. Definition of Ready

An application, software or engineering work item is Ready when:

- The application, requirement, defect, change, release, vulnerability, technical-debt item, integration, test, exception or retirement activity is clearly identified.
- Ownership, scope, priority, dependencies, risk, architecture, security, data and operational requirements are known.
- Development, testing, release, deployment, rollback, evidence and acceptance requirements are defined.

---

# 117. Definition of Done

An application, software or engineering work item is Done when:

```text
Requirement Identified
        ↓
Owner Assigned
        ↓
Design / Development Completed
        ↓
Code Review Completed
        ↓
Build and Test Completed
        ↓
Security Validation Completed
        ↓
Release / Deployment Completed Where Applicable
        ↓
Operational / Business Validation Completed
        ↓
Documentation / Configuration / Records Updated
        ↓
Evidence Captured
        ↓
Exceptions / Findings Addressed
        ↓
Outcome Accepted
```

---

# 118. Final Application Principle

> **Applications are enterprise assets and must be governed throughout their complete lifecycle.**

---

# 119. Final Engineering Principle

> **Software must be engineered using controlled, repeatable, secure and maintainable practices.**

---

# 120. Final Testing Principle

> **Software must not progress to operational use without evidence that defined quality and acceptance requirements have been met.**

---

# 121. Final Security Principle

> **Security must be integrated throughout the software lifecycle from design through retirement.**

---

# 122. Final Release Principle

> **Releases must be reproducible, authorized, tested, traceable and recoverable.**

---

# 123. Final Deployment Principle

> **Deployments must be controlled, validated and supported by appropriate rollback or recovery arrangements.**

---

# 124. Final Configuration Principle

> **Application configuration, dependencies and environments must remain sufficiently controlled and traceable to support reliable operations.**

---

# 125. Final Technical Debt Principle

> **Technical debt must be visible, risk-assessed, owned and actively managed.**

---

# 126. Final Documentation Principle

> **Critical application knowledge must be documented sufficiently to support operation, support, security, recovery and lifecycle decisions.**

---

# 127. Final Retirement Principle

> **Applications must be retired in a controlled manner that protects data, services, security, contractual obligations and organizational records.**

---

# 128. Final Improvement Principle

> **Application incidents, defects, vulnerabilities, technical debt, metrics, user feedback and lessons learned must continuously improve software quality and lifecycle effectiveness.**

---

# 129. Final Integration Principle

> **Application Management must integrate with Enterprise Architecture, Service Management, Cybersecurity, Privacy, Data Management, Business Continuity, Supplier Management, Financial Management, People Management, Risk, Compliance and Enterprise Governance.**

---

# 130. Final Steady-State Application Principle

> **MFM applications must be designed, developed, tested, secured, released, operated, maintained and retired through controlled, traceable and continuously improving lifecycle processes.**

---

# 131. Summary

MFM v1.2-Steady-State-30 establishes the permanent Enterprise Application Management, Software Lifecycle, Development, Testing, DevSecOps, Release Engineering and Application Governance baseline.

It defines:

- Application Governance / Application Ownership / Portfolio Management
- Application Records / Classification / Lifecycle Status
- Application Dependencies
- Software Development Lifecycle
- Requirements / Traceability
- Software Architecture / Architecture Review / Solution Design
- Development Standards / Coding Standards
- Source Code Management / Repository Governance / Branching
- Code Review
- Build Management / Automation / Continuous Integration / Continuous Delivery
- DevSecOps / Secure Development / Secure Coding
- Dependency / Vulnerability / Software Composition Management
- Secrets Management
- Environment Management
- Test Strategy / Planning / Unit / Integration / System / Regression / Performance / Security / UAT
- Test Data / Evidence / Defect Management
- Quality Gates
- Release Engineering / Release Planning / Release Packages / Versioning
- Release Approval / Deployment / Automation / Rollback
- Database Changes / Application Configuration
- API Governance / Integration Management
- Application Monitoring / Observability / Logging
- Application Support / Support Models
- Technical Debt / Technical Debt Register
- Application Risk / Resilience / Continuity
- Application Documentation / Knowledge Transfer
- Software Licensing / Open Source Governance
- Application Vendor Management
- Application Findings / Exceptions / Remediation
- Application Metrics / Dashboards
- Daily / Weekly / Monthly / Quarterly / Annual Application Reviews
- Application Maturity
- Application / Requirements / Development / Test / Security / Release / Deployment / Operations / Retirement / Assurance Quality Gates
- Definition of Ready
- Definition of Done

---

# 132. Next Document

The next document shall be:

**MFM v1.2-Steady-State-31 – Enterprise Data Management, Data Governance, Data Quality, Master Data, Metadata, Information Lifecycle & Data Architecture**

It shall establish the permanent enterprise data-management and data-governance operating model supporting MFM.

---

# 133. Document Control

**Document:** MFM v1.2-Steady-State-30  
**Version:** 1.2  
**Status:** Steady-State Enterprise Application & Software Engineering Baseline  
**Previous Document:** MFM v1.2-Steady-State-29  
**Next Document:** MFM v1.2-Steady-State-31  
**Lifecycle:** Steady-State Operation  
**Primary Transition:** Enterprise Service Management / IT Service Operations / Service Desk / Incident / Problem / Change / Configuration Management → Enterprise Application Management / Software Lifecycle / Development / Testing / DevSecOps / Release Engineering / Application Governance  
**Application Authority:** Application Management / Application Governance  
**Software Engineering Authority:** Software Engineering / Development Governance  
**Architecture Authority:** Enterprise Architecture / Solution Architecture  
**Security Authority:** Cybersecurity / Application Security / DevSecOps  
**Privacy Authority:** Privacy / Data Protection  
**Data Authority:** Enterprise Data Management / Data Governance  
**Service Authority:** Enterprise Service Management / ITSM  
**Operations Authority:** IT Operations / Application Operations  
**Release Authority:** Release Engineering / Release Management  
**Change Authority:** Change Management / Change Governance  
**Supplier Authority:** Supplier Management / Application Vendors  
**Financial Authority:** Financial Management / IT Financial Management  
**People Authority:** Human Resources / Workforce Management  
**Risk Authority:** Enterprise Risk Management / Technology Risk  
**Compliance Authority:** Compliance / Regulatory Compliance  
**Continuity Authority:** Business Continuity / Disaster Recovery  
**Assurance Authority:** Application Assurance / Internal Audit / Independent Assurance  
**Legal Authority:** Legal / Software Licensing / Contract Governance  
**Improvement Authority:** Application Continual Improvement  
**Principle:** MFM applications must be designed, developed, tested, secured, released, operated, maintained and retired through controlled, traceable and continuously improving lifecycle processes.
