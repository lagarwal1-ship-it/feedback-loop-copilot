# Feedback Loop Copilot — TPM Prototype

A lightweight prototype for a feedback loop that turns agent failures into regression tests, approved changes, verification, and release gates.

> **Failure → Pattern → Regression Test → Human Approval → Verification → Release Gate**

The implementation is intentionally small. The goal is to make the **operating mechanism** concrete and inspectable, not to simulate a production AI platform.

## What the prototype demonstrates

The demo uses three synthetic agent failures:

- **SIM-01 — High:** A $1,200 refund is approved without required manager approval.
- **SIM-02 — High:** A $900 refund is processed directly after an eligibility check, again bypassing manager approval.
- **SIM-03 — Medium:** Ambiguous support language is treated as permission to issue an irreversible credit.

The prototype then:

1. Captures the failures and expected behavior.
2. Clusters them into two recurring patterns.
3. Creates two regression tests.
4. Proposes two changes.
5. Requires a simulated accountable human approval.
6. Replays the same failure patterns against the proposed controls.
7. Turns the release gate **GREEN** only after verification passes.

## System framing

The important artifact is the operating model around the model:

```text
Failure
   ↓
Pattern
   ↓
Regression Test
   ↓
Human Approval
   ↓
Verification
   ↓
Release Gate
```

The broader feedback loop is:

```text
Observe → Act → Evaluate → Learn → Adjust
```

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

## Run locally

### 1. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Start the app

```bash
python app.py
```

Open:

`http://127.0.0.1:8000`

The default demo is fully local and deterministic. It does not require an API key and does not make external API calls.

## Demo sequence

Use the controls in this order:

**1. Simulate agent runs** — creates the three synthetic failures.

**2. Analyze failures** — clusters the failures into two patterns and creates two regression tests.

**3. Approve & apply fix** — represents accountable human review and approval of the proposed changes.

**4. Verify approved fixes** — replays the same failure patterns and records the verification result.

The release gate remains **BLOCKED** until the approved changes are verified.

## Test the workflow

```bash
python -m unittest discover -s tests -v
```

The tests cover the blocked-to-green release transition and the expected regression outcomes.

## Safety and privacy

This repository is designed as a public-safe prototype:

- Synthetic failures only.
- No customer records or production logs.
- No company-specific operational data.
- No API keys or credentials.
- No external API calls in the default mode.

Do not add secrets, private customer data, production traces, or proprietary identifiers to the repository.

## What would change in production

A production implementation would connect this operating model to real telemetry, evaluation systems, identity-aware ownership, incident workflows, CI/CD, approval evidence, policy controls, and historical regression data.

The prototype intentionally stops before those integrations.
