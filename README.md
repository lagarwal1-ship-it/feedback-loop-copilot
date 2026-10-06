# Feedback Loop Copilot — Principal TPM Prototype

A deliberately small prototype for an **AI reliability operating model**:

> **Failure → Pattern → Regression Test → Human Approval → Verification → Release Gate**

The implementation is intentionally lightweight. The goal is not to simulate a production AI platform; it is to make the **operating mechanism** concrete and inspectable.

## Why this exists

A capable agent is not enough. As AI systems act in the real world, the organization needs a repeatable way to learn from failures, encode those learnings as regression coverage, make accountable changes, and require evidence before release.

This prototype demonstrates that loop using three synthetic agent failures:

- A refund bypasses a manager-approval policy.
- A second refund bypasses the same control, demonstrating pattern clustering.
- Ambiguous support language is treated as permission for an irreversible credit.

The demo then turns those failures into two recurring patterns, two regression tests, proposed changes, a human approval step, and a verification result.

## What to look for

This project is intentionally **not** trying to impress through code volume. Review the system design:

1. **Capture** — preserve the failure and expected behavior.
2. **Analyze** — cluster similar failures and identify a likely root cause.
3. **Change** — create durable regression coverage and an accountable approval step.
4. **Verify** — replay the same failure pattern against the changed behavior.
5. **Gate** — keep release blocked until required evidence is green.

See [`docs/architecture.md`](docs/architecture.md), [`docs/operating-model.md`](docs/operating-model.md), [`docs/evaluation.md`](docs/evaluation.md), [`docs/risk-and-release-gates.md`](docs/risk-and-release-gates.md), and [`docs/decisions.md`](docs/decisions.md).

## Repository structure

```text
feedback-loop-copilot/
├── README.md
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── docs/
│   ├── architecture.md
│   ├── operating-model.md
│   ├── evaluation.md
│   ├── risk-and-release-gates.md
│   └── decisions.md
├── sample_data/
│   └── simulated_failures.json
├── tests/
│   └── test_feedback_loop.py
└── static/
    └── index.html
```

## Run locally — Mac first

### Option A: Finder

1. Download the ZIP from GitHub.
2. Open **Downloads**.
3. Double-click the ZIP to extract it.
4. Open **Terminal**.
5. Type `cd ` (including the space), drag the extracted `feedback-loop-copilot` folder into Terminal, and press **Return**.
6. Continue with the setup below.

### Option B: Terminal

```bash
cd ~/Downloads
unzip feedback-loop-copilot.zip
cd feedback-loop-copilot
```

### Set up the environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open:

`http://127.0.0.1:8000`

Keep the Terminal process running while the browser demo is open.

## Demo sequence

Click the controls in this order:

**1. Simulate agent runs**  
Creates three synthetic failures.

**2. Analyze failures**  
Clusters them into recurring patterns and creates regression tests.

**3. Approve & apply fix**  
Represents the accountable human review / change-approval step.

**4. Verify approved fixes**  
Replays the failure patterns and records whether the new controls pass.

The release gate turns **GREEN** only after the approved patterns are verified.

## Run the tests

The test suite validates the core loop without starting the web server:

```bash
python -m unittest discover -s tests -v
```

Expected result: all tests pass, including the blocked-to-green release transition.

## Optional model-backed analysis

The default demo uses deterministic local analysis and makes no external API calls.

To experiment with model-backed analysis, set one API key in your shell before starting the server:

```bash
export OPENAI_API_KEY="your-key-here"
python app.py
```

or:

```bash
export ANTHROPIC_API_KEY="your-key-here"
python app.py
```

The provider-specific endpoint is already isolated in `app.py`; the public demo does not require a key.

**Never commit API keys.** Use environment variables or an untracked local `.env` file if you add one. `.gitignore` excludes common secret/local-development files.

## Public-sharing / privacy notes

This repository is designed as a public-safe prototype:

- Synthetic failures only.
- No customer records, production logs, or company-specific data.
- No real API keys or credentials.
- No local machine usernames or absolute user paths.
- Default mode makes no external network call.

Before adding organization-specific examples, run a repository secret scan and remove proprietary identifiers or real operational data.

## Principal-level system framing

The code is intentionally small. The deeper artifact is the **operating model around the model**.

The prototype establishes explicit answers to:

- **What counts as a failure?** — a mismatch between observed agent behavior and the expected control / outcome.
- **Who owns the response?** — a named accountable role, not a vague "team".
- **How fast should feedback return?** — measured as failure-to-test and failure-to-verified-fix latency.
- **What changes?** — a durable control plus a regression test, not only an incident note.
- **What blocks release?** — severity-aware gates defined in [`docs/risk-and-release-gates.md`](docs/risk-and-release-gates.md).

The production path would connect these concepts to real agent telemetry, incident systems, CI/CD, policy controls, ownership systems, and historical evaluation data.

## Production evolution

A production implementation would add, at minimum:

- Real agent/tool traces and human-override events.
- Persistent failure and regression-test storage.
- Identity-aware ownership and SLA tracking.
- Automated regression execution in CI/CD.
- Evidence and audit history for approvals.
- Severity-aware and workflow-specific release gates.
- Metrics for recurrence, coverage, and mean time from failure to verified fix.
- Governance around when AI may recommend versus automatically apply changes.

This repository intentionally stops before those production integrations.
