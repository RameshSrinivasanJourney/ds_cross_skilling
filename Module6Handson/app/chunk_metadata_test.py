from app.services.pdf_loader import PDFLoader
from app.services.token_chunker import (
    TokenChunker
)

from app.models.chunk_models import (
    ChunkMetadata,
    DocumentChunk
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
# Create Chunks
# ==========================================================

chunks = TokenChunker.chunk_documents(
    documents=documents,
    chunk_size=512,
    overlap=50
)


print(
    f"\nTotal chunks: {len(chunks)}"
)


# ==========================================================
# Validate Metadata
# ==========================================================

validated_chunks = []


for chunk in chunks:

    metadata = ChunkMetadata(
        document_id=chunk[
            "document_id"
        ],

        page_id=chunk[
            "page_id"
        ],

        source=chunk[
            "source"
        ],

        page=chunk[
            "page"
        ],

        chunk_number=chunk[
            "chunk_number"
        ],

        chunking_strategy=chunk[
            "chunking_strategy"
        ],

        chunk_size=chunk[
            "chunk_size"
        ],

        chunk_overlap=chunk[
            "chunk_overlap"
        ],

        token_count=chunk[
            "token_count"
        ]
    )

    document_chunk = DocumentChunk(
        metadata=metadata,
        text=chunk["text"]
    )

    validated_chunks.append(
        document_chunk
    )


# ==========================================================
# Display Result
# ==========================================================

for chunk in validated_chunks[:5]:

    print(
        "\n========================================"
    )

    print(
        "DOCUMENT CHUNK"
    )

    print(
        "========================================"
    )

    print(
        f"Document ID : "
        f"{chunk.metadata.document_id}"
    )

    print(
        f"Page ID     : "
        f"{chunk.metadata.page_id}"
    )

    print(
        f"Source      : "
        f"{chunk.metadata.source}"
    )

    print(
        f"Page        : "
        f"{chunk.metadata.page}"
    )

    print(
        f"Chunk       : "
        f"{chunk.metadata.chunk_number}"
    )

    print(
        f"Strategy    : "
        f"{chunk.metadata.chunking_strategy}"
    )

    print(
        f"Size        : "
        f"{chunk.metadata.chunk_size}"
    )

    print(
        f"Overlap     : "
        f"{chunk.metadata.chunk_overlap}"
    )

    print(
        f"Tokens      : "
        f"{chunk.metadata.token_count}"
    )

    print(
        "\nText:"
    )

    print(
        chunk.text[:500]
    )