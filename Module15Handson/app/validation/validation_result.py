from dataclasses import dataclass, field


@dataclass
class ValidationResult:
    valid: bool

    normalized_text: str

    reasons: list[str] = field(
        default_factory=list
    )

    categories: list[str] = field(
        default_factory=list
    )