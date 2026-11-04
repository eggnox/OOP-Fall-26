
"""Unit tests for WeatherClient using mocking and patching."""

import io
import json
import unittest
from unittest.mock import patch
from urllib.error import URLError
from urllib.parse import parse_qs, urlsplit

from weather_client import WeatherClient


class TestWeatherClient(unittest.TestCase):
    """Test API requests without making real network calls."""

    def setUp(self) -> None:
        """Create a sample API response."""
        self.sample = {
            "current": {
                "temperature_2m": 18.5,
                "apparent_temperature": 17.0,
                "relative_humidity_2m": 45,
                "wind_speed_10m": 12.3,
                "weather_code": 2,
            }
        }

    def test_default_timeout(self) -> None:
        """Check the default request timeout."""
        client = WeatherClient()
        self.assertEqual(client.timeout, 10.0)

    def test_custom_timeout(self) -> None:
        """Check a custom request timeout."""
        client = WeatherClient(timeout=5.0)
        self.assertEqual(client.timeout, 5.0)

    def test_invalid_timeout(self) -> None:
        """Reject zero and negative timeouts."""
        for timeout in (0.0, -5.0):
            with self.subTest(timeout=timeout):
                with self.assertRaises(ValueError):
                    WeatherClient(timeout=timeout)

    @patch("weather_client.urlopen")
    def test_successful_request(self, mock_urlopen) -> None:
        """Test a successful mocked API response."""
        response = io.BytesIO(
            json.dumps(self.sample).encode("utf-8")
        )
        mock_urlopen.return_value.__enter__.return_value = response

        client = WeatherClient()
        weather = client.fetch_current(
            "Grand Junction", 39.0639, -108.5506
        )

        self.assertEqual(weather.city, "Grand Junction")
        self.assertEqual(weather.temperature_c, 18.5)
        self.assertEqual(weather.humidity_percent, 45)
        self.assertEqual(weather.condition, "Partly cloudy")

        self.assertEqual(
            mock_urlopen.call_args.kwargs["timeout"], 10.0
        )

    @patch("weather_client.urlopen")
    def test_request_parameters(self, mock_urlopen) -> None:
        """Verify URL parameters sent to the API."""
        response = io.BytesIO(
            json.dumps(self.sample).encode("utf-8")
        )
        mock_urlopen.return_value.__enter__.return_value = response

        client = WeatherClient(timeout=7.0)
        client.fetch_current("Denver", 39.7392, -104.9903)

        url = mock_urlopen.call_args.args[0]
        params = parse_qs(urlsplit(url).query)

        self.assertEqual(params["latitude"], ["39.7392"])
        self.assertEqual(params["longitude"], ["-104.9903"])
        self.assertEqual(params["temperature_unit"], ["celsius"])
        self.assertEqual(params["wind_speed_unit"], ["kmh"])
        self.assertEqual(
            mock_urlopen.call_args.kwargs["timeout"], 7.0
        )

    @patch("weather_client.urlopen")
    def test_network_error(self, mock_urlopen) -> None:
        """Handle a failed network request."""
        mock_urlopen.side_effect = URLError("No connection")

        client = WeatherClient()

        with self.assertRaises(RuntimeError):
            client.fetch_current("Denver", 39.7, -105.0)

    @patch("weather_client.urlopen")
    def test_request_timeout(self, mock_urlopen) -> None:
        """Handle an API request timeout."""
        mock_urlopen.side_effect = TimeoutError("Timed out")

        client = WeatherClient()

        with self.assertRaises(RuntimeError):
            client.fetch_current("Denver", 39.7, -105.0)

    @patch("weather_client.urlopen")
    def test_invalid_json(self, mock_urlopen) -> None:
        """Handle an invalid JSON response."""
        response = io.BytesIO(b"{invalid json")
        mock_urlopen.return_value.__enter__.return_value = response

        client = WeatherClient()

        with self.assertRaises(RuntimeError):
            client.fetch_current("Denver", 39.7, -105.0)

    @patch("weather_client.urlopen")
    def test_missing_weather_fields(self, mock_urlopen) -> None:
        """Check behavior when API fields are missing."""
        response = io.BytesIO(b'{"current": {}}')
        mock_urlopen.return_value.__enter__.return_value = response

        client = WeatherClient()

        with self.assertRaises(KeyError):
            client.fetch_current("Denver", 39.7, -105.0)


if __name__ == "__main__":
    unittest.main()
