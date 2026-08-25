# EA-IMETA-PC-RG-484

## ENTERPRISE CAPITAL DYNAMICS, INVESTMENT FLOW, LIQUIDITY GOVERNANCE, REAL-OPTION PORTFOLIOS & DYNAMIC CAPITAL ALLOCATION ARCHITECTURE


# 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-484 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Enterprise Capital Dynamics, Investment Flow, Liquidity Governance, Real-Option Portfolios & Dynamic Capital Allocation Architecture |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-483 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Establish the enterprise architecture for capital pools, investment flow, liquidity, funding constraints, real options, staged commitments and dynamic capital allocation |
| Architectural Boundary | Capital State → Liquidity → Funding → Investment Options → Sequencing → Allocation → Commitment → Realisation → Recycle |

# 2. Architectural Position

RG-484 continues the Enterprise Economics family.

RG-481 established autonomous economics, opportunity cost and allocation economics.

RG-482 established resource intelligence, capacity forecasting, scarcity modelling and dynamic resource markets.

RG-483 established value networks, marginal value propagation, portfolio interaction and multi-objective optimisation.

RG-484 now focuses on the **capital system itself**.

The principal question becomes:

> **How should enterprise capital move through the organisation over time so that liquidity remains protected, high-value opportunities can be funded, commitments are sequenced intelligently, future options remain available, and realised capital can be recycled into the next generation of value creation?**

Capital is therefore treated as a dynamic flow rather than a static budget.

```text
CAPITAL STATE
      ↓
LIQUIDITY POSITION
      ↓
FUNDING CAPACITY
      ↓
INVESTMENT OPTIONS
      ↓
SEQUENCING
      ↓
CAPITAL ALLOCATION
      ↓
COMMITMENT
      ↓
DEPLOYMENT
      ↓
VALUE REALISATION
      ↓
CASH / CAPITAL RECOVERY
      ↓
RECYCLE
      ↺
```

# 3. Core Principle

> **Enterprise capital SHALL remain liquid enough to preserve continuity and optionality while being dynamically allocated toward the highest governed combination of value, strategic contribution, resilience, risk-adjusted return and future choice.**

Capital optimisation SHALL never be permitted to create hidden liquidity fragility.

The architecture SHALL therefore distinguish:

```text
CAPITAL
≠
CASH
≠
LIQUIDITY
≠
FUNDING CAPACITY
≠
INVESTMENT CAPACITY
≠
VALUE
≠
PROFIT
≠
RETURN
≠
OPTION VALUE
```

# 4. Core Definitions

