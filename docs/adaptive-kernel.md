# Adaptive, Model-Agnostic Kernel

ProjectOS is designed to remain useful when models, tools, and agent platforms change. It achieves this through stable contracts and controlled evolution, not by allowing a model to rewrite production rules autonomously.

## Design principle

> Keep intent, evidence, state, permissions, and evaluation stable. Treat models, tools, and skills as replaceable adapters.

## System layers

```text
Project intent and governance
        ↓
ProjectOS stable kernel
        ↓
Capability negotiation
        ↓
Model, tool, and skill adapters
        ↓
Sandboxed execution
        ↓
Independent evaluation
        ↓
Durable evidence and memory
        ↓
Controlled improvement pipeline
```

### Layer 1: Stable kernel

The kernel defines portable behavior:

- Goal Contract and Definition of Done;
- Sources of Truth and evidence policy;
- Context Manifest;
- Decision and risk records;
- permission boundaries;
- Quality Gate;
- handoff and resume protocol;
- change control and rollback.

The kernel must not depend on model-specific prompt syntax.

### Layer 2: Capability negotiation

Before selecting a workflow, inspect the environment:

```yaml
model:
context_capacity:
modalities:
available_tools:
available_resources:
available_skills:
filesystem_roots:
network_policy:
approval_policy:
persistence:
parallelism:
cost_and_time_limits:
```

Unknown capability means unavailable until verified.

### Layer 3: Adapters

Adapters translate ProjectOS contracts into a host environment.

```yaml
adapter_id:
platform:
model_family:
supported_contract_version:
capabilities:
limitations:
tool_mapping:
approval_mapping:
state_mapping:
verification_commands:
```

Adapters may optimize execution but cannot weaken kernel permissions or completion criteria.

### Layer 4: Skills

Skills provide bounded procedural knowledge. They are selected by applicability, risk, evaluation history, and available capabilities. Skills are dependencies, not authorities.

### Layer 5: Durable memory

Project memory is a set of inspectable artifacts:

| Memory class | Contents | Update rule |
|---|---|---|
| Evidence | Sources, observations, test results | Append with provenance |
| Decisions | Accepted choices and rationale | Versioned change record |
| State | Current work, blockers, ownership | Updated at checkpoints |
| Lessons | Reusable patterns from verified outcomes | Promotion required |
| Models | Capability and benchmark results | Replaceable profile |
| Skills | Versions, permissions, eval history | Admission process |

Conversation history may help execution but is not authoritative project memory.

## Two independent loops

### Execution loop

```text
Understand
→ select workflow
→ assemble context
→ execute
→ verify
→ approve
→ update state
→ hand off
```

### Evolution loop

```text
Observe a failure or opportunity
→ create a structured lesson
→ propose a candidate change
→ review provenance and risk
→ test in isolation
→ run regression and cross-model evals
→ compare with the current version
→ approve or reject
→ release with rollback
→ monitor
```

The producing model cannot unilaterally approve its own kernel change.

## Learning record

```yaml
lesson_id:
observed_in:
failure_or_opportunity:
evidence:
root_cause:
scope:
candidate_change:
affected_contracts:
new_tests:
evaluation_results:
review_decision:
released_version:
rollback_target:
```

Raw feedback is not a lesson. A lesson becomes reusable only after evidence, scope, and regression testing are complete.

## Cross-model evaluation

When a new model or major model version appears:

1. Register a provisional adapter.
2. Run the ProjectOS conformance suite.
3. Run representative workflow cases.
4. Measure outcome quality, evidence use, tool behavior, approvals, recovery, cost, and latency.
5. Identify model-specific strengths and failure modes.
6. Update only the adapter unless the evidence reveals a kernel defect.
7. Publish the compatibility result.

This prevents one model's habits from leaking into the universal kernel.

## Conformance suite

Every supported adapter should demonstrate:

- correct reading of project instructions;
- source precedence;
- context reconstruction after a fresh session;
- safe refusal of unavailable or prohibited actions;
- permission escalation at the correct moment;
- deterministic template completion;
- recovery after an interrupted workflow;
- independent Quality Gate behavior;
- handoff to another model;
- reproducible reporting of evidence and uncertainty.

## Safe autonomy

ProjectOS may automate discovery, classification, testing, comparison, and draft improvement proposals. Promotion, external publication, destructive changes, sensitive-data access, and kernel releases remain governed actions.

The target is an evidence-driven self-improving system, not an uncontrolled self-modifying agent.
