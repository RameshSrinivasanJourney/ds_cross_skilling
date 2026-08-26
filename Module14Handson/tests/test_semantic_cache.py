from app.services.semantic_cached_llm import (
    SemanticCachedLLM,
)


def print_result(
    label: str,
    result: dict,
) -> None:

    print(
        f"\n=== {label} ==="
    )

    print(
        f"Source: {result['source']}"
    )

    print(
        f"Cache hit: "
        f"{result['cache_hit']}"
    )

    print(
        f"Similarity: "
        f"{result['similarity']:.4f}"
    )

    print(
        f"Latency: "
        f"{result['latency_ms']:.2f} ms"
    )

    if result["matched_query"]:
        print(
            f"Matched query: "
            f"{result['matched_query']}"
        )

    print(
        f"Answer: "
        f"{result['answer'][:300]}"
    )


def test_semantic_cache():

    service = SemanticCachedLLM(
        threshold=0.85
    )

    first = service.generate(
        "What is RAG?"
    )

    print_result(
        "REQUEST 1",
        first,
    )

    second = service.generate(
        "Explain Retrieval-Augmented Generation."
    )

    print_result(
        "REQUEST 2",
        second,
    )

    third = service.generate(
        "What are embeddings in AI?"
    )

    print_result(
        "REQUEST 3",
        third,
    )


if __name__ == "__main__":
    test_semantic_cache()