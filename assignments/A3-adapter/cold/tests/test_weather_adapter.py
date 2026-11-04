
"""Unit tests for the Open-Meteo weather adapter."""

import unittest
from typing import Any

from weather_adapter import WeatherAdapter
from weather_reading import WeatherReading


class TestWeatherAdapter(unittest.TestCase):
    """Test conversion of external API data."""

    def setUp(self) -> None:
        """Create a sample Open-Meteo response."""
        self.data: dict[str, Any] = {
            "current": {
                "temperature_2m": 18.5,
                "apparent_temperature": 17.0,
                "relative_humidity_2m": 45,
                "wind_speed_10m": 12.3,
                "weather_code": 2,
            }
        }

    def test_valid_weather(self) -> None:
        """Test conversion of a valid API response."""
        weather = WeatherAdapter.adapt(
            self.data, "Grand Junction"
        )

        self.assertIsInstance(weather, WeatherReading)
        self.assertEqual(weather.city, "Grand Junction")
        self.assertEqual(weather.temperature_c, 18.5)
        self.assertEqual(weather.feels_like_c, 17.0)
        self.assertEqual(weather.humidity_percent, 45)
        self.assertEqual(weather.wind_speed_kmh, 12.3)
        self.assertEqual(weather.condition, "Partly cloudy")

    def test_unknown_weather_code(self) -> None:
        """Test an unknown weather condition code."""
        self.data["current"]["weather_code"] = 999

        weather = WeatherAdapter.adapt(
            self.data, "Denver"
        )

        self.assertEqual(weather.condition, "Unknown")
        self.assertEqual(weather.city, "Denver")

    def test_missing_current_data(self) -> None:
        """Test a response missing current weather."""
        with self.assertRaises(KeyError):
            WeatherAdapter.adapt({}, "Denver")

    def test_missing_temperature(self) -> None:
        """Test a response missing temperature."""
        del self.data["current"]["temperature_2m"]

        with self.assertRaises(KeyError):
            WeatherAdapter.adapt(self.data, "Denver")

    def test_invalid_temperature(self) -> None:
        """Test temperature that cannot be converted."""
        self.data["current"]["temperature_2m"] = "invalid"

        with self.assertRaises(ValueError):
            WeatherAdapter.adapt(self.data, "Denver")


if __name__ == "__main__":
    unittest.main()
