from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentStep:
    """Represent one observable agent step."""

    step_number: int
    action: str
    arguments: dict[str, Any]
    result: Any
    success: bool = True


@dataclass
class AgentTrace:
    """Store an agent execution trajectory."""

    user_question: str

    expected_tools: list[str]

    expected_steps: int

    final_answer: str = ""

    completed: bool = False

    steps: list[AgentStep] = field(
        default_factory=list
    )

    def add_step(
        self,
        action: str,
        arguments: dict[str, Any],
        result: Any,
        success: bool = True,
    ) -> None:
        """Record one agent action."""

        self.steps.append(
            AgentStep(
                step_number=len(self.steps) + 1,
                action=action,
                arguments=arguments,
                result=result,
                success=success,
            )
        )

    @property
    def actual_tools(self) -> list[str]:
        """Return tools in execution order."""

        return [
            step.action
            for step in self.steps
        ]

    @property
    def step_count(self) -> int:
        """Return number of agent tool steps."""

        return len(self.steps)