from app.agent.langchain_tools_agent import (
    create_langchain_tools_agent,
)


def test_langchain_tools_agent():

    agent = create_langchain_tools_agent()

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "Multiply 25 by 4 using "
                        "the calculator tool."
                    ),
                }
            ]
        }
    )

    print("\nAgent Messages:")

    for index, message in enumerate(
        result["messages"],
        start=1,
    ):
        print(
            f"\n--- Message {index} ---"
        )
        print(message)

    print("\nFinal Answer:")
    print(
        result["messages"][-1].content
    )


if __name__ == "__main__":
    test_langchain_tools_agent()