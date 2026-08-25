import uuid

from app.tracing.langfuse_client import (
    langfuse,
)
from app.tracing.langfuse_pipeline import (
    run_observable_request,
)


def test_langfuse():

    user_id = "employee-001"

    session_id = (
        f"module13-"
        f"{uuid.uuid4()}"
    )

    print(
        "\n=== LANGFUSE TEST ==="
    )

    question = (
        "Explain Retrieval-Augmented "
        "Generation in simple terms."
    )

    print(
        "\nUser:"
    )
    print(question)

    answer = run_observable_request(
        question,
        user_id=user_id,
        session_id=session_id,
        feature="rag-explanation",
    )

    print(
        "\nAnswer:"
    )
    print(answer)

    print(
        "\nUser ID:"
    )
    print(user_id)

    print(
        "\nSession ID:"
    )
    print(session_id)

    # Ensure buffered events are sent.
    langfuse.flush()

    print(
        "\nLangfuse events flushed."
    )


if __name__ == "__main__":
    test_langfuse()