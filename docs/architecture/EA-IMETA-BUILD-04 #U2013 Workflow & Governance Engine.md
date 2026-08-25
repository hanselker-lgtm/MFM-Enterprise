# EA-IMETA-BUILD-04
# WORKFLOW & GOVERNANCE ENGINE

### Version 1.0
### Status: COMPLETE
### Governing Architecture: EA-IMETA-MASTER-01
### Previous Build: EA-IMETA-BUILD-03 – Metamodel Engine
### Implementation Basis: EA-IMETA-IMPLEMENTATION-03 and EA-IMETA-IMPLEMENTATION-04

---

# 1. PURPOSE

EA-IMETA-BUILD-04 defines the physical Workflow & Governance Engine of the EA-IMETA platform.

BUILD-01 established the technical foundation.

BUILD-02 established the repository and database.

BUILD-03 established the semantic Metamodel Engine.

BUILD-04 now establishes the controlled mechanism by which architecture information is:

```text
PROPOSED
→ REVIEWED
→ APPROVED
→ REJECTED
→ PUBLISHED
→ CHANGED
→ RETIRED
```

The central principle is:

> GOVERNANCE CONTROLS WHO MAY CHANGE ARCHITECTURE INFORMATION, WHY IT MAY CHANGE, HOW IT IS REVIEWED, AND WHO IS ACCOUNTABLE FOR THE DECISION.

---

# 2. BUILD-04 SCOPE

BUILD-04 covers:

```text
WORKFLOW DEFINITIONS
WORKFLOW INSTANCES
WORKFLOW STATES
TRANSITIONS
TASKS
ASSIGNMENTS
ROLES
PERMISSIONS
APPROVALS
DECISIONS
CHANGE REQUESTS
REVIEWS
ESCALATIONS
DELEGATION
SLAs
EVIDENCE
COMMENTS
NOTIFICATIONS
AUDIT
POLICY ENFORCEMENT
GOVERNANCE CONTROLS
SEPARATION OF DUTIES
EXCEPTION MANAGEMENT
WORKFLOW HISTORY
GOVERNANCE DASHBOARD FOUNDATION
```

BUILD-04 does not yet implement the full integration, AI, agent or adaptive layers.

---

# 3. GOVERNANCE MODEL

The governance architecture is:

```text
POLICY
  ↓
RULE
  ↓
WORKFLOW
  ↓
TASK
  ↓
REVIEW
  ↓
DECISION
  ↓
ACTION
  ↓
AUDIT
```

---

# 4. GOVERNANCE PRINCIPLE

The system must distinguish:

```text
CAN
```

from:

```text
MAY
```

and:

```text
SHOULD
```

Technical capability does not automatically grant authority.

---

# 5. AUTHORITY MODEL

The system shall enforce:

```text
CAPABILITY
≠
AUTHORITY
```

A user, service or AI agent may technically be able to perform an operation while still being prohibited from doing so.

---

# 6. WORKFLOW ROLE

The Workflow Engine orchestrates controlled changes.

```text
REQUEST
 ↓
VALIDATE
 ↓
ASSIGN
 ↓
REVIEW
 ↓
APPROVE
 ↓
EXECUTE
 ↓
VERIFY
 ↓
CLOSE
```

---

# 7. GOVERNANCE ROLE

The Governance Engine determines:

```text
WHO
WHAT
WHEN
WHY
UNDER WHICH POLICY
WITH WHICH EVIDENCE
WITH WHICH APPROVAL
```

---

# 8. WORKFLOW VS BUSINESS LOGIC

Workflow should not contain the core domain logic.

Prefer:

```text
WORKFLOW
 ↓
APPLICATION SERVICE
 ↓
DOMAIN
 ↓
REPOSITORY
```

Workflow orchestrates; domain services enforce business semantics.

---

# 9. WORKFLOW DEFINITION

A workflow definition describes a reusable process.

Conceptual table:

```text
workflow_definition
```

Fields:

```text
id
code
name
description
version
status
trigger_type
object_type
owner_id
created_at
created_by
updated_at
updated_by
```

---

# 10. WORKFLOW STATUS

Workflow definitions may be:

```text
DRAFT
ACTIVE
SUSPENDED
DEPRECATED
RETIRED
```

Only active definitions may normally create new workflow instances.

---

# 11. WORKFLOW VERSIONING

Workflow definitions are versioned.

An active workflow version should be immutable.

Changes create a new version.

---

# 12. WORKFLOW INSTANCE

A workflow instance represents one execution.

Conceptual table:

```text
workflow_instance
```

Fields:

```text
id
workflow_definition_id
workflow_version
subject_type
subject_id
status
started_at
started_by
completed_at
completed_by
priority
due_at
```

---

# 13. WORKFLOW INSTANCE STATUS

Initial states:

