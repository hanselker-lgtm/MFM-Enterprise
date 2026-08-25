# API Inventory

## Summary

Features: 5

Compliant: 0

Partial: 1

Non-compliant: 7

## Scope

Gennemgået:

- src/mfm/application/features/
- src/mfm/application/services/
- src/mfm/application/workflows/
- src/mfm/application/queries/

Bemærk:

- Der findes ingen filer under `src/mfm/application/services/`.
- Der findes ingen filer under `src/mfm/application/queries/`.

Statusvurdering er baseret på den officielle standard i `docs/architecture/public_api_standard.md`.

## Inventory

| Name | Responsibility | Request DTO | Response DTO | Exceptions | Return Type | Status |
|---|---|---|---|---|---|---|
| MemberEnrollmentFeature | Orkestrerer oprettelse af contact/member/membership/invoice/journal | EnrollmentRequest (mutable; indeholder Domain Objects) | EnrollmentResult (mutable) | DuplicateMemberNumberError, NoActiveContingentPlanError | EnrollmentResult | NON_COMPLIANT |
| AnnualContingentGenerationFeature | Genererer årlige contingent-fakturaer og journal drafts | AnnualContingentRequest (mutable; indeholder Domain Object MembershipType) | AnnualContingentResult (mutable) | ValueError via repositories/fiscal checks (ingen standard application exceptions) | AnnualContingentResult | NON_COMPLIANT |
| GeneralLedgerService | Genererer hovedbogsvisning fra posteringer | GeneralLedgerRequest (mutable) | GeneralLedgerDTO (mutable; indeholder Domain Value Object Money) | Ingen standardiseret ApplicationException-hierarki | list[GeneralLedgerDTO] | NON_COMPLIANT |
| AccountsReceivableService | Aggregere debitoroversigt, overdue og aging | Ingen Request DTO (kun `as_of_date` parameter) | AccountsReceivableSummary (mutable; indeholder Domain Value Objects Money/AgingBucket) | ValueError opsamles i errors; ingen standard application exceptions | AccountsReceivableSummary | NON_COMPLIANT |
| OpenItemsService | Returnerer åbne poster med dynamisk saldo og overdue-info | OpenItemsRequest (mutable) | OpenItemsDTO (mutable; indeholder Domain Value Object Money) | ValueError ignoreres internt; ingen standard application exceptions | list[OpenItemsDTO] | NON_COMPLIANT |
| AnnualContingentWorkflow | Workflow-orchestration for årlig fakturering | Ingen request DTO (run_date parameter) | SummaryDTO (mutable) | ValueError via repositories/fiscal checks | SummaryDTO | PARTIALLY_COMPLIANT |
| EnrollMemberWorkflow | Workflow-orchestration for enrollment inkl. rollback | EnrollMemberWorkflowInput (mutable; indeholder Domain Objects) | EnrollMemberWorkflowResult (mutable; returnerer Domain Objects) | DuplicateMemberNumberError, NoActiveContingentPlanError | EnrollMemberWorkflowResult | NON_COMPLIANT |
| RegisterPaymentWorkflow | Workflow-orchestration for betaling, journal og event | RegisterPaymentWorkflowInput (mutable; bruger Domain Value Object Money) | RegisterPaymentWorkflowResult (mutable; returnerer Domain Objects) | ValueError for not found/duplicate reference | RegisterPaymentWorkflowResult | NON_COMPLIANT |

## Findings

1. Ingen klassificerede API-klasser er fuldt COMPLIANT med standarden.
2. Hovedårsager til NON_COMPLIANT:
- DTO'er er mutable (`@dataclass(slots=True)` fremfor frozen).
- Domain Objects lækkes i request/response eller indlejrede typer.
- Manglende standardiseret exception-hierarki (`ApplicationException`, `ValidationException`, `BusinessRuleViolation`, `RepositoryException`).
- Uens public metode-navngivning (`execute`, `generate`, `summarize`, `list_open_items`).
3. Workflows opfører sig som interne orkestratorer, men er stadig offentlige klasser uden fælles API-standard.

## Standardisering (anbefalet)

1. Feature entry points standardiseres til:
- `execute(request)` -> immutable response DTO
2. Alle Request/Response DTO'er gøres immutable:
- `@dataclass(frozen=True, slots=True)`
3. Domain Objects fjernes fra public API-kontrakter:
- map til primitive felter eller dedikerede transport-DTO'er
4. Exception-model standardiseres:
- `ApplicationException`
- `ValidationException`
- `BusinessRuleViolation`
- `RepositoryException`
5. Naming harmoniseres:
- `<Create>Feature`
- `<Update>Feature`
- `<Delete>Feature`
- `<Get>Feature`
- `<List>Feature`
