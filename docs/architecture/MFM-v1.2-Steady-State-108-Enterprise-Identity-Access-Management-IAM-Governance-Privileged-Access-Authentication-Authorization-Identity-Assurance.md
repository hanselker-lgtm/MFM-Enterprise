# MFM v1.2-Steady-State-108
## Enterprise Identity & Access Management, IAM Governance, Privileged Access, Authentication, Authorization & Identity Assurance

**Version:** 1.2  
**Document ID:** MFM v1.2-Steady-State-108  
**Status:** Steady-State Enterprise Identity & Access Management Baseline  
**Lifecycle:** Post-Implementation / Steady-State Operation  
**Document Type:** Identity Architecture / IAM Governance / Authentication / Authorization / Privileged Access / Identity Assurance Document  

---

# 1. Purpose

This document establishes the one-hundred-and-eighth document in the MFM v1.2 Steady-State series.

It follows MFM v1.2-Steady-State-107 – Enterprise Security Operations Center, SIEM/SOAR, Detection Engineering, Threat Hunting, Digital Forensics & Security Incident Response.

The purpose is to establish the permanent enterprise operating model for identity governance, identity lifecycle, joiner-mover-leaver processes, authentication, authorization, privileged access management, service identities, federation, single sign-on, access reviews, entitlement governance, segregation of duties, identity monitoring, identity incidents, identity exceptions, identity remediation, identity assurance, identity metrics, dashboards, maturity and continual enterprise identity capability improvement.

The central objective is:

> **MFM must manage digital identities and access rights as controlled enterprise assets, ensuring that every identity is attributable, appropriately authenticated, authorized according to business need, continuously governed and removed or adjusted when no longer required.**

---

# 2. Scope

This document covers:

- Enterprise Identity Architecture
- Identity Governance
- Identity Lifecycle Management
- Joiner / Mover / Leaver
- Authentication
- Authorization
- Privileged Access Management
- Service Identities
- Federation
- Single Sign-On
- Access Reviews
- Entitlement Governance
- Segregation of Duties
- Identity Monitoring
- Identity Incidents
- Identity Exceptions
- Identity Remediation
- Identity Assurance
- Identity Metrics
- Identity Dashboards
- Identity Maturity
- Continual Enterprise Identity Capability Improvement

---

# 3. Identity Governance Objective

The primary objective is:

> **Establish clear authority, ownership, lifecycle controls, access standards and assurance for enterprise identities and entitlements.**

# 4. Identity Architecture Objective

The primary objective is:

> **Provide a coherent enterprise identity architecture supporting secure authentication, authorization, federation, privileged access, service identities and application integration.**

# 5. Identity Lifecycle Objective

The primary objective is:

> **Ensure identities and access rights are created, changed, reviewed, suspended and removed according to authoritative business events and approved requirements.**

# 6. Authentication Objective

The primary objective is:

> **Verify identity using authentication mechanisms proportionate to risk and appropriate to the access being requested.**

# 7. Authorization Objective

The primary objective is:

> **Ensure access is granted according to legitimate business need, least privilege, role requirements and segregation-of-duties principles.**

# 8. Privileged Access Objective

The primary objective is:

> **Protect privileged identities and administrative access through enhanced controls, monitoring, approval, time limitation and accountability.**

# 9. Identity Assurance Objective

The primary objective is:

> **Provide evidence that identities, authentication mechanisms, entitlements and privileged access remain appropriately governed and effective.**

# 10. Identity Principles

Identity should be:

```text
Unique
Attributable
Verified
Governed
Least-Privilege
Lifecycle-Controlled
Observable
```

# 11. Authentication Principles

Authentication should be:

```text
Risk-Based
Strong
Appropriate
Traceable
Resilient
```

# 12. Authorization Principles

Authorization should be:

```text
Need-Based
Least-Privilege
Role-Based
Time-Aware
Reviewable
```

# 13. Privileged Access Principles

Privileged access should be:

```text
Restricted
Approved
Time-Limited where Appropriate
Monitored
Auditable
```

# 14. Identity Lifecycle

Identity management should integrate:

```text
Join
 ↓
Provision
 ↓
Authenticate
 ↓
Authorize
 ↓
Use
 ↓
Review
 ↓
Change
 ↓
Suspend
 ↓
Deprovision
```

# 15. Identity Governance

Identity governance should establish:

