from app.services.markdown_chunker import (
    MarkdownChunker
)


markdown_text = """
# Employee Leave Policy

This policy explains employee leave rules.

## Eligibility

All full-time employees are eligible for annual leave.

Employees must complete the required probation period.

## Leave Entitlement

Employees receive twenty days of annual leave.

Leave can be taken throughout the calendar year.

## Carry Forward

Unused leave may be carried forward according to company policy.

Employees must obtain manager approval.

## Remote Work

Employees can work remotely two days per week.

Remote work requires manager approval.
"""


chunks = MarkdownChunker.chunk_text(
    text=markdown_text,
    max_chunk_size=500
)


print(
    f"\nTotal chunks: {len(chunks)}"
)


for chunk in chunks:

    print(
        "\n========================================"
    )

    print(
        f"Chunk       : "
        f"{chunk['chunk_number']}"
    )

    print(
        f"Heading     : "
        f"{chunk['heading']}"
    )

    print(
        f"Level       : "
        f"{chunk['heading_level']}"
    )

    print(
        f"Strategy    : "
        f"{chunk['chunking_strategy']}"
    )

    print("\nText:")

    print(
        chunk["text"]
    )