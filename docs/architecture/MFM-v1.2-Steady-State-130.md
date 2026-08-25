# MFM v1.2-Steady-State-130
## Enterprise Identity & Access Management Architecture, IAM Governance, Authentication, Authorization, Privileged Access, Identity Lifecycle, Federation, Directory Services, Access Governance, Identity Security & IAM Assurance

**Version:** 1.2  
**Document ID:** MFM v1.2-Steady-State-130  
**Status:** Steady-State Enterprise Identity & Access Management Architecture & Operations Baseline  
**Lifecycle:** Post-Implementation / Steady-State Operation  
**Document Type:** Identity Architecture / IAM Governance / Authentication / Authorization / Privileged Access / Identity Lifecycle / Federation / Directory Services / Access Governance / Identity Security / IAM Assurance Document  

---

# 1. Purpose

This document establishes the one-hundred-and-thirtieth document in the MFM v1.2 Steady-State series.

It follows MFM v1.2-Steady-State-129 – Enterprise Data Architecture, Data Governance, Data Lifecycle, Data Quality, Master Data, Metadata, Data Integration, Data Security, Data Privacy, Data Resilience & Data Assurance.

The purpose is to establish the permanent enterprise operating model for identity strategy, IAM governance, identity architecture, workforce identity, customer identity where applicable, machine identity, directory services, authentication, authorization, federation, privileged access, access requests, access reviews, joiner/mover/leaver processes, identity lifecycle, credentials, secrets, certificates, identity security, access incidents, IAM changes, IAM suppliers, IAM compliance, IAM exceptions, remediation, IAM assurance, metrics, dashboards, maturity and continual enterprise identity capability improvement.

The central objective is:

> **MFM must govern identity and access as a controlled enterprise security and business capability, ensuring that every material human, machine, application and external identity is appropriately established, authenticated, authorized, monitored, reviewed and lifecycle-controlled according to business need, risk and service requirements.**

---

# 2. Scope

This document covers:

- Identity Strategy
- IAM Governance
- Identity Architecture
- Workforce Identity
- Customer Identity where Applicable
- Machine Identity
- Application Identity
- Directory Services
- Authentication
- Authorization
- Federation
- Single Sign-On
- Privileged Access
- Access Requests
- Access Approvals
- Access Reviews
- Joiner / Mover / Leaver
- Identity Lifecycle
- Credentials
- Secrets
- Certificates
- Identity Security
- Identity Monitoring
- Identity Incidents
- IAM Changes
- IAM Suppliers
- IAM Compliance
- IAM Exceptions
- IAM Remediation
- IAM Assurance
- IAM Metrics
- IAM Dashboards
- IAM Maturity
- Continual Enterprise Identity Capability Improvement

---

# 3. Identity Governance Objective

The primary objective is:

> **Establish clear authority, ownership, standards, lifecycle controls, access responsibilities, security requirements and assurance for enterprise identities and access.**

# 4. Identity Architecture Objective

The primary objective is:

> **Provide a coherent identity architecture supporting people, applications, machines, services, devices, partners and customers across enterprise, cloud and external environments.**

# 5. Authentication Objective

The primary objective is:

> **Verify identity reliably using authentication mechanisms appropriate to identity type, access risk and service requirements.**

# 6. Authorization Objective

The primary objective is:

> **Ensure access is granted according to legitimate business need, least privilege, separation of duties and defined authorization policies.**

# 7. Privileged Access Objective

The primary objective is:

> **Protect privileged identities and administrative capabilities through enhanced controls, monitoring, approval, time limitation and accountability.**

# 8. Identity Lifecycle Objective

The primary objective is:

> **Ensure identities and access rights are created, changed, reviewed, suspended and removed accurately and promptly throughout their lifecycle.**

# 9. Identity Security Objective

The primary objective is:

> **Protect identity systems and credentials against compromise, misuse, privilege escalation, unauthorized access and identity-based attacks.**

# 10. IAM Assurance Objective

The primary objective is:

> **Provide evidence that material identity and access controls operate effectively and support business, security, compliance and risk requirements.**

# 11. Identity Principles

Identity capability should be:

```text
Business-Aligned
Unique
Accountable
Authenticated
Authorized
Least-Privilege
Lifecycle-Controlled
Observable
Secure
Auditable
```

# 12. IAM Governance Principles

IAM governance should be:

```text
Accountable
Risk-Based
Policy-Driven
Architecture-Led
Evidence-Based
Continuously Improved
```

# 13. Authentication Principles

Authentication should be:

