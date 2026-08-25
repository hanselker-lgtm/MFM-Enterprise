# MFM v1.2-590 – Notifications, Background Jobs & Asynchronous Processing Implementation

Version: 1.2

Document ID: MFM-v1.2-590

Status: Implementation Execution Baseline

---

# 1. Purpose

This document defines the implementation baseline for notifications, background jobs and asynchronous processing in MaritimForeningsManager (MFM) v1.2.

It follows:

- MFM v1.2-500 – Architecture Consolidation & Implementation Readiness
- MFM v1.2-510 – Implementation Backlog, Work Packages & Traceability
- MFM v1.2-520 – Implementation Execution, Coding Standards & Development Workflow
- MFM v1.2-530 – Database Implementation, Schema Evolution & Migration Execution
- MFM v1.2-540 – Security Hardening, Secrets Management & Access Control Execution
- MFM v1.2-550 – Core Services & Domain Logic Implementation
- MFM v1.2-560 – Repository, Persistence Services & Data Access Implementation
- MFM v1.2-570 – GUI, Presentation Layer & User Workflow Implementation
- MFM v1.2-580 – Reporting, Dashboard & Read-Model Implementation

The purpose is to define how MFM performs non-blocking and deferred work while preserving business correctness, auditability and the authoritative ownership of each domain.

The document establishes:

- Notification Architecture
- Background Job Architecture
- Job Lifecycle
- Queuing
- Scheduling
- Retries
- Idempotency
- Failure Handling
- Email / Internal Notifications
- Report Jobs
- Backup Jobs
- Document Jobs
- Maintenance Jobs
- Job Security
- Job Monitoring
- Operational Recovery
- Testing
- Performance
- Traceability

---

# 2. Scope

This document covers:

- User Notifications
- Internal Notifications
- Email Notifications where configured
- Background Jobs
- Scheduled Jobs
- Deferred Processing
- Report Generation
- Backup Processing
- Document Processing
- Maintenance Processing
- Notification Delivery
- Retry Handling
- Job Monitoring

It does not introduce a mandatory distributed messaging platform.

---

# 3. Core Principle

MFM should use asynchronous processing only where it provides a practical benefit.

Examples:

```text
Large Report

↓

Background Job
```

```text
Email Notification

↓

Background Delivery
```

```text
Backup

↓

Maintenance Job
```

Simple operations should remain synchronous.

---

# 4. Small-Association Principle

MFM is intended for a small non-profit association.

The default architecture should therefore remain:

```text
Desktop Application

+

Local Database

+

Controlled Background Processing
```

Avoid introducing:

- Message Brokers
- Distributed Worker Clusters
- Container Orchestration
- Complex Event Streaming

unless future requirements genuinely justify them.

---

# 5. Asynchronous Boundary

The recommended flow is:

```text
Application Service

↓

Commit Business Transaction

↓

Create Job / Notification Request

↓

Background Processor

↓

Execute

↓

Record Result
```

The business transaction should normally complete before non-critical external work begins.

---

# 6. Business Transaction Principle

A notification failure should normally not roll back an already successful business transaction.

Example:

```text
Grant Saved

↓

Email Delivery

↓

Failure

```

Result:

```text
Grant = Saved

Notification = Failed / Retryable
```

---

# 7. Critical vs Non-Critical Work

Operations should be classified.

### Critical

Must succeed as part of the business transaction.

Examples may include:

- Accounting Ledger Posting
- Required Domain State Change

### Non-Critical

May occur after the transaction.

Examples:

- Email
- Dashboard Refresh
- Report Notification
- Optional Integration

---

# 8. Job Model

A background job should have a controlled lifecycle.

Typical states:

```text
Queued

↓

Running

↓

Succeeded
```

or:

```text
Queued

↓

Running

↓

Failed

↓

Retrying

↓

Succeeded
```

Terminal failure may be:

```text
Failed
```

---

