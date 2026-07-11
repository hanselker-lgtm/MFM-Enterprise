# TECH-000 Technical Configuration Domain Design

## Purpose
Technical Configuration capability etablerer et generisk teknisk domæne til registrering af tekniske installationer og komponenter knyttet til et Vessel.

Målet er at kunne:
- beskrive et fartojs tekniske konfiguration uden ændring af Fleet Core
- bevare teknisk historik ved installation, udskiftning og fjernelse
- understotte strukturel kobling mellem tekniske komponenter (drivlinje m.v.)
- eksponere en stabil public API-kontrakt via application services og features

Capability'en skal kunne modellere tekniske konfigurationer for historiske og moderne fartojer, inklusive situationsbestemt ændring over tid.

## Bounded Context
Technical Configuration er et selvstændigt bounded context med ansvar for teknisk struktur og komponenthistorik pr. vessel-reference.

Context ansvar:
- technical configuration identity pr. vessel_id
- technical component identity og klassifikation
- installation/removal/replacement historik
- teknisk struktur og relationer mellem komponenter
- domænekontrollerede tekniske specifikationer

Context grænser:
- ejer ikke Vessel aggregate eller Fleet lifecycle
- ejer ikke Asset Core data/lifecycle
- ejer ikke maintenance processer
- ejer ikke certificate lifecycle

## Capability Responsibility
Technical Configuration ejer:
- technical configuration structure
- technical component identity
- technical specification model
- installation/removal lifecycle for components
- replacement and component history

Technical Configuration ejer ikke:
- maintenance plans
- work orders
- inspections
- service history
- maintenance intervals
- certificate issue/expiry/renewal flows

## Aggregates
Primært aggregate:

- TechnicalConfiguration
  - root: TechnicalConfiguration
  - identity: technical_configuration_id
  - external reference: vessel_id (UUID reference til Fleet/Vessel)
  - ansvar: samlet konsistens for komponenter, struktur og historik for et vessel
  - invariants:
    - vessel_id er obligatorisk og uforanderlig efter oprettelse
    - component_id er entydig indenfor aggregate
    - aktiv komponent kan ikke have removed_date
    - removed component skal have removed_date
    - replacement relation må ikke skabe cykliske erstatningskæder
    - en component må ikke være current hvis den har replacement successor

Designvalg:
- TechnicalComponent modelleres som entity under TechnicalConfiguration aggregate.
- Ingen separate aggregates pr. komponenttype i v1.

## Entities
Foreslåede entities under TechnicalConfiguration:

- TechnicalComponent
  - identity: component_id
  - felter:
    - component_type
    - name
    - manufacturer
    - model
    - serial_number
    - build_year
    - installed_date
    - removed_date
    - status
    - notes
    - specification
  - regler:
    - installed_date obligatorisk ved aktiv installation
    - removed_date kan ikke være tidligere end installed_date
    - status skal være konsistent med installed_date/removed_date

- ComponentLink
  - identity: link_id
  - ansvar: beskriver teknisk relation i konfigurationsstrukturen
  - felter:
    - upstream_component_id
    - downstream_component_id
    - link_role (f.eks. DRIVES, COUPLED_TO, FEEDS, CONTROLS)
    - effective_from
    - effective_to
  - regler:
    - link-referencer skal pege på eksisterende components i aggregate
    - effektiv periode skal være gyldig

- ComponentReplacementRecord
  - identity: replacement_id
  - ansvar: historisk spor for udskiftning
  - felter:
    - replaced_component_id
    - replacement_component_id
    - replaced_on
    - reason
    - notes
  - regler:
    - replaced_component_id og replacement_component_id skal være forskellige
    - replaced_on skal være lig med eller senere end replaced components installed_date

## Value Objects
Technical Configuration value objects skal være immutable.

Foreslåede value objects:
- TechnicalConfigurationId
- TechnicalComponentId
- TechnicalComponentType
- TechnicalComponentStatus
- ManufacturerName
- ComponentModelName
- SerialNumber
- BuildYear
- InstallationPeriod
- ComponentNotes
- ComponentLinkRole
- ReplacementReason

TechnicalComponentType skal i v1 mindst understotte:
- PROPULSION_ENGINE
- AUXILIARY_ENGINE
- GEARBOX
- SHAFT
- PROPELLER
- GENERATOR
- PUMP
- STEERING_GEAR
- TANK
- OTHER

Regel:
- typed component klassifikation bruges via value object/enums, ikke subclass-hierarki.

## Repositories
Repository contracts ved application boundary:

- TechnicalConfigurationRepository
  - add
  - get_by_id
  - get_by_vessel_id
  - update
  - exists
  - list
  - search

UnitOfWork:
- alle write-operationer gennemfores i explicit UnitOfWork
- commit/rollback defineres centralt i UnitOfWork-kontrakten

Regel:
- repositories returnerer domain aggregate/DTO-mapping kontrakter, aldrig ORM-modeller.

## Domain Events
Forslaede events:
- TechnicalConfigurationCreatedEvent
- TechnicalComponentInstalledEvent
- TechnicalComponentRemovedEvent
- TechnicalComponentReplacedEvent
- TechnicalConfigurationStructureChangedEvent
- TechnicalSpecificationUpdatedEvent

Event-principper:
- immutable payloads
- publiceres efter succesfuld commit
- beskriver business-tilstand, ikke persistence detaljer

## Application Services
Foreslaede use cases:
- CreateTechnicalConfigurationUseCase
- InstallTechnicalComponentUseCase
- RemoveTechnicalComponentUseCase
- ReplaceTechnicalComponentUseCase
- UpdateTechnicalSpecificationUseCase
- LinkTechnicalComponentsUseCase
- UnlinkTechnicalComponentsUseCase
- GetTechnicalConfigurationUseCase
- ListTechnicalConfigurationsUseCase

Principper:
- immutable request/response DTO
- request.validate()
- UnitOfWork scope
- repository access via kontrakt
- konsistent exception-oversaettelse

## Features
Feature layer entry points:
- CreateTechnicalConfigurationFeature
- InstallTechnicalComponentFeature
- RemoveTechnicalComponentFeature
- ReplaceTechnicalComponentFeature
- UpdateTechnicalSpecificationFeature
- LinkTechnicalComponentsFeature
- UnlinkTechnicalComponentsFeature
- GetTechnicalConfigurationFeature
- ListTechnicalConfigurationsFeature

Feature-principper:
- standard signatur: execute(request)
- returnerer kun response DTO'er
- ingen domain entity/persistence leakage
- standardiseret exception mapping

## Public API
Public API følger eksisterende capability-standard:
- Input: immutable Request DTO
- Output: immutable Response DTO
- Fejltyper:
  - ApplicationException
  - ValidationException
  - BusinessRuleViolation
  - RepositoryException

Kontraktskrav:
- API maa ikke eksponere ORM/persistence internals
- API maa ikke returnere Fleet eller Asset domain objects
- Vessel reference eksponeres som vessel_id (UUID)

## Integration Points
Integration sker via kontrakter:
- Feature API til GUI og workflows
- Application services til intern orchestration
- Repository interfaces til persistence adapters
- Event dispatcher/event bus til inter-capability integration

Integration med Fleet:
- Technical Configuration modtager vessel_id som reference
- Technical Configuration maa validere existence via application boundary contract (read model/service), ikke via Fleet infrastructure import

Integration med Asset:
- ingen direkte Asset infrastructure dependency
- ingen mutation af Asset Core state

## Asset ↔ Fleet ↔ Technical dependency direction
Tilladt dependency direction:
- Asset Core -> (ingen dependency paa Fleet/Technical)
- Fleet -> Asset reference
- Technical Configuration -> Fleet reference via vessel_id

Forbudt dependency direction:
- Technical Configuration -> Fleet infrastructure internals
- Technical Configuration -> Asset infrastructure internals
- Fleet -> Technical internals i lockede flows uden ny capability plan

Boundary-konklusion:
- Technical Configuration kan bygges alene via vessel_id-reference og capability boundary contracts.

## Lifecycle
TechnicalConfiguration lifecycle (foreslaet):
- DRAFT
- ACTIVE
- ARCHIVED

TechnicalComponent lifecycle (foreslaet):
- PLANNED
- INSTALLED
- REMOVED
- RETIRED

Lifecycle-regler:
- component kan kun være CURRENT hvis status er INSTALLED og removed_date er None
- REMOVED/RETIRED component bevares historisk
- replacement operation skifter current-markering uden at slette historiske records

## Historical Configuration
Historik maa ikke destrueres ved udskiftning.

Modelkrav:
- original component bevares
- removed component bevares med removed_date og status
- replacement component oprettes som ny identity
- current state udledes af seneste aktive component i replacement chain

Dette understotter historiske fartojsforlob uden datatab.

## Replacement and Component History
Replacement-forlob modelleres eksplicit:
- replaced_component_id -> replacement_component_id
- replaced_on timestamp/date
- reason + notes