```text
Strong
Risk-Based
Context-Aware where Appropriate
Phishing-Resistant where Appropriate
Monitored
Recoverable
```

# 14. Authorization Principles

Authorization should be:

```text
Least-Privilege
Need-to-Know
Role-Based where Appropriate
Attribute-Based where Appropriate
Separation-of-Duties Aware
Time-Bounded where Appropriate
```

# 15. Identity Lifecycle

Identity management should integrate:

```text
Request
 ↓
Verify
 ↓
Create
 ↓
Provision
 ↓
Use
 ↓
Review
 ↓
Change
 ↓
Suspend
 ↓
Revoke
 ↓
Retain / Audit
```

# 16. IAM Governance

IAM governance should establish:

```text
Authority
Ownership
Identity Standards
Authentication Standards
Authorization Standards
Privileged Access
Lifecycle
Federation
Directory Services
Access Governance
Security
Risk
Assurance
Improvement
```

# 17. IAM Authority

IAM authority should define who may:

```text
Approve IAM Strategy
Approve IAM Architecture
Approve Authentication Standards
Approve Authorization Standards
Approve Privileged Access Standards
Approve Material Identity Exceptions
Accept Identity Risk
Approve Material Identity Architecture Changes
```

# 18. IAM Ownership

Material IAM services should have accountable owners for:

```text
Service
Availability
Security
Performance
Lifecycle
Compliance
Risk
Cost
```

# 19. Identity Types

Identity governance should distinguish, where applicable:

```text
Human Identity
Workforce Identity
Contractor Identity
Partner Identity
Customer Identity
Machine Identity
Application Identity
Service Identity
Device Identity
Privileged Identity
Emergency / Break-Glass Identity
```

# 20. Identity Uniqueness

Material identities should be uniquely identifiable within the relevant identity domain.

# 21. Identity Proofing

Identity proofing should establish sufficient confidence that an identity represents the claimed person, organization, machine or service.

# 22. Workforce Identity

Workforce identities should be linked to authoritative personnel or contractual records where appropriate.

# 23. Contractor Identity

Contractor identities should have:

```text
Sponsor
Organization
Purpose
Start Date
End Date
Access Scope
Review Requirement
```

# 24. External Identity

External identities should be governed according to:

```text
Relationship
Purpose
Trust
Risk
Access Scope
Lifecycle
```

# 25. Customer Identity

Where customer identity exists, it should have appropriate:

```text
Registration
Verification
Authentication
Consent / Privacy Controls where Applicable
Access
Recovery
Lifecycle
```

# 26. Machine Identity

Machine identities should have:

```text
Owner
Purpose
System
Credential / Trust Mechanism
Permissions
Expiry / Rotation
Monitoring
Lifecycle
```

# 27. Application Identity

Application identities should have:

```text
Owner
Purpose
Application
Permissions
Credential / Trust Mechanism
Monitoring
Lifecycle
```

# 28. Service Accounts

Service accounts should be:

```text
Owned
Purpose-Limited
Least-Privilege
Monitored
Rotated
Lifecycle-Controlled
```

# 29. Non-Human Identity Inventory

Material non-human identities should be inventoried.

Inventory may include:

```text
Identity
Type
Owner
Purpose
Application
System
Permissions
Credential
Expiry
Last Use
Lifecycle
```

# 30. Directory Services

Directory services should provide governed identity repositories and directory capabilities.

# 31. Directory Architecture

Directory architecture should address:

```text
Domains
Directories
Trusts
Replication
Availability
Security
Synchronization
Lifecycle
```

# 32. Directory Synchronization

Synchronization between authoritative sources and directories should be controlled and monitored.

# 33. Directory Security

Directory services should be:

```text
Hardened
Patched
Monitored
Access-Controlled
Resilient
Backed Up where Required
```

# 34. Identity Sources

Identity provisioning should use authoritative sources where possible.

# 35. Identity Reconciliation

Identity records should be periodically reconciled against authoritative sources.

# 36. Authentication

Authentication should verify:

```text
Identity
Credential
Context
Device / Session where Relevant
```

# 37. Authentication Factors

Authentication may use:

```text
Something You Know
Something You Have
Something You Are
Cryptographic / Phishing-Resistant Factors
```

# 38. Multi-Factor Authentication

MFA should be required for appropriate risk levels, particularly privileged and sensitive access.

# 39. Password Authentication

Where passwords are used, controls should address:

```text
Length
Complexity where Appropriate
Secure Storage
Rate Limiting
Lockout / Protection
Reset
Monitoring
```

# 40. Passwordless Authentication

Passwordless authentication should be considered where it improves security, usability and operational resilience.