```text
PENDING
ACTIVE
WAITING
COMPLETED
REJECTED
CANCELLED
FAILED
SUSPENDED
```

---

# 14. WORKFLOW STATE

Each workflow has explicit states.

Conceptual table:

```text
workflow_state
```

Fields:

```text
id
workflow_definition_id
code
name
description
state_type
sequence
```

---

# 15. STATE TYPES

Examples:

```text
START
TASK
REVIEW
APPROVAL
WAIT
DECISION
END
```

---

# 16. TRANSITIONS

Transitions define valid movement between states.

Conceptual:

```text
workflow_transition
```

Fields:

```text
id
workflow_definition_id
from_state_id
to_state_id
code
condition
requires_authorization
```

---

# 17. TRANSITION VALIDATION

A transition shall validate:

```text
CURRENT STATE
ACTOR
ROLE
POLICY
REQUIRED DATA
REQUIRED EVIDENCE
```

---

# 18. TASKS

A task represents an actionable unit of work.

Conceptual table:

```text
workflow_task
```

Fields:

```text
id
workflow_instance_id
state_id
name
description
assigned_to
assigned_role
status
priority
created_at
started_at
due_at
completed_at
completed_by
```

---

# 19. TASK STATUS

Use:

```text
OPEN
IN_PROGRESS
BLOCKED
COMPLETED
CANCELLED
EXPIRED
```

---

# 20. TASK ASSIGNMENT

Tasks may be assigned to:

```text
USER
ROLE
TEAM
ORGANIZATION
SERVICE
```

The assignment must resolve to an accountable actor.

---

# 21. ACCOUNTABILITY

A workflow must always be able to answer:

```text
WHO OWNS THIS?
WHO IS DOING THIS?
WHO APPROVES THIS?
```

---

# 22. GOVERNANCE ROLE

A governance role is an authorization responsibility.

Examples:

```text
ARCHITECT
DOMAIN_OWNER
DATA_OWNER
SECURITY_REVIEWER
RISK_OWNER
APPROVER
GOVERNANCE_ADMIN
```

Roles are not necessarily job titles.

---

# 23. PERMISSION

A permission represents an allowed action.

Examples:

```text
OBJECT_VIEW
OBJECT_CREATE
OBJECT_UPDATE
OBJECT_RETIRE
WORKFLOW_START
WORKFLOW_ASSIGN
WORKFLOW_APPROVE
WORKFLOW_REJECT
METAMODEL_ACTIVATE
```

---

# 24. ROLE-PERMISSION MODEL

```text
USER
 ↓
ROLE
 ↓
PERMISSION
 ↓
ACTION
```

---

# 25. OBJECT-SCOPED AUTHORIZATION

Permissions may be scoped by:

```text
OBJECT TYPE
DOMAIN
ORGANIZATION
CLASSIFICATION
LIFECYCLE
PROJECT
```

---

# 26. POLICY

A policy defines a governance requirement.

Conceptual table:

```text
governance_policy
```

Fields:

```text
id
code
name
description
version
status
severity
owner_id
effective_from
effective_to
```

---

# 27. POLICY STATUS

```text
DRAFT
ACTIVE
SUSPENDED
SUPERSEDED
RETIRED
```

---

# 28. POLICY RULE

A policy may contain rules.

Conceptual:

```text
policy_rule
```

Fields:

```text
id
policy_id
code
description
rule_type
expression
severity
blocking
```

---

# 29. POLICY ENFORCEMENT

Policy enforcement may occur at:

```text
REQUEST
WORKFLOW START
TASK COMPLETION
APPROVAL
EXECUTION
PUBLICATION
RETIREMENT
```

---

# 30. POLICY PRIORITY

Policies may have:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

Conflicting policies require explicit precedence.

---

# 31. POLICY CONFLICT

The engine shall not silently choose between contradictory blocking policies.

It must produce:

```text
POLICY_CONFLICT
```

and route the matter for governance resolution.

---

# 32. CHANGE REQUEST

Material architecture changes should be represented by a change request.

Conceptual table:

```text
change_request
```

Fields:

```text
id
reference_id
title
description
change_type
subject_type
subject_id
requested_by
owner_id
priority
risk_level
status
created_at
updated_at
```

---

# 33. CHANGE TYPES

Examples:

```text
CREATE
MODIFY
RETIRE
RELATE
UNRELATE
METAMODEL_CHANGE
POLICY_CHANGE
ARCHITECTURE_DECISION
EXCEPTION
```

---

# 34. CHANGE STATUS

```text
DRAFT
SUBMITTED
UNDER_REVIEW
APPROVAL_PENDING
APPROVED
REJECTED
IMPLEMENTING
VERIFICATION
COMPLETED
CANCELLED
```

---

# 35. CHANGE RISK

Risk may be:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

Risk classification may determine required approval levels.

---

# 36. CHANGE IMPACT

A change request should eventually include:

```text
AFFECTED OBJECTS
AFFECTED RELATIONSHIPS
AFFECTED SYSTEMS
AFFECTED USERS
SECURITY IMPACT
DATA IMPACT
BUSINESS IMPACT
```

Detailed automated impact analysis uses later services.

---

# 37. REVIEW

A review evaluates a proposal before decision.

Conceptual:

```text
governance_review
```

Fields:

```text
id
change_request_id
review_type
reviewer
status
comments
started_at
completed_at
```

---

# 38. REVIEW TYPES

Examples:

```text
ARCHITECTURE
SECURITY
DATA
RISK
LEGAL
COMPLIANCE
OPERATIONS
FINANCIAL
```

---

# 39. REVIEW STATUS

```text
PENDING
IN_PROGRESS
APPROVED
APPROVED_WITH_CONDITIONS
REJECTED
WAIVED
```

---

# 40. APPROVAL

Approval is an explicit governance decision.

Conceptual:

```text
approval_record
```

Fields:

```text
id
change_request_id
approval_type
approver
decision
decision_at
conditions
reason
```

---

# 41. APPROVAL DECISIONS

```text
APPROVE
APPROVE_WITH_CONDITIONS
REJECT
DEFER
```

---

# 42. APPROVAL RULE

An approval is valid only when:

```text
APPROVER IS AUTHORIZED
APPROVAL IS WITHIN SCOPE
REQUIRED EVIDENCE EXISTS
POLICY REQUIREMENTS ARE SATISFIED
```

---

# 43. SEPARATION OF DUTIES

Where required:

```text
REQUESTER
≠
APPROVER
```

and:

```text
EXECUTOR
≠
FINAL APPROVER
```

unless an explicit exception is approved.

---

# 44. FOUR-EYES PRINCIPLE

High-risk changes should support:

```text
MAKER
+
CHECKER
```

At least two authorized actors participate.

---

# 45. DELEGATION

Delegation may be allowed.

Delegation must specify:

```text
DELEGATOR
DELEGATE
SCOPE
START
END
REASON
```

---

# 46. DELEGATION LIMITS

Delegation should not automatically transfer:

```text
SUPER-ADMIN
AUDIT ADMIN
METAMODEL ACTIVATION
CRITICAL SECURITY AUTHORITY
```

unless explicitly permitted.

---

# 47. ESCALATION

Workflows may escalate when:

```text
TASK OVERDUE
APPROVAL OVERDUE
RISK INCREASES
POLICY VIOLATION
CRITICAL FAILURE
```

---

# 48. SLA

A workflow task may have:

```text
response_due
completion_due
```

SLA definitions should be configurable.

---

# 49. SLA STATUS

```text
ON_TIME
AT_RISK
OVERDUE
BREACHED
```

---

# 50. SLA ESCALATION

Example:

```text
AT_RISK
 ↓
OWNER NOTIFICATION
 ↓
ESCALATION
 ↓
MANAGER
 ↓
GOVERNANCE BODY
```

---

# 51. EXCEPTION

A governance exception is an approved deviation from a policy or rule.

Conceptual:

```text
governance_exception
```

Fields:

```text
id
reference_id
policy_id
subject_type
subject_id
reason
risk
approved_by
valid_from
valid_to
status
```

---

# 52. EXCEPTION STATUS

```text
REQUESTED
UNDER_REVIEW
APPROVED
REJECTED
EXPIRED
REVOKED
```

---

# 53. EXCEPTION PRINCIPLE

An exception must never silently disable a policy.

It must be:

```text
EXPLICIT
SCOPED
TIME-BOUND
OWNED
AUDITED
```

---

# 54. TEMPORARY EXCEPTION

Exceptions should normally have an expiry date.

Permanent exceptions require stronger governance.

---

# 55. EVIDENCE

Governance decisions require evidence where policy demands it.

Evidence may include:

```text
DOCUMENT
REPORT
ANALYSIS
TEST RESULT
RISK ASSESSMENT
ARCHITECTURE DIAGRAM
SECURITY ASSESSMENT
```

---

# 56. EVIDENCE REQUIREMENTS

A workflow step may specify:

```text
MINIMUM EVIDENCE
EVIDENCE TYPE
CLASSIFICATION
VALIDITY PERIOD
```

---

# 57. COMMENTS

Workflow participants may add comments.

Comments should retain:

```text
AUTHOR
TIMESTAMP
TASK
CHANGE REQUEST
TEXT
```

Comments are part of the governance record where relevant.

---

# 58. DECISION RECORD

A material governance decision should produce a decision record.

Conceptual:

```text
decision_record
```

Fields:

```text
id
reference_id
decision_type
subject_type
subject_id
decision
rationale
decision_maker
decision_date
effective_date
review_date
```

---

# 59. DECISION RATIONALE

A decision should record:

```text
WHY
```

