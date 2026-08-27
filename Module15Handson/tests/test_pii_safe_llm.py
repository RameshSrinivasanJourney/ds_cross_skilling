from app.services.pii_safe_llm import (
    PIISafeLLM,
)


def test_pii_safe_llm():

    service = PIISafeLLM()

    message = (
        "Please draft a confirmation email "
        "to ramesh@example.com and mention "
        "that we will call +1-212-555-1234 "
        "tomorrow."
    )

    result = service.generate(
        message
    )

    print(
        "\n=== ORIGINAL INPUT ==="
    )

    print(
        result["original_input"]
    )

    print(
        "\n=== SAFE INPUT SENT TO LLM ==="
    )

    print(
        result["safe_input"]
    )

    print(
        "\n=== MODEL RESPONSE ==="
    )

    print(
        result["model_response"]
    )

    print(
        "\n=== FINAL RESPONSE ==="
    )

    print(
        result["final_response"]
    )

    print(
        "\n=== PII TOKEN MAP ==="
    )

    print(
        result["pii_tokens"]
    )


if __name__ == "__main__":
    test_pii_safe_llm()