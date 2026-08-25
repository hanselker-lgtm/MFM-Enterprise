# EA-IMETA-PC-RG-408

## LEGACY-TO-ACTIVE REQUIREMENT TRACEABILITY MATRIX

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-408 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Requirement Traceability & Consolidation Control |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-407 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Preserve requirements while consolidating legacy PC-RG artifacts into the active baseline |
| Evidence Boundary | Legacy content must be sourced before final disposition |

---

# 2. Purpose

EA-IMETA-PC-RG-408 defines the controlled method for tracing requirements from the legacy PC-RG document population into the active architecture defined by EA-IMETA-PC-RG-407.

Its purpose is to prevent two opposite errors:

```text
DUPLICATION
```

where the same requirement is implemented repeatedly,

and:

```text
REQUIREMENT LOSS
```

where consolidation removes a requirement that was actually necessary.

The governing principle is:

> **Consolidate documents, not requirements.**

---

# 3. Scope

The matrix covers:

```text
EA-IMETA-PC-RG-001
        ↓
        …
        ↓
EA-IMETA-PC-RG-404
```

and maps requirements into the nine active responsibilities:

```text
VAL
VER
ACC
CLO
MON
REG
REM
RVA
RAC
```

Cross-cutting requirements may additionally map to:

```text
AUTHORITY
EVIDENCE
AUDIT
SECURITY
COMPLIANCE
RISK
ACCOUNTABILITY
TRACEABILITY
```

---

# 4. Evidence Rule

No legacy requirement SHALL be inferred from a filename alone.

The minimum evidence for a requirement mapping is:

```text
SOURCE FILE
+
SOURCE SECTION
+
SOURCE TEXT / REQUIREMENT
+
INTERPRETATION
+
TARGET RESPONSIBILITY
+
TARGET CONTROL / BEHAVIOUR
```

Where source content is unavailable:

```text
STATUS = SOURCE REQUIRED
```

This status SHALL NOT be converted into an assumed mapping.

---

# 5. Requirement Identity

Every extracted requirement SHALL receive a stable identifier.

Recommended form:

```text
PC-RG-LEG-<FILE>-<SECTION>-<SEQ>
```

Example:

```text
PC-RG-LEG-042-07-003
```

The identifier SHALL remain stable even if the requirement is later merged into another active document.

---

# 6. Requirement Record

| Attribute | Required |
|---|---|
| Requirement ID | Yes |
| Source File | Yes |
| Source Section | Yes |
| Source Text | Yes |
| Requirement Type | Yes |
| Interpretation | Yes |
| Canonical Responsibility | Yes |
| Cross-Cutting Capability | Where applicable |
| Target Control | Yes |
| Target Data Object | Where applicable |
| Target State | Where applicable |
| Target Decision | Where applicable |
| MFM Impact | Yes |
| Disposition | Yes |
| Rationale | Yes |
| Verification Method | Yes |
| Evidence Requirement | Yes |
| Status | Yes |

---

# 7. Requirement Types

Each requirement SHALL be classified.

```text
FUNCTIONAL
CONTROL
DATA
WORKFLOW
AUTHORITY
SECURITY
COMPLIANCE
AUDIT
REPORTING
INTEGRATION
UI
OPERATIONAL
PERFORMANCE
RESILIENCE
DOCUMENTATION
```

A requirement may have more than one secondary classification but SHALL have one primary type.

---

# 8. Requirement Strength

Source requirements SHALL retain their normative strength.

```text
SHALL
MUST
REQUIRED
SHOULD
MAY
INFORMATIVE
```

The consolidation process SHALL not weaken a mandatory requirement into a recommendation without an explicit architectural decision.

---

# 9. Requirement Interpretation

Every requirement SHALL be decomposed into:

```text
ACTOR
+
ACTION
+
OBJECT
+
CONDITION
+
CRITERIA
+
RESULT
```

Example:

```text
"An authorised reviewer SHALL approve the closure
when all mandatory evidence is present."

ACTOR      = authorised reviewer
ACTION     = approve
OBJECT     = closure
CONDITION  = mandatory evidence present
RESULT     = closure approved
```

This decomposition makes duplicate detection possible.

---

# 10. Canonical Mapping

Requirements SHALL map to one primary responsibility.

