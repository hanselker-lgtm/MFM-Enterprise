# MFM v1.2-Steady-State-116
## Enterprise Identity & Access Management, IAM Governance, Authentication, Authorization, Privileged Access, Identity Lifecycle & IAM Assurance

**Version:** 1.2  
**Document ID:** MFM v1.2-Steady-State-116  
**Status:** Steady-State Enterprise Identity & Access Management Baseline  
**Lifecycle:** Post-Implementation / Steady-State Operation  
**Document Type:** Identity Architecture / IAM Governance / Authentication / Authorization / Privileged Access / Identity Lifecycle / IAM Assurance Document  

---

# 1. Purpose

This document establishes the one-hundred-and-sixteenth document in the MFM v1.2 Steady-State series.

It follows MFM v1.2-Steady-State-115 – Enterprise IT Service Management, Service Governance, Service Catalog, Incident, Problem, Change, Request, Configuration & ITSM Assurance.

The purpose is to establish the permanent enterprise operating model for identity strategy, IAM governance, identity architecture, workforce identity, customer identity where applicable, machine identities, authentication, MFA, authorization, RBAC, ABAC, privileged access management, identity lifecycle, joiner-mover-leaver processes, access requests, access reviews, segregation of duties, service accounts, secrets, certificates, federation, single sign-on, identity monitoring, identity incidents, identity risk, exceptions, remediation, assurance, metrics, dashboards, maturity and continual enterprise identity capability improvement.

The central objective is:

> **MFM must govern identity and access as foundational enterprise security capabilities, ensuring that every material human, machine and service identity is appropriately established, authenticated, authorized, monitored, reviewed and retired throughout its lifecycle.**

---

# 2. Scope

This document covers:

- Identity Strategy
- IAM Governance
- Identity Architecture
- Workforce Identity
- Customer Identity where Applicable
- Machine Identities
- Authentication
- Multi-Factor Authentication
- Authorization
- Role-Based Access Control
- Attribute-Based Access Control
- Privileged Access Management
- Identity Lifecycle
- Joiner-Mover-Leaver
- Access Requests
- Access Reviews
- Segregation of Duties
- Service Accounts
- Secrets
- Certificates
- Federation
- Single Sign-On
- Identity Monitoring
- Identity Incidents
- Identity Risk
- Identity Exceptions
- Identity Remediation
- IAM Assurance
- Identity Metrics
- Identity Dashboards
- Identity Maturity
- Continual Enterprise Identity Capability Improvement

---

# 3. Identity Governance Objective

The primary objective is:

> **Establish clear authority, ownership, standards, approval requirements, risk controls and assurance for enterprise identities and access.**

# 4. Identity Architecture Objective

The primary objective is:

> **Provide a coherent identity architecture supporting secure authentication, authorization, federation, lifecycle management and least-privilege access across enterprise environments.**

# 5. Authentication Objective

The primary objective is:

> **Verify identity reliably and proportionately to risk before granting access to enterprise resources.**

# 6. Authorization Objective

The primary objective is:

> **Ensure access is granted only when authorized, necessary, appropriate to role and consistent with business and security requirements.**

# 7. Privileged Access Objective

The primary objective is:

> **Protect privileged identities and administrative capabilities through enhanced controls, monitoring, approval and accountability.**

# 8. Identity Lifecycle Objective

The primary objective is:

> **Ensure identities and access rights are created, changed, reviewed and removed accurately and promptly throughout the identity lifecycle.**

# 9. IAM Assurance Objective

The primary objective is:

> **Provide evidence that identity and access controls operate effectively and that excessive, inappropriate or unmanaged access is identified and remediated.**

# 10. Identity Principles

Identity should be:

```text
Unique
Owned
Authenticated
Authorized
Least-Privilege
Lifecycle-Controlled
Monitored
Reviewable
Traceable
```

# 11. Access Principles

Access should be:

```text
Need-to-Know
Need-to-Use
Least-Privilege
Role-Appropriate
Time-Bounded where Appropriate
Risk-Based
Auditable
```

# 12. Privileged Access Principles

Privileged access should be:

```text
Restricted
Approved
Strongly Authenticated
Monitored
Time-Bounded where Appropriate
Reviewed
Traceable
```

# 13. Identity Lifecycle

Identity management should integrate:

