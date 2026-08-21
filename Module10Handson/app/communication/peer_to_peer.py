from app.agents.analyst_agent import analyst_agent
from app.agents.researcher_agent import researcher_agent
from app.agents.writer_agent import writer_agent


def run_peer_to_peer(
    goal: str,
) -> dict:
    """Demonstrate direct agent-to-agent handoffs."""

    print("\n=== PEER-TO-PEER ===")

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

    return {
        "pattern": "peer-to-peer",
        "research": research,
        "analysis": analysis,
        "draft": draft,
    }