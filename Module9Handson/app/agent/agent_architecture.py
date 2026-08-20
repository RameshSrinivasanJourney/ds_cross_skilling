from typing import Any

from ollama import chat

from app.agent.executor import AgentExecutor
from app.agent.tool_registry import ToolRegistry
from app.tools.weather_tool import get_weather


MODEL_NAME = "llama3.2:3b"

MAX_ITERATIONS = 5


SYSTEM_PROMPT = """
You are a helpful employee assistant.

You can answer questions directly.

Use get_weather when the user asks about
current weather.

Do not invent tool results.

After receiving a tool result, decide whether
more information is required.

Stop when you have enough information to provide
the final answer.
"""


class SingleAgent:
    """A structured single-agent implementation."""

    def __init__(self):
        self.tool_registry = ToolRegistry()

        self.tool_registry.register(
            "get_weather",
            get_weather,
        )

        self.executor = AgentExecutor(
            self.tool_registry
        )

    def _get_tool_definitions(self):
        return [
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": (
                        "Get the current weather "
                        "information for a city."
                    ),
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "city": {
                                "type": "string",
                                "description": (
                                    "City name."
                                ),
                            }
                        },
                        "required": ["city"],
                    },
                },
            }
        ]

    def run(
        self,
        user_question: str,
    ) -> str:

        messages: list[dict[str, Any]] = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": user_question,
            },
        ]

        print("\nRegistered Tools:")
        print(
            self.tool_registry.list_tools()
        )

        for iteration in range(
            1,
            MAX_ITERATIONS + 1,
        ):

            print(
                f"\n--- Agent Iteration "
                f"{iteration} ---"
            )

            response = chat(
                model=MODEL_NAME,
                messages=messages,
                tools=[
                    get_weather
                ],
            )

            assistant_message = (
                response.message
            )

            messages.append(
                assistant_message
            )

            tool_calls = (
                assistant_message.tool_calls
            )

            # -------------------------------
            # Stop condition
            # -------------------------------

            if not tool_calls:

                print(
                    "\nStop Condition:"
                    " No tool call requested."
                )

                return (
                    assistant_message.content
                )

            # -------------------------------
            # Execute tool calls
            # -------------------------------

            for tool_call in tool_calls:

                tool_name = (
                    tool_call.function.name
                )

                arguments = (
                    tool_call.function.arguments
                )

                print("\nTool Call:")
                print(
                    f"Name: {tool_name}"
                )
                print(
                    f"Arguments: {arguments}"
                )

                result = self.executor.execute(
                    tool_name,
                    arguments,
                )

                print("\nTool Result:")
                print(result)

                messages.append(
                    {
                        "role": "tool",
                        "tool_name": tool_name,
                        "content": (
                            self.executor.format_result(
                                result
                            )
                        ),
                    }
                )

        return (
            "The agent stopped because the "
            "maximum iteration limit was reached."
        )