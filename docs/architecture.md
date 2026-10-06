# Architecture

## System view

```text
                         ┌──────────────────────┐
                         │   Agent / Robot /    │
                         │   Vehicle action     │
                         └──────────┬───────────┘
                                    │ observed outcome
                                    ▼
                         ┌──────────────────────┐
                         │   Failure Capture    │
                         │ expected vs. actual  │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  Pattern Analysis    │
                         │ cluster + root cause │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Regression Coverage  │
                         │ test + policy change │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Human Accountability │
                         │ review + approval    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     Verification     │
                         │ replay failure set   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     Release Gate     │
                         │ evidence before ship │
                         └──────────────────────┘
```

## Core entities

| Entity | Purpose |
|---|---|
| Failure | Immutable record of an observed mismatch between expected and actual behavior |
| Pattern | Recurring failure class that may warrant a systemic fix |
| Regression Test | Executable evidence that the failure category is handled correctly |
| Proposed Change | Guardrail, workflow, policy, prompt, or code change intended to prevent recurrence |
| Approval | Explicit accountable human decision to apply the proposed change |
| Verification | Evidence that the same failure pattern passes after the change |
| Release Gate | Policy that determines whether the affected workflow may ship |

## Data flow

1. The agent acts.
2. The system captures expected behavior, observed behavior, severity, and context.
3. AI or deterministic analysis proposes a category and likely root cause.
4. Similar failures are clustered into a pattern.
5. The pattern generates durable regression coverage and a proposed change.
6. An accountable reviewer approves, rejects, or edits the change.
7. The regression set is replayed.
8. Evidence is evaluated against the release policy.
9. The workflow is released only when its gate is satisfied.

## Trust boundaries

- **Agent action:** untrusted until evaluated.
- **AI recommendation:** advisory until human approval or an explicitly governed automation policy allows automatic application.
- **Regression evidence:** required before release.
- **Release gate:** policy-controlled decision point.

## Prototype boundary

The current demo uses in-memory state and synthetic failures. A production design would persist events and evidence and integrate with CI/CD, incident systems, telemetry, and access-controlled approval workflows.
