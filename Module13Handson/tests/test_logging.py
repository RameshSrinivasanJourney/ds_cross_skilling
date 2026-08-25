from app.logging.correlation import (
    create_correlation_id,
)
from app.logging.logger import (
    get_logger,
)


def test_logging():

    logger = get_logger()

    correlation_id = (
        create_correlation_id()
    )

    user_id = "employee-001"

    print(
        "\n=== CORRELATION ID ==="
    )

    print(
        correlation_id
    )

    print(
        "\n=== DEBUG LOG ==="
    )

    logger.debug(
        "debug_request_details",
        extra={
            "context": {
                "correlation_id": (
                    correlation_id
                ),
                "user_id": user_id,
                "feature": "chat",
                "prompt_version": "v1",
            }
        },
    )

    print(
        "\n=== INFO LOG ==="
    )

    logger.info(
        "llm_request_completed",
        extra={
            "context": {
                "correlation_id": (
                    correlation_id
                ),
                "user_id": user_id,
                "model": "llama3.2:3b",
                "input_tokens": 120,
                "output_tokens": 250,
                "total_tokens": 370,
                "latency_ms": 2300,
            }
        },
    )

    print(
        "\n=== PII TEST ==="
    )

    logger.info(
        "user_message_received",
        extra={
            "context": {
                "correlation_id": (
                    correlation_id
                ),
                "message": (
                    "My email is "
                    "ramesh@example.com and "
                    "my phone is "
                    "+91 98765 43210."
                ),
            }
        },
    )

    print(
        "\n=== ERROR LOG ==="
    )

    logger.error(
        "llm_request_failed",
        extra={
            "context": {
                "correlation_id": (
                    correlation_id
                ),
                "error_type": (
                    "TimeoutError"
                ),
                "feature": "rag",
                "message": (
                    "LLM request timed out."
                ),
            }
        },
    )


if __name__ == "__main__":
    test_logging()