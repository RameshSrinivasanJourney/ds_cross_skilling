import asyncio

from app.agent.llamaindex_tools_agent import (
    create_llamaindex_tools_agent,
)


async def run_test():

    agent = create_llamaindex_tools_agent()

    response = await agent.run(
        user_msg=(
            "Multiply 25 by 4 using "
            "the calculator tool."
        )
    )

    print("\nFinal Answer:")
    print(response)


def test_llamaindex_tools_agent():

    asyncio.run(run_test())


if __name__ == "__main__":
    test_llamaindex_tools_agent()