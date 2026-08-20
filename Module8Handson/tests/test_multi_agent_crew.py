from app.crews.research_writing_crew import (
    create_research_writing_crew,
)


def test_multi_agent_crew():

    crew = create_research_writing_crew()

    result = crew.kickoff()

    print("\nFinal Result:")
    print(result)


if __name__ == "__main__":
    test_multi_agent_crew()