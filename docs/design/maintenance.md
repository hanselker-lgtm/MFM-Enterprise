# MAINT-000 Maintenance Capability Domain Design

## Purpose
Maintenance capability etablerer et generisk domaene til planlaegning, udfoerelse og dokumentation af vedligehold.

Maalet er at kunne:
- planlaegge forebyggende vedligehold paa vessel- og komponentniveau
- registrere korrigerende vedligehold og inspektioner
- bevare permanent vedligeholdelseshistorik
- stoette restaureringsrelaterede vedligeholdelsesarbejder
- eksponere en stabil public API-kontrakt via application services og features

Capabilityen skal kunne anvedes paa historiske fartoejer, maritime foreninger og tekniske komponenter uden hardcoding mod et specifikt fartoej.

## Bounded Context
Maintenance er et selvstaendigt bounded context med ansvar for vedligeholdelsesbehov, due state, arbejdsudfoerelse og historik.

Maintenance ejer:
- maintenance planning
- maintenance requirements
- maintenance intervals
- due state
- maintenance work
- work execution
- completion
- maintenance records
- maintenance history

Maintenance ejer IKKE:
- Vessel identity
- TechnicalComponent identity
- technical component lifecycle
- installation/removal
- replacement history
- certificates
- accounting
- projects

Technical Configuration forbliver ejer af technical component identity og technical history.

## Capability Responsibility
Maintenance capability har ansvar for:
- at modellere vedligeholdelsesbehov pr. maintenance target
- at beregne og/eller opdatere naeste forfald (next_due)
- at oprette og styre work orders gennem gyldige lifecycle transitions
- at bevare immutable completion records
- at sikre at historik ikke overskrives ved plan- eller intervalaendringer

Maintenance capability har ikke ansvar for:
- at udfoere tekniske lifecycle operationer paa komponenter
- at opdatere vessel eller component master data
- at bogfoere omkostninger

## Aggregate Boundaries
Primary aggregates:
1. MaintenancePlan (aggregate root)
2. WorkOrder (aggregate root)

Boundary-beslutning:
- MaintenancePlan ejer planlaegningskonsistens for target-specifikke vedligeholdelseskrav.
- WorkOrder ejer execution lifecycle og completion-bevis for et konkret arbejde.
- WorkOrder er ikke child aggregate under MaintenancePlan for at undgaa et for stort aggregate og for at kunne skalere execution-historik uafhaengigt af plan-opdateringer.

Transactional consistency rules:
- MaintenancePlan-transaktioner beskytter kun plan/requirement-invarians.
- WorkOrder-transaktioner beskytter kun work-order lifecycle og completion record.
- Cross-aggregate flow (fx create work order from due requirement) sker via application service orchestration og eventuelt domain events, ikke i en enkelt aggregate-transaktion.

## Maintenance Target
Maintenance benytter et kontrolleret target-begreb uden cross-capability object references.

Value Object: MaintenanceTarget
- target_type
- target_id

Target types i v1:
- VESSEL
- TECHNICAL_COMPONENT

Regler:
- target_id er identity-reference (UUID) til ekstern capability.
- ingen direkte reference til Fleet/Vessel eller TechnicalComponent domain objects.
- target_type styrer semantisk validering og integration contracts.

## Maintenance Plan
MaintenancePlan aggregate root:
- identity: maintenance_plan_id
- target: MaintenanceTarget
- status: fx DRAFT, ACTIVE, ARCHIVED
- requirements: collection af MaintenanceRequirement entities

Invarians:
- plan er bundet til praecis ét MaintenanceTarget.
- requirement identity er unik indenfor planen.
- samme requirement maa ikke forekomme dubleret med samme titel + maintenance type + interval paa samme target uden eksplicit tilladelse.
- arkiveret plan kan ikke modtage nye requirements.

## Maintenance Task/Requirement Decision
Valgt begreb: MaintenanceRequirement

