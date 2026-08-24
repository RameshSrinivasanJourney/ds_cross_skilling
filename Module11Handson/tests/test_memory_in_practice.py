from app.agents.memory_enabled_agent import (
    MemoryEnabledAgent,
)
from app.memory.faiss_memory_store import (
    FAISSMemoryStore,
)
from app.memory.profile_memory import (
    seed_user_profile,
)
from app.memory.project_memory import (
    seed_project_context,
)


USER_ID = "employee-001"


def test_memory_in_practice():

    store = FAISSMemoryStore()

    print(
        "\n=== SESSION 1: SEED MEMORY ==="
    )

    seed_user_profile(
        store,
        USER_ID,
    )

    seed_project_context(
        store,
        USER_ID,
    )

    print(
        "Profile and project memories stored."
    )

    # -----------------------------------------
    # Session 1
    # -----------------------------------------

    agent = MemoryEnabledAgent(
        user_id=USER_ID,
        store=store,
    )

    question_1 = (
        "What do you remember about my "
        "professional background?"
    )

    print(
        "\nUser:"
    )
    print(question_1)

    answer_1 = agent.ask(
        question_1
    )

    print(
        "\nAgent:"
    )
    print(answer_1)

    # -----------------------------------------
    # New logical session
    # -----------------------------------------

    print(
        "\n=== SESSION 2 ==="
    )

    new_agent = MemoryEnabledAgent(
        user_id=USER_ID,
        store=store,
    )

    question_2 = (
        "What am I currently learning, "
        "and what did I finish before this?"
    )

    print(
        "\nUser:"
    )
    print(question_2)

    answer_2 = new_agent.ask(
        question_2
    )

    print(
        "\nAgent:"
    )
    print(answer_2)


if __name__ == "__main__":
    test_memory_in_practice()