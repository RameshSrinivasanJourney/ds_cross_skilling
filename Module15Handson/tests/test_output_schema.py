import json

from pydantic import ValidationError

from app.validation.output_validator import (
    OutputValidator,
)


def test_output_schema():

    validator = OutputValidator()

    valid_output = json.dumps(
        {
            "answer": (
                "RAG retrieves relevant "
                "context and uses it to "
                "generate an answer."
            ),
            "confidence": 0.92,
            "sources": [
                "knowledge-base"
            ],
        }
    )

    result = validator.validate_json(
        valid_output
    )

    print(
        "\nValid schema:"
    )
    print(result)

    assert result.confidence == 0.92

    invalid_output = json.dumps(
        {
            "answer": "",
            "confidence": 1.5,
        }
    )

    try:

        validator.validate_json(
            invalid_output
        )

    except ValidationError as exc:

        print(
            "\nInvalid schema correctly rejected:"
        )

        print(exc)

    else:

        raise AssertionError(
            "Invalid output was not rejected."
        )


if __name__ == "__main__":
    test_output_schema()