Begrundelse:
- "Requirement" beskriver et varigt vedligeholdelsesbehov over tid.
- "Task" kan misforstaas som en enkelt execution (som i dette design modelleres af WorkOrder).
- Skellet mellem "krav" (plan) og "arbejde" (work order) giver ren historik og tydelig aggregate boundary.

MaintenanceRequirement (entity under MaintenancePlan) indeholder:
- requirement_id
- title
- description
- maintenance_target
- maintenance_type
- interval
- due_basis
- last_completed
- next_due
- status
- instructions
- notes

## Maintenance Types
MaintenanceType i v1:
- PREVENTIVE
- CORRECTIVE
- INSPECTION
- CONDITION_BASED
- RESTORATION

Beslutning om RESTORATION:
- RESTORATION medtages i MaintenanceType i v1, fordi restaureringsarbejder kan vaere legitim vedligeholdelsesaktivitet paa historiske fartoejer.
- Stoerre restaureringsprogrammer med budget, faseplan og governance hoerer fortsat i Projects capability.
- Maintenance kan derfor registrere restaureringsrelateret arbejde operationelt, mens projektstyring forbliver udenfor scope.

## Interval Model
Value Object: MaintenanceInterval

Formaal:
- kontrolleret model for intervaller uden regelmotor-kompleksitet.

Foreslaaede felter:
- interval_type
- interval_value

Interval types i v1:
- CALENDAR_DAYS
- CALENDAR_MONTHS
- CALENDAR_YEARS
- RUNNING_HOURS

Fremtidig udvidelse (ikke implementeret i v1):
- ENGINE_HOURS
- OPERATING_CYCLES

Valideringsregler:
- interval_value skal vaere positiv integer (> 0).
- interval_type skal vaere en godkendt enum-vaerdi.
- kalenderbaserede intervaller anvedes kun med datobaseret due basis.
- running-hours intervaller anvedes kun med runtime-baseret due basis.

## Due Calculation
Ansvar:
- MaintenancePlan (eller en dedikeret domain service kaldt af planen) beregner next_due for hvert requirement baseret paa requirementets due_basis og interval.

Modelbeslutning:
- next_due persistes som planlagt naeste forfald for effektiv forespoergsel og stabil historik af plan-state.
- next_due kan re-beregnes deterministisk ved relevante state-aendringer.

Overdue-beregning:
- overdue bestemmes ved eksplicit supplied current/as_of date.
- ingen skjult system clock i domain.

Eksempel:
last_completed + interval = next_due

Running-hours uden telemetry capability:
- running-hours data tilfoeres eksplicit som supplied observation (fx observed_running_hours, observed_at).
- domain beregner due status ud fra supplied observation.
- automatisk indsamling af timer ligger udenfor MAINT-000 scope.

## Work Order
WorkOrder er selvstaendigt aggregate root.

Felter i v1:
- work_order_id
- maintenance_requirement_id
- maintenance_target
- title
- description
- status
- planned_date
- started_at
- completed_at
- performed_by reference
- notes

Designnoter:
- work order kan oprettes fra et requirement eller ad hoc (saerligt for corrective arbejde).
- maintenance_target kopieres ind i work order for sporbarhed.
- performed_by modelleres som kontrolleret reference (se Organization/People Boundary).

## Work Order Lifecycle
Lifecycle i v1:
PLANNED -> OPEN -> IN_PROGRESS -> COMPLETED

CANCELLED vurdering:
- CANCELLED medtages i v1 for realistisk driftsbehov.

Gyldige transitions:
- PLANNED -> OPEN
- OPEN -> IN_PROGRESS
- IN_PROGRESS -> COMPLETED
- PLANNED -> CANCELLED
- OPEN -> CANCELLED

Ugyldige transitions (eksempler):
- COMPLETED -> enhver anden status
- CANCELLED -> enhver anden status
- PLANNED -> COMPLETED (uden faktisk execution)
- OPEN -> COMPLETED (uden start, medmindre eksplicit policy senere indfoeres)

