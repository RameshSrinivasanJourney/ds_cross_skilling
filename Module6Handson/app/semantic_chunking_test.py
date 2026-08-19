from app.services.pdf_loader import PDFLoader
from app.services.semantic_chunker import (
    SemanticChunker
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
# Semantic Chunking
# ==========================================================

chunks = SemanticChunker.chunk_documents(
    documents=documents,
    similarity_threshold=0.55,
    max_chunk_size=1000
)


print(
    f"\nTotal semantic chunks: "
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

    print(
        f"Threshold   : "
        f"{chunk['similarity_threshold']}"
    )

    print("\nText:")

    print(
        chunk["text"]
    )