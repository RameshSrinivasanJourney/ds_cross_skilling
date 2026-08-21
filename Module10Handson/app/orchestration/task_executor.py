from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed,
)

from app.agents.analyst_agent import (
    analyst_agent,
)
from app.agents.researcher_agent import (
    researcher_agent,
)
from app.agents.writer_agent import (
    writer_agent,
)
from app.orchestration.dependency_graph import (
    get_ready_tasks,
)
from app.orchestration.task_decomposer import (
    decompose_leave_report,
)


def _execute_task(
    task_name: str,
    goal: str,
    results: dict[str, str],
) -> str:
    """Execute one task."""

    if task_name == "policy_research":

        return researcher_agent(
            (
                "Research policy information for: "
                f"{goal}"
            )
        )

    if task_name == "eligibility_research":

        return researcher_agent(
            (
                "Research eligibility information "
                f"for: {goal}"
            )
        )

    if task_name == "process_research":

        return researcher_agent(
            (
                "Research process/procedure "
                f"information for: {goal}"
            )
        )

    if task_name == "analysis":

        research = (
            f"Policy Research:\n"
            f"{results['policy_research']}\n\n"
            f"Eligibility Research:\n"
            f"{results['eligibility_research']}\n\n"
            f"Process Research:\n"
            f"{results['process_research']}"
        )

        return analyst_agent(
            goal,
            research,
        )

    if task_name == "report":

        return writer_agent(
            goal,
            results["analysis"],
            results["analysis"],
        )

    raise ValueError(
        f"Unknown task: {task_name}"
    )


def execute_decomposed_tasks(
    goal: str,
) -> dict[str, str]:
    """Execute tasks according to dependencies."""

    tasks = decompose_leave_report()

    completed: set[str] = set()

    results: dict[str, str] = {}

    while len(completed) < len(tasks):

        ready_tasks = get_ready_tasks(
            tasks,
            completed,
        )

        if not ready_tasks:
            raise RuntimeError(
                "No executable tasks remain. "
                "Dependency graph may contain a cycle."
            )

        # ---------------------------------------
        # Independent tasks run in parallel.
        # ---------------------------------------

        with ThreadPoolExecutor(
            max_workers=len(ready_tasks)
        ) as executor:

            futures = {
                executor.submit(
                    _execute_task,
                    task.name,
                    goal,
                    results,
                ): task
                for task in ready_tasks
            }

            for future in as_completed(
                futures
            ):

                task = futures[future]

                results[task.name] = (
                    future.result()
                )

                completed.add(
                    task.name
                )

                print(
                    f"\nCompleted task: "
                    f"{task.name}"
                )

    return results