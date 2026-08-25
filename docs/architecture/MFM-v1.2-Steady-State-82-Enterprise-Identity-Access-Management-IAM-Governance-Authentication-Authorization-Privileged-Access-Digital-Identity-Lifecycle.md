# MFM v1.2-Steady-State-82
## Enterprise Identity & Access Management, IAM Governance, Authentication, Authorization, Privileged Access & Digital Identity Lifecycle

**Version:** 1.2  
**Document ID:** MFM v1.2-Steady-State-82  
**Status:** Steady-State Enterprise Identity & Access Management Baseline  
**Lifecycle:** Post-Implementation / Steady-State Operation  
**Document Type:** Identity / Access Management / Authentication / Authorization / Privileged Access / Digital Identity Lifecycle Management Document  

---

# 1. Purpose

This document establishes the eighty-second document in the MFM v1.2 Steady-State series.

It follows MFM v1.2-Steady-State-81 – Enterprise Cybersecurity, Information Security, Security Operations, Identity, Threat, Vulnerability & Security Incident Management.

The purpose is to establish the permanent enterprise operating model for digital identity governance, identity strategy, identity architecture, identity lifecycle management, joiner-mover-leaver processes, identity proofing, account provisioning, account deprovisioning, authentication, multi-factor authentication, authorization, role-based access control, attribute-based access control, privileged access management, administrative identities, service identities, machine identities, application identities, federation, single sign-on, credential management, secrets coordination, access requests, access approvals, access reviews, entitlement management, segregation of duties, identity risk, identity assurance, identity incidents, identity exceptions, identity findings, identity remediation, identity metrics, identity dashboards, identity maturity and continual identity governance improvement.

The central objective is:

> **MFM must ensure every digital identity has an accountable owner, appropriate access, appropriate authentication, controlled lifecycle management and auditable evidence throughout its existence.**

---

# 2. Scope

This document covers:

- Enterprise Identity & Access Management
- IAM Governance
- Identity Strategy
- Identity Architecture
- Digital Identity
- Identity Proofing
- Identity Lifecycle Management
- Joiner Management
- Mover Management
- Leaver Management
- Account Provisioning
- Account Deprovisioning
- Authentication
- Multi-Factor Authentication
- Password and Credential Management
- Authorization
- Role-Based Access Control
- Attribute-Based Access Control
- Entitlement Management
- Access Requests
- Access Approvals
- Access Reviews
- Privileged Access Management
- Administrative Identities
- Service Identities
- Machine Identities
- Application Identities
- Federation
- Single Sign-On
- Identity Integration
- Identity Risk Management
- Segregation of Duties
- Identity Monitoring
- Identity Incidents
- Identity Assurance
- Identity Findings
- Identity Exceptions
- Identity Remediation
- Identity Metrics
- Identity Dashboards
- Identity Maturity
- Continual Identity Governance Improvement

---

# 3. IAM Objective

The primary objective is:

> **Provide trusted, secure and appropriately governed identities and access to MFM services and information.**

# 4. Identity Lifecycle Objective

The primary objective is:

> **Ensure identities and access are created, changed, reviewed and removed consistently throughout the user lifecycle.**

# 5. Authentication Objective

The primary objective is:

> **Verify that an entity requesting access is appropriately identified and authenticated.**

# 6. Authorization Objective

The primary objective is:

> **Ensure authenticated identities receive only the access required for their approved responsibilities.**

# 7. Privileged Access Objective

The primary objective is:

> **Control elevated access through additional authorization, restriction, monitoring and review.**

# 8. Identity Assurance Objective

The primary objective is:

> **Maintain sufficient confidence that digital identities represent the intended individuals, organizations, services or machines.**

# 9. IAM Principles

Identity management should be:

```text
Identity-Centric
Least-Privilege
Risk-Based
Lifecycle-Controlled
Auditable
Standardized
Business-Aligned
Continuously Improved
```

# 10. Authentication Principles

Authentication should be:

```text
Appropriate
Strong
Risk-Based
Resistant to Credential Theft
Auditable
```

