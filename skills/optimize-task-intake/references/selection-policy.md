# External skill selection policy

## Hard gates

Reject a candidate when any item is missing or unacceptable:

1. Direct relevance to the acceptance test.
2. Clear compatible license.
3. Inspectable source and referenced instructions.
4. Pinned commit or immutable release.
5. No unexplained executable, credential, persistence, deletion, messaging, or publishing behavior.
6. Validation and rollback paths.

## Weighted score

Score only candidates that pass every hard gate.

| Dimension | Weight | Evidence |
|---|---:|---|
| Task fit | 30 | Covers the exact deliverable and tools |
| Source trust | 20 | Official or known maintainer; clear provenance |
| Security and permission fit | 15 | Minimal authority and inspectable actions |
| Maintenance | 10 | Recent meaningful commits, releases, and issue handling |
| Validation quality | 10 | Tests, examples, and deterministic checks |
| Token and latency efficiency | 10 | Concise skill, scripts, and progressive disclosure |
| Adoption signal | 5 | Stars, forks, dependents, and independent references |

Select at 75 or above. Treat 60–74 as an isolated experiment. Reject below 60.

## Popularity rules

- Never use a universal minimum star count.
- For community repositories, prefer at least 100 stars or strong independent adoption evidence.
- Allow fewer stars for official vendor repositories, narrow expert tools, or new projects with strong tests and provenance.
- Reject artificial star growth, copied collections, mass-generated skills, stale forks, and repositories whose popularity belongs to unrelated content.
- Evaluate the candidate skill directory, not only repository-level popularity.

## Stop rules

Stop discovery when a passing candidate clearly dominates, the budget is exhausted, repeated queries return the same weak candidates, built-in capability already passes the acceptance test faster, or inspection cost exceeds expected savings.

Record repository URL, owner, commit, access date, license, relevant path, inventory, hashes, network and write behavior, validation output, permissions, and rollback. Re-review every update.
