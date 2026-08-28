from app.evaluation.gate import (
    EvaluationGate,
)


def test_evaluation_gate_pass():

    gate = EvaluationGate()

    report = gate.evaluate(
        exact_match=0.80,
        rouge_l=0.75,
        faithfulness=0.90,
        judge_score=4.20,
        hallucination_rate=0.05,
    )

    print(
        "\n=== PASSING EVALUATION ==="
    )

    for result in report.results:

        print(
            f"{result.metric}: "
            f"{result.value:.4f} "
            f"(threshold={result.threshold:.4f}) "
            f"PASS={result.passed}"
        )

    print(
        f"\nOverall: {report.passed}"
    )

    assert report.passed is True


def test_evaluation_gate_fail():

    gate = EvaluationGate()

    report = gate.evaluate(
        exact_match=0.80,
        rouge_l=0.40,
        faithfulness=0.90,
        judge_score=4.20,
        hallucination_rate=0.05,
    )

    print(
        "\n=== FAILING EVALUATION ==="
    )

    for result in report.results:

        print(
            f"{result.metric}: "
            f"{result.value:.4f} "
            f"(threshold={result.threshold:.4f}) "
            f"PASS={result.passed}"
        )

    print(
        f"\nOverall: {report.passed}"
    )

    assert report.passed is False


if __name__ == "__main__":

    test_evaluation_gate_pass()

    test_evaluation_gate_fail()