## Maintenance Record
Valgt model:
- MaintenanceRecord er immutable completion record entity under WorkOrder.

Begrundelse:
- mindst komplekse model som stadig sikrer permanent historik.
- recordet oprettes ved completion og muteres ikke efterfoelgende.
- intet separat aggregate/repository i v1 er noedvendigt.

Konsekvens:
- WorkOrder owner completion-bevis.
- history queries kan bygges via WorkOrder repository/read-model uden nyt aggregate.

## Historical Maintenance
Kravopfyldelse:
- Flere work orders kan knyttes til samme MaintenanceRequirement over tid.
- Hver completed work order opretter et immutable MaintenanceRecord.
- Aendring af interval eller instruktion paa MaintenanceRequirement omskriver ikke tidligere records.

Eksempelspor:
Maintenance Requirement A
-> WorkOrder 2027-001 -> Completed -> MaintenanceRecord
-> WorkOrder 2028-004 -> Completed -> MaintenanceRecord

## Technical Configuration Boundary
Integration design:
Technical Configuration -> TechnicalComponentId -> MaintenanceTarget -> MaintenancePlan

Boundary-regler:
- Maintenance gemmer kun identity/reference til component.
- Maintenance maa ikke opdatere component status.
- Maintenance maa ikke installere/remove/replace components.
- Maintenance maa ikke eje component specifications.

Hvis vedligehold finder behov for replacement:
- Maintenance registrerer finding i work order/record.
- en separat TECH operation (udenfor Maintenance aggregate) skal senere udfoeres via Technical Configuration capability.
- ingen direkte replacement execution i Maintenance.

## Organization/People Boundary
Work performer kan vaere:
- member
- volunteer
- external person
- external company

Value Object: PerformerReference
- performer_type (MEMBER, VOLUNTEER, EXTERNAL_PERSON, EXTERNAL_COMPANY)
- performer_id_or_external_key
- display_name_snapshot (optional)

Boundary:
- kun identity/reference-behov modelleres.
- ingen kopiering af Member/Volunteer/Organization domain.

## Finance Boundary
Maintenance ejer ikke bogfoering.

Fremtidigt integration point:
- WorkOrder completion kan udstille expense/reference payload til Finance capability.
- ingen accounting-model eller cost-ledger i MAINT-000.

## Domain Events
Relevante events i v1:
- MaintenanceRequirementCreated
- MaintenanceBecameDue
- WorkOrderCreated
- WorkOrderStarted
- WorkOrderCompleted
- WorkOrderCancelled
- MaintenanceRecordCreated

Event-principper:
- kun events med klart domaeneansvar.
- undgaa event inflation (ingen events for trivielle feltopdateringer uden forretningsbetydning).

## Repositories
Aggregate root repositories:
- MaintenancePlanRepository
  - add
  - get_by_id
  - list_by_target
  - update
  - delete
  - exists
- WorkOrderRepository
  - add
  - get_by_id
  - list_by_target
  - list_by_requirement
  - list_by_status
  - update
  - exists

Beslutning om MaintenanceRecord repository:
- intet separat repository i v1, da MaintenanceRecord er entity under WorkOrder.

## Application Services
Foreslaaede use cases i v1:
- CreateMaintenancePlanUseCase
- AddMaintenanceRequirementUseCase
- UpdateMaintenanceRequirementUseCase
- CalculateDueMaintenanceUseCase
- CreateWorkOrderUseCase
- StartWorkOrderUseCase
- CompleteWorkOrderUseCase
- CancelWorkOrderUseCase
- GetMaintenanceHistoryUseCase

Orchestration-princip:
- application services binder MaintenancePlan og WorkOrder flows via references og UnitOfWork.