# 11. Authorization Principles

Authorization should be:

```text
Need-to-Know
Least-Privilege
Role / Attribute Based
Time-Bounded where Appropriate
Reviewable
```

# 12. Privileged Access Principles

Privileged access should be:

```text
Restricted
Approved
Monitored
Controlled
Reviewable
Revocable
```

# 13. Identity Lifecycle

The identity lifecycle should integrate:

```text
Identity Need
 ↓
Proof
 ↓
Create
 ↓
Provision
 ↓
Authenticate
 ↓
Authorize
 ↓
Review
 ↓
Change
 ↓
Suspend / Disable
 ↓
Deprovision
 ↓
Retain Evidence
```

# 14. Identity Governance

IAM governance should establish:

```text
Authority
Accountability
Policies
Standards
Roles
Approvals
Controls
Reporting
Escalation
```

# 15. Identity Ownership

Material identities and identity populations should have accountable owners.

# 16. Identity Classes

Identity classes may include:

```text
Employee
Contractor
Temporary Worker
Partner
Customer
Supplier
Service
Machine
Application
Device
Administrator
```

# 17. Identity Classification

Identity requirements should be proportionate to:

```text
Identity Type
Access Level
Data Sensitivity
Business Criticality
Risk
```

# 18. Identity Proofing

Identity proofing should establish sufficient confidence in identity attributes before issuing material credentials or access.

# 19. Identity Registration

Registration should establish appropriate:

```text
Unique Identifier
Identity Attributes
Owner
Source
Lifecycle Status
Assurance Level
```

# 20. Unique Identity

Where appropriate, each person should have a unique digital identity to support:

```text
Accountability
Authentication
Authorization
Audit
```

# 21. Duplicate Identity Management

Duplicate identities should be identified and resolved where practical.

# 22. Joiner Management

Joiner processes should ensure new identities receive only approved access required for their role.

# 23. Joiner Inputs

Joiner processing may use authoritative:

```text
Employment
Contract
Organizational
Role
Manager
Start Date
```

information.

# 24. Joiner Provisioning

Provisioning should follow:

```text
Identity Creation
 ↓
Authentication Setup
 ↓
Role Assignment
 ↓
Access Approval
 ↓
Application / Service Provisioning
 ↓
Validation
```

# 25. Mover Management

Changes in role, organization, responsibility or location should trigger appropriate access reassessment.

# 26. Mover Access

Mover processing should identify:

```text
Access to Remove
Access to Retain
Access to Add
```

# 27. Leaver Management

Leaver processing should remove or disable access according to approved timing and risk requirements.

# 28. Leaver Deprovisioning

Deprovisioning should address:

```text
Accounts
Authentication
Privileged Access
Applications
Cloud
Remote Access
Devices
Tokens
Sessions
```

# 29. Timeliness

Joiner, mover and leaver actions should occur within defined service and risk requirements.

# 30. Account Provisioning

Account provisioning should be:

```text
Authorized
Repeatable
Traceable
Validated
```

# 31. Account Deprovisioning

Deprovisioning should be:

```text
Controlled
Complete
Timely
Evidence-Based
```

# 32. Dormant Accounts

Dormant accounts should be identified and handled according to policy and risk.

# 33. Shared Accounts

Shared accounts should be avoided where individual accountability is required.

Where unavoidable, they should have:

```text
Owner
Business Justification
Access Controls
Monitoring
Periodic Review
```

# 34. Authentication

Authentication should use mechanisms proportionate to access risk.

# 35. Multi-Factor Authentication

MFA should be applied where required by:

```text
Risk
Policy
Regulation
Service Criticality
Access Sensitivity
```

# 36. Phishing-Resistant Authentication

Where risk justifies it, authentication methods resistant to credential phishing should be preferred.

# 37. Adaptive Authentication

Where technically appropriate, authentication may consider:

```text
User
Device
Location
Network
Behavior
Resource
Risk
```

# 38. Password Management

Where passwords remain in use, controls should address:

```text
Length
Protection
Reset
Reuse
Lockout / Rate Limiting
Compromise Response
```

