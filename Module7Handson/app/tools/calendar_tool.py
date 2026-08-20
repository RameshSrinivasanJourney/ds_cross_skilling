from datetime import datetime


def create_calendar_event(
    title: str,
    date: str,
    start_time: str,
    end_time: str,
    description: str = "",
) -> dict:
    """
    Simulate creating a calendar event.

    This tool does not create a real calendar event.
    """

    # Validate title
    if not title.strip():
        return {
            "status": "failed",
            "error": "Event title cannot be empty.",
        }

    # Validate date
    try:
        event_date = datetime.strptime(
            date,
            "%Y-%m-%d"
        ).date()
    except ValueError:
        return {
            "status": "failed",
            "error": (
                "Invalid date format. "
                "Use YYYY-MM-DD."
            ),
        }

    # Validate start time
    try:
        start = datetime.strptime(
            start_time,
            "%H:%M"
        ).time()
    except ValueError:
        return {
            "status": "failed",
            "error": (
                "Invalid start time format. "
                "Use HH:MM."
            ),
        }

    # Validate end time
    try:
        end = datetime.strptime(
            end_time,
            "%H:%M"
        ).time()
    except ValueError:
        return {
            "status": "failed",
            "error": (
                "Invalid end time format. "
                "Use HH:MM."
            ),
        }

    # Validate time range
    if end <= start:
        return {
            "status": "failed",
            "error": (
                "End time must be later "
                "than start time."
            ),
        }

    # Simulate calendar event creation
    return {
        "status": "created",
        "title": title,
        "date": event_date.isoformat(),
        "start_time": start.strftime("%H:%M"),
        "end_time": end.strftime("%H:%M"),
        "description": description,
        "message": (
            "Calendar event created successfully."
        ),
    }