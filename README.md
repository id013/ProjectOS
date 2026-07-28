# ProjectOS

**Keep complex AI projects reliable after the chat ends.**

ProjectOS is an open, model-agnostic operating system for multi-step AI-assisted work. It turns scattered chats, prompts, files, and agent runs into durable project memory with sources of truth, quality gates, handoffs, permissions, and verifiable completion.

> **Status:** Public Review · **Version:** 1.3.0-rc2 · **License:** MIT

## Try it in 10 minutes

You do not need to learn the whole system first.

1. Download or clone this repository.
2. Open the folder in your AI coding or work agent.
3. Copy the prompt below into a new session.
4. Answer the agent's questions.
5. Review the charter and first workflow card it creates.

```text
Use the ProjectOS instructions in this repository.

Initialize a new project in Lite mode for this outcome:
[describe one result you want]

Create only:
1. a concise Project Charter;
2. a Source of Truth list;
3. assumptions, risks, and missing inputs;
4. one workflow card with a measurable Definition of Done;
5. the next three actions.

Do not produce the final deliverable yet. Do not perform external actions.
Separate confirmed facts from assumptions and ask only questions that block progress.
```

**Success after 10 minutes:** you have a reviewable project brief, trusted inputs, explicit completion criteria, and a safe next action—stored as files rather than trapped in a conversation.

[Run the full quickstart](docs/quickstart.md) · [Choose a starter pack](starter-packs/) · [Set up your agent](docs/platform-adapters.md)

## Why ProjectOS?

AI can create useful work quickly. Projects still break when decisions stay inside chats, context drifts, sources conflict, batch output becomes generic, or an agent acts externally without review.

ProjectOS adds the operating layer:

- **Durable context** — project knowledge lives in versioned artifacts, not chat memory.
- **Reviewable execution** — every substantial task has one outcome and a Definition of Done.
- **Source-of-truth control** — facts, assumptions, decisions, and risks stay separate.
- **Quality at scale** — validate a template, run a pilot, then produce and sample the batch.
- **Safe actions** — human gates protect publishing, sending, payments, and irreversible changes.
- **Portable handoffs** — continue with another person, model, chat, or tool without starting over.

## Choose a starter pack

| Starter pack | Use it to produce |
|---|---|
| [Website & SEO](starter-packs/website-seo.md) | Audits, site architecture, service pages, editorial programs, and release QA |
| [Software Product](starter-packs/software-product.md) | Product changes with requirements, implementation, tests, review, and release notes |
| [Research & Content](starter-packs/research-content.md) | Evidence-backed research and controlled content production |

Each pack defines the first inputs, workflow, gates, deliverables, and a ready-to-use initialization prompt.

## Works across agents

The core is plain Markdown and folders. Platform adapters explain how to load the same operating rules in:

- OpenAI Codex and ChatGPT workspaces;
- Claude Code;
- Gemini CLI;
- Cursor and other repository-aware agents.

Adapters may change. Project memory and completion rules do not. See [Platform adapters](docs/platform-adapters.md).

## The core loop

```text
Goal
  → Charter and trusted sources
  → Workflow card and context manifest
  → Focused execution
  → Independent quality gate
  → Approved deliverable
  → Updated registers and handoff
  → Retrospective and controlled improvement
```

Chats are execution sessions. Project artifacts are memory. Approved sources are stronger than conversation history.

## Operating modes

| Mode | Best for | Minimum control |
|---|---|---|
| **Lite** | Short, low-risk work with one deliverable | Charter, trusted inputs, self-check, human review before publication |
| **Standard** | Multi-step projects with several sources or outputs | Core registers, handoff, independent review |
| **Advanced** | Long-running, regulated, expensive, or reputation-sensitive work | Full audit trail, dependencies, fact-checking, release gate |
| **Program** | Several connected projects | Shared sources of truth and cross-project change control |

Start with the smallest mode that safely fits the work.

## Verify portability

ProjectOS includes a [compatibility benchmark](benchmarks/agent-handoff/) for testing whether two different agents can start, transfer, verify, and complete the same project without losing important state.

The benchmark records evidence instead of claiming universal compatibility. Results should name the tools, versions, date, prompts, failures, and human interventions.

## Explore

- [10-minute quickstart](docs/quickstart.md)
- [Documentation hub](docs/README.md)
- [Workflow catalog](docs/workflow-catalog.md)
- [Templates](templates/)
- [Anonymized website and SEO program](examples/website-seo-program.md)
- [Installable ProjectOS skill](skills/projectos/SKILL.md)
- [Skill admission standard](docs/skill-admission-standard.md)
- [Roadmap](ROADMAP.md)

## What ProjectOS is not

ProjectOS is not a promise of autonomous correctness, a replacement for subject-matter review, or proof that every model behaves the same. It is a practical system for making AI-assisted work easier to inspect, transfer, repeat, and improve.

## Help ProjectOS earn trust

ProjectOS is in Public Review. The most valuable contributions are:

- run the quickstart and report where you became confused;
- publish an anonymized case with evidence and limitations;
- submit a dated compatibility benchmark result;
- improve an adapter or starter pack;
- contribute a tested workflow card.

Read [CONTRIBUTING.md](CONTRIBUTING.md), open an issue, or start a GitHub Discussion.

## License

ProjectOS is released under the MIT License. Vendored skills retain their own licenses and provenance notices.

---

**Build AI workflows that remain reliable after the chat ends.**
