from crewai import Crew, Process

from app.agents.hr_agent import create_hr_agent
from app.agents.research_agent import create_research_agent
from app.agents.writing_agent import create_writing_agent
from app.agents.manager_agent import create_manager_agent


def create_hierarchical_crew() -> Crew:

    hr_agent = create_hr_agent()
    research_agent = create_research_agent()
    writing_agent = create_writing_agent()
    manager_agent = create_manager_agent()

    return Crew(
        agents=[
            hr_agent,
            research_agent,
            writing_agent,
        ],
        tasks=[],
        process=Process.hierarchical,
        manager_agent=manager_agent,
        verbose=True,
    )