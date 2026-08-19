from app.services.pdf_loader import PDFLoader
from app.services.chunking_service import FixedSizeChunker


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
# Create Fixed-Size Chunks
# ==========================================================

chunks = FixedSizeChunker.chunk_documents(
    documents=documents,
    chunk_size=1000,
    chunk_overlap=100
)


print(
    f"\nTotal chunks: {len(chunks)}"
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
        f"Page ID     : "
        f"{chunk['page_id']}"
    )

    print(
        f"Chunk ID    : "
        f"{chunk['chunk_id']}"
    )

    print(
        f"Page        : "
        f"{chunk['page']}"
    )

    print(
        f"Chunk No    : "
        f"{chunk['chunk_number']}"
    )

    print("\nText:")

    print(
        chunk["text"]
    )