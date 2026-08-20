from app.crews.weather_crew import create_weather_crew


def test_weather_tool_crew():

    crew = create_weather_crew()

    result = crew.kickoff()

    print("\nFinal Result:")
    print(result)


if __name__ == "__main__":
    test_weather_tool_crew()