```text
Request
 ↓
Establish
 ↓
Verify
 ↓
Provision
 ↓
Authenticate
 ↓
Authorize
 ↓
Monitor
 ↓
Review
 ↓
Change
 ↓
Revoke
 ↓
Retire
```

# 14. IAM Governance

IAM governance should establish:

```text
Authority
Ownership
Standards
Roles
Approval
Risk
Assurance
Improvement
```

# 15. IAM Authority

IAM authority should define who may:

```text
Approve Identity Strategy
Approve IAM Architecture
Approve Authentication Standards
Approve Authorization Models
Approve Privileged Access
Approve Material Exceptions
Accept Identity Risk
```

# 16. Identity Ownership

Material identity capabilities should have accountable owners for:

```text
Identity
Authentication
Authorization
Privileged Access
Lifecycle
Directories
Federation
Monitoring
Compliance
```

# 17. Identity Sources

Authoritative identity sources should be defined for relevant identity classes.

# 18. Workforce Identity

Workforce identities should be linked to authoritative employment or organizational records where appropriate.

# 19. External Identity

External users, partners and other non-workforce identities should have defined ownership, purpose, scope and lifecycle.

# 20. Customer Identity

Where customer-facing identity is applicable, customer identity should be governed separately from workforce identity where appropriate.

# 21. Machine Identity

Machine and workload identities should be treated as managed identities with:

```text
Owner
Purpose
Scope
Credential / Trust Mechanism
Lifecycle
Monitoring
```

# 22. Service Identity

Service identities should be governed for:

```text
Owner
Application
Purpose
Permissions
Credential
Rotation
Monitoring
Retirement
```

# 23. Identity Inventory

Material identities should be inventoried where technically and operationally feasible.

Inventory may include:

```text
User
Role
Group
Service Account
Machine Identity
Application Identity
Certificate
Credential
Privilege
Owner
Status
Lifecycle
```

# 24. Identity Uniqueness

Human identities should be uniquely attributable to an individual unless a formally governed exception exists.

# 25. Shared Accounts

Shared accounts should be prohibited where practical and otherwise require explicit risk-based approval, compensating controls and accountability mechanisms.

# 26. Identity Proofing

Identity proofing should establish sufficient confidence in identity according to:

```text
Risk
Access Sensitivity
Identity Type
Business Context
```

# 27. Authentication

Authentication controls should be appropriate to:

```text
Identity
Resource
Risk
Location
Device
Context
```

# 28. Password Management

Where passwords are used, controls should address:

```text
Complexity
Protection
Storage
Reset
Recovery
Compromise
```

# 29. Multi-Factor Authentication

MFA should be required for access according to risk and approved security policy, with enhanced requirements for privileged and sensitive access.

# 30. Authentication Factors

Authentication may use appropriate combinations of:

```text
Knowledge
Possession
Inherence
Cryptographic Credentials
Context
```

# 31. Adaptive Authentication

Where supported, authentication decisions may consider:

```text
Risk
Device
Location
Behavior
Resource
Identity
```

# 32. Authentication Failure

Authentication failures should be monitored for potential:

```text
Credential Abuse
Brute Force
Password Spraying
Account Enumeration
Automated Attack
```

# 33. Account Lockout and Protection

Account protection mechanisms should balance security with availability and operational recovery.

# 34. Single Sign-On

SSO should be used where appropriate to improve:

```text
Security
User Experience
Centralized Control
Lifecycle Management
```

# 35. Federation

Federation should be governed for:

```text
Trust
Identity Provider
Service Provider
Claims
Authentication
Authorization
Lifecycle
```

# 36. Federation Trust

Federated relationships should have:

```text
Owner
Purpose
Trust Basis
Security Requirements
Review
Expiry / Renewal
```

# 37. Authorization

Authorization should determine access based on approved:

```text
Role
Attributes
Business Need
Resource
Context
```

# 38. Role-Based Access Control

RBAC should define:

```text
Role
Purpose
Permissions
Owner
Eligibility
Approval
Review
```

# 39. Role Engineering

Roles should avoid unnecessary permission aggregation and should be designed according to business responsibilities.

# 40. Attribute-Based Access Control

ABAC may use controlled attributes such as:

```text
User
Role
Department
Resource
Classification
Location
Device
Risk
Time
```

# 41. Least Privilege

Access should grant the minimum privileges necessary to perform approved responsibilities.

# 42. Privilege Separation

Conflicting administrative and business responsibilities should be separated where required.

