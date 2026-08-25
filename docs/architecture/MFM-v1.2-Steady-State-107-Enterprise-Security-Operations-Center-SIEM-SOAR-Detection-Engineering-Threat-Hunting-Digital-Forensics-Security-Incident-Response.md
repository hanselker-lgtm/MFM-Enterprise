# MFM v1.2-Steady-State-107
## Enterprise Security Operations Center, SIEM/SOAR, Detection Engineering, Threat Hunting, Digital Forensics & Security Incident Response

**Version:** 1.2  
**Document ID:** MFM v1.2-Steady-State-107  
**Status:** Steady-State Security Operations Center & Cybersecurity Response Baseline  
**Lifecycle:** Post-Implementation / Steady-State Operation  
**Document Type:** Security Operations Center / SIEM / SOAR / Detection Engineering / Threat Hunting / Digital Forensics / Security Incident Response Document  

---

# 1. Purpose

This document establishes the one-hundred-and-seventh document in the MFM v1.2 Steady-State series.

It follows MFM v1.2-Steady-State-106 – Enterprise Information Security Architecture, Cybersecurity Operations, Security Monitoring, Threat Management, Vulnerability Management & Security Assurance.

The purpose is to establish the permanent enterprise operating model for Security Operations Center governance, SIEM, SOAR, security event collection, detection engineering, security use-case management, alert triage, incident investigation, threat hunting, digital forensics, evidence handling, security orchestration, automated response, incident coordination, escalation, crisis integration, lessons learned, SOC metrics, dashboards, maturity and continual security operations capability improvement.

The central objective is:

> **MFM must operate a disciplined and risk-based security operations capability that continuously collects and analyzes relevant security telemetry, detects meaningful threats, investigates incidents, coordinates response, preserves evidence and converts operational learning into continual improvement.**

---

# 2. Scope

This document covers:

- Security Operations Center Governance
- SOC Operating Model
- SIEM
- SOAR
- Security Event Collection
- Detection Engineering
- Detection Use Cases
- Alert Management
- Alert Triage
- Security Incident Investigation
- Threat Hunting
- Digital Forensics
- Evidence Handling
- Security Orchestration
- Automated Response
- Incident Coordination
- Escalation
- Crisis Integration
- Lessons Learned
- SOC Metrics
- SOC Dashboards
- SOC Maturity
- Continual Security Operations Capability Improvement

---

# 3. SOC Governance Objective

The primary objective is:

> **Establish clear authority, accountability, operating procedures, technology ownership and assurance for enterprise security operations.**

# 4. SOC Operating Objective

The primary objective is:

> **Provide continuous and coordinated security monitoring, detection, analysis, investigation, response and escalation for material cyber threats and incidents.**

# 5. SIEM Objective

The primary objective is:

> **Collect, normalize, correlate, retain and analyze relevant security telemetry to support detection, investigation, response and assurance.**

# 6. SOAR Objective

The primary objective is:

> **Use controlled orchestration and automation to improve consistency, speed and traceability of security response without bypassing required human decision authority.**

# 7. Detection Engineering Objective

The primary objective is:

> **Develop, test, maintain and improve security detections that identify meaningful malicious or anomalous activity with acceptable confidence and operational value.**

# 8. Threat Hunting Objective

The primary objective is:

> **Proactively search for threats and suspicious activity that may not be identified through existing automated detection.**

# 9. Digital Forensics Objective

The primary objective is:

> **Collect, preserve, analyze and document digital evidence in a controlled and defensible manner appropriate to the incident and applicable requirements.**

# 10. Security Incident Response Objective

The primary objective is:

> **Coordinate timely containment, eradication, recovery and validation of security incidents while preserving evidence and maintaining business continuity.**

# 11. SOC Principles

Security operations should be:

```text
Continuous
Risk-Based
Evidence-Driven
Threat-Informed
Coordinated
Traceable
```

# 12. Detection Principles

Detection should be:

```text
Relevant
Tested
Tuned
Observable
Actionable
Lifecycle-Controlled
```

# 13. Response Principles

Response should be:

```text
Fast
Controlled
Proportionate
Coordinated
Documented
Recoverable
```

# 14. Forensic Principles

Forensics should preserve:

```text
Integrity
Authenticity
Traceability
Context
Confidentiality
```

# 15. SOC Lifecycle

Security operations should integrate:

```text
Collect
 ↓
Normalize
 ↓
Detect
 ↓
Triage
 ↓
Investigate
 ↓
Contain
 ↓
Eradicate
 ↓
Recover
 ↓
Validate
 ↓
Learn
 ↓
Improve
```

# 16. SOC Governance

SOC governance should establish:

```text
Authority
Ownership
Coverage
Standards
Escalation
Assurance
```

# 17. SOC Authority

SOC authority should define who may:

```text
Approve SOC Architecture
Approve Detection Standards
Approve Response Playbooks
Approve Automated Actions
Escalate Incidents
Declare Security Incidents
Request Crisis Support
Accept Security Risk
```

# 18. SOC Ownership

Material SOC capabilities should have accountable owners for:

```text
Technology
Processes
Detection
Response
Evidence
Metrics
Improvement
```

# 19. SOC Operating Model

The SOC operating model should define:

```text
Coverage
Roles
Responsibilities
Shift Model
Escalation
Technology
Processes
Service Levels
```

# 20. SOC Coverage

Coverage should define applicable:

```text
Hours
Systems
Locations
Cloud
Applications
Endpoints
Networks
Identity
Data
```

# 21. SOC Service Levels

SOC service levels should be defined according to:

```text
Incident Severity
Business Criticality
Detection Confidence
Operational Requirement
```

# 22. SOC Roles

Roles may include:

```text
SOC Manager
Security Analyst
Incident Responder
Detection Engineer
Threat Hunter
Forensic Specialist
Security Engineer
SOC Platform Administrator
Threat Intelligence Analyst
```

# 23. Role Separation

Where appropriate, duties should be separated for:

```text
Monitoring
Investigation
Approval
Response
Forensics
Assurance
```

# 24. Shift Handover

SOC shift handovers should capture:

```text
Active Incidents
Outstanding Alerts
Threat Intelligence
Detection Changes
System Issues
Open Actions
```

# 25. SOC Knowledge Management

SOC knowledge should include:

```text
Playbooks
Detection Documentation
Known Issues
Threat Intelligence
Incident History
Investigation Guidance
```

# 26. SIEM Architecture

SIEM architecture should provide:

```text
Collection
Normalization
Storage
Correlation
Detection
Search
Investigation
Retention
```

# 27. Security Data Sources

Relevant sources may include:

```text
Identity
Endpoint
Network
Firewall
Application
Cloud
Infrastructure
Database
Email
Security Tools
```

# 28. Log Source Inventory

Material security log sources should have:

```text
Owner
Purpose
Source
Format
Criticality
Retention
Health Monitoring
```

# 29. Log Onboarding

New security log sources should be:

```text
Assessed
Approved
Integrated
Validated
Monitored
Documented
```

# 30. Log Normalization

Where practical, security telemetry should be normalized to improve:

```text
Correlation
Search
Detection
Investigation
```

# 31. Log Quality

Log quality should consider:

```text
Completeness
Accuracy
Timestamp Integrity
Source Reliability
Continuity
```

# 32. Time Synchronization

Security-relevant systems should use appropriate time synchronization to support event correlation.

# 33. SIEM Retention

Security telemetry retention should align with:

```text
Security Need
Incident Investigation
Legal Requirements
Regulatory Requirements
Storage Constraints
```

# 34. SIEM Access

SIEM access should follow:

```text
Least Privilege
Role-Based Access
Need-to-Know
```

# 35. SIEM Security

The SIEM platform itself should be protected through:

```text
Authentication
Authorization
Monitoring
Backup
Change Control
```

# 36. SIEM Availability

Critical SIEM services should have resilience appropriate to operational requirements.

# 37. SIEM Search

Security analysts should have controlled capability to search relevant historical telemetry.

# 38. SIEM Correlation

Correlation should combine relevant events to improve detection and investigation.

