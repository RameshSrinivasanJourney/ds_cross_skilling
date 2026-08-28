import re
from dataclasses import dataclass

from ollama import Client

from collections import Counter



@dataclass
class SampleResult:
    response: str
    sentences: list[str]


class SelfCheckSampler:
    """
    Local SelfCheckGPT-style sampler.

    Generates multiple stochastic responses and
    measures sentence-level consistency.
    """

    def __init__(
        self,
        model: str = "llama3.2:3b",
    ) -> None:

        self.client = Client(
            host="http://localhost:11434"
        )

        self.model = model

    @staticmethod
    def split_sentences(
        text: str,
    ) -> list[str]:

        return [
            sentence.strip()
            for sentence in re.split(
                r"(?<=[.!?])\s+",
                text.strip(),
            )
            if sentence.strip()
        ]

    def generate_samples(
        self,
        prompt: str,
        sample_count: int = 5,
        temperature: float = 0.8,
    ) -> list[SampleResult]:

        results = []

        for _ in range(sample_count):

            response = self.client.chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                options={
                    "temperature": temperature
                },
            )

            text = (
                response.message.content
                or ""
            )

            results.append(
                SampleResult(
                    response=text,
                    sentences=(
                        self.split_sentences(
                            text
                        )
                    ),
                )
            )

        return results

class ConsistencyAnalyzer:

    @staticmethod
    def normalize(
        sentence: str,
    ) -> set[str]:

        words = re.findall(
            r"\b[a-zA-Z0-9]+\b",
            sentence.lower(),
        )

        return set(
            words
        )

    def similarity(
        self,
        sentence_a: str,
        sentence_b: str,
    ) -> float:

        words_a = self.normalize(
            sentence_a
        )

        words_b = self.normalize(
            sentence_b
        )

        if not words_a or not words_b:

            return 0.0

        intersection = (
            words_a & words_b
        )

        union = (
            words_a | words_b
        )

        return (
            len(intersection)
            / len(union)
        )

    def consistency_score(
        self,
        samples: list[SampleResult],
    ) -> float:

        sentences = [
            sentence
            for sample in samples
            for sentence in sample.sentences
        ]

        if len(sentences) < 2:

            return 1.0

        similarities = []

        for index, first in enumerate(
            sentences
        ):

            for second in sentences[
                index + 1:
            ]:

                similarities.append(
                    self.similarity(
                        first,
                        second,
                    )
                )

        if not similarities:

            return 0.0

        return (
            sum(similarities)
            / len(similarities)
        )