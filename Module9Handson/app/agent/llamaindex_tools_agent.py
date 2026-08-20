from llama_index.core.agent.workflow import (
    FunctionAgent,
)
from llama_index.llms.ollama import Ollama

from app.tools.calculator_tool import multiply


def create_llamaindex_tools_agent():

    llm = Ollama(
        model="llama3.2:3b",
        base_url="http://localhost:11434",
        request_timeout=120.0,
    )

    return FunctionAgent(
        name="calculator_agent",
        description=(
            "An agent that performs calculations "
            "using calculator tools."
        ),
        system_prompt=(
            "You are a calculator assistant. "
            "Use the available calculator tool "
            "when a calculation is required."
        ),
        tools=[multiply],
        llm=llm,
    )