# MFM Post-Steady-State Phase Control
## N2-F.00 — Materiality & Traceability Depth Disposition Record

**Control ID:** MFM-Post-Steady-State-Phase-Control-N2-F.00-Materiality-and-Depth-Disposition-Record-001  
**Version:** 1.0  
**Status:** CLOSED — CONSOLIDATED INTO N2-A / GOVERNED BY N2-E  
**Date:** 18 August 2026  
**Previous Controlled Artifact:** N2-E.00 — Traceability Status & State Control  
**Phase:** MFM Post-Steady-State  
**Workstream:** N2 — Architecture-to-Implementation Traceability  
**Planned Work Package:** N2-F — Materiality / Depth Model  
**Disposition:** CONSOLIDATED / NO SEPARATE N2-F MODEL REQUIRED

---

# 1. Purpose

N2-F.00 records the formal disposition of the originally planned N2-F work package:

```text
N2-F — Materiality / Depth Model
```

The review confirms that materiality and traceability depth are already established as core dimensions of the N2 traceability meta-model.

N2-A.00 explicitly includes:

```text
Materiality
Traceability Depth
```

as model components and includes both in its completion criteria. fileciteturn49file1

N2-E.00 subsequently uses these dimensions as controlled attributes of status and state.

Therefore, creating a second independent N2-F model would duplicate an already established semantic function.

---

# 2. Original N2 Work Package

The original controlled N2 work-package structure was:

```text
N2-A  Traceability Model
N2-B  Entity Catalogue
N2-C  Relationship Catalogue
N2-D  Evidence Model
N2-E  Traceability Status
N2-F  Materiality / Depth Model
N2-G  Gap & Orphan Model
N2-H  Pilot Traceability
N2-I  Validation
N2-J  N2 Completion Assessment
```

N2.00 explicitly defines these as work packages rather than automatic documents. fileciteturn49file4

---

# 3. Existing Materiality Model

N2-A.00 already established materiality as a controlled traceability dimension.

The model uses:

```text
M1 — LOW
M2 — MODERATE
M3 — HIGH
M4 — CRITICAL
```

Materiality determines the degree of traceability, evidence and validation appropriate to an object or relationship.

Materiality is therefore not an unimplemented future concept.

---

# 4. Existing Depth Model

N2-A.00 established traceability depth as a controlled dimension.

The conceptual levels are:

```text
D1 — Identity
D2 — Context
D3 — Relationship
D4 — Ownership
D5 — Evidence
D6 — Implementation
D7 — Operation
D8 — Measurement / Value
```

These levels describe how deeply an element must be traced for the applicable scope.

---

# 5. Why N2-F Is Consolidated

The originally planned N2-F function can be represented as:

```text
Materiality
+
Traceability Depth
```

Both are already established in N2-A.00.

N2-E.00 then demonstrates that these dimensions remain active controls by incorporating them into status interpretation.

Therefore:

```text
N2-F separate model
        ↓
DUPLICATES N2-A
        ↓
NOT REQUIRED
```

---

# 6. Authority

The authority chain is:

```text
N2-A.00
Materiality & Depth Semantics
        ↓
N2-E.00
Status / State Application
        ↓
N2-H
Pilot Application
        ↓
N2-I
Validation
```

N2-F does not become a competing authority.

---

# 7. Materiality Principle

Materiality answers:

> **How important is this object or relationship to the required traceability outcome?**

Materiality shall influence:

```text
Evidence Requirement
Validation Requirement
Traceability Depth
Review Intensity
Exception Handling
Closure Threshold
```

It shall not be used merely as a reporting label.

---

# 8. Materiality Levels

## M1 — LOW

Limited business, architectural or operational consequence.

Typical control:

```text
Basic traceability
Appropriate supporting evidence
Limited validation
```

## M2 — MODERATE

Meaningful dependency or organizational consequence.

Typical control:

```text
Identifiable authoritative evidence
Verified relationship
Defined ownership
```

## M3 — HIGH

Significant business, architectural, security or operational consequence.

Typical control:

```text
Validated relationship
Strong evidence
Explicit ownership
Higher traceability depth
Controlled exceptions
```

## M4 — CRITICAL

Failure or incorrect traceability could create critical consequence.

Typical control:

```text
Validated relationship
High-quality evidence
Appropriate corroboration / independence
Explicit authority
Formal acceptance where required
```

---

# 9. Depth Principle

Depth answers:

> **How far through the architecture-to-operation/value chain must this item be traced?**

Depth is not a quality score.

A D8 trace is not inherently better than a D3 trace.

The correct depth is determined by:

```text
Materiality
Purpose
Scope
Risk
Decision Need
Lifecycle
Evidence Requirement
```

---

# 10. Depth Levels

The controlled levels remain:

```text
D1 — Identity
D2 — Context
D3 — Relationship
D4 — Ownership
D5 — Evidence
D6 — Implementation
D7 — Operation
D8 — Measurement / Value
```

