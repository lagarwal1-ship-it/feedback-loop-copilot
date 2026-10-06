# Operating Model

The central TPM question is not only **"did we fix the incident?"** It is **"did the organization change the system so this class of failure is less likely to recur?"**

## Five-step operating loop

### 1. Capture

Record the smallest useful unit of evidence:

- observed action / output
- expected outcome or policy
- severity
- human override, if any
- timestamp / version / environment in a production system

### 2. Analyze

Use AI to reduce review effort:

- cluster similar failures
- identify likely root causes
- detect recurrence
- suggest missing tests
- distinguish local case fixes from systemic control gaps

AI should recommend; governance determines what becomes policy.

### 3. Change

Every meaningful pattern should result in a durable artifact:

- regression test
- control / policy / workflow change
- accountable owner
- target date / SLA
- approval record

A ticket without a regression test is often just a promise to learn.

### 4. Verify

Verification should replay the failure pattern rather than rely on a narrative that the fix "should" work.

Minimum evidence:

- same failure case passes
- related regression cases pass
- no new high-severity regression introduced
- change is traceable to an approval

### 5. Gate

Release decisions should be policy-driven, not ad hoc.

The gate answers:

> **What evidence is sufficient to ship this workflow?**

## Accountability model

Each failure pattern gets one accountable owner role / name. Avoid assigning ownership to "the team."

Example:

| Artifact | Accountable role | Supporting roles |
|---|---|---|
| Failure pattern | TPM / product owner | ML, policy, operations |
| Regression test | Engineering owner | QA / evaluation |
| Policy change | Policy owner | Legal / security as needed |
| Release decision | Workflow owner | TPM + engineering |

## Escalation principle

The higher the impact of a failure, the less acceptable it is to rely on model confidence alone.

High-impact failures should have:

- deterministic controls where possible
- explicit approval evidence
- reproducible regression tests
- release-blocking behavior until evidence is green

## What changes in a scaled environment

At scale, this becomes a portfolio operating rhythm:

**Failure telemetry → weekly pattern review → ownership/SLA → regression coverage → release evidence → trend review**

The TPM owns the system of learning, not each individual model response.