not merely:

```text
WHAT
```

---

# 60. DECISION EVIDENCE

Decision records should link to supporting evidence.

---

# 61. DECISION REVIEW

Some decisions require periodic review.

Example:

```text
DECISION
→ REVIEW IN 12 MONTHS
```

---

# 62. GOVERNANCE BODY

The platform should support governance bodies.

Examples:

```text
ARCHITECTURE BOARD
SECURITY BOARD
DATA GOVERNANCE BOARD
CHANGE ADVISORY BOARD
```

---

# 63. GOVERNANCE BODY MEMBERSHIP

Membership should specify:

```text
MEMBER
ROLE
SCOPE
VALID_FROM
VALID_TO
```

---

# 64. QUORUM

Governance decisions may require quorum.

Example:

```text
minimum 3 voting members
```

Quorum requirements are policy-specific.

---

# 65. VOTING

Where required, decisions may support:

```text
APPROVE
REJECT
ABSTAIN
```

Voting is optional and must not replace individual accountability.

---

# 66. CONFLICT OF INTEREST

A governance participant may need to declare:

```text
CONFLICT
```

A conflicted person may be excluded from the decision.

---

# 67. WORKFLOW TRIGGER

Workflow may start from:

```text
USER REQUEST
SYSTEM EVENT
SCHEDULE
POLICY VIOLATION
DATA CHANGE
METAMODEL CHANGE
RISK EVENT
INTEGRATION EVENT
```

---

# 68. AUTOMATIC TRIGGER

Automated triggers must still respect governance authorization.

An event may start a workflow, but it does not automatically approve the outcome.

---

# 69. WORKFLOW CONDITIONS

Conditions may inspect:

```text
OBJECT STATE
RISK
CLASSIFICATION
OWNER
VALUE
POLICY
ROLE
```

Conditions must use controlled expressions.

---

# 70. RULE SECURITY

No arbitrary executable code may be stored in workflow definitions.

Expressions must be:

```text
VALIDATED
ALLOW-LISTED
SANDBOXED WHERE REQUIRED
```

---

# 71. WORKFLOW ACTIONS

Actions may include:

```text
CREATE TASK
ASSIGN TASK
REQUEST REVIEW
REQUEST APPROVAL
UPDATE OBJECT
SEND NOTIFICATION
CREATE AUDIT RECORD
START CHILD WORKFLOW
```

---

# 72. ACTION AUTHORIZATION

Every material workflow action must pass authorization.

```text
WORKFLOW
 ↓
ACTION
 ↓
AUTHORIZATION
 ↓
APPLICATION SERVICE
```

---

# 73. CHILD WORKFLOWS

Complex governance processes may invoke child workflows.

Example:

```text
ARCHITECTURE CHANGE
 ↓
SECURITY REVIEW
 ↓
DATA REVIEW
 ↓
MAIN APPROVAL
```

---

# 74. WORKFLOW COMPOSITION

Child workflow results must be explicit.

Possible outcomes:

```text
PASS
FAIL
APPROVED
REJECTED
CONDITIONALLY_APPROVED
```

---

# 75. WORKFLOW CANCELLATION

A workflow may be cancelled by authorized actors.

Cancellation requires:

```text
REASON
ACTOR
TIMESTAMP
```

---

# 76. WORKFLOW SUSPENSION

Suspension pauses processing without closing the governance record.

Reason must be recorded.

---

# 77. WORKFLOW RESUMPTION

Resumption must verify that:

```text
POLICY
AUTHORITY
METAMODEL
DATA
```

remain valid.

---

# 78. WORKFLOW FAILURE

Technical failure must not be confused with governance rejection.

Use distinct states:

```text
FAILED
```

versus:

```text
REJECTED
```

---

# 79. RETRY

Technical workflow failures may be retried when safe.

Governance decisions should never be duplicated by automatic retry.

---

# 80. IDEMPOTENCY

Workflow actions that change governed information should support idempotency.

This prevents duplicate execution after retries.

---

# 81. WORKFLOW HISTORY

Every workflow state change should be recorded.

Conceptual:

```text
workflow_history
```

Fields:

```text
id
workflow_instance_id
from_state
to_state
actor
timestamp
reason
request_id
```

---

# 82. TASK HISTORY

Task changes should also be traceable.

---

# 83. APPROVAL HISTORY

Approval records are immutable once recorded.

Corrections should create a new governance event rather than overwrite history.

---

# 84. AUDIT

The Workflow & Governance Engine shall create audit events for:

```text
START
ASSIGN
REASSIGN
REVIEW
APPROVE
REJECT
ESCALATE
DELEGATE
EXCEPTION
EXECUTE
CANCEL
SUSPEND
RESUME
COMPLETE
```

---

# 85. AUDIT IMMUTABILITY

Governance history should be append-oriented.

Do not silently edit historical decisions.

