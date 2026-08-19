import logging

from flashrank import Ranker, RerankRequest


logger = logging.getLogger("Module6")


class RerankerService:

    # ==========================================================
    # FlashRank Model
    # ==========================================================

    _ranker = None

    # ==========================================================
    # Get Reranker
    # ==========================================================

    @classmethod
    def _get_ranker(cls):

        if cls._ranker is None:

            logger.info(
                "Initializing FlashRank reranker..."
            )

            cls._ranker = Ranker()

            logger.info(
                "FlashRank reranker initialized."
            )

        return cls._ranker

    # ==========================================================
    # Rerank
    # ==========================================================

    @classmethod
    def rerank(
        cls,
        query: str,
        documents: list,
        top_k: int = 3
    ):

        if not documents:

            logger.warning(
                "No documents available for reranking."
            )

            return []

        logger.info(
            f"Reranking {len(documents)} "
            f"documents."
        )

        ranker = cls._get_ranker()

        # ======================================================
        # Convert Documents to FlashRank Passages
        # ======================================================

        passages = []

        for document in documents:

            passages.append(
                {
                    "id":
                        document["point_id"],

                    "text":
                        document["text"],

                    "meta":
                        document
                }
            )

        # ======================================================
        # Create Rerank Request
        # ======================================================

        rerank_request = RerankRequest(
            query=query,
            passages=passages
        )

        # ======================================================
        # Execute Reranking
        # ======================================================

        ranked_results = ranker.rerank(
            rerank_request
        )

        # ======================================================
        # Build Final Results
        # ======================================================

        results = []

        for result in ranked_results[:top_k]:

            original_document = result["meta"]

            results.append(
                {
                    **original_document,

                    "rerank_score":
                        round(
                            float(
                                result["score"]
                            ),
                            4
                        )
                }
            )

        logger.info(
            f"Reranking completed. "
            f"Final results: {len(results)}"
        )

        return results