```text
CAPITAL
= RESOURCE AVAILABLE FOR FUNDING ENTERPRISE ACTIVITIES, INVESTMENTS OR strategic commitments

CAPITAL POOL
= GOVERNED AGGREGATION OF CAPITAL AVAILABLE FOR allocation

CAPITAL CLASS
= CATEGORY OF CAPITAL WITH DISTINCT GOVERNANCE OR ECONOMIC characteristics

CAPITAL OWNER
= ACCOUNTABLE AUTHORITY FOR A CAPITAL POOL

CAPITAL MANDATE
= GOVERNED PURPOSE AND BOUNDARIES OF A CAPITAL POOL

CAPITAL STATE
= CURRENT REPRESENTATION OF AVAILABLE, COMMITTED, RESERVED AND DEPLOYED capital

CAPITAL POSITION
= CURRENT QUANTIFIED CAPITAL STATE ACROSS relevant classes

CAPITAL AVAILABILITY
= CAPITAL CURRENTLY AVAILABLE FOR allocation

CAPITAL COMMITMENT
= CAPITAL LEGALLY OR GOVERNED-APPROVED FOR FUTURE deployment

CAPITAL RESERVATION
= CAPITAL HELD FOR A DEFINED FUTURE purpose

CAPITAL DEPLOYMENT
= ACTUAL RELEASE OF CAPITAL INTO an approved use

CAPITAL RELEASE
= RETURN OF CAPITAL TO an available pool

CAPITAL RECOVERY
= RETURN OF CAPITAL FROM an investment or activity

CAPITAL RECYCLING
= REUSE OF RECOVERED CAPITAL FOR new value creation

CAPITAL VELOCITY
= RATE AT WHICH CAPITAL MOVES FROM commitment THROUGH deployment AND recovery

CAPITAL LATENCY
= TIME BETWEEN CAPITAL COMMITMENT AND VALUE OR capital recovery

CAPITAL TURNOVER
= RATE AT WHICH CAPITAL IS recycled through investment cycles

CAPITAL PRODUCTIVITY
= VALUE OR OUTCOME GENERATED PER UNIT OF capital

CAPITAL EFFICIENCY
= OUTPUT RELATIVE TO capital consumed

CAPITAL EFFECTIVENESS
= DEGREE TO WHICH CAPITAL ACHIEVES intended outcomes

LIQUIDITY
= ABILITY TO MEET CURRENT AND NEAR-TERM financial obligations without unacceptable disruption

LIQUIDITY POSITION
= CURRENT AVAILABLE LIQUID RESOURCES RELATIVE TO obligations and buffers

LIQUIDITY BUFFER
= PROTECTED LIQUIDITY RESERVED FOR uncertainty or disruption

LIQUIDITY FLOOR
= MINIMUM ACCEPTABLE LIQUIDITY LEVEL

LIQUIDITY CEILING
= UPPER BOUND ON LIQUID HOLDING WHERE excess liquidity has an economic cost

LIQUIDITY GAP
= DIFFERENCE BETWEEN REQUIRED AND available liquidity

LIQUIDITY STRESS
= CONDITION WHERE LIQUIDITY APPROACHES critical thresholds

LIQUIDITY FORECAST
= PREDICTION OF future liquidity position

LIQUIDITY HORIZON
= PERIOD OVER WHICH LIQUIDITY IS assessed

LIQUIDITY SHOCK
= SUDDEN MATERIAL REDUCTION IN available liquidity

LIQUIDITY RECOVERY
= RESTORATION OF required liquidity after a shock

FUNDING CAPACITY
= ABILITY TO OBTAIN OR deploy additional capital within approved constraints

FUNDING SOURCE
= SOURCE FROM WHICH CAPITAL CAN BE obtained

FUNDING COMMITMENT
= GOVERNED AGREEMENT TO provide capital

FUNDING COST
= COST ASSOCIATED WITH obtaining or maintaining capital

FUNDING WINDOW
= TIME PERIOD IN WHICH funding is available

FUNDING CONSTRAINT
= LIMITATION ON capital availability or financing

FUNDING DIVERSIFICATION
= DISTRIBUTION OF funding exposure across sources

FUNDING CONCENTRATION
= DEPENDENCE ON limited funding sources

FUNDING RESILIENCE
= ABILITY TO maintain funding under disruption

CAPITAL COST
= ECONOMIC COST ASSOCIATED WITH deploying or holding capital

COST OF CAPITAL
= GOVERNED MEASURE OF required return or economic cost of capital

CAPITAL HURDLE
= MINIMUM REQUIRED economic performance for a capital commitment

RETURN
= ECONOMIC OUTCOME GENERATED BY capital deployment

RISK-ADJUSTED RETURN
= RETURN ADJUSTED FOR relevant risk

RETURN PROFILE
= DISTRIBUTION OF expected returns and downside

RETURN LATENCY
= TIME UNTIL RETURN IS expected or realised

DOWNSIDE
= POTENTIAL NEGATIVE ECONOMIC outcome

UPSIDE
= POTENTIAL POSITIVE ECONOMIC outcome

CAPITAL AT RISK
= CAPITAL EXPOSED TO potential loss or impairment

VALUE AT RISK
= POTENTIAL LOSS OF expected enterprise value

INVESTMENT
= CAPITAL COMMITMENT INTENDED TO produce future value

INVESTMENT THESIS
= GOVERNED LOGIC EXPLAINING WHY an investment should create value

INVESTMENT CASE
= STRUCTURED REPRESENTATION OF value, cost, risk, timing and assumptions

INVESTMENT OPTION
= AVAILABLE INVESTMENT ALTERNATIVE

INVESTMENT PIPELINE
= SET OF current and potential investment opportunities

INVESTMENT BACKLOG
= APPROVED OR qualified investments awaiting capacity or funding

INVESTMENT STAGE
= DEFINED STEP IN AN investment lifecycle

STAGE GATE
= DECISION POINT AT WHICH continuation requires reassessment

STAGED COMMITMENT
= CAPITAL COMMITMENT RELEASED IN multiple governed stages

TRANCHE
= DEFINED PORTION OF capital released under specified conditions

CAPITAL RELEASE CONDITION
= CONDITION REQUIRED BEFORE additional capital is deployed

CAPITAL STOP CONDITION
= CONDITION THAT prevents further deployment

CAPITAL STOP-LOSS
= GOVERNED THRESHOLD FOR reducing or ending capital exposure

INVESTMENT ABANDONMENT VALUE
= VALUE OF TERMINATING AN investment and redeploying remaining resources

REAL OPTION
= VALUE OF RETAINING THE RIGHT BUT NOT obligation TO make a future investment decision

OPTION VALUE
= ECONOMIC VALUE OF future decision flexibility

EXPANSION OPTION
= OPTION TO INCREASE future investment

CONTRACTION OPTION
= OPTION TO REDUCE future investment

ABANDONMENT OPTION
= OPTION TO stop an investment

DEFERMENT OPTION
= OPTION TO delay a capital commitment

SWITCHING OPTION
= OPTION TO change investment or operating configuration

SEQUENCING
= ORDERING OF capital commitments over time

INVESTMENT SEQUENCING
= ORDERING INVESTMENTS TO maximise value, optionality and constraint compliance

CAPITAL PRIORITY
= GOVERNED ORDER OF capital allocation

CAPITAL ENVELOPE
= BOUNDED RANGE OF capital that may be committed or deployed

CAPITAL QUOTA
= DEFINED MAXIMUM OR TARGET allocation

CAPITAL RESERVE
= CAPITAL PROTECTED FOR defined future needs

STRATEGIC CAPITAL RESERVE
= CAPITAL RESERVED FOR strategic opportunities or risks

CONTINGENCY CAPITAL
= CAPITAL HELD FOR unexpected events

WORKING CAPITAL
= CAPITAL REQUIRED TO SUPPORT ongoing operations

GROWTH CAPITAL
= CAPITAL RESERVED FOR expansion or growth

MAINTENANCE CAPITAL
= CAPITAL REQUIRED TO preserve existing capability

TRANSFORMATION CAPITAL
= CAPITAL USED FOR strategic transformation

INNOVATION CAPITAL
= CAPITAL USED FOR uncertain future opportunities

RESILIENCE CAPITAL
= CAPITAL USED TO preserve or increase resilience

CAPITAL BUCKET
= GOVERNED CATEGORY OF capital with distinct allocation rules

CAPITAL WATERFALL
= ORDERED LOGIC FOR capital distribution and priority

CAPITAL CASCADE
= SEQUENTIAL FLOW OF capital through governed decision stages

CAPITAL GATE
= GOVERNED CONTROL POINT FOR capital release

CAPITAL ALLOCATION
= DISTRIBUTION OF capital across uses

DYNAMIC CAPITAL ALLOCATION
= CAPITAL ALLOCATION THAT ADAPTS TO changing value, risk, liquidity and strategy

CAPITAL REALLOCATION
= TRANSFER OF capital between existing allocations

CAPITAL ROTATION
= CONTROLLED SHIFT OF capital across opportunities

CAPITAL CHURN
= FREQUENCY OF capital movement between allocations

CAPITAL LOCK-IN
= CONDITION WHERE capital cannot be readily redeployed

CAPITAL STRANDED
= CAPITAL COMMITTED TO a use with limited ability to generate expected value or be recovered

CAPITAL SLACK
= AVAILABLE UNCOMMITTED capital beyond protected reserves

CAPITAL SCARCITY
= CONDITION WHERE available capital is insufficient for qualified demand

CAPITAL BOTTLENECK
= CAPITAL CONSTRAINT LIMITING enterprise value creation

CAPITAL QUEUE
= ORDERED SET OF funding requests awaiting allocation

CAPITAL DEMAND
= REQUIRED CAPITAL FOR planned or potential uses

CAPITAL SUPPLY
= CAPITAL AVAILABLE FOR allocation

CAPITAL MARKET
= GOVERNED INTERNAL OR external mechanism for sourcing and allocating capital

INTERNAL CAPITAL MARKET
= ENTERPRISE MECHANISM FOR allocating capital among units, portfolios or initiatives

CAPITAL BID
= REQUEST FOR CAPITAL WITH defined economic and strategic conditions

CAPITAL OFFER
= AVAILABLE FUNDING WITH defined terms or conditions

CAPITAL CLEARING
= PROCESS OF MATCHING CAPITAL supply and demand

CAPITAL PRICE
= ECONOMIC COST OR required return associated with capital

SHADOW COST OF CAPITAL
= IMPLIED ECONOMIC COST OF capital under constraint

CAPITAL LIQUIDITY PREMIUM
= ADDITIONAL VALUE OR cost associated with maintaining liquidity

OPTION PREMIUM
= COST OF preserving future decision flexibility

CAPITAL CONCENTRATION
= CONCENTRATION OF capital exposure

CAPITAL DIVERSIFICATION
= DISTRIBUTION OF capital exposure across opportunities

CAPITAL CORRELATION
= DEGREE TO WHICH capital outcomes move together

CAPITAL DEPENDENCY
= DEPENDENCE OF one capital allocation on another

CAPITAL COMPLEMENTARITY
= CONDITION WHERE combined investments create additional value

CAPITAL CANNIBALISATION
= REDUCTION OF value in one investment caused by another capital allocation

CAPITAL SYNERGY
= ADDITIONAL VALUE CREATED BY coordinated capital deployment

CAPITAL EXTERNALITY
= EFFECT OF capital deployment on other enterprise areas

CAPITAL NETWORK
= CONNECTED SYSTEM OF capital pools, investments, funding sources and value outcomes

CAPITAL GRAPH
= GRAPH REPRESENTING capital flows, dependencies and commitments

CAPITAL FLOW
= MOVEMENT OF capital through the enterprise

CAPITAL FLOW RATE
= RATE OF capital movement through a process or portfolio

CAPITAL FLOW CONSTRAINT
= LIMITATION ON capital movement

CAPITAL FLOW BOTTLENECK
= CONSTRAINT THAT SLOWS capital movement

CAPITAL FLOW FRICTION
= COST OR DELAY IN capital movement

CAPITAL RECYCLE RATE
= RATE AT WHICH recovered capital becomes available for redeployment

CAPITAL REINVESTMENT RATE
= RATE AT WHICH recovered or generated capital is reinvested

CAPITAL DEPLOYMENT CURVE
= PROFILE OF capital deployment over time

VALUE REALISATION CURVE
= PROFILE OF value realisation over time

CASH FLOW PROFILE
= TIME-BASED REPRESENTATION OF cash inflows and outflows

LIQUIDITY PROFILE
= TIME-BASED REPRESENTATION OF liquidity availability and obligations

FUNDING PROFILE
= TIME-BASED REPRESENTATION OF funding availability and cost

INVESTMENT PROFILE
= TIME-BASED REPRESENTATION OF investment commitments and deployment

CAPITAL SCENARIO
= DEFINED FUTURE capital and liquidity condition

CAPITAL STRESS TEST
= TEST OF capital system under adverse conditions

LIQUIDITY STRESS TEST
= TEST OF liquidity under adverse cash or funding conditions

FUNDING STRESS TEST
= TEST OF funding resilience under adverse conditions

CAPITAL DIGITAL TWIN
= MODEL OF capital flows, liquidity, funding and investment dynamics

CAPITAL ORCHESTRATOR
= GOVERNED SERVICE COORDINATING capital decisions

INVESTMENT AGENT
= AUTONOMOUS COMPONENT SPECIALISED IN investment analysis

LIQUIDITY AGENT
= AUTONOMOUS COMPONENT SPECIALISED IN liquidity monitoring and forecasting

CAPITAL ALLOCATION AGENT
= AUTONOMOUS COMPONENT SPECIALISED IN capital allocation

FUNDING AGENT
= AUTONOMOUS COMPONENT SPECIALISED IN funding analysis

OPTION AGENT
= AUTONOMOUS COMPONENT SPECIALISED IN real-option analysis

CAPITAL QUORUM
= REQUIRED INDEPENDENT EVIDENCE OR approval FOR material capital decisions

CAPITAL DISSENT
= MATERIAL DISAGREEMENT ABOUT capital allocation or investment assumptions

CAPITAL EXPLAINABILITY
= ABILITY TO EXPLAIN WHY capital was allocated

CAPITAL PROVENANCE
= TRACEABILITY OF capital assumptions, approvals, releases and outcomes

CAPITAL AUDIT TRAIL
= RECONSTRUCTABLE RECORD OF capital decisions and movements

CAPITAL GOVERNANCE
= GOVERNANCE OF capital ownership, allocation, liquidity, funding and investment

CAPITAL AUTHORITY
= AUTHORITY TO approve or execute capital decisions

LIQUIDITY AUTHORITY
= AUTHORITY TO change protected liquidity positions

INVESTMENT AUTHORITY
= AUTHORITY TO approve investment commitments

CAPITAL GUARDRAIL
= CONSTRAINT PREVENTING economically, strategically or operationally unsafe capital decisions

LIQUIDITY GUARDRAIL
= LIMIT PROTECTING required liquidity

FUNDING GUARDRAIL
= LIMIT PROTECTING funding resilience

CONCENTRATION GUARDRAIL
= LIMIT ON capital concentration

OPTIONALITY GUARDRAIL
= PROTECTION OF minimum future decision flexibility

CAPITAL RECOVERY EVENT
= EVENT RETURNING capital or value to an available pool

CAPITAL RECYCLING EVENT
= EVENT MAKING recovered capital available for new allocation

CAPITAL LEARNING LOOP
= DEPLOY → MEASURE → REALISE → RECOVER → RECYCLE → LEARN
```