# 41. Phishing-Resistant Authentication

Phishing-resistant mechanisms should be preferred for high-risk authentication where practical.

# 42. Adaptive Authentication

Risk-based authentication may consider:

```text
Location
Device
Behavior
Network
Application
Risk Signals
```

# 43. Single Sign-On

SSO should be used where appropriate to:

```text
Reduce Credential Exposure
Improve User Experience
Centralize Access Control
Improve Auditability
```

# 44. Federation

Identity federation should enable controlled trust between approved identity domains.

# 45. Federation Governance

Federation arrangements should define:

```text
Trust Relationship
Identity Provider
Service Provider
Claims
Authentication
Authorization
Security
Lifecycle
```

# 46. Federation Security

Federation should use approved protocols and security controls.

# 47. Claims Management

Federated claims should be:

```text
Purpose-Defined
Minimized
Accurate
Protected
Lifecycle-Controlled
```

# 48. Authorization

Authorization should determine what an authenticated identity may access or perform.

# 49. Role-Based Access Control

RBAC should be used where roles provide an effective representation of business responsibilities.

# 50. Attribute-Based Access Control

ABAC may be used where decisions require contextual attributes such as:

```text
User
Role
Location
Device
Data
Application
Time
Risk
```

# 51. Access Policies

Material access policies should define:

```text
Subject
Resource
Action
Conditions
Approval
Review
```

# 52. Least Privilege

Access should provide only the permissions necessary to perform authorized duties.

# 53. Separation of Duties

Conflicting responsibilities should be identified and controlled where appropriate.

# 54. Privileged Access

Privileged access includes access capable of:

```text
Changing Security
Changing Infrastructure
Changing Identity
Changing Applications
Accessing Sensitive Data
Circumventing Controls
```

# 55. Privileged Access Management

PAM should provide appropriate:

```text
Central Control
Approval
Credential Protection
Session Control
Monitoring
Recording where Required
Time Limitation
```

# 56. Privileged Account Inventory

Privileged accounts should be inventoried and reviewed.

# 57. Just-In-Time Privilege

Time-bounded or just-in-time privilege should be used where appropriate to reduce persistent administrative access.

# 58. Break-Glass Access

Emergency access should be:

```text
Restricted
Protected
Monitored
Tested
Reviewed
```

# 59. Emergency Access Review

Break-glass use should trigger appropriate review and evidence.

# 60. Access Requests

Access requests should identify:

```text
Requester
Subject
Resource
Role / Permission
Business Need
Duration
Approver
Risk
```

# 61. Access Approval

Approvals should be performed by authorized persons according to defined ownership and segregation requirements.

# 62. Access Provisioning

Approved access should be provisioned through controlled processes.

# 63. Automated Provisioning

Automated provisioning should be used where it improves accuracy, speed and control.

# 64. Access Changes

Access changes should be traceable to:

```text
Business Event
Request
Approval
Role Change
Risk Decision
```

# 65. Joiner Process

Joiner processes should ensure that new personnel receive only appropriate access.

# 66. Mover Process

Mover processes should identify and remove obsolete access when responsibilities change.

# 67. Leaver Process

Leaver processes should promptly:

```text
Disable Identity
Revoke Access
Revoke Sessions where Required
Recover Credentials / Devices where Relevant
Remove Privileges
Update Records
```

# 68. Identity Suspension

Suspension should be used where access must be temporarily blocked without full identity retirement.

# 69. Identity Deprovisioning

Deprovisioning should remove or disable access across relevant systems.

# 70. Dormant Accounts

Dormant identities should be identified and investigated.

# 71. Orphaned Accounts

Orphaned accounts should be identified, assigned ownership or removed.

# 72. Shared Accounts

Shared accounts should be avoided where practical.

Where unavoidable they should have:

```text
Business Justification
Owner
Compensating Controls
Access Monitoring
Periodic Review
```

# 73. Access Reviews

Material access should be periodically reviewed.

# 74. User Access Reviews

Reviews should verify:

```text
Identity
Role
Access
Business Need
Approver
Expiry
```

# 75. Privileged Access Reviews

Privileged access should receive enhanced periodic review.

# 76. Application Access Reviews

Material application access should be reviewed with application owners.

# 77. Data Access Reviews

Sensitive data access should be reviewed with data owners.

# 78. Recertification

Access recertification should produce evidence of:

```text
Review
Decision
Approver
Date
Revocation where Required
```

# 79. Identity Lifecycle

Identity lifecycle should cover:

```text
Creation
Provisioning
Use
Change
Review
Suspension
Deprovisioning
Retention
Audit
```

