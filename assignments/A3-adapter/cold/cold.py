
"""Kattis Cold-puter Science solution."""

import sys

from cold_counter import ColdCounter


def solve(data: str) -> str:
    """Count negative temperatures in Kattis input."""
    numbers = list(map(int, data.split()))

    total = numbers[0]
    temperatures = numbers[1:total + 1]

    result = ColdCounter.count(temperatures)
    return f"{result}\n"


def main() -> None:
    """Read standard input and print the result."""
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":  # pragma: no cover
    main()
