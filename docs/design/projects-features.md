# PROJ-005 — Feature Layer

Status: Draft

---

# Purpose

The Feature Layer exposes stable use cases to the presentation layer.

It delegates all business operations to Application Services.

The Feature Layer contains no domain logic.

---

# Package Structure

application/
    features/
        projects/

            create_project.py
            update_project.py
            activate_project.py
            complete_project.py
            archive_project.py

            create_milestone.py
            complete_milestone.py

            create_activity.py
            update_activity.py
            complete_activity.py

            assign_member.py
            remove_assignment.py

            add_reference.py
            remove_reference.py

            get_project.py
            list_projects.py
            search_projects.py

            dashboard.py

---

# Feature Contract

Each feature exposes

execute()

Example

CreateProjectFeature.execute(command)

GetProjectFeature.execute(query)

SearchProjectsFeature.execute(query)

---

# Dependencies

GUI

↓

Feature

↓

Application

↓

Domain

↓

Repository

No reverse dependencies.

---

# Returned Objects

Commands

↓

ProjectDto

Queries

↓

Projection DTOs

The Feature Layer never exposes Domain entities.

---

# Error Mapping

Domain Exception

↓

Feature Exception

↓

Presentation

Examples

DuplicateProjectNumber

↓

DuplicateProjectNumberError

ProjectNotFound

↓

ProjectNotFoundError

ConcurrencyConflict

↓

ConcurrencyConflictError

---

# Validation

Presentation validates UI.

Feature validates request completeness.

Application validates orchestration.

Domain validates business rules.

---

# Logging

Feature layer logs

Entry

Exit

Duration

CorrelationId

Exceptions

No business data logged.

---

# Security Hook

Authorization occurs before Application Service execution.

Future authentication providers integrate here.

---

# Acceptance Criteria

One feature per use case.

No SQL.

No ORM.

No Domain mutations.

Application Services only.

Stable public interface.