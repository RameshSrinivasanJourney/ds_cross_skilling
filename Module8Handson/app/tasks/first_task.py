from crewai import Task

from app.agents.first_agent import create_first_agent


def create_first_task() -> Task:
    """Create the first CrewAI task."""

    agent = create_first_agent()

    return Task(
        description=(
            "Explain the difference between a Python list "
            "and a Python tuple. Give one simple example "
            "of each and explain when each should be used."
        ),
        expected_output=(
            "A clear beginner-friendly explanation containing "
            "the differences between lists and tuples, one "
            "example of each, and guidance on when to use each."
        ),
        agent=agent,
    )