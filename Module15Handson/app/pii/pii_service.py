from presidio_anonymizer import (
    AnonymizerEngine,
)

from app.pii.presidio_detector import (
    PIIDetector,
)


class PIIService:
    """Detect and anonymize PII."""

    def __init__(self) -> None:

        self.detector = (
            PIIDetector()
        )

        self.anonymizer = (
            AnonymizerEngine()
        )

    def anonymize(
        self,
        text: str,
    ) -> dict:

        entities = (
            self.detector.analyze(
                text
            )
        )

        result = (
            self.anonymizer.anonymize(
                text=text,
                analyzer_results=entities,
            )
        )

        return {
            "original": text,
            "anonymized": result.text,
            "entities": [
                {
                    "type": entity.entity_type,
                    "start": entity.start,
                    "end": entity.end,
                    "score": entity.score,
                }
                for entity in entities
            ],
        }