```text
Authority
Ownership
Policy
Standards
Lifecycle
Risk
Assurance
```

# 16. Identity Authority

Identity authority should define who may:

```text
Approve Identity Standards
Approve Authentication Standards
Approve Access Models
Approve Privileged Access
Approve Exceptions
Accept Identity Risk
```

# 17. Identity Ownership

Material identity capabilities should have accountable owners for:

```text
Architecture
Lifecycle
Authentication
Authorization
Privileged Access
Monitoring
Evidence
Remediation
```

# 18. Identity Inventory

Material identity stores and identity populations should be sufficiently inventoried.

# 19. Identity Types

Identity management should distinguish where applicable:

```text
Human Identity
Privileged Identity
Service Identity
Application Identity
Device Identity
External Identity
Guest Identity
Emergency Identity
```

# 20. Authoritative Identity Source

Each material identity population should have an identified authoritative source where appropriate.

# 21. Identity Attributes

Identity attributes should be managed according to business and security requirements.

Examples may include:

```text
Name
Unique Identifier
Organization
Role
Employment Status
Manager
Location
Access Eligibility
```

# 22. Identity Correlation

Identity records across systems should be correlated where required to maintain a coherent identity view.

# 23. Identity Lifecycle Events

Material lifecycle events may include:

```text
Joiner
Mover
Leaver
Contractor Start
Contractor End
Role Change
Access Change
Suspension
Termination
```

# 24. Joiner Process

Joiner provisioning should establish:

```text
Identity
Authentication
Required Access
Approvals
Ownership
```

before access is activated.

# 25. Mover Process

Role or organizational changes should trigger appropriate access reassessment.

# 26. Leaver Process

Termination should trigger timely:

```text
Account Disablement
Access Revocation
Privileged Access Removal
Session / Credential Handling
Asset Recovery Coordination
```

according to applicable requirements.

# 27. Contractor Lifecycle

Contractor identities should have:

```text
Sponsor
Purpose
Start Date
End Date
Access Scope
Review
```

# 28. Guest Identity Lifecycle

Guest identities should have:

```text
Sponsor
Purpose
Expiration
Access Scope
Review
```

# 29. Emergency Identity

Emergency or break-glass identities should have enhanced:

```text
Protection
Approval
Monitoring
Testing
Review
```

# 30. Authentication

Authentication mechanisms should align with:

```text
Risk
Application
Data Sensitivity
Access Type
User Population
```

# 31. Multi-Factor Authentication

MFA should be required for material access where risk warrants it, particularly for privileged and externally exposed access.

# 32. Password Authentication

Where passwords are used, they should be governed for:

```text
Strength
Protection
Storage
Reset
Recovery
Compromise Response
```

# 33. Passwordless Authentication

Where appropriate, stronger passwordless authentication may be used to reduce credential risk.

# 34. Authentication Factors

Authentication may use:

```text
Knowledge
Possession
Inherence
Cryptographic Credentials
Federated Trust
```

according to approved standards.

# 35. Authentication Recovery

Credential recovery should use controlled identity verification and recovery procedures.

# 36. Authentication Risk

Higher-risk access should use stronger authentication controls.

# 37. Federation

Federation should provide controlled trust between approved identity domains and relying services.

# 38. Federation Governance

Federation arrangements should define:

```text
Trust
Provider
Consumer
Claims
Authentication
Authorization
Lifecycle
```

# 39. Single Sign-On

SSO should be used where appropriate to improve:

```text
Security
User Experience
Centralized Control
```

# 40. SSO Lifecycle

Applications integrated with SSO should have:

```text
Owner
Configuration
Authentication Method
Authorization Model
Lifecycle
```

# 41. Identity Providers

Identity providers should have:

```text
Owner
Architecture
Security
Availability
Monitoring
Recovery
```

# 42. Authorization

Authorization should be based on:

```text
Role
Need
Context
Resource
Risk
```

# 43. Role-Based Access Control

RBAC should be used where appropriate to simplify consistent entitlement management.

# 44. Attribute-Based Access Control

ABAC may be used where context and attributes provide meaningful authorization benefits.

# 45. Least Privilege

Users and services should receive only the access required to perform authorized activities.

# 46. Entitlement Management

Entitlements should have:

```text
Owner
Purpose
Scope
Approval
Risk
Review
```

# 47. Access Request

Access requests should identify:

```text
Requester
User
Resource
Purpose
Duration
Approver
```