# 39. Credential Protection

Credentials should be protected against:

```text
Disclosure
Replay
Theft
Unauthorized Use
```

# 40. Credential Lifecycle

Credentials should be:

```text
Issued
Protected
Rotated where Required
Revoked
Retired
```

# 41. Session Management

Sessions should have appropriate:

```text
Timeout
Reauthentication
Revocation
Monitoring
```

# 42. Authorization

Authorization should be based on approved:

```text
Role
Attributes
Entitlements
Business Need
```

# 43. Least Privilege

Access should be limited to the minimum required for approved duties.

# 44. Need-to-Know

Access to sensitive information should be limited according to legitimate business need.

# 45. Role-Based Access Control

RBAC should define access according to approved organizational roles where appropriate.

# 46. Role Design

Roles should have:

```text
Name
Purpose
Owner
Entitlements
Eligibility
Approval
Review Frequency
```

# 47. Attribute-Based Access Control

ABAC may use appropriate attributes such as:

```text
Identity
Role
Device
Location
Data
Risk
Context
```

# 48. Entitlement Management

Entitlements should be:

```text
Defined
Owned
Approved
Provisioned
Reviewed
Removed
```

# 49. Access Requests

Access requests should identify:

```text
Requester
Identity
Resource
Access
Business Need
Duration
Approver
```

# 50. Access Approval

Approvals should be provided by authorized decision-makers according to access risk and ownership.

# 51. Time-Bounded Access

Temporary access should have defined:

```text
Start
End
Owner
Purpose
```

# 52. Emergency Access

Emergency access should be:

```text
Restricted
Justified
Approved
Monitored
Reviewed
```

# 53. Privileged Access Management

PAM should protect elevated access to critical systems.

# 54. Privileged Account Classification

Privileged accounts may include:

```text
Domain / Directory Administrator
Cloud Administrator
Database Administrator
Network Administrator
Security Administrator
Application Administrator
Infrastructure Administrator
```

# 55. Separate Administrative Identity

Where appropriate, administrative activity should use separate privileged identities rather than ordinary user identities.

# 56. Privileged Credential Protection

Privileged credentials should receive enhanced protection such as:

```text
Vaulting
Rotation
MFA
Session Control
Monitoring
```

# 57. Just-in-Time Privileged Access

Where technically appropriate, privileged access should be granted for limited periods.

# 58. Privileged Session Monitoring

Material privileged sessions should be monitored according to risk and applicable requirements.

# 59. Privileged Access Review

Privileged access should be reviewed more frequently or rigorously than ordinary access where risk warrants.

# 60. Segregation of Duties

Conflicting access combinations should be identified and controlled where they could create unacceptable risk.

# 61. SoD Rules

SoD rules should define:

```text
Conflict
Risk
Owner
Compensating Control
Exception Process
```

# 62. Access Reviews

Access reviews should confirm:

```text
Need
Appropriateness
Owner Approval
Privilege
SoD
```

# 63. Access Review Frequency

Review frequency should be proportionate to:

```text
Risk
Privilege
Data Sensitivity
Business Criticality
```

# 64. Review Evidence

Reviews should retain sufficient evidence of:

```text
Population
Reviewer
Decision
Changes
Exceptions
Date
```

# 65. Access Certification

Where appropriate, accountable owners should certify access for their services, applications or information.

# 66. Identity Federation

Federation should be governed for:

```text
Trust
Identity Attributes
Authentication
Authorization
Lifecycle
Termination
```

# 67. Single Sign-On

SSO should be used where appropriate to improve:

```text
Security
User Experience
Centralized Control
```

# 68. Federation Trust

Federated relationships should have accountable owners and defined trust boundaries.

# 69. Identity Integration

Identity integrations should address:

```text
Provisioning
Authentication
Authorization
Deprovisioning
Error Handling
Monitoring
```

# 70. Identity Sources

Authoritative identity sources should be identified for relevant identity populations.

# 71. Identity Synchronization

Synchronization should be monitored for:

```text
Completeness
Accuracy
Timeliness
Failures
Duplicates
```

