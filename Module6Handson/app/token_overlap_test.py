from app.services.pdf_loader import PDFLoader
from app.services.token_chunker import (
    TokenChunker
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


# ==========================================================
# Configuration
# ==========================================================

chunk_size = 256
overlap = 50


print(
    "\n========================================"
)

print(
    "TOKEN CHUNKING WITH OVERLAP"
)

print(
    "========================================"
)

print(
    f"Chunk size : {chunk_size} tokens"
)

print(
    f"Overlap    : {overlap} tokens"
)


# ==========================================================
# Create Chunks
# ==========================================================

chunks = TokenChunker.chunk_documents(
    documents=documents,
    chunk_size=chunk_size,
    overlap=overlap
)


print(
    f"\nTotal chunks: {len(chunks)}"
)


# ==========================================================
# Display Chunks
# ==========================================================

for chunk in chunks[:5]:

    print(
        "\n----------------------------------------"
    )

    print(
        f"Chunk       : "
        f"{chunk['chunk_number']}"
    )

    print(
        f"Token count : "
        f"{chunk['token_count']}"
    )

    print(
        f"Chunk size  : "
        f"{chunk['chunk_size']}"
    )

    print(
        f"Overlap     : "
        f"{chunk['chunk_overlap']}"
    )

    print(
        f"Source      : "
        f"{chunk['source']}"
    )

    print("\nText:")

    print(
        chunk["text"][:500]
    )