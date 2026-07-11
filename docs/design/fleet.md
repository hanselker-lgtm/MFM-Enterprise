# FLEET-000 Fleet Design

## Purpose
Fleet capability etablerer domænet for styring af flåder og relationen mellem flåder og assets.

Målet er at kunne:
- oprette og vedligeholde flådestrukturer
- registrere medlemskab af assets i flåder
- håndhæve flådeinvarians og statusregler
- eksponere en stabil og testbar API-kontrakt via application services og features

## Bounded Context
Fleet er et selvstændigt bounded context med ansvar for organisatorisk gruppering af assets.

Context ansvar:
- Fleet identitet og klassifikation
- Fleet status og livscyklus
- Fleet-Asset medlemskab
- Fleet metadata (for eksempel navn, beskrivelse, formål)

Context grænser:
- Fleet definerer ikke asset-domæneregler (ejes af Asset capability)
- Fleet håndterer ikke operationel planlægning (rejser, vedligehold, certifikater)

## Aggregates
Primære aggregates i Fleet:

- Fleet
  - root: Fleet
  - ansvar: konsistens for fleet-identitet, status og medlemskaber
  - invariants:
    - fleet_id er entydig
    - fleet_code er entydig i scope
    - fleet_name er obligatorisk og gyldigt
    - medlemskab må ikke indeholde samme asset mere end én gang
    - statusovergange følger tilladt transition-matrix

- FleetMembership
  - indlejret entity under Fleet (anbefalet)
  - ansvar: relation mellem fleet og asset med tids- og rolleattributter
  - invariants:
    - asset_id er obligatorisk
    - joined_at er obligatorisk
    - left_at kan ikke være før joined_at

## Value Objects
Fleet value objects skal være immutable.

Foreslåede value objects:
- FleetId
- FleetCode
- FleetName
- FleetStatus
- FleetCategory
- FleetMembershipId
- MembershipPeriod

Regel:
- Value objects repræsenterer validerede begreber uden identitet og må ikke kunne muteres efter oprettelse.

## Repositories
Repository contracts ved application boundary:

- FleetRepository
  - add
  - get_by_id
  - get_by_code
  - update
  - delete
  - exists
  - list
  - search

UnitOfWork:
- Alle write-operationer gennemføres i en explicit UnitOfWork.
- Commit/rollback defineres centralt i UnitOfWork-kontrakten.

Regel:
- Repositories returnerer domæneobjekter eller response DTO mapping contracts, aldrig ORM-modeller.

## Events
Domæne- og applikationsevents for løs kobling:

- FleetCreatedEvent
- FleetUpdatedEvent
- FleetRenamedEvent
- FleetActivatedEvent
- FleetDeactivatedEvent
- AssetAssignedToFleetEvent
- AssetRemovedFromFleetEvent
- FleetArchivedEvent

Event-principper:
- Events er immutable payloads.
- Events publiceres efter succesfuld commit.
- Event-navne er business-orienterede og versionsstabile.

## Application Services
Foreslåede use cases:

- CreateFleetUseCase
- UpdateFleetUseCase
- ActivateFleetUseCase
- DeactivateFleetUseCase
- AssignAssetToFleetUseCase
- RemoveAssetFromFleetUseCase
- GetFleetUseCase
- ListFleetsUseCase
- SearchFleetsUseCase

Principper:
- Request DTO immutable
- Response DTO immutable
- Validation, business rules, UnitOfWork og event dispatch i ét konsistent flow

## Features
Feature layer entry points:

- CreateFleetFeature
- UpdateFleetFeature
- ActivateFleetFeature
- DeactivateFleetFeature
- AssignAssetToFleetFeature
- RemoveAssetFromFleetFeature
- GetFleetFeature
- ListFleetsFeature
- SearchFleetsFeature

Feature-principper:
- Standard signatur: execute(request)
- Returnerer kun response DTO'er
- Ingen domain entities eller persistence-objekter i output
- Standardiseret exception mapping

## Public API
Public API følger capability-standarden:

- Input: immutable Request DTO
- Output: immutable Response DTO
- Fejltyper:
  - ApplicationException
  - ValidationException
  - BusinessRuleViolation
  - RepositoryException

Kontraktskrav:
- API er stabil på tværs af persistence-implementeringer.
- API eksponerer ikke interne ORM/persistence detaljer.

## Integration Points
Fleet integrerer via kontrakter:

- Feature API til GUI og eksterne workflows
- Application services til intern orchestration
- Repository interfaces til persistence adapters
- Event dispatcher/event bus til inter-capability kommunikation

Vigtige regler:
- Ingen direkte afhængighed til GUI i domæne/persistence
- Integrationer går via application boundary og events
- Dependency guards skal håndhæve lagdeling

## Asset relation
Fleet capability relaterer til Asset capability gennem referencer, ikke ejerskab af asset-tilstand.

Regler for relationen:
- FleetMembership refererer til asset_id fra Asset capability
- Fleet validerer kun medlemskabskonsistens (ikke asset lifecycle)
- Asset eksisterer uafhængigt af Fleet
- Ved asset-sletning håndteres medlemskab via policy (for eksempel event-drevet cleanup)

## Ikke mål
Dette design omfatter ikke:

- Motor
- Maintenance
- Voyages
- Certificates

Eksplicit afgrænsning:
Fleet capability modellerer flådestruktur og asset-medlemskab, men ikke motor-, vedligeholds-, rejse- eller certifikatdomæner.

## Capability Status (CAP-07 Fleet)

Status: LOCKED

Status pr. 2026-07-11:
- FLEET-000: design dokumenteret.
- FLEET-001: vessel domain implementeret og testet.
- FLEET-002: SQLAlchemy persistence + mapper implementeret og testet.
- FLEET-003: repository contract + SQLite repository implementeret og testet.
- FLEET-004: application services implementeret og testet.
- FLEET-005: feature layer implementeret og testet.
- FLEET-006: end-to-end integration workflows implementeret og testet.
- FLEET-007: capability review dokumenteret i fleet_capability_review.md med konklusion READY FOR LOCK.

Lock-regler:
- Eksisterende public Fleet API betragtes som stabil.
- Kun fejlrettelser må ændre låst adfærd uden ny plan.
- Nye maritime områder implementeres som nye capabilities.
- Engine må ikke tilføjes til Fleet Core.
- Maintenance må ikke tilføjes til Fleet Core.
- Certificates må ikke tilføjes til Fleet Core.
- Voyages må ikke tilføjes til Fleet Core.

Kvalitetsgate:
- Fuldt regressionssæt skal være grønt (0 failures, 0 warnings).
- Permanente architecture compliance tests skal være grønne.
- Asset ↔ Fleet dependency direction og public API boundary må ikke brydes.
