# MFM v1.2-Steady-State-138
## Enterprise Identity & Access Management Architecture, Identity Governance, Authentication, Authorization, Privileged Access, Directory Services, Federation, SSO, MFA, Access Lifecycle, Identity Security, Access Reviews, Identity Monitoring, Identity Resilience, Identity Recovery & Identity Assurance

**Version:** 1.2  
**Document ID:** MFM v1.2-Steady-State-138  
**Status:** Steady-State Enterprise Identity & Access Management Baseline  
**Lifecycle:** Post-Implementation / Steady-State Operation  
**Document Type:** Identity Architecture / Identity Governance / Authentication / Authorization / Privileged Access / Directory Services / Federation / SSO / MFA / Access Lifecycle / Identity Security / Monitoring / Resilience / Recovery / Assurance Document  

---

# 1. Purpose

This document establishes the one-hundred-and-thirty-eighth document in the MFM v1.2 Steady-State series.

It follows MFM v1.2-Steady-State-137 – Enterprise Data Architecture & Data Management, Data Governance, Data Ownership, Data Classification, Data Lifecycle, Data Quality, Master Data, Reference Data, Metadata, Data Integration, Data Security, Data Privacy, Data Platform, Data Resilience, Data Retention & Data Assurance.

The purpose is to establish the permanent enterprise operating model for identity strategy, identity governance, identity architecture, identity ownership, directory services, authentication, authorization, federation, single sign-on, multi-factor authentication, privileged access, identity lifecycle, access lifecycle, identity security, access reviews, identity monitoring, identity resilience, identity recovery, identity suppliers, identity compliance, identity exceptions, remediation, identity assurance, metrics, dashboards, maturity and continual enterprise identity capability improvement.

The central objective is:

> **MFM must govern enterprise identities and access as controlled, secure, traceable and lifecycle-managed capabilities that ensure the right people, systems and services receive the right access to the right resources at the right time for the right purpose.**

---

# 2. Scope

This document covers:

- Identity Strategy
- Identity Governance
- Identity Architecture
- Identity Ownership
- Identity Lifecycle
- Account Lifecycle
- Joiner / Mover / Leaver
- Human Identity
- Workforce Identity
- Member / Customer Identity where Applicable
- Service Identity
- Machine Identity
- Workload Identity
- Directory Services
- Authentication
- Authorization
- Access Control
- Role-Based Access Control
- Attribute-Based Access Control where Applicable
- Federation
- Single Sign-On
- Multi-Factor Authentication
- Password Management
- Privileged Access Management
- Administrative Access
- Identity Proofing
- Identity Verification
- Access Requests
- Access Approvals
- Access Reviews
- Access Certification
- Identity Monitoring
- Identity Logging
- Identity Threat Detection
- Identity Security
- Identity Resilience
- Identity Recovery
- Credential Recovery
- Identity Backup
- Identity Suppliers
- Identity Compliance
- Identity Exceptions
- Identity Remediation
- Identity Assurance
- Identity Metrics
- Identity Dashboards
- Identity Maturity
- Continual Identity Capability Improvement

---

# 3. Identity Governance Objective

The primary objective is:

> **Establish clear authority, ownership, lifecycle controls, access standards, security requirements and assurance for enterprise identities and access.**

# 4. Identity Architecture Objective

The primary objective is:

> **Provide coherent identity services supporting users, applications, systems, devices, workloads and external parties across enterprise, cloud and third-party environments.**

# 5. Identity Security Objective

The primary objective is:

> **Protect identities, credentials, authentication mechanisms, privileged access and authorization decisions against misuse, compromise and unauthorized access.**

# 6. Access Management Objective

The primary objective is:

> **Ensure access is granted according to business need, identity assurance, least privilege, segregation of duties and approved authorization.**

# 7. Identity Operations Objective

The primary objective is:

> **Operate identity services reliably through disciplined lifecycle management, monitoring, support, incident response, recovery and continual improvement.**

