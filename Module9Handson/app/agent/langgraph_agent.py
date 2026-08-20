from typing import Annotated, TypedDict

from langchain_core.messages import BaseMessage
from langchain_ollama import ChatOllama
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

from app.tools.calculator_tool import add, multiply


class AgentState(TypedDict):
    """State carried through the agent graph."""

    messages: Annotated[
        list[BaseMessage],
        add_messages,
    ]


MODEL_NAME = "llama3.2:3b"

TOOLS = [
    multiply,
    add,
]


llm = ChatOllama(
    model=MODEL_NAME,
    temperature=0,
    base_url="http://localhost:11434",
).bind_tools(TOOLS)


def call_llm(
    state: AgentState,
) -> dict:
    """
    LLM node.

    Reads the current messages and produces
    the next AI message.
    """

    response = llm.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }


tool_node = ToolNode(
    tools=TOOLS
)


def build_agent_graph():

    graph = StateGraph(
        AgentState
    )

    # -------------------------------
    # Add nodes
    # -------------------------------

    graph.add_node(
        "call_llm",
        call_llm,
    )

    graph.add_node(
        "tool_node",
        tool_node,
    )

    # -------------------------------
    # Start → LLM
    # -------------------------------

    graph.add_edge(
        START,
        "call_llm",
    )

    # -------------------------------
    # LLM → Tool or END
    # -------------------------------

    graph.add_conditional_edges(
        "call_llm",
        tools_condition,
        {
            "tools": "tool_node",
            END: END,
        },
    )

    # -------------------------------
    # Tool → LLM
    # -------------------------------

    graph.add_edge(
        "tool_node",
        "call_llm",
    )

    return graph.compile()