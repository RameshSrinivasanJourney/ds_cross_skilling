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


print(
    f"\nPages extracted: "
    f"{len(documents)}"
)


# ==========================================================
# Compare Chunk Sizes
# ==========================================================

for chunk_size in [
    256,
    512,
    1024
]:

    print(
        "\n\n########################################"
    )

    print(
        f"CHUNK SIZE: {chunk_size} TOKENS"
    )

    print(
        "########################################"
    )

    chunks = TokenChunker.chunk_documents(
        documents=documents,
        chunk_size=chunk_size
    )

    print(
        f"\nTotal chunks: "
        f"{len(chunks)}"
    )

    for chunk in chunks[:3]:

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
            f"Strategy    : "
            f"{chunk['chunking_strategy']}"
        )

        print(
            "\nText:"
        )

        print(
            chunk["text"][:500]
        )