# 5. Capital Pool Object

Minimum attributes:

```text
Capital Pool ID
Capital Class
Owner
Purpose
Available Capital
Reserved Capital
Committed Capital
Liquidity Requirement
Investment Mandate
Risk Limit
Strategic Weight
Status
```

# 6. Liquidity Position Object

Minimum attributes:

```text
Liquidity ID
Current Liquidity
Committed Outflows
Expected Inflows
Liquidity Buffer
Liquidity Floor
Stress Horizon
Funding Capacity
Confidence
Status
```

# 7. Investment Option Object

Minimum attributes:

```text
Option ID
Investment
Required Capital
Expected Value
Risk
Time to Value
Option Value
Reversibility
Stage
Dependencies
Status
```

# 8. Capital Commitment Object

Minimum attributes:

```text
Commitment ID
Capital Pool
Investment
Approved Amount
Released Amount
Remaining Amount
Release Conditions
Stop Conditions
Expiry
Authority
Status
```

# 9. Capital Flow Object

Minimum attributes:

```text
Flow ID
Source
Destination
Amount
Timing
Purpose
Cost
Constraint
Expected Outcome
Actual Outcome
Status
```

# 10. Capital Allocation Object

Minimum attributes:

```text
Allocation ID
Capital Pool
Investment / Portfolio
Current Allocation
Proposed Allocation
Marginal Value
Liquidity Impact
Opportunity Cost
Risk
Option Value
Strategic Weight
Status
```