---

# 86. REQUEST CORRELATION

Workflow operations should preserve:

```text
request_id
workflow_instance_id
change_request_id
actor
```

for traceability.

---

# 87. NOTIFICATIONS

Notifications may be triggered by:

```text
TASK ASSIGNMENT
DUE DATE
APPROVAL REQUEST
ESCALATION
REJECTION
COMPLETION
POLICY VIOLATION
```

---

# 88. NOTIFICATION CHANNELS

Possible channels:

```text
IN-APP
EMAIL
SYSTEM MESSAGE
INTEGRATION EVENT
```

Channel configuration belongs to the integration layer.

---

# 89. NOTIFICATION PRINCIPLE

Notification is not authorization.

Receiving a message does not grant permission.

---

# 90. WORKFLOW API

Initial API:

```text
/api/v1/workflows
/api/v1/workflows/{id}
/api/v1/workflows/{id}/tasks
/api/v1/workflows/{id}/history
/api/v1/change-requests
/api/v1/reviews
/api/v1/approvals
/api/v1/governance/policies
/api/v1/governance/exceptions
```

---

# 91. GOVERNANCE API

Read operations may expose governance status according to authorization.

Write operations must enforce role and policy.

---

# 92. APPROVAL API

Approval endpoints must:

```text
AUTHENTICATE
AUTHORIZE
VALIDATE
RECORD DECISION
AUDIT
```

---

# 93. API CONCURRENCY

Approval operations should use optimistic concurrency.

A stale approval page must not overwrite a newer governance state.

---

# 94. GOVERNANCE LOCK

Critical workflows may temporarily prevent conflicting changes.

Example:

```text
METAMODEL ACTIVATION
```

may lock conflicting metamodel modifications.

---

# 95. CHANGE COLLISION

The engine should detect concurrent change requests affecting the same subject.

Possible status:

```text
CONFLICT
```

---

# 96. GOVERNANCE QUEUE

Pending governance work should be queryable by:

```text
OWNER
ROLE
PRIORITY
RISK
SLA
AGE
```

---

# 97. GOVERNANCE DASHBOARD FOUNDATION

Metrics:

```text
OPEN CHANGE REQUESTS
PENDING APPROVALS
OVERDUE TASKS
HIGH-RISK CHANGES
POLICY VIOLATIONS
ACTIVE EXCEPTIONS
FAILED WORKFLOWS
```

Detailed dashboards belong to BUILD-07.

---

# 98. POLICY COMPLIANCE

The engine should calculate:

```text
COMPLIANT
NON-COMPLIANT
EXCEPTION
UNKNOWN
```

Unknown must not be treated as compliant.

---

# 99. POLICY VIOLATION

A violation should contain:

```text
policy
subject
severity
detected_at
evidence
status
owner
```

---

# 100. VIOLATION STATUS

```text
OPEN
ACKNOWLEDGED
REMEDIATING
RESOLVED
ACCEPTED_RISK
```

---

# 101. ACCEPTED RISK

An accepted risk is not the same as compliance.

It means:

```text
NON-COMPLIANCE EXISTS
+
AUTHORIZED RISK ACCEPTANCE EXISTS
```

---

# 102. GOVERNANCE ESCALATION

Critical violations should be escalated according to policy.

Example:

```text
CRITICAL
 ↓
DOMAIN OWNER
 ↓
SECURITY / RISK
 ↓
GOVERNANCE BOARD
```

---

# 103. POLICY EFFECTIVE DATES

Policies must support:

```text
effective_from
effective_to
```

A historical decision should be evaluated against the policy applicable at the time.

---

# 104. POLICY VERSIONING

Policies are immutable once active.

Changes create new versions.

---

# 105. POLICY RETROACTIVITY

A new policy should not silently invalidate historical decisions unless explicitly defined.

---

# 106. GOVERNANCE SCOPE

Policies and workflows may be scoped to:

```text
ENTERPRISE
DOMAIN
ORGANIZATION
OBJECT TYPE
PROJECT
ENVIRONMENT
CLASSIFICATION
```

---

# 107. GOVERNANCE INHERITANCE

A child scope may inherit governance from a parent.

Example:

```text
ENTERPRISE POLICY
 ↓
DOMAIN POLICY
 ↓
PROJECT POLICY
```

Conflict resolution must be explicit.

---

# 108. POLICY PRECEDENCE

Recommended precedence:

```text
LAW / REGULATION
 ↓
ENTERPRISE POLICY
 ↓
DOMAIN POLICY
 ↓
LOCAL PROCEDURE
```

Actual precedence must be configured for the organization.

---

# 109. REGULATORY RULES

Regulatory obligations should be represented separately from internal policy where possible.

This distinction improves auditability.

---

# 110. GOVERNANCE EVIDENCE

The system should preserve:

```text
POLICY
RULE
DECISION
EVIDENCE
APPROVER
EXECUTION
RESULT
```

as one traceable chain.

---

# 111. GOVERNANCE TRACE

A complete trace should look like:

```text
CHANGE REQUEST
      ↓
IMPACT ANALYSIS
      ↓
REVIEWS
      ↓
APPROVAL
      ↓
EXECUTION
      ↓
VERIFICATION
      ↓
DECISION RECORD
      ↓
AUDIT
```

---

# 112. VERIFICATION

After execution, the workflow should verify:

```text
EXPECTED STATE
ACTUAL STATE
POLICY COMPLIANCE
TEST RESULT
EVIDENCE
```

---

# 113. FAILED VERIFICATION

If verification fails:

```text
DO NOT CLOSE AS COMPLETED
```

The workflow should move to:

```text
REMEDIATION
```

or another defined failure path.

---

# 114. ROLLBACK

Governed changes should define rollback where technically possible.

Rollback itself is a controlled action and must be audited.

---

# 115. CHANGE REVERSAL

A reversal should not erase the original change.

It creates a new change event:

```text
CHANGE A
 ↓
REVERSAL B
```

---

# 116. GOVERNANCE DRY RUN

High-risk workflows may support a dry run:

```text
VALIDATE
IMPACT
POLICY
APPROVAL REQUIREMENTS
```

without executing the change.

---

# 117. SIMULATION

Simulation may produce:

```text
EXPECTED IMPACT
REQUIRED APPROVALS
POLICY VIOLATIONS
AFFECTED OBJECTS
```

---

# 118. GOVERNANCE BOUNDARY

The engine must not allow:

```text
AI recommendation
=
automatic approval
```

A recommendation and a governance decision are distinct.

---

# 119. AI GOVERNANCE FOUNDATION

Later AI services may:

```text
PREPARE CHANGE REQUEST
SUMMARIZE EVIDENCE
IDENTIFY POLICY CONFLICTS
RECOMMEND REVIEWERS
```

but authorization remains controlled by governance rules.

---

# 120. AGENT GOVERNANCE

An agent may be granted explicit permissions.

Example:

```text
AGENT
→ READ APPLICATIONS
→ CREATE DRAFT CHANGE REQUESTS
```

but not:

```text
ACTIVATE METAMODEL
```

unless explicitly authorized.

---

# 121. AUTONOMY BOUNDARY

Agent authority shall be:

```text
EXPLICIT
SCOPED
TIME-BOUND
AUDITED
REVOCABLE
```

---

# 122. EMERGENCY STOP

The governance layer shall provide an emergency stop mechanism for automated actions.

Emergency stop must:

```text
BLOCK NEW ACTIONS
PRESERVE HISTORY
IDENTIFY ACTIVE OPERATIONS
ESCALATE
```

---

# 123. GOVERNANCE SECURITY

Security requirements:

```text
LEAST PRIVILEGE
SEPARATION OF DUTIES
STRONG AUTHENTICATION
AUDIT
CLASSIFICATION
SCOPED AUTHORIZATION
```

---

# 124. GOVERNANCE DATA MODEL

Core entities:

```text
WORKFLOW_DEFINITION
WORKFLOW_INSTANCE
WORKFLOW_STATE
WORKFLOW_TRANSITION
WORKFLOW_TASK
CHANGE_REQUEST
REVIEW
APPROVAL
DECISION
POLICY
POLICY_RULE
EXCEPTION
VIOLATION
EVIDENCE
AUDIT_EVENT
DELEGATION
```

---

# 125. DATABASE RELATIONSHIP MODEL

Conceptual:

```text
CHANGE_REQUEST
      │
      ├──< REVIEW
      ├──< APPROVAL
      ├──< DECISION
      ├──< EVIDENCE
      └── WORKFLOW_INSTANCE
                │
                ├──< WORKFLOW_TASK
                └──< WORKFLOW_HISTORY

POLICY
   ├──< POLICY_RULE
   ├──< EXCEPTION
   └──< VIOLATION
```

---

# 126. WORKFLOW ENGINE SERVICE

Core service operations:

```text
START_WORKFLOW
GET_WORKFLOW
ASSIGN_TASK
COMPLETE_TASK
TRANSITION
ESCALATE
SUSPEND
RESUME
CANCEL
```

---

# 127. GOVERNANCE SERVICE

Core operations:

```text
CREATE_CHANGE_REQUEST
SUBMIT_REVIEW
RECORD_REVIEW
REQUEST_APPROVAL
RECORD_APPROVAL
CREATE_EXCEPTION
RESOLVE_VIOLATION
CREATE_DECISION
```

---

# 128. AUTHORIZATION SERVICE

Core operations:

```text
CAN_PERFORM
GET_PERMISSIONS
GET_EFFECTIVE_ROLE
CHECK_SEPARATION_OF_DUTIES
CHECK_POLICY
```

