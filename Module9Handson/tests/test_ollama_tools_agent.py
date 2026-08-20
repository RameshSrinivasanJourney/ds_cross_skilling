from app.agent.ollama_tools_agent import (
    run_ollama_tools_agent,
)


def test_ollama_tools_agent():

    question = (
        "Multiply 25 by 4 using the calculator tool."
    )

    print("\nUser:")
    print(question)

    result = run_ollama_tools_agent(
        question
    )

    print("\nFinal Answer:")
    print(result)


if __name__ == "__main__":
    test_ollama_tools_agent()