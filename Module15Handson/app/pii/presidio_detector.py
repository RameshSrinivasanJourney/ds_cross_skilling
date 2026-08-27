from presidio_analyzer import (
    AnalyzerEngine,
)


class PIIDetector:
    """Detect common PII using Presidio."""

    def __init__(self) -> None:

        self.analyzer = AnalyzerEngine()

    def analyze(
        self,
        text: str,
    ):
        return self.analyzer.analyze(
            text=text,
            language="en",
        )