# 48. Access Approval

Approvals should be performed by authorized persons with sufficient business or technical authority.

# 49. Access Provisioning

Approved access should be provisioned through controlled processes.

# 50. Access Revocation

Access should be revoked when:

```text
No Longer Required
Role Changes
Contract Ends
Employment Ends
Risk Changes
Approval Expires
```

# 51. Access Reviews

Material access should be periodically reviewed.

# 52. Access Review Scope

Reviews should consider:

```text
User
Role
Entitlement
Criticality
Privileged Status
Last Use
Owner
```

# 53. Entitlement Certification

Where appropriate, access owners should certify continued business need.

# 54. Segregation of Duties

Material conflicting access combinations should be identified and controlled.

# 55. SoD Exceptions

Exceptions should identify:

```text
Conflict
Reason
Risk
Compensating Control
Approver
Expiry
```

# 56. Privileged Access Management

Privileged access should be governed through enhanced controls.

# 57. Privileged Account Inventory

Privileged accounts should be identified and inventoried.

# 58. Privileged Access Approval

Privileged access should require appropriate approval.

# 59. Just-in-Time Privilege

Where appropriate, privileged access should be time-limited and activated only when needed.

# 60. Privileged Session Monitoring

Material privileged activity should be monitored and auditable.

# 61. Privileged Credential Protection

Privileged credentials should be protected through approved secure mechanisms.

# 62. Privileged Credential Rotation

Credentials should be rotated according to:

```text
Risk
Credential Type
Technology
Compromise
Policy
```

# 63. Break-Glass Privileged Access

Break-glass access should be:

```text
Restricted
Protected
Monitored
Tested
Reviewed
```

# 64. Service Identities

Service identities should have:

```text
Owner
Purpose
Application
Scope
Credential / Federation
Rotation
Monitoring
Lifecycle
```

# 65. Non-Human Identity Governance

Non-human identities should receive governance comparable to human identities according to risk.

# 66. Application Identity

Application identities should be:

```text
Unique
Scoped
Protected
Monitored
Lifecycle-Controlled
```

# 67. Device Identity

Where device identity is used, devices should have controlled identity lifecycle and trust status.

# 68. External Identity

External identities should have:

```text
Sponsor
Purpose
Access Scope
Expiration
Review
```

# 69. Identity Monitoring

Identity monitoring should cover:

```text
Authentication
Authorization
Privileged Access
Lifecycle Events
Suspicious Activity
```

# 70. Authentication Monitoring

Monitoring should identify relevant:

```text
Failed Logins
Impossible Travel / Anomalies where Applicable
Credential Abuse
MFA Events
Password Resets
```

# 71. Privileged Activity Monitoring

Privileged activity should be monitored according to risk.

# 72. Identity Analytics

Identity analytics may identify:

```text
Dormant Accounts
Excessive Privilege
Unusual Access
Privilege Escalation
Orphaned Accounts
Duplicate Identities
```

# 73. Dormant Accounts

Dormant identities should be identified and handled according to approved policy.

# 74. Orphaned Accounts

Accounts without valid ownership should be identified and remediated.

# 75. Shared Accounts

Shared accounts should be avoided where individual attribution is possible.

Where unavoidable, they should have enhanced controls and accountability.

# 76. Identity Incident Management

Identity incidents should integrate with enterprise security incident management.

# 77. Identity Incident Classification

Incidents may include:

```text
Credential Compromise
Unauthorized Access
Privilege Escalation
Account Takeover
MFA Abuse
Identity Misconfiguration
Orphaned Access
```

# 78. Identity Incident Response

Response should integrate:

```text
Detect
 ↓
Validate
 ↓
Contain
 ↓
Reset / Revoke
 ↓
Investigate
 ↓
Recover
 ↓
Validate
 ↓
Learn
```

# 79. Credential Compromise

Compromised credentials should be:

```text
Contained
Reset / Revoked
Investigated
Monitored
```

according to risk.

# 80. Identity Configuration

Identity configurations should use approved security baselines.

# 81. Identity Configuration Monitoring

Configuration should be monitored for:

```text
Unauthorized Changes
Weak Authentication
Excessive Privilege
Policy Violations
```

# 82. Identity Integration

Identity services should integrate with:

```text
Applications
Cloud
Infrastructure
Network
Security
Data
```

# 83. Directory Services

Directory services should be governed for:

```text
Architecture
Replication
Security
Availability
Backup
Recovery
Lifecycle
```

# 84. Identity Federation Security

Federation should protect:

```text
Trust Relationships
Tokens
Claims
Keys
Endpoints
```

# 85. Token Security

Authentication and authorization tokens should have appropriate:

```text
Lifetime
Scope
Protection
Validation
Revocation
```

# 86. Identity Key Management

Identity cryptographic keys should have:

```text
Owner
Protection
Rotation
Access Control
Recovery
Lifecycle
```

# 87. Identity Backup and Recovery

Critical identity services should have appropriate backup and recovery arrangements.

# 88. Identity Resilience

Identity services should have resilience appropriate to business criticality.

# 89. Identity Change Management

Material identity changes should be:

```text
Requested
Assessed
Approved
Tested
Implemented
Validated
Recorded
```

# 90. Identity Automation

Automation may support:

```text
Provisioning
Deprovisioning
Access Changes
Reviews
Credential Rotation
Compliance
```

with appropriate controls.

# 91. Identity Governance Automation

Identity workflows should be automated where this improves consistency and traceability.

# 92. Identity Exceptions

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

# 93. Identity Remediation

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

# 94. Identity Assurance

Assurance may include:

```text
Identity Reviews
Access Reviews
Privileged Access Reviews
SoD Reviews
Authentication Reviews
Service Identity Reviews
Configuration Reviews
Federation Reviews
Internal Audit
Independent Assurance
```

# 95. Identity Evidence

Evidence should support:

```text
Identity Lifecycle
Access Approval
Access Review
Privileged Access
Authentication
Configuration
Exceptions
Remediation
```

# 96. Identity Metrics

Metrics may include:

```text
Identity Inventory Coverage
Joiner Completion
Mover Completion
Leaver Completion
Account Disablement Timeliness
MFA Coverage
SSO Coverage
Access Review Completion
Access Revocation Timeliness
Privileged Account Coverage
JIT Usage
Privileged Session Monitoring
Service Identity Ownership
Dormant Accounts
Orphaned Accounts
SoD Conflicts
Identity Incidents
Credential Compromise
Authentication Failure Rate
Identity Findings
Remediation Completion
```

# 97. Identity Dashboard

May include:

```text
Identity Estate
Lifecycle
Authentication
Authorization
Privileged Access
Service Identities
Federation
SSO
Access Reviews
SoD
Identity Monitoring
Incidents
Findings
Remediation
```

# 98. Daily Review

Where appropriate:

```text
Critical Identity Alerts
Privileged Access Events
Credential Compromise
Authentication Anomalies
Identity Service Health
```

# 99. Weekly Review

May consider:

```text
Lifecycle Backlog
Access Requests
Access Revocations
Privileged Activity
Identity Incidents
Dormant Accounts
Orphaned Accounts
Open Remediation
```

# 100. Monthly Review

May consider:

```text
Identity Governance
MFA
SSO
Access Reviews
Privileged Access
Service Identities
SoD
Authentication
Incidents
Configuration
Assurance
```

# 101. Quarterly Review

May consider:

```text
Identity Strategy
Architecture
Lifecycle
Authentication
Authorization
Privileged Access
Federation
Service Identities
SoD
Third-Party Identity
Risk
Assurance
Maturity
```

# 102. Annual Review

May consider:

```text
Identity Strategy
Operating Model
Governance
Architecture
Identity Lifecycle
Authentication
Authorization
PAM
Federation
SSO
Service Identities
Directory Services
Identity Monitoring
Identity Incidents
Resilience
Recovery
Automation
Third-Party Identity
Assurance
Maturity
Improvement
```

# 103. Identity Maturity

Identity capability maturity should be periodically assessed.

# 104. Maturity Dimensions

Assess:

```text
Governance
Strategy
Authority
Ownership
Inventory
Identity Types
Authoritative Sources
Attributes
Correlation
Lifecycle Events
Joiner
Mover
Leaver
Contractor
Guest
Emergency Identity
Authentication
MFA
Password
Passwordless
Authentication Factors
Recovery
Risk
Federation
SSO
Identity Providers
Authorization
RBAC
ABAC
Least Privilege
Entitlement Management
Access Requests
Approvals
Provisioning
Revocation
Access Reviews
Certification
SoD
PAM
Privileged Inventory
Approval
JIT
Session Monitoring
Credential Protection
Credential Rotation
Break-Glass
Service Identities
Non-Human Identity
Application Identity
Device Identity
External Identity
Monitoring
Authentication Monitoring
Privileged Monitoring
Identity Analytics
Dormant Accounts
Orphaned Accounts
Shared Accounts
Identity Incidents
Credential Compromise
Configuration
Directory Services
Federation Security
Token Security
Key Management
Backup
Recovery
Resilience
Change Management
Automation
Exceptions
Remediation
Assurance
Metrics
Improvement
```

