import unittest

from analyzer import build_alerts, parse_failed_logins, severity_for_count


class AnalyzerTests(unittest.TestCase):
    def test_parse_failed_logins(self):
        lines = [
            "Failed password for admin from 203.0.113.10 port 22 ssh2",
            "Accepted password for admin from 203.0.113.10 port 22 ssh2",
        ]
        self.assertEqual(
            parse_failed_logins(lines),
            [{"username": "admin", "ip": "203.0.113.10"}],
        )

    def test_build_alerts_threshold(self):
        attempts = [{"username": "admin", "ip": "203.0.113.10"}] * 3
        alerts = build_alerts(attempts)
        self.assertEqual(len(alerts), 1)
        self.assertIn("MEDIUM", alerts[0])

    def test_severity(self):
        self.assertEqual(severity_for_count(2), "LOW")
        self.assertEqual(severity_for_count(3), "MEDIUM")
        self.assertEqual(severity_for_count(5), "HIGH")


if __name__ == "__main__":
    unittest.main()
