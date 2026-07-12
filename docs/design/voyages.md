# VOY-000 Generic Voyages Core Design

## Purpose
Voyages defines a generic maritime voyage capability for planning and recording voyage execution history across association vessels, preserved vessels, commercial-style vessel records, and historical voyage records.

The scope is domain design only. The capability is generic and does not hardcode vessel names, jurisdictions, ports, or maritime authorities.

## Bounded Context
Voyages is a standalone bounded context.

Voyages owns:
- voyage identity
- vessel identity reference
- voyage reference value
- planned departure and planned arrival context
- actual departure and actual arrival context
- voyage lifecycle
- voyage purpose classification
- voyage notes
- historical voyage truth for planned versus actual state

Voyages does not own:
- vessel aggregate lifecycle or metadata ownership
- fleet registration or vessel technical identity
- technical configuration, maintenance, or certificate lifecycle
- crew management and employment domains
- navigation planning systems, telemetry tracks, or binary document storage

## Aggregate Boundary
Primary aggregate root:
- Voyage

Boundary decision:
- One aggregate root is sufficient for CAP-11 first scope.
- Planned and actual state are owned by Voyage and must be preserved together for historical truth.
- No secondary aggregates are required in first scope.

## Voyage Aggregate
Voyage aggregate state (first scope):

Required:
- voyage_id
- vessel_id
- planned_departure_location
- planned_arrival_location
- planned_departure_at
- planned_arrival_at
- status

Optional:
- voyage_reference
- actual_departure_location
- actual_arrival_location
- departed_at
- arrived_at
- voyage_purpose
- notes
- cancellation_reason
- cancelled_at
- cancelled_by_reference

State ownership rules:
- planned fields are never overwritten by actual fields
- actual arrival location may differ from planned arrival location
- completed and cancelled voyages are terminal and immutable except append-only audit metadata if later approved

## Vessel Reference
Approved vessel association model:
- identity/reference only via vessel_id

Boundary rule:
- Voyage stores vessel_id and does not store or own vessel registration, status, dimensions, machinery, or lifecycle state.
- Voyage must not depend on Fleet infrastructure.

## Location / Port Model
Decision: Option C, external location identity plus historical name snapshot, without a Port aggregate.

Value object model:
- location_external_id (optional)
- name_snapshot (required)
- locality_snapshot (optional)
- country_snapshot (optional)

Rationale:
- preserves historical readability even if external registry names change
- supports optional integration with external location registries
- avoids introducing a dedicated Port capability in CAP-11

## Voyage Purpose
Decision: controlled value object with bounded code set plus optional free detail text.

Model:
- purpose_code (controlled code)
- purpose_detail (optional short text)

Initial code set for first scope:
- OPERATIONAL
- TRAINING
- PRESERVATION
- DEMONSTRATION
- TRANSFER
- INSPECTION
- OTHER

Rule:
- codes are capability-owned and generic, with no legislation-specific semantics.

## Planned and Actual Time Model
Voyage distinguishes planned and actual timeline explicitly.

Planned state:
- planned_departure_at
- planned_arrival_at

Actual state:
- departed_at
- arrived_at

Chronology invariants:
- planned_departure_at <= planned_arrival_at
- if both actual timestamps are set: departed_at <= arrived_at
- if departed_at is set then status must be UNDERWAY or COMPLETED
- if arrived_at is set then status must be COMPLETED

Historical truth rule:
- planned timestamps remain preserved and are never replaced by actual timestamps.

## Lifecycle
Voyage lifecycle states in first scope:
- DRAFT
- PLANNED
- UNDERWAY
- COMPLETED
- CANCELLED

Allowed transitions:
- DRAFT -> PLANNED
- DRAFT -> CANCELLED
- PLANNED -> UNDERWAY
- PLANNED -> CANCELLED
- UNDERWAY -> COMPLETED

Not allowed:
- transitions out of COMPLETED
- transitions out of CANCELLED
- direct DRAFT -> UNDERWAY
- direct PLANNED -> COMPLETED without departure

Terminal states:
- COMPLETED
- CANCELLED

## Historical Voyage Truth
Voyages supports planned and actual divergence.

Example supported by model:
- planned departure A, planned arrival B, planned times P1/P2
- actual departure A, actual arrival C, actual times A1/A2

Rules:
- planned arrival context remains B
- actual arrival context remains C
- both planned and actual records remain available in the same aggregate history

## Departure Operation
Domain operation concept:
- depart(departed_at, actual_departure_location)

Preconditions:
- current status must be PLANNED
- departed_at must be explicitly supplied
- departed_at must be greater than or equal to planned_departure_at policy floor if policy is enabled in application layer

