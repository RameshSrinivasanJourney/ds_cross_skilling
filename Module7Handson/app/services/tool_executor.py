from concurrent.futures import ThreadPoolExecutor, as_completed


class ToolExecutor:
    """Execute multiple tools concurrently."""

    def __init__(self, tool_registry: dict):
        self.tool_registry = tool_registry

    def execute_parallel(self, tool_calls):
        """Execute multiple tool calls concurrently."""

        results = []

        with ThreadPoolExecutor(
            max_workers=len(tool_calls)
        ) as executor:

            future_to_tool = {
                executor.submit(
                    self._execute_tool,
                    tool_call
                ): tool_call
                for tool_call in tool_calls
            }

            for future in as_completed(
                future_to_tool
            ):
                tool_call = future_to_tool[future]

                result = future.result()

                results.append(result)

        return results

    def _execute_tool(self, tool_call):
        """Execute a single tool call."""

        tool_name = tool_call.function.name
        arguments = tool_call.function.arguments

        tool_function = self.tool_registry.get(
            tool_name
        )

        if tool_function is None:
            raise ValueError(
                f"Unknown tool requested: {tool_name}"
            )

        result = tool_function(**arguments)

        return {
            "tool_name": tool_name,
            "arguments": arguments,
            "result": result,
        }