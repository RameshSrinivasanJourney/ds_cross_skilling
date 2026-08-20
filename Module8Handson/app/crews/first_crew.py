from crewai import Crew, Process

from app.agents.first_agent import create_first_agent
from app.tasks.first_task import create_first_task


def create_first_crew() -> Crew:
    """Create the first CrewAI crew."""

    agent = create_first_agent()
    task = create_first_task()

    return Crew(
        agents=[agent],
        tasks=[task],
        process=Process.sequential,
        verbose=True,
    )