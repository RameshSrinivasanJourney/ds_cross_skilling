from dataclasses import dataclass, field

from app.moderation.categories import (
    ModerationCategory,
    ModerationDecision,
)


@dataclass
class ModerationResult:
    decision: ModerationDecision

    categories: list[
        ModerationCategory
    ] = field(
        default_factory=list
    )

    reason: str = ""

    score: float = 0.0

    matched_rules: list[str] = field(
        default_factory=list
    )