# 80. Credential Lifecycle

Credentials should be:

```text
Issued
Protected
Rotated
Revoked
Recovered where Required
Retired
```

# 81. Credential Storage

Credentials should be securely stored and never unnecessarily exposed.

# 82. Secrets Management

Secrets should be managed through approved mechanisms with:

```text
Ownership
Access Control
Rotation
Monitoring
Lifecycle
```

# 83. Certificate Management

Certificates should have:

```text
Owner
Purpose
Issuer
Expiry
Renewal
Revocation
Monitoring
```

# 84. Token Management

Tokens should have appropriate:

```text
Scope
Lifetime
Protection
Revocation
Monitoring
```

# 85. Session Management

Sessions should use appropriate:

```text
Timeout
Idle Timeout
Reauthentication
Token Protection
Revocation
Monitoring
```

# 86. Identity Security

Identity security should integrate:

```text
MFA
PAM
Conditional Access
Credential Protection
Threat Detection
Anomaly Detection
Access Reviews
Lifecycle Controls
```

# 87. Identity Threat Detection

Identity telemetry should support detection of:

```text
Credential Abuse
Password Spraying
Brute Force
Impossible Travel
MFA Abuse
Privilege Escalation
Suspicious Login
Token Theft
Session Hijacking
Dormant Account Abuse
Service Account Abuse
```

# 88. Identity Monitoring

Monitoring should cover:

```text
Authentication
Authorization
Privileged Access
Directory Changes
Federation
Provisioning
Deprovisioning
Credential Events
```

# 89. Identity Alerting

Alerts should be:

```text
Actionable
Prioritized
Owned
Escalated
Tuned
Reviewed
```

# 90. Identity Risk

Identity risk should consider:

```text
Privilege
Exposure
Credential Strength
Authentication Method
Lifecycle Status
Behavior
Data Access
Business Criticality
```

# 91. Identity Risk Scoring

Where appropriate, identity risk may combine:

```text
Identity Risk
Access Risk
Device Risk
Behavior Risk
Resource Risk
```

# 92. Identity Incidents

Identity incidents may include:

```text
Account Compromise
Credential Theft
MFA Abuse
Unauthorized Access
Privilege Escalation
Identity Provisioning Failure
Deprovisioning Failure
Federation Failure
Directory Failure
Service Account Compromise
```

# 93. Identity Incident Response

Response should integrate:

```text
Detect
 ↓
Triage
 ↓
Contain
 ↓
Revoke / Reset
 ↓
Investigate
 ↓
Recover
 ↓
Validate
 ↓
Learn
```

# 94. Credential Compromise Response

Potentially compromised credentials should be:

```text
Disabled / Revoked
Investigated
Reset / Rotated
Monitored
Documented
```

# 95. Identity Problem Management

Recurring identity failures should undergo root-cause analysis.

# 96. IAM Change Management

Material IAM changes should be:

```text
Requested
Assessed
Tested
Approved
Implemented
Validated
Recorded
```

# 97. IAM Change Impact

Impact analysis should consider:

```text
Users
Applications
Data
Infrastructure
Cloud
Security
Federation
Business Processes
Recovery
```

# 98. IAM Configuration Management

IAM configurations should be:

```text
Documented
Baselined
Controlled
Versioned where Appropriate
Recoverable
```

# 99. Identity Architecture Change

Material changes to:

```text
Directories
Authentication
Federation
PAM
Authorization
Provisioning
```

should receive architecture review appropriate to risk.

# 100. Identity Recovery

IAM recovery arrangements should define:

```text
Failure
Dependencies
Emergency Access
Recovery Sequence
RTO
Validation
```

# 101. IAM Resilience

Critical identity services should address:

```text
Directory Failure
Authentication Service Failure
Network Failure
Cloud Provider Failure
Federation Failure
Certificate Failure
```

# 102. Identity Recovery Testing

Critical IAM recovery should be tested periodically.

# 103. Identity Business Continuity

Identity dependencies should be included in business continuity and operational resilience planning.

# 104. IAM Supplier Management

Material IAM suppliers should be governed for:

```text
Security
Availability
Performance
Support
Continuity
Compliance
Lifecycle
Contract
Exit
```

# 105. Identity Provider Management

Identity providers should have documented:

```text
Trust
Availability
Security
Support
Recovery
Exit
```

# 106. IAM Licensing

IAM licensing should be monitored for:

```text
Entitlement
Usage
Cost
Renewal
Compliance
```

# 107. IAM Cost

IAM financial management should consider:

```text
Licensing
Platforms
MFA
PAM
Directory Services
Support
Integration
Professional Services
```

# 108. IAM Compliance

IAM services should comply with applicable:

```text
Policies
Standards
Contracts
Legal Requirements
Regulatory Requirements
```

# 109. IAM Compliance Monitoring

Compliance should be periodically assessed according to risk.

# 110. IAM Exceptions

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

# 111. IAM Remediation

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

# 112. IAM Assurance

Assurance may include:

```text
IAM Architecture Reviews
Identity Inventory Reviews
Access Reviews
Privileged Access Reviews
Authentication Reviews
Directory Reviews
Federation Reviews
Provisioning Reviews
Joiner / Mover / Leaver Reviews
Credential Reviews
Secrets Reviews
Certificate Reviews
Security Assessments
Penetration Testing where Appropriate
Recovery Tests
Supplier Reviews
Compliance Assessments
Internal Audit
Independent Assurance
```

# 113. IAM Testing

IAM testing may include:

```text
Authentication
Authorization
Provisioning
Deprovisioning
Privilege Escalation
Federation
Recovery
Security
Access Recertification
```

# 114. IAM Evidence

Evidence should support:

```text
Governance
Ownership
Identity Inventory
Identity Types
Identity Proofing
Directories
Synchronization
Authentication
MFA
SSO
Federation
Claims
Authorization
RBAC
ABAC
Least Privilege
Separation of Duties
PAM
Privileged Accounts
Break-Glass
Access Requests
Approvals
Provisioning
Joiner
Mover
Leaver
Access Reviews
Recertification
Credentials
Secrets
Certificates
Tokens
Sessions
Identity Security
Monitoring
Threat Detection
Incidents
Changes
Recovery
Suppliers
Licensing
Cost
Compliance
Exceptions
Remediation
Assurance
```

# 115. IAM Metrics

Metrics may include:

```text
Identity Inventory Coverage
Identity Ownership Coverage
Authoritative Source Coverage
Identity Reconciliation Success
MFA Coverage
Phishing-Resistant Authentication Coverage
SSO Coverage
Federation Coverage
Privileged Account Inventory Coverage
Privileged Access Review Completion
Just-In-Time Privilege Coverage
Break-Glass Account Review Completion
Service Account Ownership Coverage
Machine Identity Ownership Coverage
Dormant Account Count
Orphaned Account Count
Shared Account Count
Joiner Provisioning Success
Mover Deprovisioning Success
Leaver Deprovisioning SLA
Access Request SLA
Access Approval SLA
Automated Provisioning Coverage
Access Recertification Completion
Access Revocation Timeliness
Excessive Privilege Findings
Segregation-of-Duties Conflicts
Credential Rotation Compliance
Secrets Rotation Compliance
Certificate Renewal Compliance
Authentication Failure Rate
Suspicious Authentication Events
Identity Security Alerts
Identity Incident Volume
Compromised Identity Count
Mean Time to Contain Identity Incident
Mean Time to Restore IAM Service
IAM Availability
Directory Availability
Federation Availability
Recovery Test Success
RTO Achievement
IAM Change Success Rate
Emergency IAM Change Rate
IAM Vulnerability Exposure
Critical IAM Vulnerability Age
Supplier SLA Achievement
IAM License Compliance
IAM Cost Variance
IAM Risk Exposure
Exception Age
Remediation Completion
IAM Assurance Findings
```

# 116. IAM Dashboard

May include:

```text
Identity Health
Identity Inventory
Authentication
MFA
SSO
Federation
Authorization
Privileged Access
Lifecycle
Joiner / Mover / Leaver
Access Reviews
Service Accounts
Machine Identities
Credentials
Secrets
Certificates
Identity Security
Threat Detection
Incidents
Availability
Recovery
Changes
Suppliers
Licensing
Cost
Risk
Compliance
Assurance
```

# 117. Daily Review

Where appropriate:

```text
Critical Authentication Alerts
Compromised Identity Alerts
Privileged Access Alerts
MFA Abuse
Directory Failures
Federation Failures
Provisioning Failures
Deprovisioning Failures
Certificate Expiry
Identity Provider Incidents
```

# 118. Weekly Review

May consider:

```text
Identity Incidents
Authentication Trends
MFA Coverage
Privileged Access
Dormant Accounts
Orphaned Accounts
Provisioning
Deprovisioning
Access Reviews
Credential Rotation
Secrets
Certificates
Security Findings
Supplier Issues
Open Remediation
```

# 119. Monthly Review

May consider:

```text
IAM Governance
Identity Architecture
Identity Inventory
Authentication
Authorization
PAM
Lifecycle
Directories
Federation
Access Governance
Identity Security
Monitoring
Incidents
Changes
Recovery
Suppliers
Licensing
Cost
Risk
Compliance
Exceptions
Remediation
Assurance
```

# 120. Quarterly Review

May consider:

```text
Identity Strategy
IAM Architecture
Authentication Strategy
Authorization Model
PAM Strategy
Identity Lifecycle
Federation
Directory Strategy
Access Governance
Identity Security
Resilience
Recovery
Supplier Risk
Licensing
Cost
Compliance
Assurance
Maturity
```

# 121. Annual Review

May consider:

```text
Identity Strategy
Operating Model
Governance
Architecture
Identity Types
Inventory
Identity Proofing
Directories
Authentication
MFA
SSO
Federation
Authorization
RBAC
ABAC
PAM
Lifecycle
Joiner / Mover / Leaver
Access Reviews
Credentials
Secrets
Certificates
Identity Security
Monitoring
Threat Detection
Incidents
Changes
Resilience
Recovery
Suppliers
Licensing
Cost
Compliance
Exceptions
Remediation
Assurance
Maturity
Improvement
```

# 122. IAM Maturity

Identity capability maturity should be periodically assessed.

# 123. Maturity Dimensions

Assess:

```text
Governance
Strategy
Authority
Ownership
Identity Types
Identity Uniqueness
Identity Proofing
Workforce Identity
Contractor Identity
External Identity
Customer Identity
Machine Identity
Application Identity
Service Accounts
Non-Human Identity Inventory
Directory Services
Directory Architecture
Synchronization
Directory Security
Identity Sources
Identity Reconciliation
Authentication
Authentication Factors
MFA
Password Controls
Passwordless
Phishing-Resistant Authentication
Adaptive Authentication
SSO
Federation
Federation Governance
Federation Security
Claims
Authorization
RBAC
ABAC
Access Policies
Least Privilege
Separation of Duties
PAM
Privileged Account Inventory
Just-In-Time Privilege
Break-Glass
Access Requests
Access Approval
Access Provisioning
Automated Provisioning
Access Changes
Joiner
Mover
Leaver
Suspension
Deprovisioning
Dormant Accounts
Orphaned Accounts
Shared Accounts
Access Reviews
User Access Reviews
Privileged Access Reviews
Application Access Reviews
Data Access Reviews
Recertification
Identity Lifecycle
Credential Lifecycle
Credential Storage
Secrets Management
Certificate Management
Token Management
Session Management
Identity Security
Threat Detection
Monitoring
Alerting
Identity Risk
Risk Scoring
Identity Incidents
Incident Response
Credential Compromise
Problem Management
IAM Change Management
Configuration Management
Identity Architecture Change
Identity Recovery
IAM Resilience
Recovery Testing
Business Continuity
Supplier Management
Identity Provider Management
Licensing
Cost
Compliance
Exceptions
Remediation
Assurance
Testing
Evidence
Metrics
Improvement
```

# 124. Maturity Levels

```text
1 – Initial
2 – Repeatable
3 – Defined
4 – Managed
5 – Optimized
```

# 125. Identity Architecture Quality Gate

```text
Business Requirement
 ↓
Identity Requirement
 ↓
Identity Type
 ↓
Authoritative Source
 ↓
Authentication
 ↓
Authorization
 ↓
Security
 ↓
Lifecycle
 ↓
Monitoring
 ↓
Recovery
 ↓
Assurance
```

must be controlled.

# 126. Authentication Quality Gate

```text
Access Risk
 ↓
Identity
 ↓
Authentication Method
 ↓
MFA where Required
 ↓
Context / Device where Relevant
 ↓
Session
 ↓
Monitoring
 ↓
Recovery
```

must be controlled.

# 127. Authorization Quality Gate

```text
Business Need
 ↓
Identity
 ↓
Resource
 ↓
Role / Attribute
 ↓
Least Privilege
 ↓
Separation of Duties
 ↓
Approval
 ↓
Provisioning
 ↓
Review
 ↓
Revocation
```

must be controlled.

# 128. Privileged Access Quality Gate

```text
Business Need
 ↓
Privileged Identity
 ↓
Approval
 ↓
Strong Authentication
 ↓
Just-In-Time where Appropriate
 ↓
Session Control
 ↓
Monitoring
 ↓
Review
 ↓
Revocation
```

must be controlled.

# 129. Joiner / Mover / Leaver Quality Gate

