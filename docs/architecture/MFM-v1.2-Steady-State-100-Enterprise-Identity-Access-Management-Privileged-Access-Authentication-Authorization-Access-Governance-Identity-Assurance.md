# MFM v1.2-Steady-State-100
## Enterprise Identity & Access Management, Privileged Access, Authentication, Authorization, Access Governance & Identity Assurance

**Version:** 1.2  
**Document ID:** MFM v1.2-Steady-State-100  
**Status:** Steady-State Enterprise Identity & Access Management Baseline  
**Lifecycle:** Post-Implementation / Steady-State Operation  
**Document Type:** Identity & Access Management / Authentication / Authorization / Privileged Access / Access Governance / Identity Assurance Document  

---

# 1. Purpose

This document establishes the one-hundredth document in the MFM v1.2 Steady-State series.

It follows MFM v1.2-Steady-State-99 – Enterprise Cybersecurity Operations, Security Monitoring, Security Incident Response, Threat Management, Vulnerability Management & Security Assurance.

The purpose is to establish the permanent enterprise operating model for identity lifecycle management, workforce identity, customer and external identity, service identities, authentication, authorization, role management, access requests, approvals, provisioning, deprovisioning, privileged access management, access reviews, segregation of duties, identity governance, federation, single sign-on, credential management, identity monitoring, access exceptions, remediation, identity metrics, dashboards, maturity and continual enterprise identity and access management improvement.

The central objective is:

> **MFM must ensure that every identity receives only the access required for its legitimate purpose, for the appropriate duration, through controlled authentication, authorization, provisioning, monitoring, review and removal.**

---

# 2. Scope

This document covers:

- Enterprise Identity & Access Management
- Workforce Identity
- Customer and External Identity
- Service Identities
- Authentication
- Authorization
- Role Management
- Access Requests
- Access Approvals
- Provisioning
- Deprovisioning
- Privileged Access Management
- Access Reviews
- Segregation of Duties
- Identity Governance
- Federation
- Single Sign-On
- Credential Management
- Identity Monitoring
- Access Exceptions
- Identity Remediation
- Identity Metrics
- Identity Dashboards
- Identity Maturity
- Identity Assurance
- Continual Enterprise Identity and Access Management Improvement

---

# 3. Identity Governance Objective

The primary objective is:

> **Establish clear ownership, authority, lifecycle controls and assurance for all enterprise identities and access rights.**

# 4. Authentication Objective

The primary objective is:

> **Verify identity reliably using authentication controls proportionate to risk, sensitivity and access privilege.**

# 5. Authorization Objective

The primary objective is:

> **Ensure access decisions are based on approved roles, attributes, business purpose and applicable security requirements.**

# 6. Privileged Access Objective

The primary objective is:

> **Protect privileged access through enhanced controls, monitoring, approval, time limitation and accountability.**

# 7. Access Governance Objective

The primary objective is:

> **Ensure access is requested, approved, provisioned, reviewed and removed through controlled and auditable processes.**

# 8. Identity Assurance Objective

The primary objective is:

> **Provide evidence that identities, credentials, access rights and privileged activities remain accurate, authorized and appropriately governed.**

# 9. Identity Principles

Identity management should be:

```text
Unique
Traceable
Purpose-Based
Least-Privilege
Lifecycle-Controlled
Risk-Based
Auditable
```

# 10. Access Principles

Access should be:

```text
Authorized
Necessary
Proportionate
Time-Bounded where Appropriate
Reviewable
Revocable
```

# 11. Authentication Principles

Authentication should be:

```text
Strong
Risk-Based
Resistant to Credential Theft
Appropriate to Assurance Level
Monitored
```

# 12. Privileged Access Principles

Privileged access should be:

```text
Restricted
Approved
Time-Limited
Monitored
Recorded
Reviewed
```

# 13. Identity Lifecycle

The identity lifecycle should integrate:

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
Remove
```

# 14. Access Lifecycle

The access lifecycle should integrate:

```text
Need
 ↓
Request
 ↓
Approve
 ↓
Provision
 ↓
Use
 ↓
Review
 ↓
Modify
 ↓
