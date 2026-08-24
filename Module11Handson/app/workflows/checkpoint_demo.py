from typing import TypedDict

from langgraph.checkpoint.sqlite import (
    SqliteSaver,
)
from langgraph.graph import (
    END,
    START,
    StateGraph,
)


class GraphState(TypedDict):
    counter: int
    message: str


def increment(
    state: GraphState,
) -> dict:

    return {
        "counter": state["counter"] + 1,
        "message": (
            f"Counter is now "
            f"{state['counter'] + 1}"
        ),
    }


def build_checkpointed_graph(
    connection,
):

    builder = StateGraph(
        GraphState
    )

    builder.add_node(
        "increment",
        increment,
    )

    builder.add_edge(
        START,
        "increment",
    )

    builder.add_edge(
        "increment",
        END,
    )

    checkpointer = SqliteSaver(
        connection
    )

    return (
        builder.compile(
            checkpointer=checkpointer
        )
    )