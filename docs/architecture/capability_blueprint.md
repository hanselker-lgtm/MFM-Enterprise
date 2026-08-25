# MFM Enterprise Capability Blueprint

Version: 1.0

Purpose

This document defines the mandatory structure for every capability
implemented in MFM Enterprise.

---

# Directory Structure

src/mfm/

    domain/

    application/

    infrastructure/

    presentation/

Every capability follows exactly the same structure.

---

# Domain

Contains

Aggregate Roots

Entities

Value Objects

Domain Events

Repository Interfaces

No framework dependencies.

---

# Application

Contains

Commands

Queries

DTOs

Application Services

Transaction orchestration

No SQL.

No ORM.

No GUI.

---

# Infrastructure

Contains

ORM Models

Repositories

Mappers

SQLite implementation

Future PostgreSQL implementation

Future API implementation

Infrastructure depends on Domain.

Never opposite.

---

# Presentation

Contains

GUI

CLI

REST API

Future integrations

Presentation depends only on Feature Layer.

---

# Dependency Rule

Presentation

↓

Feature

↓

Application

↓

Domain

↓

Repository Contract

↓

Infrastructure

Reverse dependencies prohibited.

---

# Aggregate Rule

One repository

↓

One aggregate

One transaction

---

# Repository Rule

Repositories return

Complete Aggregate

or

Projection

Never partial aggregates.

---

# DTO Rule

DTOs cross layer boundaries.

Domain objects never cross layer boundaries.

---

# Persistence Rule

Persistence is replaceable.

Changing SQLite shall never change Domain.

---

# Test Structure

tests/

    domain/

    application/

    infrastructure/

    integration/

    end_to_end/

Capability tests follow identical layout.

---

# Review Checklist

Architecture

Domain

Persistence

Repository

Application

Feature

Integration

Documentation

Quality Gates

All green before capability lock.