
"""Template Method pattern for Kattis solutions."""

from typing import TextIO, final

from kattis import Kattis


class StatisticsTemplate(Kattis):
    """Define the fixed sequence for solving a Kattis problem."""

    def __init__(self, data_source: TextIO, output: TextIO) -> None:
        """Initialize input and output streams."""
        super().__init__(data_source)
        self._output = output

    @final
    def run(self) -> None:
        """Execute the algorithm in a fixed order."""
        self.read_input()
        self.solve()
        self.print_answer()
