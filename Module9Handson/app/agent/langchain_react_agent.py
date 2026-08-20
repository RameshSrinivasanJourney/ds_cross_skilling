from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from app.tools.calculator_tool import add, multiply


def create_langchain_agent():

    model = ChatOllama(
        model="llama3.2:3b",
        temperature=0,
        base_url="http://localhost:11434",
    )

    return create_agent(
        model=model,
        tools=[multiply, add],
        system_prompt=(
            "You are a calculation agent.\n"
            "You MUST use the available tools.\n"
            "For multi-step calculations, execute each "
            "operation separately and use the previous "
            "tool result as the input to the next operation.\n"
            "Do not perform arithmetic mentally when a "
            "calculator tool is available."
        ),
    )