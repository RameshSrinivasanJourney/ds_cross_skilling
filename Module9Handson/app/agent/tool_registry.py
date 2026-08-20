from typing import Callable, Any


class ToolRegistry:
    """Store and retrieve agent tools."""

    def __init__(self):
        self._tools: dict[str, Callable[..., Any]] = {}

    def register(
        self,
        name: str,
        function: Callable[..., Any],
    ) -> None:
        """Register a tool by name."""

        self._tools[name] = function

    def get(
        self,
        name: str,
    ) -> Callable[..., Any] | None:
        """Return a registered tool."""

        return self._tools.get(name)

    def list_tools(self) -> list[str]:
        """Return registered tool names."""

        return list(self._tools.keys())