# 8. Identity Resilience Objective

The primary objective is:

> **Ensure critical identity services remain available and recoverable during infrastructure, application, cloud, security or operational disruption.**

# 9. Identity Assurance Objective

The primary objective is:

> **Provide reliable evidence that identity, authentication, authorization, privileged access, lifecycle and monitoring controls operate effectively.**

# 10. Identity Principles

Identity should be:

```text
Unique
Owned
Verified
Secure
Traceable
Least-Privilege
Lifecycle-Controlled
Recoverable
Observable
Risk-Based
```

# 11. Access Principles

Access should be:

```text
Business-Justified
Explicitly Authorized
Least-Privilege
Time-Appropriate
Segregated where Required
Monitored
Reviewed
Revoked when No Longer Required
```

# 12. Identity Governance Principles

Identity governance should be:

```text
Accountable
Risk-Based
Policy-Driven
Architecture-Led
Evidence-Based
Continuously Improved
```

# 13. Identity Lifecycle

Identity should be governed through:

```text
Request / Establish
 ↓
Verify
 ↓
Provision
 ↓
Authenticate
 ↓
Authorize
 ↓
Use
 ↓
Monitor
 ↓
Review
 ↓
Modify
 ↓
Suspend / Revoke
 ↓
Retire
```

# 14. Access Lifecycle

Access should be governed through:

```text
Request
 ↓
Validate
 ↓
Approve
 ↓
Provision
 ↓
Use
 ↓
Monitor
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
Authority
Ownership
Identity Standards
Authentication
Authorization
Directories
Federation
SSO
MFA
Privileged Access
Lifecycle
Access Requests
Approvals
Reviews
Monitoring
Security
Resilience
Recovery
Suppliers
Compliance
Assurance
Improvement
```

# 16. Identity Authority

Identity authority should define who may:

```text
Approve Identity Strategy
Approve Identity Architecture
Approve Authentication Standards
Approve Authorization Standards
Approve Privileged Access Standards
Approve Material Identity Designs
Approve Material Identity Risk
Approve Material Identity Exceptions
```

# 17. Identity Ownership

Material identity services should have accountable ownership for:

```text
Purpose
Availability
Security
Performance
Lifecycle
Recovery
Compliance
Risk
```

# 18. Identity Sources

Identity sources should be defined for material identity populations.

Examples may include:

```text
HR
Membership
Customer Management
Supplier Management
Application
Directory
Identity Provider
```

# 19. Identity Authority Sources

The authoritative source for identity attributes should be identified where appropriate.

# 20. Identity Types

Identity types may include:

```text
Workforce Identity
Member Identity
Customer Identity
Supplier Identity
External Identity
Service Identity
Machine Identity
Device Identity
Workload Identity
Privileged Identity
Emergency / Break-Glass Identity
```

# 21. Unique Identity

Material identities should have unique identifiers.

Shared identities should be avoided unless there is a documented and approved operational requirement.

# 22. Identity Proofing

Where identity assurance is required, identity proofing should establish appropriate confidence in identity ownership.

# 23. Identity Verification

Verification requirements should align with:

```text
Risk
Identity Type
Access Level
Data Sensitivity
Business Impact
```

# 24. Workforce Identity

Workforce identities should be linked to an authoritative employment or organizational relationship where appropriate.

# 25. Joiner Process

Joiner processes should establish:

```text
Identity
Required Attributes
Baseline Access
Authentication
MFA
Role
Manager
Lifecycle State
```

# 26. Mover Process

Mover processes should ensure previous access is:

```text
Reviewed
Modified
Removed where No Longer Required
Replaced by New Access
```

# 27. Leaver Process

Leaver processes should ensure access is revoked appropriately and promptly.

This should include where applicable:

```text
Directory
Applications
Cloud
VPN
Privileged Access
Remote Access
Certificates
Tokens
Devices
```

# 28. Dormant Identities

Dormant identities should be identified and handled according to policy.

