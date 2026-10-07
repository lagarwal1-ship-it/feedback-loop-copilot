# Risk and Release Gates

The release gate is intentionally evidence-based: approval alone does not turn the gate green.

| Severity / class | Example | Gate behavior |
|---|---|---|
| High / safety or financial-control failure | Refund executes without required approval | Block affected workflow until verified |
| Medium / ambiguity or quality risk | Irreversible action taken on unclear intent | Block affected action until clarified behavior is verified |
| Lower-risk quality issue | Non-critical response quality drift | Track and monitor; do not automatically block unrelated workflows |

In the demo, both known patterns are release-relevant. The gate remains **BLOCKED** until both approved fixes pass verification.