# 43. Segregation of Duties

SoD controls should identify and prevent or detect incompatible combinations of access.

# 44. SoD Rules

Material SoD rules should have:

```text
Definition
Owner
Risk
Exception Process
Review
```

# 45. Access Requests

Access requests should be:

```text
Requested
Justified
Approved
Provisioned
Recorded
Reviewed
```

# 46. Access Approval

Approvals should be performed by authorized business or technical owners according to access type.

# 47. Access Provisioning

Provisioning should use controlled processes and automation where practical.

# 48. Access Changes

Access changes should be triggered by:

```text
Role Change
Department Change
Project Change
Risk Change
Business Need
```

# 49. Joiner Process

New identity onboarding should establish:

```text
Identity
Authentication
Required Access
Security Controls
Ownership
```

# 50. Mover Process

Role or organizational changes should trigger review and adjustment of existing access.

# 51. Leaver Process

Termination or departure should trigger timely:

```text
Access Revocation
Session / Credential Invalidation where Required
Asset Recovery
Token / Certificate Revocation where Required
```

# 52. Dormant Accounts

Dormant or inactive identities should be identified and handled according to policy.

# 53. Orphaned Accounts

Orphaned accounts should be identified, assigned an owner or disabled.

# 54. Privileged Access Management

Privileged access should use enhanced controls including where appropriate:

```text
Approval
JIT / JEA
Strong Authentication
Credential Vaulting
Session Monitoring
Command Logging
Periodic Review
```

# 55. Privileged Roles

Privileged roles should be clearly identified and inventoried.

# 56. Administrative Accounts

Administrative accounts should be separated from normal user identities where practical.

# 57. Break-Glass Access

Emergency or break-glass access should have:

```text
Restricted Use
Strong Protection
Approval / Justification
Monitoring
Immediate Review
```

# 58. Privileged Session Management

Privileged sessions should be monitored or recorded according to risk and applicable requirements.

# 59. Privileged Credential Management

Privileged credentials should use controlled storage, rotation and access mechanisms.

# 60. Service Accounts

Service accounts should have:

```text
Owner
Purpose
Application
Permissions
Credential
Rotation
Monitoring
Expiry / Review
```

# 61. Non-Interactive Accounts

Non-interactive accounts should be restricted from interactive use unless explicitly required and approved.

# 62. Secrets Management

Secrets should be stored in approved secure mechanisms and should not be exposed in:

```text
Source Code
Configuration Files
Logs
Tickets
Documentation
```

# 63. Secret Rotation

Material secrets should be rotated according to risk and capability.

# 64. Certificates

Certificates should have:

```text
Owner
Purpose
Issuer
Subject
Validity
Renewal
Revocation
Lifecycle
```

# 65. Certificate Management

Certificate expiry should be monitored to prevent service disruption.

# 66. Identity Tokens

Tokens should be appropriately protected with controls for:

```text
Issuance
Scope
Lifetime
Validation
Revocation
```

# 67. Identity Governance

Identity governance should maintain visibility of:

```text
Who
Has What
Why
For How Long
Approved By Whom
```

# 68. Access Reviews

Access reviews should be performed according to:

```text
Risk
Privilege
Sensitivity
Criticality
Regulatory Requirements
```

# 69. Privileged Access Reviews

Privileged access should receive enhanced periodic review.

# 70. Service Account Reviews

Service and machine identities should be reviewed for:

```text
Ownership
Purpose
Permissions
Usage
Lifecycle
```

# 71. Group Reviews

Security-sensitive groups should be reviewed according to risk.

# 72. Role Reviews

Material roles should be reviewed for:

```text
Business Need
Permissions
Conflicts
Usage
Owner
```

# 73. Access Recertification

Recertification should provide evidence of:

```text
Reviewer
Scope
Decision
Date
Exceptions
Remediation
```

# 74. Identity Monitoring

Identity monitoring should detect relevant:

```text
Authentication Anomalies
Privilege Changes
Unusual Access
Credential Abuse
Dormant Accounts
MFA Changes
Administrative Activity
```

# 75. Identity Analytics

Where appropriate, identity analytics may identify:

```text
Impossible Travel
Abnormal Login Patterns
Privilege Escalation
Unusual Resource Access
Risky Devices
```

# 76. Identity Risk

Identity risks should be:

```text
Identified
Assessed
Owned
Treated
Monitored
Reported
```

