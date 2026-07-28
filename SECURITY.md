# Security Policy

ProjectOS is a methodology and template system, not a security guarantee.

## Reporting a vulnerability

Do not publish credentials, personal data, customer information, or exploitable details in a public issue.

Until a dedicated private reporting channel is available, contact the repository owner through a private method listed on the GitHub profile. Include:

- the affected file or workflow;
- the potential impact;
- a safe reproduction that uses no real secrets;
- a suggested mitigation when available.

## Operating principles

Before any external write, message, publication, payment, or irreversible action:

- use the minimum required permissions;
- verify the destination and intended change;
- inspect the diff or payload;
- classify and minimize data;
- require human approval when risk is material;
- preserve an audit trail and rollback path.

Never store real secrets in ProjectOS templates or examples.
