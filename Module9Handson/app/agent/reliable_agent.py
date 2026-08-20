import json
from concurrent.futures import (
    ThreadPoolExecutor,
    TimeoutError,
)
from typing import Any, Callable

from ollama import chat

from app.config.logging_config import (
    configure_logging,
)
from app.tools.reliability_test_tools import (
    failing_tool,
    slow_tool,
    successful_tool,
)
from app.tools.weather_tool import get_weather


MODEL_NAME = "llama3.2:3b"

MAX_ITERATIONS = 5

TOOL_TIMEOUT_SECONDS = 3.0


class ReliableAgent:
    """Single agent with reliability controls."""

    def __init__(self):

        self.logger = (
            configure_logging()
        )

        self.tools: dict[
            str,
            Callable[..., Any],
        ] = {
            "get_weather": get_weather,
            "successful_tool": successful_tool,
            "failing_tool": failing_tool,
            "slow_tool": slow_tool,
        }

        self.tool_definitions = [
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": (
                        "Get current weather "
                        "for a city."
                    ),
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "city": {
                                "type": "string",
                            }
                        },
                        "required": ["city"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "successful_tool",
                    "description": (
                        "Process a text value."
                    ),
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "value": {
                                "type": "string",
                            }
                        },
                        "required": ["value"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "failing_tool",
                    "description": (
                        "A tool that may fail."
                    ),
                    "parameters": {
                        "type": "object",
                        "properties": {},
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "slow_tool",
                    "description": (
                        "A slow tool used for "
                        "timeout testing."
                    ),
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "seconds": {
                                "type": "number",
                            }
                        },
                    },
                },
            },
        ]

    def _execute_tool(
        self,
        tool_name: str,
        arguments: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Execute one tool with failure and timeout
        handling.
        """

        self.logger.info(
            "tool_requested name=%s arguments=%s",
            tool_name,
            arguments,
        )

        tool = self.tools.get(
            tool_name
        )

        # ----------------------------------------
        # Invalid tool
        # ----------------------------------------

        if tool is None:

            error = (
                f"Unknown tool: {tool_name}"
            )

            self.logger.error(
                "tool_invalid name=%s",
                tool_name,
            )

            return {
                "status": "failed",
                "error": error,
                "error_type": (
                    "unknown_tool"
                ),
            }

        # ----------------------------------------
        # Execute with timeout
        # ----------------------------------------

        try:

            with ThreadPoolExecutor(
                max_workers=1
            ) as executor:

                future = executor.submit(
                    tool,
                    **arguments,
                )

                result = future.result(
                    timeout=TOOL_TIMEOUT_SECONDS
                )

            self.logger.info(
                "tool_success name=%s result=%s",
                tool_name,
                result,
            )

            return {
                "status": "success",
                "data": result,
            }

        except TimeoutError:

            error = (
                f"Tool '{tool_name}' "
                f"timed out after "
                f"{TOOL_TIMEOUT_SECONDS} "
                f"seconds."
            )

            self.logger.error(
                "tool_timeout name=%s",
                tool_name,
            )

            return {
                "status": "failed",
                "error": error,
                "error_type": "timeout",
            }

        except Exception as exc:

            error = str(exc)

            self.logger.error(
                "tool_failure name=%s error=%s",
                tool_name,
                error,
            )

            return {
                "status": "failed",
                "error": error,
                "error_type": (
                    "execution_error"
                ),
            }

    def run(
        self,
        user_question: str,
    ) -> str:
        """Run the reliable agent."""

        messages = [
            {
                "role": "system",
                "content": (
                    "You are a reliable employee "
                    "assistant.\n\n"
                    "Use tools only when required.\n"
                    "If a tool fails, explain the "
                    "failure honestly.\n"
                    "Do not invent tool results."
                ),
            },
            {
                "role": "user",
                "content": user_question,
            },
        ]

        for iteration in range(
            1,
            MAX_ITERATIONS + 1,
        ):

            self.logger.info(
                "agent_iteration=%s",
                iteration,
            )

            response = chat(
                model=MODEL_NAME,
                messages=messages,
                tools=self.tool_definitions,
            )

            assistant_message = (
                response["message"]
            )

            messages.append(
                assistant_message
            )

            tool_calls = (
                assistant_message.get(
                    "tool_calls",
                    [],
                )
            )

            # ------------------------------------
            # Stop condition
            # ------------------------------------

            if not tool_calls:

                self.logger.info(
                    "agent_stop reason=no_tool_call"
                )

                return assistant_message.get(
                    "content",
                    "",
                )

            # ------------------------------------
            # Execute tools
            # ------------------------------------

            for tool_call in tool_calls:

                tool_name = (
                    tool_call["function"][
                        "name"
                    ]
                )

                arguments = (
                    tool_call["function"][
                        "arguments"
                    ]
                )

                result = self._execute_tool(
                    tool_name,
                    arguments,
                )

                messages.append(
                    {
                        "role": "tool",
                        "tool_name": tool_name,
                        "content": json.dumps(
                            result
                        ),
                    }
                )

        # ----------------------------------------
        # Max iteration safety boundary
        # ----------------------------------------

        self.logger.error(
            "agent_stop reason=max_iterations "
            "limit=%s",
            MAX_ITERATIONS,
        )

        return (
            "The agent stopped because the "
            "maximum iteration limit was reached."
        )