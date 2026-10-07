# Operating Model

The prototype answers four operating questions:

1. **Evaluate — What counts as failure?**
   A mismatch between observed behavior and an expected control or outcome.

2. **Review — Who looks at it?**
   The approval step represents a named accountable human rather than a vague "team" owner.

3. **Speed — How fast does feedback return?**
   Track failure-to-test and failure-to-verified-fix latency.

4. **Change — What actually changes?**
   A durable control plus regression coverage, not only an incident note.

The reliability mechanism is therefore:

**Failure → Pattern → Regression Test → Human Approval → Verification → Release Gate**
