import logging
from typing import List

import numpy as np
from sentence_transformers import SentenceTransformer


logger = logging.getLogger("Module6")


class SemanticChunker:

    # ==========================================================
    # Initialize Embedding Model
    # ==========================================================

    _model = None

    @classmethod
    def _get_model(cls):

        if cls._model is None:

            logger.info(
                "Loading Sentence Transformer model..."
            )

            cls._model = SentenceTransformer(
                "sentence-transformers/all-MiniLM-L6-v2"
            )

            logger.info(
                "Sentence Transformer model loaded."
            )

        return cls._model

    # ==========================================================
    # Split Sentences
    # ==========================================================

    @staticmethod
    def split_sentences(
        text: str
    ) -> List[str]:

        import re

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
    # Calculate Cosine Similarity
    # ==========================================================

    @staticmethod
    def cosine_similarity(
        vector_a: np.ndarray,
        vector_b: np.ndarray
    ) -> float:

        norm_a = np.linalg.norm(
            vector_a
        )

        norm_b = np.linalg.norm(
            vector_b
        )

        if norm_a == 0 or norm_b == 0:

            return 0.0

        return float(
            np.dot(
                vector_a,
                vector_b
            )
            / (
                norm_a * norm_b
            )
        )

    # ==========================================================
    # Create Semantic Chunks
    # ==========================================================

    @classmethod
    def chunk_text(
        cls,
        text: str,
        similarity_threshold: float = 0.55,
        max_chunk_size: int = 1000
    ) -> List[str]:

        sentences = cls.split_sentences(
            text
        )

        if not sentences:

            return []

        if len(sentences) == 1:

            return sentences

        model = cls._get_model()

        logger.info(
            f"Generating embeddings for "
            f"{len(sentences)} sentences..."
        )

        embeddings = model.encode(
            sentences,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        chunks = []

        current_chunk = [
            sentences[0]
        ]

        current_length = len(
            sentences[0]
        )

        for index in range(
            1,
            len(sentences)
        ):

            previous_embedding = (
                embeddings[index - 1]
            )

            current_embedding = (
                embeddings[index]
            )

            similarity = cls.cosine_similarity(
                previous_embedding,
                current_embedding
            )

            sentence = sentences[index]

            additional_length = (
                len(sentence)
                + 1
            )

            # --------------------------------------------------
            # Decide whether to continue current chunk
            # --------------------------------------------------

            should_continue = (
                similarity
                >= similarity_threshold
                and
                (
                    current_length
                    + additional_length
                    <= max_chunk_size
                )
            )

            if should_continue:

                current_chunk.append(
                    sentence
                )

                current_length += (
                    additional_length
                )

            else:

                chunks.append(
                    " ".join(
                        current_chunk
                    )
                )

                current_chunk = [
                    sentence
                ]

                current_length = len(
                    sentence
                )

        # ------------------------------------------------------
        # Add final chunk
        # ------------------------------------------------------

        if current_chunk:

            chunks.append(
                " ".join(
                    current_chunk
                )
            )

        logger.info(
            f"Semantic chunking created "
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
        similarity_threshold: float = 0.55,
        max_chunk_size: int = 1000
    ) -> list[dict]:

        chunks = []

        for document in documents:

            text_chunks = cls.chunk_text(
                text=document["text"],
                similarity_threshold=(
                    similarity_threshold
                ),
                max_chunk_size=max_chunk_size
            )

            for chunk_number, chunk_text in enumerate(
                text_chunks,
                start=1
            ):

                chunk_id = (
                    f"{document['page_id']}"
                    f"_sem_c{chunk_number}"
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
                            "semantic",

                        "similarity_threshold":
                            similarity_threshold,

                        "text":
                            chunk_text
                    }
                )

        logger.info(
            f"Created {len(chunks)} semantic "
            f"document chunks."
        )

        return chunks