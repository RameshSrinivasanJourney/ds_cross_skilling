from app.agent.memory_agent import MemoryAgent


def test_agent_memory():

    user_id = "employee-001"

    print("\n=== Conversation 1 ===")

    agent = MemoryAgent(
        user_id=user_id
    )

    agent.remember(
        "preferred_city",
        "Chennai",
    )

    print("\nStored Memory:")
    print(
        agent.recall("preferred_city")
    )

    response = agent.ask(
        "What is my preferred city?"
    )

    print("\nAgent Response:")
    print(response)

    agent.close()

    print("\n=== Conversation 2 ===")

    new_agent = MemoryAgent(
        user_id=user_id
    )

    print("\nRecovered Long-Term Memory:")
    print(
        new_agent.recall(
            "preferred_city"
        )
    )

    response = new_agent.ask(
        "Do you remember which city I prefer?"
    )

    print("\nAgent Response:")
    print(response)

    new_agent.close()


if __name__ == "__main__":
    test_agent_memory()