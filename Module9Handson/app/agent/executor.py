import json
from typing import Any, Callable


class AgentExecutor:
    """Execute registered agent tools."""

    def __init__(
        self,
        tool_registry,
    ):
        self.tool_registry = tool_registry

    def execute(
        self,
        tool_name: str,
        arguments: dict[str, Any],
    ) -> Any:
        """Execute a tool from the registry."""

        tool: Callable[..., Any] | None = (
            self.tool_registry.get(tool_name)
        )

        if tool is None:
            raise ValueError(
                f"Unknown tool: {tool_name}"
            )

        return tool(**arguments)

    @staticmethod
    def format_result(
        result: Any,
    ) -> str:
        """Convert tool result to LLM-friendly text."""

        if isinstance(result, str):
            return result

        return json.dumps(
            result,
            ensure_ascii=False,
        )