Revoke
```

# 15. Identity Governance

Identity governance should establish:

```text
Ownership
Policy
Standards
Roles
Approval
Review
Assurance
```

# 16. Identity Authority

Identity authority should define who may:

```text
Create Identity
Approve Identity
Approve Access
Grant Privilege
Suspend Identity
Disable Identity
Reset Credentials
Accept Identity Risk
```

# 17. Identity Types

Enterprise identity governance should consider:

```text
Employees
Contractors
Partners
Customers
Suppliers
Service Accounts
Application Identities
Machine Identities
Privileged Identities
Emergency / Break-Glass Identities
```

# 18. Workforce Identity

Workforce identities should be linked to authoritative employment or engagement records where appropriate.

# 19. External Identity

External identities should have:

```text
Owner
Purpose
Sponsor
Lifecycle
Access Scope
Expiry
```

where applicable.

# 20. Customer Identity

Customer identities should be managed according to applicable business, security, privacy and authentication requirements.

# 21. Service Identities

Service identities should have:

```text
Owner
Purpose
Application
Privileges
Credential
Rotation
Lifecycle
```

# 22. Machine Identities

Machine identities should be uniquely identifiable and governed according to:

```text
Owner
Purpose
Certificate / Credential
Lifecycle
Access
```

# 23. Identity Inventory

Material identities should be recorded in authoritative identity systems or inventories.

# 24. Identity Attributes

Relevant attributes may include:

```text
Identity ID
Name
Type
Owner
Department
Role
Status
Sponsor
Authentication Method
Risk
Expiry
```

# 25. Identity Proofing

Identity creation should use appropriate identity proofing according to identity type and assurance requirements.

# 26. Identity Verification

Identity verification should be performed before granting or recovering sensitive access.

# 27. Identity Uniqueness

Individuals should not have unnecessary duplicate identities.

# 28. Identity Status

Identity status should support states such as:

```text
Pending
Active
Suspended
Disabled
Expired
Deleted / Archived
```

# 29. Joiner Process

New identities should be created through controlled joiner processes.

# 30. Joiner Access

Initial access should be based on:

```text
Role
Business Need
Approved Entitlements
```

# 31. Mover Process

Changes in role, department, responsibilities or engagement should trigger appropriate access reassessment.

# 32. Mover Access

Access no longer required should be removed or adjusted promptly.

# 33. Leaver Process

Termination or end of engagement should trigger controlled identity deprovisioning.

# 34. Leaver Timing

Removal timing should be proportionate to:

```text
Risk
Role
Privilege
Termination Circumstances
```

# 35. Suspension

Identities may be suspended when:

```text
Security Concern
Investigation
Leave
Administrative Requirement
```

requires it.

# 36. Reinstatement

Suspended identities should only be reinstated through authorized processes.

# 37. Access Request

Access requests should identify:

```text
Requester
Identity
Resource
Role / Entitlement
Business Need
Duration
```

# 38. Access Approval

Access should be approved by an appropriately authorized owner.

# 39. Access Ownership

Resource or application owners should remain accountable for access decisions to their resources.

# 40. Role-Based Access Control

RBAC should be used where appropriate to align access with defined organizational roles.

# 41. Attribute-Based Access Control

ABAC may be used where access depends on attributes such as:

```text
Identity
Device
Location
Risk
Resource
Time
```

# 42. Policy-Based Access

Access policies should provide consistent authorization decisions.

# 43. Least Privilege

Identities should receive only the permissions necessary to perform legitimate duties.

# 44. Need-to-Know

Access to sensitive information should be limited to legitimate business need.

# 45. Separation of Duties

Conflicting responsibilities should be separated where necessary to reduce fraud, error or unauthorized activity risk.

# 46. Segregation of Duties Rules

Material conflicts should be:

```text
Identified
Assessed
Blocked or Controlled
Exception-Managed
Reviewed
```

# 47. Access Provisioning

Approved access should be provisioned through controlled processes.

# 48. Automated Provisioning

Automation should be used where appropriate to improve:

```text
Speed
Consistency
Accuracy
Traceability
```

# 49. Manual Provisioning

Manual provisioning should remain controlled, authorized and evidenced.

# 50. Access Removal

Access should be removed when:

```text
Need Ends
Role Changes
Identity Ends
Authorization Expires
Risk Requires
```

# 51. Access Expiry

Temporary access should have defined expiry where appropriate.

# 52. Access Review

Access reviews should confirm that:

```text
Access Exists
Owner Exists
Need Exists
Privilege Is Appropriate
```

# 53. Periodic Access Certification

Critical applications and sensitive resources should receive periodic access certification.

# 54. Privileged Access Management

Privileged access should use enhanced controls including where appropriate:

```text
Approval
Time Limitation
Credential Vaulting
Session Monitoring
Session Recording
Command Logging
```

# 55. Privileged Identity

Privileged identities should be distinguishable from standard user identities.

# 56. Just-in-Time Privilege

Just-in-time access should be used where appropriate to reduce persistent privilege.

# 57. Privilege Elevation

Privilege elevation should be:

```text
Authorized
Time-Limited
Traceable
Monitored
```

# 58. Break-Glass Access

Emergency access should be tightly controlled and reviewed after use.

# 59. Privileged Session Monitoring

Material privileged sessions should be monitored according to risk.

# 60. Privileged Session Evidence

Privileged activity should provide sufficient evidence for investigation and assurance.

# 61. Authentication

Authentication controls should match identity assurance and access risk.

# 62. Multi-Factor Authentication

MFA should be used for sensitive and privileged access according to risk and policy.

# 63. Password Authentication

Where passwords are used, controls should address:

```text
Length
Strength
Protection
Reset
Lockout
Reuse
Monitoring
```

# 64. Passwordless Authentication

Passwordless methods may be used where supported and appropriate.

# 65. Phishing-Resistant Authentication

High-risk access should use phishing-resistant authentication where feasible.

# 66. Adaptive Authentication

Authentication decisions may consider:

```text
Risk
Device
Location
Behavior
Resource
```

# 67. Credential Management

Credentials should be:

```text
Protected
Stored Securely
Rotated
Revoked
Monitored
```

# 68. Credential Rotation

Sensitive service and privileged credentials should rotate according to risk and policy.

# 69. Credential Recovery

Credential recovery should use strong identity verification and controlled procedures.

# 70. Authentication Monitoring

Authentication monitoring should identify:

```text
Failed Attempts
Unusual Locations
Impossible Travel
Anomalous Devices
Privilege Changes
Suspicious Sessions
```

where applicable.

# 71. Federation

Identity federation should be governed through:

```text
Trust
Authentication
Authorization
Attribute Mapping
Lifecycle
Monitoring
```

# 72. Single Sign-On

SSO should be used where appropriate to improve:

```text
User Experience
Central Control
Authentication Security
Lifecycle Management
```

# 73. Identity Provider Governance

Identity providers should have:

```text
Owner
Security Controls
Availability
Recovery
Monitoring
```

# 74. Directory Services

Directory services should be governed for:

```text
Identity
Groups
Attributes
Authentication
Access
Lifecycle
```

# 75. Group Management

Groups should have:

```text
Owner
Purpose
Membership Rules
Review
Expiry where Appropriate
```

# 76. Nested Groups

Nested group structures should be controlled to avoid unintended privilege inheritance.

# 77. Role Management

Roles should have:

```text
Name
Purpose
Owner
Entitlements
Eligibility
Review
```

# 78. Role Engineering

Roles should be designed to minimize excessive or conflicting access.

# 79. Role Lifecycle

Roles should be:

```text
Created
Approved
Used
Reviewed
Modified
Retired
```

# 80. Entitlement Management

Entitlements should be identifiable and associated with appropriate owners.

# 81. Entitlement Catalog

Material applications and resources should maintain an entitlement catalog where appropriate.

# 82. Access Bundles

Common role-based access packages may be used to standardize provisioning.

# 83. Access Analytics

Access analytics may identify:

```text
Excessive Privilege
Dormant Accounts
Orphaned Access
Conflicting Roles
Anomalous Access
```

# 84. Dormant Accounts

Dormant identities should be identified and disabled or reviewed according to policy.

# 85. Orphaned Accounts

Accounts without valid ownership should be investigated and remediated.

# 86. Shared Accounts

Shared accounts should be avoided where practical and controlled through compensating measures when unavoidable.

# 87. Service Account Governance

Service accounts should have:

```text
Named Owner
Purpose
System
Privilege
Credential
Rotation
Monitoring
Retirement
```

# 88. Non-Human Identity Governance

Machine, application and workload identities should receive lifecycle and access governance equivalent to their risk.

# 89. Identity Security

Identity security should integrate with:

```text
Cybersecurity
Data Protection
Privacy
Application Security
Infrastructure Security
```

# 90. Identity Incident Integration

Identity-related security incidents should integrate with security incident management.

# 91. Access Change Integration

Access changes should integrate with enterprise change management where applicable.

# 92. Identity Lifecycle Integration

Identity lifecycle should integrate with:

```text
HR
Contract Management
Supplier Management
Customer Management
Application Management
```

where relevant.

# 93. Identity Data Quality

Identity records should be:

```text
Accurate
Complete
Current
Unique
Consistent
Traceable
```

# 94. Identity Reconciliation

Identity repositories should be reconciled against authoritative sources where appropriate.

# 95. Access Reconciliation

Material access records should be reconciled against source systems where practical.

# 96. Identity Exceptions

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
Identity Reviews
Access Reviews
Privileged Access Reviews
SoD Reviews
Authentication Reviews
Credential Reviews
Provisioning Reviews
Deprovisioning Reviews
Internal Audit
Independent Assurance
```