# 9. Job Identity

Each job should have a unique identifier.

Example:

```text
JOB-2026-000123
```

The exact ID strategy follows the established MFM implementation.

---

# 10. Job Record

A job may contain:

```text
Job ID

Type

Status

Created At

Scheduled At

Started At

Completed At

Attempt Count

Maximum Attempts

Correlation ID

Requested By

Payload Reference

Error Reference
```

---

# 11. Job Payload

Job payloads should contain only the information required to execute the job.

Prefer references such as:

```text
report_id

project_id

document_id
```

rather than duplicating large business objects.

---

# 12. Sensitive Job Data

Do not place secrets or unnecessary personal information into job payloads.

Examples of prohibited payload content where avoidable:

```text
Plaintext Password

API Secret

Full Credential

Unnecessary Personal Data
```

---

# 13. Job Queue

For the current MFM scale, a database-backed job queue is sufficient where background processing is required.

Conceptually:

```text
jobs
```

or an equivalent existing table may contain queued work.

---

# 14. Queue Ownership

The Job Service owns job lifecycle management.

Domain services own the business operation that requests the job.

---

# 15. Job Creation

A service may create a job:

```text
Request Business Operation

↓

Commit Business State

↓

Create Job
```

If the job must be guaranteed to exist with the business transaction, the job record may be created within the same database transaction.

---

# 16. Transactional Job Creation

Where appropriate:

```text
Business Change

+

Job Record

↓

One Transaction

↓

Commit
```

This prevents:

```text
Business Change committed

Job request lost
```

---

# 17. Outbox-Style Principle

For important deferred actions, MFM may use a lightweight outbox pattern.

Example:

```text
Business Transaction

↓

Outbox / Job Record

↓

Commit

↓

Worker

↓

External Action
```

This provides reliable handoff without requiring a message broker.

---

# 18. Job Dispatcher

The Job Dispatcher finds eligible queued jobs.

Conceptually:

```text
Find Queued Job

↓

Lock / Claim

↓

Run Handler

↓

Record Result
```

---

# 19. Job Claiming

A worker must claim a job safely before execution.

The implementation should prevent two workers from executing the same job simultaneously.

For a single-user or low-concurrency desktop deployment, a simple database claim mechanism is normally sufficient.

---

# 20. Job Locking

A job may use:

```text
status

locked_at

locked_by
```

or an equivalent mechanism.

---

# 21. Stale Job Recovery

If a worker crashes while processing:

```text
Running

↓

No Worker

↓

Stale Timeout

↓

Eligible for Recovery
```

The recovery threshold should be configured according to job type.

---

# 22. Retry Principle

Retries are appropriate only for failures that may reasonably succeed later.

Examples:

```text
Temporary Network Failure

Temporary Email Provider Failure

Database Busy Condition
```

Do not retry permanent business validation failures indefinitely.

---

# 23. Retry Count

Every retryable job should have a bounded attempt count.

Example:

```text
Attempt 1

Attempt 2

Attempt 3

↓

Final Failure
```

The exact maximum may be configurable.

---

# 24. Exponential Backoff

Retry delays may increase between attempts.

Conceptually:

```text
Attempt 1 → Short Delay

Attempt 2 → Longer Delay

Attempt 3 → Longer Delay
```

The implementation should cap the maximum delay.

---

# 25. Retry Jitter

If multiple jobs are retried, a small randomized delay may reduce synchronized retries.

For the small MFM environment this is optional.

---

# 26. Permanent Failure

A job should become terminally failed when:

- Maximum Attempts Reached
- Invalid Configuration
- Invalid Reference
- Permanent Provider Rejection
- Business Rule Prevents Execution

---

# 27. Failed Job Information

A failed job should preserve:

```text
Failure Time

Attempt Count

Failure Category

Safe Error Message

Correlation ID
```

Technical diagnostics remain in logs.

---

# 28. Job Error Categories

