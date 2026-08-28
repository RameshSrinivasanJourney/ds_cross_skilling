from app.judges.calibration import (
    calibrate,
)


def test_calibration():

    human_scores = [
        5,
        4,
        3,
        4,
        2,
        5,
        3,
        4,
        1,
        5,
    ]

    judge_scores = [
        5,
        4,
        3,
        3,
        2,
        5,
        4,
        4,
        1,
        4,
    ]

    result = calibrate(
        human_scores,
        judge_scores,
    )

    print(
        "\n=== JUDGE CALIBRATION ==="
    )

    print(
        f"Total: {result.total}"
    )

    print(
        f"Exact matches: "
        f"{result.exact_matches}"
    )

    print(
        f"Agreement rate: "
        f"{result.agreement_rate:.2%}"
    )


if __name__ == "__main__":
    test_calibration()