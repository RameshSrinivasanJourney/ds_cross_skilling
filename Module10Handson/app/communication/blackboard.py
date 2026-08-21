from typing import Any

from app.agents.analyst_agent import analyst_agent
from app.agents.researcher_agent import researcher_agent
from app.agents.writer_agent import writer_agent


class Blackboard:
    """Shared state used by multiple agents."""

    def __init__(self):
        self.state: dict[str, Any] = {}

    def write(
        self,
        key: str,
        value: Any,
    ) -> None:
        self.state[key] = value

    def read(
        self,
        key: str,
    ) -> Any:
        return self.state.get(key)


def run_blackboard(
    goal: str,
) -> dict:
    """Demonstrate shared-state communication."""

    print("\n=== BLACKBOARD ===")

    board = Blackboard()

    research = researcher_agent(
        goal
    )

    board.write(
        "research",
        research,
    )

    print(
        "Blackboard updated: research"
    )

    analysis = analyst_agent(
        goal,
        board.read("research"),
    )

    board.write(
        "analysis",
        analysis,
    )

    print(
        "Blackboard updated: analysis"
    )

    draft = writer_agent(
        goal,
        board.read("research"),
        board.read("analysis"),
    )

    board.write(
        "draft",
        draft,
    )

    print(
        "Blackboard updated: draft"
    )

    return {
        "pattern": "blackboard",
        "state": board.state,
    }