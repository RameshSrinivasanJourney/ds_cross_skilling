from app.agents.llm import ask_llm


class FlakyResearcher:
    """Researcher that fails on the first attempts."""

    def __init__(self):
        self.attempts = 0

    def run(
        self,
        question: str,
    ) -> str:
        self.attempts += 1

        if self.attempts < 3:
            raise RuntimeError(
                "Primary researcher temporary failure."
            )

        return ask_llm(
            system_prompt=(
                "You are a research specialist. "
                "Provide concise, useful information."
            ),
            user_prompt=question,
        )


def fallback_researcher(
    question: str,
) -> str:
    """Backup researcher."""

    return (
        "Fallback research result: "
        "Review the official company leave policy "
        "and contact HR for clarification."
    )