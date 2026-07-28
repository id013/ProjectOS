# ProjectOS

**The open operating system for reliable AI-assisted work.**

ProjectOS turns scattered chats, prompts, files, and agent runs into a durable project workflow with explicit context, sources of truth, quality gates, handoffs, permissions, and verifiable completion criteria.

> **Status:** Public Review · **Version:** 1.3.0-rc2 · **License:** MIT

## Why ProjectOS?

AI can produce useful work quickly. Long-running projects still fail when decisions stay inside chats, context drifts, sources conflict, batch output becomes generic, or external actions happen without review.

ProjectOS gives teams a portable operating layer that works across ChatGPT Work, Codex, and other AI agents:

- **Durable context** — project knowledge lives in versioned artifacts, not chat memory.
- **Reviewable execution** — every substantial task has an outcome, constraints, and Definition of Done.
- **Source-of-truth control** — facts, assumptions, decisions, and risks stay separate.
- **Quality at scale** — batch manifests, pilot runs, sampling, and independent QA reduce silent failure.
- **Safe actions** — permission levels and human gates protect publishing, sending, payments, and irreversible changes.
- **Portable handoffs** — move work between people, models, chats, and tools without starting over.

## The core loop

```text
Goal
  → Project Charter and Project DNA
  → Sources of Truth
  → Workflow Card and Context Manifest
  → Execution
  → Independent Quality Gate
  → Approved Deliverable
  → Updated Registries and Handoff
  → Retrospective and Controlled Improvement
```

Chats are execution sessions. Project artifacts are memory. Approved sources are stronger than conversation history.

## Who it is for

ProjectOS is designed for:

- founders and operators running AI-assisted projects;
- agencies producing research, websites, SEO programs, and content at scale;
- product, marketing, operations, and knowledge-work teams;
- AI leads who need repeatable workflows, governance, and auditability;
- contributors building reusable agent skills and playbooks.

## Example workflows

- redesign a website and SEO architecture;
- produce service and editorial pages in controlled batches;
- run customer and competitor research;
- create reports, strategy documents, spreadsheets, and presentations;
- coordinate long-running technical or operational work;
- package repeatable processes as agent skills.

## Operating modes

| Mode | Best for | Required control |
|---|---|---|
| **Lite** | Short, low-risk work with one deliverable | Self-check plus human review before publication |
| **Standard** | Multi-step projects with several sources or outputs | Core registries and an independent reviewer |
| **Advanced** | Long-running, regulated, expensive, or reputation-sensitive work | Full audit trail, dependencies, fact-checking, and release gate |
| **Program** | Several connected projects | Shared sources of truth and cross-project change control |

Start with the smallest mode that safely fits the work. Increase control when scale, external publication, sensitive data, or irreversible actions raise the risk.

## Quick start

1. Open this repository as a local project or ChatGPT/Codex workspace.
2. Read `AGENTS.md` for the durable operating rules.
3. Choose a workflow from the catalog.
4. Define the outcome, constraints, sources of truth, and Definition of Done.
5. Run one focused task per primary outcome.
6. Complete the Quality Gate before publishing or changing external systems.
7. Update the project registers and handoff before closing the task.

## Repository structure

```text
AGENTS.md                 Durable instructions for AI agents
README.md                 Product overview and quick start
docs/                     Architecture, lifecycle, workflows, QA, and examples
templates/                Project artifacts, workflow cards, and handoffs
checklists/               Domain-specific quality checks
skills/                   Reusable and vendored agent skills
.agents/                  Shared product and marketing context
```

## What ProjectOS is not

ProjectOS is not a promise of fully autonomous work, a replacement for subject-matter review, or a guarantee that every AI output is correct. It is a practical system for making AI-assisted work easier to inspect, transfer, repeat, and improve.

## Roadmap

- publish the complete English documentation set;
- release an installable ProjectOS skill;
- add complete public case studies;
- add automated repository validation;
- build workflow packs for website/SEO, research, content operations, and technical delivery;
- establish a stable release after public pilots.

## Contributing

ProjectOS is in Public Review. Useful contributions include:

- tested workflow cards;
- public case studies with measurable outcomes;
- clearer templates and quality gates;
- portability improvements across AI agents;
- corrections backed by primary evidence.

Please read `CONTRIBUTING.md` and `SECURITY.md` before submitting changes.

## License

ProjectOS is released under the MIT License. Vendored skills retain their own license and provenance notices.

---

**Build AI workflows that remain reliable after the chat ends.**
