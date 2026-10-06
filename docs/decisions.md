# Design Decisions

## 1. Why a simulated agent?

The prototype is meant to demonstrate the feedback-loop operating model without requiring access to a production agent, confidential telemetry, or customer data.

The simulated agent intentionally produces realistic failures so the downstream process can be evaluated end to end.

## 2. Why deterministic local analysis by default?

A public demo should be reproducible, inexpensive, and safe to run without credentials.

The code includes optional OpenAI / Anthropic integration for experimentation, but the core demo does not depend on an external model.

## 3. Why human approval?

The prototype separates **AI recommendation** from **authorization to change behavior**.

That makes the accountability boundary visible and avoids implying that the model should unilaterally rewrite production behavior.

## 4. Why regression tests instead of only tickets?

An incident record describes what happened. A regression test creates durable evidence that the organization learned from it.

The desired transition is:

> incident → learning → executable evidence

## 5. Why cluster failures?

SIM-01 and SIM-02 are intentionally different incidents with the same systemic failure. Treating them as one pattern demonstrates that the loop should reduce recurrence at the **category** level rather than produce one-off fixes.

## 6. Why a release gate?

Without a release policy, learning remains advisory. The gate makes the feedback loop consequential: the system cannot claim a fix is complete until the evidence passes.

## 7. Why is the implementation small?

The prototype is intentionally scoped to illustrate system design rather than infrastructure complexity. A production implementation would introduce persistent storage, identity, audit history, CI/CD integration, real telemetry, security controls, and workflow-specific policy enforcement.
