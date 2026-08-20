from typing import Any

from ollama import chat

from app.evaluation.agent_trace import (
    AgentTrace,
)
from app.tools.weather_tool import get_weather


MODEL_NAME = "llama3.2:3b"


class EvaluationAgent:
    """Agent that records its execution trajectory."""

    def run(
        self,
        question: str,
    ) -> AgentTrace:
        """Run the agent and record its trajectory."""

        trace = AgentTrace(
            user_question=question,
            expected_tools=[
                "get_weather"
            ],
            expected_steps=1,
        )

        messages: list[dict[str, Any]] = [
            {
                "role": "system",
                "content": (
                    "You are a weather assistant.\n"
                    "Use get_weather when the user "
                    "asks for current weather.\n"
                    "Do not invent weather information."
                ),
            },
            {
                "role": "user",
                "content": question,
            },
        ]

        response = chat(
            model=MODEL_NAME,
            messages=messages,
            tools=[get_weather],
        )

        assistant_message = (
            response.message
        )

        tool_calls = (
            assistant_message.tool_calls
        )

        if not tool_calls:

            trace.final_answer = (
                assistant_message.content
            )

            trace.completed = False

            return trace

        messages.append(
            assistant_message
        )

        for tool_call in tool_calls:

            tool_name = (
                tool_call.function.name
            )

            arguments = (
                tool_call.function.arguments
            )

            if tool_name != "get_weather":

                trace.add_step(
                    action=tool_name,
                    arguments=arguments,
                    result={
                        "error": "Unexpected tool"
                    },
                    success=False,
                )

                continue

            result = get_weather(
                **arguments
            )

            trace.add_step(
                action=tool_name,
                arguments=arguments,
                result=result,
                success=True,
            )

            messages.append(
                {
                    "role": "tool",
                    "tool_name": tool_name,
                    "content": str(result),
                }
            )

        final_response = chat(
            model=MODEL_NAME,
            messages=messages,
        )

        trace.final_answer = (
            final_response.message.content
        )

        trace.completed = True

        return trace