# 105. Maturity Levels

```text
1 – Initial
2 – Repeatable
3 – Defined
4 – Managed
5 – Optimized
```

# 106. Identity Architecture Quality Gate

```text
Business Need
 ↓
Identity Requirement
 ↓
Risk
 ↓
Architecture
 ↓
Authentication
 ↓
Authorization
 ↓
Privileged Access
 ↓
Monitoring
 ↓
Assurance
```

must be controlled.

# 107. Identity Lifecycle Quality Gate

```text
Authoritative Event
 ↓
Identity Validation
 ↓
Provision
 ↓
Access Approval
 ↓
Access Assignment
 ↓
Review
 ↓
Change / Revoke
 ↓
Evidence
```

must be controlled.

# 108. Access Quality Gate

```text
Request
 ↓
Business Need
 ↓
Risk
 ↓
Approval
 ↓
Provision
 ↓
Monitor
 ↓
Review
 ↓
Revoke
```

must be controlled.

# 109. Privileged Access Quality Gate

```text
Need
 ↓
Approval
 ↓
JIT / Controlled Access
 ↓
Session Monitoring
 ↓
Activity Review
 ↓
Revoke
 ↓
Evidence
```

must be controlled.

# 110. Identity Assurance Quality Gate

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

# 111. Definition of Ready

An identity architecture, lifecycle change, access request, privileged access arrangement, service identity, federation integration, authentication change, exception, remediation or assurance review is Ready when purpose, owner, identity population, resource, business need, risk, authentication requirements, authorization model, lifecycle, approval authority and acceptance criteria are defined.

# 112. Definition of Done

An identity work item is Done when:

```text
Requirement / Identity Event Identified
        ↓
Owner Assigned
        ↓
Identity Action Completed
        ↓
Authentication / Authorization / Privileged Access / Lifecycle Validation Completed where Required
        ↓
Identity / Access / Configuration / Evidence Records Updated
        ↓
Evidence Captured
        ↓
Findings / Exceptions Addressed
        ↓
Outcome Accepted
```

# 113. Final Identity Governance Principle

> **MFM must manage digital identities and access rights as controlled enterprise assets, ensuring that every identity is attributable, appropriately authenticated, authorized according to business need, continuously governed and removed or adjusted when no longer required.**

# 114. Final Authentication Principle

> **Authentication must provide assurance proportionate to the risk of the identity, application, data and access being protected.**

# 115. Final Authorization Principle

> **Authorization must grant only the access required for legitimate business activity and must remain reviewable throughout the identity lifecycle.**

# 116. Final Privileged Access Principle

> **Privileged access must receive enhanced controls, including approval, restriction, monitoring, accountability and time limitation where appropriate.**

# 117. Final Lifecycle Principle

> **Identity lifecycle events must drive timely provisioning, modification, review, suspension and deprovisioning of identities and entitlements.**

# 118. Final Service Identity Principle

> **Non-human identities must be uniquely owned, appropriately scoped, securely protected, monitored and lifecycle-controlled.**

# 119. Final Assurance Principle

> **Material identity controls must be supported by reliable evidence and periodically assessed through risk-based assurance.**

# 120. Final Improvement Principle

> **Identity incidents, access findings, lifecycle failures, privilege weaknesses and assurance results must continuously improve MFM's identity capability.**

# 121. Final Integration Principle

> **Identity and Access Management must integrate with Enterprise Architecture, Cybersecurity, Applications, Data, Infrastructure, Cloud, Network, Service Management, HR / authoritative personnel processes, Suppliers, Risk, Compliance, Legal and Business Continuity.**

# 122. Final Steady-State Identity Principle

> **MFM must manage digital identities and access rights as controlled enterprise assets, ensuring that every identity is attributable, appropriately authenticated, authorized according to business need, continuously governed and removed or adjusted when no longer required.**

# 123. Summary