| Code | Responsibility |
|---|---|
| VAL | Validation |
| VER | Verification |
| ACC | Acceptance |
| CLO | Closure |
| MON | Monitoring |
| REG | Regression |
| REM | Remediation |
| RVA | Revalidation |
| RAC | Reacceptance |

Cross-cutting requirements may additionally be tagged.

---

# 11. Mapping Decision

Each requirement SHALL receive one primary disposition:

```text
DIRECT MAP
MERGED
GENERALIZED
REPLACED
SUPERSEDED
REFERENCE ONLY
HISTORICAL
DUPLICATE
SOURCE REQUIRED
```

### DIRECT MAP

Requirement maps directly to one active control or behaviour.

### MERGED

Equivalent requirements are consolidated into one stronger requirement.

### GENERALIZED

Several specific requirements are represented by a common architectural rule.

### REPLACED

The old requirement is replaced by a newer requirement with equivalent or stronger intent.

### SUPERSEDED

A formally approved architecture decision removes the requirement.

### REFERENCE ONLY

The requirement remains useful as explanatory or historical context.

### HISTORICAL

No current requirement remains, but the record is retained.

### DUPLICATE

The requirement is materially identical to another requirement.

### SOURCE REQUIRED

The actual source content has not yet been obtained.

---

# 12. Duplicate Requirement Test

Two requirements are duplicate candidates when they have substantially the same:

```text
ACTOR
+
ACTION
+
OBJECT
+
CONDITION
+
RESULT
```

Differences in terminology SHALL NOT automatically create separate requirements.

Example:

```text
"validate"
"perform validation"
"confirm validity"
"establish validity"
```

may represent the same underlying requirement.

---

# 13. Conflict Detection

Requirements SHALL also be checked for contradiction.

```text
REQUIREMENT A
    ↓
"SHALL"

REQUIREMENT B
    ↓
"MAY NOT"

SAME OBJECT?
    ↓
CONFLICT
```

Conflicting requirements SHALL be escalated for architectural resolution.

They SHALL not be silently merged.

---

# 14. Requirement Lifecycle

```text
EXTRACTED
   ↓
CLASSIFIED
   ↓
MAPPED
   ↓
REVIEWED
   ↓
ACCEPTED INTO BASELINE
   ↓
IMPLEMENTED
   ↓
TESTED
   ↓
VERIFIED
```

Possible exception states:

```text
REJECTED
DUPLICATE
SUPERSEDED
SOURCE REQUIRED
CONFLICTING
DEFERRED
```

---

# 15. Traceability Chain

Every active requirement SHALL be traceable:

```text
LEGACY SOURCE
     ↓
REQUIREMENT ID
     ↓
CANONICAL RESPONSIBILITY
     ↓
CONTROL / BEHAVIOUR
     ↓
DATA / STATE
     ↓
IMPLEMENTATION
     ↓
TEST
     ↓
EVIDENCE
     ↓
DECISION
```

This chain is the core assurance mechanism of the consolidation.

---

# 16. Backward Traceability

Every active requirement SHALL be traceable back to its source or an approved architectural decision.

```text
ACTIVE REQUIREMENT
       ↓
WHY DOES IT EXIST?
       ↓
SOURCE / DECISION
```

If no source or approved architectural rationale exists:

```text
ORIGIN UNKNOWN
```

The requirement SHALL be reviewed before being treated as authoritative.

---

# 17. Forward Traceability

Every retained legacy requirement SHALL have a forward destination.

```text
LEGACY REQUIREMENT
       ↓
ACTIVE RESPONSIBILITY
       ↓
CONTROL / BEHAVIOUR
       ↓
TEST
```

No retained requirement may disappear during consolidation.

---

# 18. State Traceability

Requirements affecting lifecycle state SHALL identify:

```text
Previous State
Trigger
Rule
Decision
New State
Authority
```

Example:

```text
VALIDATED
    ↓
verification performed
    ↓
criteria satisfied
    ↓
authorised verifier
    ↓
VERIFIED
```

---

# 19. Decision Traceability

Requirements affecting decisions SHALL identify:

```text
Decision
Decision Authority
Decision Criteria
Evidence
Decision Record
Resulting State
```

This prevents decision logic from being hidden in narrative documents.

---

# 20. Control Traceability

Controls SHALL be linked to requirements.

