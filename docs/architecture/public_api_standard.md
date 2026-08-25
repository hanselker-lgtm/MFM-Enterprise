# Public API Standard

## Formål

Dette dokument definerer projektets officielle standard for offentlige API'er i application-laget.

Standarden gælder for:

- Features
- Services med offentlig API-kontrakt
- Workflows hvis de eksponeres offentligt
- Query-orienterede application entry points

Målet er en ensartet, stabil og transport-sikker public API, som ikke lækker domæne- eller persistence-detaljer.

## Grundprincipper

1. Public API'er må ikke eksponere Domain Objects direkte.
2. Public API'er må ikke eksponere SQLAlchemy-typer eller persistence-modeller.
3. Requests og responses skal være simple, immutable og forudsigelige.
4. Validering skal være tydelig og konsistent.
5. Exceptions skal følge en fælles application-hierarki.
6. Naming skal være ens på tværs af alle offentlige features.

## Request DTO

### Krav

En Request DTO skal:

- være en immutable dataclass
- bruge `@dataclass(frozen=True, slots=True)`
- kun indeholde primitive typer, enums, andre DTO'er eller simple collections af disse
- ikke indeholde Domain Objects
- ikke indeholde SQLAlchemy-modeller, sessions eller ORM-referencer

### Tilladte typer

Tilladte felttyper i Request DTO'er:

- `str`
- `int`
- `float` når det er fagligt nødvendigt
- `bool`
- `date`
- `datetime`
- `UUID`
- `Decimal`
- enums
- andre immutable DTO'er
- `list`, `tuple`, `set`, `dict` kun når indholdet består af primitive typer eller DTO'er

### Forbudt

En Request DTO må ikke indeholde:

- domæneaggregater
- domæneentiteter
- value objects fra domain-laget
- repository-instanser
- SQLAlchemy sessions
- SQLAlchemy ORM models
- andre infrastructure-afhængigheder

### Validering

Hvis validering er nødvendig, skal DTO'en selv tilbyde den gennem en `validate()` metode.

Regel:

- simpel strukturel validering kan ligge i `__post_init__`
- udvidet eller eksplicit validering skal ligge i `validate()`

Eksempler på validering:

- obligatoriske felter
- tomme strenge
- ugyldige dato-intervaller
- negative beløb
- ugyldige filterkombinationer

### Anbefalet mønster

```python
from dataclasses import dataclass
from datetime import date
from uuid import UUID

@dataclass(frozen=True, slots=True)
class GetMemberRequest:
    member_id: UUID
    as_of_date: date | None = None

    def validate(self) -> None:
        if self.as_of_date is not None and self.as_of_date.year < 2000:
            raise ValidationException("as_of_date is out of allowed range")
```

## Response DTO

### Krav

En Response DTO skal:

- være en immutable dataclass
- bruge `@dataclass(frozen=True, slots=True)`
- ikke returnere Domain Objects
- ikke returnere SQLAlchemy-typer
- kun bestå af primitive typer eller andre DTO'er

### Tilladte typer

En Response DTO må indeholde:

- primitive typer
- `UUID`, `date`, `datetime`, `Decimal`, enums
- lister af andre response DTO'er
- nested DTO-strukturer

### Forbudt

En Response DTO må ikke indeholde:

- aggregates
- entities
- value objects fra domain-laget
- repositories
- ORM models
- sessions
- lazy-loaded persistence-objekter

### Struktur

Responses skal være flade eller bevidst komponerede.

Regler:

- command-orienterede features returnerer én response DTO
- list/get features returnerer DTO'er eller lister af DTO'er
- fejltilstande signaleres via exceptions, ikke blandede success/error payloads, medmindre en eksplicit batch-kontrakt kræver det

### Anbefalet mønster

```python
from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from uuid import UUID

@dataclass(frozen=True, slots=True)
class MemberSummaryDTO:
    member_id: UUID
    member_number: str
    join_date: date
    outstanding_balance: Decimal
```

## Feature Standard

### Definition

En Feature er projektets officielle offentlige application entry point for en use case.

### Public metode

Alle Features skal eksponere præcis én offentlig metode med denne signatur:

- `execute(request)`
- returnerer en Response DTO

### Kontrakt

Feature-kontrakten er:

1. modtag `request`
2. validér `request` hvis nødvendigt
3. udfør application orchestration
4. returnér `response`

