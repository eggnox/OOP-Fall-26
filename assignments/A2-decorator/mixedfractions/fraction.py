"""Fraction class for the Mixed Fractions problem."""


class Fraction:
    """Represent a fraction using a numerator and denominator."""

    def __init__(self, numerator: int, denominator: int) -> None:
        """Initialize a fraction."""
        self.numerator = numerator
        self.denominator = denominator

    @property
    def numerator(self) -> int:
        """Get the numerator."""
        return self._numerator

    @numerator.setter
    def numerator(self, value: int) -> None:
        """Set the numerator."""
        self._numerator = value

    @property
    def denominator(self) -> int:
        """Get the denominator."""
        return self._denominator

    @denominator.setter
    def denominator(self, value: int) -> None:
        """Set the denominator and reject invalid values."""
        if value <= 0:
            raise ValueError("Denominator must be positive")

        self._denominator = value
        
    def to_mixed(self) -> tuple[int, int, int]:
        """Convert a fraction into mixed-number components."""
        whole, remainder = divmod(
            self.numerator, self.denominator
        )
        return whole, remainder, self.denominator