Historikfunktioner:
- vis komponentkæde over tid
- spor original komponent
- spor alle efterfolgende replacement-led
- identificer current component uden at overskrive historiske data

Strukturvalidering:
- ingen self-replacement
- ingen cycles i replacement chains
- replacement maa kun pege paa komponent inden for samme TechnicalConfiguration

## Technical Specification
Technical specification modelleres som domænekontrolleret typed struktur, ikke fri JSON/dict.

Foreslaet v1 model:
- TechnicalSpecification (value object) med:
  - schema_key (f.eks. ENGINE_V1, GEARBOX_V1, SHAFT_V1, PROPELLER_V1)
  - typed parameter entries (key, typed value, unit)
  - valideringsregler bundet til schema_key

Eksempler paa schema-specifikke felter:
- Engine:
  - power
  - rpm
  - cylinders
  - fuel_type
- Gearbox:
  - ratio
  - manufacturer
  - model
- Shaft:
  - diameter
  - material
- Propeller:
  - pitch_type (fixed/controllable)
  - diameter
  - blade_count
  - handedness

Evolution uden aggregate-graensebrud:
- senere typed specification value objects kan introduceres per schema
- TechnicalConfiguration aggregate-graensen forbliver uændret
- migration sker i specification mapping/validation lag, ikke via split af aggregate

## Alvur validation scenario
Designet kan repræsentere et fartoj som Alvur SA 98 uden hardcoding:

- Vessel reference:
  - vessel_id = reference til Fleet/Vessel
- Components:
  - PROPULSION_ENGINE: B&W Alpha 342V
  - GEARBOX: reversing arrangement
  - SHAFT
  - PROPELLER: controllable pitch
- ComponentLink chain:
  - Engine -> Gearbox -> Shaft -> Propeller

Konfigurationen beskrives i TechnicalConfiguration aggregate uden ændring af Fleet eller Asset Core.

## Maintenance Boundary
Eksplicit grænse:

Technical Configuration ejer:
- technical component identity
- technical specification
- installation
- removal
- replacement history
- technical configuration structure

Maintenance ejer senere:
- maintenance plans
- work orders
- inspections
- service history
- maintenance intervals

Maintenance implementeres ikke i TECH-000.

## Certificates Boundary
Certificates implementeres ikke i TECH-000.

Regel:
- Technical Configuration maa ikke eje certifikat-lifecycle.
- Certificate relations kan senere refereres via integration contracts, men ikke ejes i dette capability scope.

## Ikke mål
Dette design omfatter ikke:
- Engine som separat capability i Fleet Core
- Maintenance capability
- Certificates capability
- Voyages capability
- telemetri/sensorstreaming
- predictive analytics
- redesign af Asset Core eller Fleet
- nye generiske framework-abstraktioner

Eksplicit afgrænsning:
TECH-000 definerer kun teknisk konfigurationsdomæne omkring vessel_id-reference.

## Design Recommendation
READY FOR DOMAIN IMPLEMENTATION

Begrundelse:
- Designet etablerer klar aggregate-graense omkring TechnicalConfiguration.
- Capability boundary mod Asset/Fleet er tydelig og kan holdes via vessel_id-reference.
- Ingen blocker i Asset Core eller Fleet er nødvendig for opstart af domain-implementering.

## Capability Status (CAP-08 Technical Configuration)

Status: LOCKED

Status pr. 2026-07-11:
- TECH-000: design dokumenteret.
- TECH-001: domain implementeret og testet.
- TECH-002: SQLAlchemy persistence + mapper implementeret og testet.
- TECH-003: repository contract + SQLite repository implementeret og testet.
- TECH-004: application services implementeret og testet.
- TECH-005: feature layer implementeret og testet.
- TECH-006: end-to-end integration workflows implementeret og testet.
- TECH-007: capability review dokumenteret i technical_configuration_capability_review.md med konklusion READY FOR LOCK.

Lock-regler:
- Eksisterende public Technical Configuration API betragtes som stabil.
- Kun fejlrettelser ma ændre låst adfærd uden ny plan.
- Maintenance implementeres som separat capability.
- Certificates implementeres som separat capability.
- Voyages implementeres som separat capability.
- Fleet udvides ikke med technical component ownership.

Kvalitetsgate:
- Fuldt regressionssæt skal være grønt (0 failures, 0 warnings).
- Permanente architecture compliance tests skal være grønne.
- Asset ↔ Fleet ↔ Technical dependency direction og public API boundary ma ikke brydes.
