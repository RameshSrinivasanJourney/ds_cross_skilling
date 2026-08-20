from app.agent.reliable_agent import (
    ReliableAgent,
)


def test_successful_tool():

    agent = ReliableAgent()

    result = agent._execute_tool(
        "successful_tool",
        {
            "value": "hello",
        },
    )

    print("\nSuccessful Tool:")
    print(result)

    assert result["status"] == "success"


def test_unknown_tool():

    agent = ReliableAgent()

    result = agent._execute_tool(
        "does_not_exist",
        {},
    )

    print("\nUnknown Tool:")
    print(result)

    assert result["status"] == "failed"
    assert (
        result["error_type"]
        == "unknown_tool"
    )


def test_failing_tool():

    agent = ReliableAgent()

    result = agent._execute_tool(
        "failing_tool",
        {},
    )

    print("\nFailing Tool:")
    print(result)

    assert result["status"] == "failed"
    assert (
        result["error_type"]
        == "execution_error"
    )


def test_slow_tool_timeout():

    agent = ReliableAgent()

    result = agent._execute_tool(
        "slow_tool",
        {
            "seconds": 5,
        },
    )

    print("\nSlow Tool:")
    print(result)

    assert result["status"] == "failed"
    assert (
        result["error_type"]
        == "timeout"
    )


def test_agent_normal_execution():

    agent = ReliableAgent()

    result = agent.run(
        "What is the weather in Chennai?"
    )

    print("\nAgent Result:")
    print(result)


if __name__ == "__main__":

    test_successful_tool()
    test_unknown_tool()
    test_failing_tool()
    test_slow_tool_timeout()
    test_agent_normal_execution()