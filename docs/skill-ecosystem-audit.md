# Agent Skill Ecosystem Audit

This preliminary admission review examines twenty published skills and workflow components that can inform ProjectOS. It is an architectural assessment, not a security certification or endorsement.

## Method

The review used immutable local snapshots of the source repositories and inspected:

- `SKILL.md` scope and trigger;
- bundled scripts and references;
- platform coupling;
- permission-bearing actions;
- verification behavior;
- maintainability and composition potential;
- repository-level license signals.

No third-party script was executed.

## Decision labels

- **Adopt pattern** — incorporate the underlying method into ProjectOS with attribution where required.
- **Adapter candidate** — useful behind a platform or domain adapter.
- **Reference implementation** — study and link; do not make part of the kernel.
- **Domain skill** — useful for an optional workflow pack.
- **Do not vendor** — avoid copying; use only as research input.

## Reviewed candidates

| # | Source | Skill | Main value | Portability | Risk | Decision |
|---:|---|---|---|---:|---:|---|
| 1 | Anthropic | `skill-creator` | Skill structure, triggering, evaluation, iteration | 5/5 | L2 | Adopt pattern |
| 2 | Anthropic | `mcp-builder` | Tool design and external-service integration | 4/5 | L2-L3 | Adapter candidate |
| 3 | Anthropic | `webapp-testing` | Browser-based functional verification | 3/5 | L2 | Domain skill |
| 4 | Anthropic | `doc-coauthoring` | Context transfer, iterative drafting, reader validation | 5/5 | L1 | Adopt pattern |
| 5 | Anthropic | `frontend-design` | Intentional visual direction and anti-template heuristics | 5/5 | L1 | Domain skill |
| 6 | Superpowers | `brainstorming` | Intent and design before implementation | 5/5 | L0 | Adopt pattern |
| 7 | Superpowers | `writing-plans` | Small, verifiable implementation steps | 4/5 | L0 | Adopt pattern |
| 8 | Superpowers | `executing-plans` | Checkpointed execution against an approved plan | 4/5 | L1-L2 | Adopt pattern |
| 9 | Superpowers | `verification-before-completion` | Evidence before completion claims | 5/5 | L0 | Adopt pattern |
| 10 | Superpowers | `systematic-debugging` | Root-cause analysis before fixes | 4/5 | L1-L2 | Adopt pattern |
| 11 | Superpowers | `test-driven-development` | Red-green-refactor discipline | 3/5 | L1-L2 | Domain skill |
| 12 | Superpowers | `requesting-code-review` | Independent review before integration | 4/5 | L1 | Adopt pattern |
| 13 | Superpowers | `receiving-code-review` | Verify feedback rather than accepting blindly | 5/5 | L0 | Adopt pattern |
| 14 | Superpowers | `writing-skills` | Test-first skill authoring | 4/5 | L2 | Reference implementation |
| 15 | OpenAI plugin | `agents-sdk` | Runnable agents, local eval harness, deployment separation | 2/5 | L2-L3 | Platform adapter |
| 16 | OpenAI plugin | `github` | Connector-first repository orientation | 2/5 | L1-L3 | Platform adapter |
| 17 | OpenAI plugin | `gh-fix-ci` | Evidence-based CI diagnosis and scoped fixes | 2/5 | L2 | Domain skill |
| 18 | OpenAI plugin | `huggingface-community-evals` | Reproducible model evaluation on local hardware | 2/5 | L2 | Reference implementation |
| 19 | OpenAI plugin | `cite-check` | Claim-level source and quotation validation | 2/5 | L2-L4 | Domain skill |
| 20 | OpenAI plugin | `document-quality-check` | Structured document QA | 2/5 | L1-L3 | Domain skill |

## Findings

### Strongest kernel patterns

The most universal patterns are:

1. clarify intent before execution;
2. use a written, reviewable plan;
3. separate execution from independent verification;
4. require fresh evidence before declaring completion;
5. preserve state and handoff artifacts;
6. test skills and workflow changes against representative cases;
7. verify feedback before incorporating it;
8. keep platform-specific commands outside the kernel.

### What should remain outside the kernel

The following belong in adapters or workflow packs:

- SDK and deployment commands;
- browser automation details;
- GitHub-specific connector behavior;
- local GPU model evaluation;
- legal citation checking;
- document-platform automation;
- strict software TDD rules for non-software projects.

### Main ecosystem risks

- Moving-branch installation without pinning.
- Skills that contain scripts but lack explicit permission contracts.
- Vendor-specific tools embedded in otherwise portable workflows.
- Broad trigger descriptions that activate too often.
- A skill grading its own output.
- Catalog entries treated as verified packages.
- Missing or incompatible licenses at the skill level.
- Hidden expansion of scope through linked web instructions.
- Automatic dependency installation or external writes.

## Source policy

Use sources in this order:

1. official model or tool vendor;
2. open standard or foundation;
3. mature project with tests, releases, license, and active maintenance;
4. curated catalog for discovery only;
5. community repository after full admission review.

Stars and forks help measure attention, not safety or fitness.

## Initial conclusion

ProjectOS should not become a bundle of hundreds of copied skills. Its durable advantage should be a trusted skill supply chain:

```text
Discover
→ quarantine
→ inspect
→ classify permissions
→ test
→ compare
→ approve for a bounded scope
→ monitor
→ update or roll back
```

The next audit stage should add executable conformance cases and lock approved candidates to exact commits.
