
"""Unit tests for the live weather application."""

import io
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import MagicMock, patch

from weather_app import main
from weather_reading import WeatherReading


class TestWeatherApp(unittest.TestCase):
    """Test command-line behavior with mocked dependencies."""

    def setUp(self) -> None:
        """Create a sample weather reading."""
        self.weather = WeatherReading(
            "Test City", 18.5, 17.0,
            45, 12.3, "Clear sky"
        )

    @patch("weather_app.WeatherDashboard")
    @patch("weather_app.WeatherManager")
    def test_default_city(
        self, mock_manager: MagicMock,
        mock_dashboard: MagicMock
    ) -> None:
        """Verify Grand Junction is the default city."""
        mock_manager.return_value.get_weather.return_value = (
            self.weather
        )

        main([])

        mock_manager.return_value.get_weather.assert_called_once_with(
            city="Grand Junction",
            latitude=39.0639,
            longitude=-108.5506,
        )
        mock_dashboard.return_value.show.assert_called_once_with(
            self.weather
        )

    @patch("weather_app.WeatherDashboard")
    @patch("weather_app.WeatherManager")
    def test_denver_city(
        self, mock_manager: MagicMock,
        mock_dashboard: MagicMock
    ) -> None:
        """Verify Denver can be selected."""
        mock_manager.return_value.get_weather.return_value = (
            self.weather
        )

        main(["--city", "denver"])

        mock_manager.return_value.get_weather.assert_called_once_with(
            city="Denver",
            latitude=39.7392,
            longitude=-104.9903,
        )
        mock_dashboard.return_value.show.assert_called_once_with(
            self.weather
        )

    @patch("weather_app.WeatherDashboard")
    @patch("weather_app.WeatherManager")
    def test_fort_collins(
        self, mock_manager: MagicMock,
        mock_dashboard: MagicMock
    ) -> None:
        """Verify Fort Collins coordinates."""
        mock_manager.return_value.get_weather.return_value = (
            self.weather
        )

        main(["--city", "fort-collins"])

        mock_manager.return_value.get_weather.assert_called_once_with(
            city="Fort Collins",
            latitude=40.5853,
            longitude=-105.0844,
        )
        mock_dashboard.return_value.show.assert_called_once_with(
            self.weather
        )

    @patch("weather_app.WeatherManager")
    def test_invalid_city(
        self, mock_manager: MagicMock
    ) -> None:
        """Reject unsupported city selections."""
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as error:
                main(["--city", "invalid-city"])

        self.assertEqual(error.exception.code, 2)
        mock_manager.assert_not_called()

    @patch("weather_app.WeatherManager")
    def test_help_option(
        self, mock_manager: MagicMock
    ) -> None:
        """Verify command-line help displays correctly."""
        output = io.StringIO()

        with redirect_stdout(output):
            with self.assertRaises(SystemExit) as error:
                main(["--help"])

        self.assertEqual(error.exception.code, 0)
        self.assertIn("--city", output.getvalue())
        mock_manager.assert_not_called()

    @patch("weather_app.WeatherDashboard")
    @patch("weather_app.WeatherManager")
    def test_api_failure(
        self, mock_manager: MagicMock,
        mock_dashboard: MagicMock
    ) -> None:
        """Verify an API failure propagates."""
        mock_manager.return_value.get_weather.side_effect = (
            RuntimeError("API unavailable")
        )

        with self.assertRaises(RuntimeError):
            main(["--city", "denver"])

        mock_dashboard.assert_not_called()


if __name__ == "__main__":
    unittest.main()