Possible categories:

```text
Validation

Authorization

Configuration

Network

Provider

Database

Timeout

Storage

Unknown
```

---

# 29. Idempotency Principle

A retried job must not accidentally create duplicate business effects.

Examples:

```text
Send Email

Create External Record

Generate Report

Create Notification
```

---

# 30. Idempotency Key

Where required, use a stable key.

Example:

```text
notification_id

+

delivery_channel
```

or:

```text
business_event_id
```

---

# 31. Email Idempotency

Before sending a retryable email, the system should determine whether that delivery has already succeeded.

This prevents duplicate messages where provider behavior is ambiguous.

---

# 32. Notification Model

A notification may contain:

```text
Notification ID

Recipient

Type

Subject

Message

Priority

Created At

Scheduled At

Status

Related Entity

Correlation ID
```

---

# 33. Notification States

Possible states:

```text
Created

Queued

Sending

Sent

Failed

Cancelled
```

---

# 34. Internal Notification

Internal notifications may appear in the MFM application.

Example:

```text
Grant deadline in 7 days.
```

---

# 35. Email Notification

Email notifications are optional and depend on configuration.

Example:

```text
Grant deadline approaching

↓

Notification Service

↓

Email Adapter

↓

Provider
```

---

# 36. Notification Preferences

Users may have preferences for:

- Email
- In-App
- Disabled Categories

Preferences must not suppress legally or operationally required notifications where such requirements exist.

---

# 37. Notification Templates

Templates should be centralized.

Example:

```text
grant_deadline_warning
backup_failed
report_ready
```

This avoids duplicated message text in service code.

---

# 38. Template Variables

Templates may use controlled variables:

```text
{{grant_name}}

{{deadline}}

{{project_name}}
```

Variables must be safely substituted.

---

# 39. Template Security

Do not allow arbitrary executable content in templates.

User-provided text should be escaped or safely handled according to the output channel.

---

# 40. Notification Priority

Possible priorities:

```text
Low

Normal

High

Critical
```

The exact priority model follows MFM requirements.

---

# 41. Critical Notification

Critical notifications may require:

- Immediate Delivery
- Persistent In-App Display
- Administrative Attention

The exact policy must be defined by the relevant domain.

---

# 42. Notification Expiration

Temporary notifications may have an expiration time.

Example:

```text
Deadline reminder

Valid until deadline
```

---

# 43. Notification Read State

Internal notifications may track:

```text
Unread

Read

Dismissed
```

---

# 44. Notification Security

A notification must only be delivered to an authorized recipient.

Do not rely solely on a client-side recipient selection.

---

# 45. Notification Privacy

Messages should contain only necessary personal or confidential information.

---

# 46. Background Report Job

Large reports may be generated asynchronously.

Flow:

```text
User Requests Report

↓

Create Report Job

↓

Return Job ID

↓

Worker Generates Report

↓

Store Result

↓

Notify User
```

---

# 47. Report Job Result

A completed report job may produce:

```text
File Reference

Report Metadata

Generation Time

Source Period
```

---

# 48. Report Job Failure

The user should receive:

```text
The report could not be generated.
```

The job record should contain diagnostic status.

---

# 49. Backup Job

Backups may be scheduled or manually triggered.

Flow:

```text
Backup Request

↓

Create Job

↓

Prepare Database

↓

Create Backup

↓

Verify

↓

Record Result
```

---

# 50. Backup Failure

A failed backup should generate an administrative notification where configured.

---

# 51. Backup Verification

A successful backup job should not be considered complete merely because a file was created.

Verification should confirm:

```text
File Exists

File Readable

Expected Structure / Integrity

Optional Restore Test
```

---

# 52. Restore Job

Restore is a privileged maintenance operation.

It should normally not be executed concurrently with ordinary business activity.

---

# 53. Restore Lock

During restore:

```text
Application Operational Mode

→ Maintenance / Locked
```