# 99. Identity Findings

Findings may identify weaknesses in:

```text
Identity Lifecycle
Authentication
Authorization
Provisioning
Deprovisioning
Privilege
Access Reviews
SoD
Credentials
Service Accounts
Monitoring
```

# 100. Identity Evidence

Evidence should support:

```text
Identity Creation
Proofing
Access Request
Approval
Provisioning
Privilege
Review
Removal
```

# 101. Identity Metrics

Metrics may include:

```text
Identity Inventory Accuracy
Joiner Completion
Mover Completion
Leaver Completion
Provisioning Time
Deprovisioning Time
MFA Coverage
Privileged Account Count
JIT Usage
Access Review Completion
SoD Conflicts
Dormant Accounts
Orphaned Accounts
Credential Rotation Compliance
Authentication Failure Rate
Identity Findings
Remediation Completion
```

# 102. Identity Dashboard

May include:

```text
Identity Population
Lifecycle
Access Requests
Approvals
Provisioning
Deprovisioning
MFA
Privileged Access
Access Reviews
SoD
Dormant Accounts
Orphaned Accounts
Authentication
Findings
Remediation
```

# 103. Daily Review

Where appropriate:

```text
Critical Authentication Events
Privileged Access
Emergency Access
Identity Incidents
High-Risk Access Requests
```

