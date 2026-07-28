# Platform Adapters

ProjectOS keeps its core portable by storing instructions and state in ordinary files. An adapter only tells a specific agent where to read those files and where to write results.

## Shared contract

Every adapter must:

1. load `AGENTS.md` and the selected workflow before substantial work;
2. treat approved project files as stronger than chat history;
3. separate facts, assumptions, proposals, and decisions;
4. stop before external or irreversible actions without approval;
5. update the handoff before declaring completion.

## OpenAI Codex

Open the repository as the workspace. Codex reads `AGENTS.md` as durable repository guidance. Start with the prompt in [Quickstart](quickstart.md).

Recommended layout:

```text
AGENTS.md
00_Project_Control/
01_Project_DNA/
02_Sources/
```

Use a separate task for each primary outcome. Review diffs before allowing publication or other external writes.

## ChatGPT workspace

Attach or connect the ProjectOS repository and the project sources. Tell ChatGPT which file is the current Source of Truth and ask it to return updated artifacts as files.

Do not rely on conversation memory as the only project record. Copy approved decisions and handoffs back into the project.

## Claude Code

Keep `AGENTS.md` as the canonical cross-platform contract. If your setup expects `CLAUDE.md`, create a small pointer rather than duplicating the operating system:

```markdown
# Project instructions

Read and follow `AGENTS.md`.
Use the selected workflow in `docs/workflow-catalog.md`.
Preserve ProjectOS gates, sources of truth, and handoff rules.
```

Verify how the installed Claude Code version discovers instructions before relying on automatic loading.

## Gemini CLI

Keep `AGENTS.md` canonical. If the installed version uses `GEMINI.md`, use a pointer:

```markdown
# Project instructions

Read and follow `AGENTS.md`.
Treat approved project artifacts as stronger than conversation history.
Stop before external actions unless a human approves them.
```

Record the Gemini CLI version in benchmark results because instruction-loading behavior can change.

## Cursor and similar editors

Add a short repository rule that points to `AGENTS.md`; do not maintain a second copy of the full methodology. Ask the agent to name the workflow card and Definition of Done before editing.

The exact rule location depends on the editor version. Confirm the current product documentation and test instruction loading with a harmless task.

## Adapter acceptance test

An adapter passes only if the agent can:

- identify the requested outcome and mode;
- find the approved sources;
- distinguish facts from assumptions;
- stop at the publication gate;
- write a usable handoff for another agent.

Use the [agent handoff benchmark](../benchmarks/agent-handoff/README.md) to record evidence.
