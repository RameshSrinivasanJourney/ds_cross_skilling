import json

import ollama

from app.config.config import settings


class OllamaService:
    """Service responsible for communicating with the local Ollama model."""

    def __init__(self):
        self.client = ollama.Client(host=settings.ollama_host)
        self.model = settings.ollama_model

    def chat(self, messages: list[dict]) -> str:
        """Send messages to Ollama and return the response content."""

        response = self.client.chat(
            model=self.model,
            messages=messages,
        )

        return response["message"]["content"]

    def chat_with_tools(
        self,
        messages: list[dict],
        tools: list[dict],
    ):
        """Send messages and tool definitions to Ollama."""

        return self.client.chat(
            model=self.model,
            messages=messages,
            tools=tools,
        )

    def chat_with_tool_execution(self, messages, tools, tool_registry):
        """
        Execute model-requested tools and return the final response.
        """

        response = self.chat_with_tools(
            messages=messages,
            tools=tools,
        )

        tool_calls = response["message"].get("tool_calls", [])

        if not tool_calls:
            return response

        messages.append(response["message"])

        for tool_call in tool_calls:

            tool_name = tool_call.function.name
            arguments = tool_call.function.arguments

            tool_function = tool_registry.get(tool_name)

            if tool_function is None:
                raise ValueError(
                    f"Unknown tool requested: {tool_name}"
                )

            tool_result = tool_function(**arguments)

            messages.append(
                {
                    "role": "tool",
                    "tool_name": tool_name,
                    "content": json.dumps(tool_result),
                }
            )

        return self.chat(messages)


    def chat_with_multi_turn_tools(
        self,
        messages,
        tools,
        tool_registry,
        max_turns=5,
    ):
        """
        Continue the conversation while the model
        requests tool execution.
        """

        for _ in range(max_turns):

            response = self.chat_with_tools(
                messages=messages,
                tools=tools,
            )

            tool_calls = response["message"].get(
                "tool_calls",
                []
            )

            # No tool call means the model has produced
            # the final response.
            if not tool_calls:
                return response

            # Add the assistant's tool-call message
            # to the conversation.
            messages.append(response["message"])

            for tool_call in tool_calls:

                tool_name = tool_call.function.name
                arguments = tool_call.function.arguments

                tool_function = tool_registry.get(tool_name)

                if tool_function is None:
                    raise ValueError(
                        f"Unknown tool requested: {tool_name}"
                    )

                print(
                    f"\nExecuting tool: {tool_name}"
                )

                print(
                    f"Arguments: {arguments}"
                )

                tool_result = tool_function(**arguments)

                print(
                    f"Tool result: {tool_result}"
                )

                messages.append(
                    {
                        "role": "tool",
                        "tool_name": tool_name,
                        "content": json.dumps(tool_result),
                    }
                )

        raise RuntimeError(
            "Maximum tool execution turns exceeded."
        )