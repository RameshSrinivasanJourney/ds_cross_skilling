from typing import TypedDict

from langgraph.checkpoint.memory import (
    InMemorySaver,
)
from langgraph.graph import (
    END,
    START,
    StateGraph,
)
from langgraph.types import (
    Command,
    interrupt,
)

from app.workflows.audit import (
    record_audit,
)


class ApprovalState(TypedDict):
    """State carried through the HITL workflow."""

    request: str
    plan: list[str]
    approved_plan: list[str]
    decision: str
    status: str

def create_plan(
    state: ApprovalState,
) -> dict:

    plan = [
        "Research the relevant leave policy.",
        "Analyze eligibility and important restrictions.",
        "Prepare an employee-facing explanation.",
        "Review the final response.",
    ]

    record_audit(
        "plan_created",
        {
            "request": state["request"],
            "plan": plan,
        },
    )

    return {
        "plan": plan,
        "status": "awaiting_human_review",
    }

def human_review(
    state: ApprovalState,
) -> dict:

    record_audit(
        "human_review_requested",
        {
            "plan": state["plan"],
        },
    )

    decision = interrupt(
        {
            "type": "plan_review",
            "message": (
                "Review the proposed multi-agent plan."
            ),
            "plan": state["plan"],
            "allowed_decisions": [
                "approve",
                "edit",
                "reject",
            ],
        }
    )

    decision_type = decision.get(
        "decision"
    )

    if decision_type == "approve":

        approved_plan = state["plan"]

    elif decision_type == "edit":

        approved_plan = decision.get(
            "plan",
            state["plan"],
        )

    elif decision_type == "reject":

        approved_plan = []

    else:

        raise ValueError(
            f"Unsupported human decision: "
            f"{decision_type}"
        )

    record_audit(
        "human_decision",
        {
            "decision": decision_type,
            "approved_plan": approved_plan,
        },
    )

    return {
        "decision": decision_type,
        "approved_plan": approved_plan,
        "status": (
            "approved"
            if decision_type in {
                "approve",
                "edit",
            }
            else "rejected"
        ),
    }

def execute_plan(
    state: ApprovalState,
) -> dict:

    if state["decision"] == "reject":

        record_audit(
            "execution_skipped",
            {
                "reason": "human_rejected_plan"
            },
        )

        return {
            "status": "rejected",
        }

    print("\n=== EXECUTING APPROVED PLAN ===")

    for index, step in enumerate(
        state["approved_plan"],
        start=1,
    ):
        print(
            f"{index}. {step}"
        )

    record_audit(
        "execution_started",
        {
            "plan": state["approved_plan"],
        },
    )

    record_audit(
        "execution_completed",
        {
            "plan": state["approved_plan"],
        },
    )

    return {
        "status": "completed",
    }

def route_after_review(
    state: ApprovalState,
) -> str:

    if state["decision"] == "reject":
        return "end"

    return "execute"

def build_approval_graph():

    builder = StateGraph(
        ApprovalState
    )

    builder.add_node(
        "create_plan",
        create_plan,
    )

    builder.add_node(
        "human_review",
        human_review,
    )

    builder.add_node(
        "execute_plan",
        execute_plan,
    )

    builder.add_edge(
        START,
        "create_plan",
    )

    builder.add_edge(
        "create_plan",
        "human_review",
    )

    builder.add_conditional_edges(
        "human_review",
        route_after_review,
        {
            "execute": "execute_plan",
            "end": END,
        },
    )

    builder.add_edge(
        "execute_plan",
        END,
    )

    checkpointer = InMemorySaver()

    return builder.compile(
        checkpointer=checkpointer
    )

