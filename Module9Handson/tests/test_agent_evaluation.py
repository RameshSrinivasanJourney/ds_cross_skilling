from app.agent.evaluation_agent import (
    EvaluationAgent,
)
from app.evaluation.agent_evaluator import (
    AgentEvaluator,
)


def test_agent_evaluation():

    agent = EvaluationAgent()

    question = (
        "What is the current weather in Chennai?"
    )

    print("\nUser:")
    print(question)

    trace = agent.run(
        question
    )

    print("\nAgent Trace:")

    print(
        f"Question: "
        f"{trace.user_question}"
    )

    for step in trace.steps:

        print(
            f"\nStep {step.step_number}"
        )

        print(
            f"Action: "
            f"{step.action}"
        )

        print(
            f"Arguments: "
            f"{step.arguments}"
        )

        print(
            f"Result: "
            f"{step.result}"
        )

        print(
            f"Success: "
            f"{step.success}"
        )

    print("\nFinal Answer:")
    print(trace.final_answer)

    evaluation = (
        AgentEvaluator.evaluate(
            trace
        )
    )

    print("\nEvaluation:")
    print(evaluation.summary)


if __name__ == "__main__":
    test_agent_evaluation()