# 29. Identity Suspension

Identities may be suspended when:

```text
Employment Ends
Membership Ends
Security Risk Exists
Identity Integrity Is Uncertain
Policy Requires Suspension
```

# 30. Identity Retirement

Retirement should include:

```text
Access Revocation
Credential Revocation
Session Termination where Appropriate
Group Membership Removal
Application Access Removal
Asset Association Update
Evidence
```

# 31. Directory Services

Directory services should provide controlled identity information for authorized systems.

# 32. Directory Architecture

Directory architecture should define:

```text
Directories
Domains / Tenants
Trusts
Replication
Synchronization
Administrative Boundaries
Security
Monitoring
Recovery
```

# 33. Directory Synchronization

Synchronization should maintain:

```text
Accuracy
Consistency
Timeliness
Traceability
```

# 34. Directory Security

Directory services should be protected through:

```text
Strong Administration
Least Privilege
Monitoring
Configuration Control
Backup
Recovery
```

# 35. Authentication

Authentication should establish confidence that an identity is genuine before access is granted.

# 36. Authentication Factors

Authentication may use:

```text
Knowledge
Possession
Inherence
Device
Context
```

# 37. Multi-Factor Authentication

MFA should be required according to risk and policy, with stronger requirements for privileged, remote, sensitive or high-impact access.

# 38. MFA Resilience

MFA should provide controlled recovery options without undermining the security objective.

# 39. Password Management

Where passwords are used, controls should address:

```text
Length
Strength
Storage
Protection
Reset
Recovery
Reuse
Compromise Detection
```

# 40. Passwordless Authentication

Passwordless methods may be adopted where they provide appropriate security, usability and lifecycle control.

# 41. Single Sign-On

SSO should provide:

```text
Central Authentication
Consistent Access
Reduced Credential Exposure
Improved User Experience
Central Monitoring
```

# 42. Federation

Federation should support controlled trust between identity domains.

# 43. Federation Governance

Federated relationships should have:

```text
Owner
Trust Definition
Authentication Requirements
Attribute Requirements
Security Controls
Monitoring
Lifecycle
Exit
```

# 44. Authorization

Authorization should determine whether an authenticated identity may perform a defined action against a resource.

# 45. Least Privilege

Access should provide only the permissions necessary for the approved purpose.

# 46. Role-Based Access Control

RBAC may define access through:

```text
Role
Function
Organization
Service
Application
```

# 47. Attribute-Based Access Control

ABAC may use:

```text
Identity
Role
Device
Location
Risk
Resource
Action
Context
```

# 48. Access Policies

Access policies should define:

```text
Who
What
Where
When
Why
Under Which Conditions
```

# 49. Segregation of Duties

Conflicting access combinations should be identified and controlled where required.

# 50. Privileged Access

Privileged access should receive enhanced controls.

# 51. Privileged Access Management

PAM should address:

```text
Privileged Accounts
Credential Protection
Approval
Session Control
Monitoring
Recording where Appropriate
Time-Limited Access
Review
```

# 52. Privileged Identity Separation

Administrative privileges should be separated from normal user activity where appropriate.

# 53. Just-in-Time Privileged Access

JIT access may be used to reduce persistent privileged permissions.

# 54. Break-Glass Access

Emergency identities should be:

```text
Restricted
Protected
Monitored
Tested
Reviewed
```

# 55. Service Identities

Service identities should have:

```text
Owner
Purpose
Application / Service
Permissions
Credential
Rotation
Monitoring
Lifecycle
```

# 56. Machine Identities

Machine identities should be governed for:

```text
Ownership
Authentication
Certificates / Credentials
Authorization
Rotation
Monitoring
Lifecycle
```

# 57. Workload Identities

Workload identity should provide controlled authentication between applications, services and platforms.

# 58. Identity Credentials

Credentials should be:

```text
Protected
Scoped
Rotated
Monitored
Revoked
Recoverable where Appropriate
```

