# Architecture

## Purpose

This prototype separates the reliability loop into explicit states rather than treating a failure as a log-only event.

```text
Synthetic agent run
        |
        v
   Failure capture
        |
        v
 Pattern clustering ----> Regression tests
        |
        v
  Proposed controls
        |
        v
 Human approval
        |
        v
 Verification / replay
        |
        v
 Release gate
```

## Design choice

The demo uses deterministic local logic instead of an external model. This keeps the failure-to-gate path observable and reproducible while making it easy to replace any stage with a production system later.

## Production boundary

A production implementation would connect the same states to:

- agent/tool traces,
- evaluation and incident systems,
- identity-aware ownership,
- CI/CD regression execution,
- approval evidence and audit history,
- policy enforcement points, and
- persistent historical evaluation data.
