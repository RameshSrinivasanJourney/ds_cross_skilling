from crewai.tools import tool

from app.tools.weather_tool import get_weather


@tool("get_current_weather")
def get_current_weather(city: str) -> str:
    """
    Get the current weather for a city.

    Use this tool when the user asks about
    the current weather or temperature.
    """

    result = get_weather(city)

    return (
        f"City: {result['city']}\n"
        f"Temperature: {result['temperature']} "
        f"{result['unit']}\n"
        f"Condition: {result['condition']}"
    )