```text
Authoritative Event
 ↓
Identity Update
 ↓
Access Assessment
 ↓
Approval where Required
 ↓
Provision / Change / Revoke
 ↓
Validation
 ↓
Record
 ↓
Review
```

must be controlled.

# 130. IAM Recovery Quality Gate

```text
Failure
 ↓
Assess
 ↓
Activate Recovery
 ↓
Restore Directory / IAM Services
 ↓
Restore Dependencies
 ↓
Validate Authentication
 ↓
Validate Authorization
 ↓
Validate Privileged Access
 ↓
Validate RTO
 ↓
Communicate
 ↓
Review
```

must be controlled.

# 131. IAM Assurance Quality Gate

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

# 132. Definition of Ready

An identity architecture, authentication method, authorization model, privileged-access arrangement, directory service, federation trust, access request, access review, identity lifecycle process, credential mechanism, secret, certificate, IAM change, recovery arrangement, supplier decision, exception, remediation or assurance review is Ready when purpose, identity type, owner, scope, dependencies, risk, security requirements, business need, lifecycle requirements, approval authority and acceptance criteria are defined.

# 133. Definition of Done

An IAM work item is Done when:

```text
Requirement / Identity Event Identified
        ↓
Owner Assigned
        ↓
IAM Action Completed
        ↓
Authentication / Authorization / Security / Lifecycle / Recovery Validation Completed where Required
        ↓
Identity / Access / Directory / Configuration / Monitoring / Asset / CMDB Records Updated
        ↓
Evidence Captured
        ↓
Findings / Exceptions Addressed
        ↓
Outcome Accepted
```

# 134. Final IAM Governance Principle

> **MFM must govern identity and access as a controlled enterprise security and business capability, ensuring that every material human, machine, application and external identity is appropriately established, authenticated, authorized, monitored, reviewed and lifecycle-controlled according to business need, risk and service requirements.**

# 135. Final Identity Principle

> **Every material identity must have a defined purpose, accountable owner, authoritative source, appropriate authentication, authorization and lifecycle controls.**

# 136. Final Authentication Principle

> **Authentication strength must be proportionate to access risk, with strong and phishing-resistant mechanisms preferred for privileged and sensitive access where practical.**

# 137. Final Authorization Principle

> **Access must be explicitly justified, least-privileged, appropriately approved, periodically reviewed and promptly revoked when no longer required.**

# 138. Final Privileged Access Principle

> **Privileged access must receive enhanced protection through strong authentication, controlled elevation, monitoring, accountability and time limitation where appropriate.**

# 139. Final Lifecycle Principle

> **Identity lifecycle controls must ensure that joiners receive appropriate access, movers lose obsolete access and leavers have access revoked promptly and comprehensively.**

# 140. Final Non-Human Identity Principle

> **Machine, application and service identities must be treated as governed identities with accountable ownership, purpose limitation, credential protection, monitoring and lifecycle management.**

# 141. Final Federation Principle

> **Federated identity relationships must use explicit trust, minimized claims, approved protocols, controlled authorization and lifecycle governance.**

# 142. Final Security Principle

> **Identity security must integrate MFA, privileged access management, credential protection, conditional access, monitoring, threat detection and lifecycle controls.**

# 143. Final Resilience Principle

> **Critical identity services must have resilient architecture and tested recovery capabilities aligned with business and service requirements.**

# 144. Final Assurance Principle

> **Material IAM controls and services must be supported by reliable evidence and periodically assessed through risk-based assurance.**

# 145. Final Improvement Principle

> **Identity incidents, excessive privileges, lifecycle failures, authentication weaknesses, security findings, recovery results and assurance findings must continuously improve MFM's identity capability.**

# 146. Final Enterprise IAM Integration Principle

> **Identity Architecture and Operations must integrate with Enterprise Architecture, Applications, Data, Infrastructure, Network, Cloud, Cybersecurity, IT Service Management, Configuration Management, Asset Management, Finance, Suppliers, Risk, Compliance, Legal and Business Continuity.**

# 147. Final Steady-State IAM Principle

> **MFM must govern identity and access as a controlled enterprise security and business capability, ensuring that every material human, machine, application and external identity is appropriately established, authenticated, authorized, monitored, reviewed and lifecycle-controlled according to business need, risk and service requirements.**

# 148. Summary

MFM v1.2-Steady-State-130 establishes the permanent Enterprise Identity & Access Management Architecture and IAM Operations baseline.

It defines:

