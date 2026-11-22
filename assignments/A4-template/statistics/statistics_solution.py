
"""Object-oriented solution to Kattis Statistics."""

from typing import TextIO

from statistics_template import StatisticsTemplate
from statistics_values import StatisticsValues


class StatisticsSolution(StatisticsTemplate):
    """Read, solve, and output Statistics test cases."""

    def __init__(self, data_source: TextIO, output: TextIO) -> None:
        """Initialize the solution and its results."""
        super().__init__(data_source, output)
        self._data: list[StatisticsValues] = []
        self._answer: list[str] = []

    def read_input(self) -> None:
        """Read test cases until end of input."""
        cases: list[StatisticsValues] = []

        for line in self._input_source:
            numbers = list(map(int, line.split()))

            if not numbers:
                continue

            count = numbers[0]
            values = numbers[1:]

            if count < 1 or len(values) != count:
                raise ValueError("Invalid Statistics test case.")

            cases.append(StatisticsValues(values))

        self._data = cases

    @property
    def data(self) -> list[StatisticsValues]:
        """Return the parsed test cases."""
        return self._data

    @property
    def answer(self) -> list[str]:
        """Return the formatted answers."""
        return self._answer

    def solve(self) -> None:
        """Calculate minimum, maximum, and range."""
        self._answer = [
            f"Case {index}: "
            f"{values.minimum} {values.maximum} {values.spread}"
            for index, values in enumerate(self.data, start=1)
        ]

    def print_answer(self) -> None:
        """Write the answers in the required Kattis format."""
        if self.answer:
            self._output.write("\n".join(self.answer) + "\n")