---

# 129. POLICY SERVICE

Core operations:

```text
GET_ACTIVE_POLICY
EVALUATE_POLICY
GET_VIOLATIONS
CHECK_EXCEPTION
```

---

# 130. SLA SERVICE

Core operations:

```text
CALCULATE_DUE_DATE
CHECK_SLA
ESCALATE
```

---

# 131. AUDIT SERVICE

Core operation:

```text
RECORD_GOVERNANCE_EVENT
```

Audit recording should be reliable and failure-aware.

---

# 132. TESTING

BUILD-04 testing shall include:

```text
WORKFLOW TESTS
AUTHORIZATION TESTS
POLICY TESTS
APPROVAL TESTS
SEPARATION OF DUTIES
DELEGATION
ESCALATION
SLA
EXCEPTION
AUDIT
CONCURRENCY
API
```

---

# 133. WORKFLOW TESTS

Verify:

```text
START
TRANSITION
TASK ASSIGNMENT
TASK COMPLETION
REJECTION
CANCELLATION
SUSPENSION
RESUMPTION
```

---

# 134. AUTHORIZATION TESTS

Verify:

```text
authorized action succeeds
unauthorized action fails
scope is respected
expired delegation fails
```

---

# 135. APPROVAL TESTS

Verify:

```text
authorized approval succeeds
unauthorized approval fails
maker/checker separation works
duplicate approval is prevented
stale approval is rejected
```

---

# 136. POLICY TESTS

Verify:

```text
compliant request
non-compliant request
exception
expired exception
policy conflict
```

---

# 137. SLA TESTS

Verify:

```text
on time
at risk
overdue
breached
escalated
```

---

# 138. AUDIT TESTS

Every material governance operation must generate the expected audit event.

---

# 139. NEGATIVE TESTING

Test:

```text
missing approver
invalid transition
expired policy
expired delegation
insufficient evidence
conflicting policy
unauthorized actor
duplicate decision
```

---

# 140. PERFORMANCE

Measure:

```text
WORKFLOW START
TASK ASSIGNMENT
AUTHORIZATION
POLICY EVALUATION
APPROVAL
AUDIT WRITE
```

Actual targets require workload evidence.

---

# 141. OBSERVABILITY

Metrics:

```text
ACTIVE WORKFLOWS
WORKFLOW FAILURES
APPROVAL AGE
SLA BREACHES
POLICY VIOLATIONS
EXCEPTIONS
AUTHORIZATION DENIALS
```

---

# 142. ALERTING

Alerts may be generated for:

```text
CRITICAL POLICY VIOLATION
CRITICAL SLA BREACH
REPEATED AUTHORIZATION FAILURE
WORKFLOW ENGINE FAILURE
AUDIT FAILURE
EMERGENCY STOP
```

---

# 143. AUDIT FAILURE

Failure to record a mandatory governance audit event must be treated as a serious system condition.

The system must not silently continue as if the audit succeeded.

---

# 144. DATA RETENTION

Governance records should be retained according to policy and regulatory requirements.

Approval and decision history must remain traceable.

---

# 145. PRIVACY

Governance records may contain personal information.

Access must follow:

```text
PURPOSE
CLASSIFICATION
AUTHORIZATION
RETENTION
```

---

# 146. WORKFLOW EXPORT

A workflow definition should be exportable for controlled deployment.

Package should include:

```text
DEFINITION
VERSION
STATES
TRANSITIONS
RULES
POLICIES
DOCUMENTATION
```

---

# 147. WORKFLOW IMPORT

Import must validate:

```text
VERSION
DEPENDENCIES
METAMODEL COMPATIBILITY
POLICY REFERENCES
ROLE REFERENCES
```

---

# 148. DEPLOYMENT

Workflow definitions should be deployed through controlled configuration or migration mechanisms.

Avoid manual production edits.

---

# 149. WORKFLOW COMPATIBILITY

Workflow definitions should declare compatible:

```text
EA-IMETA VERSION
METAMODEL VERSION
POLICY VERSION
```

---

# 150. BUILD-04 DELIVERABLES

BUILD-04 shall produce:

1. workflow definitions
2. workflow instances
3. workflow states
4. workflow transitions
5. workflow tasks
6. workflow history
7. role/permission foundation
8. authorization service
9. governance policies
10. policy rules
11. change requests
12. reviews
13. approvals
14. decision records
15. exceptions
16. violations
17. delegation
18. SLA foundation
19. escalation
20. evidence linkage
21. governance audit
22. workflow API
23. governance API
24. governance dashboard foundation
25. test suite
26. BUILD-04 acceptance report

---

# 151. BUILD-04 ACCEPTANCE CRITERIA

BUILD-04 is accepted when:

```text
[ ] Workflow definitions can be created
[ ] Workflow versions are supported
[ ] Workflow instances can start
[ ] States and transitions are enforced
[ ] Tasks can be assigned
[ ] Tasks can be completed
[ ] Invalid transitions are rejected
[ ] Roles and permissions are enforced
[ ] Object-scoped authorization works
[ ] Change requests can be created
[ ] Reviews can be requested
[ ] Approvals can be recorded
[ ] Separation of duties works
[ ] Delegation works
[ ] SLA tracking works
[ ] Escalation works
[ ] Policies can be evaluated
[ ] Exceptions are time-bound
[ ] Violations are tracked
[ ] Decisions are recorded
[ ] Evidence is linked
[ ] Audit history is preserved
[ ] Concurrency protection works
[ ] API tests pass
[ ] Workflow tests pass
[ ] Security tests pass
```

---

# 152. QUALITY GATE

BUILD-04 must pass:

```text
AUTHORITY
    ↓
POLICY
    ↓
WORKFLOW
    ↓
DECISION
    ↓
AUDIT
```

---

# 153. AUTHORITY GATE

Verify:

```text
role
permission
scope
delegation
separation of duties
```

---

# 154. POLICY GATE

Verify:

```text
active policy
rule evaluation
exceptions
violations
precedence
```

---

# 155. WORKFLOW GATE

Verify:

```text
states
transitions
tasks
SLA
escalation
failure handling
```

---

# 156. DECISION GATE

Verify:

```text
review
approval
rationale
evidence
decision maker
```

---

# 157. AUDIT GATE

Verify:

```text
complete history
immutable decisions
actor
timestamp
request correlation
```

---

# 158. BUILD-04 RISKS

Known risks:

```text
OVER-COMPLEX WORKFLOWS
AUTHORIZATION GAPS
POLICY CONFLICT
AUTOMATIC APPROVAL
AUDIT FAILURE
DELEGATION ABUSE
SLA NOISE
EXCEPTION CREEP
```

---

# 159. RISK MITIGATION

Use:

```text
SIMPLE WORKFLOW PRIMITIVES
+
EXPLICIT AUTHORITY
+
POLICY PRECEDENCE
+
SEPARATION OF DUTIES
+
IMMUTABLE DECISIONS
+
TIME-BOUND EXCEPTIONS
+
AUDIT
```

---

# 160. CRITICAL DESIGN DECISION

Workflow automation must never silently bypass governance.

Automation can accelerate:

```text
PREPARATION
ROUTING
VALIDATION
NOTIFICATION
```

but approval authority remains explicit.

---

# 161. CRITICAL AI DECISION

AI may:

```text
RECOMMEND
SUMMARIZE
CLASSIFY
PREPARE
```

but:

```text
RECOMMENDATION
≠
APPROVAL
```

unless a separately governed automation policy explicitly permits the action.

---

# 162. CRITICAL EXCEPTION DECISION

Exceptions are not a back door around governance.

Every exception must be:

```text
JUSTIFIED
APPROVED
SCOPED
TIME-BOUND
AUDITED
```

---

# 163. CRITICAL AUDIT DECISION

A governance decision without a reliable audit record is incomplete.

---

# 164. FINAL BUILD-04 PRINCIPLES

1. Governance controls authority.
2. Workflow controls process.
3. Policy defines requirements.
4. Metamodel defines semantic validity.
5. Repository stores governed information.
6. Decisions are explicit.
7. Approvals are attributable.
8. Separation of duties is enforced where required.
9. Delegation is scoped and temporary.
10. Exceptions are explicit and time-bound.
11. Audit history is preserved.
12. Technical failure is distinct from governance rejection.
13. AI recommendations are distinct from governance decisions.
14. Automated actions require explicit authorization.
15. Workflow definitions are versioned.
16. Policies are versioned.
17. Active definitions are immutable.
18. Concurrency is controlled.
19. Governance evidence is traceable.
20. No hidden bypasses are permitted.

---

# 165. BUILD-04 COMPLETION STATEMENT

EA-IMETA-BUILD-04 establishes the Workflow & Governance Engine that controls how architecture information is changed.

The physical architecture now progresses from:

```text
TECHNICAL FOUNDATION
        ↓
REPOSITORY
        ↓
METAMODEL
        ↓
GOVERNANCE
```

The next phase connects EA-IMETA to the surrounding enterprise:

```text
EXTERNAL SYSTEMS
DATA SOURCES
APIs
EVENTS
IMPORTS
EXPORTS
IDENTITY
SERVICES
```

Therefore:

> THE REPOSITORY STORES THE TRUTH; THE METAMODEL DEFINES ITS MEANING; GOVERNANCE CONTROLS ITS CHANGE; INTEGRATION CONNECTS IT TO THE ENTERPRISE.

---

# END OF EA-IMETA-BUILD-04
## WORKFLOW & GOVERNANCE ENGINE
## COMPLETE