where required by the implementation.

---

# 54. Document Background Jobs

Background document jobs may include:

- Checksum Calculation
- File Integrity Check
- Metadata Processing
- Archive Processing

---

# 55. Document Job Principle

Document jobs must not bypass document authorization or retention rules.

---

# 56. Maintenance Jobs

Maintenance jobs may include:

```text
Database Integrity Check

Cleanup Temporary Files

Verify Backups

Process Failed Notifications

Refresh Read Models
```

---

# 57. Scheduled Jobs

Scheduled jobs may run:

```text
Daily

Weekly

Monthly

On Startup

At Specific Time
```

The scheduling mechanism should remain simple.

---

# 58. Scheduler

The Scheduler determines when jobs become eligible.

It should not contain the business logic of the job itself.

---

# 59. Scheduler Flow

```text
Schedule

↓

Job Eligible

↓

Create / Release Job

↓

Worker

↓

Handler
```

---

# 60. Scheduler Reliability

The scheduler should tolerate application restarts.

Scheduled work must not depend solely on in-memory timers.

---

# 61. Missed Schedule

If the application was closed when a scheduled job should have run, the system should have an explicit policy:

```text
Run Immediately

Skip

Run Once on Next Startup
```

The policy should be job-specific.

---

# 62. Duplicate Schedule Prevention

A scheduler must avoid creating duplicate jobs for the same scheduled occurrence.

Use a deterministic schedule key where appropriate.

---

# 63. Job Handler

Each job type should have a controlled handler.

Example:

```text
ReportJobHandler

BackupJobHandler

NotificationJobHandler

MaintenanceJobHandler
```

---

# 64. Handler Responsibilities

A handler should:

- Validate Payload
- Execute Service
- Record Result
- Handle Retryable Failure
- Handle Permanent Failure

---

# 65. Handler Business Logic

Business rules should remain in application/domain services.

The handler coordinates execution.

Avoid putting domain rules directly in job handlers.

---

# 66. Job Dependency

Jobs may depend on other jobs.

Example:

```text
Generate Report

↓

Send Report Notification
```

Dependencies should be explicit.

---

# 67. Job Dependency Failure

If a prerequisite fails:

```text
Dependent Job

→ Waiting / Cancelled / Failed
```

according to the workflow definition.

---

# 68. Job Cancellation

Where practical, queued jobs may be cancelled.

A running job may only be cancellable if the operation safely supports cancellation.

---

# 69. Cancellation State

Possible:

```text
Queued

↓

Cancelled
```

or:

```text
Running

↓

Cancellation Requested

↓

Cancelled
```

---

# 70. Job Progress

Long-running jobs may expose progress:

```text
0–100%
```

If progress cannot be measured, show status instead.

---

# 71. Job Status UI

Administration may display:

```text
Queued

Running

Succeeded

Retrying

Failed

Cancelled
```

---

# 72. User Job UI

Normal users should generally see only jobs relevant to their own actions.

Example:

```text
Report generation

Status:
Running
```

---

# 73. Administrative Job UI

Authorized administrators may see:

```text
Job ID

Type

Status

Created

Attempts

Error

Duration
```

---

# 74. Job Logging

Every job should have a correlation context.

Technical logs should record:

```text
Job ID

Handler

Start

End

Result

Error
```

Do not log secrets.

---

# 75. Job Audit

Business-significant actions initiated through jobs may require audit.

Example:

```text
Scheduled Backup

Manual Restore

Report Export
```

---

# 76. Audit vs Job Log

Job log:

```text
Technical Execution
```

Audit:

```text
Business / Administrative Accountability
```

They are complementary.

---

# 77. Background Authorization

A background job should carry an appropriate execution identity.

Possible identities:

```text
System

Scheduled Service

Requesting User
```

The identity model must be explicit.

---

# 78. User-Requested Jobs

If a user requests a report:

```text
Requested By = User X
```

