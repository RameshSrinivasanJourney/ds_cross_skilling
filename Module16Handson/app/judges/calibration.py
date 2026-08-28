from dataclasses import dataclass


@dataclass
class CalibrationResult:
    total: int
    exact_matches: int
    agreement_rate: float


def calibrate(
    human_scores: list[int],
    judge_scores: list[int],
) -> CalibrationResult:

    if len(human_scores) != len(
        judge_scores
    ):

        raise ValueError(
            "Human and judge score lists "
            "must have the same length."
        )

    if not human_scores:

        return CalibrationResult(
            total=0,
            exact_matches=0,
            agreement_rate=0.0,
        )

    matches = sum(
        human == judge
        for human, judge in zip(
            human_scores,
            judge_scores,
        )
    )

    return CalibrationResult(
        total=len(human_scores),
        exact_matches=matches,
        agreement_rate=(
            matches
            / len(human_scores)
        ),
    )