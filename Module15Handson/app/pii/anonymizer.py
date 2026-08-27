from presidio_anonymizer import (
    AnonymizerEngine,
)


class PIIAnonymizer:
    """Replace detected PII with placeholders."""

    def __init__(self) -> None:

        self.engine = (
            AnonymizerEngine()
        )

    def anonymize(
        self,
        text: str,
        entities,
    ):

        return self.engine.anonymize(
            text=text,
            analyzer_results=entities,
        )