from app.semantic_cache.embedding_service import (
    EmbeddingService,
)
from app.semantic_cache.semantic_cache import (
    SemanticCache,
)


def test_thresholds():

    embedding_service = (
        EmbeddingService()
    )

    cache = SemanticCache(
        embedding_service,
        threshold=0.0,
    )

    cache.store(
        query="What is RAG?",
        response="RAG combines retrieval and generation.",
        model="llama3.2:3b",
    )

    queries = [
        "Explain Retrieval-Augmented Generation.",
        "What is the weather today?",
    ]

    for query in queries:

        entry, score = cache.lookup(
            query,
            "llama3.2:3b",
        )

        print(
            f"\nQuery: {query}"
        )

        print(
            f"Best similarity: "
            f"{score:.4f}"
        )


if __name__ == "__main__":
    test_thresholds()