Effects:
- set departed_at
- set actual_departure_location
- transition status to UNDERWAY
- emit VoyageDeparted event

Clock rule:
- no hidden clock usage; time must be provided as input.

## Arrival Operation
Domain operation concept:
- arrive(arrived_at, actual_arrival_location)

Preconditions:
- current status must be UNDERWAY
- arrived_at must be explicitly supplied
- departed_at must already exist
- arrived_at must be greater than or equal to departed_at

Effects:
- set arrived_at
- set actual_arrival_location
- transition status to COMPLETED
- preserve planned arrival fields unchanged
- emit VoyageArrived event

Clock rule:
- no hidden clock usage; time must be provided as input.

## Cancellation Decision
Cancellation is included in first scope.

Allowed source states:
- DRAFT
- PLANNED

Cancellation fields:
- cancellation_reason (required on cancellation)
- cancelled_at (required, explicitly supplied)
- cancelled_by_reference (optional)

Terminal behavior:
- CANCELLED is terminal and cannot be re-opened.

## Time and Timezone Policy
Decision:
- use timezone-aware datetime for all voyage timestamps.

Policy:
- timestamps are accepted as timezone-aware input and normalized to UTC for persistence-independent domain comparisons.
- display/local timezone transformation is outside domain scope.
- no hidden date.today or datetime.now calls in domain operations.

## Voyage Reference / Number
Decision:
- voyage_reference is optional and externally supplied when available.

Uniqueness responsibility:
- uniqueness by vessel and reference belongs to repository/application boundary, not domain sequence generation.
- domain validates format constraints only if a reference is provided.

## Crew Boundary
Decision:
- no crew state in CAP-11 first scope.

Out of scope:
- employment
- rank management
- person certificates
- payroll
- watch schedules

Future possibility:
- person identity references may be added later by explicit roadmap decision if voyage invariants require it.

## Fleet Boundary
Fleet is locked and protected.

Voyages boundary result:
- consume Fleet by vessel identity/reference only
- no Fleet aggregate ownership
- no Fleet infrastructure dependency
- no Fleet API behavior changes required

## Asset Boundary
Decision:
- Voyage references Vessel identity only.
- Voyage does not directly reference Asset identity in first scope.

Rationale:
- avoids redundant ownership and preserves existing Fleet boundary.

## Certificates Boundary
Certificates and Compliance is locked and protected.

Voyages boundary result:
- no certificate issuance, renewal, expiry evaluation, or compliance mutation in Voyage aggregate
- any future departure-readiness checks are application integration concerns outside VOY-000 domain core

## Maintenance Boundary
Maintenance is locked and protected.

Voyages boundary result:
- no MaintenancePlan, WorkOrder, or MaintenanceRecord ownership
- voyage outcomes may later be consumed by Maintenance through explicit integration outside VOY-000

## Technical Configuration Boundary
Technical Configuration is locked and protected.

Voyages boundary result:
- no machinery configuration ownership
- no component state/specification ownership
- no Technical Configuration infrastructure dependency

## Position / Track Data Decision
Decision for CAP-11 first scope:
- no position observation stream
- no GPS/AIS track storage
- only departure and arrival location/time context

## Passage Planning Boundary
Decision:
- passage planning is out of scope for CAP-11.

Out of scope examples:
- berth-to-berth route planning
- waypoints and safety contour logic
- CATZOC, cross-track distance, parallel index
- pilot/tug planning
- weather routing and navigation optimization

## Document Reference Decision
Decision:
- optional voyage document_reference metadata is allowed in first scope.
- metadata/reference only.

Out of scope:
- binary storage
- filesystem/blob handling
- document management subsystem ownership

## Domain Events
Meaningful voyage domain events for first scope:
- VoyageCreated
- VoyagePlanned
- VoyageDeparted
- VoyageArrived
- VoyageCancelled

Event guidance:
- emit only for lifecycle-significant transitions
- avoid event inflation for trivial field edits

## Repository Contract
VoyageRepository contract for first scope:
- add(voyage)
- get_by_id(voyage_id)
- update(voyage)
- exists(voyage_id)
- list()
- get_by_vessel(vessel_id)
- get_planned(vessel_id optional)
- get_underway(vessel_id optional)
- get_completed(vessel_id optional)
- get_by_period(start_at, end_at, vessel_id optional)

Contract rules:
- repository returns domain aggregate instances
- no persistence model leakage in contract

