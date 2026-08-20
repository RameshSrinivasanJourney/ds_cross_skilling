# Module 9 - Single Agent Systems

## Overview

Module 9 focuses on **Single Agent Systems** and builds on the function calling, tool use, orchestration, and CrewAI concepts learned in Modules 7 and 8.

The module starts with a minimal agent implemented from scratch and progressively introduces:

* Agent architecture
* ReAct
* Tool-calling agents
* LangGraph
* Memory
* Reliability
* Evaluation

The hands-on approach uses a local **Ollama `llama3.2:3b`** model wherever possible, avoiding dependency on paid cloud APIs.

---

# Learning Objectives

By the end of this module, you will understand:

* What an AI agent is
* Agent vs simple LLM call vs chain
* Perceive → Think → Act → Observe
* When to use agents vs fixed pipelines
* Limitations of single agents
* Agent architecture
* LLM as the agent brain
* Agent tools
* Tool registry
* System prompt design
* Scratchpad
* Stop conditions
* ReAct
* ReAct implementation from scratch
* LangChain agents
* LlamaIndex agents
* Function/tool-calling agents
* LangGraph single-agent architecture
* Graph state
* LLM nodes
* Tool nodes
* Conditional edges
* Short-term memory
* Long-term memory
* Agent state
* Tool-result injection
* Error handling
* Retry and fallback concepts
* Iteration limits
* Tool timeouts
* Agent logging
* Agent evaluation
* Task completion rate
* Trajectory evaluation
* Step efficiency
* Human trace review

---

# Environment

```text
Python 3.13.15
Ollama
llama3.2:3b
```

The project uses a local Ollama model for most hands-on exercises.

---

# Project Structure

```text
Module9Handson/
│
├── .venv/
│
├── app/
│   ├── __init__.py
│   │
│   ├── agent/
│   │   ├── basic_agent.py
│   │   ├── agent_architecture.py
│   │   ├── executor.py
│   │   ├── evaluation_agent.py
│   │   ├── langchain_react_agent.py
│   │   ├── langchain_tools_agent.py
│   │   ├── langgraph_agent.py
│   │   ├── llamaindex_react_agent.py
│   │   ├── llamaindex_tools_agent.py
│   │   ├── memory_agent.py
│   │   ├── ollama_tools_agent.py
│   │   ├── react_agent.py
│   │   ├── reliable_agent.py
│   │   └── tool_registry.py
│   │
│   ├── config/
│   │   └── logging_config.py
│   │
│   ├── evaluation/
│   │   ├── agent_evaluator.py
│   │   └── agent_trace.py
│   │
│   ├── memory/
│   │   └── long_term_memory.py
│   │
│   └── tools/
│       ├── calculator_tool.py
│       ├── reliability_test_tools.py
│       ├── structured_calculator_tool.py
│       └── weather_tool.py
│
├── tests/
│   ├── test_agent_architecture.py
│   ├── test_agent_evaluation.py
│   ├── test_agent_evaluation_batch.py
│   ├── test_agent_memory.py
│   ├── test_agent_reliability.py
│   ├── test_basic_agent.py
│   ├── test_langchain_react_agent.py
│   ├── test_langchain_tools_agent.py
│   ├── test_langgraph_agent.py
│   ├── test_llamaindex_react_agent.py
│   ├── test_llamaindex_tools_agent.py
│   ├── test_ollama_tools_agent.py
│   ├── test_react_agent.py
│   └── test_structured_tool_output.py
│
├── data/
│   └── evaluation_cases.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── main.py
```

---

# Topic 1 - Core Concepts

## 1.1 What is an AI Agent

An AI agent is an LLM-driven system that can decide what action to take, execute actions through tools, observe the results, and continue until the task is complete.

Basic loop:

```text
User
 ↓
Agent
 ↓
LLM Decision
 ↓
Tool / Action
 ↓
Observation
 ↓
LLM Decision
 ↓
Final Answer
```

## 1.2 Agent vs Simple LLM Call vs Chain

### Simple LLM Call

```text
User
 ↓
LLM
 ↓
Answer
```

### Chain

```text
Input
 ↓
Step 1
 ↓
Step 2
 ↓
Step 3
```

### Agent

```text
User
 ↓
Agent
 ↓
Dynamic Decision
 ├── Tool A
 ├── Tool B
 └── Final Answer
```

Key distinction:

```text
LLM Call = Generate

Chain = Fixed workflow

Agent = Dynamic decision and action loop
```

## 1.3 Agent Loop