# 72. Service Identities

Service identities should have:

```text
Owner
Purpose
Scope
Credentials
Dependencies
Lifecycle
```

# 73. Machine Identities

Machine identities should be managed according to:

```text
Ownership
Authentication
Authorization
Credential / Certificate Lifecycle
Monitoring
```

# 74. Application Identities

Application identities should be governed for:

```text
Owner
Purpose
Permissions
Secrets
Certificates
Lifecycle
```

# 75. Certificate Identity

Certificates should be managed for:

```text
Ownership
Validity
Renewal
Revocation
Key Protection
```

# 76. Secrets Coordination

Identity governance should coordinate with secrets management for:

```text
API Keys
Tokens
Passwords
Certificates
Service Credentials
```

# 77. Identity Monitoring

Monitoring should detect relevant:

```text
Authentication Anomalies
Privilege Escalation
Impossible Travel / Unusual Location where Relevant
Credential Abuse
Account Takeover Indicators
Dormant Accounts
```

# 78. Identity Risk

Identity risks should be:

```text
Identified
Assessed
Owned
Treated
Monitored
```

# 79. Identity Incident Management

Identity incidents may include:

```text
Account Compromise
Credential Theft
Unauthorized Access
Privilege Abuse
Provisioning Failure
Deprovisioning Failure
Federation Failure
```

# 80. Identity Incident Response

Response should include appropriate:

```text
Containment
Credential Reset
Session Revocation
Access Removal
Investigation
Recovery
```

# 81. Identity Recovery

Recovery should restore trusted identity state after:

```text
Compromise
Corruption
Provisioning Failure
Directory Failure
Federation Failure
```

# 82. Identity Resilience

Critical identity services should have proportionate:

```text
Redundancy
Backup
Recovery
Monitoring
Continuity
```

# 83. Identity Assurance

Assurance may include:

```text
Access Reviews
Identity Audits
Configuration Reviews
PAM Reviews
SoD Reviews
Control Testing
```

# 84. Identity Findings

Findings may identify weaknesses in:

```text
Lifecycle
Authentication
Authorization
Privileged Access
Reviews
Federation
Service Identities
```

# 85. Identity Exceptions

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

# 86. Identity Remediation

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

# 87. Identity Metrics

Metrics may include:

```text
MFA Coverage
Provisioning Time
Deprovisioning Time
Access Review Completion
Privileged Access Count
Privileged Review Completion
Dormant Accounts
Orphaned Accounts
SoD Conflicts
Authentication Failures
Identity Incidents
Federation Availability
Service Identity Compliance
Certificate Expiry Risk
```

# 88. Identity Dashboard

May include:

```text
Identity Lifecycle
Authentication
MFA
Authorization
Privileged Access
Access Reviews
SoD
Service Identities
Federation
Identity Incidents
Exceptions
Findings
```

# 89. Daily Review

Where appropriate:

```text
Critical Authentication Failures
Privileged Access Alerts
Account Compromise Indicators
Identity Platform Issues
Certificate / Credential Expiry Risks
```

# 90. Weekly Review

May consider:

```text
Provisioning
Deprovisioning
Access Reviews
Privileged Access
Identity Incidents
Federation
Service Identities
```

# 91. Monthly Review

May consider:

```text
IAM Performance
MFA
Access Reviews
SoD
Privileged Access
Lifecycle Timeliness
Identity Risks
Findings
```

# 92. Quarterly Review

May consider:

```text
IAM Strategy
Identity Architecture
Critical Services
Privileged Access
Access Governance
Federation
Identity Resilience
Risk
Assurance
Maturity
```

# 93. Annual Review

May consider:

```text
Identity Strategy
IAM Governance
Lifecycle
Authentication
Authorization
PAM
Federation
Service Identities
Identity Security
Resilience
Assurance
Maturity
Improvement
```

# 94. IAM Maturity

IAM maturity should be periodically assessed.

# 95. Maturity Dimensions

Assess:

```text
Governance
Strategy
Architecture
Identity Proofing
Lifecycle
Joiner
Mover
Leaver
Provisioning
Deprovisioning
Authentication
MFA
Credential Management
Authorization
RBAC
ABAC
Entitlement Management
Access Requests
Access Approvals
Access Reviews
PAM
Administrative Identities
Service Identities
Machine Identities
Application Identities
Federation
SSO
Identity Integration
SoD
Monitoring
Incident Management
Resilience
Assurance
Metrics
Improvement
```

# 96. Maturity Levels

```text
1 – Initial
2 – Repeatable
3 – Defined
4 – Managed
5 – Optimized
```

# 97. Identity Creation Quality Gate

```text
Identity Need
 ↓
Proof
 ↓
Registration
 ↓
Owner
 ↓
Authentication
 ↓
Provisioning
 ↓
Validation
```

must be controlled.

# 98. Joiner Quality Gate

```text
Authoritative Source
 ↓
Identity Creation
 ↓
Role
 ↓
Access Approval
 ↓
Provision
 ↓
Validate
```

must be controlled.

# 99. Mover Quality Gate

```text
Role Change
 ↓
Review Existing Access
 ↓
Remove
 ↓
Add
 ↓
Approve
 ↓
Validate
```

must be controlled.

# 100. Leaver Quality Gate

```text
Termination
 ↓
Disable
 ↓
Revoke
 ↓
Remove Access
 ↓
Recover / Transfer Assets
 ↓
Validate
 ↓
Evidence
```

must be controlled.

# 101. Access Request Quality Gate

```text
Request
 ↓
Business Need
 ↓
Approval
 ↓
Provision
 ↓
Validate
 ↓
Review
```

must be controlled.

# 102. Privileged Access Quality Gate

```text
Need
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

# 103. Access Review Quality Gate

```text
Population
 ↓
Owner
 ↓
Review
 ↓
Decision
 ↓
Remove / Retain
 ↓
Evidence
```

must be traceable.

# 104. Identity Incident Quality Gate

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
Review
```

must be controlled.

# 105. Identity Assurance Quality Gate

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

# 106. Definition of Ready

An identity, identity lifecycle event, access request, role, entitlement, privileged access assignment, access review, federation relationship, service identity, identity incident, exception, remediation, assurance review or IAM improvement item is Ready when purpose, owner, identity population, resource, access, risk, dependencies, approval requirements, acceptance criteria and evidence requirements are defined.

# 107. Definition of Done

An IAM work item is Done when:

```text
Requirement Identified
        ↓
Owner Assigned
        ↓
Identity Action Completed
        ↓
Security / Business / Technical Validation Completed where Required
        ↓
Identity / Access Records Updated
        ↓
Evidence Captured
        ↓
Findings / Exceptions Addressed
        ↓
Outcome Accepted
```

# 108. Final IAM Principle

> **MFM must ensure every digital identity has an accountable owner, appropriate access, appropriate authentication, controlled lifecycle management and auditable evidence throughout its existence.**

# 109. Final Lifecycle Principle

> **Identity and access must be controlled from creation through change, review, suspension and deprovisioning.**

# 110. Final Authentication Principle

> **Authentication must provide assurance proportionate to the sensitivity and risk of the requested access.**

# 111. Final Authorization Principle

> **Authorization must provide only the access required for legitimate and approved responsibilities.**

# 112. Final Privileged Access Principle

> **Privileged access must receive enhanced restriction, authorization, monitoring and review.**

# 113. Final Identity Resilience Principle

> **Critical identity services must remain sufficiently resilient to support secure access during disruption and recovery.**

# 114. Final Assurance Principle

> **Material identity controls, access decisions and lifecycle events must be supported by reliable evidence and periodically assessed for effectiveness.**

# 115. Final Improvement Principle

> **Identity incidents, access reviews, risk findings, authentication data and lifecycle performance must continuously improve MFM's identity governance.**

# 116. Final Integration Principle

> **Identity and Access Management must integrate with Cybersecurity, Enterprise Architecture, Applications, Infrastructure, Workplace, Data, Service Management, Suppliers, Privacy, Risk, Compliance, HR / People processes and Business Continuity.**

