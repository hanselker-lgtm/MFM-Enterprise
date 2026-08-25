# PROJ-001 — Domain Model

Status: Draft

---

# Aggregate Root

Project

The Project aggregate is the only aggregate root in version 1.

Everything else belongs to Project.

---

# Entity

## Project

Identity

ProjectId

Properties

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

Collections

Milestones

Activities

Assignments

References

---

## Milestone

Identity

MilestoneId

Properties

Name

Description

DueDate

CompletedDate

Status

Sequence

---

## Activity

Identity

ActivityId

Properties

Title

Description

Status

PlannedStart

PlannedFinish

ActualStart

ActualFinish

Priority

EstimatedHours

ActualHours

---

## Assignment

Identity

AssignmentId

Properties

OrganisationId

ContactId

Role

AssignedFrom

AssignedUntil

---

## ExternalReference

Identity

ReferenceId

Properties

ReferenceType

ExternalId

Description