The job must preserve the user's authorization scope.

---

# 79. Scheduled Jobs

Scheduled jobs should use a controlled system or service identity with explicitly defined permissions.

---

# 80. Privileged Jobs

Backup and restore jobs require privileged execution.

Their handlers must not inherit unrestricted permissions unnecessarily.

---

# 81. Job Payload Authorization

Do not assume that because a job was created by an authorized user it can later access everything.

The execution scope must be checked or securely captured.

---

# 82. Job Retention

Completed jobs should be retained according to operational requirements.

Do not keep unlimited historical job data without reason.

---

# 83. Job Cleanup

Cleanup should:

```text
Identify Old Completed Jobs

↓

Apply Retention Policy

↓

Archive / Delete Safely
```

Failed jobs may require longer retention for diagnostics.

---

# 84. Notification Retention

Notifications may have a separate retention policy.

---

# 85. Job Queue Maintenance

Maintenance should detect:

```text
Stale Jobs

Repeated Failures

Queue Growth

Old Jobs

Unknown Job Types
```

---

# 86. Queue Health

A queue is unhealthy if:

- Jobs remain queued too long
- Failure rate increases
- Worker is not running
- Jobs remain locked indefinitely

---

# 87. Queue Monitoring

Administrative dashboards may show:

```text
Queued

Running

Failed

Retrying

Oldest Queued Job
```

---

# 88. Worker Health

A worker may publish or record:

```text
Last Heartbeat

Current Job

Last Successful Job
```

This is optional for a simple deployment but useful for diagnostics.

---

# 89. Single Worker Principle

For the current MFM scale, one background worker is generally sufficient.

Multiple workers may be introduced only if actual workload requires them.

---

# 90. Worker Concurrency

If concurrency is enabled, job handlers must be designed for safe parallel execution.

Do not assume database or file operations are automatically safe.

---

# 91. Accounting Job Rule

Background jobs must not bypass Accounting Core.

If a job creates financial transactions:

```text
Job Handler

↓

AccountingService

↓

Accounting Core

```

not:

```text
Job Handler

↓

Direct Ledger SQL
```

---

# 92. Reporting Job Rule

Report jobs query authoritative sources.

They do not modify source financial data.

---

# 93. Notification Job Rule

Notification jobs may report delivery results but do not modify the business event that caused the notification.

---

# 94. Backup Job Rule

Backup jobs create recovery artifacts.

They do not alter accounting truth.

---

# 95. Maintenance Job Rule

Maintenance jobs must be designed to avoid destructive operations unless explicitly authorized and controlled.

---

# 96. Database Job Transaction

A job that performs multiple database writes should use appropriate transaction boundaries.

---

# 97. External Call Job

For external calls:

```text
Validate

↓

Call Provider

↓

Interpret Response

↓

Record Result
```

Timeouts must be bounded.

---

# 98. External Call Retry

Retry only when:

- Provider Failure Is Transient
- Operation Is Safe to Retry
- Idempotency Is Controlled

---

# 99. External Provider Ambiguity

If the provider result is unknown:

```text
Do Not Blindly Retry

↓

Check Delivery / Provider Status

↓

Determine Outcome
```

where possible.

---

# 100. Notification Delivery Example

```text
Grant Deadline Event

↓

NotificationService

↓

Create Notification

↓

Queue Delivery Job

↓

EmailNotificationHandler

↓

Email Provider

↓

Record Sent

```

---

# 101. Report Generation Example

```text
User

↓

ReportingService

↓

Create Report Job

↓

Worker

↓

ReportingService.Generate

↓

Store Export

↓

Notification

↓

User Opens Report
```

---

# 102. Backup Example

```text
Scheduler

↓

Backup Job

↓

Backup Handler

↓

Create Backup

↓

Verify

↓

Record Result

↓

Notify Administrator
```

---

# 103. Maintenance Example

