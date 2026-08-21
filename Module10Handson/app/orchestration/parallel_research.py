from concurrent.futures import ThreadPoolExecutor

from app.agents.researcher_agent import research_agent


def run_parallel_research(
    question: str,
) -> dict[str, str]:
    """Run independent research tasks in parallel."""

    research_questions = {
        "policy": (
            f"Identify the important policy facts "
            f"needed for this question:\n{question}"
        ),
        "process": (
            f"Identify the process/procedure information "
            f"needed for this question:\n{question}"
        ),
    }

    with ThreadPoolExecutor(
        max_workers=2
    ) as executor:

        futures = {
            name: executor.submit(
                research_agent,
                prompt,
            )
            for name, prompt in research_questions.items()
        }

        return {
            name: future.result()
            for name, future in futures.items()
        }