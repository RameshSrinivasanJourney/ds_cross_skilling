from app.services.cached_benchmark import (
    CachedBenchmark,
)
from app.services.llm_benchmark import (
    LLMBenchmark,
)


def print_metric(
    metric,
    cache_hit: bool | None = None,
):

    print(
        f"\nQuestion: {metric.question}"
    )

    print(
        f"Latency: "
        f"{metric.latency_ms:.2f} ms"
    )

    print(
        f"Input tokens: "
        f"{metric.input_tokens}"
    )

    print(
        f"Output tokens: "
        f"{metric.output_tokens}"
    )

    print(
        f"Total tokens: "
        f"{metric.total_tokens}"
    )

    print(
        f"LLM called: "
        f"{metric.llm_called}"
    )

    if cache_hit is not None:

        print(
            f"Cache hit: "
            f"{cache_hit}"
        )


def test_without_cache():

    print(
        "\n================================"
    )

    print(
        "EXPERIMENT 1 - WITHOUT CACHE"
    )

    print(
        "================================"
    )

    benchmark = LLMBenchmark()

    questions = [
        "What is RAG?",
        "What is RAG?",
        "What is RAG?",
    ]

    total_tokens = 0
    llm_calls = 0

    for question in questions:

        _, metric = benchmark.generate(
            question
        )

        print_metric(
            metric
        )

        total_tokens += (
            metric.total_tokens
        )

        if metric.llm_called:
            llm_calls += 1

    print(
        "\nSummary:"
    )

    print(
        f"Requests: {len(questions)}"
    )

    print(
        f"LLM calls: {llm_calls}"
    )

    print(
        f"Total tokens: {total_tokens}"
    )


def test_with_cache():

    print(
        "\n================================"
    )

    print(
        "EXPERIMENT 2 - WITH EXACT CACHE"
    )

    print(
        "================================"
    )

    benchmark = CachedBenchmark()

    questions = [
        "What is RAG?",
        "What is RAG?",
        "What is RAG?",
    ]

    total_tokens = 0
    llm_calls = 0
    cache_hits = 0

    for question in questions:

        (
            _,
            metric,
            cache_hit,
        ) = benchmark.generate(
            question
        )

        print_metric(
            metric,
            cache_hit,
        )

        total_tokens += (
            metric.total_tokens
        )

        if metric.llm_called:
            llm_calls += 1

        if cache_hit:
            cache_hits += 1

    print(
        "\nSummary:"
    )

    print(
        f"Requests: {len(questions)}"
    )

    print(
        f"LLM calls: {llm_calls}"
    )

    print(
        f"Cache hits: {cache_hits}"
    )

    print(
        f"Total tokens: {total_tokens}"
    )

    hit_rate = (
        cache_hits / len(questions)
    )

    print(
        f"Cache hit rate: "
        f"{hit_rate:.2%}"
    )


def test_semantically_similar_queries():

    print(
        "\n================================"
    )

    print(
        "EXPERIMENT 3 - SIMILAR QUERIES"
    )

    print(
        "================================"
    )

    benchmark = CachedBenchmark()

    questions = [
        "What is RAG?",
        "Explain Retrieval Augmented Generation.",
    ]

    for question in questions:

        (
            _,
            metric,
            cache_hit,
        ) = benchmark.generate(
            question
        )

        print_metric(
            metric,
            cache_hit,
        )

    print(
        "\nThese queries have similar meaning"
        " but will NOT share an exact cache"
        " entry."
    )


if __name__ == "__main__":

    test_without_cache()

    test_with_cache()

    test_semantically_similar_queries()