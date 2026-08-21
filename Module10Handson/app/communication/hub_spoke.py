from app.agents.critic_agent import critic_agent
from app.agents.researcher_agent import researcher_agent
from app.agents.writer_agent import writer_agent


def run_hub_and_spoke(
    goal: str,
) -> dict:
    """Supervisor communicates with specialists."""

    print("\n=== HUB-AND-SPOKE ===")

    research = researcher_agent(
        goal
    )

    draft = writer_agent(
        goal=goal,
        research=research,
        execution_result=(
            "No separate executor was required "
            "for this demonstration."
        ),
    )

    review = critic_agent(
        goal=goal,
        draft=draft,
    )

    return {
        "pattern": "hub-and-spoke",
        "research": research,
        "draft": draft,
        "review": review,
    }