# 77. Identity Risk Factors

Assessment may consider:

```text
Privilege
Data Sensitivity
Resource Criticality
Authentication Strength
Exposure
Behavior
Lifecycle Status
```

# 78. Identity Incidents

Identity incidents may include:

```text
Account Compromise
Credential Theft
MFA Abuse
Privilege Escalation
Unauthorized Access
Orphaned Access
Federation Failure
Certificate Compromise
```

# 79. Identity Incident Response

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
Revoke / Reset
 ↓
Recover
 ↓
Validate
 ↓
Learn
```

# 80. Credential Compromise

Compromised credentials should be handled through appropriate:

```text
Revocation
Reset
Token Invalidation
Session Termination
Investigation
Monitoring
```

# 81. Identity Threat Detection

Identity threat detection should integrate with enterprise security monitoring and incident response.

# 82. Access Logging

Material identity and access events should be logged according to risk and requirements.

# 83. Identity Log Governance

Identity logs should have:

```text
Source
Owner
Retention
Integrity
Access Control
Monitoring
```

# 84. Identity Integration

IAM should integrate with:

```text
HR / Workforce Systems
Applications
Cloud Platforms
Infrastructure
Networks
Data Platforms
Security Operations
IT Service Management
```

# 85. Directory Services

Enterprise directories should have:

```text
Owner
Architecture
Replication
Security
Backup
Recovery
Lifecycle
```

# 86. Identity Synchronization

Synchronization between identity sources should be:

```text
Controlled
Monitored
Validated
Recoverable
```

# 87. Identity Data Quality

Identity records should be assessed for:

```text
Accuracy
Completeness
Uniqueness
Timeliness
Ownership
```

# 88. Identity Reconciliation

Material identity stores should be periodically reconciled with authoritative sources.

# 89. Identity Provisioning Automation

Where appropriate, provisioning and deprovisioning should be automated to reduce manual error and delay.

# 90. Identity Workflow

Identity workflows should provide:

```text
Request
Approval
Provision
Validate
Review
Revoke
```

# 91. Access Certification Workflow

Access certification should support:

```text
Scope
Reviewer Assignment
Review
Decision
Remediation
Evidence
```

# 92. Privileged Access Workflow

Privileged access should support:

```text
Request
Risk Assessment
Approval
Activation
Monitoring
Expiration
Review
```

# 93. Identity Security Baseline

Identity security baselines should address:

```text
Authentication
MFA
Authorization
Privileged Access
Lifecycle
Logging
Monitoring
Secrets
Certificates
```

# 94. Identity Compliance

IAM should comply with applicable:

```text
Policies
Standards
Contracts
Legal Requirements
Regulatory Requirements
```

# 95. Identity Compliance Monitoring

Compliance should be periodically assessed according to risk.

# 96. Identity Exceptions

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

# 97. Identity Remediation

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

# 98. Identity Assurance

Assurance may include:

```text
Identity Architecture Reviews
Authentication Reviews
MFA Reviews
Access Reviews
Privileged Access Reviews
SoD Reviews
Service Account Reviews
Certificate Reviews
Federation Reviews
Configuration Reviews
Identity Testing
Supplier Reviews
Internal Audit
Independent Assurance
```

# 99. Identity Evidence

Evidence should support:

```text
Identity Ownership
Authentication
Authorization
Access Approval
Provisioning
Deprovisioning
Privileged Access
SoD
Access Reviews
Service Accounts
Secrets
Certificates
Federation
Monitoring
Incidents
Risk
Exceptions
Remediation
Compliance
Assurance
```

# 100. Identity Metrics

Metrics may include:

```text
Identity Inventory Coverage
Identity Ownership Coverage
MFA Coverage
Strong Authentication Coverage
SSO Coverage
Federation Coverage
Access Request SLA
Provisioning Time
Deprovisioning Time
Leaver Revocation Compliance
Dormant Account Rate
Orphaned Account Rate
Privileged Account Coverage
Privileged Access Review Completion
Service Account Ownership Coverage
Service Account Review Completion
SoD Conflict Volume
SoD Remediation Rate
Access Review Completion
Access Recertification Completion
Excessive Privilege Findings
Authentication Failure Rate
Identity Incident Volume
Credential Compromise Volume
Identity Detection Coverage
Certificate Expiry Risk
Secret Rotation Compliance
Directory Synchronization Success
Identity Data Quality
Identity Compliance
Exception Age
Remediation Completion
IAM Assurance Findings
```

# 101. Identity Dashboard

May include:

```text
Identity Health
Authentication
MFA
SSO
Federation
Authorization
Privileged Access
JML
Access Requests
Access Reviews
SoD
Service Accounts
Secrets
Certificates
Directories
Identity Monitoring
Identity Incidents
Identity Risk
Compliance
Exceptions
Remediation
Assurance
```

# 102. Daily Review

Where appropriate:

```text
Critical Authentication Alerts
Privileged Access Alerts
Identity Incidents
Credential Compromise
MFA Anomalies
Federation Failures
Certificate Expiry Alerts
Provisioning Failures
```

# 103. Weekly Review

May consider:

```text
Identity Incidents
Privileged Activity
MFA Coverage
Access Changes
JML Performance
Dormant Accounts
Orphaned Accounts
Service Accounts
Certificate Issues
Open Remediation
```

# 104. Monthly Review

May consider:

```text
IAM Governance
Identity Inventory
Authentication
MFA
SSO
Authorization
Privileged Access
JML
Access Reviews
SoD
Service Accounts
Secrets
Certificates
Directories
Monitoring
Incidents
Risk
Compliance
Assurance
```

# 105. Quarterly Review

May consider:

```text
Identity Strategy
IAM Architecture
Governance
Authentication
Authorization
Privileged Access
JML
Access Governance
SoD
Machine Identity
Federation
Security Monitoring
Identity Risk
Supplier Risk
Compliance
Assurance
Maturity
```

# 106. Annual Review

May consider:

```text
Identity Strategy
Operating Model
Governance
Architecture
Identity Sources
Workforce Identity
External Identity
Customer Identity
Machine Identity
Authentication
MFA
Authorization
RBAC
ABAC
PAM
JML
Access Requests
Access Reviews
SoD
Service Accounts
Secrets
Certificates
Federation
SSO
Monitoring
Incidents
Risk
Compliance
Exceptions
Remediation
Assurance
Maturity
Improvement
```

# 107. IAM Maturity

Identity capability maturity should be periodically assessed.

# 108. Maturity Dimensions

Assess:

```text
Governance
Strategy
Authority
Ownership
Identity Sources
Workforce Identity
External Identity
Customer Identity
Machine Identity
Service Identity
Identity Inventory
Uniqueness
Identity Proofing
Authentication
Password Management
MFA
Authentication Factors
Adaptive Authentication
Authentication Failure Monitoring
Account Protection
SSO
Federation
Federation Trust
Authorization
RBAC
Role Engineering
ABAC
Least Privilege
Privilege Separation
SoD
Access Requests
Access Approval
Provisioning
Access Changes
Joiner
Mover
Leaver
Dormant Accounts
Orphaned Accounts
PAM
Privileged Roles
Administrative Accounts
Break-Glass
Privileged Sessions
Privileged Credentials
Service Accounts
Non-Interactive Accounts
Secrets
Secret Rotation
Certificates
Certificate Management
Tokens
Identity Governance
Access Reviews
Privileged Reviews
Service Account Reviews
Group Reviews
Role Reviews
Access Recertification
Identity Monitoring
Identity Analytics
Identity Risk
Identity Incidents
Incident Response
Credential Compromise
Threat Detection
Access Logging
Log Governance
Directory Services
Identity Synchronization
Identity Data Quality
Identity Reconciliation
Provisioning Automation
Identity Workflows
Access Certification
Privileged Workflows
Security Baselines
Compliance
Exceptions
Remediation
Assurance
Evidence
Metrics
Improvement
```

# 109. Maturity Levels

```text
1 – Initial
2 – Repeatable
3 – Defined
4 – Managed
5 – Optimized
```

# 110. Identity Architecture Quality Gate

```text
Business Need
 ↓