```text
Scheduler

↓

Integrity Check Job

↓

Maintenance Handler

↓

Database Integrity Check

↓

Record Result

↓

Administrative Notification if Failed
```

---

# 104. Read Model Refresh Example

```text
Voucher Posted

↓

Refresh Request

↓

Read Model Builder

↓

Update Derived View

```

If the refresh fails, authoritative accounting data remains unaffected.

---

# 105. Failure Isolation

A failure in one background operation should not unnecessarily stop unrelated work.

Example:

```text
Email Provider Down

↓

Email Jobs Fail / Retry

↓

Backup Jobs Continue
```

---

# 106. Dead-Letter Concept

For repeatedly failing jobs, MFM may use a terminal failure state equivalent to a dead-letter queue.

Example:

```text
Failed Permanently
```

The job remains available for diagnosis and controlled retry.

---

# 107. Manual Retry

Authorized administrators may retry a failed job where safe.

Before retry:

```text
Review Failure

↓

Confirm Safe

↓

Retry
```

---

# 108. Force Retry

A force retry must not bypass:

- Authorization
- Idempotency
- Business Rules
- Security

---

# 109. Job Reprocessing

A completed job should not normally be reprocessed unless the operation is explicitly designed to be repeatable.

---

# 110. Duplicate Prevention

Use unique business references or idempotency keys where duplicate effects would be harmful.

---

# 111. Background Data Validation

Jobs should validate that referenced entities still exist.

Example:

```text
Report Job references Project 123

↓

Project deleted / archived

↓

Handle according to policy
```

---

# 112. Job Payload Versioning

If job payload structures evolve, the job type or payload version should be identifiable.

Example:

```text
report_generation
payload_version = 2
```

---

# 113. Compatibility

Application updates should consider queued jobs from an earlier version.

Options:

```text
Process

Migrate

Cancel Safely
```

The system must not blindly interpret incompatible payloads.

---

# 114. Deployment Principle

Before application upgrade:

```text
Review Queued Jobs

↓

Apply Compatibility Strategy

↓

Upgrade

↓

Resume Processing
```

---

# 115. Job Schema Migration

Changes to job persistence must follow the MFM migration process.

---

# 116. Background Job Testing

Every job type should have tests for:

- Valid Execution
- Invalid Payload
- Success
- Retry
- Permanent Failure
- Idempotency
- Authorization
- Logging
- Audit where required

---

# 117. Notification Tests

Minimum:

```text
Create

Queue

Send

Failure

Retry

Duplicate Prevention

Read State
```

---

# 118. Report Job Tests

Minimum:

```text
Queue

Generate

Store

Notify

Failure

Retry

Authorization
```

---

# 119. Backup Job Tests

Minimum:

```text
Create

Verify

Failure

Authorization

Recovery
```

---

# 120. Maintenance Job Tests

Minimum:

```text
Run

Failure

Result Recording

Notification
```

---

# 121. Scheduler Tests

Minimum:

```text
Due Job

Not Due

Missed Schedule

Duplicate Prevention

Restart Recovery
```

---

# 122. Worker Tests

Minimum:

```text
Claim

Execute

Success

Failure

Retry

Crash Recovery
```

---

# 123. Concurrency Tests

If multiple workers are supported, test:

```text
Same Job

↓

Worker A Claims

Worker B Attempts

↓

Only A Executes
```

---

# 124. Performance

Background processing exists partly to keep the GUI responsive.

Long operations should not block normal user interaction unnecessarily.

---

# 125. Queue Backpressure

If jobs accumulate faster than they are processed:

```text
Detect Growth

↓

Monitor

↓

Limit / Defer New Work if Necessary

↓

Administrative Attention
```

The implementation should remain simple for the current scale.

---

# 126. Notification Rate

Where providers impose limits, delivery should respect those limits.

---

# 127. Email Batch Processing

Large batches may be processed incrementally.

Example:

```text
10–50 messages

↓

Pause / Continue
```

