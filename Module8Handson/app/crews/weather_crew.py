from crewai import Crew, Process

from app.agents.weather_agent import create_weather_agent
from app.tasks.weather_task import create_weather_task


def create_weather_crew() -> Crew:

    agent = create_weather_agent()
    task = create_weather_task()

    return Crew(
        agents=[agent],
        tasks=[task],
        process=Process.sequential,
        verbose=True,
    )