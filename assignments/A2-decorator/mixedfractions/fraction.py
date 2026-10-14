"""Fraction class for the Mixed Fractions problem."""


class Fraction:
    """Represent a fraction using a numerator and denominator."""

    def __init__(self, numerator: int, denominator: int) -> None:
        """Initialize a fraction."""
        self._numerator: int = numerator
        self._denominator: int = denominator