# 117. Final Steady-State IAM Principle

> **MFM must ensure every digital identity has an accountable owner, appropriate access, appropriate authentication, controlled lifecycle management and auditable evidence throughout its existence.**

# 118. Summary

MFM v1.2-Steady-State-82 establishes the permanent Enterprise Identity and Access Management baseline.

It defines:

- Enterprise IAM / IAM Governance / Identity Strategy / Identity Architecture
- Digital Identity / Identity Proofing / Registration / Unique Identity
- Identity Classes / Classification / Ownership
- Joiner / Mover / Leaver Management
- Account Provisioning / Deprovisioning / Dormant and Shared Accounts
- Authentication / MFA / Phishing-Resistant Authentication / Adaptive Authentication
- Password / Credential / Session Management
- Authorization / Least Privilege / Need-to-Know
- RBAC / Role Design / ABAC
- Entitlement Management
- Access Requests / Approvals / Time-Bounded Access / Emergency Access
- Privileged Access Management / Administrative Identities
- Privileged Credential Protection / Just-in-Time Access / Session Monitoring / Reviews
- Segregation of Duties / SoD Rules
- Access Reviews / Certification / Evidence
- Identity Federation / SSO / Federation Trust
- Identity Integration / Identity Sources / Synchronization
- Service / Machine / Application Identities
- Certificate Identity / Secrets Coordination
- Identity Monitoring / Identity Risk
- Identity Incident Management / Response / Recovery / Resilience
- Identity Assurance / Findings / Exceptions / Remediation
- Identity Metrics / Identity Dashboard
- Daily / Weekly / Monthly / Quarterly / Annual Reviews
- IAM Maturity
- Identity Creation / Joiner / Mover / Leaver / Access Request / Privileged Access / Access Review / Identity Incident / Identity Assurance Quality Gates
- Definition of Ready
- Definition of Done

# 119. Next Document

**MFM v1.2-Steady-State-83 – Enterprise Data Governance, Data Management, Data Quality, Metadata, Master Data, Data Lifecycle & Data Protection Management**

It shall establish the permanent enterprise operating model for data governance, data ownership, data classification, data domains, metadata, data quality, master data, reference data, data lifecycle, data retention, data lineage, data stewardship, data architecture coordination, data protection coordination and continual enterprise data management improvement supporting MFM.

# 120. Document Control

**Document:** MFM v1.2-Steady-State-82  
**Version:** 1.2  
**Status:** Steady-State Enterprise Identity & Access Management Baseline  
**Previous Document:** MFM v1.2-Steady-State-81  
**Next Document:** MFM v1.2-Steady-State-83  
**Lifecycle:** Steady-State Operation  
**IAM Authority:** Enterprise Identity & Access Management  
**Identity Governance Authority:** Identity Governance  
**Authentication Authority:** Authentication / Identity Security  
**Privileged Access Authority:** Privileged Access Management  
**Cybersecurity Authority:** Enterprise Cybersecurity / Information Security  
**Architecture Authority:** Enterprise Architecture / Security Architecture  
**Application Authority:** Enterprise Application Management  
**Infrastructure Authority:** Enterprise Infrastructure Management  
**Workplace Authority:** Enterprise Workplace Management  
**Data Authority:** Enterprise Data Management  
**Privacy Authority:** Privacy / Data Protection  
**Service Authority:** Enterprise Service Management  
**Supplier Authority:** Supplier / Third-Party Management  
**People Authority:** HR / People / Workforce Management  
**Risk Authority:** Enterprise Risk Management  
**Compliance Authority:** Compliance / Regulatory Governance  
**Continuity Authority:** Business Continuity / Disaster Recovery  
**Assurance Authority:** IAM Assurance / Internal Audit / Independent Assurance  
**Improvement Authority:** Continual Identity Governance Improvement  

**Principle:** MFM must ensure every digital identity has an accountable owner, appropriate access, appropriate authentication, controlled lifecycle management and auditable evidence throughout its existence.
