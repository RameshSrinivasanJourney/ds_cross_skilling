from app.hallucination.self_check import (
    ConsistencyAnalyzer,
    SelfCheckSampler,
)


def test_self_check():

    sampler = SelfCheckSampler()

    prompt = (
        "Explain Retrieval-Augmented Generation "
        "in simple terms."
    )

    samples = sampler.generate_samples(
        prompt,
        sample_count=5,
        temperature=0.8,
    )

    analyzer = ConsistencyAnalyzer()

    score = (
        analyzer.consistency_score(
            samples
        )
    )

    print(
        "\n=== SELFCHECKGPT-STYLE TEST ==="
    )

    for index, sample in enumerate(
        samples,
        start=1,
    ):

        print(
            f"\n--- SAMPLE {index} ---"
        )

        print(
            sample.response
        )

    print(
        "\nConsistency score:"
    )

    print(
        f"{score:.4f}"
    )


if __name__ == "__main__":
    test_self_check()