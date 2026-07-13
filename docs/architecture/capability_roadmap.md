# Capability Roadmap

## Purpose
Define one authoritative capability sequence for MFM Enterprise after CAP-10 lock,
based on committed repository evidence and dependency readiness.

This document closes the prior gap where the next capability was not
authoritatively defined.

## Authority
This file is the authoritative source for capability sequencing and CAP assignment.

Supporting material:
- `CHANGELOG.md`
- `docs/design/*.md`
- `*_capability_review.md`

Supporting material may describe boundaries, non-goals, and candidate mentions,
but it does not override sequence decisions recorded here.

## Current Capability Status

### Implemented baseline (from design status + git history)

| Sequence | Identifier | Capability | Status | Evidence |
|---|---|---|---|---|
| 1 | ORG-000..ORG-011 | Organization | REVIEW | `organization_capability_review.md` (conclusion READY FOR LOCK), `docs/design/organization.md` |
| 2 | ASSET-000..ASSET-007 | Asset Core | REVIEW | `asset_capability_review.md` (conclusion READY FOR LOCK), `docs/design/asset_core.md` |
| 3 | CAP-07 / FLEET-000..FLEET-008 | Fleet | LOCKED | `docs/design/fleet.md`, `CHANGELOG.md` |
| 4 | CAP-08 / TECH-000..TECH-008 | Technical Configuration | LOCKED | `docs/design/technical_configuration.md`, `CHANGELOG.md` |
| 5 | CAP-09 / MAINT-000..MAINT-008 | Maintenance | LOCKED | `docs/design/maintenance.md`, `CHANGELOG.md` |
| 6 | CAP-10 / CERT-000..CERT-008 | Certificates and Compliance | LOCKED | `docs/design/certificates_compliance.md`, `CHANGELOG.md` |
| 7 | CAP-11 / VOY-000..VOY-008 | Voyages | LOCKED | `docs/design/voyages.md`, `CHANGELOG.md` |

Status interpretation rules in this roadmap:
- LOCKED: explicitly marked LOCKED in design capability status and lock release notes.
- REVIEW: capability review completed with READY FOR LOCK evidence, but no explicit
	lock status recorded in the capability status section.
- IN DEVELOPMENT: implementation started without review completion.
- PLANNED: roadmap-planned but not started.

## Locked Foundation
Current locked foundation that must be preserved:
- CAP-07 Fleet (LOCKED)
- CAP-08 Technical Configuration (LOCKED)
- CAP-09 Maintenance (LOCKED)
- CAP-10 Certificates and Compliance (LOCKED)
- CAP-11 Voyages (LOCKED)

Completed but not lock-marked in design status:
- Asset Core (ASSET-007 READY FOR LOCK)
- Organization (ORG-011 READY FOR LOCK)

All future capabilities must consume these capabilities through identity/reference
boundaries and stable public API contracts.

## Sequencing Principles
1. Minimize modifications to locked capabilities.
2. Prefer capabilities with clear bounded-context ownership already documented.
3. Prefer identity/reference consumption over cross-context state ownership.
4. Avoid reverse dependencies into locked capabilities.
5. Avoid speculative shared frameworks and premature cross-capability abstractions.
6. Sequence by dependency readiness, not by mention frequency or conversational intent.

## Candidate Capabilities

### Candidate: Voyages
- Repository evidence:
	- `docs/design/fleet.md` (Voyages explicitly excluded from Fleet)
	- `docs/design/technical_configuration.md` (Voyages excluded from CAP-08)
	- `docs/design/maintenance.md` (Voyages excluded from CAP-09; separate capability)
	- `docs/design/certificates_compliance.md` (Voyages excluded from CAP-10)
- Documented purpose: operational planning/execution area outside Fleet,
	Maintenance, Technical Configuration, and Certificates scopes.
- Known dependencies: Fleet vessel identity/reference foundation.
- Likely boundary: voyage lifecycle, route/schedule/log context, separate from
	maintenance/certificate lifecycle ownership.
- Existing design document: no dedicated Voyages design document found.

### Candidate: Inventory (including spare parts)
- Repository evidence:
	- `docs/design/maintenance.md` (inventory/spare parts explicitly out of scope)
- Documented purpose: inventory/spare parts management not owned by Maintenance.
- Known dependencies: likely linkage to maintenance execution outcomes and
	technical component usage (dependency is not yet formally documented).
- Likely boundary: stock, item identity, movements, reservation/consumption.
- Existing design document: none found.

### Candidate: Procurement
- Repository evidence:
	- `docs/design/maintenance.md` (procurement explicitly out of scope)
- Documented purpose: purchasing flow outside Maintenance ownership.
- Known dependencies: likely dependent on inventory demand and supplier/payment
	processes (not formally specified yet).
- Likely boundary: purchase requests, orders, supplier flow.
- Existing design document: none found.

### Candidate: Projects
- Repository evidence:
	- `docs/design/organization.md` (project listed as placeholder context)
	- `docs/design/maintenance.md` (project management out of scope; restoration
		governance explicitly points to Projects capability)
	- `README.md` (mentions restoration projects)
- Documented purpose: governance of larger restoration programs, outside
	maintenance work-order execution.