### Standardform

```python
class GetMemberFeature:
    def execute(self, request: GetMemberRequest) -> GetMemberResponse:
        request.validate()
        ...
        return response
```

### Return type

Features skal returnere:

- én immutable Response DTO
- eller en liste af immutable DTO'er hvis featuretypen er en listefunktion

Features må ikke returnere:

- domain entities
- aggregates
- repositories
- raw tuples/dicts som primær public kontrakt

## Exceptions

Alle offentlige application API'er skal anvende følgende exception-hierarki.

### Base exceptions

```python
class ApplicationException(Exception):
    pass

class ValidationException(ApplicationException):
    pass

class BusinessRuleViolation(ApplicationException):
    pass

class RepositoryException(ApplicationException):
    pass
```

### Betydning

- `ApplicationException`: fælles base for alle application-fejl
- `ValidationException`: ugyldig request eller inputformat
- `BusinessRuleViolation`: forretningsregel eller use-case regel blokerer handlingen
- `RepositoryException`: persistence- eller repository-fejl, der skal oversættes til application-laget

### Regler

1. Public API'er må ikke lække tilfældige `ValueError` eller `TypeError` som en del af den officielle kontrakt.
2. Domain exceptions skal oversættes ved application-boundary når de bliver en del af public API.
3. Infrastructure/persistence exceptions skal oversættes til `RepositoryException`.

## Naming

### Feature naming

Alle Features skal følge dette mønster:

- `<Create>Feature`
- `<Update>Feature`
- `<Delete>Feature`
- `<Get>Feature`
- `<List>Feature`

### Eksempler

- `CreateMemberFeature`
- `UpdateMemberFeature`
- `DeleteMemberFeature`
- `GetMemberFeature`
- `ListMembersFeature`

### DTO naming

Requests:

- `<Action><Target>Request`

Responses:

- `<Action><Target>Response`
- `<Target>DTO` for read-models når det er mere naturligt

Eksempler:

- `CreateMemberRequest`
- `CreateMemberResponse`
- `GetMemberRequest`
- `MemberDTO`
- `ListMembersResponse`

### Konsistensregler

1. Brug samme verb i Feature, Request og Response.
2. Undgå blanding af `Result`, `DTO`, `Summary`, `Output` uden en bevidst regel.
3. Hvis API'et er et command, foretræk `Response`.
4. Hvis API'et er et read-model view, foretræk `DTO`.

## Domain Boundary Rules

Public API'er i application-laget må ikke:

- kræve domain aggregates som request-objekter
- returnere domain aggregates som response-objekter
- eksponere value objects direkte
- eksponere ORM-modeller direkte

Mapping mellem domain og DTO skal ske inde i feature/service-laget.

## SQLAlchemy Boundary Rules

SQLAlchemy må ikke optræde i den offentlige kontrakt.

Forbudt i public API:

- `Session`
- ORM models
- query objects
- lazy relations
- ORM exceptions uden oversættelse

Tilladt:

- intern brug i repository/infrastructure-laget
- oversættelse til application exceptions ved boundary

## Standardisering af collections

Hvis en response returnerer flere elementer, anbefales en wrapper-response når metadata er nødvendig.

Eksempel:

```python
@dataclass(frozen=True, slots=True)
class ListMembersResponse:
    items: tuple[MemberDTO, ...]
    total_count: int
```

Hvis ingen metadata er nødvendig, kan en feature returnere en liste eller tuple af DTO'er, men immutable collections foretrækkes.

## Migration Guidance

Eksisterende offentlige API'er bør gradvist standardiseres i denne rækkefølge:

1. indfør fælles application exceptions
2. gør request/response DTO'er immutable
3. fjern domain objects fra public responses
4. standardisér feature naming
5. standardisér `execute(request) -> response`

## Summary

Projektets officielle standard er:

1. Request DTO: immutable, ingen Domain Objects, ingen SQLAlchemy, `validate()` hvis nødvendig
2. Response DTO: immutable, ingen Domain Objects, kun primitive typer eller DTO'er
3. Feature API: `execute(request)` returnerer response
4. Exceptions: `ApplicationException`, `ValidationException`, `BusinessRuleViolation`, `RepositoryException`
5. Naming: `<Create>Feature`, `<Update>Feature`, `<Delete>Feature`, `<Get>Feature`, `<List>Feature`
