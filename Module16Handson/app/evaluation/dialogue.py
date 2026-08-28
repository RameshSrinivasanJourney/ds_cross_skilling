class DialogueEvaluator:

    def evaluate(
        self,
        conversation: list[dict],
        final_response: str,
        required_terms: list[str] | None = None,
    ) -> dict:

        required_terms = (
            required_terms
            or []
        )

        response = (
            final_response.strip()
        )

        coherence = (
            1.0
            if response
            else 0.0
        )

        context_turns = sum(
            1
            for message
            in conversation
            if message.get("role")
            in {"user", "assistant"}
        )

        context_score = min(
            context_turns / 4,
            1.0,
        )

        if required_terms:

            matched = sum(
                term.lower()
                in response.lower()
                for term in required_terms
            )

            task_completion = (
                matched
                / len(required_terms)
            )

        else:

            task_completion = 1.0

        return {
            "coherence": coherence,
            "context_score": context_score,
            "task_completion": (
                task_completion
            ),
        }