```text
Requirement
    ↓
Control Objective
    ↓
Control
    ↓
Execution
    ↓
Evidence
    ↓
Test
```

A control without a requirement SHALL be classified as:

```text
ARCHITECTURAL CONTROL
```

and must have an explicit rationale.

---

# 21. Data Traceability

Requirements that create or modify data SHALL identify:

```text
Data Object
Field
Source
Owner
Lifecycle
Retention
Security Classification
Audit Requirement
```

Primary PC-RG data objects include:

```text
Case
Baseline
Criteria
Evidence
Validation
Verification
Acceptance
Closure
Monitoring Record
Regression Finding
Remediation
Revalidation
Reacceptance
Decision
Condition
Audit Event
```

---

# 22. MFM Traceability

Every implementation-relevant requirement SHALL map to one or more MFM layers:

```text
DATABASE
SERVICE
WORKFLOW
PERMISSION
UI
REPORT
AUDIT
INTEGRATION
TEST
```

Example:

```text
"Only authorised users may approve acceptance."

DATABASE → approval record
SERVICE  → permission check
UI       → approval action
AUDIT    → approval event
TEST     → authorised / unauthorised cases
```

---

# 23. Test Traceability

Every mandatory requirement SHALL have an objective test method.

```text
REQUIREMENT
    ↓
TEST CASE
    ↓
EXPECTED RESULT
    ↓
ACTUAL RESULT
    ↓
PASS / FAIL
    ↓
EVIDENCE
```

Requirements that cannot be objectively tested SHALL be reviewed for ambiguity.

---

# 24. Requirement Quality Tests

Each requirement SHALL be assessed for:

- necessity;
- clarity;
- consistency;
- feasibility;
- testability;
- traceability;
- ownership;
- authority;
- implementation impact.

A requirement failing one or more critical tests SHALL be flagged.

---

# 25. Matrix Structure

The master matrix SHALL use:

| Requirement ID | Source | Section | Requirement | Type | Strength | Responsibility | Control | State | Decision | MFM Layer | Test | Disposition | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PC-RG-LEG-001-… | RG-001 | TBD | SOURCE REQUIRED | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | SOURCE REQUIRED | OPEN |
| PC-RG-LEG-002-… | RG-002 | TBD | SOURCE REQUIRED | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | SOURCE REQUIRED | OPEN |
| … | … | … | … | … | … | … | … | … | … | … | … | … | … |
| PC-RG-LEG-404-… | RG-404 | TBD | SOURCE REQUIRED | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | SOURCE REQUIRED | OPEN |

---

# 26. Source Acquisition Rule

The matrix SHALL be populated only from actual source material.

Acceptable sources include:

```text
Markdown
DOCX
PDF
TXT
Repository files
Approved architecture records
Approved change records
```

A filename, summary or previous assistant response SHALL not be treated as equivalent to the source document unless formally accepted as the authoritative source.

---

# 27. Legacy Document Batch Processing

When source files become available, they SHOULD be processed in controlled batches.

Recommended sequence:

```text
BATCH 001
RG-001 → RG-025

BATCH 002
RG-026 → RG-050

...

BATCH N
remaining artifacts
```

Each batch SHALL produce:

```text
Extracted Requirements
Duplicate Candidates
Conflicts
Canonical Mapping
Disposition
Traceability Gaps
```

---

# 28. Consolidation Gate

A legacy artifact may be removed from the active baseline only when:

```text
SOURCE REVIEW COMPLETE
+
REQUIREMENTS EXTRACTED
+
REQUIREMENTS MAPPED
+
DUPLICATES IDENTIFIED
+
CONFLICTS RESOLVED
+
IMPLEMENTATION IMPACT ASSESSED
+
TRACEABILITY PRESERVED
```

Only then may:

```text
MERGE
SUPERSEDE
ARCHIVE
```

be approved.

---

# 29. Requirement Loss Prevention

Before approving consolidation, the system SHALL calculate:

```text
LEGACY REQUIREMENTS
        ↓
MAPPED REQUIREMENTS
        ↓
UNMAPPED REQUIREMENTS
```

Target:

```text
UNMAPPED = 0
```

unless each exception is explicitly approved as:

```text
SUPERSEDED
HISTORICAL
REFERENCE ONLY
```

