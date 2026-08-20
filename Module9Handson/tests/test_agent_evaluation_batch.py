from app.agent.evaluation_agent import (
    EvaluationAgent,
)
from app.evaluation.agent_evaluator import (
    AgentEvaluator,
)
from data.evaluation_cases import (
    EVALUATION_CASES,
)


def test_batch_agent_evaluation():

    agent = EvaluationAgent()

    total = len(
        EVALUATION_CASES
    )

    completed = 0

    trajectory_correct = 0

    total_efficiency = 0.0

    print("\n=== Agent Evaluation ===")

    for index, case in enumerate(
        EVALUATION_CASES,
        start=1,
    ):

        trace = agent.run(
            case["question"]
        )

        # Override expectations from
        # the evaluation dataset.
        trace.expected_tools = (
            case["expected_tools"]
        )

        trace.expected_steps = (
            case["expected_steps"]
        )

        evaluation = (
            AgentEvaluator.evaluate(
                trace
            )
        )

        if evaluation.task_completed:
            completed += 1

        if evaluation.trajectory_correct:
            trajectory_correct += 1

        total_efficiency += (
            evaluation.step_efficiency
        )

        print(
            f"\nCase {index}"
        )

        print(
            f"Question: "
            f"{case['question']}"
        )

        print(
            f"Completed: "
            f"{evaluation.task_completed}"
        )

        print(
            f"Trajectory Correct: "
            f"{evaluation.trajectory_correct}"
        )

        print(
            f"Steps: "
            f"{evaluation.actual_steps}"
        )

        print(
            f"Efficiency: "
            f"{evaluation.step_efficiency:.2f}"
        )

    completion_rate = (
        completed / total
    )

    trajectory_rate = (
        trajectory_correct / total
    )

    average_efficiency = (
        total_efficiency / total
    )

    print("\n=== Aggregate Metrics ===")

    print(
        f"Task Completion Rate: "
        f"{completion_rate:.2%}"
    )

    print(
        f"Trajectory Accuracy: "
        f"{trajectory_rate:.2%}"
    )

    print(
        f"Average Step Efficiency: "
        f"{average_efficiency:.2%}"
    )


if __name__ == "__main__":
    test_batch_agent_evaluation()