from app.guardrails.custom_validators import (
    NoPIIValidator,
    NoToxicTermsValidator,
    NoURLValidator,
)


def test_custom_validators():

    pii_validator = (
        NoPIIValidator()
    )

    url_validator = (
        NoURLValidator()
    )

    toxicity_validator = (
        NoToxicTermsValidator()
    )

    print(
        "\n=== PII TEST ==="
    )

    try:

        pii_validator.validate(
            "Contact me at "
            "ramesh@example.com"
        )

    except ValueError as exc:

        print(
            "Rejected:",
            exc,
        )

    print(
        "\n=== URL TEST ==="
    )

    try:

        url_validator.validate(
            "Visit https://example.com"
        )

    except ValueError as exc:

        print(
            "Rejected:",
            exc,
        )

    print(
        "\n=== TOXICITY TEST ==="
    )

    try:

        toxicity_validator.validate(
            "This contains explicit_slur."
        )

    except ValueError as exc:

        print(
            "Rejected:",
            exc,
        )


if __name__ == "__main__":
    test_custom_validators()