import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


class CommandLineTests(unittest.TestCase):
    def test_missing_book_reports_an_error(self):
        with TemporaryDirectory() as directory:
            missing_book = Path(directory) / "missing.txt"
            result = subprocess.run(
                [sys.executable, "main.py", str(missing_book)],
                capture_output=True,
                text=True,
            )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Could not read book", result.stderr)
        self.assertIn(str(missing_book), result.stderr)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
