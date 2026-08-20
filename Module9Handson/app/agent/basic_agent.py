from ollama import chat

from app.tools.weather_tool import get_weather


MODEL_NAME = "llama3.2:3b"


AVAILABLE_TOOLS = {
    "get_weather": get_weather,
}


SYSTEM_PROMPT = """
You are a helpful employee assistant.

When the user asks about current weather,
use the get_weather tool.

After receiving the tool result, provide
a concise final answer.

Do not invent weather information.
"""


def run_agent(user_question: str) -> str:
    """Run a minimal single-agent loop."""

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": user_question,
        },
    ]

    while True:

        response = chat(
            model=MODEL_NAME,
            messages=messages,
            tools=[get_weather],
        )

        # Add the assistant response to the conversation.
        messages.append(response.message)

        tool_calls = response.message.tool_calls

        # ------------------------------------------
        # No tool call -> agent is finished
        # ------------------------------------------

        if not tool_calls:
            return response.message.content

        # ------------------------------------------
        # Agent requested one or more tools
        # ------------------------------------------

        for tool_call in tool_calls:

            tool_name = tool_call.function.name
            arguments = tool_call.function.arguments

            print("\nAgent Action:")
            print(f"Tool     : {tool_name}")
            print(f"Arguments: {arguments}")

            tool_function = AVAILABLE_TOOLS.get(
                tool_name
            )

            if tool_function is None:
                raise ValueError(
                    f"Unknown tool: {tool_name}"
                )

            # --------------------------------------
            # ACT
            # --------------------------------------

            result = tool_function(
                **arguments
            )

            print("\nAgent Observation:")
            print(result)

            # --------------------------------------
            # Send observation back to the LLM
            # --------------------------------------

            messages.append(
                {
                    "role": "tool",
                    "tool_name": tool_name,
                    "content": str(result),
                }
            )