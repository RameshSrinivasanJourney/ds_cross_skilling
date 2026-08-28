import json

from ollama import Client


JUDGE_MODEL = "llama3.2:3b"


class LLMJudge:
    """Use an LLM to evaluate another model response."""

    def __init__(
        self,
        model: str = JUDGE_MODEL,
    ) -> None:

        self.client = Client(
            host="http://localhost:11434"
        )

        self.model = model

    def _call_judge(
        self,
        prompt: str,
    ) -> str:

        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return (
            response.message.content
            or ""
        )

    def pointwise(
        self,
        question: str,
        answer: str,
        reference: str | None = None,
    ) -> dict:

        reference_section = ""

        if reference:

            reference_section = f"""
Reference answer:
{reference}
""".strip()

        prompt = f"""
You are an impartial evaluator.

Evaluate the answer to the user's question.

Question:
{question}

Answer:
{answer}

{reference_section}

Score the answer from 1 to 5:

1 = Completely incorrect or unusable
2 = Mostly incorrect
3 = Partially correct
4 = Mostly correct and useful
5 = Excellent, correct, relevant, and complete

Evaluate these dimensions:
- correctness
- relevance
- completeness
- clarity

Return ONLY valid JSON:

{{
  "score": 1,
  "reason": "brief explanation"
}}
""".strip()

        raw = self._call_judge(
            prompt
        )

        try:

            result = json.loads(raw)

        except json.JSONDecodeError:

            result = {
                "score": None,
                "reason": (
                    "Judge returned "
                    "non-JSON output."
                ),
                "raw": raw,
            }

        return result

    def pairwise(
        self,
        question: str,
        answer_a: str,
        answer_b: str,
    ) -> dict:

        prompt = f"""
You are an impartial evaluator.

Compare two answers to the same question.

Question:
{question}

Answer A:
{answer_a}

Answer B:
{answer_b}

Choose the better answer based on:
- correctness
- relevance
- completeness
- clarity

Do NOT prefer an answer merely because it is longer.

Return ONLY valid JSON:

{{
  "winner": "A",
  "reason": "brief explanation"
}}

Allowed winner values:
A
B
tie
""".strip()

        raw = self._call_judge(
            prompt
        )

        try:

            result = json.loads(raw)

        except json.JSONDecodeError:

            result = {
                "winner": None,
                "reason": (
                    "Judge returned "
                    "non-JSON output."
                ),
                "raw": raw,
            }

        return result