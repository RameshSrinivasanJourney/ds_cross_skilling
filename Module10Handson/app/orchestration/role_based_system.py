from app.agents.critic_agent import critic_agent
from app.agents.executor_agent import executor_agent
from app.agents.planner_agent import planner_agent
from app.agents.researcher_agent import researcher_agent
from app.agents.supervisor_agent import supervisor_agent
from app.agents.writer_agent import writer_agent


def run_role_based_system(
    goal: str,
) -> dict:
    """Run the complete role-based multi-agent system."""

    print("\n=== SUPERVISOR ===")
    print("Starting multi-agent workflow.")

    print("\n=== PLANNER ===")

    plan = planner_agent(goal)
    print(plan)

    print("\n=== RESEARCHER ===")

    research = researcher_agent(
        goal,
        plan,
    )
    print(research)

    print("\n=== EXECUTOR ===")

    execution_result = executor_agent(
        goal,
        plan,
        research,
    )
    print(execution_result)

    print("\n=== WRITER ===")

    draft = writer_agent(
        goal,
        research,
        execution_result,
    )
    print(draft)

    print("\n=== CRITIC ===")

    review = critic_agent(
        goal,
        draft,
    )
    print(review)

    print("\n=== SUPERVISOR FINAL DECISION ===")

    final_result = supervisor_agent(
        goal,
        plan,
        research,
        execution_result,
        draft,
        review,
    )

    print(final_result)

    return {
        "goal": goal,
        "plan": plan,
        "research": research,
        "execution": execution_result,
        "draft": draft,
        "review": review,
        "final": final_result,
    }