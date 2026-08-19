import logging
import re


logger = logging.getLogger("Module6")


class SentenceAwareChunker:

    # ==========================================================
    # Split Text Into Sentences
    # ==========================================================

    @staticmethod
    def split_sentences(
        text: str
    ) -> list[str]:

        if not text:
            return []

        text = re.sub(
            r"\s+",
            " ",
            text
        ).strip()

        if not text:
            return []

        sentences = re.split(
            r"(?<=[.!?])\s+",
            text
        )

        return [
            sentence.strip()
            for sentence in sentences
            if sentence.strip()
        ]

    # ==========================================================
    # Create Sentence-Aware Chunks
    # ==========================================================

    @classmethod
    def chunk_text(
        cls,
        text: str,
        chunk_size: int = 1000,
        chunk_overlap: int = 1
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

        sentences = cls.split_sentences(
            text
        )

        chunks = []

        current_sentences = []
        current_length = 0

        for sentence in sentences:

            sentence_length = len(sentence)

            # --------------------------------------------------
            # Single sentence larger than chunk size
            # --------------------------------------------------

            if (
                sentence_length > chunk_size
                and not current_sentences
            ):

                chunks.append(sentence)

                continue

            # --------------------------------------------------
            # Add sentence to current chunk
            # --------------------------------------------------

            additional_length = (
                sentence_length
                + (
                    1
                    if current_sentences
                    else 0
                )
            )

            if (
                current_length
                + additional_length
                <= chunk_size
            ):

                current_sentences.append(
                    sentence
                )

                current_length += (
                    additional_length
                )

            else:

                if current_sentences:

                    chunks.append(
                        " ".join(
                            current_sentences
                        )
                    )

                # --------------------------------------------------
                # Sentence overlap
                # --------------------------------------------------

                overlap_sentences = (
                    current_sentences[
                        -chunk_overlap:
                    ]
                    if chunk_overlap > 0
                    else []
                )

                current_sentences = (
                    overlap_sentences.copy()
                )

                current_length = sum(
                    len(sentence)
                    for sentence
                    in current_sentences
                )

                if current_sentences:
                    current_length += (
                        len(current_sentences) - 1
                    )

                # --------------------------------------------------
                # Add current sentence
                # --------------------------------------------------

                current_sentences.append(
                    sentence
                )

                current_length += (
                    sentence_length
                    + (
                        1
                        if len(current_sentences) > 1
                        else 0
                    )
                )

        # ----------------------------------------------------------
        # Add final chunk
        # ----------------------------------------------------------

        if current_sentences:

            chunks.append(
                " ".join(
                    current_sentences
                )
            )

        logger.info(
            f"Sentence-aware chunking created "
            f"{len(chunks)} chunks."
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
        chunk_overlap: int = 1
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
                    f"_sa_c{chunk_number}"
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

                        "chunking_strategy":
                            "sentence_aware",

                        "text":
                            chunk_text
                    }
                )

        logger.info(
            f"Sentence-aware chunking created "
            f"{len(chunks)} document chunks."
        )

        return chunks