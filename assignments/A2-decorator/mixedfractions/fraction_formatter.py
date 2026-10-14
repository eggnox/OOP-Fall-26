"""Classes for formatting mixed fractions."""

from abc import ABC, abstractmethod

from fraction import Fraction


class FractionFormatter(ABC):
    """Abstract interface for formatting fractions."""

    @abstractmethod
    def format(self, fraction: Fraction) -> str:
        """Return a formatted fraction."""


class BasicMixedFormatter(FractionFormatter):
    """Format fractions as basic mixed numbers."""

    def format(self, fraction: Fraction) -> str:
        """Return the mixed fraction without extra spacing."""
        whole, remainder, bottom = fraction.to_mixed()

        return f"{whole} {remainder}/{bottom}"