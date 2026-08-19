import json
import logging
from pathlib import Path

from app.services.rag_service import RAGService
from app.services.generation_service import GenerationService


logger = logging.getLogger("Module6")


class EvaluationService:

    # ==========================================================
    # Dataset
    # ==========================================================

    DATASET_PATH = (
        Path(__file__)
        .resolve()
        .parent.parent
        / "data"
        / "golden_qa.json"
    )

    # ==========================================================
    # Evaluate
    # ==========================================================

    @classmethod
    def evaluate(
        cls,
        top_k: int = 5
    ):

        logger.info(
            "RAG evaluation started."
        )

        dataset = cls._load_dataset()

        results = []

        for item in dataset:

            question = item["question"]

            ground_truth = item["ground_truth"]

            logger.info(
                f"Evaluating question: {question}"
            )

            # ==================================================
            # STEP 1 — RETRIEVAL
            # ==================================================

            retrieval_response = (
                RAGService.retrieve(
                    query=question,
                    top_k=top_k
                )
            )

            retrieved_contexts = [
                result["text"]
                for result
                in retrieval_response["results"]
            ]

            # ==================================================
            # STEP 2 — GENERATION
            # ==================================================

            generation_response = (
                GenerationService.generate(
                    query=question,
                    top_k=top_k
                )
            )

            answer = generation_response.get(
                "answer",
                ""
            )

            # ==================================================
            # STEP 3 — RETRIEVAL @ K
            # ==================================================

            retrieval_at_k = (
                cls._calculate_retrieval_at_k(
                    ground_truth=ground_truth,
                    retrieved_contexts=retrieved_contexts
                )
            )

            results.append(
                {
                    "question":
                        question,

                    "ground_truth":
                        ground_truth,

                    "answer":
                        answer,

                    "retrieved_contexts":
                        retrieved_contexts,

                    "retrieval_at_k":
                        retrieval_at_k
                }
            )

        # ======================================================
        # STEP 4 — SUMMARY
        # ======================================================

        return cls._build_summary(
            results
        )

    # ==========================================================
    # Retrieval @ K
    # ==========================================================

    @staticmethod
    def _calculate_retrieval_at_k(
        ground_truth: str,
        retrieved_contexts: list[str]
    ):

        if not retrieved_contexts:

            return 0.0

        ground_truth_words = set(
            ground_truth.lower().split()
        )

        if not ground_truth_words:

            return 0.0

        best_score = 0.0

        for context in retrieved_contexts:

            context_words = set(
                context.lower().split()
            )

            overlap = (
                ground_truth_words
                & context_words
            )

            score = (
                len(overlap)
                / len(ground_truth_words)
            )

            best_score = max(
                best_score,
                score
            )

        return round(
            best_score,
            4
        )

    # ==========================================================
    # Dataset Loader
    # ==========================================================

    @classmethod
    def _load_dataset(cls):

        with open(
            cls.DATASET_PATH,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    # ==========================================================
    # Summary
    # ==========================================================

    @classmethod
    def _build_summary(
        cls,
        results
    ):

        def average(field):

            values = [
                item[field]
                for item in results
                if item[field] is not None
            ]

            if not values:

                return None

            return round(
                sum(values) / len(values),
                4
            )

        return {

            "total_questions":
                len(results),

            "average_retrieval_at_k":
                average(
                    "retrieval_at_k"
                ),

            "results":
                results
        }