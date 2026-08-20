from app.crews.first_crew import create_first_crew


def test_first_crew():

    crew = create_first_crew()

    result = crew.kickoff()

    print("\nFinal Result:")
    print(result)


if __name__ == "__main__":
    test_first_crew()