from app.agents.analyst_agent import analyst_agent
from app.agents.researcher_agent import researcher_agent
from app.agents.reviewer_agent import reviewer_agent
from app.agents.writer_agent import writer_agent


def run_pipeline(
    goal: str,
) -> dict:
    """Demonstrate linear agent handoff."""

    print("\n=== PIPELINE ===")

    research = researcher_agent(
        goal
    )

    analysis = analyst_agent(
        goal,
        research,
    )

    draft = writer_agent(
        goal,
        research,
        analysis,
    )

    review = reviewer_agent(
        goal,
        draft,
    )

    return {
        "pattern": "pipeline",
        "research": research,
        "analysis": analysis,
        "draft": draft,
        "review": review,
    }