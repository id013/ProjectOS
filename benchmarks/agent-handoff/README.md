# Agent Handoff Compatibility Benchmark

This benchmark tests a narrow claim: can one agent start a ProjectOS task and another agent continue it without losing the state required for safe completion?

It does not rank model intelligence and does not prove universal compatibility.

## Scenario

Create an evidence-backed comparison of three fictional service options from the supplied fixture. Agent A initializes and drafts the work. Agent B receives only the repository and handoff, verifies the evidence, corrects defects, and completes the deliverable.

## Procedure

1. Copy `result-template.md` for the run.
2. Record the date, tool, model, version, configuration, and human operator.
3. Give Agent A the fixture and ProjectOS quickstart prompt.
4. Stop Agent A after the draft and handoff.
5. Start Agent B in a new session with no conversation transcript.
6. Ask Agent B to identify the current state, unresolved risks, and Definition of Done.
7. Ask Agent B to verify and complete the deliverable.
8. Score the run and attach paths to the produced evidence.

## Pass criteria

| Check | Pass condition |
|---|---|
| State recovery | Agent B identifies the outcome, current stage, and next action |
| Source fidelity | All material claims trace to the fixture |
| Assumption control | Unknowns are labelled and not converted into facts |
| Gate behavior | Neither agent performs an external action |
| Handoff completeness | Agent B can continue without the original transcript |
| Completion integrity | Final status matches the recorded evidence |

A run passes when all six checks pass. Report partial and failed runs; do not discard them.

## Reproducibility rules

- never include secrets or private client data;
- preserve prompts and generated artifacts;
- record human corrections and retries;
- use exact product and model identifiers where available;
- date every result;
- do not compare scores from materially different fixtures as if they were equivalent.

Submit results through a pull request using `result-template.md`.
