# Batch Production

Batch production amplifies both quality and error. Never scale an unvalidated template.

## Pipeline

```text
Inventory → Normalize → Segment → Template → Pilot → Gate
          → Batch → Automated checks → Sample QA → Release
```

## Batch Manifest

For every item record:

- stable ID and target URL/path;
- audience and intent;
- source inputs;
- template version;
- required unique fields;
- owner and status;
- automated checks;
- reviewer result;
- release version.

## Scale gates

1. Validate the source schema.
2. Produce a small, representative pilot.
3. Review the pilot manually.
4. Freeze the template version.
5. Run deterministic checks on every item.
6. Sample across risk groups, not only at random.
7. Stop the batch when the failure threshold is exceeded.
8. Release only approved items.

## Sample strategy

Always include:

- highest-risk items;
- items with missing or unusual inputs;
- each major segment or template variant;
- newly introduced logic;
- a random remainder.

## Content-specific checks

- unique purpose and useful information;
- no fabricated facts, testimonials, or statistics;
- correct titles, headings, canonicals, and internal links;
- claim preservation after editing;
- natural language without generic filler;
- clear user next action.

