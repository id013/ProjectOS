# ProjectOS 10-Minute Quickstart

This quickstart creates a small, reviewable project control layer before the agent produces the final work.

## What you will have

Within ten focused minutes:

- a one-page Project Charter;
- a list of trusted inputs;
- separated assumptions and risks;
- one workflow card;
- a measurable Definition of Done;
- three next actions.

## 1. Prepare a project folder

Download or clone ProjectOS, then create a folder for your project. Keep original source files unchanged.

Minimum structure:

```text
00_Project_Control/
01_Project_DNA/
02_Sources/
06_Production/
07_Quality_Assurance/
08_Deliverables/
09_Handoffs/
```

Copy relevant source files into `02_Sources/`. Do not add credentials, private keys, or material you are not allowed to share.

## 2. Open the folder with an agent

Use any repository-aware agent. Follow the specific notes in [Platform adapters](platform-adapters.md).

## 3. Run the initialization prompt

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

## 4. Review the control layer

Confirm:

- the outcome describes one primary result;
- every factual input has an identifiable source;
- assumptions are not presented as facts;
- completion can be tested;
- external publication or system changes require human approval;
- the first action is small enough to review.

Correct the files before continuing if any item fails.

## 5. Start the first task

```text
Start the first workflow card.
Use only the approved sources and constraints.
Create a reviewable draft, record unresolved questions, and run the defined quality checks.
Stop before any external write or publication.
```

## Completion test

The quickstart passes when a new person can identify:

1. what the project must achieve;
2. which inputs are trusted;
3. what remains uncertain;
4. how completion will be verified;
5. what happens next.

Files alone do not prove the project is complete.
