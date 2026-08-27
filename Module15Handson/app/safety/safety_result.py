from dataclasses import dataclass, field

from app.safety.risk_categories import (
    RiskCategory,
    RiskLevel,
)


@dataclass
class SafetyResult:
    level: RiskLevel

    categories: list[
        RiskCategory
    ] = field(
        default_factory=list
    )

    reasons: list[str] = field(
        default_factory=list
    )

    matched_rules: list[str] = field(
        default_factory=list
    )

    @property
    def allowed(self) -> bool:
        return self.level != RiskLevel.BLOCK