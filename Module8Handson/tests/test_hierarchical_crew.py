from crewai import Task

from app.crews.hierarchical_crew import (
    create_hierarchical_crew,
)


def test_hierarchical_crew():

    crew = create_hierarchical_crew()

    task = Task(
        description=(
            "An employee asks: "
            "'How should I handle a question about "
            "company policy? Provide a practical answer "
            "and explain which type of specialist should "
            "be consulted when necessary.'"
        ),
        expected_output=(
            "A clear and practical response explaining "
            "how an employee should approach policy "
            "questions."
        ),
    )

    crew.tasks = [task]

    result = crew.kickoff()

    print("\nFinal Result:")
    print(result)


if __name__ == "__main__":
    test_hierarchical_crew()