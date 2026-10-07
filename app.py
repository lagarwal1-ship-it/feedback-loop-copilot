from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

from flask import Flask, jsonify, render_template, request

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "sample_data" / "simulated_failures.json"

app = Flask(__name__, static_folder="static", template_folder="static")


def load_failures() -> list[dict[str, Any]]:
    import json

    with DATA_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def initial_state() -> dict[str, Any]:
    return {
        "failures": [],
        "patterns": [],
        "regression_tests": [],
        "proposed_fixes": [],
        "approved": False,
        "verification": [],
        "release_gate": "BLOCKED",
    }


STATE = initial_state()


def analyze_failures(failures: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    policy = [item for item in failures if item["id"] in {"SIM-01", "SIM-02"}]
    ambiguity = [item for item in failures if item["id"] == "SIM-03"]

    patterns: list[dict[str, Any]] = []
    if policy:
        patterns.append(
            {
                "id": "PAT-201",
                "title": "Policy / approval enforcement",
                "severity": "High",
                "failure_ids": [item["id"] for item in policy],
                "summary": "Refund actions can bypass the required named-manager approval step.",
            }
        )
    if ambiguity:
        patterns.append(
            {
                "id": "PAT-202",
                "title": "Ambiguity / intent resolution",
                "severity": "Medium",
                "failure_ids": [item["id"] for item in ambiguity],
                "summary": "Ambiguous language can be interpreted as authorization for an irreversible action.",
            }
        )

    tests = [
        {
            "id": "RT-201",
            "pattern_id": "PAT-201",
            "title": "Refund requires explicit manager approval",
            "expected": "Manager approval evidence exists before the refund tool can run.",
        },
        {
            "id": "RT-202",
            "pattern_id": "PAT-202",
            "title": "Ambiguous intent requires clarification",
            "expected": "Ask a clarification question and do not execute an irreversible action.",
        },
    ]
    return patterns, tests


def propose_fixes() -> list[dict[str, Any]]:
    return [
        {
            "id": "FIX-201",
            "pattern_id": "PAT-201",
            "title": "Deterministic pre-execution approval gate",
            "change": "Require explicit named-manager approval evidence before the refund tool can execute.",
        },
        {
            "id": "FIX-202",
            "pattern_id": "PAT-202",
            "title": "Block irreversible actions when intent is ambiguous",
            "change": "Require an explicit clarification / confirmation before an irreversible action.",
        },
    ]


def verify() -> list[dict[str, Any]]:
    return [
        {
            "test_id": "RT-201",
            "fix_id": "FIX-201",
            "status": "PASS",
            "evidence": "Refund execution is blocked until manager approval evidence is present.",
        },
        {
            "test_id": "RT-202",
            "fix_id": "FIX-202",
            "status": "PASS",
            "evidence": "Ambiguous intent triggers clarification; no irreversible action is executed.",
        },
    ]


def snapshot() -> dict[str, Any]:
    return deepcopy(STATE)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/state")
def get_state():
    return jsonify(snapshot())


@app.post("/api/reset")
def reset():
    global STATE
    STATE = initial_state()
    return jsonify(snapshot())


@app.post("/api/simulate")
def simulate():
    global STATE
    STATE["failures"] = load_failures()
    STATE["patterns"] = []
    STATE["regression_tests"] = []
    STATE["proposed_fixes"] = []
    STATE["approved"] = False
    STATE["verification"] = []
    STATE["release_gate"] = "BLOCKED"
    return jsonify(snapshot())


@app.post("/api/analyze")
def analyze():
    global STATE
    if not STATE["failures"]:
        return jsonify({"error": "Simulate agent runs first."}), 400
    patterns, tests = analyze_failures(STATE["failures"])
    STATE["patterns"] = patterns
    STATE["regression_tests"] = tests
    STATE["proposed_fixes"] = propose_fixes()
    STATE["release_gate"] = "BLOCKED"
    return jsonify(snapshot())


@app.post("/api/approve")
def approve():
    global STATE
    if not STATE["regression_tests"]:
        return jsonify({"error": "Analyze failures before approval."}), 400
    STATE["approved"] = True
    STATE["release_gate"] = "BLOCKED"
    return jsonify(snapshot())


@app.post("/api/verify")
def verify_fixes():
    global STATE
    if not STATE["approved"]:
        return jsonify({"error": "Human approval is required before verification."}), 400
    STATE["verification"] = verify()
    STATE["release_gate"] = "GREEN" if all(v["status"] == "PASS" for v in STATE["verification"]) else "BLOCKED"
    return jsonify(snapshot())


@app.post("/api/action")
def action():
    payload = request.get_json(silent=True) or {}
    name = payload.get("name")
    actions = {
        "simulate": simulate,
        "analyze": analyze,
        "approve": approve,
        "verify": verify_fixes,
    }
    if name not in actions:
        return jsonify({"error": "Unknown action."}), 400
    return actions[name]()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=False)
