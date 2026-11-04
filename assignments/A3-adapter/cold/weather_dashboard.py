
"""Rich terminal interface for displaying weather."""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from weather_reading import WeatherReading


class WeatherDashboard:
    """Display weather information in a Rich terminal panel."""

    def __init__(self, console: Console | None = None) -> None:
        """Initialize the dashboard with a console."""
        self._console = console if console is not None else Console()

    @property
    def console(self) -> Console:
        """Return the Rich console."""
        return self._console

    def show(self, weather: WeatherReading) -> None:
        """Display a formatted weather report."""
        table = Table(show_header=False)

        table.add_column("Weather Metric", style="cyan")
        table.add_column("Value", style="bold white")

        table.add_row(
            "Temperature", f"{weather.temperature_c:.1f} °C"
        )
        table.add_row(
            "Feels Like", f"{weather.feels_like_c:.1f} °C"
        )
        table.add_row(
            "Humidity", f"{weather.humidity_percent}%"
        )
        table.add_row(
            "Wind Speed", f"{weather.wind_speed_kmh:.1f} km/h"
        )
        table.add_row("Conditions", weather.condition)

        panel = Panel(
            table,
            title=f"Weather in {weather.city}",
            border_style="blue",
        )

        self._console.print(panel)