# 11. Lifecycle

```text
CAPITAL STATE
      ↓
LIQUIDITY ASSESSMENT
      ↓
FUNDING CAPACITY
      ↓
INVESTMENT PIPELINE
      ↓
OPTION VALUATION
      ↓
SEQUENCING
      ↓
CAPITAL ALLOCATION
      ↓
STAGED COMMITMENT
      ↓
DEPLOYMENT
      ↓
VALUE REALISATION
      ↓
CAPITAL RECOVERY
      ↓
RECYCLING
      ↺
```

# 12. Capital Governance

Enterprise capital SHALL be governed as a dynamic enterprise capability rather than as an isolated budgeting process.

# 13. Capital Ownership

Every material capital pool SHALL have an accountable owner.

# 14. Capital Mandate

Every capital pool SHALL have a documented mandate, purpose and allocation boundary.

# 15. Capital Classification

Capital SHALL be classified according to purpose, liquidity, risk and governance characteristics.

# 16. Capital State

Available, reserved, committed, deployed and recoverable capital SHALL be distinguishable.

# 17. Capital Availability

Capital available for new allocation SHALL be continuously or periodically determined.

# 18. Capital Reservations

Strategic and contingency reserves SHALL be visible and protected.

# 19. Capital Commitments

Future commitments SHALL be visible against the capital pool.

