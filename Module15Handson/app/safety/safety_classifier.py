import re

from app.safety.risk_categories import (
    RiskCategory,
    RiskLevel,
)

from app.safety.safety_result import (
    SafetyResult,
)


class SafetyClassifier:
    """
    Lightweight rule-based safety classifier.

    Educational implementation for demonstrating
    guardrail architecture. It is not a production
    moderation system.
    """

    BLOCK_RULES = {
        RiskCategory.VIOLENCE: [
            # Examples:
            # "how to build a bomb"
            # "how can I build a bomb"
            # "what can I do to make a bomb"
            r"\b(?:how|what)\s+"
            r"(?:to\s+|can\s+|could\s+|do\s+|"
            r"can\s+i\s+|could\s+i\s+|"
            r"do\s+i\s+)"
            r".*\b(?:build|make|create)\b"
            r".*\b(?:bomb|explosive|weapon)\b",

            r"\bhow\s+to\s+"
            r"(?:build|make|create)\s+"
            r"(?:a\s+)?"
            r"(?:bomb|explosive|weapon)\b",

            r"\b(?:kill|murder)\s+someone\b",
        ],

        RiskCategory.SELF_HARM: [
            r"\bhow\s+to\s+kill\s+myself\b",
            r"\bhow\s+to\s+commit\s+suicide\b",
            r"\bways\s+to\s+kill\s+myself\b",
        ],

        RiskCategory.ILLEGAL: [
            r"\bhow\s+to\s+hack\s+a\s+bank\b",
            r"\bsteal\s+someone'?s\s+password\b",
        ],
    }

    REVIEW_RULES = {
        RiskCategory.PRIVACY: [
            r"\bssn\b",
            r"\bsocial\s+security\s+number\b",
            r"\bcredit\s+card\b",
            r"\bpassword\b",
        ],

        RiskCategory.BIAS: [
            r"\bwhich\s+race\s+is\s+better\b",
            r"\bwhich\s+gender\s+is\s+superior\b",
        ],

        RiskCategory.COMPLIANCE: [
            r"\bpatient\s+record\b",
            r"\bmedical\s+record\b",
            r"\bprotected\s+health\s+information\b",
        ],

        RiskCategory.PROMPT_INJECTION: [
            r"\bignore\s+(?:all\s+)?previous\s+instructions\b",
            r"\bignore\s+(?:all\s+)?prior\s+instructions\b",
            r"\breveal\s+your\s+system\s+prompt\b",
            r"\bshow\s+your\s+system\s+prompt\b",
            r"\breveal\s+the\s+developer\s+message\b",
            r"\bshow\s+the\s+developer\s+message\b",
        ],
    }

    def classify(
        self,
        text: str,
    ) -> SafetyResult:

        normalized = re.sub(
            r"\s+",
            " ",
            text.lower().strip(),
        )

        blocked_categories = []
        review_categories = []

        reasons = []
        matched_rules = []

        # ---------------------------------
        # BLOCK RULES
        # ---------------------------------

        for category, patterns in (
            self.BLOCK_RULES.items()
        ):

            category_matched = False

            for pattern in patterns:

                if re.search(
                    pattern,
                    normalized,
                ):

                    category_matched = True

                    matched_rules.append(
                        pattern
                    )

            if category_matched:

                blocked_categories.append(
                    category
                )

                reasons.append(
                    f"Blocked pattern detected "
                    f"for {category.value}."
                )

        if blocked_categories:

            return SafetyResult(
                level=RiskLevel.BLOCK,
                categories=list(
                    dict.fromkeys(
                        blocked_categories
                    )
                ),
                reasons=list(
                    dict.fromkeys(
                        reasons
                    )
                ),
                matched_rules=list(
                    dict.fromkeys(
                        matched_rules
                    )
                ),
            )

        # ---------------------------------
        # REVIEW RULES
        # ---------------------------------

        for category, patterns in (
            self.REVIEW_RULES.items()
        ):

            category_matched = False

            for pattern in patterns:

                if re.search(
                    pattern,
                    normalized,
                ):

                    category_matched = True

                    matched_rules.append(
                        pattern
                    )

            if category_matched:

                review_categories.append(
                    category
                )

                reasons.append(
                    f"Review pattern detected "
                    f"for {category.value}."
                )

        if review_categories:

            return SafetyResult(
                level=RiskLevel.REVIEW,
                categories=list(
                    dict.fromkeys(
                        review_categories
                    )
                ),
                reasons=list(
                    dict.fromkeys(
                        reasons
                    )
                ),
                matched_rules=list(
                    dict.fromkeys(
                        matched_rules
                    )
                ),
            )

        # ---------------------------------
        # SAFE
        # ---------------------------------

        return SafetyResult(
            level=RiskLevel.SAFE,
            categories=[],
            reasons=[
                "No configured safety rules matched."
            ],
            matched_rules=[],
        )