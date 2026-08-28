from dataclasses import dataclass, field


@dataclass
class EvaluationResult:
    metric: str
    value: float
    threshold: float
    passed: bool


@dataclass
class EvaluationReport:
    prompt_version: str
    model_version: str
    dataset_version: str

    results: list[EvaluationResult] = field(
        default_factory=list
    )

    @property
    def passed(self) -> bool:
        return all(
            result.passed
            for result in self.results
        )