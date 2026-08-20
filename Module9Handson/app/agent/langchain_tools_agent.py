from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from app.tools.calculator_tool import multiply


def create_langchain_tools_agent():

    model = ChatOllama(
        model="llama3.2:3b",
        temperature=0,
        base_url="http://localhost:11434",
    )

    return create_agent(
        model=model,
        tools=[multiply],
        system_prompt=(
            "You are a calculator assistant. "
            "Use the calculator tool whenever "
            "calculation is required."
        ),
    )