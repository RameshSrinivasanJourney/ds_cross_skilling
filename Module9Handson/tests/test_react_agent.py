from app.agent.react_agent import run_react_agent


def test_react_agent():

    question = (
        "First multiply 25 by 4. "
        "Then add 10 to the result. "
        "You must use the available tools for "
        "both operations."
    )

    print("\nUser:")
    print(question)

    result = run_react_agent(
        question
    )

    print("\nFinal Answer:")
    print(result)


if __name__ == "__main__":
    test_react_agent()