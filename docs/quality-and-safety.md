# Quality and Safety

## Universal Quality Gate

Evaluate every material deliverable across the relevant dimensions:

1. objective and audience fit;
2. factual accuracy;
3. source quality and freshness;
4. logical consistency;
5. completeness against requirements;
6. usability and accessibility;
7. domain correctness;
8. privacy and data minimization;
9. security and permissions;
10. legal and policy constraints;
11. operational readiness;
12. release and rollback readiness.

Record each check as pass, fail, not applicable, or blocked. “Looks good” is not evidence.

## Permission levels

| Level | Meaning |
|---|---|
| Read only | Analyze without changes |
| Workspace write | Change files inside the approved project |
| External read | Retrieve approved external information |
| External write | Modify a connected external system |
| Publish / irreversible | Publish, send, pay, delete, or perform a hard-to-reverse action |

Permission to use a tool does not equal business authorization to use all accessible data.

## Capability maturity

| Maturity | Guidance |
|---|---|
| Under development | Do not depend on it |
| Experimental | Isolated tests only |
| Beta | Pilots and non-critical production with fallback |
| Stable | Production use after ordinary gates |
| Unknown | Verify before use |

## Release Gate

- version and date are fixed;
- links, formatting, and secrets are checked;
- licenses and provenance are reviewed;
- claims match evidence;
- required human approvals are recorded;
- limitations and rollback are documented;
- the published snapshot matches the reviewed snapshot.

