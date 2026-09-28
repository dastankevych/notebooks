import unittest

from quick_check import quick_check


class QuickCheckTests(unittest.TestCase):
    def test_uses_default_label(self):
        self.assertEqual(quick_check(), "notebook-check: ok")

    def test_accepts_custom_label(self):
        self.assertEqual(quick_check("weather"), "weather: ok")


if __name__ == "__main__":
    unittest.main()