- Known dependencies: organization governance and links to maintenance activities.
- Likely boundary: project phases, budget/governance, milestone coordination.
- Existing design document: none found.

### Candidate: Document Management
- Repository evidence:
	- `docs/design/certificates_compliance.md` (binary document storage out of scope;
		document management not part of CERT)
	- `docs/design/organization.md` (document placeholder context)
	- `README.md` (mentions document archive)
- Documented purpose: archive/storage lifecycle separate from certificate metadata.
- Known dependencies: broad cross-capability references for document links.
- Likely boundary: document storage, metadata, retrieval, retention.
- Existing design document: none found.

### Candidate: Fund Administration
- Repository evidence:
	- `docs/design/organization.md` (fund placeholder context)
	- `README.md` (mentions fund administration)
- Documented purpose: funding/grant domain not part of currently locked capability
	scopes.
- Known dependencies: organization/finance/accounting interactions.
- Likely boundary: fund sources, grant lifecycle, reporting.
- Existing design document: none found.

### Candidate: Finance as standalone capability
- Repository evidence:
	- `README.md` (mentions economics)
	- `docs/design/organization.md` (Finance and Accounting contexts already modeled
		inside Organization domain)
- Documented purpose: receivables/accounting flows already present under
	Organization context.
- Known dependencies: Organization identity and membership billing flows.
- Likely boundary: if split later, it must be extracted from Organization with
	explicit boundary decision.
- Existing design document: no separate finance capability design document found.

## Dependency Analysis

### Readiness against locked foundation
- Voyages has the clearest immediate dependency path:
	- consumes Fleet vessel identity/reference
	- does not require ownership transfer from Technical Configuration,
		Maintenance, or Certificates
	- is explicitly marked as out-of-scope sibling capability in multiple locked docs

- Inventory and Procurement are valid candidates but have less explicit current
	dependency contracts than Voyages and appear downstream of maintenance outcomes.

- Projects and Document Management are broad, cross-cutting capabilities with
	higher coordination risk and wider locked-capability impact surfaces.

- Standalone Finance would require an explicit extraction/ownership decision from
	Organization before safe sequencing.

### Architectural risk summary
- Lowest near-term lock impact: Voyages.
- Medium risk (dependency clarity pending): Inventory, Procurement.
- Higher cross-cutting risk: Projects, Document Management, Finance split.

## CAP-11 Decision

### Selected capability
- CAP-11 identifier: CAP-11
- Exact capability name: Voyages
- Approved prefix: VOY
- Next waypoint identifier: VOY-000
- Status: LOCKED

### Capability purpose
Define voyage planning and operational voyage lifecycle as a separate bounded
context, without changing ownership in locked capabilities.

### Bounded-context responsibility
Voyages is responsible for voyage-centric lifecycle and execution records.
Voyages is not responsible for:
- Fleet ownership/lifecycle
- Technical component lifecycle
- Maintenance planning/work-order ownership
- Certificate lifecycle
- Document binary storage

### Dependency position
CAP-11 Voyages is sequenced immediately after CAP-10 and depends on existing
Fleet identity/reference boundaries.

Voyages may reference by identity:
- Fleet/Vessel identity
- Organization identity where required by future approved scenarios

Voyages must not own:
- Fleet aggregate state
- Technical Configuration state
- Maintenance state
- Certificate state

### Why CAP-11 Voyages precedes other candidates
1. Strongest repository evidence as explicit separate capability across multiple
	 locked domains.
2. Clearest dependency path on already locked Fleet foundation.
3. Minimal required change pressure on locked capabilities.
4. Lower architectural risk than broad cross-cutting candidates.

## Provisional Future Sequence
These entries are provisional and subject to explicit roadmap decisions.

- CAP-11 Voyages (VOY) - LOCKED
- CAP-12 Inventory (INV) - PLANNED
	- INV-002 (Inventory Persistence and Mapper) is verified complete at baseline commit 0a114fe.
	- Provenance and completeness were audited; no duplicate INV-002 implementation commit is required.
	- Accepted baseline for proceeding to INV-003: 0a114fe.
- CAP-13 Procurement (PROC) - PROVISIONAL
- CAP-14 Projects (PROJ) - PROVISIONAL
- CAP-15 Document Management (DOC) - PROVISIONAL

Note:
- Finance/fund capabilities remain provisional and require explicit boundary
	decisions relative to Organization before CAP assignment.

## Capability Naming and Prefixes
Approved prefix rules:
- Existing capability prefixes remain unchanged.
- New capability prefixes are assigned in this roadmap file at CAP decision time.
- CAP-11 approved prefix: VOY.

Existing sequence references:
- ASSET, FLEET, TECH, MAINT, CERT, ORG

## Roadmap Change Rules
Changing the capability sequence requires:
1. Explicit roadmap decision recorded in this file.
2. Documented dependency reason.
3. Assessment of locked capability impact.

A future capability must not be selected solely from conversational context or
informal mention.

Competing sequence sources are not authoritative unless this file is updated.

## Locked Capability Change Requirement
If future sequencing implies redesign of a locked capability:
- document the risk and impact,
- do not redesign within roadmap work,
- raise a separate explicit capability decision before any implementation.
