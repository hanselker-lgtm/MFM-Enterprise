# PROJ-003 — Repository Specification

Status: Draft

---

# Repository Contract

Aggregate

Project

Repository

ProjectRepository

Purpose

Persist and retrieve Project aggregates.

Repository never contains business rules.

---

# Operations

add(project)

update(project)

remove(project_id)

get(project_id)

exists(project_id)

list(filters)

search(criteria)

next_identity()

---

# Transaction Rules

One aggregate per transaction.

Commit occurs only after aggregate validation.

Rollback restores aggregate consistency.

---

# Loading Strategy

Repository always returns

Complete Aggregate.

Never partially loaded aggregates.

No lazy loading inside Domain.

---

# Save Strategy

Repository persists

Project

ProjectMilestones

ProjectActivities

ProjectAssignments

ProjectReferences

atomically.

---

# Search

Search never returns aggregates by default.

Search returns lightweight projections.

Examples

ProjectSummary

ProjectSearchResult

ProjectDashboard

Aggregate loaded only through get().

---

# Specification Objects

Allowed

ProjectSearchCriteria

ProjectFilter

ProjectSortOrder

ProjectPage

Repository never receives SQL fragments.

---

# Exceptions

ProjectNotFound

DuplicateProjectNumber

ConcurrencyConflict

PersistenceFailure

---

# Optimistic Locking

Repository validates Version.

Conflict

↓

ConcurrencyConflict

---

# Infrastructure Boundary

Domain depends on

ProjectRepository

Infrastructure depends on

Domain

Never opposite.

---

# Acceptance Criteria

Single repository

Single aggregate

Atomic persistence

Optimistic locking

Projection-based searching

No SQL exposure

No ORM exposure

No framework dependency