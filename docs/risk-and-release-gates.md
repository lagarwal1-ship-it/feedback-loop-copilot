# Risk and Release Gates

The release gate should be proportional to the consequence of failure.

| Severity | Example | Minimum response | Release behavior |
|---|---|---|---|
| P0 | Safety event, material financial loss, unauthorized irreversible action | Immediate incident response; deterministic control; root-cause review | **Immediate block** for affected workflow |
| P1 | Policy violation, repeated high-impact quality failure | Owner + regression test + approved fix + verification | **Block affected workflow** until evidence is green |
| P2 | Quality degradation, recoverable UX issue | Owner + test or monitoring + SLA | Ship only with explicit risk acceptance |
| P3 | Low-impact cosmetic / non-critical issue | Track and prioritize | Usually does not block release |

## Gate rules

A release gate should be machine-checkable where possible.

### Block release when

- a new P0 or P1 failure is unresolved;
- an approved regression test is failing;
- required approval evidence is missing;
- a known failure category has no owner;
- verification does not cover the affected workflow.

### Allow release when

- required high-severity patterns are fixed;
- regression tests pass;
- approval evidence is present;
- the release artifact is linked to the evidence set;
- any accepted residual risk is explicitly recorded.

## Why this matters for Agentic / Physical AI

For software agents, a bad action can cause financial, privacy, policy, or operational impact.

For physical AI, the same loop becomes more consequential because the system acts in an environment it does not fully control. Human overrides, near misses, edge cases, and out-of-distribution behavior should therefore feed the same reliability machinery.

The key principle is:

> **The more costly the failure, the more the release decision should depend on deterministic evidence rather than model confidence.**
