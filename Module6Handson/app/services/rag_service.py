import logging

import faiss
import numpy as np

from app.core.config import settings
from app.services.embedding_service import EmbeddingService
from app.services.reranker_service import RerankerService


logger = logging.getLogger("Module6")


class RAGService:

    # ==========================================================
    # Shared FAISS Index
    # ==========================================================

    index = None

    # ==========================================================
    # Indexed Chunks / Documents
    # ==========================================================

    documents = []

    # ==========================================================
    # Set Index
    #
    # IndexingService will provide the FAISS index and
    # corresponding chunks after indexing.
    # ==========================================================

    @classmethod
    def set_index(
        cls,
        index,
        documents
    ):

        cls.index = index

        cls.documents = documents

        logger.info(
            "RAG retrieval index updated."
        )

        logger.info(
            f"Total vectors available: "
            f"{cls.index.ntotal}"
        )

        logger.info(
            f"Total documents available: "
            f"{len(cls.documents)}"
        )

    # ==========================================================
    # Retrieve
    # ==========================================================

    @classmethod
    def retrieve(
        cls,
        query: str,
        top_k: int = 3,
        rerank: bool = False,
        retrieval_k: int = 10
    ):

        # ======================================================
        # Validate Index
        # ======================================================

        if cls.index is None:

            logger.warning(
                "FAISS index is not initialized."
            )

            return {
                "query": query,
                "total_results": 0,
                "results": [],
                "context": ""
            }

        if cls.index.ntotal == 0:

            logger.warning(
                "FAISS index contains no vectors."
            )

            return {
                "query": query,
                "total_results": 0,
                "results": [],
                "context": ""
            }

        # ======================================================
        # Determine FAISS Candidate Count
        # ======================================================

        if rerank:

            actual_retrieval_k = min(
                retrieval_k,
                cls.index.ntotal
            )

        else:

            actual_retrieval_k = min(
                top_k,
                cls.index.ntotal
            )

        logger.info(
            f"Retrieving documents for query: "
            f"{query}"
        )

        logger.info(
            f"Final top_k: {top_k}"
        )

        logger.info(
            f"Reranking enabled: {rerank}"
        )

        logger.info(
            f"Retrieval candidate_k: "
            f"{actual_retrieval_k}"
        )

        # ======================================================
        # STEP 1 — EMBED USER QUERY
        # ======================================================

        query_embedding = (
            EmbeddingService.generate_embedding(
                query
            )
        )

        logger.info(
            f"Query embedding dimension: "
            f"{len(query_embedding)}"
        )

        # ======================================================
        # Validate Embedding Dimension
        # ======================================================

        if (
            len(query_embedding)
            != settings.EMBEDDING_DIMENSION
        ):

            raise ValueError(
                "Query embedding dimension mismatch. "
                f"Expected "
                f"{settings.EMBEDDING_DIMENSION}, "
                f"but received "
                f"{len(query_embedding)}."
            )

        # ======================================================
        # STEP 2 — Convert Query to FAISS Vector
        # ======================================================

        query_vector = np.asarray(
            [query_embedding],
            dtype="float32"
        )

        logger.info(
            f"Query vector shape: "
            f"{query_vector.shape}"
        )

        # ======================================================
        # STEP 3 — FAISS CANDIDATE SEARCH
        # ======================================================

        distances, indices = (
            cls.index.search(
                query_vector,
                actual_retrieval_k
            )
        )

        logger.info(
            f"Retrieved "
            f"{len(indices[0])} candidates "
            f"from FAISS."
        )

        # ======================================================
        # STEP 4 — BUILD RETRIEVAL RESULTS
        # ======================================================

        results = []

        for distance, index in zip(
            distances[0],
            indices[0]
        ):

            if index == -1:

                continue

            # --------------------------------------------------
            # Safety Check
            # --------------------------------------------------

            if index >= len(cls.documents):

                logger.warning(
                    f"FAISS index {index} does not "
                    f"have a corresponding document."
                )

                continue

            document = cls.documents[index]

            results.append(
                {
                    "point_id": str(
                        document.get(
                            "chunk_id",
                            document.get(
                                "id",
                                index
                            )
                        )
                    ),

                    "department":
                        document.get(
                            "department",
                            ""
                        ),

                    "category":
                        document.get(
                            "category",
                            ""
                        ),

                    "text":
                        document.get(
                            "text",
                            ""
                        ),

                    "distance":
                        round(
                            float(distance),
                            4
                        ),

                    "rerank_score":
                        None
                }
            )

        logger.info(
            f"FAISS candidate results: "
            f"{len(results)}"
        )

        # ======================================================
        # STEP 5 — RERANK CANDIDATES
        # ======================================================

        if rerank:

            logger.info(
                "Starting FlashRank reranking..."
            )

            results = RerankerService.rerank(
                query=query,
                documents=results,
                top_k=top_k
            )

            logger.info(
                f"FlashRank returned "
                f"{len(results)} final results."
            )

        else:

            # ==================================================
            # No Reranking
            #
            # FAISS already returned top_k results because
            # actual_retrieval_k = top_k.
            # ==================================================

            results = results[:top_k]

        # ======================================================
        # STEP 6 — BUILD RAG CONTEXT
        # ======================================================

        context = "\n\n".join(
            [
                result["text"]
                for result in results
            ]
        )

        logger.info(
            f"Final retrieval results: "
            f"{len(results)}"
        )

        # ======================================================
        # STEP 7 — RETURN RESPONSE
        # ======================================================

        return {
            "query": query,

            "total_results":
                len(results),

            "results":
                results,

            "context":
                context
        }

    # ==========================================================
    # Count
    # ==========================================================

    @classmethod
    def count(cls):

        if cls.index is None:

            return 0

        return cls.index.ntotal