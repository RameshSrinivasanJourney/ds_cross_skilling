from crewai import Task

from app.agents.writing_agent import create_writing_agent
from app.tasks.research_task import create_research_task


def create_writing_task() -> Task:

    agent = create_writing_agent()
    research_task = create_research_task()

    return Task(
        description=(
            "Using the research from the previous task, "
            "write a clear explanation of Python lists "
            "versus tuples for a beginner developer. "
            "Include simple examples."
        ),
        expected_output=(
            "A clear explanation of lists and tuples "
            "with examples and practical guidance."
        ),
        agent=agent,
        context=[research_task],
    )