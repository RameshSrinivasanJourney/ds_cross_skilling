from app.models.tool_models import CURRENT_WEATHER_TOOL
from app.services.ollama_service import OllamaService
from app.services.tool_result_formatter import ToolResultFormatter
from app.tools.tool_registry import TOOL_REGISTRY
from app.security.tool_access import is_tool_allowed


def test_role_based_tool_execution():

    user_role = "manager"

    service = OllamaService()

    messages = [
        {
            "role": "user",
            "content": "What is the weather in Chennai?"
        }
    ]

    response = service.chat_with_tools(
        messages=messages,
        tools=[CURRENT_WEATHER_TOOL],
    )

    tool_calls = response["message"].get(
        "tool_calls",
        []
    )

    if not tool_calls:
        print("\nNo tool call generated.")
        return

    for tool_call in tool_calls:

        tool_name = tool_call.function.name
        arguments = tool_call.function.arguments

        print("\nUser Role:")
        print(user_role)

        print("\nTool Requested:")
        print(tool_name)

        print("\nArguments:")
        print(arguments)

        # -----------------------------------------
        # Authorization Check
        # -----------------------------------------

        if not is_tool_allowed(
            user_role,
            tool_name
        ):

            result = ToolResultFormatter.failure(
                "Tool access denied for this role."
            )

            print("\nAccess Denied:")
            print(result)

            return

        # -----------------------------------------
        # Tool Execution
        # -----------------------------------------

        tool_function = TOOL_REGISTRY.get(
            tool_name
        )

        if tool_function is None:

            result = ToolResultFormatter.failure(
                f"Unknown tool: {tool_name}"
            )

            print("\nTool Error:")
            print(result)

            return

        try:

            tool_result = tool_function(
                **arguments
            )

            result = ToolResultFormatter.success(
                tool_result
            )

        except Exception as exc:

            result = ToolResultFormatter.failure(
                str(exc)
            )

        print("\nFinal Tool Result:")
        print(result)


if __name__ == "__main__":
    test_role_based_tool_execution()