# 20. Capital Deployment

Deployment SHALL be traceable to an approved commitment.

# 21. Capital Recovery

Recovered capital SHALL be reconciled into the appropriate capital pool.

# 22. Capital Recycling

Recovered capital SHOULD be assessed for redeployment rather than automatically treated as idle.

# 23. Capital Velocity

Capital velocity SHALL be measured where it materially affects value creation.

# 24. Capital Latency

Time between commitment and value or recovery SHALL be represented.

# 25. Capital Turnover

Capital turnover SHALL be monitored.

# 26. Capital Productivity

Capital productivity SHOULD be compared across portfolios.

# 27. Capital Efficiency

Capital efficiency SHALL not replace outcome effectiveness as the primary objective.

# 28. Capital Effectiveness

Capital effectiveness SHALL be measured against approved outcomes.

# 29. Liquidity Position

Current liquidity SHALL be visible across relevant time horizons.

# 30. Liquidity Forecast

Liquidity SHALL be forecast against expected inflows, outflows and commitments.

# 31. Liquidity Horizon

Liquidity forecasts SHALL specify their horizon.

# 32. Liquidity Buffer

Minimum liquidity buffers SHALL be defined.

# 33. Liquidity Floor

Critical liquidity floors SHALL be protected.

# 34. Liquidity Stress

Approaching liquidity floors SHALL trigger early warning.

# 35. Liquidity Shock

Material liquidity shocks SHALL trigger controlled capital preservation.

# 36. Liquidity Recovery

Recovery paths SHALL be defined for material liquidity stress.

# 37. Liquidity Optionality

Liquidity SHALL be treated as a source of future decision flexibility.

# 38. Funding Capacity

Available and potential funding capacity SHALL be visible.

# 39. Funding Sources

Material funding sources SHALL be represented.

# 40. Funding Cost

Funding cost SHALL be included in capital decisions.

# 41. Funding Windows

Time-limited funding availability SHALL be represented.

# 42. Funding Constraints

Funding constraints SHALL be explicit.

# 43. Funding Diversification

Material dependence on a limited funding source SHALL be monitored.

# 44. Funding Concentration

Funding concentration risk SHALL be measured.

# 45. Funding Resilience

Funding resilience SHALL be stress-tested.

# 46. Cost of Capital

Relevant cost-of-capital assumptions SHALL be explicit.

# 47. Capital Hurdles

Investment hurdles SHALL be governed and documented.

# 48. Return Profiles

Expected return distributions SHALL be represented where meaningful.

# 49. Risk-Adjusted Return

Material capital decisions SHALL consider risk-adjusted return.

# 50. Return Latency

Time to expected return SHALL be included.

# 51. Capital at Risk

Capital exposure to loss SHALL be visible.

# 52. Investment Thesis

Material investments SHALL have explicit investment theses.

# 53. Investment Case

Investment cases SHALL include value, cost, risk, timing, assumptions and dependencies.

# 54. Investment Pipeline

Potential and approved investments SHALL be represented in a common pipeline.

# 55. Investment Backlog

Fundable but currently unfunded investments SHALL be visible.

# 56. Investment Stages

Material investments SHOULD have defined stages.

# 57. Stage Gates

Stage gates SHALL reassess value, risk, liquidity and strategic fit.

# 58. Staged Commitments

Uncertain investments SHOULD use staged commitments where appropriate.

# 59. Tranches

Capital MAY be released in governed tranches.

# 60. Release Conditions

Each tranche SHALL have explicit release conditions.

# 61. Stop Conditions

Material investments SHALL have defined stop conditions.

# 62. Stop-Loss

Material capital exposure MAY use stop-loss governance.

# 63. Abandonment Value

