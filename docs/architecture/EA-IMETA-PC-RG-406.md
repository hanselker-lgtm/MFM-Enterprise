# EA-IMETA-PC-RG-406

## PC-RG RESPONSIBILITY INVENTORY & CONSOLIDATION MATRIX

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-406 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Responsibility Inventory & Consolidation Matrix |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent Architecture | EA-IMETA-PC-RG-405 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Map the existing PC-RG document population to distinct architectural responsibilities |
| Decision Gate | Determines which legacy artifacts are retained, merged, referenced, superseded or archived |

---

# 2. Purpose

EA-IMETA-PC-RG-406 converts the consolidation principle established by EA-IMETA-PC-RG-405 into an operational inventory method.

The purpose is not to generate another layer of governance terminology.

The purpose is to answer:

> **What distinct architectural responsibility does each existing PC-RG artifact actually provide?**

The inventory SHALL become the authoritative working index for the PC-RG consolidation.

---

# 3. Scope

The initial population is:

```text
EA-IMETA-PC-RG-001
        ↓
        …
        ↓
EA-IMETA-PC-RG-404
```

The inventory SHALL evaluate each artifact independently.

A document number SHALL NOT be treated as evidence that the document represents a unique responsibility.

---

# 4. Canonical Responsibility Set

The initial canonical responsibility model from RG-405 is:

| Code | Responsibility | Core Question |
|---|---|---|
| VAL | Validation | Is the state valid against criteria? |
| VER | Verification | Was the validation performed correctly? |
| ACC | Acceptance | May the organisation rely on the result? |
| CLO | Closure | Has the lifecycle been formally completed? |
| MON | Monitoring | Does the accepted/closed state remain valid? |
| REG | Regression Detection | Has a material change occurred? |
| REM | Remediation | What must be corrected? |
| RVA | Revalidation | Is the corrected/current state valid again? |
| RAC | Reacceptance | May reliance be restored? |

Cross-cutting concerns such as governance, authority, accountability, evidence and compliance SHALL normally be mapped into these responsibilities rather than treated as separate responsibilities.

---

# 5. Consolidation Outcomes

Each legacy artifact SHALL receive exactly one primary disposition.

```text
RETAIN
MERGE
REFERENCE
SUPERSEDE
ARCHIVE
```

### RETAIN

The artifact contains a materially unique architectural responsibility that remains required.

### MERGE

The artifact contains valid requirements that belong inside another canonical responsibility.

### REFERENCE

The artifact provides useful historical, explanatory or traceability material but does not require an independent active responsibility.

### SUPERSEDE

The artifact is replaced by a newer authoritative architecture artifact.

### ARCHIVE

The artifact has historical value but no active architectural responsibility.

---

# 6. Inventory Record

Every PC-RG artifact SHALL be assessed using the following record:

| Field | Required |
|---|---|
| File ID | Yes |
| Title | Yes |
| Existing Parent | Yes |
| Existing Purpose | Yes |
| Existing Core Principle | Yes |
| Primary Verb | Yes |
| Primary Object | Yes |
| Claimed Responsibility | Yes |
| Canonical Responsibility | Yes |
| Decision Produced | Yes |
| State Produced | Yes |
| Input | Yes |
| Output | Yes |
| Authority | Yes |
| Evidence | Yes |
| Control Mechanism | Yes |
| MFM Relevance | Yes |
| Duplicate Candidate | Yes |
| Dependencies | Yes |
| Disposition | Yes |
| Reason | Yes |
| Replacement Reference | Where applicable |
| Traceability Requirement | Yes |

---

# 7. Primary Verb Test

The primary verb is more important than the title.

Examples:

```text
VALIDATE
VERIFY
ACCEPT
CLOSE
MONITOR
DETECT
REMEDIATE
REVALIDATE
REACCEPT
```

If the primary verb cannot be identified, the artifact SHALL be reviewed for duplication or abstraction without operational responsibility.

---

# 8. Primary Object Test

The inventory SHALL identify what the responsibility actually acts upon.

Examples:

```text
State
Validation Result
Verification Result
Acceptance Decision
Closed Case
Baseline
Current State
Regression Finding
Remediation Action
Revalidation Result
```

A title containing multiple nouns does not prove multiple objects.

---

# 9. Decision Test

The inventory SHALL determine whether the artifact produces an independent decision.

Examples:

```text
VALID
INVALID
VERIFIED
NOT VERIFIED
ACCEPTED
REJECTED
CLOSED
REOPENED
REGRESSION
NO REGRESSION
REMEDIATION COMPLETE
REVALIDATED
REACCEPTED
```

If an artifact produces no identifiable decision or state transition, it is a candidate for MERGE or REFERENCE.

