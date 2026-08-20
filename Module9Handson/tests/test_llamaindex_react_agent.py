import asyncio

from app.agent.llamaindex_react_agent import (
    create_llamaindex_react_agent,
)


async def run_test():

    agent = create_llamaindex_react_agent()

    question = (
        "Multiply 25 by 4 using the calculator tool."
    )

    print("\nUser:")
    print(question)

    response = await agent.run(
        user_msg=question
    )

    print("\nFinal Result:")
    print(response)


def test_llamaindex_react_agent():

    asyncio.run(run_test())


if __name__ == "__main__":
    test_llamaindex_react_agent()