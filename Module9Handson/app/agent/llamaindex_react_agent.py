from llama_index.core.agent.workflow import ReActAgent
from llama_index.llms.ollama import Ollama

from app.tools.calculator_tool import add, multiply


def create_llamaindex_react_agent() -> ReActAgent:
    """Create a LlamaIndex ReAct agent."""

    llm = Ollama(
        model="llama3.2:3b",
        base_url="http://localhost:11434",
        request_timeout=120.0,
    )

    agent = ReActAgent(
        name="calculator_react_agent",
        description=(
            "A ReAct agent that solves calculations "
            "using calculator tools."
        ),
        system_prompt=(
            "You are a calculation assistant.\n"
            "Use the available tools for arithmetic.\n"
            "For multi-step calculations, use the result "
            "of one operation as the input to the next.\n"
            "Do not invent tool results."
        ),
        tools=[
            multiply,
            add,
        ],
        llm=llm,
        verbose=True,
    )

    return agent