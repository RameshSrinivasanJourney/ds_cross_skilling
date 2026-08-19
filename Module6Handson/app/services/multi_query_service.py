import logging

from app.services.rag_service import RAGService


logger = logging.getLogger("Module6")


class MultiQueryService:

    # ==========================================================
    # Multi-Query Retrieval
    # ==========================================================

    @classmethod
    def retrieve(
        cls,
        query: str,
        top_k: int = 3
    ):

        logger.info(
            f"Multi-query retrieval started: {query}"
        )

        # ======================================================
        # STEP 1 — Generate Query Variations
        # ======================================================

        queries = cls._generate_queries(
            query
        )

        logger.info(
            f"Generated {len(queries)} queries."
        )

        # ======================================================
        # STEP 2 — Retrieve for Each Query
        # ======================================================

        all_results = []

        query_results = []

        for generated_query in queries:

            response = RAGService.retrieve(
                query=generated_query,
                top_k=top_k
            )

            results = response["results"]

            query_results.append(
                {
                    "query": generated_query,
                    "results": results
                }
            )

            all_results.extend(
                results
            )

        # ======================================================
        # STEP 3 — Deduplicate Results
        # ======================================================

        unique_results = {}

        for result in all_results:

            point_id = result["point_id"]

            if point_id not in unique_results:

                unique_results[
                    point_id
                ] = result

        final_results = list(
            unique_results.values()
        )

        # ======================================================
        # STEP 4 — Limit Results
        # ======================================================

        final_results = final_results[
            :top_k
        ]

        # ======================================================
        # STEP 5 — Build Context
        # ======================================================

        context = "\n\n".join(
            [
                result["text"]
                for result in final_results
            ]
        )

        logger.info(
            f"Multi-query retrieval completed. "
            f"Final results: {len(final_results)}"
        )

        return {

            "original_query": query,

            "generated_queries": queries,

            "query_results": query_results,

            "total_results":
                len(final_results),

            "results":
                final_results,

            "context":
                context
        }

    # ==========================================================
    # Generate Query Variations
    # ==========================================================

    @staticmethod
    def _generate_queries(
        query: str
    ):

        return [
            query,

            f"What is the policy regarding: {query}",

            f"What are the employee entitlements related to: {query}"
        ]