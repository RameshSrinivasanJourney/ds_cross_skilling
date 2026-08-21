from app.orchestration.dependency_graph import (
    build_dependency_graph,
)
from app.orchestration.task_decomposer import (
    decompose_leave_report,
)
from app.orchestration.task_executor import (
    execute_decomposed_tasks,
)


def test_task_decomposition():

    goal = (
        "Prepare a complete employee leave-policy report."
    )

    tasks = decompose_leave_report()

    print("\n=== TASK DEFINITIONS ===")

    for task in tasks:

        print(
            f"\nTask: {task.name}"
        )

        print(
            f"Dependencies: "
            f"{task.dependencies}"
        )

    graph = build_dependency_graph(
        tasks
    )

    print("\n=== DEPENDENCY GRAPH ===")

    for task, dependencies in graph.items():

        print(
            f"{task} <- {dependencies}"
        )

    print("\n=== EXECUTION ===")

    results = execute_decomposed_tasks(
        goal
    )

    print("\n=== FINAL RESULTS ===")

    for name, result in results.items():

        print(
            f"\n--- {name} ---"
        )
        print(result)


if __name__ == "__main__":
    test_task_decomposition()