Identity Requirement
 ↓
Risk
 ↓
Identity Architecture
 ↓
Authentication
 ↓
Authorization
 ↓
Lifecycle
 ↓
Monitoring
 ↓
Assurance
```

must be controlled.

# 111. Access Request Quality Gate

```text
Request
 ↓
Business Need
 ↓
Identity
 ↓
Role / Permission
 ↓
Risk / SoD
 ↓
Approval
 ↓
Provision
 ↓
Validate
 ↓
Record
```

must be controlled.

# 112. Privileged Access Quality Gate

```text
Request
 ↓
Risk
 ↓
Approval
 ↓
Strong Authentication
 ↓
Activation
 ↓
Monitor
 ↓
Expire / Revoke
 ↓
Review
```

must be controlled.

# 113. Joiner-Mover-Leaver Quality Gate

```text
Authoritative Event
 ↓
Identity Update
 ↓
Access Assessment
 ↓
Provision / Modify / Revoke
 ↓
Validate
 ↓
Record
 ↓
Review
```

must be controlled.

# 114. Access Review Quality Gate

```text
Scope
 ↓
Reviewer
 ↓
Review
 ↓
Decision
 ↓
Remediation
 ↓
Validation
 ↓
Evidence
```

must be traceable.

# 115. Identity Recovery Quality Gate

```text
Identity Failure / Compromise
 ↓