---

# 10. State Transition Test

Each retained responsibility SHALL have a state transition.

Example:

```text
UNVALIDATED
    ↓
VALIDATION
    ↓
VALIDATED
```

Verification:

```text
VALIDATED
    ↓
VERIFICATION
    ↓
VERIFIED
```

Acceptance:

```text
VERIFIED
    ↓
ACCEPTANCE
    ↓
ACCEPTED
```

Regression:

```text
MONITORED
    ↓
CHANGE DETECTED
    ↓
MATERIALITY ASSESSMENT
    ↓
REGRESSION / NO REGRESSION
```

If no state transition exists, the artifact SHALL be examined for whether it is a supporting specification rather than a lifecycle responsibility.

---

# 11. Authority Test

The inventory SHALL identify who is authorised to perform each responsibility.

Minimum authority distinctions:

```text
PERFORM
REVIEW
VERIFY
APPROVE
ACCEPT
REVOKE
REOPEN
```

The same actor SHALL not automatically receive all authorities.

Where separation of duties is required, it SHALL be explicitly recorded.

---

# 12. Evidence Test

Evidence SHALL answer:

```text
What proves that the responsibility was performed?
```

Evidence shall be linked to:

```text
Subject
Action
Actor
Time
Criteria
Decision
Result
```

A document describing evidence requirements is not itself evidence that the process occurred.

---

# 13. MFM Relevance Test

Each artifact SHALL be classified according to its expected MFM impact:

```text
DOMAIN LOGIC
WORKFLOW
DATA MODEL
AUTHORITY / PERMISSION
UI
REPORTING
AUDIT
NOT DIRECTLY IMPLEMENTED
```

This prevents abstract EA language from being mistaken for implemented functionality.

---

# 14. Duplicate Classification

Two artifacts are duplicate candidates when they have substantially the same:

```text
Primary Verb
+
Primary Object
+
Decision
+
State Transition
+
Authority
+
Output
```

Example:

```text
RG-392
RG-394
RG-396
RG-398
RG-400
RG-402
RG-404
```

If these all perform the same substantive VALIDATE responsibility, their differing titles or Parent references do not make them independent responsibilities.

They SHALL therefore be consolidated unless a documented architectural distinction exists.

---

# 15. Legacy Chain Analysis

The repeated sequence shall be evaluated as a semantic chain rather than accepted as an architectural chain.

```text
RG-N
 ↓
"validates previous verification"
 ↓
RG-N+1
 ↓
"verifies previous validation"
 ↓
RG-N+2
 ↓
"validates previous verification"
```

The inventory SHALL determine whether the sequence represents:

```text
A REAL CONTROL LOOP
```

or merely:

```text
A DOCUMENT GENERATION LOOP
```

A control loop requires measurable state, evidence, decision, authority and consequence.

---

# 16. Control Loop Test

A genuine assurance loop SHALL satisfy:

```text
BASELINE
   ↓
ASSESS
   ↓
DECIDE
   ↓
ACT
   ↓
OBSERVE
   ↓
COMPARE
   ↓
CORRECT
   ↓
REASSESS
```

If a document adds no new stage to this loop, it SHALL not be considered a new control merely because its title differs.

---

# 17. Preliminary Mapping Framework

The following mapping is the starting hypothesis and SHALL be verified against the actual contents of RG-001–404.

| Legacy Pattern | Likely Canonical Responsibility |
|---|---|
| Validation-oriented artifact | VAL |
| Verification-oriented artifact | VER |
| Acceptance-oriented artifact | ACC |
| Closure-oriented artifact | CLO |
| Monitoring-oriented artifact | MON |
| Regression-oriented artifact | REG |
| Remediation-oriented artifact | REM |
| Revalidation-oriented artifact | RVA |
| Reacceptance-oriented artifact | RAC |
| Governance-only artifact | MERGE / REFERENCE |
| Authority-only artifact | MERGE |
| Role-only artifact | MERGE |
| Accountability-only artifact | MERGE |
| Criteria-only artifact | MERGE |
| Evidence-only artifact | MERGE |
| Repeated Validate/Verify variant | DUPLICATE CANDIDATE |

This table is a hypothesis, not a final disposition.

---

# 18. Consolidation Matrix Template

The active matrix SHALL use the following structure:

| File ID | Existing Title | Primary Verb | Primary Object | Decision | State | Canonical Responsibility | MFM Impact | Disposition | Reason |
|---|---|---|---|---|---|---|---|---|---|
| RG-001 | TBD from source | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| RG-002 | TBD from source | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| RG-003 | TBD from source | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| … | … | … | … | … | … | … | … | … | … |
| RG-404 | TBD from source | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

