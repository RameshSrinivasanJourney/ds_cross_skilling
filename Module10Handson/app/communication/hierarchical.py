from app.agents.analyst_agent import analyst_agent
from app.agents.researcher_agent import researcher_agent
from app.agents.writer_agent import writer_agent


def run_hierarchical(
    goal: str,
) -> dict:
    """Demonstrate manager-controlled communication."""

    print("\n=== HIERARCHICAL ===")

    print("Manager → Researcher")

    research = researcher_agent(
        goal
    )

    print("Manager → Analyst")

    analysis = analyst_agent(
        goal,
        research,
    )

    print("Manager → Writer")

    draft = writer_agent(
        goal,
        research,
        analysis,
    )

    return {
        "pattern": "hierarchical",
        "research": research,
        "analysis": analysis,
        "draft": draft,
    }