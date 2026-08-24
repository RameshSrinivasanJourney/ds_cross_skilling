from app.memory.memory_manager import (
    MemoryManager,
)


def test_memory_types():

    memory = MemoryManager()

    # ========================================
    # 1. In-context / short-term memory
    # ========================================

    memory.add_message(
        "user",
        "My preferred city is Chennai.",
    )

    memory.add_message(
        "assistant",
        "I will remember that.",
    )

    print("\n=== 1. SHORT-TERM MEMORY ===")

    print(
        memory.get_context()
    )

    # ========================================
    # 2. External / long-term memory
    # ========================================

    memory.save_long_term(
        "preferred_city",
        "Chennai",
    )

    print("\n=== 2. LONG-TERM MEMORY ===")

    print(
        memory.get_long_term(
            "preferred_city"
        )
    )

    # ========================================
    # 3. Episodic memory
    # ========================================

    memory.remember_event(
        event="User asked about Chennai weather.",
        details={
            "city": "Chennai",
            "topic": "weather",
        },
    )

    print("\n=== 3. EPISODIC MEMORY ===")

    for event in memory.episodic:

        print(
            f"Event: {event.event}"
        )

        print(
            f"Time: {event.timestamp}"
        )

        print(
            f"Details: {event.details}"
        )

    # ========================================
    # 4. Semantic memory
    # ========================================

    memory.remember_fact(
        "preferred_city",
        "Chennai",
    )

    memory.remember_fact(
        "role",
        "Software Architect",
    )

    print("\n=== 4. SEMANTIC MEMORY ===")

    print(
        "Preferred City:",
        memory.get_fact(
            "preferred_city"
        ),
    )

    print(
        "Role:",
        memory.get_fact(
            "role"
        ),
    )

    # ========================================
    # 5. Procedural memory
    # ========================================

    memory.remember_procedure(
        "submit_leave_request",
        [
            "Open employee portal.",
            "Select Leave.",
            "Choose leave type.",
            "Enter dates.",
            "Submit request.",
        ],
    )

    print("\n=== 5. PROCEDURAL MEMORY ===")

    procedure = (
        memory.get_procedure(
            "submit_leave_request"
        )
    )

    for index, step in enumerate(
        procedure or [],
        start=1,
    ):

        print(
            f"{index}. {step}"
        )


if __name__ == "__main__":
    test_memory_types()