---

# 30. Duplicate Reduction

The target is not to preserve the number of legacy requirements.

The target is:

```text
MAXIMUM REQUIREMENT COVERAGE
+
MINIMUM DUPLICATION
+
FULL TRACEABILITY
```

A successful consolidation may therefore produce:

```text
404 DOCUMENTS
        ↓
FEWER ACTIVE DOCUMENTS
        ↓
SAME OR GREATER REQUIREMENT COVERAGE
```

This is a desired outcome, not a defect.

---

# 31. Conflict Resolution

Where requirements conflict, resolution SHALL consider:

1. authority;
2. recency;
3. scope;
4. normative strength;
5. risk;
6. legal/compliance obligations;
7. approved architecture;
8. implementation impact.

The result SHALL be documented as an architectural decision.

---

# 32. Requirement Change Control

Once accepted into the active baseline, a requirement SHALL have:

```text
Version
Owner
Change Reason
Approver
Effective Date
Previous Version
Impact Assessment
Test Impact
Traceability
```

---

# 33. Requirement Metrics

The consolidation process SHALL report at least:

```text
Total Source Files
Files Reviewed
Files Pending
Requirements Extracted
Requirements Mapped
Requirements Unmapped
Duplicate Requirements
Conflicting Requirements
Superseded Requirements
Historical Requirements
Active Requirements
Test Coverage
Traceability Coverage
```

---

# 34. Quality Thresholds

Recommended minimum thresholds:

```text
Requirement Mapping Coverage       = 100%
Critical Requirement Traceability = 100%
Mandatory Requirement Testability  = 100%
Unresolved Critical Conflicts      = 0
Unknown Active Requirement Origin  = 0
```

Lower values require documented exception approval.

---

# 35. Audit Requirements

All consolidation decisions SHALL be auditable.

Audit events SHALL include:

```text
Requirement ID
Reviewer
Action
Previous Disposition
New Disposition
Reason
Evidence
Timestamp
Approval
```

---

# 36. AI-Assisted Extraction

AI may assist with:

```text
Requirement Candidate Extraction
Duplicate Detection
Classification
Traceability Suggestions
Conflict Detection
```

AI SHALL NOT independently approve:

```text
Requirement Deletion
Requirement Supersession
Critical Conflict Resolution
Active Baseline Acceptance
```

Human authority remains required for material architectural decisions.

---

# 37. AI Extraction Control

AI-assisted extraction SHALL preserve:

```text
Source Reference
Original Text
AI Interpretation
Confidence
Reviewer
Reviewer Decision
Final Requirement
```

The original source text SHALL remain recoverable.

---

# 38. Consolidation Dashboard

The eventual MFM dashboard SHOULD provide:

```text
┌──────────────────────────────────────┐
│ PC-RG CONSOLIDATION STATUS           │
├──────────────────────────────────────┤
│ Source Files            404          │
│ Reviewed                XXX          │
│ Pending                 XXX          │
│ Requirements            XXXX         │
│ Mapped                  XXXX         │
│ Unmapped                XX           │
│ Duplicates              XXX          │
│ Conflicts               X            │
│ Traceability            XX%          │
│ Test Coverage           XX%          │
└──────────────────────────────────────┘
```

Numbers SHALL be calculated from actual matrix data.

---

# 39. Definition of Done

EA-IMETA-PC-RG-408 is operationally complete when:

- all available legacy source files have been indexed;
- requirements have stable IDs;
- each requirement has a source reference;
- each requirement has a canonical mapping or approved exception;
- duplicate candidates are identified;
- conflicts are identified;
- implementation impact is known;
- tests are identified;
- forward and backward traceability exist;
- consolidation decisions are auditable.

---

# 40. Next Architecture Step

The next file SHOULD formalise the actual **requirement-to-control and control-to-test model** after source inventory begins.

Provisional candidate:

> **EA-IMETA-PC-RG-409 — ACTIVE CONTROL & TEST TRACEABILITY MODEL**

This is conditional on the consolidation matrix progressing sufficiently to support real mappings.

---

# 41. Governing Principle

> **No requirement disappears because documents are consolidated. No duplicate requirement survives merely because it appears in multiple documents. Every active requirement must have a source, owner, implementation path and test.**

# END OF EA-IMETA-PC-RG-408
