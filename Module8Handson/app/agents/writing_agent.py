from crewai import Agent, LLM


ollama_llm = LLM(
    model="ollama/llama3.2:3b",
    base_url="http://localhost:11434",
    temperature=0.2,
)


def create_writing_agent() -> Agent:
    return Agent(
        role="Technical Writer",
        goal=(
            "Transform technical research into a clear, "
            "concise explanation for software developers."
        ),
        backstory=(
            "You are an experienced technical writer who "
            "turns complex technical information into "
            "easy-to-understand content."
        ),
        llm=ollama_llm,
        verbose=True,
    )