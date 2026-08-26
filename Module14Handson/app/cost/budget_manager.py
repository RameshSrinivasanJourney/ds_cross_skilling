from dataclasses import dataclass


@dataclass
class Budget:
    limit: float
    spent: float = 0.0

    @property
    def remaining(self) -> float:
        return max(
            self.limit - self.spent,
            0.0,
        )

    @property
    def exceeded(self) -> bool:
        return self.spent >= self.limit

    def add_cost(
        self,
        amount: float,
    ) -> None:

        self.spent += amount


class BudgetManager:
    """Track project/user/feature budgets."""

    def __init__(
        self,
        project_limit: float,
        user_limit: float,
        feature_limit: float,
    ):

        self.project = Budget(
            project_limit
        )

        self.user_limit = user_limit
        self.feature_limit = feature_limit

        self.users: dict[
            str,
            Budget,
        ] = {}

        self.features: dict[
            str,
            Budget,
        ] = {}

    def ensure_user(
        self,
        user_id: str,
    ) -> Budget:

        if user_id not in self.users:

            self.users[user_id] = Budget(
                self.user_limit
            )

        return self.users[user_id]

    def ensure_feature(
        self,
        feature: str,
    ) -> Budget:

        if feature not in self.features:

            self.features[feature] = Budget(
                self.feature_limit
            )

        return self.features[feature]

    def can_spend(
        self,
        user_id: str,
        feature: str,
        estimated_cost: float,
    ) -> bool:

        user = self.ensure_user(
            user_id
        )

        feature_budget = (
            self.ensure_feature(
                feature
            )
        )

        return (
            not self.project.exceeded
            and not user.exceeded
            and not feature_budget.exceeded
            and (
                self.project.remaining
                >= estimated_cost
            )
            and (
                user.remaining
                >= estimated_cost
            )
            and (
                feature_budget.remaining
                >= estimated_cost
            )
        )

    def record_cost(
        self,
        user_id: str,
        feature: str,
        amount: float,
    ) -> None:

        self.project.add_cost(
            amount
        )

        self.ensure_user(
            user_id
        ).add_cost(
            amount
        )

        self.ensure_feature(
            feature
        ).add_cost(
            amount
        )