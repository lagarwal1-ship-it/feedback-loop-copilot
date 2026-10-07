# Decisions

## Deterministic local analysis

**Decision:** Keep the demo deterministic and local.

**Why:** The objective is to show the reliability operating mechanism, not model-provider integration. Determinism makes the demo repeatable and makes verification evidence easier to inspect.

## Human approval is explicit

**Decision:** Approval is a distinct workflow state.

**Why:** A proposed change should not silently become a deployed change. Production implementations should attach identity, evidence, and audit history to this step.

## Regression tests precede release

**Decision:** A known failure pattern becomes a regression test before verification can pass.

**Why:** The organization should encode the lesson so the same class of failure is less likely to recur.

## Small implementation

**Decision:** Keep the code intentionally lightweight.

**Why:** The useful abstraction is the operating model around the agent. More code would not by itself make the reliability model more credible.
