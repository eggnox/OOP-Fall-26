
"""Unit tests for the Singleton WeatherManager."""

import unittest
from typing import cast
from unittest.mock import Mock, patch

from weather_client import WeatherClient
from weather_manager import WeatherManager
from weather_reading import WeatherReading


class TestWeatherManager(unittest.TestCase):
    """Test Singleton behavior and weather request delegation."""

    def setUp(self) -> None:
        """Reset the Singleton and prepare a mocked client."""
        singleton_patch = patch.object(
            WeatherManager, "_instance", None
        )
        singleton_patch.start()
        self.addCleanup(singleton_patch.stop)

        self.mock_client = Mock(spec=WeatherClient)
        self.reading = WeatherReading(
            "Grand Junction", 18.5, 17.0,
            45, 12.3, "Partly cloudy"
        )
        self.mock_client.fetch_current.return_value = self.reading

    def create_manager(self) -> WeatherManager:
        """Create a manager with the mocked weather client."""
        return WeatherManager(
            client=cast(WeatherClient, self.mock_client)
        )

    def test_singleton_same_instance(self) -> None:
        """Verify that two managers share one instance."""
        manager1 = self.create_manager()
        manager2 = WeatherManager()

        self.assertIs(manager1, manager2)

    def test_injected_client(self) -> None:
        """Verify that dependency injection works."""
        manager = self.create_manager()

        self.assertIs(manager.client, self.mock_client)

    def test_default_client(self) -> None:
        """Verify that a default client is created."""
        manager = WeatherManager()

        self.assertIsInstance(manager.client, WeatherClient)

    def test_client_not_replaced(self) -> None:
        """Verify that a second initialization keeps the client."""
        manager1 = self.create_manager()
        another_client = Mock(spec=WeatherClient)

        manager2 = WeatherManager(
            client=cast(WeatherClient, another_client)
        )

        self.assertIs(manager1, manager2)
        self.assertIs(manager2.client, self.mock_client)

    def test_get_weather_result(self) -> None:
        """Verify that the manager returns the weather reading."""
        manager = self.create_manager()

        result = manager.get_weather(
            "Grand Junction", 39.0639, -108.5506
        )

        self.assertIs(result, self.reading)

    def test_get_weather_arguments(self) -> None:
        """Verify the correct coordinates are forwarded."""
        manager = self.create_manager()

        manager.get_weather("Denver", 39.7392, -104.9903)

        self.mock_client.fetch_current.assert_called_once_with(
            city="Denver",
            latitude=39.7392,
            longitude=-104.9903,
        )

    def test_multiple_weather_requests(self) -> None:
        """Verify that the manager handles multiple requests."""
        manager = self.create_manager()

        manager.get_weather("Denver", 39.7392, -104.9903)
        manager.get_weather("Grand Junction", 39.0639, -108.5506)

        self.assertEqual(
            self.mock_client.fetch_current.call_count, 2
        )

    def test_weather_error_propagates(self) -> None:
        """Verify that API errors propagate to the caller."""
        self.mock_client.fetch_current.side_effect = RuntimeError(
            "API unavailable"
        )
        manager = self.create_manager()

        with self.assertRaises(RuntimeError):
            manager.get_weather("Denver", 39.7392, -104.9903)


if __name__ == "__main__":
    unittest.main()