The value of stopping an investment SHALL be considered.

# 64. Real Options

Investment decisions SHALL consider the value of future flexibility where material.

# 65. Expansion Options

Potential future expansion SHALL be represented as an option.

# 66. Contraction Options

Potential reduction of commitment SHALL be represented where relevant.

# 67. Abandonment Options

The ability to stop an investment SHALL have explicit economic value.

# 68. Deferment Options

The value of waiting for additional information SHALL be considered.

# 69. Switching Options

Ability to change investment configuration SHALL be represented.

# 70. Option Premium

The economic cost of preserving an option SHALL be visible.

# 71. Sequencing

Capital commitments SHALL be sequenced to preserve liquidity, optionality and strategic value.

# 72. Investment Sequencing

Investment order SHALL be evaluated rather than assuming simultaneous deployment.

# 73. Capital Priority

Capital priorities SHALL be governed.

# 74. Capital Envelopes

Autonomous capital allocation SHALL operate within explicit envelopes.

# 75. Capital Quotas

Capital concentration limits MAY be established.

# 76. Strategic Reserves

Strategic capital reserves SHALL have explicit purposes.

# 77. Contingency Capital

Contingency capital SHALL be protected against premature deployment.

# 78. Working Capital

Working capital requirements SHALL remain protected from discretionary optimisation.

# 79. Growth Capital

Growth capital SHALL be governed against strategic objectives.

# 80. Maintenance Capital

Maintenance capital SHALL preserve critical existing capability.

# 81. Transformation Capital

Transformation capital SHALL remain linked to approved transformation outcomes.

# 82. Innovation Capital

Innovation capital SHALL accommodate uncertainty without weakening governance.

# 83. Resilience Capital

Resilience capital SHALL reflect continuity and recovery requirements.

# 84. Capital Waterfall

Capital allocation MAY use a governed waterfall for competing claims.

# 85. Capital Cascade

Capital decisions SHALL pass through defined governance stages.

# 86. Capital Gates

Material capital releases SHALL use explicit gates.

# 87. Dynamic Capital Allocation

Capital allocation MAY adapt to changing value, risk, liquidity and strategy.

# 88. Capital Reallocation

Capital MAY be reallocated when marginal value changes materially.

# 89. Capital Rotation

Capital rotation SHALL be governed by explicit triggers.

# 90. Capital Churn

Excessive capital churn SHALL be treated as an economic cost.

# 91. Capital Lock-In

Material capital lock-in SHALL be visible.

# 92. Stranded Capital

Capital with low expected value and limited recoverability SHALL be identified.

# 93. Capital Scarcity

Capital scarcity SHALL be measured.

# 94. Capital Bottlenecks

Capital constraints limiting enterprise outcomes SHALL be visible.

# 95. Capital Queue

Unfunded capital demand SHALL be prioritised in a governed queue.

# 96. Capital Demand

Capital demand SHALL include timing, value, risk and dependencies.

# 97. Capital Supply

Capital supply SHALL include liquidity, funding and reserve constraints.

# 98. Internal Capital Market

An internal capital market MAY be used where allocation across business units or portfolios benefits from market-like mechanisms.

# 99. Capital Bids

Capital requests SHALL contain sufficient economic and strategic information.

# 100. Capital Offers

Available capital SHALL be represented with applicable terms and constraints.

# 101. Capital Clearing

Capital clearing SHALL produce reconstructable allocation decisions.

# 102. Capital Price

Capital pricing assumptions SHALL be explicit.

# 103. Shadow Cost of Capital

Shadow cost MAY be used when capital is materially constrained.

# 104. Liquidity Premium

The value of maintaining liquidity SHALL be recognised.

# 105. Capital Concentration

Capital concentration SHALL be monitored.

# 106. Capital Diversification

Diversification SHALL be considered where it improves resilience or risk-adjusted value.

# 107. Capital Correlation

Correlated investment outcomes SHALL be identified.

# 108. Capital Dependencies

Dependencies between investments SHALL be explicit.

# 109. Capital Complementarity

Complementary investments SHALL be evaluated jointly.

# 110. Capital Cannibalisation

Competing investments SHALL be evaluated for cannibalisation.

# 111. Capital Synergy

Potential synergy SHALL be represented.

# 112. Capital Externalities

Material effects on other enterprise areas SHALL be included.

# 113. Capital Network

Material capital flows and dependencies SHOULD be represented as a network.

# 114. Capital Graph

Capital relationships SHOULD be represented as a graph.

# 115. Capital Flow

Capital movement SHALL be observable.

# 116. Capital Flow Rate

Material capital flow rates SHALL be measurable.

# 117. Capital Flow Constraints

Flow constraints SHALL be visible.

# 118. Capital Flow Bottlenecks

Capital flow bottlenecks SHALL be identified.

# 119. Capital Flow Friction

Transaction and governance friction SHALL be measured where material.

# 120. Capital Recycling

Recovered capital SHALL be evaluated for reuse.

# 121. Reinvestment Rate