MFM v1.2-Steady-State-108 establishes the permanent Enterprise Identity & Access Management baseline.

It defines:

- Identity Governance / Authority / Ownership / Inventory
- Human / Privileged / Service / Application / Device / External / Guest / Emergency Identities
- Authoritative Identity Sources / Attributes / Correlation
- Identity Lifecycle / Joiner / Mover / Leaver
- Contractor / Guest / Emergency Identity
- Authentication / MFA / Password / Passwordless / Authentication Factors
- Authentication Recovery / Risk
- Federation / Federation Governance / SSO
- Identity Providers / Authorization
- RBAC / ABAC / Least Privilege
- Entitlement Management / Access Request / Approval / Provisioning / Revocation
- Access Reviews / Entitlement Certification
- Segregation of Duties / SoD Exceptions
- Privileged Access Management / Privileged Inventory / Approval
- JIT Privilege / Session Monitoring / Credential Protection / Rotation
- Break-Glass Access
- Service Identities / Non-Human Identities / Application Identities / Device Identities
- External Identities
- Identity Monitoring / Authentication Monitoring / Privileged Activity Monitoring
- Identity Analytics / Dormant / Orphaned / Shared Accounts
- Identity Incidents / Credential Compromise / Response
- Identity Configuration / Directory Services
- Federation Security / Token Security / Identity Key Management
- Identity Backup / Recovery / Resilience
- Identity Change Management / Automation
- Identity Exceptions / Remediation / Assurance / Evidence
- Identity Metrics / Identity Dashboard
- Daily / Weekly / Monthly / Quarterly / Annual Reviews
- Identity Maturity
- Identity Architecture / Lifecycle / Access / Privileged Access / Assurance Quality Gates
- Definition of Ready
- Definition of Done

# 124. Next Document

**MFM v1.2-Steady-State-109 – Enterprise Network Architecture, Network Security, Connectivity, Segmentation, Remote Access, DNS, IP Management & Network Assurance**

It shall establish the permanent enterprise operating model for network architecture, network governance, connectivity, routing, switching, segmentation, firewalling, remote access, VPN, wireless, DNS, DHCP, IP address management, network monitoring, network performance, network resilience, network configuration, network incidents, network changes, network lifecycle, network security integration, network exceptions, network remediation, network assurance, network metrics, dashboards, maturity and continual enterprise network capability improvement supporting MFM.

# 125. Document Control

**Document:** MFM v1.2-Steady-State-108  
**Version:** 1.2  
**Status:** Steady-State Enterprise Identity & Access Management Baseline  
**Previous Document:** MFM v1.2-Steady-State-107  
**Next Document:** MFM v1.2-Steady-State-109  
**Lifecycle:** Steady-State Operation  
**Identity Governance Authority:** Identity and Access Management  
**Identity Architecture Authority:** Enterprise Identity Architecture  
**Authentication Authority:** Authentication Services  
**Authorization Authority:** Access / Entitlement Management  
**Privileged Access Authority:** Privileged Access Management  
**Federation Authority:** Identity Federation / SSO  
**Service Identity Authority:** Non-Human Identity Management  
**Security Authority:** Information Security / Cybersecurity  
**Application Authority:** Enterprise Application Management  
**Data Authority:** Enterprise Data Management  
**Infrastructure Authority:** Enterprise Infrastructure Architecture  
**Cloud Authority:** Enterprise Cloud Architecture  
**Network Authority:** Enterprise Network Architecture  
**Architecture Authority:** Enterprise Architecture  
**Service Authority:** Enterprise Service Management  
**Configuration Authority:** Configuration Management  
**Asset Authority:** Enterprise Asset Management  
**Change Authority:** Enterprise Change Management  
**Supplier Authority:** Supplier / Third-Party Management  
**Risk Authority:** Enterprise Risk Management  
**Compliance Authority:** Enterprise Compliance  
**Legal Authority:** Legal / Regulatory Affairs  
**Business Continuity Authority:** Business Continuity / Operational Resilience  
**People / Personnel Authority:** HR / Authoritative Personnel Processes  
**Assurance Authority:** Identity Assurance / Internal Audit / Independent Assurance  
**Improvement Authority:** Continual Enterprise Identity Capability Improvement  

**Principle:** MFM must manage digital identities and access rights as controlled enterprise assets, ensuring that every identity is attributable, appropriately authenticated, authorized according to business need, continuously governed and removed or adjusted when no longer required.