# 39. Detection Engineering

Detection engineering should integrate:

```text
Threat Intelligence
Attack Techniques
Incident History
Risk
Telemetry
```

# 40. Detection Use Cases

Each material detection use case should have:

```text
Purpose
Threat
Data Sources
Logic
Severity
Owner
Testing
Tuning
Lifecycle
```

# 41. Detection Logic

Detection logic should be:

```text
Documented
Versioned
Tested
Reviewed
Monitored
```

# 42. Detection Testing

Detections should be tested for:

```text
True Positive
False Positive
Coverage
Performance
Data Dependency
```

# 43. Detection Tuning

Detection tuning should consider:

```text
False Positives
False Negatives
Business Context
Asset Criticality
Threat Context
```

# 44. Detection Coverage

Coverage should be assessed across relevant:

```text
Threats
Techniques
Assets
Identities
Applications
Cloud
Network
Endpoints
```

# 45. Detection Gaps

Material detection gaps should be recorded and risk-assessed.

# 46. Detection Retirement

Detections should be retired when:

```text
Obsolete
Duplicated
Unsupported
Low Value
No Longer Relevant
```

# 47. Alert Management

Alerts should be:

```text
Collected
Prioritized
Assigned
Triaged
Resolved
Recorded
```

# 48. Alert Severity

Severity should consider:

```text
Threat
Confidence
Asset Criticality
Data Sensitivity
Business Impact
Scope
```

# 49. Alert Triage

Triage should determine:

```text
Benign
False Positive
Suspicious
Confirmed Incident
```

# 50. Alert Enrichment

Alerts should be enriched where practical with:

```text
Asset
Identity
Threat Intelligence
Vulnerability
Business Context
Historical Activity
```

# 51. Alert Deduplication

Duplicate alerts should be correlated where practical to reduce analyst overload.

# 52. Alert Escalation

Alerts should be escalated according to:

```text
Severity
Confidence
Business Impact
Persistence
```

# 53. Case Management

Material security investigations should use controlled case records containing:

```text
Alert
Timeline
Analyst
Evidence
Actions
Findings
Disposition
```

# 54. Incident Declaration

Criteria should define when an alert or case becomes a formal security incident.

# 55. Incident Investigation

Investigation should establish:

```text
What Happened
When
Where
Who / What Was Involved
How
Impact
Scope
Persistence
```

# 56. Investigation Timeline

Material investigations should maintain a chronological event timeline.

# 57. Investigation Hypotheses

Investigators should document relevant hypotheses and supporting or contradictory evidence where appropriate.

# 58. Investigation Evidence

Evidence should be:

```text
Identified
Collected
Preserved
Analyzed
Recorded
```

# 59. Threat Hunting

Threat hunting should be planned using:

```text
Threat Intelligence
Known Techniques
Anomalies
Incident Lessons
Risk
```

# 60. Threat Hunt Hypothesis

Material hunts should begin with a defined hypothesis or research question.

# 61. Threat Hunt Scope

Hunts should define:

```text
Systems
Time Period
Data Sources
Techniques
Expected Evidence
```

# 62. Threat Hunt Results

Results should classify findings as:

```text
No Finding
Benign
Suspicious
Confirmed Threat
Detection Gap
```

# 63. Threat Hunt Improvement

Hunt findings should feed:

```text
Detection Engineering
Vulnerability Management
Security Architecture
Incident Response
```

# 64. Digital Forensics

Forensics should be initiated when evidence collection and analysis are required by:

```text
Incident Severity
Legal Need
Regulatory Need
Security Requirement
Investigation Complexity
```

# 65. Forensic Scope

Forensic scope may include:

```text
Endpoint
Server
Cloud
Network
Identity
Application
Email
Storage
```

# 66. Evidence Collection

Evidence collection should minimize unnecessary alteration of the source.

# 67. Evidence Integrity

Evidence integrity should be supported through appropriate:

```text
Hashing
Checks
Access Controls
Chain of Custody
```

# 68. Chain of Custody

Material evidence should maintain records of:

```text
Collector
Date / Time
Source
Transfer
Storage
Access
Analysis
Disposition
```

