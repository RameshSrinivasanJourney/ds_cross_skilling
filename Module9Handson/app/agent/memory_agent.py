from typing import Any

from ollama import chat

from app.memory.long_term_memory import (
    LongTermMemory,
)
from app.tools.weather_tool import get_weather


MODEL_NAME = "llama3.2:3b"


class MemoryAgent:
    """Single agent with short-term and long-term memory."""

    def __init__(self, user_id: str):
        self.user_id = user_id
        self.memory = LongTermMemory()

        self.messages: list[dict[str, Any]] = [
            {
                "role": "system",
                "content": (
                    "You are an employee assistant.\n\n"
                    "Use the conversation history and the "
                    "provided long-term memory when answering.\n\n"
                    "Only use the weather tool when the user "
                    "explicitly asks about weather.\n\n"
                    "Do not invent personal information."
                ),
            }
        ]

    def remember(
        self,
        key: str,
        value: str,
    ) -> None:
        """Store long-term memory."""

        self.memory.save(
            self.user_id,
            key,
            value,
        )

    def recall(
        self,
        key: str,
    ) -> str | None:
        """Retrieve long-term memory."""

        return self.memory.get(
            self.user_id,
            key,
        )

    def _inject_memory(self) -> None:
        """Inject relevant long-term memory into context."""

        preferred_city = self.recall(
            "preferred_city"
        )

        memory_message = (
            "Known long-term memory for this user:\n"
            f"- preferred_city: {preferred_city}"
        )

        self.messages.append(
            {
                "role": "system",
                "content": memory_message,
            }
        )

    def ask(
        self,
        question: str,
    ) -> str:
        """Send a question to the agent."""

        self._inject_memory()

        self.messages.append(
            {
                "role": "user",
                "content": question,
            }
        )

        response = chat(
            model=MODEL_NAME,
            messages=self.messages,
            tools=[get_weather],
        )

        assistant_message = response.message

        tool_calls = (
            assistant_message.tool_calls
        )

        if tool_calls:

            for tool_call in tool_calls:

                tool_name = (
                    tool_call.function.name
                )

                arguments = (
                    tool_call.function.arguments
                )

                if tool_name != "get_weather":
                    raise ValueError(
                        f"Unknown tool: {tool_name}"
                    )

                result = get_weather(
                    **arguments
                )

                print("\nTool Result:")
                print(result)

                self.messages.append(
                    assistant_message
                )

                self.messages.append(
                    {
                        "role": "tool",
                        "tool_name": tool_name,
                        "content": str(result),
                    }
                )

            final_response = chat(
                model=MODEL_NAME,
                messages=self.messages,
            )

            self.messages.append(
                final_response.message
            )

            return final_response.message.content

        self.messages.append(
            assistant_message
        )

        return assistant_message.content

    def close(self) -> None:
        """Release resources."""

        self.memory.close()