from app.services.pdf_loader import PDFLoader
from app.services.sentence_chunker import (
    SentenceAwareChunker
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
# Sentence-Aware Chunking
# ==========================================================

chunks = SentenceAwareChunker.chunk_documents(
    documents=documents,
    chunk_size=1000,
    chunk_overlap=1
)


print(
    f"\nTotal sentence-aware chunks: "
    f"{len(chunks)}"
)


# ==========================================================
# Display Chunks
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

    print(
        f"Chunk No    : "
        f"{chunk['chunk_number']}"
    )

    print("\nText:")

    print(
        chunk["text"]
    )