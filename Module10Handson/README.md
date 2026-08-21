# Module 10 - Multi-Agent Systems

## Overview

Module 10 focuses on **Multi-Agent Systems** and builds on the single-agent architecture, tool calling, LangGraph, memory, reliability, and evaluation concepts introduced in Module 9.

The module demonstrates how multiple specialized agents can collaborate to solve complex tasks.

The hands-on implementations use a local **Ollama `llama3.2:3b`** model wherever practical, avoiding unnecessary dependency on paid cloud APIs.

---

# Learning Objectives

By the end of this module, you will understand:

* Why multi-agent systems can be useful compared with single agents
* Task specialization
* Parallel agent execution
* Verification and self-correction
* Multi-agent scalability
* Planner agents
* Executor agents
* Critic / Reviewer agents
* Researcher agents
* Writer / Generator agents
* Orchestrator / Supervisor agents
* Hub-and-spoke communication
* Peer-to-peer communication
* Hierarchical communication
* Blackboard / shared-state communication
* Pipeline communication
* Task decomposition
* Task dependency graphs
* Parallel vs sequential execution
* Result merging
* Retry strategies
* Tool and agent timeouts
* Fallback agents
* Output guardrails
* Maximum iteration limits
* Multi-agent logging
* Human approval
* LangGraph interrupts
* Plan review before execution
* Approve / Reject / Edit decisions
* Audit trails

---

# Environment

```text
Python 3.13.15
Ollama
llama3.2:3b
```

The project is designed to run locally using Ollama.

---

# Project Structure

```text
Module10Handson/
│
├── .venv/
│
├── app/
│   ├── __init__.py
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── llm.py
│   │   ├── planner_agent.py
│   │   ├── researcher_agent.py
│   │   ├── analyst_agent.py
│   │   ├── executor_agent.py
│   │   ├── writer_agent.py
│   │   ├── reviewer_agent.py
│   │   └── supervisor_agent.py
│   │
│   ├── communication/
│   │   ├── __init__.py
│   │   ├── hub_spoke.py
│   │   ├── peer_to_peer.py
│   │   ├── hierarchical.py
│   │   ├── blackboard.py
│   │   └── pipeline.py
│   │
│   ├── orchestration/
│   │   ├── __init__.py
│   │   ├── multi_agent_system.py
│   │   ├── role_based_system.py
│   │   ├── parallel_research.py
│   │   ├── task_decomposer.py
│   │   ├── dependency_graph.py
│   │   └── task_executor.py
│   │
│   ├── reliability/
│   │   ├── __init__.py
│   │   ├── retry.py
│   │   ├── timeout.py
│   │   ├── guardrails.py
│   │   ├── fallback.py
│   │   └── reliable_multi_agent.py
│   │
│   ├── workflows/
│   │   ├── __init__.py
│   │   ├── audit.py
│   │   └── human_approval_workflow.py
│   │
│   ├── memory/
│   │   ├── __init__.py
│   │
│   └── config/
│       ├── __init__.py
│
├── tests/
│   ├── test_multi_agent_core.py
│   ├── test_parallel_multi_agent.py
│   ├── test_agent_roles.py
│   ├── test_communication_patterns.py
│   ├── test_task_decomposition.py
│   ├── test_multi_agent_reliability.py
│   └── test_human_in_the_loop.py
│
├── data/
│
├── .gitignore
├── README.md
├── requirements.txt
└── main.py
```

---

# Topic 1 - Core Concepts

## 1.1 Why Multi-Agent over Single-Agent

A single agent may have to perform many responsibilities:

```text
Single Agent
├── Research
├── Analysis
├── Execution
├── Writing
└── Review
```

A multi-agent architecture separates responsibilities:

```text
Supervisor
├── Researcher
├── Analyst
├── Executor
├── Writer
└── Reviewer
```

This can improve specialization, maintainability, and extensibility.

## 1.2 Task Specialization

Each agent has a focused responsibility.

```text
Researcher → Find information

Analyst → Analyze findings

Executor → Perform work

Writer → Generate response

Reviewer → Validate result

Supervisor → Coordinate agents
```

## 1.3 Parallel Execution

Independent tasks can execute concurrently.

Example:

```text
                 Goal
          +-------+-------+
          |       |       |
          ↓       ↓       ↓
       Policy  Eligibility Process
       Research Research   Research
          |       |       |
          +-------+-------+
                  ↓
               Analysis
```

## 1.4 Verification and Self-Correction

A reviewer can validate the output of another agent.

```text
Writer
  ↓
Draft
  ↓
Reviewer
  ↓
PASS / REVISE
```

## 1.5 Scalability

As responsibilities grow, specialized agents can be added instead of continuously expanding one large agent.

Multi-agent architecture can improve organization, but it also introduces additional coordination, latency, and failure points.

---

# Hands-on 1 - Multi-Agent Core Concepts

Implemented:

```text
Researcher
    ↓
Analyst
    ↓
Writer
    ↓
Reviewer
```

Parallel research was also demonstrated.

Tests:

```powershell
python -m tests.test_multi_agent_core
```

```powershell
python -m tests.test_parallel_multi_agent
```

---

# Topic 2 - Agent Roles

The module implements six specialized roles.

## Planner

Determines what work needs to be performed.

```text
Goal → Plan
```

## Executor

Performs the assigned work.

```text
Plan → Execution
```

## Critic / Reviewer

Validates the result.

```text
Draft → Review
```

## Researcher

Gathers relevant information.

```text
Question → Research
```

## Writer / Generator

Converts results into a user-facing response.

```text
Results → Response
```

## Supervisor / Orchestrator

Coordinates the specialist agents.

