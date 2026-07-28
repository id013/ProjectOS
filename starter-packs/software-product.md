# Starter Pack: Software Product

Use this pack for a feature, bug fix, integration, migration, or release.

## Required inputs

- repository and current branch state;
- problem statement and affected users;
- expected behavior and constraints;
- architecture and dependency sources;
- test, security, compatibility, and release requirements.

## Workflow

1. reproduce or define the problem;
2. identify sources of truth and affected surfaces;
3. write acceptance criteria and a rollback path;
4. implement the smallest coherent change;
5. run proportional tests and security checks;
6. perform independent review;
7. prepare a diff, handoff, and release notes.

## Gates

- **Scope Gate:** one primary outcome and explicit non-goals.
- **Implementation Gate:** tests cover the changed behavior.
- **Review Gate:** important changes receive a second-pass review.
- **Release Gate:** compatibility, migration, monitoring, and rollback are documented.

## Initialization prompt

```text
Initialize the Software Product starter pack in Standard mode.
Inspect the repository before proposing implementation.
Create a charter, reproduction or behavior baseline, affected-component map,
acceptance criteria, risk register, test plan, rollback plan, and first workflow card.
Do not change external systems or publish a release.
```
