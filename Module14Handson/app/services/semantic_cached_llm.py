import time

from ollama import Client

from app.semantic_cache.embedding_service import (
    EmbeddingService,
)
from app.semantic_cache.semantic_cache import (
    SemanticCache,
)


MODEL_NAME = "llama3.2:3b"


class SemanticCachedLLM:
    """Ollama with semantic response caching."""

    def __init__(
        self,
        threshold: float = 0.85,
    ) -> None:

        self.client = Client(
            host="http://localhost:11434"
        )

        self.embedding_service = (
            EmbeddingService()
        )

        self.cache = SemanticCache(
            embedding_service=(
                self.embedding_service
            ),
            threshold=threshold,
        )

    def generate(
        self,
        query: str,
    ) -> dict:

        start = time.perf_counter()

        cached, similarity = (
            self.cache.lookup(
                query,
                MODEL_NAME,
            )
        )

        if cached is not None:

            latency = (
                time.perf_counter()
                - start
            ) * 1000

            return {
                "answer": cached.response,
                "cache_hit": True,
                "matched_query": cached.query,
                "similarity": similarity,
                "latency_ms": latency,
                "source": "semantic_cache",
            }

        response = self.client.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": query,
                }
            ],
        )

        answer = (
            response.message.content
        )

        self.cache.store(
            query=query,
            response=answer,
            model=MODEL_NAME,
        )

        latency = (
            time.perf_counter()
            - start
        ) * 1000

        return {
            "answer": answer,
            "cache_hit": False,
            "matched_query": None,
            "similarity": similarity,
            "latency_ms": latency,
            "source": "ollama",
        }