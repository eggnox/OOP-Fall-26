
"""Entry point for the Kattis Statistics problem."""

import sys

from statistics_solution import StatisticsSolution


def main() -> None:
    """Run the Statistics solution using standard input/output."""
    solution = StatisticsSolution(sys.stdin, sys.stdout)
    solution.run()


if __name__ == "__main__":  # pragma: no cover
    main()