# 69. Evidence Storage

Evidence should be stored securely with controlled access.

# 70. Forensic Analysis

Analysis should be:

```text
Documented
Repeatable where Practical
Evidence-Based
Traceable
```

# 71. Forensic Reporting

Reports should document:

```text
Scope
Method
Evidence
Findings
Limitations
Conclusion
```

# 72. Security Orchestration

SOAR workflows should coordinate:

```text
Alert
Enrichment
Decision
Action
Evidence
Closure
```

# 73. Automated Response

Automation may perform predefined actions such as:

```text
Enrichment
Ticket Creation
Notification
Account Disablement
Endpoint Isolation
IP Blocking
Domain Blocking
```

only where approved and appropriately controlled.

# 74. Human Approval

High-impact automated actions should require appropriate human authorization unless formally approved for automatic execution.

# 75. Playbook Management

Response playbooks should have:

```text
Purpose
Trigger
Conditions
Actions
Owner
Approval
Testing
Version
Review
```

# 76. Playbook Testing

Playbooks should be tested through:

```text
Simulation
Tabletop
Technical Exercise
Controlled Execution
```

where appropriate.

# 77. Playbook Tuning

Playbooks should be improved based on:

```text
Incidents
Exercises
Analyst Feedback
Automation Results
Lessons Learned
```

# 78. Incident Coordination

Material incidents should establish:

```text
Incident Lead
Technical Lead
Security Lead
Business Contact
Communications
```

where appropriate.

# 79. Incident Escalation

Escalation should consider:

```text
Severity
Business Impact
Data Sensitivity
Persistence
External Reporting
```

# 80. Crisis Integration

Major cyber incidents should integrate with enterprise crisis management and business continuity arrangements.

# 81. Legal and Regulatory Coordination

Where applicable, security incident response should coordinate with:

```text
Legal
Privacy
Compliance
Regulatory
```

functions.

# 82. Communications

Incident communications should be:

```text
Accurate
Controlled
Timely
Need-to-Know
```

# 83. Recovery Coordination

SOC recovery activities should coordinate with:

```text
IT Operations
Application Operations
Infrastructure
Cloud
Network
Identity
Business Continuity
```

# 84. Post-Incident Review

Material incidents should undergo structured review.

# 85. Lessons Learned

Lessons learned should identify:

```text
Detection Improvements
Response Improvements
Control Improvements
Architecture Improvements
Process Improvements
Training Improvements
```

# 86. Detection-to-Response Feedback

Incident outcomes should feed back into:

```text
Detection
Threat Intelligence
Threat Hunting
Vulnerability Management
Security Architecture
```

# 87. SOC Platform Management

SOC platforms should have:

```text
Owner
Architecture
Configuration
Backup
Monitoring
Change Management
Lifecycle
```

# 88. SOC Change Management

Changes to SIEM, SOAR, detections and response playbooks should be:

```text
Requested
Assessed
Tested
Approved
Implemented
Validated
Recorded
```

# 89. SOC Configuration Management

SOC configurations should be controlled and versioned where practical.

# 90. SOC Availability

Critical SOC services should have appropriate resilience and recovery arrangements.

# 91. SOC Capacity

Capacity should consider:

```text
Event Volume
Data Sources
Analyst Workload
Retention
Search
Detection Processing
```

# 92. Analyst Workload

Analyst workload should be monitored to identify:

```text
Alert Fatigue
Backlog
Coverage Gaps
Skill Constraints
```

# 93. Alert Fatigue

Alert volume and quality should be managed to avoid excessive analyst overload.

# 94. SOC Training

SOC personnel should maintain skills relevant to:

```text
Detection
Investigation
Threat Intelligence
Forensics
Response
Tools
```

# 95. SOC Exercises

SOC exercises may include:

```text
Tabletop
Threat Hunt
Incident Simulation
Technical Exercise
Recovery Exercise
```

# 96. SOC Metrics

Metrics may include:

```text
Security Alerts
True Positive Rate
False Positive Rate
Mean Time to Triage
Mean Time to Detect
Mean Time to Investigate
Mean Time to Contain
Mean Time to Respond
Mean Time to Recover
Incident Volume
Incident Severity
Detection Coverage
Detection Gaps
Detection Tuning
Threat Hunt Volume
Threat Hunt Findings
Forensic Cases
Playbook Usage
Automation Success
Automation Failure
Analyst Backlog
Log Source Coverage
Log Source Health
SIEM Availability
SOAR Availability
Security Findings
Remediation Completion
```

# 97. SOC Dashboard

May include:

```text
SOC Health
Alerts
Incidents
Threats
Detection
Threat Hunting
Forensics
Response
Automation
Log Sources
SIEM
SOAR
Analyst Workload
Open Findings
```

# 98. Daily Review

Where appropriate:

```text
Critical Alerts
Active Incidents
Detection Health
Log Source Health
SOAR Failures
Threat Intelligence
Analyst Backlog
```

# 99. Weekly Review

May consider:

```text
Alert Quality
Incident Trends
Detection Changes
Threat Hunts
Forensic Cases
Playbook Performance
Analyst Workload
Open Actions
```

# 100. Monthly Review

May consider:

```text
SOC Performance
Detection Coverage
Incident Response
Threat Intelligence
Vulnerability Trends
Log Coverage
SIEM / SOAR Health
Automation
Training
Assurance
```

# 101. Quarterly Review

May consider:

```text
SOC Strategy
Operating Model
Coverage
Detection Capability
Threat Hunting
Forensics
Response
Automation
Technology
Skills
Third-Party Dependencies
Assurance
Maturity
```

# 102. Annual Review

May consider:

```text
SOC Strategy
Operating Model
Governance
Architecture
SIEM
SOAR
Detection Engineering
Threat Intelligence
Threat Hunting
Digital Forensics
Incident Response
Crisis Integration
Technology
Capacity
Skills
Supplier Risk
Assurance
Maturity
Improvement
```

# 103. SOC Maturity

Security operations capability maturity should be periodically assessed.

# 104. Maturity Dimensions

Assess:

```text
Governance
Strategy
Authority
Ownership
Operating Model
Coverage
Service Levels
Roles
Separation of Duties
Shift Handover
Knowledge Management
SIEM Architecture
Data Sources
Log Inventory
Log Onboarding
Normalization
Log Quality
Time Synchronization
Retention
Access
SIEM Security
Availability
Search
Correlation
Detection Engineering
Use Cases
Detection Logic
Testing
Tuning
Coverage
Gaps
Retirement
Alert Management
Severity
Triage
Enrichment
Deduplication
Escalation
Case Management
Incident Declaration
Investigation
Timeline
Hypotheses
Evidence
Threat Hunting
Hunt Hypothesis
Hunt Scope
Hunt Results
Hunt Improvement
Digital Forensics
Evidence Collection
Integrity
Chain of Custody
Storage
Analysis
Reporting
SOAR
Automation
Human Approval
Playbooks
Playbook Testing
Playbook Tuning
Incident Coordination
Escalation
Crisis Integration
Legal / Regulatory Coordination
Communications
Recovery Coordination
Post-Incident Review
Lessons Learned
Feedback Loops
Platform Management
Change Management
Configuration
Availability
Capacity
Analyst Workload
Alert Fatigue
Training
Exercises
Metrics
Assurance
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

# 106. SOC Architecture Quality Gate

```text
Business / Security Need
 ↓
Threat / Risk
 ↓
Coverage
 ↓
Telemetry
 ↓
SIEM / SOAR
 ↓
Detection
 ↓
Response
 ↓
Assurance
```

must be controlled.

# 107. Detection Quality Gate

```text
Threat
 ↓
Use Case
 ↓
Data Source
 ↓
Logic
 ↓
Test
 ↓
Deploy
 ↓
Monitor
 ↓
Tune
 ↓
Review
```

must be controlled.

# 108. Alert Quality Gate

```text
Alert
 ↓
Enrichment
 ↓
Triage
 ↓
Disposition
 ↓
Escalation
 ↓
Case / Incident
 ↓
