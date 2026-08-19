import logging


logger = logging.getLogger("Module6")


class FixedSizeChunker:

    # ==========================================================
    # Create Fixed-Size Text Chunks
    # ==========================================================

    @staticmethod
    def chunk_text(
        text: str,
        chunk_size: int = 1000,
        chunk_overlap: int = 100
    ) -> list[str]:

        if not text:
            return []

        if chunk_size <= 0:
            raise ValueError(
                "chunk_size must be greater than zero."
            )

        if chunk_overlap < 0:
            raise ValueError(
                "chunk_overlap cannot be negative."
            )

        if chunk_overlap >= chunk_size:
            raise ValueError(
                "chunk_overlap must be smaller "
                "than chunk_size."
            )

        chunks = []

        start = 0
        text_length = len(text)

        while start < text_length:

            end = min(
                start + chunk_size,
                text_length
            )

            chunk = text[start:end].strip()

            if chunk:
                chunks.append(chunk)

            # Prevent infinite loop
            if end == text_length:
                break

            start = end - chunk_overlap

        logger.info(
            f"Created {len(chunks)} chunks from text."
        )

        return chunks

    # ==========================================================
    # Chunk Documents
    # ==========================================================

    @classmethod
    def chunk_documents(
        cls,
        documents: list[dict],
        chunk_size: int = 1000,
        chunk_overlap: int = 100
    ) -> list[dict]:

        chunks = []

        for document in documents:

            text_chunks = cls.chunk_text(
                text=document["text"],
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap
            )

            for chunk_number, chunk_text in enumerate(
                text_chunks,
                start=1
            ):

                chunk_id = (
                    f"{document['page_id']}"
                    f"_c{chunk_number}"
                )

                chunks.append(
                    {
                        "document_id":
                            document["document_id"],

                        "page_id":
                            document["page_id"],

                        "chunk_id":
                            chunk_id,

                        "source":
                            document["source"],

                        "page":
                            document["page"],

                        "chunk_number":
                            chunk_number,

                        "text":
                            chunk_text
                    }
                )

        logger.info(
            f"Created {len(chunks)} document chunks."
        )

        return chunks