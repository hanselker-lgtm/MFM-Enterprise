# MFM v1.2-Steady-State-123
## Enterprise Identity & Access Management Architecture, IAM Governance, Authentication, Authorization, Privileged Access, Identity Lifecycle & IAM Assurance

**Version:** 1.2  
**Document ID:** MFM v1.2-Steady-State-123  
**Status:** Steady-State Enterprise Identity & Access Management Baseline  
**Lifecycle:** Post-Implementation / Steady-State Operation  
**Document Type:** Identity Architecture / IAM Governance / Authentication / Authorization / Privileged Access / Identity Lifecycle / IAM Assurance Document  

---

# 1. Purpose

This document establishes the one-hundred-and-twenty-third document in the MFM v1.2 Steady-State series.

It follows MFM v1.2-Steady-State-122 – Enterprise Integration Architecture, Integration Governance, API & Event Integration, Messaging, Data Exchange, Integration Operations & Integration Assurance.

The purpose is to establish the permanent enterprise operating model for identity strategy, IAM governance, identity architecture, directories, federation, authentication, authorization, role management, privileged access, service identities, machine identities, secrets, identity lifecycle, joiner/mover/leaver processes, access requests, access reviews, segregation of duties, identity security, identity incidents, identity changes, identity resilience, identity suppliers, identity compliance, identity exceptions, remediation, IAM assurance, metrics, dashboards, maturity and continual enterprise identity capability improvement.

The central objective is:

> **MFM must govern identity and access as a foundational enterprise security capability, ensuring that every material human, privileged, service and machine identity is appropriately established, authenticated, authorized, monitored, reviewed and removed throughout its complete lifecycle.**

---

# 2. Scope

This document covers:

- Identity Strategy
- IAM Governance
- Identity Architecture
- Directories
- Federation
- Authentication
- Authorization
- Role Management
- Privileged Access
- Service Identities
- Machine Identities
- Secrets
- Identity Lifecycle
- Joiner / Mover / Leaver
- Access Requests
- Access Reviews
- Segregation of Duties
- Identity Security
- Identity Incidents
- Identity Changes
- Identity Resilience
- Identity Suppliers
- Identity Compliance
- Identity Exceptions
- Identity Remediation
- IAM Assurance
- IAM Metrics
- IAM Dashboards
- IAM Maturity
- Continual Enterprise Identity Capability Improvement

---

# 3. Identity Governance Objective

The primary objective is:

> **Establish clear authority, ownership, standards, lifecycle controls, security requirements, access responsibilities and assurance for enterprise identities and access.**

# 4. IAM Architecture Objective

The primary objective is:

> **Provide a coherent enterprise identity architecture that enables trusted authentication, controlled authorization, lifecycle management, federation and secure access across applications, infrastructure, cloud, data and services.**

# 5. Authentication Objective

The primary objective is:

> **Verify identity reliably using authentication mechanisms proportionate to risk and access sensitivity.**

# 6. Authorization Objective

The primary objective is:

> **Ensure access is explicitly authorized according to business need, least privilege, role, context and risk.**

# 7. Privileged Access Objective

The primary objective is:

> **Control privileged access through stronger authentication, approval, time limitation, monitoring, accountability and periodic review.**

# 8. Identity Lifecycle Objective

The primary objective is:

> **Ensure identities and access rights are created, changed, reviewed, suspended and removed accurately and promptly throughout the identity lifecycle.**

# 9. IAM Assurance Objective

The primary objective is:

> **Provide evidence that identity governance, authentication, authorization, privileged access and lifecycle controls operate effectively.**

# 10. Identity Principles

Identity should be:

```text
Unique
Owned
Verified
Authenticated
Authorized
Monitored
Reviewed
Lifecycle-Controlled
```

# 11. IAM Governance Principles

IAM governance should be:

```text
Accountable
Risk-Based
Least-Privilege
Business-Aligned
Evidence-Based
Continuously Improved
```

# 12. Authentication Principles

Authentication should be:

```text
Strong
Risk-Based
Phishing-Resistant where Appropriate
Multi-Factor where Required
Monitored
Auditable
```

# 13. Authorization Principles

Authorization should be:

```text
Explicit
Least-Privilege
Need-to-Know
Role / Attribute-Based
Time-Bounded where Appropriate
Reviewed
```

# 14. Privileged Access Principles

Privileged access should be:

```text
Minimized
Separated
Strongly Authenticated
Approved
Monitored
Recorded
Periodically Reviewed
```

# 15. Identity Lifecycle

Identity management should integrate:

```text
Request / Source
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
Remove
```

# 16. IAM Governance

IAM governance should establish:

```text
Authority
Ownership
Identity Standards
Authentication
Authorization
Privileged Access
Lifecycle
Security
Risk
Assurance
Improvement
```

# 17. IAM Authority

IAM authority should define who may:

```text
Approve Identity Strategy
Approve IAM Architecture
Approve Authentication Standards
Approve Authorization Models
Approve Privileged Access Policies
Approve Material IAM Exceptions
Accept Identity Risk
```

# 18. IAM Ownership

Material IAM capabilities should have accountable owners for:

```text
Architecture
Identity Data
Authentication
Authorization
Privileged Access
Lifecycle
Security
Availability
Compliance
Risk
```

# 19. Identity Inventory

Material identities and identity objects should be inventoried.

Inventory may include:

```text
Human Identities
Privileged Identities
Service Identities
Machine Identities
Application Identities
External Identities
Federated Identities
Groups
Roles
Credentials
Certificates
Secrets
```

# 20. Identity Source of Truth

Authoritative identity sources should be defined for relevant identity populations.

# 21. Human Identity

Human identities should have:

```text
Unique Identifier
Owner / Employer Relationship
Status
Attributes
Source
Lifecycle
Access
```

# 22. Identity Uniqueness

Each material human identity should be uniquely identifiable.

# 23. Identity Proofing

Identity proofing should establish sufficient confidence in identity according to risk.

# 24. External Identity

External identities should be governed for:

```text
Purpose
Sponsor
Organization
Access
Expiry
Review
```

# 25. Guest Identity

Guest identities should have explicit ownership and lifecycle controls.

# 26. Identity Federation

Federation should provide controlled trust between approved identity domains.

# 27. Federation Governance

Federated relationships should define:

```text
Trust Owner
Provider
Consumer
Attributes
Authentication Assurance
Authorization
Logging
Lifecycle
```

# 28. Single Sign-On

Where appropriate, SSO should reduce credential proliferation while preserving appropriate security controls.

# 29. Directory Services

Directory services should have:

```text
Owner
Architecture
Replication
Availability
Security
Backup
Recovery
Lifecycle
```

# 30. Directory Data

Directory attributes should be governed for:

```text
Accuracy
Ownership
Purpose
Privacy
Retention
```

# 31. Authentication

Authentication should use approved mechanisms appropriate to risk.

# 32. Multi-Factor Authentication

MFA should be required for material privileged, administrative and sensitive access according to risk and policy.

# 33. Strong Authentication

Higher-risk access should use stronger authentication methods where appropriate.

# 34. Password Governance

Where passwords remain in use, controls should address:

```text
Complexity
Protection
Reset
Lockout
Reuse
Exposure
Monitoring
```

# 35. Passwordless Authentication

Passwordless or phishing-resistant authentication should be considered for suitable high-risk use cases.

# 36. Authentication Assurance

Authentication assurance should be appropriate to:

```text
Data Sensitivity
Business Criticality
Privilege
Threat Exposure
Access Context
```

# 37. Adaptive Authentication

Where supported, authentication decisions may consider:

```text
Device
Location
Behavior
Risk
Session
Network
```

# 38. Session Management

Sessions should have appropriate:

```text
Timeout
Reauthentication
Revocation
Monitoring
```

# 39. Authentication Logging

Material authentication events should be logged according to risk.

# 40. Authorization

Authorization should define what an authenticated identity may access or perform.

# 41. Role-Based Access Control

RBAC should be used where suitable.

# 42. Attribute-Based Access Control

ABAC may be used where contextual or attribute-based decisions provide value.

# 43. Least Privilege

Access should be limited to the minimum required permissions.

# 44. Need-to-Know

Sensitive information should only be accessible where legitimate business need exists.

# 45. Separation of Duties

Conflicting responsibilities should be separated where required to reduce fraud, error and abuse risk.

# 46. Role Governance

Roles should have:

```text
Owner
Purpose
Permissions
Eligibility
Approval
Review
Lifecycle
```

# 47. Group Governance

Groups should have:

```text
Owner
Purpose
Membership Rules
Approval
Review
Lifecycle
```

# 48. Access Entitlements

Material entitlements should be:

```text
Defined
Owned
Approved
Reviewable
Traceable
```

# 49. Access Request

Access requests should include:

```text
Requester
Identity
Resource
Role / Entitlement
Business Need
Duration
Approver
```

# 50. Access Approval

Approval should be performed by appropriate accountable authority.

# 51. Access Provisioning

Provisioning should be controlled and automated where practical.

# 52. Access Deprovisioning

Access should be removed promptly when:

```text
Employment Ends
Role Changes
Contract Ends
Business Need Ends
Access Expires
Risk Requires Removal
```

# 53. Joiner Process

Joiner processes should establish:

```text
Identity
Attributes
Baseline Access
Authentication
Required Applications
Required Roles
```

# 54. Mover Process

Mover processes should remove obsolete access and provision new access based on the new role.

# 55. Leaver Process

Leaver processes should:

```text
Disable Identity
Revoke Sessions
Remove Access
Revoke Privileges
Recover Credentials / Assets where Relevant
Retain Required Records
```

# 56. Lifecycle Timeliness

Joiner, mover and leaver processes should meet defined service expectations.

# 57. Privileged Access Management

Privileged access should be centrally governed where appropriate.

# 58. Privileged Account Types

Examples include:

```text
Administrator
Root
Domain Administrator
Database Administrator
Cloud Administrator
Security Administrator
Application Administrator
Emergency / Break-Glass
```

# 59. Privileged Account Separation

Administrative activity should use separate privileged identities where appropriate.

# 60. Privileged Authentication

Privileged access should use strong authentication and enhanced controls.

# 61. Just-in-Time Access

Where supported and justified, privileged access should be time-bound.

# 62. Privileged Approval

Material privileged access should require appropriate authorization.

# 63. Privileged Session Monitoring

Privileged sessions should be monitored or recorded where required by risk and policy.

# 64. Break-Glass Access

Emergency access should be:

```text
Protected
Restricted
Monitored
Logged
Reviewed
```

# 65. Service Identities

Service identities should have:

```text
Owner
Purpose
Application / Service
Permissions
Credential Method
Lifecycle
Monitoring
```

# 66. Machine Identities

Machine identities should be governed similarly to service identities.

# 67. Workload Identity

Cloud and application workloads should use managed or securely controlled workload identities where appropriate.

# 68. Non-Human Identity Inventory

Non-human identities should be included in IAM inventory and lifecycle governance.

# 69. Service Account Privileges

Service accounts should receive only required permissions.

# 70. Service Credential Rotation

Service credentials should be rotated according to risk and policy.

# 71. Secrets Management

Secrets should be stored using approved secure mechanisms.

# 72. Secret Types

Secrets may include:

```text
Passwords
API Keys
Tokens
Private Keys
Connection Strings
Certificates
Encryption Keys
```

# 73. Secret Exposure

Secrets should not be embedded in:

```text
Source Code
Logs
Tickets
Documentation
Unprotected Configuration
```

# 74. Credential Lifecycle

Credentials should be:

```text
Issued
Protected
Rotated
Revoked
Expired
Destroyed
```

# 75. Certificate Identity

Certificates used for identity or authentication should have:

```text
Owner
Purpose
Subject
Expiry
Renewal
Revocation
Monitoring
```

# 76. Identity Security

IAM security should protect against:

```text
Credential Theft
Account Takeover
Privilege Escalation
Unauthorized Access
Identity Abuse
Persistence
```

# 77. Identity Threat Detection

Identity monitoring should detect relevant:

```text
Impossible Travel
Abnormal Login
Privilege Escalation
Credential Abuse
Mass Authentication Failures
Suspicious Federation
Unusual Administrative Activity
```

# 78. Identity Risk

Identity risk should consider:

```text
Privilege
Sensitivity
Exposure
Authentication Strength
Behavior
Access Scope
Lifecycle Status
```

# 79. Identity Monitoring

Critical identity activity should be monitored.

# 80. Identity Logging

Material identity events should be logged, including where appropriate:

```text
Authentication
Authorization
Provisioning
Deprovisioning
Role Changes
Privilege Changes
Credential Changes
Federation Events
Administrative Actions
```

# 81. Identity Incident Management

Identity incidents should integrate with enterprise security and ITSM processes.

# 82. Identity Incident Types

Examples include:

```text
Account Compromise
Credential Theft
Unauthorized Access
Privilege Abuse
Authentication Failure
Federation Failure
Directory Failure
Provisioning Failure
```

