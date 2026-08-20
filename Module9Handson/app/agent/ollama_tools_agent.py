from ollama import chat

from app.tools.calculator_tool import multiply


MODEL_NAME = "llama3.2:3b"


def run_ollama_tools_agent(
    user_question: str,
) -> str:
    """Run a local Ollama tool-calling agent."""

    messages = [
        {
            "role": "system",
            "content": (
                "You are a calculator assistant. "
                "Use the available calculator tool when "
                "a calculation is required. "
                "Return the final answer clearly."
            ),
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
            tools=[multiply],
        )

        assistant_message = response.message

        messages.append(
            assistant_message
        )

        tool_calls = (
            assistant_message.tool_calls
        )

        if not tool_calls:

            return assistant_message.content

        for tool_call in tool_calls:

            tool_name = (
                tool_call.function.name
            )

            arguments = (
                tool_call.function.arguments
            )

            print("\nTool Call:")
            print(f"Name: {tool_name}")
            print(f"Arguments: {arguments}")

            if tool_name == "multiply":

                result = multiply(
                    **arguments
                )

            else:

                raise ValueError(
                    f"Unknown tool: {tool_name}"
                )

            print("\nTool Result:")
            print(result)

            messages.append(
                {
                    "role": "tool",
                    "tool_name": tool_name,
                    "content": str(result),
                }
            )