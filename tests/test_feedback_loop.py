import unittest

import app


class FeedbackLoopTests(unittest.TestCase):
    def setUp(self):
        app.STATE = app.initial_state()
        self.client = app.app.test_client()

    def test_release_starts_blocked(self):
        response = self.client.get("/api/state")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["release_gate"], "BLOCKED")

    def test_full_feedback_loop_reaches_green(self):
        self.assertEqual(self.client.post("/api/simulate").status_code, 200)

        analyzed = self.client.post("/api/analyze")
        self.assertEqual(analyzed.status_code, 200)
        body = analyzed.get_json()
        self.assertEqual(len(body["failures"]), 3)
        self.assertEqual(len(body["patterns"]), 2)
        self.assertEqual(len(body["regression_tests"]), 2)
        self.assertEqual(len(body["proposed_fixes"]), 2)
        self.assertEqual(body["release_gate"], "BLOCKED")

        approved = self.client.post("/api/approve")
        self.assertEqual(approved.status_code, 200)
        self.assertTrue(approved.get_json()["approved"])
        self.assertEqual(approved.get_json()["release_gate"], "BLOCKED")

        verified = self.client.post("/api/verify")
        self.assertEqual(verified.status_code, 200)
        body = verified.get_json()
        self.assertEqual([item["status"] for item in body["verification"]], ["PASS", "PASS"])
        self.assertEqual(body["release_gate"], "GREEN")

    def test_verify_requires_human_approval(self):
        self.client.post("/api/simulate")
        self.client.post("/api/analyze")
        response = self.client.post("/api/verify")
        self.assertEqual(response.status_code, 400)
        self.assertIn("approval", response.get_json()["error"].lower())


if __name__ == "__main__":
    unittest.main()
