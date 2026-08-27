from app.validation.output_rules import (
    OutputRuleValidator,
)


def test_output_rules():

    validator = (
        OutputRuleValidator(
            max_characters=100
        )
    )

    valid = validator.validate(
        "RAG retrieves relevant context."
    )

    invalid = validator.validate(
        "password = secret123"
    )

    long_output = validator.validate(
        "A" * 101
    )

    print(
        "\nValid output errors:"
    )
    print(valid)

    print(
        "\nSensitive output errors:"
    )
    print(invalid)

    print(
        "\nLong output errors:"
    )
    print(long_output)

    assert valid == []

    assert invalid

    assert long_output


if __name__ == "__main__":
    test_output_rules()