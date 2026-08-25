# Cross Capability Reference Contract

Status: Draft
Contract ID: CCRC-001
Scope: Capability-neutral public reference validation contract

## Purpose
Define one public contract for safe, capability-neutral reference checks between bounded contexts.

The contract is used when one aggregate stores or validates a reference to another aggregate owned by a different capability.

The contract is design-only and infrastructure-agnostic.

## Responsibility
The contract is responsible for:
- reference existence validation
- authorization check for caller and operation intent
- target capability identification
- target aggregate identifier validation
- target aggregate type identification
- soft-deleted detection
- archived detection

The contract is not responsible for:
- loading target aggregate data
- exposing persistence models
- exposing SQLAlchemy sessions, models, or query objects
- exposing repositories
- performing cross-capability state mutation

## Public Interface

### Request Model
CrossCapabilityReferenceCheckRequest
- contract_version: string
- caller_capability: string
- caller_operation: string
- target_capability: string
- target_aggregate_type: string
- target_aggregate_id: string
- authorization_context: map of string to primitive value
- as_of_utc: datetime

Rules:
- target_capability is mandatory and must be one known capability key.
- target_aggregate_type is mandatory and scoped by target_capability.
- target_aggregate_id is mandatory and must be canonical identifier format for that aggregate.
- authorization_context must contain only transport-safe values.

### Response Model
CrossCapabilityReferenceCheckResponse
- contract_version: string
- reference_status: enum
- target_capability: string
- target_aggregate_type: string
- target_aggregate_id: string
- exists: boolean
- authorized: boolean
- is_soft_deleted: boolean
- is_archived: boolean
- validated_at_utc: datetime
- errors: list of ReferenceContractError

Reference status enum values:
- VALID
- INVALID_NOT_FOUND
- INVALID_UNAUTHORIZED
- INVALID_SOFT_DELETED
- INVALID_ARCHIVED
- INVALID_TYPE_MISMATCH
- INVALID_CAPABILITY_MISMATCH
- INVALID_REQUEST
- INDETERMINATE

### Public Operation
check_reference(request) -> response

Semantics:
- Pure validation contract.
- No persistence type leakage.
- No aggregate payload return.
- Deterministic result for the same request and evaluation point.

## Error Model
Errors are returned as structured contract errors.

ReferenceContractError
- code: string
- category: enum
- message: string
- field: optional string
- retryable: boolean

Error categories:
- VALIDATION
- AUTHORIZATION
- NOT_FOUND
- STATE
- COMPATIBILITY
- POLICY
- TRANSIENT

Required standard error codes:
- CCRC-VAL-001 INVALID_TARGET_CAPABILITY
- CCRC-VAL-002 INVALID_TARGET_AGGREGATE_TYPE
- CCRC-VAL-003 INVALID_TARGET_AGGREGATE_ID
- CCRC-AUT-001 UNAUTHORIZED_REFERENCE
- CCRC-NFD-001 TARGET_NOT_FOUND
- CCRC-STA-001 TARGET_SOFT_DELETED
- CCRC-STA-002 TARGET_ARCHIVED
- CCRC-CMP-001 CONTRACT_VERSION_UNSUPPORTED
- CCRC-TRN-001 VALIDATION_BACKEND_UNAVAILABLE

Behavioral rules:
- INVALID_REQUEST is used when mandatory request fields are invalid.
- INDETERMINATE is used only when validation cannot complete due to transient or policy-gated conditions.
- Multiple errors may be returned, but primary failure reason must appear first.

## Versioning Strategy
Versioning policy:
- Semantic versioning for the contract: MAJOR.MINOR.PATCH.
- Initial release: 1.0.0.

Compatibility rules:
- PATCH: wording and clarifications only, no field or semantic change.
- MINOR: additive fields and additive enum values, backward compatible.
- MAJOR: breaking changes to required fields, semantics, or error behavior.

Negotiation rules:
- request includes contract_version.
- provider returns evaluated contract_version.
- unsupported major versions return CCRC-CMP-001.

Deprecation policy:
- at least one full capability cycle overlap for deprecated MINOR versions.
- deprecation notice must include migration mapping.

## Future Extension Rules
Extensions must preserve capability neutrality.

Allowed extensions:
- additive request metadata fields
- additive response diagnostics fields
- additive reference status enum values
- additive authorization dimensions
- additive policy signals

Forbidden extensions:
- returning persistence entities or ORM details
- embedding repository contracts
- embedding SQL text or query primitives
- capability-specific branching inside base contract names
- mutable side-effect operations in check_reference

Extension governance:
- all extensions require architecture review note in docs/architecture.
- each new enum or field must include backward compatibility notes.
- capability-specific needs must be introduced through optional extension sections, never by breaking base fields.

## Security and Privacy Constraints
- Contract must not expose confidential target aggregate payload.
- Authorization result may be returned as boolean plus coded reason only.
- No personal data fields are required in the base contract.
- Logging must avoid sensitive authorization context values by default.

## Non Goals
- Cross-capability transactional orchestration
- Domain event dispatching
- Bulk synchronization
- Replication of foreign aggregate state

## Example Capability Keys
- ORGANIZATION
- PROJECTS
- MAINTENANCE
- INVENTORY
- PROCUREMENT
- CERTIFICATES
- DOCUMENTS

Example keys are illustrative and can be extended through roadmap governance.