No unknown value SHALL be silently converted into a positive architectural conclusion.

---

# 19. Required Evidence for Final Disposition

Before an artifact is marked RETAIN, MERGE or SUPERSEDE, the following SHALL be available:

```text
SOURCE DOCUMENT
      ↓
REQUIREMENTS EXTRACTED
      ↓
RESPONSIBILITY IDENTIFIED
      ↓
DECISION IDENTIFIED
      ↓
STATE IDENTIFIED
      ↓
DEPENDENCIES IDENTIFIED
      ↓
MFM IMPACT IDENTIFIED
      ↓
DISPOSITION JUSTIFIED
```

---

# 20. Consolidation Rules

### Rule 1 — No title-based decisions

The title alone SHALL never determine disposition.

### Rule 2 — No parent-chain authority

A Parent reference SHALL not create architectural authority.

### Rule 3 — No document-count assurance

The number of documents SHALL not be used as evidence of control maturity.

### Rule 4 — No duplicate controls

Equivalent responsibilities SHALL be consolidated.

### Rule 5 — Preserve valid requirements

Redundant documents may contain requirements that must survive consolidation.

### Rule 6 — Preserve historical traceability

Historical artifacts SHALL remain traceable even after being removed from the active baseline.

### Rule 7 — Implementation must be identifiable

An active responsibility should map to a process, service, data object, workflow, permission or test.

---

# 21. Consolidation Decision Tree

```text
LEGACY DOCUMENT
      │
      ▼
UNIQUE RESPONSIBILITY?
      │
 ┌────┴────┐
NO        YES
 │          │
 ▼          ▼
MERGE/     DECISION?
REFERENCE     │
              ▼
          STATE CHANGE?
              │
              ▼
          AUTHORITY?
              │
              ▼
          MFM IMPACT?
              │
              ▼
            RETAIN
```

Historical-only material:

```text
NO ACTIVE RESPONSIBILITY
        ↓
REFERENCE / ARCHIVE
```

---

# 22. Required Consolidated Architecture

The final active PC-RG model SHOULD converge toward:

```text
                ┌──────────────┐
                │  VALIDATION  │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │ VERIFICATION │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │  ACCEPTANCE  │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │   CLOSURE    │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │  MONITORING  │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │  REGRESSION  │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │ REMEDIATION  │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │REVALIDATION  │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │REACCEPTANCE  │
                └──────────────┘
```

Cross-cutting architecture:

```text
        AUTHORITY
           │
EVIDENCE ──┼── AUDIT
           │
      ACCOUNTABILITY
           │
      TRACEABILITY
           │
        SECURITY
           │
       COMPLIANCE
```

These cross-cutting elements SHALL support the lifecycle rather than create parallel title chains.

---

# 23. Deliverable of This Inventory

The completed inventory SHALL produce four outputs:

### A. Legacy-to-Canonical Map

Every RG-001–404 artifact mapped to a canonical responsibility.

### B. Duplicate Cluster List

Groups of documents that express the same responsibility.

### C. Requirement Preservation Map

Requirements from legacy artifacts mapped to the retained architecture.

### D. Active Baseline Proposal

A proposed set of active PC-RG documents with explicit responsibilities and dependencies.

---

# 24. Completion Criteria

This inventory is complete when:

- all in-scope legacy artifacts have been assessed;
- no artifact has an unexplained disposition;
- duplicate clusters are identified;
- requirements are preserved;
- canonical responsibilities are confirmed;
- state transitions are documented;
- decision authority is mapped;
- MFM relevance is identified;
- historical traceability is preserved;
- the proposed active baseline is internally consistent.

---

# 25. Critical Limitation

The present document defines the **inventory method and consolidation framework**.

It does not claim that RG-001–404 have been individually inspected here.

Where the actual source content of a legacy file is unavailable, the matrix SHALL record:

```text
UNKNOWN — SOURCE CONTENT REQUIRED
```

rather than inventing a mapping.

This distinction is mandatory for architectural integrity.

---

# 26. Next Active Artifact

The next artifact SHALL be created only after the inventory evidence required for its scope is available.

The likely next artifact is:

> **PC-RG Active Baseline Architecture**

but that name SHALL remain provisional until the consolidation matrix establishes which responsibilities actually need separate active documents.

---

# 27. Governing Principle

> **The inventory is authoritative about what is known, explicit about what is unknown, and conservative about what is retained.**

The PC-RG architecture SHALL become smaller and clearer when consolidation removes duplication.

It SHALL become larger only when a demonstrably distinct responsibility requires it.

# END OF EA-IMETA-PC-RG-406
