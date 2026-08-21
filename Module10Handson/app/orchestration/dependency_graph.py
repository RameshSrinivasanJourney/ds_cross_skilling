from app.orchestration.task_decomposer import (
    TaskDefinition,
)


def build_dependency_graph(
    tasks: list[TaskDefinition],
) -> dict[str, list[str]]:
    """Build task -> dependencies mapping."""

    return {
        task.name: task.dependencies
        for task in tasks
    }


def get_ready_tasks(
    tasks: list[TaskDefinition],
    completed: set[str],
) -> list[TaskDefinition]:
    """Return tasks whose dependencies are complete."""

    ready = []

    for task in tasks:

        if task.name in completed:
            continue

        if all(
            dependency in completed
            for dependency in task.dependencies
        ):
            ready.append(task)

    return ready