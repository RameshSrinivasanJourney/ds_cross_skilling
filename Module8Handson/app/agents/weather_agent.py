from crewai import Agent, LLM

from app.tools.weather_crew_tool import get_current_weather


ollama_llm = LLM(
    model="ollama/llama3.2:3b",
    base_url="http://localhost:11434",
    temperature=0.2,
)


def create_weather_agent() -> Agent:

    return Agent(
        role="Weather Assistant",
        goal=(
            "Provide accurate current weather information "
            "using the weather tool."
        ),
        backstory=(
            "You are a helpful weather assistant. "
            "When current weather information is needed, "
            "use the available weather tool instead of "
            "guessing."
        ),
        tools=[
            get_current_weather
        ],
        llm=ollama_llm,
        verbose=True,
    )