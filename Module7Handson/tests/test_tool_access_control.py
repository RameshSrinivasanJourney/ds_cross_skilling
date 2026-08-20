from app.security.tool_access import is_tool_allowed


def test_tool_access_control():

    test_cases = [
        ("employee", "get_current_weather"),
        ("employee", "calculate"),
        ("employee", "send_email"),
        ("manager", "send_email"),
        ("manager", "query_database"),
        ("admin", "write_file"),
        ("admin", "execute_code"),
        ("unknown", "send_email"),
    ]

    for role, tool_name in test_cases:

        allowed = is_tool_allowed(
            role,
            tool_name
        )

        print(
            f"\nRole: {role}"
        )

        print(
            f"Tool: {tool_name}"
        )

        print(
            f"Allowed: {allowed}"
        )


if __name__ == "__main__":
    test_tool_access_control()