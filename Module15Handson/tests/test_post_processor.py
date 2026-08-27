from app.validation.post_processor import (
OutputPostProcessor,
)

def test_post_processor():

    processor = OutputPostProcessor()

    raw = """
    ```text
    RAG retrieves context.

    and generates an answer.

    """

    result = processor.process(
        raw
    )

    print(
        "\nRaw:"
    )

    print(raw)

    print(
        "\nProcessed:"
    )

    print(result)

    assert not result.startswith(
        "```"
    )

    assert "RAG retrieves context." in (
        result
    )

    if __name__ == "__main__":
        test_post_processor()