# 104. Weekly Review

May consider:

```text
Identity Lifecycle
Provisioning
Deprovisioning
Privileged Access
Authentication
Access Exceptions
Open Remediation
```

# 105. Monthly Review

May consider:

```text
Identity Performance
Access Review Status
MFA
Privileged Access
SoD
Dormant Accounts
Service Accounts
Identity Findings
```

# 106. Quarterly Review

May consider:

```text
Identity Strategy
IAM Architecture
Authentication
Authorization
PAM
Federation
Lifecycle
SoD
Identity Risk
Assurance
Maturity
```

# 107. Annual Review

May consider:

```text
Identity Strategy
Operating Model
Identity Architecture
Lifecycle
Authentication
Authorization
PAM
Federation
SSO
Role Model
SoD
Service Identities
Access Governance
Metrics
Assurance
Maturity
Improvement
```

# 108. Identity Maturity

Identity and access management maturity should be periodically assessed.

# 109. Maturity Dimensions

Assess:

```text
Governance
Strategy
Authority
Identity Types
Inventory
Proofing
Verification
Uniqueness
Status
Joiner
Mover
Leaver
Suspension
Reinstatement
Access Requests
Approval
Ownership
RBAC
ABAC
Policy-Based Access
Least Privilege
Need-to-Know
SoD
Provisioning
Automation
Deprovisioning
Expiry
Access Reviews
Certification
PAM
Privileged Identity
JIT
Elevation
Break-Glass
Session Monitoring
Authentication
MFA
Passwordless
Phishing Resistance
Adaptive Authentication
Credentials
Federation
SSO
Identity Providers
Directories
Groups
Roles
Entitlements
Access Analytics
Dormant Accounts
Orphaned Accounts
Shared Accounts
Service Accounts
Non-Human Identities
Security Integration
Incident Integration
Lifecycle Integration
Data Quality
Reconciliation
Exceptions
Remediation
Assurance
Metrics
Improvement
```

