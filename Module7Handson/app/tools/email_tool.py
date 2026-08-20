import re


def send_email(
    to: str,
    subject: str,
    body: str,
) -> dict:
    """
    Simulate sending an email.

    This tool does not send a real email.
    """

    # Validate email address
    email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    if not re.match(email_pattern, to):
        return {
            "status": "failed",
            "error": "Invalid email address.",
        }

    # Validate subject
    if not subject.strip():
        return {
            "status": "failed",
            "error": "Email subject cannot be empty.",
        }

    # Validate body
    if not body.strip():
        return {
            "status": "failed",
            "error": "Email body cannot be empty.",
        }

    # Simulate sending
    return {
        "status": "sent",
        "to": to,
        "subject": subject,
        "message": "Email sent successfully.",
    }