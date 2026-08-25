# PROJ-004 — Application Services

Status: Draft

---

# Purpose

Application Services coordinate use cases.

They do not contain business rules.

Business rules belong exclusively to the Domain.

Repositories perform persistence only.

---

# Commands

## CreateProject

Input

ProjectNumber

ProjectName

Description

StartDate

EndDate

Priority

Output

ProjectId

---

## UpdateProject

Input

ProjectId

Updated fields

Output

None

---

## ActivateProject

Input

ProjectId

---

## CompleteProject

Input

ProjectId

---

## ArchiveProject

Input

ProjectId

---

## CreateMilestone

Input

ProjectId

Milestone data

---

## CompleteMilestone

Input

ProjectId

MilestoneId

---

## CreateActivity

Input

ProjectId

Activity data

---

## CompleteActivity

Input

ProjectId

ActivityId

---

## AssignMember

Input

ProjectId

OrganisationId

ContactId

Role

---

## RemoveAssignment

Input

ProjectId

AssignmentId

---

## AddReference

Input

ProjectId

ReferenceType

ExternalId

---

# Queries

GetProject

ListProjects

SearchProjects

ListActiveProjects

ListCompletedProjects

ListArchivedProjects

ProjectDashboard

ProjectSummary

---

# Transaction Boundary

Exactly one aggregate per transaction.

No distributed transactions.

---

# Validation

Application validates

Required fields

DTO consistency

Authorization

Domain validates

Business rules

State transitions

Invariants

---

# Dependencies

Application

↓

Domain

↓

Repository

Never reverse.

---

# Exceptions

ProjectNotFound

DuplicateProjectNumber

ConcurrencyConflict

ValidationError

PermissionDenied

PersistenceFailure

---

# DTOs

Commands

CreateProjectCommand

UpdateProjectCommand

AssignMemberCommand

CreateActivityCommand

CreateMilestoneCommand

Queries

ProjectDto

ProjectSummaryDto

ProjectDashboardDto

ProjectSearchResultDto

---

# Acceptance Criteria

Application contains no SQL.

Application contains no ORM.

Application contains no business rules.

Every use case represented by one command or one query.

Repositories injected through interfaces only.