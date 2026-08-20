from crewai import Agent, LLM, Task, Crew, Process


ollama_llm = LLM(
    model="ollama/llama3.2:3b",
    base_url="http://localhost:11434",
    temperature=0.2,
)


def run_agent(
    role: str,
    goal: str,
    backstory: str,
):

    agent = Agent(
        role=role,
        goal=goal,
        backstory=backstory,
        llm=ollama_llm,
        verbose=True,
    )

    task = Task(
        description=(
            "Explain the difference between "
            "lists and tuples in Python."
        ),
        expected_output=(
            "A concise beginner-friendly explanation "
            "with one example of each."
        ),
        agent=agent,
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        process=Process.sequential,
        verbose=True,
    )

    return crew.kickoff()


def test_agent_persona():

    print("\n========== PYTHON TUTOR ==========")

    result = run_agent(
        role="Python Tutor",
        goal="Teach Python to beginners.",
        backstory=(
            "You are a patient Python instructor "
            "who explains concepts using simple examples."
        ),
    )

    print("\nTutor Result:")
    print(result)

    print("\n========== SENIOR PYTHON ARCHITECT ==========")

    result = run_agent(
        role="Senior Python Architect",
        goal=(
            "Explain Python concepts from a production "
            "software architecture perspective."
        ),
        backstory=(
            "You are a senior Python architect with years "
            "of experience designing scalable applications."
        ),
    )

    print("\nArchitect Result:")
    print(result)


if __name__ == "__main__":
    test_agent_persona()