# PROJ-002 — Persistence Model

Status: Draft

---

# Objective

Persist the Project aggregate without violating aggregate boundaries.

Persistence is an implementation detail.

The domain remains persistence ignorant.

---

# Tables

## project

Primary Key

ProjectId

Columns

ProjectNumber

ProjectName

Description

Status

Priority

StartDate

EndDate

CreatedAt

UpdatedAt

ArchivedAt

Version

---

## project_milestone

Primary Key

ProjectMilestoneId

Foreign Key

ProjectId

Columns

Name

Description

Sequence

Status

DueDate

CompletedDate

---

## project_activity

Primary Key

ProjectActivityId

Foreign Key

ProjectId

Columns

Title

Description

Status

Priority

EstimatedHours

ActualHours

PlannedStart

PlannedFinish

ActualStart

ActualFinish

Sequence

---

## project_assignment

Primary Key

ProjectAssignmentId

Foreign Key

ProjectId

Columns

OrganisationId

ContactId

Role

AssignedFrom

AssignedUntil

---

## project_reference

Primary Key

ProjectReferenceId

Foreign Key

ProjectId

Columns

ReferenceType

ExternalId

Description

CreatedAt

---

# ORM Model

One SQLAlchemy model per table.

No ORM model outside this capability may reference these models.

No relationship() crosses capability boundaries.

Allowed relationships

ProjectModel

↓

ProjectMilestoneModel

ProjectActivityModel

ProjectAssignmentModel

ProjectReferenceModel

Only within this aggregate.

---

# Mapper

Single mapper

ProjectMapper

Responsibilities

Domain

↓

Persistence

Persistence

↓

Domain

No business rules.

No validation.

No database access.

Pure mapping.

---

# Repository

Repository owns

Loading aggregate

Saving aggregate

Deleting aggregate

Optimistic concurrency

Nothing else.

---

# Versioning

Project table contains

Version

Used for optimistic locking.

Increment on every aggregate modification.

---

# Cascade Rules

Delete Project

↓

Delete Milestones

↓

Delete Activities

↓

Delete Assignments

↓

Delete References

Aggregate consistency only.

---

# Foreign Keys

Allowed

ProjectId

Only internal foreign keys.

External capabilities

Never foreign keys.

Only identifiers stored as scalar values.

Example

PurchaseOrderId

stored as UUID

NOT foreign key.

---

# Indexes

ProjectNumber

Status

Priority

StartDate

EndDate

OrganisationId

ExternalId

Composite

(Status, Priority)

(ProjectId, Sequence)

(ProjectId, Status)

---

# Constraints

Unique

ProjectNumber

Check

EndDate >= StartDate

EstimatedHours >= 0

ActualHours >= 0

Version >= 1

---

# Persistence Rules

Persistence never creates domain logic.

Mapper never validates.

Repository never changes business state.

Domain remains authoritative.

---

# Acceptance Criteria

Five ORM models

One mapper

One repository contract

No cross-capability ORM

No infrastructure leakage

Aggregate persisted atomically

Optimistic locking implemented