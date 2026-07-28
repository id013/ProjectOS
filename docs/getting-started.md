# Getting Started

ProjectOS separates project memory from conversation history. Use chats and agent runs to execute work; use versioned artifacts to preserve what the project knows.

## Choose an operating mode

| Mode | Use when | Minimum control |
|---|---|---|
| Lite | One short, low-risk deliverable | Charter, sources, task list, human review |
| Standard | Several steps, sources, or outputs | Core registers, handoff, independent QA |
| Advanced | Long-running, public, sensitive, or expensive work | Full audit trail, dependencies, fact-checking, release gate |
| Program | Several connected projects | Shared sources of truth and cross-project change control |

Move up one level when two or more are true: public release, sensitive data, irreversible actions, more than ten sources, more than five workstreams, batch production, multiple owners, or significant legal/financial impact.

## Bootstrap a project

1. Copy the templates into a dedicated project folder.
2. Create a Project Charter and name the owner.
3. List primary sources without modifying the originals.
4. Define the output, constraints, and measurable Definition of Done.
5. Select a workflow card or create one.
6. Record capability maturity and required permissions.
7. Run a small pilot before scaling.
8. Close the stage only after QA and handoff updates.

## Suggested project structure

```text
00_Project_Control/       status, registers, plan, change log
01_Project_DNA/           charter, glossary, voice, quality standard
02_Sources/               immutable originals and metadata
03_Knowledge_Base/        normalized knowledge and maps
04_Research/              evidence and findings
05_Planning/              stages, workflows, dependencies
06_Production/            working drafts
07_Quality_Assurance/     reviews, tests, conflict reports
08_Deliverables/          approved outputs only
09_Handoffs/              context manifests and transfer packs
10_Retrospectives/        lessons and proposed improvements
99_Archive/               superseded and closed versions
```

## First prompt

```text
Initialize this project with ProjectOS in Standard mode.

First, inspect the available sources. Do not produce the final deliverable yet.
Create:
1. a Project Charter draft;
2. a Source of Truth Register;
3. a list of assumptions, risks, and missing inputs;
4. a stage plan;
5. a recommended workflow card for the first outcome;
6. measurable completion criteria.

Separate confirmed facts from assumptions. Flag any external action that requires approval.
```

## Completion rule

Do not call work complete because files exist. Completion requires evidence that the defined outcome, constraints, and verification criteria have been satisfied.

