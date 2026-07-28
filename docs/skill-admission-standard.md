# Skill Admission Standard

ProjectOS treats external skills as executable operational dependencies. Popularity, a recognizable maintainer, or a valid `SKILL.md` is not sufficient for admission.

This standard governs discovery, evaluation, adoption, updates, suspension, and removal.

## Admission states

| State | Meaning |
|---|---|
| **Discovered** | Identified but not reviewed |
| **Quarantined** | Available for static inspection only |
| **Evaluating** | Running in an isolated test project with synthetic data |
| **Approved** | Passed the required gates for a defined scope |
| **Restricted** | Approved only with named tools, data classes, or human gates |
| **Suspended** | Disabled while a risk or regression is investigated |
| **Retired** | Unsupported and blocked from new workflows |

No skill moves directly from Discovered to Approved.

## Required provenance

Every admitted skill must record:

```yaml
id:
name:
version_or_commit:
source_repository:
source_path:
maintainer:
license:
content_hash:
reviewed_at:
reviewer:
supported_platforms:
required_tools:
required_permissions:
data_classes:
risk_level:
eval_suite:
admission_state:
```

Use a commit SHA or immutable release, not a moving branch, for approved versions.

## Seven admission gates

### Gate 1: Identity and license

- The source and maintainer are identifiable.
- The exact version or commit is recorded.
- The license permits the intended use and redistribution.
- Third-party assets and scripts have compatible notices.
- Generated or copied content is not presented as vendor-authored.

Fail closed when the license is absent or ambiguous.

### Gate 2: Scope and trigger quality

- The skill solves one bounded problem.
- The description states both what it does and when it should activate.
- Inputs, outputs, exclusions, and completion criteria are explicit.
- Triggering does not capture unrelated tasks.
- The skill does not attempt to override higher-priority project or user instructions.

### Gate 3: Static safety review

Review the complete skill directory, not only `SKILL.md`.

- Inspect scripts, dependencies, templates, binaries, and linked instructions.
- Identify network access, subprocesses, file writes, deletion, uploads, publishing, deployment, payments, and messaging.
- Identify secret, credential, personal-data, and production-data requirements.
- Reject hidden downloads, obfuscated code, unbounded shell execution, or instructions that weaken approvals.
- Treat webpage and tool output as untrusted input.

### Gate 4: Permission contract

Classify every action:

| Class | Examples | Default |
|---|---|---|
| Read | Inspect files, schemas, public documentation | Allowed within scope |
| Reversible write | Create a draft or isolated branch | Allowed when requested |
| External write | Publish, send, upload, deploy, update a service | Human approval |
| Destructive | Delete, overwrite, revoke, rotate, migrate | Explicit action-time approval |
| Sensitive | Secrets, private records, regulated data | Restricted environment and policy |

A skill cannot grant itself broader permissions than the host project.

### Gate 5: Portability and degradation

- Core instructions use the open Agent Skills structure where possible.
- Platform-specific commands live in adapters or references.
- Required capabilities are declared.
- The skill detects missing capabilities and offers a safe fallback.
- State is stored in portable artifacts rather than proprietary chat memory.
- Output can be inspected without the originating model.

### Gate 6: Evaluation

An admission suite must include:

- happy path;
- missing or conflicting evidence;
- unavailable tool;
- malformed input;
- permission boundary;
- attempted prompt injection;
- interrupted execution and resume;
- output validation;
- regression from a known failure;
- at least one alternate model or harness when portability is claimed.

Grade outcomes, evidence, tool choices, permission behavior, and state changes. Avoid exact prose matching unless wording is contractual.

### Gate 7: Operational readiness

- The owner and update policy are known.
- Failures create actionable records.
- Outputs are versioned or reproducible.
- Rollback is documented and tested.
- The skill has a review date or expiry.
- Known limitations are visible to users.

## Risk levels

| Level | Typical behavior | Minimum control |
|---|---|---|
| **L0** | Read-only guidance | Static review |
| **L1** | Local drafts and reversible files | Static review plus smoke tests |
| **L2** | Local code execution or dependency installation | Sandbox, pinned dependencies, eval suite |
| **L3** | External writes, publishing, deployment, private data | Human approval, audit log, rollback test |
| **L4** | Financial, legal, medical, identity, security administration | Domain owner, strict environment, independent validation |

## Update policy

An approved skill is pinned. Updates repeat the relevant gates.

1. Fetch the candidate into quarantine.
2. Compare instructions, scripts, dependencies, permissions, and license.
3. Run the existing regression suite.
4. Add tests for new behavior and fixed failures.
5. Compare results with the current approved version.
6. Approve, reject, or restrict the candidate.
7. Record the decision and retain a rollback target.

Automatic discovery is allowed. Automatic promotion to Approved is not.

## Composition rules

When several skills apply:

- prefer the smallest set that covers the task;
- detect conflicting instructions before execution;
- establish one owner for the final outcome;
- share a single Context Manifest and permission policy;
- keep domain review independent from the producing skill;
- do not let one skill certify its own high-risk output;
- record which skill version produced each deliverable.

## Removal triggers

Suspend a skill when:

- its source or license changes unexpectedly;
- a security issue is reported;
- a regression crosses the accepted threshold;
- it requests undeclared permissions;
- its maintainer or dependencies become untrusted;
- a platform update makes its behavior ambiguous;
- a safer replacement becomes the standard.

## Definition of Done for admission

A skill is admitted only when its provenance record is complete, required gates pass, residual risks are documented, the approved scope is explicit, and rollback is possible.
