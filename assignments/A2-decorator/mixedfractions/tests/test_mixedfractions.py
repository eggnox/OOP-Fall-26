
"""Unit tests for the Mixed Fractions main program."""

import io
import runpy
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from mixedfractions import solve


class TestMixedFractions(unittest.TestCase):
    """Test the main program and its input handling."""

    def test_single_fraction(self) -> None:
        """Test converting one improper fraction."""
        output = io.StringIO()

        with patch("sys.stdin", io.StringIO("27 12\n0 0\n")):
            with redirect_stdout(output):
                solve()

        self.assertEqual(output.getvalue(), "2 3 / 12\n")

    def test_multiple_fractions(self) -> None:
        """Test processing multiple fractions."""
        output = io.StringIO()
        data = "5 2\n1 7\n0 0\n"

        with patch("sys.stdin", io.StringIO(data)):
            with redirect_stdout(output):
                solve()

        self.assertEqual(
            output.getvalue(),
            "2 1 / 2\n0 1 / 7\n"
        )

    def test_main_entry_point(self) -> None:
        """Test running the module as a program."""
        output = io.StringIO()

        with patch("sys.stdin", io.StringIO("0 0\n")):
            with redirect_stdout(output):
                runpy.run_path(
                    "mixedfractions.py",
                    run_name="__main__"
                )

        self.assertEqual(output.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
