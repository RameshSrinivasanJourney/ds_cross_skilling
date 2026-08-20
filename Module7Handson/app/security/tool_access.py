ROLE_TOOL_ACCESS = {
    "employee": {
        "get_current_weather",
        "calculate",
        "create_calendar_event",
    },

    "manager": {
        "get_current_weather",
        "calculate",
        "query_database",
        "send_email",
        "create_calendar_event",
        "read_file",
        "scrape_web_page",
        "search_web",
    },

    "admin": {
        "get_current_weather",
        "calculate",
        "query_database",
        "send_email",
        "create_calendar_event",
        "read_file",
        "write_file",
        "scrape_web_page",
        "search_web",
        "execute_code",
    },
}


def is_tool_allowed(role: str, tool_name: str) -> bool:

    allowed_tools = ROLE_TOOL_ACCESS.get(
        role,
        set()
    )

    return tool_name in allowed_tools