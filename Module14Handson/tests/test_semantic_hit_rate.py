from app.services.semantic_cached_llm import (
    SemanticCachedLLM,
)


def test_hit_rate():

    service = SemanticCachedLLM(
        threshold=0.85
    )

    queries = [
        "What is RAG?",
        "Explain retrieval augmented generation.",
        "What is retrieval augmented generation?",
        "Explain embeddings.",
        "What are embeddings in AI?",
        "What is the weather in Chennai?",
    ]

    hits = 0
    misses = 0

    for query in queries:

        result = service.generate(
            query
        )

        if result["cache_hit"]:
            hits += 1
        else:
            misses += 1

        print(
            f"\nQuery: {query}"
        )

        print(
            f"Hit: {result['cache_hit']}"
        )

        print(
            f"Similarity: "
            f"{result['similarity']:.4f}"
        )

    total = (
        hits + misses
    )

    hit_rate = (
        hits / total
        if total
        else 0.0
    )

    print(
        "\n=== CACHE METRICS ==="
    )

    print(
        f"Total requests: {total}"
    )

    print(
        f"Hits: {hits}"
    )

    print(
        f"Misses: {misses}"
    )

    print(
        f"Hit rate: "
        f"{hit_rate:.2%}"
    )


if __name__ == "__main__":
    test_hit_rate()