The model shall not require D8 for every object.

---

# 11. Materiality-to-Depth Guidance

Initial guidance is:

```text
M1
D1–D3 normally sufficient

M2
D3–D5 normally expected

M3
D5–D7 normally expected

M4
D6–D8 normally expected where applicable
```

These are control guidelines, not absolute automatic rules.

The actual required depth must be determined by scope and purpose.

---

# 12. Materiality-to-Evidence Relationship

Materiality determines the expected evidence burden.

```text
M1
Evidence appropriate to claim

M2
Authoritative / controlled evidence normally expected

M3
Validated evidence normally expected

M4
Validated and, where appropriate, corroborated or independent evidence
```

N2-D.00 provides the evidence-control mechanism.

---

# 13. Materiality-to-Status Relationship

N2-E.00 uses materiality to establish status expectations.

Illustrative minimums:

```text
M1
T2 SUPPORTED may be sufficient

M2
T3 VERIFIED normally expected

M3
T4 VALIDATED normally expected

M4
T4 VALIDATED + formal acceptance / exception where required
```

Therefore N2-F does not need a separate status model.

---

# 14. Materiality and Lifecycle

Materiality does not override lifecycle.

Example:

```text
Materiality = M4
Lifecycle = RETIRED
```

may still require deep historical traceability.

Similarly:

```text
Materiality = M1
Lifecycle = ACTIVE
```

does not automatically require D8.

---

# 15. Depth and Lifecycle

Depth shall be selected according to the required traceability purpose.

Examples:

```text
Historical decision
→ D5 may be sufficient

Critical implementation dependency
→ D6–D7 may be required

Strategic value relationship
→ D8 may be required
```

This prevents unnecessary over-tracing.

---

# 16. Depth and Evidence

D5 is the explicit evidence level:

```text
D5 — Evidence
```

Higher levels may require evidence of:

```text
Implementation
Operation
Measurement / Value
```

Evidence itself therefore does not automatically imply D8.

---

# 17. Depth Escalation

Depth may be increased when:

```text
Materiality increases
Risk increases
Implementation dependency is discovered
Operational dependency is discovered
Control significance increases
Decision requirements change
Evidence requirements increase
```

Depth escalation is a controlled traceability decision.

---

# 18. Depth Reduction

Depth may be reduced when:

```text
Materiality is reassessed
Scope is narrowed
Lifecycle changes
Dependency is removed
Required decision has been completed
Evidence requirement changes
```

Reduction must not remove required traceability for a still-active critical relationship.

---

# 19. Materiality Reassessment

Materiality shall be reassessed when:

```text
Business impact changes
Architecture changes
Security significance changes
Operational criticality changes
Ownership changes
Dependency changes
Regulatory significance changes
```

A materiality change may trigger a depth review.

---

# 20. Depth Reassessment

Depth shall be reassessed when:

```text
Traceability purpose changes
Implementation is introduced
Operation becomes relevant
Measurement becomes relevant
A material gap is discovered
A new dependency is identified
```

---

# 21. Materiality Conflicts

If different owners assign different materiality:

```text
Owner A → M2
Owner B → M4
```

the conflict shall be resolved through the N2 governance mechanism.

The higher level may be used provisionally where required to avoid under-control, pending formal resolution.

---

# 22. Depth Conflicts

If one analysis requires D3 and another requires D7:

```text
D3
vs
D7
```

the difference shall be treated as a scope/control question rather than a semantic contradiction.

The required depth shall be determined from:

```text
Purpose
Materiality
Risk
Decision Need
```

---

# 23. No Automatic Maximum Depth

N2 explicitly rejects the assumption:

```text
More depth = better architecture
```

The objective is:

```text
Sufficient traceability
```

not:

```text
Maximum traceability
```

---

# 24. Materiality and Evidence Gaps

A missing evidence item for an M1 relationship may be a low-priority finding.

The same missing evidence for an M4 relationship may be a critical traceability finding.

Therefore:

```text
Gap Severity
=
Function of Materiality + Impact + Required Depth
```

---

# 25. Materiality and Orphans

An orphaned low-materiality entity may be resolved during normal cleanup.

An orphaned critical implementation component may require immediate investigation.

The orphan model must therefore consume materiality rather than duplicate it.

---

# 26. Materiality and Contradictions

A contradiction involving an M4 relationship shall receive higher resolution priority than an equivalent M1 contradiction.

This ensures that N2 findings remain risk-oriented.

---

# 27. Materiality and Closure

A work package cannot be considered complete merely because:

```text
all objects have a status
```

The closure assessment must consider whether required materiality/depth controls have been satisfied.

---

# 28. Materiality and Exceptions

Where required depth or validation cannot be achieved:

```text
Exception
+
Risk
+
Owner
+
Review Date
+
Approval
```

shall be recorded for material cases.

The exception does not change the underlying materiality.

---

# 29. Repository Representation

