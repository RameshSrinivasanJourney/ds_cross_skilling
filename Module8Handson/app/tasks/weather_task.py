from crewai import Task

from app.agents.weather_agent import create_weather_agent


def create_weather_task() -> Task:

    agent = create_weather_agent()

    return Task(
        description=(
            "Tell me the current weather in Chennai. "
            "Use the weather tool to retrieve the "
            "information. Do not guess the weather."
        ),
        expected_output=(
            "A concise response containing the current "
            "temperature and weather condition in Chennai."
        ),
        agent=agent,
    )