Reinvestment of recovered capital SHOULD be measured.

# 122. Deployment Curve

Material investment programmes SHALL have deployment profiles.

# 123. Value Realisation Curve

Expected value timing SHALL be represented.

# 124. Cash Flow Profile

Material investments SHALL model expected cash-flow profiles.

# 125. Liquidity Profile

Capital decisions SHALL show their liquidity impact over time.

# 126. Funding Profile

Funding cost and availability SHALL be represented over time.

# 127. Investment Profile

Investment commitments and releases SHALL be time-aware.

# 128. Capital Scenarios

Material capital decisions SHOULD be evaluated across scenarios.

# 129. Capital Stress Tests

Capital systems SHALL be stress-tested.

# 130. Liquidity Stress Tests

Liquidity SHALL be stress-tested against plausible adverse conditions.

# 131. Funding Stress Tests

Funding resilience SHALL be stress-tested.

# 132. Capital Digital Twin

Material capital systems SHOULD support digital-twin analysis.

# 133. Capital Orchestration

Cross-pool capital decisions SHALL be coordinated by governed orchestration.

# 134. Investment Agents

Investment agents MAY analyse opportunities and investment cases.

# 135. Liquidity Agents

Liquidity agents MAY monitor and forecast liquidity.

# 136. Capital Allocation Agents

Capital allocation agents MAY generate bounded allocation proposals.

# 137. Funding Agents

Funding agents MAY analyse funding alternatives.

# 138. Option Agents

Option agents MAY calculate or compare real-option structures.

# 139. Agent Authority

Analytical capability SHALL not automatically confer authority to commit capital.

# 140. Capital Quorum

High-impact capital decisions MAY require independent evidence or quorum.

# 141. Capital Dissent

Material disagreement about capital assumptions SHALL remain visible.

# 142. Capital Explainability

Material capital allocations SHALL be explainable.

# 143. Capital Provenance

Capital decisions SHALL preserve provenance.

# 144. Capital Audit Trail

Material capital movements SHALL be reconstructable.

# 145. Capital Governance

Capital authority, ownership and decision rights SHALL be explicit.

# 146. Capital Authority

Material capital commitments SHALL require the appropriate authority.

# 147. Liquidity Authority

Changes to protected liquidity positions SHALL require appropriate authority.

# 148. Investment Authority

Investment commitments SHALL have explicit approval authority.

# 149. Capital Guardrails

Capital optimisation SHALL operate within defined guardrails.

# 150. Liquidity Guardrails

Liquidity floors SHALL remain authoritative.

# 151. Funding Guardrails

Funding resilience constraints SHALL remain authoritative.

# 152. Concentration Guardrails

Capital concentration SHALL remain within approved limits.

# 153. Optionality Guardrails

Minimum future decision flexibility SHALL be protected where strategically required.

# 154. Interlock with RG-481

Capital allocation SHALL use the value, opportunity-cost and decision-economics structures established in RG-481.

# 155. Interlock with RG-482

Capital allocation SHALL use resource scarcity, capacity and market intelligence from RG-482.

# 156. Interlock with RG-483

Capital allocation SHALL use value-network effects, marginal value and portfolio optimisation from RG-483.

# 157. Security Interlock

Security constraints established in RG-478–480 SHALL remain authoritative.

# 158. Resilience Interlock

Resilience requirements SHALL constrain capital optimisation.

# 159. Transformation Interlock

Transformation capital SHALL remain aligned with approved strategic transformation objectives.

# 160. Human Governance

Strategic capital allocation and irreversible commitments SHALL retain appropriate human authority.

# 161. AI-Assisted Capital Economics

AI MAY assist with:

```text
Liquidity Forecasting
Funding Analysis
Investment Screening
Investment Sequencing
Real-Option Valuation
Capital Flow Analysis
Capital Scenario Modelling
Capital Stress Testing
Portfolio Rebalancing
Capital Recycling Analysis
``` 

AI SHALL NOT silently:

```text
LOWER LIQUIDITY FLOORS
RELEASE STRATEGIC RESERVES
CHANGE CAPITAL MANDATES
CHANGE INVESTMENT HURDLES
REMOVE STOP CONDITIONS
CREATE CAPITAL AUTHORITY
HIDE FUNDING CONCENTRATION
HIDE LIQUIDITY RISK
CHANGE OPTION GOVERNANCE
OVERRIDE SECURITY OR RESILIENCE CONSTRAINTS
COMMIT IRREVERSIBLE CAPITAL WITHOUT AUTHORITY
```

# 162. AI Explainability

Material AI-assisted capital decisions SHALL preserve assumptions, forecasts, liquidity impact, alternatives, option value, constraints, authority and expected outcomes.

# 163. Automation Boundary

Low-impact capital reallocation MAY be automated inside approved envelopes. Strategic, irreversible, liquidity-critical or high-impact capital decisions SHALL remain governed.

# 164. Manual Fallback

Manual treasury, investment and capital allocation procedures SHALL remain available when capital intelligence services degrade.