## Application Use Cases
First-scope use cases:
- CreateVoyage
- PlanVoyage
- DepartVoyage
- ArriveVoyage
- CancelVoyage
- GetVoyage
- ListVesselVoyages

Optional justified query use case:
- ListVoyagesByPeriod

## Public Feature API
Expected public feature entry points follow execute(request) convention:
- CreateVoyageFeature
- PlanVoyageFeature
- DepartVoyageFeature
- ArriveVoyageFeature
- CancelVoyageFeature
- GetVoyageFeature
- ListVesselVoyagesFeature
- ListVoyagesByPeriodFeature

Public API rules:
- request and response DTOs are immutable
- response fields are primitive and API-safe
- no Voyage aggregate leakage
- no value object leakage
- no persistence leakage

## Failure Model
Domain failure categories:
- invalid planned chronology
- invalid actual chronology
- invalid lifecycle transition
- arrival before departure
- cancellation from invalid state
- invalid purpose code
- invalid location snapshot

Application/boundary failure categories:
- invalid vessel reference
- duplicate voyage reference where uniqueness policy applies
- voyage not found
- repository/infrastructure failures

Mapping boundary:
- domain raises business rule failures
- application maps boundary and repository failures to application exception model

## Generic Maritime Validation Scenarios
Scenario 1, planned and actual aligned:
- planned departure A, planned arrival B, planned P1/P2
- actual departure A, actual arrival B, actual A1/A2
- design preserves both planned and actual context

Scenario 2, planned and actual destination divergence:
- planned arrival B
- actual arrival C
- design preserves planned B and actual C independently

Scenario 3, planned then cancelled:
- voyage is planned and cancelled with explicit reason and timestamp
- lifecycle ends in terminal CANCELLED

Scenario 4, fleet metadata changes after completion:
- voyage remains linked by vessel_id
- voyage does not own or copy Fleet state
- historical voyage remains valid through identity reference

## Non-Goals
CAP-11 first scope non-goals:
- passage planning and ECDIS functionality
- AIS and GPS track storage
- weather routing
- fuel optimization and bunkers
- crew management and payroll
- watch scheduling
- Maintenance workflow ownership
- certificate lifecycle ownership
- technical configuration ownership
- inventory and procurement ownership
- finance ownership
- project management ownership
- binary document storage
- GUI behavior

## Design Recommendation
READY FOR DOMAIN IMPLEMENTATION

## Capability Status (CAP-11 Voyages)

Status: LOCKED

Status pr. 2026-07-12:
- VOY-000: design dokumenteret.
- VOY-001: domain implementeret og testet.
- VOY-002: SQLAlchemy persistence + mapper implementeret og testet.
- VOY-003: repository contract + SQLite repository implementeret og testet.
- VOY-004: application services implementeret og testet.
- VOY-005: feature layer implementeret og testet.
- VOY-006: end-to-end integration workflows implementeret og testet.
- VOY-007: capability review dokumenteret i voyage_capability_review.md med konklusion READY FOR LOCK.
- VOY-008: capability locked.

Lock-regler:
- Eksisterende public Voyages API betragtes som stabil.
- Kun fejlrettelser maa aendre laast adfaerd uden ny plan.
- Voyage lifecycle ownership forbliver i Voyage domain aggregate.
- Vessel association er identity/reference only via vessel_id (UUID); Fleet aggregate maa ikke ejes af Voyages.
- Planned voyage context og actual voyage context forbliver uafhaengige og maa ikke sammenlaegges.
- Historical voyage truth maa ikke brydes: planlagt destination forbliver planlagt destination; faktisk ankomst forbliver faktisk ankomst.
- Alle lifecycle timestamps (departed_at, arrived_at, cancelled_at) skal vaere eksplicit supplied; ingen hidden clock i Voyage production code.
- Repository ejer ikke transaktionsgrænsen; UnitOfWork ejer commit/rollback.
- Mapper restoration maa ikke afspille Voyage domain operationer eller emittere falske lifecycle events.
- Public Feature API foelger execute(request) med immutable request/response DTOs; response felter er primitive og API-safe.
- Voyages ejer ikke Fleet, Certificates, Maintenance eller Technical Configuration adfaerd.
- Passage planning, ECDIS, AIS, GPS track storage og telemetri forbliver uden for laast CAP-11 scope.
- Fleet og Organization anvendes kun via identity/reference boundaries.
- Ingen document storage subsystem maa introduceres i Voyage capability.

Kvalitetsgate:
- Fuldt regressionssaet skal vaere groent (0 failures, 0 warnings).
- Permanente architecture compliance tests skal vaere groenne.
- Historical voyage truth og aggregate boundaries maa ikke brydes.
