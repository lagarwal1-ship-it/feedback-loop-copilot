import unittest

import app


class FeedbackLoopTests(unittest.TestCase):
    def setUp(self):
        app.reset_state()

    def test_capture_creates_three_simulated_failures(self):
        self.assertEqual(len(app.state["runs"]), 3)
        self.assertEqual({r["id"] for r in app.state["runs"]}, {"SIM-01", "SIM-02", "SIM-03"})

    def test_analysis_clusters_failures_into_two_patterns(self):
        result = app.analyze_current_runs()
        self.assertEqual(result["failures_reviewed"], 3)
        self.assertEqual(result["patterns"]["Policy / approval enforcement"], 2)
        self.assertEqual(result["patterns"]["Ambiguity / intent resolution"], 1)
        self.assertEqual(result["regression_tests_added"], 2)
        self.assertEqual(result["release_gate"], "BLOCKED")

    def test_release_gate_stays_blocked_until_both_patterns_are_approved(self):
        app.analyze_current_runs()
        app.apply_fix("Policy / approval enforcement")
        result = app.build_result()
        self.assertEqual(result["fixes_verified"], 0)
        self.assertEqual(result["release_gate"], "BLOCKED")

    def test_verification_turns_gate_green_after_all_approved_patterns_pass(self):
        app.analyze_current_runs()
        app.apply_fix("Policy / approval enforcement")
        app.apply_fix("Ambiguity / intent resolution")
        result = app.verify_fixes()
        self.assertEqual(result["fixes_verified"], 2)
        self.assertEqual(result["still_failing"], 0)
        self.assertEqual(result["release_gate"], "GREEN")


if __name__ == "__main__":
    unittest.main()
