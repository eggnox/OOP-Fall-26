"""Whole-program tests for convexpolygonarea."""

import subprocess
import sys
import unittest


class TestConvexPolygonAreaProgram(unittest.TestCase):
    """Test the complete Convex Polygon Area program."""

    def run_program(self, program_input: str) -> str:
        """Run the program with input and return its output."""
        result = subprocess.run(
            [sys.executable, "convexpolygonarea.py"],
            input=program_input,
            text=True,
            capture_output=True,
            check=True,
        )

        return result.stdout.strip()

    def test_kattis_sample(self) -> None:
        """Test the official Kattis sample."""
        program_input = (
            "2\n"
            "3 1 1 2 1 2 2\n"
            "4 0 0 10 0 13 5 10 8\n"
        )

        expected = "0.5\n52"

        self.assertEqual(
            self.run_program(program_input),
            expected,
        )

    def test_triangle(self) -> None:
        """Test one triangle."""
        program_input = (
            "1\n"
            "3 0 0 4 0 0 3\n"
        )

        self.assertEqual(
            self.run_program(program_input),
            "6",
        )

    def test_rectangle(self) -> None:
        """Test one rectangle."""
        program_input = (
            "1\n"
            "4 0 0 4 0 4 3 0 3\n"
        )

        self.assertEqual(
            self.run_program(program_input),
            "12",
        )


if __name__ == "__main__":
    unittest.main()