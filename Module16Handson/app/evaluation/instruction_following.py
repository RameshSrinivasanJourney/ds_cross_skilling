import json


class InstructionFollowingEvaluator:

    def evaluate(
        self,
        response: str,
        *,
        required_terms: list[str] | None = None,
        max_words: int | None = None,
        required_bullets: int | None = None,
        require_json: bool = False,
    ) -> dict:

        required_terms = (
            required_terms
            or []
        )

        checks = {}

        # Required terms

        checks["required_terms"] = all(
            term.lower()
            in response.lower()
            for term in required_terms
        )

        # Maximum words

        if max_words is not None:

            checks["max_words"] = (
                len(response.split())
                <= max_words
            )

        # Bullet count

        if required_bullets is not None:

            bullet_lines = [
                line
                for line in response.splitlines()
                if line.strip().startswith(
                    ("-", "*")
                )
            ]

            checks["bullet_count"] = (
                len(bullet_lines)
                == required_bullets
            )

        # JSON

        if require_json:

            try:

                json.loads(response)

                checks["valid_json"] = True

            except json.JSONDecodeError:

                checks["valid_json"] = False

        passed = all(
            checks.values()
        )

        return {
            "passed": passed,
            "checks": checks,
        }