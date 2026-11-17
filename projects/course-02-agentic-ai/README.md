# Course 2 — Agentic AI: project

The evolving project for Course 2: an incident-response system for the
Meridian Exchange, a fictional stock exchange simulated locally.

It grows in three milestones:

1. First-Line Incident Agent (sessions 1–3)
2. Production On-Call Agent (sessions 4–6)
3. 24/7 Incident Response Center (sessions 7–9)

Start with the [project goals](docs/project.md) and [reference incident](docs/reference-incident.md). Follow the [roadmap](../../ROADMAP.md) for milestone outcomes.

## Design index

Each specification includes a diagram. To refresh the diagrams and offline decision report, install Graphviz and run this command from the repository root:

```sh
python3 projects/course-02-agentic-ai/docs/flows/render.py
```

Open `../meridian-report/index.html`. Edit `docs/flows/flows.dot` to change a diagram and the corresponding specification to change its caption.

- [Architecture and information ownership](docs/architecture.md)
- [Prompts](docs/specs/prompts.md) and [context](docs/specs/context.md)
- [Memory](docs/specs/memory.md) and [caching](docs/specs/caching.md)
- [Evaluation](docs/specs/evaluation.md) and [experiment log](docs/experiments.md)
- [Permissions](docs/specs/permissions.md), [coordination](docs/specs/coordination.md), and [resume](docs/specs/execution.md)
- [Decision log](docs/decisions.md) and [specification template](docs/specs/template.md)

Discuss one incident example before choosing a policy. The owner reviews the contract, then a coding agent implements it. Review both the outcome and the evidence used to reach it.