# 59. Certificates

Certificates should be managed for:

```text
Owner
Purpose
Validity
Renewal
Revocation
Key Protection
Lifecycle
```

# 60. Secrets

Secrets should be stored in approved secure mechanisms and should not be embedded in application source code where avoidable.

# 61. Access Requests

Access requests should include:

```text
Identity
Resource
Role / Permission
Purpose
Duration
Approver
Risk
```

# 62. Access Approval

Approvals should be performed by authorized decision-makers according to access risk and ownership.

# 63. Access Provisioning

Provisioning should be:

```text
Authorized
Traceable
Repeatable
Accurate
Timely
```

# 64. Automated Provisioning

Where appropriate, provisioning should be automated to reduce errors and improve lifecycle consistency.

# 65. Access Reviews

Access should be reviewed according to:

```text
Risk
Criticality
Sensitivity
Privilege
Regulatory Need
```

# 66. Access Certification

Access owners should periodically certify that access remains appropriate.

# 67. Privileged Access Reviews

Privileged access should receive enhanced and more frequent review where required.

# 68. Dormant Access

Dormant accounts and unused permissions should be identified and remediated.

# 69. Identity Monitoring

Identity services should be monitored for:

```text
Authentication
Authorization
Privilege
Provisioning
Deprovisioning
Failures
Anomalies
Configuration
```

# 70. Identity Logging

Material identity events should be logged according to:

```text
Security
Operational Need
Compliance
Investigation Need
Privacy
Retention
```

# 71. Identity Threat Detection

Identity monitoring should identify suspicious behavior such as:

```text
Impossible Travel where Relevant
Credential Abuse
Brute Force
Privilege Escalation
Unusual Access
MFA Abuse
Dormant Account Use
Administrative Anomalies
```

# 72. Identity Incident Management

Identity incidents should integrate with enterprise security and incident management.

# 73. Compromised Identity Response

Response may include:

```text
Suspend Identity
Revoke Sessions
Reset Credentials
Revoke Tokens
Remove Privileges
Investigate Activity
Restore Secure Access
```

# 74. Identity Configuration Management

Identity configurations should be:

```text
Baselined
Controlled
Reviewed
Backed Up
Recoverable
```

# 75. Identity Resilience

Critical identity services should address:

```text
Directory Failure
Identity Provider Failure
Network Failure
Cloud Failure
Certificate Failure
MFA Service Failure
Configuration Failure
Cybersecurity Event
```

# 76. Identity Redundancy

Critical identity services should use appropriate:

```text
Redundancy
Replication
Failover
Alternate Authentication
```

# 77. Identity Recovery

Recovery plans should define:

```text
Failure
Authority
Sequence
Dependencies
Directory Recovery
Identity Provider Recovery
MFA Recovery
Credential Recovery
Validation
```

# 78. Identity Recovery Testing

Critical identity recovery should be tested periodically.

# 79. Identity Backup

Where technically applicable, identity configuration and required identity data should be backed up securely.

# 80. Identity Change Management

Material identity changes should follow enterprise change-management requirements.

# 81. Identity Problem Management

Recurring identity failures should receive root-cause analysis.

# 82. Identity Support

Support arrangements should define:

```text
Coverage
Response
Resolution
Escalation
Specialist Support
```

# 83. Identity Supplier Management

Material identity suppliers should be governed for:

```text
Security
Availability
Performance
Support
Continuity
Compliance
Lifecycle
Cost
Exit
```

# 84. Identity Supplier Dependencies

Supplier dependencies should be identified for:

```text
Authentication
MFA
Federation
Directory
PAM
Certificates
Identity Proofing
```

# 85. Identity Exit Strategy

Material identity services should consider:

```text
Identity Data Export
Configuration Export
Credential Migration
Federation Transition
Application Dependencies
Recovery
Alternative Provider
Contract Exit
```

# 86. Identity Compliance

Identity services should comply with applicable:

```text
Policies
Standards
Contracts
Legal Requirements
Regulatory Requirements
Customer Requirements
```

# 87. Identity Exceptions

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

# 88. Identity Remediation

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

# 89. Identity Assurance

Assurance may include:

```text
Identity Architecture Reviews
Identity Inventory Reviews
Joiner / Mover / Leaver Reviews
Authentication Reviews
MFA Reviews
Authorization Reviews
RBAC Reviews
ABAC Reviews
SoD Reviews
PAM Reviews
Directory Reviews
Federation Reviews
SSO Reviews
Service Identity Reviews
Machine Identity Reviews
Certificate Reviews
Access Reviews
Access Certification
Identity Monitoring Reviews
Configuration Audits
Recovery Tests
Supplier Reviews
Compliance Assessments
Internal Audit
Independent Assurance
```

# 90. Identity Evidence

Evidence should support:

```text
Governance
Ownership
Identity Sources
Identity Types
Unique Identity
Proofing
Verification
Joiners
Movers
Leavers
Dormant Identities
Suspension
Retirement
Directories
Synchronization
Authentication
MFA
Passwords
Passwordless
SSO
Federation
Authorization
Least Privilege
RBAC
ABAC
SoD
PAM
Break-Glass
Service Identities
Machine Identities
Workload Identities
Credentials
Certificates
Secrets
Access Requests
Approvals
Provisioning
Access Reviews
Access Certification
Monitoring
Logging
Threat Detection
Incident Response
Configuration
Resilience
Recovery
Backup
Changes
Problems
Support
Suppliers
Compliance
Exceptions
Remediation
Assurance
```

# 91. Identity Metrics

Metrics may include:

```text
Identity Inventory Coverage
Unique Identity Coverage
Identity Ownership Coverage
Identity Source Accuracy
Joiner Completion SLA
Mover Completion SLA
Leaver Revocation SLA
Dormant Identity Rate
MFA Coverage
Privileged MFA Coverage
Passwordless Coverage
SSO Coverage
Federation Coverage
Authentication Success Rate
Authentication Failure Rate
Account Lockout Rate
Privileged Account Coverage
PAM Coverage
JIT Privilege Coverage
Break-Glass Review Coverage
Service Identity Ownership Coverage
Machine Identity Coverage
Workload Identity Coverage
Credential Rotation Compliance
Certificate Renewal Compliance
Secret Rotation Compliance
Access Request SLA
Access Approval SLA
Access Provisioning Accuracy
Access Review Completion
Access Certification Completion
SoD Violation Count
Excess Privilege Findings
Dormant Access Findings
Identity Security Incident Volume
Identity Anomaly Detection Volume
Identity Incident Resolution Time
Identity Configuration Compliance
Identity Recovery Test Success
RTO Achievement
Identity Availability
Identity Supplier SLA Achievement
Identity Compliance Coverage
Exception Age
Remediation Completion
Identity Assurance Findings
```

# 92. Identity Dashboard

May include:

```text
Identity Portfolio
Governance
Identity Sources
Workforce Identity
External Identity
Service Identity
Machine Identity
Workload Identity
Authentication
MFA
SSO
Federation
Authorization
RBAC
ABAC
SoD
PAM
Credentials
Certificates
Access Requests
Provisioning
Access Reviews
Monitoring
Threat Detection
Incidents
Resilience
Recovery
Suppliers
Compliance
Risk
Assurance
```

# 93. Daily Review

Where appropriate:

```text
Critical Authentication Alerts
Identity Provider Failures
MFA Failures
Privileged Access Alerts
Credential Abuse
Suspicious Logins
Provisioning Failures
Deprovisioning Failures
Directory Failures
Certificate Expiry Risks
Identity Supplier Incidents
Recovery Issues
```

# 94. Weekly Review

May consider:

```text
Authentication
MFA
SSO
Federation
Privileged Access
Access Requests
Provisioning
Deprovisioning
Identity Incidents
Threat Detection
Configuration
Certificates
Credentials
Access Reviews
Recovery
Supplier Issues
Open Remediation
```

