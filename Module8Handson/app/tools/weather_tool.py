def get_weather(city: str) -> dict:
    """Return sample weather information for a city."""

    return {
        "city": city,
        "temperature": 32,
        "unit": "Celsius",
        "condition": "Sunny"
    }