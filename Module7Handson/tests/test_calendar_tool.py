from app.tools.calendar_tool import (
    create_calendar_event,
)


def test_calendar_tool():

    result = create_calendar_event(
        title="Module 7 Review",
        date="2026-08-20",
        start_time="10:00",
        end_time="11:00",
        description=(
            "Review Function Calling and Tool Use."
        ),
    )

    print("\nCalendar Result:")
    print(result)


if __name__ == "__main__":
    test_calendar_tool()