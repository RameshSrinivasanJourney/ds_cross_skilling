from app.tools.calendar_tool import (
    create_calendar_event,
)


def test_calendar_validation():

    result = create_calendar_event(
        title="Invalid Meeting",
        date="2026-08-20",
        start_time="11:00",
        end_time="10:00",
        description="Invalid time range.",
    )

    print("\nValidation Result:")
    print(result)


if __name__ == "__main__":
    test_calendar_validation()