- Identity Strategy / IAM Governance / Authority / Ownership
- Identity Types / Uniqueness / Identity Proofing
- Workforce / Contractor / External / Customer Identity
- Machine / Application / Service Identities
- Non-Human Identity Inventory
- Directory Services / Directory Architecture / Synchronization / Directory Security
- Identity Sources / Reconciliation
- Authentication / Authentication Factors / MFA
- Password / Passwordless / Phishing-Resistant / Adaptive Authentication
- SSO / Federation / Federation Governance / Federation Security / Claims
- Authorization / RBAC / ABAC / Access Policies
- Least Privilege / Separation of Duties
- Privileged Access / PAM / Privileged Account Inventory
- Just-In-Time Privilege / Break-Glass Access
- Access Requests / Approvals / Provisioning / Automated Provisioning
- Joiner / Mover / Leaver / Suspension / Deprovisioning
- Dormant / Orphaned / Shared Accounts
- Access Reviews / Privileged Reviews / Application Reviews / Data Reviews / Recertification
- Identity / Credential / Secret / Certificate / Token / Session Lifecycle
- Identity Security / Threat Detection / Monitoring / Alerting
- Identity Risk / Risk Scoring
- Identity Incidents / Credential Compromise / Problem Management
- IAM Change / Configuration / Architecture Change
- Identity Recovery / IAM Resilience / Recovery Testing / Business Continuity
- IAM Supplier Management / Identity Provider Management
- Licensing / Cost
- Compliance / Exceptions / Remediation
- IAM Assurance / Testing / Evidence
- IAM Metrics / IAM Dashboard
- Daily / Weekly / Monthly / Quarterly / Annual Reviews
- IAM Maturity
- Identity Architecture / Authentication / Authorization / Privileged Access / Joiner-Mover-Leaver / Recovery / Assurance Quality Gates
- Definition of Ready
- Definition of Done

# 149. Next Document

**MFM v1.2-Steady-State-131 – Enterprise Service Management Architecture, ITSM Governance, Service Portfolio, Service Catalogue, Incident Management, Problem Management, Request Management, Change Management, Release Management, Configuration Management, Asset Management, Knowledge Management, Service Continuity & ITSM Assurance**

It shall establish the permanent enterprise operating model for service-management strategy, ITSM governance, service portfolio, service catalogue, service ownership, service-level management, incident management, major incident management, problem management, request fulfilment, change management, release management, configuration management, asset management, knowledge management, event management, service monitoring, service continuity, service reporting, ITSM suppliers, ITSM compliance, ITSM exceptions, remediation, ITSM assurance, metrics, dashboards, maturity and continual enterprise service-management capability improvement supporting MFM.

# 150. Document Control

**Document:** MFM v1.2-Steady-State-130  
**Version:** 1.2  
**Status:** Steady-State Enterprise Identity & Access Management Architecture & Operations Baseline  
**Previous Document:** MFM v1.2-Steady-State-129  
**Next Document:** MFM v1.2-Steady-State-131  
**Lifecycle:** Steady-State Operation  
**IAM Governance Authority:** Enterprise Identity & Access Management  
**Identity Architecture Authority:** Enterprise Identity Architecture  
**Authentication Authority:** Identity and Access Management  
**Authorization Authority:** Access Governance / IAM  
**Privileged Access Authority:** Privileged Access Management  
**Directory Authority:** Directory Services Management  
**Federation Authority:** Identity Federation Management  
**Lifecycle Authority:** Identity Lifecycle Management  
**Identity Security Authority:** Enterprise Cybersecurity / Identity Security  
**Application Authority:** Enterprise Application Architecture  
**Data Authority:** Enterprise Data Management  
**Infrastructure Authority:** Enterprise Infrastructure Architecture  
**Network Authority:** Enterprise Network Architecture  
**Cloud Authority:** Enterprise Cloud Architecture  
**Service Authority:** Enterprise IT Service Management  
**Configuration Authority:** Configuration Management  
**Asset Authority:** Enterprise Asset Management  
**Supplier Authority:** Supplier / Third-Party Management  
**Finance Authority:** Financial Management / Technology Financial Management  
**Risk Authority:** Enterprise Risk Management  
**Compliance Authority:** Enterprise Compliance  
**Legal Authority:** Legal / Regulatory Affairs  
**Continuity Authority:** Business Continuity / Operational Resilience  
**Assurance Authority:** IAM Assurance / Internal Audit / Independent Assurance  
**Improvement Authority:** Continual Enterprise Identity Capability Improvement  

**Principle:** MFM must govern identity and access as a controlled enterprise security and business capability, ensuring that every material human, machine, application and external identity is appropriately established, authenticated, authorized, monitored, reviewed and lifecycle-controlled according to business need, risk and service requirements.