# 95. Monthly Review

May consider:

```text
Identity Governance
Ownership
Architecture
Identity Sources
Lifecycle
Directories
Authentication
Authorization
MFA
SSO
Federation
PAM
Service Identities
Machine Identities
Workload Identities
Access Reviews
Monitoring
Security
Resilience
Recovery
Suppliers
Compliance
Exceptions
Remediation
Assurance
```

# 96. Quarterly Review

May consider:

```text
Identity Strategy
Architecture
Identity Lifecycle
Authentication Strategy
MFA
SSO
Federation
Authorization
PAM
SoD
Service / Machine / Workload Identity
Identity Security
Access Governance
Supplier Risk
Resilience
Recovery
Compliance
Assurance
Maturity
```

# 97. Annual Review

May consider:

```text
Identity Strategy
Operating Model
Governance
Ownership
Identity Sources
Identity Types
Lifecycle
Directory Architecture
Authentication
Authorization
MFA
SSO
Federation
PAM
RBAC
ABAC
SoD
Service Identity
Machine Identity
Workload Identity
Credentials
Certificates
Access Requests
Provisioning
Access Reviews
Monitoring
Threat Detection
Incidents
Resilience
Recovery
Backup
Suppliers
Compliance
Exceptions
Remediation
Assurance
Maturity
Improvement
```

# 98. Identity Maturity

Identity capability maturity should be periodically assessed.

# 99. Maturity Dimensions

Assess:

```text
Governance
Strategy
Authority
Ownership
Identity Sources
Identity Types
Unique Identity
Proofing
Verification
Joiner
Mover
Leaver
Dormant Identity
Suspension
Retirement
Directory Services
Synchronization
Authentication
MFA
Password Management
Passwordless
SSO
Federation
Authorization
Least Privilege
RBAC
ABAC
SoD
PAM
Privileged Identity
JIT Access
Break-Glass
Service Identity
Machine Identity
Workload Identity
Credentials
Certificates
Secrets
Access Requests
Approvals
Provisioning
Automation
Access Reviews
Certification
Monitoring
Logging
Threat Detection
Incident Response
Configuration
Resilience
Redundancy
Recovery
Backup
Change Management
Problem Management
Support
Supplier Management
Exit Strategy
Compliance
Exceptions
Remediation
Assurance
Evidence
Metrics
Improvement
```

# 100. Maturity Levels

```text
1 – Initial
2 – Repeatable
3 – Defined
4 – Managed
5 – Optimized
```

# 101. Identity Architecture Quality Gate

```text
Business Requirement
 ↓
Identity Type
 ↓
Authoritative Source
 ↓
Identity Proofing
 ↓
Authentication
 ↓
Authorization
 ↓
Least Privilege
 ↓
Security
 ↓
Monitoring
 ↓
Lifecycle
 ↓
Resilience
 ↓
Recovery
 ↓
Assurance
```

must be controlled.

# 102. Access Provisioning Quality Gate

```text
Request
 ↓
Identity Validation
 ↓
Business Need
 ↓
Resource
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
Monitor
 ↓
Review
```

must be controlled.

# 103. Privileged Access Quality Gate

```text
Request
 ↓
Identity Assurance
 ↓
Business Justification
 ↓
Privilege Scope
 ↓
Approval
 ↓
Time-Bound Provisioning where Appropriate
 ↓
Session / Activity Monitoring
 ↓
Review
 ↓
Revoke
```

must be controlled.

# 104. Identity Recovery Quality Gate

```text
Failure
 ↓
Assess
 ↓
Activate Recovery
 ↓
Recover Directory / Identity Provider
 ↓
Recover Authentication
 ↓
Recover MFA
 ↓
Recover Authorization
 ↓
Validate Security
 ↓
Validate Applications
 ↓
Confirm Service
 ↓
Review
```