Evidence
```

must be controlled.

# 109. Threat Hunt Quality Gate

```text
Hypothesis
 ↓
Scope
 ↓
Data
 ↓
Search
 ↓
Analysis
 ↓
Finding
 ↓
Detection / Control Improvement
```

must be controlled.

# 110. Forensic Quality Gate

```text
Need
 ↓
Scope
 ↓
Collection
 ↓
Integrity
 ↓
Chain of Custody
 ↓
Analysis
 ↓
Reporting
 ↓
Disposition
```

must be controlled.

# 111. Incident Response Quality Gate

```text
Detect
 ↓
Triage
 ↓
Investigate
 ↓
Contain
 ↓
Eradicate
 ↓
Recover
 ↓
Validate
 ↓
Learn
```

must be controlled.

# 112. Automation Quality Gate

```text
Trigger
 ↓
Condition
 ↓
Authorization
 ↓
Action
 ↓
Validation
 ↓
Evidence
 ↓
Review
```

must be controlled.

# 113. Definition of Ready

A SOC service, SIEM integration, detection use case, response playbook, threat hunt, forensic case, security incident, automation, exception, remediation or assurance review is Ready when purpose, owner, scope, affected assets, threat or risk, dependencies, required telemetry, authority, acceptance criteria and evidence requirements are defined.

# 114. Definition of Done

A SOC work item is Done when:

```text
Requirement / Threat / Incident Identified
        ↓
Owner Assigned
        ↓
SOC Action Completed
        ↓
Detection / Response / Evidence / Validation Completed where Required
        ↓
SOC / SIEM / SOAR / Case / Incident Records Updated
        ↓
Evidence Captured
        ↓
Findings / Exceptions Addressed
        ↓
