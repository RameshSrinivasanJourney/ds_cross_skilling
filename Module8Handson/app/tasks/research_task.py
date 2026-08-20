from crewai import Task

from app.agents.research_agent import create_research_agent


def create_research_task() -> Task:

    agent = create_research_agent()

    return Task(
        description=(
            "Research the key differences between "
            "Python lists and tuples. Cover mutability, "
            "performance considerations, syntax, and "
            "common use cases."
        ),
        expected_output=(
            "Accurate technical research notes covering "
            "lists, tuples, their differences, and "
            "appropriate use cases."
        ),
        agent=agent,
    )