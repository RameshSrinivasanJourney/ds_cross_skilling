from langfuse import (
    observe,
    propagate_attributes,
)

from app.tracing.langfuse_client import (
    langfuse,
)
from app.tracing.langfuse_ollama import (
    generate_with_ollama,
)


@observe(
    name="genai_request",
    as_type="chain",
)
def run_observable_request(
    question: str,
    *,
    user_id: str,
    session_id: str,
    feature: str,
) -> str:
    """
    Root observability trace.

    User/session metadata is propagated to
    all child observations.
    """

    with propagate_attributes(
        user_id=user_id,
        session_id=session_id,
        tags=[
            "module13",
            feature,
            "ollama",
        ],
        metadata={
            "environment": "local",
            "model_provider": "ollama",
            "feature": feature,
        },
    ):

        with langfuse.start_as_current_observation(
            as_type="span",
            name="prepare-request",
        ) as span:

            span.update(
                input={
                    "question": question
                }
            )

            processed_question = (
                question.strip()
            )

            span.update(
                output={
                    "processed_question": (
                        processed_question
                    )
                }
            )

        answer = generate_with_ollama(
            processed_question
        )

        return answer