# 165. Technology Failure

Failure of capital intelligence SHALL trigger conservative liquidity protection and commitment reconciliation.

# 166. Reconciliation

After restoration:

```text
CAPITAL STATE GAP
      ↓
LIQUIDITY RECONCILIATION
      ↓
COMMITMENT RECONCILIATION
      ↓
FUNDING RECONCILIATION
      ↓
INVESTMENT STATE VALIDATION
      ↓
OPTION VALUE REASSESSMENT
      ↓
SAFE CAPITAL REALLOCATION
```

# 167. Negative Testing

The system SHALL verify:

```text
Unknown capital pool → BLOCK
Unknown authority → BLOCK
Liquidity below floor → BLOCK DISCRETIONARY ALLOCATION
Strategic reserve breach → BLOCK
Funding capacity overstated → LOWER AUTONOMY
Liquidity forecast confidence too low → CONSERVATIVE MODE
Capital commitment exceeds envelope → BLOCK
Investment stop condition breached → STOP / ESCALATE
Stage gate failed → BLOCK NEXT TRANCHE
Capital concentration exceeds limit → BLOCK
Funding concentration excessive → ESCALATE
Capital lock-in excessive → REVIEW
Stranded capital detected → REVIEW
Option value omitted → REVIEW
Opportunity cost omitted → REVIEW
Sunk cost drives continuation → BLOCK / REVIEW
Irreversible commitment without authority → BLOCK
Capital flow reconciliation failure → BLOCK
AI changes capital mandate → BLOCK
AI changes liquidity floor → BLOCK
AI releases strategic reserve → BLOCK
Security constraint conflict → SECURITY PRECEDENCE
Resilience constraint conflict → RESILIENCE PRECEDENCE
Audit evidence missing → BLOCK MATERIAL COMMITMENT
```

# 168. Scenario Testing

Representative scenarios:

```text
Normal capital allocation
Liquidity surplus
Liquidity stress
Liquidity shock
Funding disruption
Funding concentration
Capital scarcity
Capital surplus
Investment pipeline surge
High-value opportunity
Low-confidence opportunity
Staged investment
Stage-gate failure
Investment abandonment
Investment expansion
Investment deferment
Investment switching
Capital lock-in
Stranded capital
Capital rotation
Capital churn
Strategic reserve release
Reserve replenishment
Working-capital pressure
Transformation funding surge
Innovation portfolio uncertainty
Real-option investment
Cross-portfolio capital conflict
Capital market activation
Capital market halt
Capital market recovery
Capital stress scenario
Enterprise disruption
Security constraint activation
Resilience constraint activation
Manual fallback
Capital recovery
Capital recycling
Post-investment learning
```

# 169. Acceptance Criteria

EA-IMETA-PC-RG-484 is accepted when:

- capital pools, classes, mandates and ownership are explicitly represented;
- available, reserved, committed, deployed and recoverable capital are distinguishable;
- liquidity position and liquidity forecasts are visible across relevant horizons;
- liquidity floors and buffers are protected;
- funding sources, capacity, cost and concentration are represented;
- investment pipelines and backlogs are visible;
- investment cases contain value, risk, timing, assumptions and dependencies;
- staged commitments, tranches, release conditions and stop conditions are supported;
- real options including expansion, contraction, abandonment, deferment and switching are represented;
- capital sequencing and dynamic reallocation are supported;
- capital concentration, diversification, correlation and dependency are measurable;
- capital flows, bottlenecks, latency and friction are visible;
- internal capital-market mechanisms can be governed where appropriate;
- capital scenarios and stress testing are supported;
- capital recovery and recycling are integrated into the lifecycle;
- autonomous capital agents have explicit authority boundaries;
- liquidity, security, resilience and strategic guardrails remain authoritative;
- AI cannot silently alter capital mandates, liquidity floors or strategic reserves;
- material capital decisions remain explainable, auditable and appropriately human-governed;
- negative and scenario tests prevent unsafe capital allocation.

# 170. Next Step

> **EA-IMETA-PC-RG-485 — ENTERPRISE CAPITAL-RESOURCE-VALUE EQUILIBRIUM, LIQUIDITY-OPTIONALITY OPTIMISATION, CROSS-MARKET CLEARING & AUTONOMIC ECONOMIC BALANCE ARCHITECTURE**

RG-484 establishes the capital flow layer. RG-485 should integrate capital, resources and value into a governed enterprise economic equilibrium model: simultaneous capital/resource scarcity, liquidity-versus-optionality trade-offs, cross-market clearing, enterprise-wide economic balance and controlled autonomous re-equilibration.

# 171. Governing Principle

> **Capital SHALL be treated as a dynamic enterprise flow: liquidity, funding, investment sequencing, option value, capital concentration and recovery SHALL remain continuously visible, enabling capital to move toward superior enterprise outcomes without sacrificing continuity, resilience, strategic optionality or governance authority.**

# END OF EA-IMETA-PC-RG-484
