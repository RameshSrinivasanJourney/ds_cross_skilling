from langchain_core.messages import HumanMessage

from app.agent.langgraph_agent import (
    build_agent_graph,
)


def test_langgraph_agent():

    graph = build_agent_graph()

    question = (
        "Multiply 25 by 4 using the calculator tool."
    )

    print("\nUser:")
    print(question)

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content=question
                )
            ]
        }
    )

    print("\nGraph Messages:")

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
    test_langgraph_agent()