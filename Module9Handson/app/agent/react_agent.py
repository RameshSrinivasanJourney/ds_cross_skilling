import json
import re

from ollama import chat

from app.agent.react_tool_registry import TOOLS


MODEL_NAME = "llama3.2:3b"

MAX_ITERATIONS = 5


SYSTEM_PROMPT = """
You are a ReAct-style calculation agent.

You MUST use the available tools to solve the user's request.

Available tools:

1. multiply
   Input:
   {"a": number, "b": number}

2. add
   Input:
   {"a": number, "b": number}

Rules:

1. Return only ONE action per response.
2. Perform exactly ONE tool call at a time.
3. Wait for the Observation before deciding the next action.
4. Never perform arithmetic yourself when a tool is available.
5. Never include mathematical expressions inside JSON.
6. Use numeric JSON values only.
7. When the task is complete, return:
   Final Answer: <answer>
"""

def _parse_action(response: str):
    """
    Extract the first observable Action and Action Input
    from the model response.
    """

    action_match = re.search(
        r"Action:\s*([a-zA-Z_][a-zA-Z0-9_]*)",
        response,
    )

    if not action_match:
        return None

    action_input_match = re.search(
        r"Action Input:\s*(\{.*?\})",
        response,
        re.DOTALL,
    )

    if not action_input_match:
        return None

    tool_name = action_match.group(1)

    try:
        arguments = json.loads(
            action_input_match.group(1)
        )
    except json.JSONDecodeError:
        return None

    return tool_name, arguments
def run_react_agent(
    user_question: str,
) -> str:
    """Run a ReAct-style agent loop."""

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": user_question,
        },
    ]

    for iteration in range(
        1,
        MAX_ITERATIONS + 1,
    ):

        print(
            f"\n--- ReAct Iteration "
            f"{iteration} ---"
        )

        response = chat(
            model=MODEL_NAME,
            messages=messages,
        )

        assistant_text = (
            response.message.content
        )

        print("\nAgent Decision:")
        print(assistant_text)

        # ---------------------------------------
        # Final answer?
        # ---------------------------------------

        final_match = re.search(
            r"Final Answer:\s*(.*)",
            assistant_text,
            re.DOTALL,
        )

        if final_match:

            return final_match.group(1).strip()

        # ---------------------------------------
        # Action?
        # ---------------------------------------

        action = _parse_action(
            assistant_text
        )

        if action is None:

            return (
                "Agent produced an invalid "
                "ReAct action."
            )

        tool_name, arguments = action

        print("\nAction:")
        print(tool_name)

        print("\nAction Input:")
        print(arguments)

        tool = TOOLS.get(tool_name)

        if tool is None:

            observation = (
                f"Unknown tool: {tool_name}"
            )

        else:

            try:

                result = tool(**arguments)

                observation = str(result)

            except Exception as exc:

                observation = (
                    f"Tool execution failed: {exc}"
                )

        print("\nObservation:")
        print(observation)

        messages.append(
            {
                "role": "assistant",
                "content": assistant_text,
            }
        )

        messages.append(
            {
                "role": "user",
                "content": (
                    "Observation: "
                    f"{observation}\n\n"
                    "Continue the ReAct process. "
                    "Return either another Action and "
                    "Action Input, or a Final Answer."
                ),
            }
        )

    return (
        "The agent stopped because the "
        "maximum iteration limit was reached."
    )