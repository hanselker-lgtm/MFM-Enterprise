# ASSET-000 Asset Core Design

## Purpose
Asset Core etablerer en generisk domænekerne for registrering, identifikation, klassificering og livscyklusstyring af aktiver.

Målet er at kunne repræsentere ethvert aktiv med en stabil og genbrugelig model, uanset senere domænespecifikke udvidelser.

Asset Core skal:
- understøtte entydig identitet og sporbarhed
- understøtte type- og kategoribaseret klassificering
- understøtte status/livscyklus med validerede overgangsregler
- kunne udvides via metadata uden hard-coded domæneafhængigheder
- eksponere en stabil public API-kontrakt via application services og features

## Bounded Context
Asset Core er et selvstændigt bounded context med fokus på generiske aktivbegreber.

Context ansvar:
- Asset identitet
- Asset klassifikation
- Asset relationer (for eksempel parent-child)
- Asset livscyklus
- Asset registrering af attributter/metadata

Context grænser:
- Asset Core må ikke indeholde domænelogik for specifikke aktivtyper
- Asset Core må ikke kende eller importere senere kapabiliteter

## Aggregates
Primære aggregates i Asset Core:

- Asset
  - root: Asset
  - ansvar: samlet konsistens for identitet, klassifikation, status og metadata
  - invariants:
    - asset_id er entydig
    - asset_code er entydig inden for defineret scope
    - statusovergange følger tilladt transition-matrix
    - krævede kernefelter er til stede

- AssetType
  - root: AssetType
  - ansvar: klassifikationsdefinitioner
  - invariants:
    - type_code er entydig
    - navn/label er gyldigt
    - type kan markeres aktiv/inaktiv uden at bryde historik

- AssetRelation
  - root: AssetRelation (eller relationer indlejret i Asset, afhængigt af implementeringsvalg)
  - ansvar: strukturel relation mellem aktiver
  - invariants:
    - relationstype skal være gyldig
    - ingen ulovlige cykler for relationstyper med acyclic-krav

## Value Objects
Asset Core value objects skal være immutable.

Foreslåede value objects:
- AssetId
- AssetCode
- AssetTypeCode
- AssetName
- AssetStatus
- AssetCategory
- AssetTag
- AttributeKey
- AttributeValue
- ValidityPeriod
- RelationType

Regel:
- Value objects repræsenterer validerede begreber uden identitet og må ikke kunne muteres efter oprettelse.

## Entities
Foreslåede entities:
- Asset
- AssetType
- AssetAttribute (hvis ikke modeleret som map/value object)
- AssetRelation
- AssetLifecycleEntry (historik)

Entity-principper:
- Entities bærer identitet og historik
- Mutation sker kun gennem aggregate root-operationer
- Konsistensregler håndhæves i domænelaget

## Repositories
Repository contracts (interfaces) i application boundary:
- AssetRepository
  - add, get_by_id, update, delete, exists, list, search
- AssetTypeRepository
  - add, get_by_code, update, exists, list, search
- AssetRelationRepository (hvis særskilt aggregate)
  - add, list_for_asset, remove

UnitOfWork:
- Alle write-operationer udføres i en explicit UnitOfWork
- Commit/rollback defineres centralt i UnitOfWork-kontrakten

Regel:
- Repositories eksponerer domæneobjekter/DTO mapping contracts, ikke persistence-modeller.

## Events
Domæne- og applikationsevents for løst koblet orchestration:

- AssetRegisteredEvent
- AssetUpdatedEvent
- AssetStatusChangedEvent
- AssetTypeDefinedEvent
- AssetRelationAddedEvent
- AssetRelationRemovedEvent
- AssetArchivedEvent

Event-principper:
- Events er immutable payloads
- Events publiceres efter succesfuld commit
- Event-navne er business-orienterede og versionsstabile

## Application Services
Application services (use cases) orkestrerer domæneoperationer:

- RegisterAssetUseCase
- UpdateAssetUseCase
- ChangeAssetStatusUseCase
- DefineAssetTypeUseCase
- LinkAssetsUseCase
- UnlinkAssetsUseCase
- ArchiveAssetUseCase
- GetAssetQueryUseCase
- SearchAssetsQueryUseCase

Principper:
- Request DTO immutable
- Response DTO immutable
- Validation, business rule checks, UnitOfWork og event dispatch i ét konsistent flow

## Features
Feature layer eksponerer public entry points:

- RegisterAssetFeature
- UpdateAssetFeature
- ChangeAssetStatusFeature
- DefineAssetTypeFeature
- LinkAssetsFeature
- UnlinkAssetsFeature
- ArchiveAssetFeature
- GetAssetFeature
- SearchAssetsFeature

Feature-principper:
- Standard signatur: execute(request)
- Returnerer kun response DTO'er
- Må ikke returnere domain entities direkte
- Standardiseret exception mapping

## Public API
Public API for Asset Core følger samme standard som øvrige capability features:

- Input: immutable Request DTO
- Output: immutable Response DTO
- Fejltyper:
  - ApplicationException
  - ValidationException
  - BusinessRuleViolation
  - RepositoryException

Kontraktskrav:
- API må være stabil på tværs af persistence-implementeringer
- API må ikke eksponere interne ORM/persistence detaljer

## Integration Points
Asset Core integrerer via kontrakter, ikke direkte domænekendskab:

- Event bus / dispatcher for domæneevents
- Repository interfaces for persistence adapters
- Feature API for GUI og eksterne applikationsflows
- Query API for søgning/rapportering

Vigtige integrationsregler:
- Ingen direkte afhængighed til specifikke asset-underdomæner
- Udvidelser sker via typekoder, metadata og relationer
- Nye capability modules kobles via events og application boundary

## Ikke mål
Dette design omfatter ikke:
- Vessel-model
- Engine-model
- Equipment-model
- Maintenance-model
- domænespecifik vedligeholdelsesplanlægning
- sensor/telemetri integration
- reservedelslogik
- operationelle workflows for konkrete aktivtyper

Eksplicit afgrænsning:
Asset Core skal være generisk og må ikke kende Vessel, Engine, Equipment eller Maintenance. Disse capability områder designes senere som separate moduler oven på Asset Core.
