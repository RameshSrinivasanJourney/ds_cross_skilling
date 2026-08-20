from crewai import Agent, Crew, LLM, Process, Task


ollama_llm = LLM(
    model="ollama/llama3.2:3b",
    base_url="http://localhost:11434",
    temperature=0.2,
)


def test_task_context():

    research_agent = Agent(
        role="Python Researcher",
        goal=(
            "Research Python list and tuple differences "
            "accurately."
        ),
        backstory=(
            "You are a Python developer who focuses on "
            "technical accuracy and useful examples."
        ),
        llm=ollama_llm,
        verbose=True,
    )

    writer_agent = Agent(
        role="Technical Writer",
        goal=(
            "Turn technical research into a clear "
            "beginner-friendly explanation."
        ),
        backstory=(
            "You are an experienced technical writer "
            "who explains software concepts clearly."
        ),
        llm=ollama_llm,
        verbose=True,
    )

    research_task = Task(
        description=(
            "Research the differences between Python "
            "lists and tuples. Cover mutability, syntax, "
            "ordering, and practical use cases."
        ),
        expected_output=(
            "Accurate research notes covering lists "
            "and tuples."
        ),
        agent=research_agent,
    )

    writing_task = Task(
        description=(
            "Using the research from the previous task, "
            "write a beginner-friendly explanation of "
            "Python lists versus tuples. Include one "
            "simple example of each."
        ),
        expected_output=(
            "A clear beginner-friendly explanation "
            "based on the research task."
        ),
        agent=writer_agent,
        context=[research_task],
    )

    crew = Crew(
        agents=[
            research_agent,
            writer_agent,
        ],
        tasks=[
            research_task,
            writing_task,
        ],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()

    print("\nFinal Result:")
    print(result)


if __name__ == "__main__":
    test_task_context()