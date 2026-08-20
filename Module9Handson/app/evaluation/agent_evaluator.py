from dataclasses import dataclass

from app.evaluation.agent_trace import (
    AgentTrace,
)


@dataclass
class EvaluationResult:
    """Store evaluation metrics."""

    task_completed: bool

    trajectory_correct: bool

    step_efficiency: float

    actual_steps: int

    expected_steps: int

    actual_tools: list[str]

    expected_tools: list[str]

    summary: str


class AgentEvaluator:
    """Evaluate a single agent execution."""

    @staticmethod
    def evaluate(
        trace: AgentTrace,
    ) -> EvaluationResult:
        """Calculate evaluation metrics."""

        task_completed = (
            trace.completed
        )

        trajectory_correct = (
            trace.actual_tools
            == trace.expected_tools
        )

        if trace.step_count == 0:

            step_efficiency = 0.0

        else:

            step_efficiency = min(
                1.0,
                trace.expected_steps
                / trace.step_count,
            )

        summary = (
            f"Task Completed: "
            f"{task_completed}\n"
            f"Trajectory Correct: "
            f"{trajectory_correct}\n"
            f"Expected Steps: "
            f"{trace.expected_steps}\n"
            f"Actual Steps: "
            f"{trace.step_count}\n"
            f"Step Efficiency: "
            f"{step_efficiency:.2f}"
        )

        return EvaluationResult(
            task_completed=task_completed,
            trajectory_correct=trajectory_correct,
            step_efficiency=step_efficiency,
            actual_steps=trace.step_count,
            expected_steps=trace.expected_steps,
            actual_tools=trace.actual_tools,
            expected_tools=trace.expected_tools,
            summary=summary,
        )