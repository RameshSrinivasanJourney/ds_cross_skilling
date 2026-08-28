from app.datasets.dataset_loader import (
    load_json_dataset,
)

from app.datasets.dataset_validator import (
    validate_golden_dataset,
)


def test_datasets():

    golden = load_json_dataset(
        "data/golden/qa_golden.json"
    )

    adversarial = load_json_dataset(
        "data/adversarial/qa_adversarial.json"
    )

    errors = validate_golden_dataset(
        golden
    )

    print(
        "\n=== GOLDEN DATASET ==="
    )

    print(
        f"Examples: {len(golden)}"
    )

    print(
        f"Validation errors: {errors}"
    )

    print(
        "\n=== ADVERSARIAL DATASET ==="
    )

    print(
        f"Examples: {len(adversarial)}"
    )

    assert not errors

    assert len(golden) == 5

    assert len(adversarial) == 3


if __name__ == "__main__":
    test_datasets()