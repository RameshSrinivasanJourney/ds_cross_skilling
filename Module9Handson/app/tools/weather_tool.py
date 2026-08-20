def get_weather(city: str) -> dict:
    """
    Get the current weather information for a city.

    Args:
        city: The name of the city.

    Returns:
        A dictionary containing city, temperature,
        unit, and condition.
    """

    return {
        "city": city,
        "temperature": 32,
        "unit": "Celsius",
        "condition": "Sunny",
    }