```text
Perceive
 ↓
Think
 ↓
Act
 ↓
Observe
 ↓
Think
 ↓
Act / Final
```

## 1.4 Agent vs Fixed Pipeline

Use a fixed pipeline when the execution path is known.

Use an agent when the next step depends on the current state or result.

## 1.5 Single Agent Limitations

Single agents can have:

* Reliability problems
* Incorrect tool selection
* Incorrect tool arguments
* Higher latency
* Higher token usage
* Higher compute or API cost
* Infinite-loop risk

---

# Hands-on 1 - Basic Single Agent

Implemented:

```text
User
 ↓
Ollama
 ↓
get_weather
 ↓
Tool Result
 ↓
Ollama
 ↓
Final Answer
```

Test:

```powershell
python -m tests.test_basic_agent
```

---

# Topic 2 - Agent Architecture

## 2.1 Agent Components

A practical agent contains:

```text
LLM Brain
Tools
Memory
Executor
State
```

## 2.2 System Prompt

The system prompt defines:

* Agent role
* Behavior
* Tool usage rules
* Boundaries
* Stop conditions

## 2.3 Tool Registry

A tool registry maps tool names to executable Python functions.

```text
Tool Name
 ↓
Tool Registry
 ↓
Python Function
```

## 2.4 Scratchpad

The scratchpad contains the observable execution context:

```text
User Message
 ↓
Assistant Tool Call
 ↓
Tool Result
 ↓
Assistant Response
```

## 2.5 Stop Conditions

The basic stop condition is:

```text
No more tool calls
 ↓
Final Answer
```

A maximum iteration limit provides an additional safety boundary.

---

# Hands-on 2 - Structured Agent Architecture

Implemented:

```text
SingleAgent
├── LLM
├── System Prompt
├── Tool Registry
├── Executor
├── Scratchpad
└── Stop Condition
```

Test:

```powershell
python -m tests.test_agent_architecture
```

---

# Topic 3 - ReAct Agent Pattern

## 3.1 Reasoning and Acting

ReAct combines reasoning/decision-making with action execution.

Conceptually:

```text
Decision
 ↓
Action
 ↓
Observation
 ↓
Decision
```

## 3.2 Thought → Action → Observation

The classic ReAct pattern is:

```text
Thought
 ↓
Action
 ↓
Observation
```

For observable application traces we record:

```text
Decision
Action
Observation
```

without exposing private chain-of-thought.

## 3.3 ReAct from Scratch

Implemented manually using:

* LLM
* Action parser
* Tool registry
* Tool executor
* Observation injection
* Iteration loop
* Stop condition

Test:

```powershell
python -m tests.test_react_agent
```

## 3.4 ReAct with LangChain

The current LangChain agent API uses `create_agent()` for the modern agent runtime.

Test:

```powershell
python -m tests.test_langchain_react_agent
```

## 3.5 ReAct with LlamaIndex

Implemented using LlamaIndex's workflow-based `ReActAgent`.

Test:

```powershell
python -m tests.test_llamaindex_react_agent
```

---

# Topic 4 - OpenAI Tools Agent Pattern

The syllabus introduces the OpenAI-style function/tool-calling agent pattern.

To avoid API cost, this hands-on uses **Ollama** to demonstrate the same architecture locally.

## 4.1 Function Calling

```text
User
 ↓
LLM
 ↓
Structured Tool Call
 ↓
Tool Executor
 ↓
Tool Result
 ↓
LLM
 ↓
Final Answer
```

## 4.2 LangChain Tool Agent

The current LangChain API uses `create_agent()` for the modern implementation.

Test:

```powershell
python -m tests.test_langchain_tools_agent
```

## 4.3 LlamaIndex Function Agent

The current LlamaIndex equivalent for native function-calling models is `FunctionAgent`.

Test:

```powershell
python -m tests.test_llamaindex_tools_agent
```

## 4.4 Structured Tool Outputs

Structured outputs provide predictable data for downstream agent decisions.

Example:

```text
operation
a
b
result
```

Test:

```powershell
python -m tests.test_structured_tool_output
```

---

# Topic 5 - LangGraph Single Agent

LangGraph models an agent explicitly as a graph.

## 5.1 Agent Graph

```text
START
 ↓
LLM Node
 ↓
Tool Required?
 ├── Yes → Tool Node → LLM
 └── No  → END
```

## 5.2 State

The graph carries message state between nodes.

## 5.3 LLM Node

The LLM node decides whether a tool is required.

## 5.4 Tool Node

The tool node executes the requested function.

## 5.5 Conditional Edge

The conditional edge chooses:

```text
Tool
or
END
```

## 5.6 Compile and Run

The graph is compiled into an executable agent.

Test:

```powershell
python -m tests.test_langgraph_agent
```

---

# Topic 6 - Agent Memory

## 6.1 Short-Term Memory

Current conversation messages form short-term memory.

## 6.2 Tool Results in Context

Tool results are inserted back into the message context.

## 6.3 Agent State

Current execution state is carried through agent steps.

## 6.4 Long-Term Memory

A local SQLite store persists information across agent instances.

Architecture:

```text
Agent
 ↓
Memory Layer
 ↓
SQLite
```

Test:

```powershell
python -m tests.test_agent_memory
```

---

# Topic 7 - Error Handling and Reliability

## 7.1 Maximum Iterations

Prevents an agent from running forever.

## 7.2 Tool Failures

Tool exceptions are converted into structured failure results.

## 7.3 Invalid Tool Calls

Unknown tools are rejected instead of executed.

## 7.4 Logging

Observable execution steps are written to a log.

## 7.5 Timeouts

Individual tools have a maximum execution time.

Reliability architecture:

```text
Agent
 ↓
Tool Request
 ↓
Validation
 ↓
Timeout / Exception Handling
 ↓
Structured Result
 ↓
Agent
```

Test:

```powershell
python -m tests.test_agent_reliability
```

---

# Topic 8 - Agent Evaluation

## 8.1 Task Completion Rate

Measures how many tasks completed successfully.

```text
Completion Rate =
Successful Tasks / Total Tasks
```

## 8.2 Trajectory Evaluation

Checks whether the correct tools were selected and executed in the expected order.

Example:

```text
Expected:
get_weather

Actual:
get_weather
```

## 8.3 Step Efficiency

Measures how efficiently the agent reached the result.

```text
Efficiency =
Expected Steps / Actual Steps
```

## 8.4 Human Trace Review

An agent trace records:

```text
Question
 ↓
Agent Step
 ↓
Tool
 ↓
Arguments
 ↓
Result
 ↓
Final Answer
```

The trace can be reviewed manually or integrated with evaluation/observability systems such as LangSmith.

Tests:

```powershell
python -m tests.test_agent_evaluation
```

```powershell
python -m tests.test_agent_evaluation_batch
```

---

# Module 9 Architecture

The complete learning progression is:

```text
Basic Agent
    ↓
Agent Architecture
    ↓
ReAct
    ↓
Tool-Calling Agent
    ↓
LangGraph Agent
    ↓
Memory
    ↓
Reliability
    ↓
Evaluation
```

Final conceptual architecture:

```text
                        Single Agent
                             |
          +------------------+------------------+
          |                  |                  |
          v                  v                  v
        LLM               Tools              Memory
          |                  |                  |
          +------------------+------------------+
                             |
                           State
                             |
                       Agent Executor
                             |
                    Reliability Controls
                             |
                       Execution Trace
                             |
                         Evaluation
```

---

# Key Interview Questions

## What is an AI agent?

An AI agent is an LLM-driven system that dynamically decides actions, uses tools, observes results, and continues until it reaches a stop condition.

## Agent vs chain?

A chain follows a predefined sequence. An agent dynamically determines the next step.

## What is ReAct?

ReAct is an agent pattern that interleaves reasoning/decision-making with actions and observations.

## What is a scratchpad?

The scratchpad is the working execution context that stores the messages, tool calls, and tool results needed across agent steps.

## Why is a stop condition necessary?

Without a stop condition an agent can execute unnecessary or infinite iterations.

## Why evaluate the trajectory?

A final answer can be correct even when the agent used the wrong tools, wrong arguments, or unnecessary steps.

## What is step efficiency?

Step efficiency measures how close the agent's execution was to the expected number of steps.

## Why is agent evaluation different from normal application testing?

Normal testing often validates the final result. Agent evaluation also needs to validate the **trajectory**, tool decisions, step count, and execution behavior.

---

# Module 9 Final Checklist

```text
1. Core Concepts
   Hands-on 1 ✅

2. Agent Architecture
   Hands-on 2 ✅

3. ReAct Agent Pattern
   Hands-on 3 ✅

4. OpenAI Tools Agent Pattern
   Hands-on 4 ✅

5. LangGraph Single Agent
   Hands-on 5 ✅

6. Agent Memory
   Hands-on 6 ✅

7. Error Handling and Reliability
   Hands-on 7 ✅

8. Agent Evaluation
   Hands-on 8 ✅
```

**Module 9 — Single Agent Systems complete.**
