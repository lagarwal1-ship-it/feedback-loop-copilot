# Evaluation

The prototype is deliberately small, but it exposes the signals that would matter in a production feedback loop.

| Metric | Definition |
|---|---|
| Failure recurrence rate | Percentage of previously observed failure patterns that recur after a change |
| Failure-to-test latency | Time from failure capture to durable regression coverage |
| Failure-to-verified-fix latency | Time from failure capture to verified corrective change |
| Regression coverage | Share of known high-severity patterns represented by executable checks |
| Open high-severity failures | Count of unresolved high-severity patterns |
| Release-blocking failures | Count of failures currently preventing release |

The demo itself exercises the last two stages: approved regression tests pass and the release gate changes from **BLOCKED** to **GREEN**.