A future traceability repository should store:

```text
Materiality
Traceability Depth
```

as controlled attributes.

They should not be encoded solely in free-text comments.

---

# 30. Reporting

Materiality/depth reporting may include:

```text
Objects by Materiality
Relationships by Materiality
Relationships by Depth
M3/M4 relationships without T4
M3/M4 relationships below required depth
Critical gaps
Critical exceptions
```

These are reporting capabilities, not mandatory dashboard requirements.

---

# 31. Pilot Use

The preferred pilot remains:

```text
CAN-01 — Enterprise Integration
```

The pilot shall verify:

```text
Materiality assignment
Depth assignment
Materiality-to-evidence relationship
Materiality-to-status relationship
Depth sufficiency
Escalation
Reduction
Exception handling
```

---

# 32. Pilot Questions

The pilot shall answer:

```text
Can materiality be assigned consistently?
Can depth be assigned without ambiguity?
Can the same object have different depth requirements for different purposes?
Can materiality drive evidence requirements?
Can materiality drive validation requirements?
Can depth be increased or reduced through control?
Can M4 items be identified reliably?
Can insufficient depth be detected?
Can exceptions be represented?
```

---

# 33. Consolidation Decision

The formal decision is:

```text
N2-F — MATERIALITY / DEPTH MODEL
        ↓
ALREADY ESTABLISHED IN N2-A.00
        ↓
APPLIED THROUGH N2-E.00
        ↓
SUPPORTED BY N2-D.00
        ↓
VALIDATED THROUGH N2-H / N2-I
```

Therefore:

```text
Separate N2-F model
= NOT REQUIRED
```

---

# 34. N2-F Closure

The work package is closed by disposition rather than by creation of a duplicate model.

Formal state:

```text
N2-F-SC-90 — MATERIALITY / DEPTH CONSOLIDATED
```

This means:

```text
Semantic Function = ESTABLISHED
Separate Artifact = NOT REQUIRED
Pilot Validation = PENDING
```

---

# 35. No N2-F Successor Chain

N2-F.00 shall not generate:

```text
N2-F.01
N2-F.02
N2-F.03
...
```

Additional materiality/depth requirements shall be handled through:

```text
N2-A controlled revision
```

unless a genuinely new, materially distinct function is demonstrated.

---

# 36. Relationship to N2-G

The next planned work package is:

```text
N2-G — Gap & Orphan Model
```

N2-G may therefore focus on:

```text
Gap Semantics
Orphan Semantics
Detection Logic
Resolution
Disposition
```

rather than recreating:

```text
Materiality
Depth
Status
Evidence
```

Those controls already exist.

---

# 37. Anti-Runaway Decision

N2-F demonstrates the intended Post-Steady-State control:

```text
Planned Work Package
        ↓
Existing Semantic Function Review
        ↓
Already Covered
        ↓
Formal Disposition
        ↓
No Duplicate Artifact
```

This is the correct alternative to document proliferation.

---

# 38. Final N2-F Finding

> **N2-F.00 formally consolidates the originally planned Materiality / Depth Model work package into the existing N2-A traceability model, with operational use governed through N2-E and evidence implications governed through N2-D. No separate N2-F semantic model is required because the materiality and traceability-depth functions are already established and sufficiently controlled.**

---

# 39. Final N2-F Principle

> **Materiality and traceability depth shall be used to achieve sufficient control for the required purpose, not to maximize documentation or traceability depth.**

---

# 40. Final N2-F Anti-Runaway Principle

> **A planned model shall not become a separate artifact when its semantic function is already adequately established in an authoritative controlled model. Consolidation is the correct completion state.**

---

# 41. Document Control

**Document:** MFM Post-Steady-State Phase Control — N2-F.00 Materiality & Traceability Depth Disposition Record  
**Control ID:** MFM-Post-Steady-State-Phase-Control-N2-F.00-Materiality-and-Depth-Disposition-Record-001  
**Version:** 1.0  
**Status:** CLOSED — CONSOLIDATED INTO N2-A / GOVERNED BY N2-E  
**Date:** 18 August 2026  
**Previous Controlled Artifact:** N2-E.00 — Traceability Status & State Control  
**Phase:** MFM Post-Steady-State  
**Workstream:** N2 — Architecture-to-Implementation Traceability  
**Planned Work Package:** N2-F — Materiality / Depth Model  
**Disposition:** CONSOLIDATED / NO SEPARATE N2-F MODEL REQUIRED  
**Materiality Levels:** 4  
**Traceability Depth Levels:** 8  
**Authoritative Semantic Model:** N2-A.00  
**Status Application:** N2-E.00  
**Evidence Control:** N2-D.00  
**Pilot:** CAN-01 Enterprise Integration — RECOMMENDED / PENDING VALIDATION  
**Closure State:** N2-F-SC-90 — MATERIALITY / DEPTH CONSOLIDATED  
**Automatic Successor Generation:** PROHIBITED
