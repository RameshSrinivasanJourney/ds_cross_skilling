import logging

from app.agents.writer_agent import writer_agent
from app.reliability.fallback import (
    FlakyResearcher,
    fallback_researcher,
)
from app.reliability.guardrails import (
    validate_agent_output,
)
from app.reliability.retry import (
    execute_with_retry,
)
from app.reliability.timeout import (
    execute_with_timeout,
)


MAX_ITERATIONS = 3

TOOL_TIMEOUT_SECONDS = 10.0


logger = logging.getLogger(
    "multi_agent_reliability"
)


def run_reliable_multi_agent(
    question: str,
) -> dict:
    """Run a multi-agent workflow with reliability controls."""

    logger.info(
        "workflow_started question=%s",
        question,
    )

    primary = FlakyResearcher()

    research = None

    for iteration in range(
        1,
        MAX_ITERATIONS + 1,
    ):
        logger.info(
            "research_iteration=%s",
            iteration,
        )

        try:

            research = execute_with_timeout(
                execute_with_retry,
                primary.run,
                question,
                max_retries=0,
                timeout_seconds=TOOL_TIMEOUT_SECONDS,
            )

            research = validate_agent_output(
                research
            )

            logger.info(
                "research_success iteration=%s",
                iteration,
            )

            break

        except Exception as exc:

            logger.error(
                "research_failure iteration=%s error=%s",
                iteration,
                exc,
            )

            research = None

    # ----------------------------------------
    # Fallback agent
    # ----------------------------------------

    if research is None:

        logger.warning(
            "primary_researcher_failed "
            "using_fallback=true"
        )

        research = fallback_researcher(
            question
        )

        research = validate_agent_output(
            research
        )

    # ----------------------------------------
    # Writer
    # ----------------------------------------

    logger.info(
        "writer_started"
    )

    draft = writer_agent(
        question,
        research,
        research,
    )

    draft = validate_agent_output(
        draft
    )

    logger.info(
        "workflow_completed"
    )

    return {
        "research": research,
        "draft": draft,
    }