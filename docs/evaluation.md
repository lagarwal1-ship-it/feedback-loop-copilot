# Evaluation and Metrics

A feedback loop should be measurable. The goal is to reduce recurrence and shorten the time between a failure being observed and the organization learning from it.

## Core metrics

| Metric | Definition | Why it matters |
|---|---|---|
| Failure recurrence rate | % of failures that repeat the same known pattern after a fix | Measures whether learning is durable |
| Failure → test latency | Median time from first failure to regression test creation | Measures learning speed |
| Failure → verified-fix latency | Median time from first failure to verified fix | Measures operational responsiveness |
| Regression coverage | % of high-severity failure patterns represented by executable tests | Measures prevention maturity |
| Open high-severity failures | Count of unresolved high-severity patterns | Measures current release risk |
| Release-blocking failures | Count of failures that should prevent shipment | Measures governance effectiveness |
| Verification pass rate | % of approved fixes that pass their defined verification suite | Detects weak or incomplete changes |
| Human override rate | % of agent actions requiring human intervention | Indicates where autonomy is still fragile |

## Suggested dashboard

For a production program, show at least:

```text
Failure recurrence         ↓
Failure → test latency     ↓
Failure → verified fix     ↓
Regression coverage        ↑
High-severity open         ↓
Release-blocking failures  ↓
Verification pass rate     ↑
Human override rate        ↓ (unless intentionally targeted)
```

## Example target framework

Targets should be set per workflow, but a useful starting pattern is:

- P0 / safety-critical: zero unresolved at release.
- P1 / financial or policy: zero unresolved in the affected workflow.
- P2 / quality: monitored with explicit owner and SLA.

## Measurement caution

A lower incident count does not automatically mean a safer system. Reporting behavior can change, exposure can change, and test coverage can change.

Pair outcome metrics with evidence metrics:

**incidents + override rate + coverage + verification quality + release gates**.
