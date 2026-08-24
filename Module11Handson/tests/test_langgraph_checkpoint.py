import sqlite3

from app.workflows.checkpoint_demo import (
    build_checkpointed_graph,
)


def test_langgraph_checkpoint():

    connection = sqlite3.connect(
        "data/langgraph_checkpoints.db",
        check_same_thread=False,
    )

    graph = build_checkpointed_graph(
        connection
    )

    config = {
        "configurable": {
            "thread_id": "module11-demo-001"
        }
    }

    print(
        "\n=== FIRST GRAPH RUN ==="
    )

    result = graph.invoke(
        {
            "counter": 0,
            "message": "Starting",
        },
        config,
    )

    print(result)

    print(
        "\n=== SAVED GRAPH STATE ==="
    )

    state = graph.get_state(
        config
    )

    print(
        state.values
    )

    print(
        "\n=== CHECKPOINT HISTORY ==="
    )

    history = list(
        graph.get_state_history(
            config
        )
    )

    print(
        f"Checkpoint count: "
        f"{len(history)}"
    )

    assert (
        result["counter"] == 1
    )

    assert (
        state.values["counter"] == 1
    )

    assert (
        len(history) > 0
    )

    connection.close()


if __name__ == "__main__":
    test_langgraph_checkpoint()