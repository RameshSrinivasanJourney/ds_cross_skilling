from app.services.pdf_loader import PDFLoader
from app.services.recursive_chunker import (
    RecursiveChunker
)


pdf_path = (
    "documents/Leave Policy.pdf"
)


# ==========================================================
# Load PDF
# ==========================================================

documents = PDFLoader.load(
    pdf_path
)

print(
    f"\nPages extracted: {len(documents)}"
)


# ==========================================================
# Recursive Chunking
# ==========================================================

chunks = RecursiveChunker.chunk_documents(
    documents=documents,
    chunk_size=1000,
    chunk_overlap=100
)


print(
    f"\nTotal recursive chunks: "
    f"{len(chunks)}"
)


# ==========================================================
# Display Results
# ==========================================================

for chunk in chunks:

    print(
        "\n========================================"
    )

    print(
        f"Document ID : "
        f"{chunk['document_id']}"
    )

    print(
        f"Page        : "
        f"{chunk['page']}"
    )

    print(
        f"Chunk ID    : "
        f"{chunk['chunk_id']}"
    )

    print(
        f"Strategy    : "
        f"{chunk['chunking_strategy']}"
    )

    print("\nText:")

    print(
        chunk["text"]
    )