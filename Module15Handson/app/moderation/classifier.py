import re

from app.moderation.categories import (
    ModerationCategory,
    ModerationDecision,
)

from app.moderation.result import (
    ModerationResult,
)


class ModerationClassifier:
    """
    Educational rule-based moderation classifier.

    It demonstrates the moderation architecture.
    It is not a production content moderation model.
    """

    BLOCK_RULES = {
        ModerationCategory.VIOLENCE: [
            r"\bhow\s+to\s+build\s+a\s+bomb\b",
            r"\bhow\s+can\s+i\s+build\s+a\s+bomb\b",
            r"\bhow\s+to\s+make\s+a\s+weapon\b",
            r"\bkill\s+someone\b",
        ],

        ModerationCategory.SELF_HARM: [
            r"\bhow\s+to\s+kill\s+myself\b",
            r"\bhow\s+to\s+commit\s+suicide\b",
        ],

        ModerationCategory.ILLEGAL: [
            r"\bhow\s+to\s+hack\s+a\s+bank\b",
            r"\bsteal\s+someone'?s\s+password\b",
        ],
    }

    REVIEW_RULES = {
        ModerationCategory.PRIVACY: [
            r"\bssn\b",
            r"\bsocial\s+security\s+number\b",
            r"\bcredit\s+card\b",
            r"\bpassword\b",
        ],

        ModerationCategory.PROMPT_INJECTION: [
            r"\bignore\s+(?:all\s+)?previous\s+instructions\b",
            r"\breveal\s+your\s+system\s+prompt\b",
            r"\bshow\s+your\s+system\s+prompt\b",
            r"\breveal\s+the\s+developer\s+message\b",
        ],
    }

    def classify(
        self,
        text: str,
    ) -> ModerationResult:

        normalized = re.sub(
            r"\s+",
            " ",
            text.lower().strip(),
        )

        blocked_categories = []
        review_categories = []

        matched_rules = []

        # --------------------------------
        # BLOCK
        # --------------------------------

        for category, patterns in (
            self.BLOCK_RULES.items()
        ):

            for pattern in patterns:

                if re.search(
                    pattern,
                    normalized,
                ):

                    if category not in (
                        blocked_categories
                    ):

                        blocked_categories.append(
                            category
                        )

                    matched_rules.append(
                        pattern
                    )

        if blocked_categories:

            return ModerationResult(
                decision=(
                    ModerationDecision.BLOCK
                ),
                categories=blocked_categories,
                reason=(
                    "Blocked content detected."
                ),
                score=1.0,
                matched_rules=list(
                    dict.fromkeys(
                        matched_rules
                    )
                ),
            )

        # --------------------------------
        # REVIEW
        # --------------------------------

        for category, patterns in (
            self.REVIEW_RULES.items()
        ):

            for pattern in patterns:

                if re.search(
                    pattern,
                    normalized,
                ):

                    if category not in (
                        review_categories
                    ):

                        review_categories.append(
                            category
                        )

                    matched_rules.append(
                        pattern
                    )

        if review_categories:

            return ModerationResult(
                decision=(
                    ModerationDecision.REVIEW
                ),
                categories=review_categories,
                reason=(
                    "Content requires "
                    "additional moderation review."
                ),
                score=0.6,
                matched_rules=list(
                    dict.fromkeys(
                        matched_rules
                    )
                ),
            )

        # --------------------------------
        # ALLOW
        # --------------------------------

        return ModerationResult(
            decision=(
                ModerationDecision.ALLOW
            ),
            categories=[],
            reason="No moderation rules matched.",
            score=0.0,
            matched_rules=[],
        )