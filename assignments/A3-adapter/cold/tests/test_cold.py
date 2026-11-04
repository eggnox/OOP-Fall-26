
"""Unit tests for the Kattis Cold-puter Science program."""

import io
import unittest
from unittest.mock import patch

from cold import main, solve


class TestCold(unittest.TestCase):
    """Test Kattis input processing and program output."""

    def test_solve_mixed_temperatures(self) -> None:
        """Count negative temperatures in mixed input."""
        data = "5\n-10 0 5 -3 12\n"
        self.assertEqual(solve(data), "2\n")

    def test_solve_all_negative(self) -> None:
        """Count all temperatures when each is negative."""
        data = "4\n-1 -2 -3 -4\n"
        self.assertEqual(solve(data), "4\n")

    def test_solve_no_negative(self) -> None:
        """Return zero when all temperatures are nonnegative."""
        data = "5\n0 1 2 3 4\n"
        self.assertEqual(solve(data), "0\n")

    def test_solve_invalid_input(self) -> None:
        """Reject input containing invalid integers."""
        with self.assertRaises(ValueError):
            solve("3\n-1 invalid 5\n")

    def test_main_mixed_temperatures(self) -> None:
        """Verify main reads input and writes the answer."""
        fake_input = io.StringIO("5\n-10 0 5 -3 12\n")
        fake_output = io.StringIO()

        with patch("cold.sys.stdin", fake_input):
            with patch("cold.sys.stdout", fake_output):
                main()

        self.assertEqual(fake_output.getvalue(), "2\n")

    def test_main_all_negative(self) -> None:
        """Verify program output for negative temperatures."""
        fake_input = io.StringIO("3\n-5 -10 -15\n")
        fake_output = io.StringIO()

        with patch("cold.sys.stdin", fake_input):
            with patch("cold.sys.stdout", fake_output):
                main()

        self.assertEqual(fake_output.getvalue(), "3\n")

    def test_main_no_negative(self) -> None:
        """Verify program output when nothing is below zero."""
        fake_input = io.StringIO("4\n0 5 10 20\n")
        fake_output = io.StringIO()

        with patch("cold.sys.stdin", fake_input):
            with patch("cold.sys.stdout", fake_output):
                main()

        self.assertEqual(fake_output.getvalue(), "0\n")


if __name__ == "__main__":  # pragma: no cover
    main()