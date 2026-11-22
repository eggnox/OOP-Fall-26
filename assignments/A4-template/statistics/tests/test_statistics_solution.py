
"""Unit tests for the Statistics solution and Template Method."""

import io
import unittest
from unittest.mock import Mock, call, patch

from kattis import Kattis
from statistics_main import main
from statistics_solution import StatisticsSolution
from statistics_template import StatisticsTemplate


class TestStatisticsSolution(unittest.TestCase):
    """Test input parsing, calculations, and output."""

    def test_single_case(self) -> None:
        """Solve one Statistics test case."""
        output = io.StringIO()
        solution = StatisticsSolution(
            io.StringIO("4 4 7 10 6\n"), output
        )

        solution.run()

        self.assertEqual(output.getvalue(), "Case 1: 4 10 6\n")

    def test_multiple_cases(self) -> None:
        """Process several cases until EOF."""
        data = "4 4 7 10 6\n3 -10 0 5\n1 8\n"
        output = io.StringIO()

        StatisticsSolution(io.StringIO(data), output).run()

        self.assertEqual(
            output.getvalue(),
            "Case 1: 4 10 6\n"
            "Case 2: -10 5 15\n"
            "Case 3: 8 8 0\n"
        )

    def test_read_input(self) -> None:
        """Verify that input is converted into integer lists."""
        solution = StatisticsSolution(
            io.StringIO("3 2 4 8\n"), io.StringIO()
        )

        solution.read_input()

        self.assertEqual(list(solution.data[0]), [2, 4, 8])

    def test_answer_property(self) -> None:
        """Verify calculated answers are accessible."""
        solution = StatisticsSolution(
            io.StringIO("3 2 4 8\n"), io.StringIO()
        )

        solution.read_input()
        solution.solve()

        self.assertEqual(solution.answer, ["Case 1: 2 8 6"])

    def test_blank_lines(self) -> None:
        """Ignore empty lines between cases."""
        output = io.StringIO()

        StatisticsSolution(
            io.StringIO("\n1 5\n\n1 -3\n"), output
        ).run()

        self.assertEqual(
            output.getvalue(),
            "Case 1: 5 5 0\nCase 2: -3 -3 0\n"
        )

    def test_invalid_count(self) -> None:
        """Reject a case with the wrong number of values."""
        solution = StatisticsSolution(
            io.StringIO("3 1 2\n"), io.StringIO()
        )

        with self.assertRaises(ValueError):
            solution.read_input()

    def test_zero_count(self) -> None:
        """Reject a test case with no integers."""
        solution = StatisticsSolution(
            io.StringIO("0\n"), io.StringIO()
        )

        with self.assertRaises(ValueError):
            solution.read_input()

    def test_invalid_integer(self) -> None:
        """Reject values that cannot be parsed as integers."""
        solution = StatisticsSolution(
            io.StringIO("3 1 hello 5\n"), io.StringIO()
        )

        with self.assertRaises(ValueError):
            solution.read_input()

    def test_empty_input(self) -> None:
        """Produce no output when input is empty."""
        output = io.StringIO()

        StatisticsSolution(io.StringIO(""), output).run()

        self.assertEqual(output.getvalue(), "")

    def test_inheritance(self) -> None:
        """Verify inheritance from the required Kattis ABC."""
        solution = StatisticsSolution(
            io.StringIO("1 5\n"), io.StringIO()
        )

        self.assertIsInstance(solution, Kattis)
        self.assertIsInstance(solution, StatisticsTemplate)

    def test_template_method_order(self) -> None:
        """Verify the fixed read, solve, print sequence."""
        solution = StatisticsSolution(
            io.StringIO("1 5\n"), io.StringIO()
        )

        recorder = Mock()

        with patch.object(solution, "read_input") as read:
            with patch.object(solution, "solve") as solve:
                with patch.object(solution, "print_answer") as show:
                    recorder.attach_mock(read, "read_input")
                    recorder.attach_mock(solve, "solve")
                    recorder.attach_mock(show, "print_answer")

                    solution.run()

        self.assertEqual(
            recorder.mock_calls,
            [
                call.read_input(),
                call.solve(),
                call.print_answer(),
            ]
        )

    def test_main_with_mocked_streams(self) -> None:
        """Verify the command-line entry point."""
        output = io.StringIO()

        with patch(
            "statistics_main.sys.stdin",
            io.StringIO("2 3 9\n")
        ):
            with patch("statistics_main.sys.stdout", output):
                main()

        self.assertEqual(output.getvalue(), "Case 1: 3 9 6\n")


if __name__ == "__main__":
    unittest.main()