The exact batch size should be configurable if required.

---

# 128. Background File Processing

Large document processing should avoid blocking the GUI.

---

# 129. Temporary Files

Background jobs creating temporary files must:

- Use Controlled Locations
- Use Safe Names
- Clean Up
- Avoid Sensitive Data Leakage

---

# 130. Temporary File Failure

If cleanup fails, the maintenance system should detect stale temporary files.

---

# 131. Job Result Storage

A job may reference a result artifact.

Example:

```text
Job

↓

Result File Reference
```

The job record should not necessarily contain the entire output file.

---

# 132. Result Security

Result files must inherit appropriate access control.

A report generated for one user must not automatically become visible to all users.

---

# 133. Notification and Report Security

If a notification says:

```text
Your report is ready.
```

the linked report must independently enforce authorization.

---

# 134. Background Job Administration

Administration may provide:

```text
Job List

Filter

Details

Retry

Cancel

Cleanup
```

---

# 135. Job Details

Details may show:

```text
Job ID

Type

Status

Created

Started

Completed

Attempts

Requested By

Error

Correlation ID
```

---

# 136. Job Error Detail

Technical error detail should be visible only to authorized administrators.

---

# 137. Job History

Historical job information should support diagnosis without becoming an unlimited data store.

---

# 138. Scheduler Configuration

Administration may configure:

```text
Enabled / Disabled

Schedule

Retry Policy

Retention
```

Only authorized users may change scheduler configuration.

---

# 139. Emergency Disable

Administrators may need to disable a problematic job type.

Example:

```text
Email Delivery

→ Disabled
```

Existing queued jobs should follow an explicit policy.

---

# 140. Maintenance Mode

For critical maintenance operations:

```text
Maintenance Mode

↓

Block Business Operations

↓

Execute Maintenance

↓

Validate

↓

Resume
```

---

# 141. Backup Before Maintenance

High-risk maintenance should consider:

```text
Verified Backup

↓

Maintenance
```

---

# 142. Restore Before Background Processing

After a database restore:

```text
Validate Database

↓

Validate Schema

↓

Validate Jobs

↓

Resume Worker
```

Queued jobs that reference invalid data must be handled safely.

---

# 143. Job Security Gate

Before execution verify:

```text
Job Type Allowed

Payload Valid

Execution Identity Valid

Referenced Data Accessible

Required Configuration Present
```

---

# 144. Secret Handling

Background jobs must retrieve credentials through the established secrets mechanism.

They must not:

- Store plaintext secrets
- Log credentials
- Place secrets in job payloads
- Include secrets in report files

---

# 145. Audit Principle

Background execution must remain traceable.

For important jobs:

```text
Who Requested

What Happened

When

Result
```

should be recoverable.

---

# 146. Traceability

Background processing should trace:

```text
Business Event

↓

Service Operation

↓

Job

↓

Handler

↓

External Action / Result

↓

Audit
```

---

# 147. Operational Metrics

Useful metrics include:

```text
Jobs Created

Jobs Completed

Jobs Failed

Retry Count

Average Duration

Oldest Queued Job

Notification Success Rate
```

These are operational metrics, not authoritative business records.

---

# 148. Dashboard Integration

Administration dashboards may display job metrics.

The dashboard remains read-only.

---

# 149. Alerting

Critical failures may trigger:

```text
In-App Notification

Email

Administrative Alert
```

according to configuration.

---

# 150. Alert Suppression

Repeated identical failures should not generate an unlimited number of alerts.

Controlled aggregation may be used.

---

# 151. Recovery Runbook

For a failed job:

```text
Identify

↓

Inspect

↓

Classify

↓

Correct Cause

↓

Retry if Safe

↓

Verify

↓

Close
```

---

# 152. Notification Failure Runbook

```text
Check Provider

↓

Check Credentials

↓

Check Job

↓

Retry

↓

Verify Delivery
```