```text
Supervisor
    ↓
Planner
    ↓
Researcher / Executor
    ↓
Writer
    ↓
Reviewer
```

Test:

```powershell
python -m tests.test_agent_roles
```

---

# Topic 3 - Communication Patterns

Five communication patterns were implemented.

## Hub-and-Spoke

```text
          Supervisor
         /    |    \
        ↓     ↓     ↓
    Research Writer Reviewer
```

## Peer-to-Peer

```text
Researcher → Analyst → Writer
```

## Hierarchical

```text
          Manager
         /   |   \
        A    B    C
```

## Blackboard / Shared State

```text
Agent A ─┐
Agent B ─┼→ Shared State ← Agent C
Agent D ─┘
```

## Pipeline

```text
Researcher
    ↓
Analyst
    ↓
Writer
    ↓
Reviewer
```

Test:

```powershell
python -m tests.test_communication_patterns
```

---

# Topic 4 - Task Decomposition

Complex goals can be decomposed into smaller tasks.

Example:

```text
Employee Leave Report
        |
   +----+----+----+
   |         |    |
   ↓         ↓    ↓
Policy   Eligibility Process
Research  Research  Research
   |         |    |
   +---------+----+
             ↓
          Analysis
             ↓
           Report
```

## Dependency Graph

Each task declares dependencies.

Independent research tasks can run in parallel.

Dependent tasks wait for their prerequisites.

## Result Merging

Multiple specialist outputs are combined before the analysis and reporting stages.

Test:

```powershell
python -m tests.test_task_decomposition
```

---

# Topic 5 - Reliability Patterns

The multi-agent reliability layer implements:

## Retry

```text
Failure
  ↓
Retry
  ↓
Retry
  ↓
Success / Fallback
```

## Timeout

Prevents slow operations from blocking the workflow indefinitely.

## Fallback Agent

```text
Primary Agent
     ↓
   Failure
     ↓
Fallback Agent
```

## Guardrails

Agent outputs are validated before being passed forward.

## Maximum Iterations

A hard limit prevents runaway loops.

## Logging

Observable workflow events are logged for debugging and monitoring.

Architecture:

```text
Agent
 ↓
Retry
 ↓
Timeout
 ↓
Guardrail
 ↓
Fallback
 ↓
Next Agent
```

Test:

```powershell
python -m tests.test_multi_agent_reliability
```

---

# Topic 6 - Human-in-the-Loop

Human approval is useful before high-impact or sensitive actions.

The hands-on demonstrates:

```text
User
 ↓
Planner
 ↓
Proposed Plan
 ↓
Human Review
 ├── Approve
 ├── Edit
 └── Reject
```

## LangGraph Interrupt

The workflow uses an interrupt to pause execution while waiting for human input.

```text
Planner
 ↓
interrupt
 ↓
Human
 ↓
Resume
```

## Audit Trail

Human decisions are recorded in:

```text
data/human_approval_audit.jsonl
```

The audit history records events such as:

```text
plan_created
human_review_requested
human_decision
execution_started
execution_completed
execution_skipped
```

Test:

```powershell
python -m tests.test_human_in_the_loop
```

---

# Module 10 Architecture

The combined multi-agent architecture is:

```text
                         User
                           |
                           v
                      Supervisor
                           |
                           v
                        Planner
                           |
              +------------+------------+
              |            |            |
              v            v            v
         Researcher     Executor      Analyst
              |            |            |
              +------------+------------+
                           |
                           v
                         Writer
                           |
                           v
                        Reviewer
                           |
                           v
                    Guardrail Check
                           |
                           v
                    Human Approval
                           |
                 +---------+---------+
                 |                   |
              Approve              Reject
                 |                   |
                 v                   v
              Execute               Stop
```

Communication can use:

```text
Hub-and-Spoke
Peer-to-Peer
Hierarchical
Blackboard
Pipeline
```

Task execution can use:

```text
Sequential
Parallel
Dependency-driven
```

Reliability can use:

```text
Retry
Timeout
Fallback
Guardrails
Max Iterations
Logging
```

Human oversight can use:

```text
Approve
Edit
Reject
Interrupt / Resume
Audit Trail
```

---

# Module 10 Final Checklist

```text
1. Core Concepts
   Hands-on 1 ✅

2. Agent Roles
   Hands-on 2 ✅

3. Communication Patterns
   Hands-on 3 ✅

4. Task Decomposition
   Hands-on 4 ✅

5. Reliability Patterns
   Hands-on 5 ✅

6. Human-in-the-Loop
   Hands-on 6 ✅
```

---

# Key Interview Questions

## Why use multiple agents?

Multiple agents allow specialization, parallel execution, independent verification, and clearer separation of responsibilities.

## When should you not use multiple agents?

When a single agent or deterministic workflow can solve the task reliably. Multi-agent systems add orchestration complexity and latency.

## What is hub-and-spoke?

A central coordinator communicates with specialist agents.

## What is peer-to-peer?

Agents communicate directly with other agents without relying on a single central coordinator.

## What is a blackboard architecture?

Agents communicate indirectly through shared state.

## What is task decomposition?

Breaking a complex goal into smaller tasks and defining the dependencies between them.

## What is a fallback agent?

A secondary agent used when the primary agent fails or cannot complete the assigned task.

## Why are guardrails important?

They prevent invalid or unsafe agent outputs from propagating to downstream agents or actions.

## Why is human-in-the-loop important?

Human approval is useful for high-impact, sensitive, irreversible, or uncertain decisions.

## What does an audit trail provide?

A historical record of agent actions, human decisions, and workflow events for debugging, compliance, and accountability.
