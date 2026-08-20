from app.agent.agent_architecture import (
    SingleAgent,
)


def test_agent_architecture():

    agent = SingleAgent()

    question = (
        "What is the weather in Chennai?"
    )

    print("\nUser:")
    print(question)

    result = agent.run(
        question
    )

    print("\nFinal Answer:")
    print(result)


if __name__ == "__main__":
    test_agent_architecture()