# 83. Identity Incident Response

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

# 84. Identity Recovery

Identity recovery should address:

```text
Directory Failure
Authentication Platform Failure
Federation Failure
Credential Recovery
Backup
Recovery
Failover
```

# 85. IAM Resilience

Critical IAM capabilities should have appropriate:

```text
Redundancy
Replication
Failover
Backup
Recovery
Monitoring
```

# 86. IAM Recovery Testing

Critical IAM recovery should be tested periodically according to risk.

# 87. Identity Change Management

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

# 88. IAM Configuration

IAM configuration should be:

```text
Documented
Version-Controlled where Appropriate
Access-Controlled
Reviewed
Recoverable
```

# 89. IAM Automation

Identity provisioning, access changes and policy enforcement should be automated where practical.

# 90. Identity Governance Automation

Automation may support:

```text
Joiner
Mover
Leaver
Access Requests
Approvals
Provisioning
Deprovisioning
Reviews
```

# 91. Access Reviews

Access reviews should confirm:

```text
Business Need
Correct Role
Appropriate Privilege
Current Employment / Relationship
Appropriate Data Access
```

# 92. Privileged Access Reviews

Privileged access should be reviewed more frequently according to risk.

# 93. Service Identity Reviews

Service and machine identities should be periodically reviewed for:

```text
Owner
Purpose
Permissions
Usage
Credential Status
Lifecycle
```

# 94. Dormant Identities

Dormant or unused identities should be identified and appropriately disabled or retired.

# 95. Orphaned Accounts

Orphaned accounts should be identified and remediated promptly.

# 96. Identity Reconciliation

Identity records should be reconciled between authoritative sources and downstream systems where appropriate.

# 97. Identity Data Quality

Identity data should be:

```text
Accurate
Complete
Consistent
Timely
Unique
```

# 98. Identity Compliance

IAM should comply with applicable:

```text
Policies
Standards
Contracts
Legal Requirements
Regulatory Requirements
```

# 99. IAM Compliance Monitoring

Compliance should be periodically assessed according to risk.

# 100. IAM Exceptions

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

# 101. IAM Remediation

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

# 102. IAM Assurance

Assurance may include:

```text
IAM Architecture Reviews
Identity Inventory Reviews
Authentication Reviews
Authorization Reviews
Privileged Access Reviews
Joiner / Mover / Leaver Testing
Access Reviews
SoD Reviews
Service Identity Reviews
Secrets Reviews
Certificate Reviews
Federation Reviews
Identity Security Assessments
Recovery Tests
Supplier Reviews
Compliance Assessments
Internal Audit
Independent Assurance
```

# 103. IAM Evidence

Evidence should support:

```text
Governance
Ownership
Identity Inventory
Identity Sources
Federation
Authentication
MFA
Authorization
Roles
Groups
Entitlements
Access Requests
Approvals
Provisioning
Deprovisioning
Privileged Access
Service Identities
Machine Identities
Secrets
Certificates
Monitoring
Logging
Incidents
Changes
Recovery
Compliance
Exceptions
Remediation
Assurance
```

# 104. IAM Metrics

Metrics may include:

```text
Identity Inventory Coverage
Human Identity Coverage
External Identity Coverage
Service Identity Coverage
Machine Identity Coverage
MFA Coverage
Strong Authentication Coverage
Passwordless Adoption where Applicable
Authentication Failure Rate
Privileged Account Inventory Coverage
Privileged MFA Coverage
Privileged Access Review Completion
JML Completion Time
JML Accuracy
Access Request SLA Achievement
Access Approval SLA Achievement
Access Provisioning SLA Achievement
Access Deprovisioning SLA Achievement
Access Review Completion
Role Certification Completion
SoD Violation Volume
Orphaned Account Count
Dormant Account Count
Inactive Identity Count
Service Identity Review Completion
Credential Rotation Compliance
Secret Rotation Compliance
Certificate Expiry Risk
Federation Availability
Identity Incident Volume
Account Compromise Volume
Privilege Escalation Events
Mean Time to Contain Identity Incidents
IAM Availability
IAM Recovery Test Success
RTO Achievement
RPO Achievement
IAM Change Success Rate
IAM Automation Coverage
IAM Compliance
IAM Risk Exposure
Exception Age
Remediation Completion
IAM Assurance Findings
```

# 105. IAM Dashboard

May include:

```text
Identity Health
Identity Inventory
Authentication
MFA
Authorization
Roles
Groups
Privileged Access
Service Identities
Machine Identities
Secrets
Certificates
Lifecycle
JML
Access Requests
Access Reviews
SoD
Security
Incidents
Recovery
Compliance
Risk
Assurance
```

# 106. Daily Review

Where appropriate:

```text
Critical Authentication Alerts
Account Compromise
Privileged Activity
Identity Security Alerts
Directory Failures
Federation Failures
Provisioning Failures
Certificate Alerts
```

# 107. Weekly Review

May consider:

```text
Identity Incidents
Authentication Trends
Privileged Activity
Access Changes
JML Performance
Provisioning Failures
Dormant Accounts
Security Findings
Certificate Status
Open Remediation
```

# 108. Monthly Review

May consider:

```text
IAM Governance
Identity Inventory
Authentication
MFA
Authorization
Roles
Groups
Privileged Access
Service Identities
Lifecycle
Access Requests
Access Reviews
SoD
Secrets
Certificates
Security
Incidents
Recovery
Compliance
Risk
Assurance
```

# 109. Quarterly Review

May consider:

```text
Identity Strategy
Architecture
IAM Platform
Authentication Strategy
Authorization Model
Privileged Access
Identity Lifecycle
Federation
Service / Machine Identity Strategy
Security
Resilience
Supplier Risk
Compliance
Assurance
Maturity
```

# 110. Annual Review

May consider:

```text
Identity Strategy
Operating Model
Governance
Architecture
Directories
Federation
Authentication
Authorization
Roles
Privileged Access
Service Identities
Machine Identities
Secrets
Certificates
Lifecycle
JML
Access Requests
Access Reviews
SoD
Security
Incidents
Resilience
Recovery
Suppliers
Compliance
Exceptions
Remediation
Assurance
Maturity
Improvement
```

# 111. IAM Maturity

Identity capability maturity should be periodically assessed.

# 112. Maturity Dimensions

Assess:

```text
Governance
Strategy
Authority
Ownership
Roles
Identity Inventory
Identity Sources
Human Identity
Identity Uniqueness
Identity Proofing
External Identity
Guest Identity
Federation
Federation Governance
Single Sign-On
Directory Services
Directory Data
Authentication
MFA
Strong Authentication
Password Governance
Passwordless
Authentication Assurance
Adaptive Authentication
Session Management
Authentication Logging
Authorization
RBAC
ABAC
Least Privilege
Need-to-Know
Separation of Duties
Role Governance
Group Governance
Entitlements
Access Requests
Access Approval
Provisioning
Deprovisioning
Joiner
Mover
Leaver
Lifecycle Timeliness
Privileged Access Management
Privileged Accounts
Privileged Separation
Privileged Authentication
Just-in-Time Access
Privileged Approval
Session Monitoring
Break-Glass
Service Identities
Machine Identities
Workload Identity
Non-Human Identity
Service Privileges
Credential Rotation
Secrets Management
Certificate Identity
Identity Security
Threat Detection
Identity Risk
Monitoring
Logging
Incident Management
Identity Recovery
IAM Resilience
Recovery Testing
Change Management
Configuration
Automation
Access Reviews
Privileged Reviews
Service Identity Reviews
Dormant Identities
Orphaned Accounts
Reconciliation
Identity Data Quality
Compliance
Exceptions
Remediation
Assurance
Evidence
Metrics
Improvement
```

# 113. Maturity Levels

```text
1 – Initial
2 – Repeatable
3 – Defined
4 – Managed
5 – Optimized
```

# 114. IAM Architecture Quality Gate

```text
Business Requirement
 ↓
Identity Requirement
 ↓
Identity Source
 ↓
Authentication
 ↓
Authorization
 ↓
Privileged Access
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

# 115. Authentication Quality Gate

```text
Identity
 ↓
Proofing
 ↓
Authentication Method
 ↓
Assurance Level
 ↓
MFA where Required
 ↓
Session
 ↓
Monitoring
 ↓
Review
```

must be controlled.

# 116. Access Quality Gate

```text
Business Need
 ↓
Identity
 ↓
Resource
 ↓
Role / Entitlement
 ↓
Least Privilege
 ↓
Approval
 ↓
Provision
 ↓
Monitor
 ↓
Review
 ↓
Remove
```

must be controlled.

# 117. Privileged Access Quality Gate

```text
Need
 ↓