Outcome Accepted
```

# 115. Final SOC Governance Principle

> **MFM must operate a disciplined and risk-based security operations capability that continuously collects and analyzes relevant security telemetry, detects meaningful threats, investigates incidents, coordinates response, preserves evidence and converts operational learning into continual improvement.**

# 116. Final SIEM Principle

> **SIEM capability must provide trustworthy, sufficiently complete and appropriately retained security telemetry for detection, investigation, response and assurance.**

# 117. Final SOAR Principle

> **Security orchestration and automation must improve response speed and consistency while remaining controlled, auditable and proportionate to risk.**

# 118. Final Detection Principle

> **Security detections must be threat-informed, tested, tuned, measurable and continuously improved.**

# 119. Final Hunting Principle

> **Threat hunting must proactively test relevant hypotheses and convert findings into improved detections, controls, architecture and response capability.**

# 120. Final Forensics Principle

> **Digital evidence must be collected, preserved, analyzed and documented in a controlled and traceable manner appropriate to the incident and applicable requirements.**

# 121. Final Incident Principle

> **Security incidents must be handled through coordinated detection, investigation, containment, eradication, recovery, validation and learning.**

# 122. Final Improvement Principle

> **Every material SOC incident, detection gap, threat hunt, forensic finding, automation failure and assurance result must contribute to continual improvement.**

# 123. Final Integration Principle

> **Security Operations must integrate with Enterprise Architecture, Cybersecurity, Identity, Data, Applications, Infrastructure, Network, Cloud, Vulnerability Management, Service Management, Change Management, Risk, Compliance, Legal, Suppliers and Business Continuity.**

# 124. Final Steady-State SOC Principle

> **MFM must operate a disciplined and risk-based security operations capability that continuously collects and analyzes relevant security telemetry, detects meaningful threats, investigates incidents, coordinates response, preserves evidence and converts operational learning into continual improvement.**

# 125. Summary

MFM v1.2-Steady-State-107 establishes the permanent Security Operations Center and Cybersecurity Response baseline.

It defines:

- SOC Governance / Authority / Ownership / Operating Model
- SOC Coverage / Service Levels / Roles / Separation of Duties
- Shift Handover / Knowledge Management
- SIEM Architecture / Security Data Sources / Log Source Inventory
- Log Onboarding / Normalization / Quality / Time Synchronization
- SIEM Retention / Access / Security / Availability / Search / Correlation
- Detection Engineering / Use Cases / Logic / Testing / Tuning / Coverage / Gaps / Retirement
- Alert Management / Severity / Triage / Enrichment / Deduplication / Escalation
- Case Management / Incident Declaration / Investigation / Timelines / Hypotheses
- Investigation Evidence
- Threat Hunting / Hypotheses / Scope / Results / Improvement
- Digital Forensics / Evidence Collection / Integrity / Chain of Custody
- Forensic Storage / Analysis / Reporting
- SOAR / Security Orchestration / Automated Response
- Human Approval / Playbook Management / Playbook Testing / Tuning
- Incident Coordination / Escalation / Crisis Integration
- Legal / Regulatory Coordination / Communications
- Recovery Coordination / Post-Incident Review / Lessons Learned
- Detection-to-Response Feedback
- SOC Platform Management / Change / Configuration / Availability / Capacity
- Analyst Workload / Alert Fatigue / Training / Exercises
- SOC Metrics / SOC Dashboard
- Daily / Weekly / Monthly / Quarterly / Annual Reviews
- SOC Maturity
- SOC Architecture / Detection / Alert / Threat Hunt / Forensic / Incident / Automation Quality Gates
- Definition of Ready
- Definition of Done

# 126. Next Document

**MFM v1.2-Steady-State-108 – Enterprise Identity & Access Management, IAM Governance, Privileged Access, Authentication, Authorization & Identity Assurance**

It shall establish the permanent enterprise operating model for identity governance, identity lifecycle, joiner-mover-leaver processes, authentication, authorization, privileged access management, service identities, federation, single sign-on, access reviews, entitlement governance, segregation of duties, identity monitoring, identity incidents, identity exceptions, identity remediation, identity assurance, identity metrics, dashboards, maturity and continual enterprise identity capability improvement supporting MFM.

# 127. Document Control

**Document:** MFM v1.2-Steady-State-107  
**Version:** 1.2  
**Status:** Steady-State Security Operations Center & Cybersecurity Response Baseline  
**Previous Document:** MFM v1.2-Steady-State-106  
**Next Document:** MFM v1.2-Steady-State-108  
**Lifecycle:** Steady-State Operation  
**SOC Authority:** Security Operations Center  
**SIEM Authority:** Security Information and Event Management  
**SOAR Authority:** Security Orchestration / Automation  
**Detection Authority:** Detection Engineering  
**Threat Hunting Authority:** Threat Hunting  
**Forensic Authority:** Digital Forensics  
**Incident Authority:** Security Incident Response  
**Threat Intelligence Authority:** Threat Intelligence / Threat Management  
**Vulnerability Authority:** Vulnerability Management  
**Security Architecture Authority:** Enterprise Security Architecture  
**Cybersecurity Authority:** Information Security / Cybersecurity  
**Identity Authority:** Identity and Access Management  
**Data Authority:** Enterprise Data Management  
**Application Authority:** Enterprise Application Management  
**Infrastructure Authority:** Enterprise Infrastructure Architecture  
**Cloud Authority:** Enterprise Cloud Architecture  
**Network Authority:** Enterprise Network Architecture  
**Service Authority:** Enterprise Service Management  
**Configuration Authority:** Configuration Management  
**Asset Authority:** Enterprise Asset Management  
**Change Authority:** Enterprise Change Management  
**Supplier Authority:** Supplier / Third-Party Management  
**Risk Authority:** Enterprise Risk Management  
**Compliance Authority:** Enterprise Compliance  
**Legal Authority:** Legal / Regulatory Affairs  
**Continuity Authority:** Business Continuity / Operational Resilience  
**Project Authority:** Project / Portfolio Management  
**Assurance Authority:** Security Assurance / Internal Audit / Independent Assurance  
**Improvement Authority:** Continual Enterprise Security Operations Capability Improvement  

**Principle:** MFM must operate a disciplined and risk-based security operations capability that continuously collects and analyzes relevant security telemetry, detects meaningful threats, investigates incidents, coordinates response, preserves evidence and converts operational learning into continual improvement.
