
"""Unit tests for the Rich weather dashboard."""

import io
import unittest
from unittest.mock import Mock

from rich.console import Console
from rich.panel import Panel

from weather_dashboard import WeatherDashboard
from weather_reading import WeatherReading


class TestWeatherDashboard(unittest.TestCase):
    """Test weather dashboard output and console behavior."""

    def setUp(self) -> None:
        """Prepare an in-memory console and sample weather."""
        self.output = io.StringIO()
        self.console = Console(
            file=self.output,
            force_terminal=False,
            color_system=None,
            width=80,
        )

        self.weather = WeatherReading(
            city="Grand Junction",
            temperature_c=18.5,
            feels_like_c=17.0,
            humidity_percent=45,
            wind_speed_kmh=12.3,
            condition="Partly cloudy",
        )

    def test_default_console(self) -> None:
        """Verify that the dashboard creates a Rich console."""
        dashboard = WeatherDashboard()

        self.assertIsInstance(dashboard.console, Console)

    def test_custom_console(self) -> None:
        """Verify that a custom console is preserved."""
        dashboard = WeatherDashboard(console=self.console)

        self.assertIs(dashboard.console, self.console)

    def test_weather_output(self) -> None:
        """Verify all weather information appears in the panel."""
        dashboard = WeatherDashboard(console=self.console)
        dashboard.show(self.weather)

        result = self.output.getvalue()

        self.assertIn("Grand Junction", result)
        self.assertIn("Temperature", result)
        self.assertIn("18.5", result)
        self.assertIn("Feels Like", result)
        self.assertIn("17.0", result)
        self.assertIn("Humidity", result)
        self.assertIn("45%", result)
        self.assertIn("Wind Speed", result)
        self.assertIn("12.3", result)
        self.assertIn("Partly cloudy", result)

    def test_freezing_weather_output(self) -> None:
        """Verify freezing temperatures display correctly."""
        weather = WeatherReading(
            city="Denver",
            temperature_c=-8.5,
            feels_like_c=-15.0,
            humidity_percent=90,
            wind_speed_kmh=25.0,
            condition="Heavy snow",
        )

        dashboard = WeatherDashboard(console=self.console)
        dashboard.show(weather)

        result = self.output.getvalue()

        self.assertIn("Denver", result)
        self.assertIn("-8.5", result)
        self.assertIn("-15.0", result)
        self.assertIn("90%", result)
        self.assertIn("25.0", result)
        self.assertIn("Heavy snow", result)

    def test_panel_rendering_with_mock(self) -> None:
        """Verify that the dashboard sends a Panel to Rich."""
        mock_console = Mock(spec=Console)
        dashboard = WeatherDashboard(console=mock_console)

        dashboard.show(self.weather)

        mock_console.print.assert_called_once()

        displayed = mock_console.print.call_args.args[0]
        self.assertIsInstance(displayed, Panel)


if __name__ == "__main__":
    unittest.main()