## Feature API
Public API foelger eksisterende Public API Standard:
- execute(request)
- immutable Request DTO
- immutable Response DTO
- API-safe types (UUID, str, date, enums, primitive values)
- ingen domain object leakage
- ingen Value Object leakage
- ingen persistence leakage
- konsistent exception mapping (ApplicationException, ValidationException, BusinessRuleViolation, RepositoryException)

## End-to-End Workflows
Planlagte E2E workflows for senere implementation/verification:
1. Create maintenance plan for vessel
2. Create maintenance plan for technical component
3. Calculate due maintenance
4. Create and complete work order
5. Preserve maintenance history
6. Change maintenance interval without rewriting history
7. Technical component boundary
8. Failure/rollback workflow

## Architecture
Dependency direction:
- Maintenance maa referere identities fra Fleet, Technical Configuration og People contexts.
- Maintenance maa ikke importere deres infrastructure internals.
- Locked capabilities (Asset Core, Fleet, Technical Configuration) maa ikke aendres.
- Ingen Maintenance imports i TECH domain.
- Ingen reverse dependency fra TECH til Maintenance.

Layering:
- domain -> ingen persistence/GUI dependencies
- application -> repository contracts + UnitOfWork boundary
- features -> public DTO API, ingen direkte repository/persistence access

## Alvur Validation Scenarios
Scenario 1 (engine oil change):
- Target: TECHNICAL_COMPONENT
- Requirement: Change lubricating oil
- Interval: 12 months
- Flow: due -> work order -> completion -> permanent maintenance record

Scenario 2 (CPP inspection with replacement finding):
- Target: TECHNICAL_COMPONENT
- Requirement: Inspect pitch mechanism
- Flow: inspection completed -> finding recorded -> possible later TECH replacement via separate capability flow

Scenario 3 (wooden vessel hull inspection):
- Target: VESSEL
- Requirement: Inspect hull planking
- Flow: work order -> completion record
- Demonstrerer at design fungerer uden technical_component_id.

## Risks
- Running-hours based due logic afhanger af kvaliteten af supplied runtime observation data.
- For mange ad hoc work orders uden requirement-link kan svakke planstyring, hvis policy ikke fastlaegges tydeligt.
- RESTORATION type kraever klar governance mod Projects for at undgaa scope overlap i senere capabilities.

## Ikke maal
MAINT-000 omfatter ikke:
- technical component lifecycle
- component replacement
- certificates
- voyages
- inventory/spare parts
- procurement
- accounting
- project management
- GUI
- telemetry
- automatic engine-hour collection

## Design Recommendation
READY FOR DOMAIN IMPLEMENTATION

## Capability Status (CAP-09 Maintenance)

Status: LOCKED

Status pr. 2026-07-11:
- MAINT-000: design dokumenteret.
- MAINT-001: domain implementeret og testet.
- MAINT-002: SQLAlchemy persistence + mapper implementeret og testet.
- MAINT-003: repository contract + SQLite repository implementeret og testet.
- MAINT-004: application services implementeret og testet.
- MAINT-005: feature layer implementeret og testet.
- MAINT-006: end-to-end integration workflows implementeret og testet.
- MAINT-007: capability review dokumenteret i maintenance_capability_review.md med konklusion READY FOR LOCK.
- MAINT-007A: lock-blocking findings korrigeret med passerende regression tests.

Lock-regler:
- Eksisterende public Maintenance API betragtes som stabil.
- Kun fejlrettelser maa aendre laast adfaerd uden ny plan.
- Component lifecycle, replacement og technical ownership forbliver i Technical Configuration.
- Certificates implementeres som separat capability.
- Voyages implementeres som separat capability.
- Asset Core og Fleet maa ikke udvides via Maintenance lock-aendringer.

Kvalitetsgate:
- Fuldt regressionssaet skal vaere groent (0 failures, 0 warnings).
- Permanente architecture compliance tests skal vaere groenne.
- Historical truth, aggregate boundaries og public API boundary maa ikke brydes.
