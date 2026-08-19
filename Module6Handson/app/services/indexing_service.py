import logging

import faiss
import numpy as np

from app.core.config import settings
from app.services.ingestion_service import IngestionService
from app.services.token_chunker import TokenChunker
from app.services.embedding_service import EmbeddingService
from app.services.rag_service import RAGService


logger = logging.getLogger("Module6")


class IndexingService:

    # ==========================================================
    # FAISS Index
    # ==========================================================

    index = None

    # ==========================================================
    # Indexed Chunks
    # ==========================================================

    chunks = []

    # ==========================================================
    # Chunk Hashes
    # ==========================================================

    chunk_hashes = set()

    # ==========================================================
    # Index Document
    # ==========================================================

    @classmethod
    def index_document(
        cls,
        file_path: str,
        chunk_size: int = 512,
        chunk_overlap: int = 50
    ):

        logger.info(
            "Starting indexing pipeline..."
        )

        # ======================================================
        # STEP 1 — INGEST
        # ======================================================

        logger.info(
            "STEP 1: Ingesting document..."
        )

        documents = (
            IngestionService.ingest(
                file_path
            )
        )

        logger.info(
            f"Documents loaded: "
            f"{len(documents)}"
        )

        # ======================================================
        # STEP 2 — CHUNK
        # ======================================================

        logger.info(
            "STEP 2: Creating chunks..."
        )

        chunks = (
            TokenChunker.chunk_documents(
                documents=documents,
                chunk_size=chunk_size,
                overlap=chunk_overlap
            )
        )

        logger.info(
            f"Chunks created: "
            f"{len(chunks)}"
        )

        # ======================================================
        # STEP 3 — DEDUPLICATION
        # ======================================================

        logger.info(
            "STEP 3: Deduplicating chunks..."
        )

        unique_chunks = []

        duplicates_skipped = 0

        for chunk in chunks:

            text = chunk["text"]

            chunk_id = (
                cls._generate_chunk_id(
                    text
                )
            )

            if chunk_id in cls.chunk_hashes:

                duplicates_skipped += 1

                continue

            chunk["chunk_id"] = chunk_id

            unique_chunks.append(
                chunk
            )

        logger.info(
            f"Unique chunks: "
            f"{len(unique_chunks)}"
        )

        logger.info(
            f"Duplicate chunks skipped: "
            f"{duplicates_skipped}"
        )

        # ======================================================
        # STEP 4 — CREATE FAISS INDEX
        # ======================================================

        if cls.index is None:

            logger.info(
                "Creating FAISS IndexFlatL2..."
            )

            cls.index = faiss.IndexFlatL2(
                settings.EMBEDDING_DIMENSION
            )

        # ======================================================
        # STEP 5 — GENERATE BATCH EMBEDDINGS
        # ======================================================

        texts = [
            chunk["text"]
            for chunk in unique_chunks
        ]

        if not texts:

            logger.info(
                "No new chunks to index."
            )

            return {
                "status": "Success",

                "source": file_path,

                "documents_loaded":
                    len(documents),

                "chunks_created":
                    len(chunks),

                "chunks_indexed":
                    len(unique_chunks),

                "duplicates_skipped":
                    duplicates_skipped,

                "total_vectors":
                    cls.count(),

                "embedding_dimension":
                    settings.EMBEDDING_DIMENSION,

                "message":
                    "Document indexed successfully."
            }

        logger.info(
            "STEP 5: Generating batch embeddings..."
        )

        embeddings = (
            EmbeddingService.generate_embeddings(
                texts
            )
        )

        vectors = np.asarray(
            embeddings,
            dtype="float32"
        )

        # ======================================================
        # STEP 6 — VALIDATE VECTOR DIMENSION
        # ======================================================

        if vectors.shape[1] != (
            settings.EMBEDDING_DIMENSION
        ):

            raise ValueError(
                "Embedding dimension mismatch. "
                f"Expected "
                f"{settings.EMBEDDING_DIMENSION}, "
                f"received "
                f"{vectors.shape[1]}."
            )

        logger.info(
            f"Embedding shape: "
            f"{vectors.shape}"
        )

        # ======================================================
        # STEP 7 — ADD VECTORS TO FAISS
        # ======================================================

        cls.index.add(
            vectors
        )

        # ======================================================
        # STEP 8 — STORE CHUNKS
        # ======================================================

        cls.chunks.extend(
            unique_chunks
        )

        # Update hash set
        for chunk in unique_chunks:

            cls.chunk_hashes.add(
                chunk["chunk_id"]
            )

        # ======================================================
        # STEP 9 — SYNCHRONIZE RAG RETRIEVAL
        # ======================================================

        RAGService.set_index(
            index=cls.index,
            documents=cls.chunks
        )

        logger.info(
            "RAGService successfully synchronized "
            "with IndexingService."
        )

        # ======================================================
        # STEP 10 — RESULT
        # ======================================================

        logger.info(
            f"Total vectors in FAISS: "
            f"{cls.index.ntotal}"
        )

        logger.info(
            "Indexing pipeline completed."
        )

        return {
            "status": "Success",

            "source": file_path,

            "documents_loaded":
                len(documents),

            "chunks_created":
                len(chunks),

            "chunks_indexed":
                len(unique_chunks),

            "duplicates_skipped":
                duplicates_skipped,

            "total_vectors":
                cls.count(),

            "embedding_dimension":
                settings.EMBEDDING_DIMENSION,

            "message":
                "Document indexed successfully."
        }

    # ==========================================================
    # Generate Chunk ID
    # ==========================================================

    @staticmethod
    def _generate_chunk_id(
        text: str
    ):

        import hashlib

        return hashlib.sha256(
            text.encode(
                "utf-8"
            )
        ).hexdigest()

    # ==========================================================
    # Count
    # ==========================================================

    @classmethod
    def count(cls):

        if cls.index is None:

            return 0

        return cls.index.ntotal