# 110. Maturity Levels

```text
1 – Initial
2 – Repeatable
3 – Defined
4 – Managed
5 – Optimized
```

# 111. Identity Creation Quality Gate

```text
Need
 ↓
Proof
 ↓
Verify
 ↓
Create
 ↓
Assign Attributes
 ↓
Approve
 ↓
Activate
```

must be controlled.

# 112. Access Quality Gate

```text
Need
 ↓
Request
 ↓
Risk
 ↓
Owner Approval
 ↓
Provision
 ↓
Validate
 ↓
Review
 ↓
Revoke
```

must be controlled.

# 113. Privileged Access Quality Gate

```text
Need
 ↓
Approval
 ↓
JIT / Time Limit
 ↓
Elevation
 ↓
Monitor
 ↓
Record
 ↓
Revoke
 ↓
Review
```

must be controlled.

# 114. Joiner-Mover-Leaver Quality Gate

```text
Authoritative Event
 ↓
Identity / Role Change
 ↓
Access Assessment
 ↓
Provision / Modify / Remove
 ↓
Validate
 ↓
Evidence
```

must be controlled.

# 115. Authentication Quality Gate

```text
Identity
 ↓
Risk
 ↓
Authentication Method
 ↓
Authenticate
 ↓
Authorize
 ↓
Monitor
```

must be controlled.

# 116. Access Review Quality Gate

```text
Population
 ↓
Owner
 ↓
Need
 ↓
Privilege
 ↓
Certify / Revoke
 ↓
Evidence
```

must be controlled.

# 117. Identity Assurance Quality Gate

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

# 118. Definition of Ready

An identity, access request, role, entitlement, privileged access session, authentication control, lifecycle event, exception, remediation or assurance review is Ready when identity, owner, purpose, resource, privilege, risk, duration, approval authority, dependencies, controls and acceptance criteria are defined.

# 119. Definition of Done

An identity and access work item is Done when:

```text
Requirement / Identity Event Identified
        ↓
Owner Assigned
        ↓
Identity / Access Action Completed
        ↓
Authentication / Authorization / Provisioning / Review / Removal Validated where Required
        ↓
Identity / Access / Role / Privilege Records Updated
        ↓
Evidence Captured
        ↓
Findings / Exceptions Addressed
        ↓
Outcome Accepted
```

# 120. Final Identity Governance Principle

> **MFM must ensure that every identity receives only the access required for its legitimate purpose, for the appropriate duration, through controlled authentication, authorization, provisioning, monitoring, review and removal.**

# 121. Final Identity Principle

> **Every material identity must be uniquely identifiable, owned, appropriately verified and managed throughout its lifecycle.**

# 122. Final Access Principle

> **Access must be granted only for legitimate business or service purposes, with appropriate authorization, least privilege and review.**

# 123. Final Authentication Principle

> **Authentication strength must be proportionate to identity assurance, resource sensitivity and access risk.**

# 124. Final Privilege Principle

> **Privileged access must be restricted, approved, time-limited where practical, monitored and fully accountable.**

# 125. Final Lifecycle Principle

> **Joiner, mover and leaver events must trigger timely and controlled changes to identity and access rights.**

# 126. Final Review Principle

> **Access must be periodically reviewed to confirm continuing business need, appropriate privilege and valid ownership.**

# 127. Final Service Identity Principle

> **Service and non-human identities must receive lifecycle, ownership, credential and access governance proportionate to their operational and security risk.**

# 128. Final Assurance Principle

> **Material identity and access controls must be supported by reliable evidence and periodically assessed through risk-based assurance.**

# 129. Final Improvement Principle

> **Identity incidents, access findings, privilege issues, lifecycle failures and assurance results must continuously improve MFM's identity capability.**

# 130. Final Integration Principle

> **Identity and Access Management must integrate with Cybersecurity, Data Management, Privacy, Enterprise Architecture, Application Management, IT Operations, Service Management, HR, Supplier Management, Customer Management, Change Management, Risk, Compliance, Legal and Business Continuity.**

# 131. Final Steady-State Identity Principle

> **MFM must ensure that every identity receives only the access required for its legitimate purpose, for the appropriate duration, through controlled authentication, authorization, provisioning, monitoring, review and removal.**

