from app.agent.basic_agent import run_agent


def test_basic_agent():

    question = (
        "What is the weather in Chennai?"
    )

    print("\nUser:")
    print(question)

    result = run_agent(
        question
    )

    print("\nFinal Answer:")
    print(result)


if __name__ == "__main__":
    test_basic_agent()