---

# 153. Backup Failure Runbook

```text
Check Storage

↓

Check Database Access

↓

Check Disk Space

↓

Check Backup Job

↓

Retry

↓

Verify
```

---

# 154. Report Failure Runbook

```text
Check Filters

↓

Check Source Data

↓

Check Query

↓

Retry

↓

Verify Output
```

---

# 155. Worker Failure Runbook

```text
Check Worker

↓

Check Database

↓

Check Stale Locks

↓

Recover Jobs

↓

Restart Worker

↓

Verify Queue
```

---

# 156. Scheduler Failure Runbook

```text
Check Scheduler

↓

Check Schedule

↓

Check Job Creation

↓

Check Duplicate Prevention

↓

Run Missed Jobs According to Policy
```

---

# 157. Background Job Definition of Ready

A job is Ready when:

- Purpose Is Defined
- Trigger Is Defined
- Payload Is Defined
- Handler Is Defined
- Authorization Is Defined
- Retry Policy Is Defined
- Idempotency Is Defined
- Failure Handling Is Defined

---

# 158. Background Job Definition of Done

A job is Done when:

- Queueing Works
- Handler Works
- Success Is Recorded
- Failure Is Recorded
- Retry Works
- Idempotency Is Tested
- Authorization Is Tested
- Monitoring Exists
- Recovery Is Documented

---

# 159. Notification Definition of Ready

A notification is Ready when:

- Event Is Defined
- Recipient Is Defined
- Channel Is Defined
- Template Is Defined
- Permission Is Defined
- Retention Is Defined

---

# 160. Notification Definition of Done

A notification is Done when:

- Created
- Queued
- Delivered
- Failed Safely
- Retried Safely
- Audited where required
- Tested

---

# 161. Asynchronous Release Gate

Before release:

```text
Queue

Worker

Scheduler

Retry

Idempotency

Failure Handling

Security

Monitoring

Recovery

Testing
```

must be reviewed.

---

# 162. Financial Release Gate

Background processing must verify:

```text
No Direct Ledger Bypass

AccountingService Used

Accounting Transactions Remain Atomic

Reports Remain Read-Only

Notifications Do Not Alter Financial Truth
```

---

# 163. Small-Association Principle

The MFM asynchronous architecture should remain proportionate.

The preferred implementation is:

```text
Database-Backed Jobs

+

Simple Worker

+

Simple Scheduler

+

Controlled Handlers
```

rather than a distributed messaging platform.

---

# 164. Future Scalability

If workload grows substantially, the architecture may evolve toward:

```text
Job Store

↓

Multiple Workers

↓

External Queue
```

without changing domain ownership.

Such a change requires a new architecture decision and implementation document.

---

# 165. Final Notification Principle

Notifications communicate business events.

They do not own those events.

---

# 166. Final Background Processing Principle

Background jobs execute deferred work.

They must remain:

```text
Controlled

Idempotent

Traceable

Recoverable
```

---

# 167. Final Financial Principle

> **Background processing must never create a parallel financial truth.**

Any financial operation must use the established Accounting Core services and persistence boundaries.

---

# 168. Summary

MFM v1.2-590 establishes the Notifications, Background Jobs and Asynchronous Processing implementation baseline.

It defines:

- Notification Model
- Job Model
- Queue
- Worker
- Scheduler
- Handlers
- Retry
- Idempotency
- Failure Handling
- Internal Notifications
- Email
- Report Jobs
- Backup Jobs
- Maintenance Jobs
- Document Jobs
- Security
- Audit
- Monitoring
- Recovery
- Testing
- Performance

The central principle remains:

> **Asynchronous processing is an execution mechanism, not a new source of business truth.**

And:

> **Accounting Core remains the sole authoritative financial ledger.**

---

# 169. Next Document

**MFM v1.2-600 – Integration, External Services & Adapter Implementation**

---

# END OF DOCUMENT
