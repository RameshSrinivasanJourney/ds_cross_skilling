from app.evaluation.code import (
    CodeEvaluator,
)


def test_code_generation():

    code = """
def add(a, b):
    return a + b
""".strip()

    tests = """
from solution import add

assert add(2, 3) == 5
assert add(-1, 1) == 0
assert add(10, 20) == 30

print("All tests passed")
""".strip()

    evaluator = CodeEvaluator()

    result = evaluator.evaluate(
        code,
        tests,
    )

    print(
        "\n=== CODE EVALUATION ==="
    )

    print(result)

    assert result["passed"] is True


if __name__ == "__main__":
    test_code_generation()