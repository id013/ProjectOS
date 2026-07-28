# Architecture

ProjectOS has four layers.

## 1. Governance

Defines ownership, decision rights, approval boundaries, risk, status, and change control.

Core artifacts:

- Project Charter;
- Source of Truth Register;
- Decision Log;
- Assumption and Risk Register;
- Capability and Permission Register;
- Change Log.

## 2. Context

Supplies the minimum sufficient information for one focused outcome.

Core artifacts:

- Project DNA;
- glossary;
- knowledge map;
- workflow card;
- Context Manifest;
- Handoff Pack.

## 3. Execution

Turns a defined outcome into reviewable work.

```text
Intake → Plan → Pilot → Produce → Review → Approve → Release
```

Each execution session has one primary outcome. Independent tasks may run in parallel only when they do not write to the same source or depend on unresolved shared decisions.

## 4. Assurance

Tests correctness, evidence, usability, safety, and release readiness.

Assurance combines:

- deterministic checks;
- fact and source review;
- domain-specific QA;
- sample review for batches;
- independent critique;
- human approval for consequential actions.

## Invariants

1. An approved source is stronger than chat history.
2. A fact without a source and date is unverified.
3. An assumption is never presented as a fact.
4. Approved artifacts are not silently overwritten.
5. The creator of a material output is not its only reviewer.
6. External, paid, public, legal, or irreversible actions require explicit approval.
7. A source change triggers review of dependent artifacts.
8. Product capabilities are verified before becoming workflow dependencies.