Contain
 ↓
Reset / Revoke
 ↓
Restore Trust
 ↓
Validate
 ↓
Monitor
 ↓
Lessons Learned
```

must be controlled.

# 116. IAM Assurance Quality Gate

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

# 117. Definition of Ready

An identity architecture, authentication method, authorization model, access request, privileged access arrangement, JML workflow, service account, federation relationship, certificate, secret, access review, exception, remediation or assurance review is Ready when purpose, identity type, owner, scope, affected resources, business need, security requirements, risk, approval authority and acceptance criteria are defined.

# 118. Definition of Done

An IAM work item is Done when:

```text
Requirement / Identity Event Identified
        ↓
Owner Assigned
        ↓
IAM Action Completed
        ↓
Authentication / Authorization / Lifecycle / Security Validation Completed where Required
        ↓
Identity / Access / Role / Privilege / Certificate / Secret / Audit Records Updated
        ↓
Evidence Captured
        ↓
Findings / Exceptions Addressed
        ↓
Outcome Accepted
```

# 119. Final Identity Governance Principle

> **MFM must govern identity and access as foundational enterprise security capabilities, ensuring that every material human, machine and service identity is appropriately established, authenticated, authorized, monitored, reviewed and retired throughout its lifecycle.**

# 120. Final Authentication Principle

> **Authentication must provide sufficient assurance of identity for the sensitivity and risk of the resource being accessed, with stronger controls applied where risk requires them.**

# 121. Final Authorization Principle

> **Authorization must grant only the access necessary for an approved business purpose and must remain aligned with role, responsibility, resource sensitivity and risk.**

# 122. Final Privileged Access Principle

> **Privileged access must receive enhanced protection, strong authentication, controlled activation, monitoring, review and accountability.**

# 123. Final Lifecycle Principle

> **Identity and access must be governed from establishment through authentication, authorization, change, review, revocation and retirement.**

# 124. Final Least-Privilege Principle

> **MFM must continuously reduce unnecessary privilege and prevent accumulation of access beyond legitimate business requirements.**

# 125. Final Identity Data Principle

> **Identity records must remain accurate, unique, timely, owned and reconciled with authoritative sources.**

# 126. Final Monitoring Principle

> **Material identity and access activity must be sufficiently observable to detect misuse, compromise, privilege abuse and lifecycle failures.**

# 127. Final Assurance Principle

> **Material IAM controls must be supported by reliable evidence and periodically assessed through risk-based assurance.**

# 128. Final Improvement Principle

> **Identity incidents, excessive access, SoD conflicts, lifecycle failures, authentication weaknesses and assurance findings must continuously improve MFM's identity capability.**

# 129. Final Integration Principle

> **Identity and Access Management must integrate with Enterprise Architecture, HR and workforce systems, Applications, Data, Network, Infrastructure, Cloud, Cybersecurity, IT Service Management, Configuration Management, Asset Management, Suppliers, Risk, Compliance, Privacy and Business Continuity.**

# 130. Final Steady-State IAM Principle

> **MFM must govern identity and access as foundational enterprise security capabilities, ensuring that every material human, machine and service identity is appropriately established, authenticated, authorized, monitored, reviewed and retired throughout its lifecycle.**

# 131. Summary

MFM v1.2-Steady-State-116 establishes the permanent Enterprise Identity & Access Management baseline.

It defines:

- Identity Strategy / IAM Governance / Authority / Ownership
- Identity Sources / Workforce / External / Customer / Machine / Service Identities
- Identity Inventory / Uniqueness / Identity Proofing
- Authentication / Passwords / MFA / Authentication Factors / Adaptive Authentication
- Authentication Monitoring / Account Protection
- SSO / Federation / Federation Trust
- Authorization / RBAC / Role Engineering / ABAC
- Least Privilege / Privilege Separation / Segregation of Duties
- Access Requests / Approval / Provisioning / Access Changes
- Joiner / Mover / Leaver
- Dormant / Orphaned Accounts
- Privileged Access Management / Privileged Roles / Administrative Accounts
- Break-Glass / Privileged Sessions / Credential Management
- Service Accounts / Non-Interactive Accounts
- Secrets / Rotation / Certificates / Certificate Management
- Identity Tokens
- Identity Governance / Access Reviews / Recertification
- Privileged / Service Account / Group / Role Reviews
- Identity Monitoring / Identity Analytics
- Identity Risk / Identity Incidents / Credential Compromise
- Identity Threat Detection / Access Logging / Log Governance
- Directory Services / Identity Synchronization / Data Quality / Reconciliation
- Provisioning Automation / Identity Workflows / Access Certification
- Privileged Access Workflows
- Identity Security Baselines
- Compliance / Exceptions / Remediation / Assurance / Evidence
- IAM Metrics / IAM Dashboard
- Daily / Weekly / Monthly / Quarterly / Annual Reviews
- IAM Maturity
- Identity Architecture / Access Request / Privileged Access / JML / Access Review / Recovery / Assurance Quality Gates
- Definition of Ready
- Definition of Done

# 132. Next Document

**MFM v1.2-Steady-State-117 – Enterprise Network Architecture, Network Governance, Connectivity, Segmentation, Firewalling, DNS, Remote Access, Network Security & Network Assurance**

It shall establish the permanent enterprise operating model for network strategy, network architecture, network governance, LAN/WAN, internet connectivity, wireless, remote access, VPN, network segmentation, firewalls, routing, switching, DNS, DHCP, IP address management, network monitoring, network performance, network resilience, network configuration, network incidents, network changes, network capacity, network suppliers, network security integration, network compliance, network exceptions, remediation, network assurance, network metrics, dashboards, maturity and continual enterprise network capability improvement supporting MFM.

# 133. Document Control

**Document:** MFM v1.2-Steady-State-116  
**Version:** 1.2  
**Status:** Steady-State Enterprise Identity & Access Management Baseline  
**Previous Document:** MFM v1.2-Steady-State-115  
**Next Document:** MFM v1.2-Steady-State-117  
**Lifecycle:** Steady-State Operation  
**IAM Governance Authority:** Enterprise Identity & Access Management  
**Identity Architecture Authority:** Enterprise Identity Architecture  
**Authentication Authority:** Authentication Management  
**Authorization Authority:** Access Governance  
**Privileged Access Authority:** Privileged Access Management  
**Identity Lifecycle Authority:** Identity Lifecycle Management  
**Directory Authority:** Directory Services  
**Federation Authority:** Federation / SSO Management  
**Identity Monitoring Authority:** Identity Security Monitoring  
**Cybersecurity Authority:** Enterprise Cybersecurity  
**Application Authority:** Enterprise Application Architecture  
**Data Authority:** Enterprise Data Management  
**Infrastructure Authority:** Enterprise Infrastructure Architecture  
**Cloud Authority:** Enterprise Cloud Architecture  
**Network Authority:** Enterprise Network Architecture  
**Service Authority:** Enterprise IT Service Management  
**Configuration Authority:** Configuration Management  
**Asset Authority:** Enterprise Asset Management  
**HR Authority:** Workforce / Human Resources Management  
**Supplier Authority:** Supplier / Third-Party Management  
**Risk Authority:** Enterprise Risk Management  
**Compliance Authority:** Enterprise Compliance  
**Privacy Authority:** Privacy / Data Protection Governance  
**Legal Authority:** Legal / Regulatory Affairs  
**Continuity Authority:** Business Continuity / Operational Resilience  
**Assurance Authority:** IAM Assurance / Internal Audit / Independent Assurance  
**Improvement Authority:** Continual Enterprise Identity Capability Improvement  

**Principle:** MFM must govern identity and access as foundational enterprise security capabilities, ensuring that every material human, machine and service identity is appropriately established, authenticated, authorized, monitored, reviewed and retired throughout its lifecycle.
