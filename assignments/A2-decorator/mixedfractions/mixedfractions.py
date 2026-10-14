"""Main program for the Kattis Mixed Fractions problem."""

import sys

from fraction_manager import FractionManager


def solve() -> None:
    """Read fractions and print their mixed-number representations."""
    manager = FractionManager()

    for line in sys.stdin:
        numerator, denominator = map(int, line.split())

        if numerator == 0 and denominator == 0:
            break

        print(manager.convert(numerator, denominator))


if __name__ == "__main__":
    solve()