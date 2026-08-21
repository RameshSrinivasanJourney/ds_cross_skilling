from app.workflows.human_approval_workflow import (
    build_approval_graph,
)
from langgraph.types import Command


def run_human_approval_test(
    human_decision: dict,
):

    graph = build_approval_graph()

    config = {
        "configurable": {
            "thread_id": "module10-hitl-001"
        }
    }

    initial_state = {
        "request": (
            "Prepare an employee-facing explanation "
            "of how to approach a leave-policy question."
        ),
        "plan": [],
        "approved_plan": [],
        "decision": "",
        "status": "started",
    }

    print("\n=== START WORKFLOW ===")

    result = graph.invoke(
        initial_state,
        config=config,
    )

    print("\n=== INTERRUPT ===")

    interrupt_data = result.get(
        "__interrupt__",
        [],
    )

    print(interrupt_data)

    print("\n=== HUMAN DECISION ===")
    print(human_decision)

    print("\n=== RESUMING WORKFLOW ===")

    final_result = graph.invoke(
        Command(
            resume=human_decision
        ),
        config=config,
    )

    print("\n=== FINAL STATE ===")
    print(final_result)

    return final_result


def test_approve_plan():

    run_human_approval_test(
        {
            "decision": "approve",
        }
    )


if __name__ == "__main__":
    test_approve_plan()