# 132. Summary

MFM v1.2-Steady-State-100 establishes the permanent Enterprise Identity and Access Management baseline.

It defines:

- Identity Governance / Identity Authority / Identity Types
- Workforce / External / Customer / Service / Machine / Privileged / Emergency Identities
- Identity Inventory / Attributes / Proofing / Verification / Uniqueness / Status
- Joiner / Mover / Leaver / Suspension / Reinstatement
- Access Request / Approval / Ownership
- RBAC / ABAC / Policy-Based Access
- Least Privilege / Need-to-Know / Separation of Duties
- Access Provisioning / Automation / Manual Provisioning / Removal / Expiry
- Access Review / Periodic Certification
- Privileged Access Management / JIT / Elevation / Break-Glass
- Privileged Session Monitoring / Evidence
- Authentication / MFA / Password / Passwordless / Phishing-Resistant / Adaptive Authentication
- Credential Management / Rotation / Recovery
- Federation / SSO / Identity Provider Governance
- Directory Services / Group Management / Nested Groups
- Role Management / Role Engineering / Role Lifecycle
- Entitlement Management / Entitlement Catalog / Access Bundles
- Access Analytics / Dormant / Orphaned / Shared Accounts
- Service Account / Non-Human Identity Governance
- Identity Security / Incident Integration / Change Integration / Lifecycle Integration
- Identity Data Quality / Identity and Access Reconciliation
- Identity Exceptions / Remediation / Assurance / Findings / Evidence
- Identity Metrics / Identity Dashboard
- Daily / Weekly / Monthly / Quarterly / Annual Reviews
- Identity Maturity
- Identity Creation / Access / Privileged / JML / Authentication / Access Review / Assurance Quality Gates
- Definition of Ready
- Definition of Done

# 133. Next Document

**MFM v1.2-Steady-State-101 – Enterprise Network Architecture, Network Operations, Connectivity, Segmentation, DNS, IPAM, Remote Access & Network Assurance**

It shall establish the permanent enterprise operating model for network architecture, network governance, connectivity, LAN/WAN, Internet connectivity, wireless, DNS, DHCP, IP address management, network segmentation, routing, switching, firewalls, remote access, VPN, network monitoring, network performance, network resilience, network configuration, network changes, network security integration, network incidents, network capacity, network assurance, findings, exceptions, remediation, network metrics, dashboards, maturity and continual enterprise network capability improvement supporting MFM.

# 134. Document Control

**Document:** MFM v1.2-Steady-State-100  
**Version:** 1.2  
**Status:** Steady-State Enterprise Identity & Access Management Baseline  
**Previous Document:** MFM v1.2-Steady-State-99  
**Next Document:** MFM v1.2-Steady-State-101  
**Lifecycle:** Steady-State Operation  
**Identity Authority:** Identity and Access Management  
**Authentication Authority:** Authentication / Identity Security  
**Authorization Authority:** Access Governance  
**Privileged Access Authority:** Privileged Access Management  
**Security Authority:** Cybersecurity / Information Security  
**Application Authority:** Enterprise Application Management  
**Architecture Authority:** Enterprise Architecture  
**Data Authority:** Enterprise Data Management  
**Privacy Authority:** Privacy / Data Protection  
**Operations Authority:** Enterprise IT Operations  
**Service Authority:** Enterprise Service Management  
**Configuration Authority:** Configuration Management  
**Asset Authority:** Enterprise Asset Management  
**HR Authority:** Human Resources / Workforce Administration  
**Supplier Authority:** Supplier / Third-Party Management  
**Customer Authority:** Customer / External Identity Management  
**Change Authority:** Enterprise Change Management  
**Risk Authority:** Enterprise Risk Management  
**Compliance Authority:** Enterprise Compliance  
**Legal Authority:** Legal / Regulatory Affairs  
**Continuity Authority:** Business Continuity / Operational Resilience  
**Project Authority:** Project / Portfolio Management  
**Assurance Authority:** Identity Assurance / Internal Audit / Independent Assurance  
**Improvement Authority:** Continual Enterprise Identity and Access Management Improvement  

**Principle:** MFM must ensure that every identity receives only the access required for its legitimate purpose, for the appropriate duration, through controlled authentication, authorization, provisioning, monitoring, review and removal.