Identity
 ↓
Privilege
 ↓
Approval
 ↓
Strong Authentication
 ↓
Time-Bound Access where Appropriate
 ↓
Monitor
 ↓
Record
 ↓
Review
```

must be controlled.

# 118. Joiner / Mover / Leaver Quality Gate

```text
Authoritative Event
 ↓
Identity Update
 ↓
Access Determination
 ↓
Provision / Modify / Revoke
 ↓
Validation
 ↓
Evidence
```

must be controlled.

# 119. Service Identity Quality Gate

```text
Purpose
 ↓
Owner
 ↓
Identity
 ↓
Permissions
 ↓
Credential / Trust
 ↓
Monitoring
 ↓
Rotation
 ↓
Review
 ↓
Retire
```

must be controlled.

# 120. IAM Recovery Quality Gate

```text
Failure
 ↓
Assess
 ↓
Activate Recovery
 ↓
Restore Identity Services
 ↓
Validate Authentication
 ↓
Validate Authorization
 ↓
Validate Dependencies
 ↓
Validate RTO / RPO
 ↓
Communicate
 ↓
Review
```

must be controlled.

# 121. IAM Assurance Quality Gate

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

An IAM architecture, identity source, authentication method, authorization model, role, entitlement, access request, privileged access arrangement, service identity, credential, secret, certificate, federation, lifecycle process, recovery arrangement, exception, remediation or assurance review is Ready when purpose, owner, scope, identity population, access requirement, risk, security requirements, lifecycle requirements, approval authority and acceptance criteria are defined.

# 123. Definition of Done

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
IAM / Identity / Access / Role / Audit / Monitoring Records Updated
        ↓
Evidence Captured
        ↓
Findings / Exceptions Addressed
        ↓
Outcome Accepted
```

# 124. Final IAM Governance Principle

> **MFM must govern identity and access as a foundational enterprise security capability, ensuring that every material human, privileged, service and machine identity is appropriately established, authenticated, authorized, monitored, reviewed and removed throughout its complete lifecycle.**

# 125. Final Identity Principle

> **Every material identity must be uniquely identifiable, owned, traceable and governed throughout its lifecycle.**

# 126. Final Authentication Principle

> **Authentication strength must be proportionate to access sensitivity, privilege, threat exposure and business risk.**

# 127. Final Authorization Principle

> **Access must be explicitly authorized according to business need, least privilege, need-to-know, role or attribute and risk.**

# 128. Final Privileged Access Principle

> **Privileged access must be minimized, separated, strongly authenticated, appropriately approved, monitored and periodically reviewed.**

# 129. Final Lifecycle Principle

> **Identity and access must be accurately provisioned, modified and removed in response to authoritative lifecycle events.**

# 130. Final Non-Human Identity Principle

> **Service, machine and workload identities must receive the same level of ownership, privilege control, credential protection, monitoring and lifecycle governance appropriate to their risk.**

# 131. Final Secrets Principle

> **Credentials, secrets, tokens, private keys and certificates must be securely stored, appropriately scoped, rotated, monitored and revoked throughout their lifecycle.**

# 132. Final Resilience Principle

> **Critical IAM services must have appropriate redundancy, recovery and tested continuity arrangements because identity failure can become enterprise-wide service failure.**

# 133. Final Assurance Principle

> **Material IAM controls must be supported by reliable evidence and periodically assessed through risk-based assurance.**

# 134. Final Improvement Principle

> **Identity incidents, access findings, orphaned accounts, privilege risks, lifecycle failures, authentication weaknesses and assurance results must continuously improve MFM's identity capability.**

# 135. Final Integration Principle

> **IAM Architecture and Operations must integrate with Enterprise Architecture, Applications, Data, Integration, Network, Infrastructure, Cloud, Cybersecurity, IT Service Management, HR / Workforce Processes, Asset Management, Suppliers, Finance, Risk, Compliance, Legal and Business Continuity.**

# 136. Final Steady-State Identity Principle

> **MFM must govern identity and access as a foundational enterprise security capability, ensuring that every material human, privileged, service and machine identity is appropriately established, authenticated, authorized, monitored, reviewed and removed throughout its complete lifecycle.**

# 137. Summary

MFM v1.2-Steady-State-123 establishes the permanent Enterprise Identity & Access Management Architecture and IAM Operations baseline.

It defines:

- Identity Strategy / IAM Governance / Authority / Ownership
- Identity Architecture / Identity Inventory / Identity Sources
- Human / External / Guest Identities
- Identity Proofing / Uniqueness
- Federation / Federation Governance / Single Sign-On
- Directory Services / Directory Data
- Authentication / MFA / Strong Authentication / Password Governance
- Passwordless / Authentication Assurance / Adaptive Authentication / Session Management
- Authorization / RBAC / ABAC / Least Privilege / Need-to-Know
- Separation of Duties / Role Governance / Group Governance / Entitlements
- Access Requests / Approval / Provisioning / Deprovisioning
- Joiner / Mover / Leaver
- Privileged Access Management / Privileged Accounts / JIT / Break-Glass
- Service Identities / Machine Identities / Workload Identity
- Non-Human Identity / Service Privileges / Credential Rotation
- Secrets Management / Certificates
- Identity Security / Threat Detection / Identity Risk
- Monitoring / Logging / Identity Incident Management
- Identity Recovery / IAM Resilience / Recovery Testing
- IAM Change Management / Configuration / Automation
- Access Reviews / Privileged Reviews / Service Identity Reviews
- Dormant / Orphaned Accounts / Identity Reconciliation / Data Quality
- Compliance / Exceptions / Remediation / Assurance / Evidence
- IAM Metrics / IAM Dashboard
- Daily / Weekly / Monthly / Quarterly / Annual Reviews
- IAM Maturity
- IAM Architecture / Authentication / Access / Privileged Access / JML / Service Identity / Recovery / Assurance Quality Gates
- Definition of Ready
- Definition of Done

# 138. Next Document

**MFM v1.2-Steady-State-124 – Enterprise Cybersecurity Architecture, Security Governance, Security Operations, Threat Detection, Vulnerability Management, Security Incident Response & Cybersecurity Assurance**

It shall establish the permanent enterprise operating model for cybersecurity strategy, security governance, security architecture, security operations, security monitoring, threat intelligence, threat detection, vulnerability management, security incident response, security engineering, endpoint security, network security integration, cloud security integration, application security integration, data security integration, security awareness, security suppliers, security compliance, security exceptions, remediation, security assurance, metrics, dashboards, maturity and continual enterprise cybersecurity capability improvement supporting MFM.

# 139. Document Control

**Document:** MFM v1.2-Steady-State-123  
**Version:** 1.2  
**Status:** Steady-State Enterprise Identity & Access Management Baseline  
**Previous Document:** MFM v1.2-Steady-State-122  
**Next Document:** MFM v1.2-Steady-State-124  
**Lifecycle:** Steady-State Operation  
**IAM Governance Authority:** Identity and Access Management  
**Identity Architecture Authority:** Enterprise Identity Architecture  
**Authentication Authority:** Authentication / Identity Platform Management  
**Authorization Authority:** Access Governance / IAM  
**Privileged Access Authority:** Privileged Access Management  
**Directory Authority:** Directory Services Management  
**Federation Authority:** Federation / Identity Platform Management  
**Service Identity Authority:** Non-Human Identity Management  
**Secrets Authority:** Secrets / Credential Management  
**Application Authority:** Enterprise Application Architecture  
**Data Authority:** Enterprise Data Management  
**Integration Authority:** Enterprise Integration Architecture  
**Network Authority:** Enterprise Network Architecture  
**Infrastructure Authority:** Enterprise Infrastructure Architecture  
**Cloud Authority:** Enterprise Cloud Architecture  
**Cybersecurity Authority:** Enterprise Cybersecurity  
**Service Authority:** Enterprise IT Service Management  
**Workforce Source Authority:** HR / Workforce Identity Source  
**Asset Authority:** Enterprise Asset Management  
**Supplier Authority:** Supplier / Third-Party Management  
**Risk Authority:** Enterprise Risk Management  
**Compliance Authority:** Enterprise Compliance  
**Legal Authority:** Legal / Regulatory Affairs  
**Continuity Authority:** Business Continuity / Operational Resilience  
**Assurance Authority:** IAM Assurance / Internal Audit / Independent Assurance  
**Improvement Authority:** Continual Enterprise Identity Capability Improvement  

**Principle:** MFM must govern identity and access as a foundational enterprise security capability, ensuring that every material human, privileged, service and machine identity is appropriately established, authenticated, authorized, monitored, reviewed and removed throughout its complete lifecycle.
