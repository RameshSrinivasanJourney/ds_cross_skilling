import logging

from ollama import Client

from app.core.config import settings
from app.prompts.rag_prompt import RAGPrompt
from app.services.multi_query_service import MultiQueryService


logger = logging.getLogger("Module6")


class GenerationService:

    # ==========================================================
    # Generate Answer
    # ==========================================================

    @classmethod
    def generate(
        cls,
        query: str,
        top_k: int = 3
    ):

        logger.info(
            f"Generation started for query: {query}"
        )

        # ======================================================
        # STEP 1 — RETRIEVE CONTEXT
        # ======================================================

        retrieval_response = (
            MultiQueryService.retrieve(
                query=query,
                top_k=top_k
            )
        )

        results = retrieval_response.get(
            "results",
            []
        )

        # ======================================================
        # STEP 2 — HANDLE MISSING CONTEXT
        # ======================================================

        if not results:

            logger.warning(
                "No relevant documents found."
            )

            return {
                "query": query,

                "answer":
                    "I could not find this information "
                    "in the provided documents.",

                "context_used": False,

                "sources": []
            }

        # ======================================================
        # STEP 3 — BUILD SOURCE-AWARE CONTEXT
        # ======================================================

        context_parts = []

        sources = []

        for position, result in enumerate(
            results,
            start=1
        ):

            source_id = (
                f"Source {position}"
            )

            text = result.get(
                "text",
                ""
            )

            context_parts.append(
                f"""
[{source_id}]

{text}
"""
            )

            sources.append(
                {
                    "source_id":
                        source_id,

                    "point_id":
                        result.get(
                            "point_id",
                            ""
                        ),

                    "text":
                        text
                }
            )

        context = "\n".join(
            context_parts
        )

        # ======================================================
        # STEP 4 — BUILD RAG PROMPT
        # ======================================================

        prompt = RAGPrompt.build(
            query=query,
            context=context
        )

        logger.info(
            "RAG prompt created successfully."
        )

        # ======================================================
        # STEP 5 — CALL LLM
        # ======================================================

        answer = cls._generate_with_llm(
            prompt
        )

        # ======================================================
        # STEP 6 — RETURN RESPONSE
        # ======================================================

        return {

            "query":
                query,

            "answer":
                answer,

            "context_used":
                True,

            "sources":
                sources
        }

    # ==========================================================
    # LLM — Ollama
    # ==========================================================

    @staticmethod
    def _generate_with_llm(
        prompt: str
    ):

        logger.info(
            f"Calling Ollama model: "
            f"{settings.OLLAMA_MODEL}"
        )

        client = Client(
            host=settings.OLLAMA_HOST
        )

        response = client.chat(
            model=settings.OLLAMA_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        answer = response["message"]["content"]

        logger.info(
            "Ollama response received successfully."
        )

        return answer.strip()