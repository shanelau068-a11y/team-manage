"""Configuration validation only: no account actions, database writes or messages."""
import os
import unittest
from pydantic import ValidationError

os.environ.setdefault("SECRET_KEY", "test-only-secret-value-with-32-characters")
os.environ.setdefault("ADMIN_PASSWORD", "test-only-initial-password")
from app.config import Settings


class ConfigurationTests(unittest.TestCase):
    def test_rejects_old_example_secret(self):
        with self.assertRaises(ValidationError):
            Settings(_env_file=None, secret_key="your-secret-key-here-change-in-production", admin_password="a-long-test-password")

    def test_rejects_empty_or_short_credentials(self):
        for secret, password in (("", "a-long-test-password"), ("x" * 40, "admin123")):
            with self.assertRaises(ValidationError):
                Settings(_env_file=None, secret_key=secret, admin_password=password)

    def test_accepts_explicit_credentials(self):
        config = Settings(_env_file=None, secret_key="x" * 40, admin_password="a-long-test-password")
        self.assertEqual(config.secret_key, "x" * 40)


if __name__ == "__main__":
    unittest.main()
