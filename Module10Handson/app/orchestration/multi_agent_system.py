from app.agents.analyst_agent import (
    analyst_agent,
)
from app.agents.researcher_agent import (
    research_agent,
)
from app.agents.reviewer_agent import (
    reviewer_agent,
)
from app.agents.writer_agent import (
    writer_agent,
)


def run_multi_agent_system(
    question: str,
) -> dict:

    print("\n=== Research Agent ===")

    research = research_agent(
        question
    )

    print(research)

    print("\n=== Analysis Agent ===")

    analysis = analyst_agent(
        question,
        research,
    )

    print(analysis)

    print("\n=== Writer Agent ===")

    draft = writer_agent(
        question,
        analysis,
    )

    print(draft)

    print("\n=== Reviewer Agent ===")

    review = reviewer_agent(
        question,
        draft,
    )

    print(review)

    return {
        "question": question,
        "research": research,
        "analysis": analysis,
        "draft": draft,
        "review": review,
    }