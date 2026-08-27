from app.pii.safe_logging import (
    SafeLogSanitizer,
)


def test_safe_logging():

    sanitizer = (
        SafeLogSanitizer()
    )

    text = (
        "User ramesh@example.com "
        "can be reached at "
        "+1-212-555-1234."
    )

    result = sanitizer.sanitize(
        text
    )

    print(
        "\nOriginal:"
    )

    print(text)

    print(
        "\nSafe log:"
    )

    print(result)

    assert (
        "ramesh@example.com"
        not in result
    )

    assert (
        "+1-212-555-1234"
        not in result
    )

    assert (
        "[REDACTED_EMAIL]"
        in result
    )

    assert (
        "[REDACTED_PHONE]"
        in result
    )


if __name__ == "__main__":
    test_safe_logging()