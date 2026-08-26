from app.services.cached_llm import (
    CachedLLM,
)


def test_exact_cache():

    service = CachedLLM()

    prompt = (
        "Explain Retrieval-Augmented "
        "Generation in simple terms."
    )

    print(
        "\n=== REQUEST 1 ==="
    )

    first = service.generate(
        prompt
    )

    print(
        first
    )

    print(
        "\n=== REQUEST 2 ==="
    )

    second = service.generate(
        prompt
    )

    print(
        second
    )

    print(
        "\n=== RESULT ==="
    )

    print(
        f"First source: "
        f"{first['source']}"
    )

    print(
        f"Second source: "
        f"{second['source']}"
    )

    print(
        f"First cache hit: "
        f"{first['cache_hit']}"
    )

    print(
        f"Second cache hit: "
        f"{second['cache_hit']}"
    )

    print(
        f"First latency: "
        f"{first['latency_ms']:.2f} ms"
    )

    print(
        f"Second latency: "
        f"{second['latency_ms']:.2f} ms"
    )

    assert first["cache_hit"] is False

    assert second["cache_hit"] is True

    assert second["source"] == "cache"


if __name__ == "__main__":
    test_exact_cache()