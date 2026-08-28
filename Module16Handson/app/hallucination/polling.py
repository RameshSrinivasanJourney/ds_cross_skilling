import re
from collections import Counter

from ollama import Client


class PollingEvaluator:

    def __init__(
        self,
        model: str = "llama3.2:3b",
    ) -> None:

        self.client = Client(
            host="http://localhost:11434"
        )

        self.model = model

    def _judge(
        self,
        context: str,
        answer: str,
        temperature: float = 0.5,
    ) -> str:

        prompt = f"""
Determine whether the answer is supported by
the provided context.

Context:
{context}

Answer:
{answer}

Return exactly one word:

SUPPORTED

or

UNSUPPORTED
""".strip()

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
        ).upper()

        if "UNSUPPORTED" in text:

            return "UNSUPPORTED"

        if "SUPPORTED" in text:

            return "SUPPORTED"

        return "UNKNOWN"

    def evaluate(
        self,
        context: str,
        answer: str,
        polls: int = 5,
    ) -> dict:

        votes = []

        for _ in range(polls):

            votes.append(
                self._judge(
                    context,
                    answer,
                )
            )

        counts = Counter(
            votes
        )

        winner, count = (
            counts.most_common(1)[0]
        )

        return {
            "decision": winner,
            "votes": votes,
            "counts": dict(counts),
            "agreement": (
                count / len(votes)
            ),
        }