must be controlled.

# 105. Identity Lifecycle Quality Gate

```text
Join
 ↓
Verify
 ↓
Provision
 ↓
Use
 ↓
Review
 ↓
Move
 ↓
Review
 ↓
Leave
 ↓
Revoke
 ↓
Retire
 ↓
Evidence
```

must be controlled.

# 106. Identity Assurance Quality Gate

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

# 107. Definition of Ready

An identity architecture, authentication service, authorization model, directory service, federation relationship, SSO capability, MFA arrangement, privileged access capability, identity lifecycle process, access request, access review, identity monitoring capability, recovery plan, supplier decision, exception, remediation or assurance review is Ready when purpose, owner, scope, identity population, dependencies, access requirements, security requirements, lifecycle requirements, resilience requirements, recovery requirements, risk, approval authority and acceptance criteria are defined.

# 108. Definition of Done

An identity work item is Done when:

```text
Requirement / Identity Event Identified
        ↓
Owner Assigned
        ↓
Identity Action Completed
        ↓
Identity / Authentication / Authorization / Security / Lifecycle / Monitoring / Resilience / Recovery Validation Completed where Required
        ↓
Identity / Directory / IAM / PAM / Application / CMDB / Service Records Updated
        ↓
Evidence Captured
        ↓
Findings / Exceptions Addressed
        ↓
Outcome Accepted
```

# 109. Final Identity Governance Principle

> **MFM must govern enterprise identities and access as controlled, secure, traceable and lifecycle-managed capabilities that ensure the right people, systems and services receive the right access to the right resources at the right time for the right purpose.**

# 110. Final Architecture Principle

> **Identity architecture must provide coherent, secure, resilient and observable identity services for workforce, external, service, machine and workload identities across enterprise, cloud and third-party environments.**

# 111. Final Authentication Principle

> **Authentication must establish appropriate confidence in identity before access is granted, with stronger controls applied according to risk and access sensitivity.**

# 112. Final Authorization Principle

> **Authorization must enforce least privilege, business need and appropriate segregation of duties, with access explicitly controlled and periodically reviewed.**

# 113. Final Privileged Access Principle

> **Privileged access must receive enhanced protection, monitoring, approval, lifecycle control and periodic certification.**

# 114. Final Lifecycle Principle

> **Identity and access must be actively managed from establishment and verification through provisioning, use, review, modification, revocation and retirement.**

# 115. Final Security Principle

> **Identity security must protect credentials, authentication, authorization, privileged access and identity infrastructure against compromise, misuse and unauthorized access.**

# 116. Final Resilience Principle

> **Critical identity services must have tested resilience and recovery capabilities sufficient to maintain or restore authorized access during disruptive events.**

# 117. Final Assurance Principle

> **Material identity and access controls must be supported by reliable evidence and periodically assessed through risk-based assurance.**

# 118. Final Improvement Principle

> **Identity incidents, access findings, privilege risks, lifecycle failures, authentication anomalies, recovery results, supplier issues and assurance findings must continuously improve MFM's identity capability.**

# 119. Final Enterprise Identity Integration Principle

> **Identity Architecture and Operations must integrate with Enterprise Architecture, Business Architecture, Applications, Data, Integration, Infrastructure, Network, Cloud, Cybersecurity, Service Management, Configuration Management, Asset Management, Suppliers, Finance, Risk, Compliance, Legal and Business Continuity.**

# 120. Final Steady-State Identity Principle

> **MFM must govern enterprise identities and access as controlled, secure, traceable and lifecycle-managed capabilities that ensure the right people, systems and services receive the right access to the right resources at the right time for the right purpose.**

# 121. Summary

MFM v1.2-Steady-State-138 establishes the permanent Enterprise Identity & Access Management Architecture baseline.

It defines:

- Identity Strategy / Governance / Authority / Ownership
- Identity Sources / Identity Types / Unique Identity
- Identity Proofing / Identity Verification
- Workforce Identity
- Joiner / Mover / Leaver
- Dormant Identity / Suspension / Retirement
- Directory Services / Directory Architecture / Synchronization / Security
- Authentication / Authentication Factors / MFA / MFA Resilience
- Password Management / Passwordless Authentication
- SSO / Federation / Federation Governance
- Authorization / Least Privilege / RBAC / ABAC / Access Policies
- Segregation of Duties
- Privileged Access / PAM / JIT / Break-Glass
- Service Identity / Machine Identity / Workload Identity
- Credentials / Certificates / Secrets
- Access Requests / Approval / Provisioning / Automation
- Access Reviews / Access Certification / Dormant Access
- Identity Monitoring / Logging / Threat Detection
- Identity Incident Management / Compromised Identity Response
- Configuration / Resilience / Redundancy / Recovery / Backup
- Change Management / Problem Management / Support
- Supplier Management / Supplier Dependencies / Exit Strategy
- Compliance / Exceptions / Remediation
- Identity Assurance / Evidence
- Identity Metrics / Identity Dashboard
- Daily / Weekly / Monthly / Quarterly / Annual Reviews
- Identity Maturity
- Architecture / Provisioning / Privileged Access / Recovery / Lifecycle / Assurance Quality Gates
- Definition of Ready
- Definition of Done

# 122. Next Document

**MFM v1.2-Steady-State-139 – Enterprise Integration Architecture & Integration Operations, Integration Governance, Integration Platforms, API Management, Messaging, Event Architecture, Data Integration, Service Integration, Integration Security, Integration Monitoring, Integration Resilience, Integration Capacity, Integration Lifecycle & Integration Assurance**

It shall establish the permanent enterprise operating model for integration strategy, integration governance, integration architecture, integration platforms, API management, messaging, event architecture, data integration, service integration, integration security, integration monitoring, integration performance, integration capacity, integration resilience, integration recovery, integration lifecycle, integration suppliers, integration compliance, integration exceptions, remediation, integration assurance, metrics, dashboards, maturity and continual enterprise integration capability improvement supporting MFM.

# 123. Document Control

**Document:** MFM v1.2-Steady-State-138  
**Version:** 1.2  
**Status:** Steady-State Enterprise Identity & Access Management Baseline  
**Previous Document:** MFM v1.2-Steady-State-137  
**Next Document:** MFM v1.2-Steady-State-139  
**Lifecycle:** Steady-State Operation  
**Identity Governance Authority:** Enterprise Identity & Access Management  
**Identity Architecture Authority:** Enterprise Identity Architecture  
**Directory Authority:** Directory Services Management  
**Authentication Authority:** Authentication / Identity Provider Management  
**Authorization Authority:** Access Management  
**Privileged Access Authority:** Privileged Access Management  
**Federation Authority:** Federation / SSO Management  
**MFA Authority:** Multi-Factor Authentication Management  
**Application Identity Authority:** Application / Workload Identity Management  
**Security Authority:** Identity Security / Enterprise Cybersecurity  
**Data Authority:** Enterprise Data Management  
**Service Authority:** Enterprise IT Service Management  
**Configuration Authority:** Configuration Management  
**Asset Authority:** Enterprise Asset Management  
**Supplier Authority:** Supplier / Third-Party Management  
**Finance Authority:** Financial Management / Technology Financial Management  
**Risk Authority:** Enterprise Risk Management  
**Compliance Authority:** Enterprise Compliance  
**Legal Authority:** Legal / Regulatory Affairs  
**Continuity Authority:** Business Continuity / Operational Resilience  
**Assurance Authority:** Identity Assurance / Internal Audit / Independent Assurance  
**Improvement Authority:** Continual Enterprise Identity Capability Improvement  

**Principle:** MFM must govern enterprise identities and access as controlled, secure, traceable and lifecycle-managed capabilities that ensure the right people, systems and services receive the right access to the right resources at the right time for the right purpose.
