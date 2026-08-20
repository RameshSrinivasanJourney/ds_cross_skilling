from crewai import Crew, Process

from app.agents.research_agent import create_research_agent
from app.agents.writing_agent import create_writing_agent

from app.tasks.research_task import create_research_task
from app.tasks.writing_task import create_writing_task


def create_research_writing_crew() -> Crew:

    research_agent = create_research_agent()
    writing_agent = create_writing_agent()

    research_task = create_research_task()
    writing_task = create_writing_task()

    return Crew(
        agents=[
            research_agent,
            writing_agent,
        ],
        tasks=[
            research_task,
            writing_task,
        ],
        process=Process.sequential,
        verbose=True,
    )