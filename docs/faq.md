# Frequently Asked Questions

Direct answers about ProjectOS, how it works, and when to use it.

## What is ProjectOS?

ProjectOS is an open operating system for reliable AI-assisted project work. It turns chats, prompts, files, tools, and agent runs into a durable workflow built around explicit goals, approved sources, versioned decisions, quality gates, permissions, and handoffs.

## What problem does ProjectOS solve?

AI is fast, but long-running work often breaks when context drifts, decisions remain trapped in conversations, sources conflict, or outputs are published without independent review. ProjectOS makes the state of a project inspectable and transferable so work can continue reliably across sessions, people, models, and tools.

## Is ProjectOS a project-management application?

No. ProjectOS is a portable operating layer, not a replacement for an issue tracker, document system, or collaboration platform. It defines how project context, execution, review, and handoffs should work; teams can apply it inside the tools they already use.

## Is ProjectOS a prompt library?

No. Prompts are only one part of execution. ProjectOS also defines sources of truth, decision records, permission boundaries, quality gates, batch controls, completion criteria, and durable handoffs.

## Is ProjectOS an AI agent framework?

ProjectOS does not prescribe a model runtime or agent architecture. It can govern work performed by one assistant, several specialized agents, or a human-and-AI team. Its artifacts remain useful even when the underlying model or platform changes.

## Which AI tools can use ProjectOS?

ProjectOS is designed to be portable across ChatGPT Work, Codex, and other assistants that can read project files and follow written operating rules. The repository includes an installable skill for compatible agent environments.

## When should I use ProjectOS?

Use ProjectOS when work lasts longer than one conversation, depends on several sources, produces many related outputs, involves multiple contributors, or carries publication, financial, legal, security, or reputation risk.

## Is ProjectOS useful for small projects?

Yes. Lite mode keeps the system intentionally small: define the outcome, constraints, approved sources, Definition of Done, and a human review point. More controls are added only when complexity or risk justifies them.

## How does ProjectOS maintain quality at scale?

For batch work, ProjectOS separates shared rules from item-specific context, tests a pilot batch, uses manifests to track every item, validates the entire set mechanically, reviews a risk-based sample, and requires a release decision before publication.

## Does ProjectOS make AI output automatically correct?

No. It reduces preventable failure and makes uncertainty visible, but it does not replace domain expertise, primary evidence, testing, or accountable human approval.

## How are risky actions controlled?

Every workflow should state what the AI may do autonomously, what requires confirmation, and what is prohibited. Publishing, sending messages, spending money, changing production systems, handling sensitive data, and other irreversible actions should have explicit human gates.

## How do I start?

Read the [Getting Started guide](getting-started.md), choose the smallest safe operating mode, copy the relevant [templates](../templates/), and run one well-defined workflow through its Quality Gate.

## Can I contribute my own workflow?

Yes. Contributions should describe the problem, inputs, steps, evidence requirements, permissions, failure modes, Quality Gate, and Definition of Done. Read the [contribution guide](https://github.com/id013/ProjectOS/blob/main/CONTRIBUTING.md) before opening a pull request.

## How is ProjectOS licensed?

The core repository is available under the MIT License. Any vendored third-party material must preserve its original license and provenance.

