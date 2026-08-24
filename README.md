# Module 11 - Memory Systems

## Overview

Module 11 focuses on **Memory Systems for AI applications and agents**.

The module explains how an agent can maintain context during a conversation, persist information across sessions, retrieve relevant memories using vector search, maintain workflow state, and integrate memory into real-world applications.

The hands-on implementations use **Ollama with `llama3.2:3b`** wherever practical, together with local persistence and vector-search components.

---

# Learning Objectives

By the end of this module, you will understand:

* In-context / short-term memory
* External / long-term memory
* Episodic memory
* Semantic memory
* Procedural memory
* Conversation history management
* Last-N-turn buffers
* Conversation summarization
* Token-aware truncation
* Summary-buffer memory
* Embedding-based memory
* Vector-store memory retrieval
* Conversation-summary memory
* Memory consolidation
* Memory freshness
* Memory expiry
* Redis session state
* PostgreSQL structured memory
* SQLite persistence
* LangGraph checkpointers
* Memory context injection
* User-profile memory
* Project-context memory
* Mem0
* Zep

---

# Environment

```text
Python 3.13.15
Ollama
llama3.2:3b
```

The project is designed to run locally and avoid unnecessary paid API dependencies.

---

# Project Structure

```text
Module11Handson/
│
├── .venv/
│
├── app/
│   ├── __init__.py
│   │
│   ├── memory/
│   │   ├── __init__.py
│   │   ├── memory_manager.py
│   │   ├── short_term_memory.py
│   │   ├── vector_memory.py
│   │   ├── faiss_memory_store.py
│   │   ├── profile_memory.py
│   │   └── project_memory.py
│   │
│   ├── stores/
│   │   ├── __init__.py
│   │   ├── state_store.py
│   │   ├── sqlite_state_store.py
│   │   ├── redis_session_store.py
│   │   └── postgres_memory_store.py
│   │
│   ├── retrieval/
│   │   ├── __init__.py
│   │   ├── embedding_service.py
│   │   └── memory_context_builder.py
│   │
│   ├── consolidation/
│   │   ├── __init__.py
│   │   └── memory_consolidator.py
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   └── memory_enabled_agent.py
│   │
│   ├── workflows/
│   │   ├── __init__.py
│   │   └── checkpoint_demo.py
│   │
│   └── config/
│       └── __init__.py
│
├── tests/
│   ├── test_memory_types.py
│   ├── test_short_term_memory.py
│   ├── test_vector_memory.py
│   ├── test_external_state_stores.py
│   ├── test_langgraph_checkpoint.py
│   └── test_memory_in_practice.py
│
├── data/
│   └── memory_store/
│
├── .gitignore
├── README.md
├── requirements.txt
└── main.py
```

---

# Topic 1 - Types of Memory

## 1.1 In-Context / Short-Term Memory

Information currently available in the conversation context.

```text
Conversation
    ↓
Messages
    ↓
LLM Context
```

## 1.2 External / Long-Term Memory

Information stored outside the current context so that it can be retrieved later.

Examples include:

* SQLite
* PostgreSQL
* Redis
* Vector stores
* Memory frameworks

## 1.3 Episodic Memory

Stores events or experiences.

Example:

```text
User asked about Chennai weather.
User completed Module 10.
User started Module 11.
```

## 1.4 Semantic Memory

Stores facts and knowledge.

Example:

```text
preferred_city = Chennai
role = Software Architect
```

## 1.5 Procedural Memory

Stores knowledge about how to perform a task.

Example:

```text
Submit leave request:
1. Open employee portal.
2. Select Leave.
3. Choose leave type.
4. Enter dates.
5. Submit.
```

Test:

```powershell
python -m tests.test_memory_types
```

---

# Topic 2 - Short-Term Memory Management

## 2.1 Conversation History

Conversation history is maintained as a messages list.

```text
User
Assistant
User
Assistant
...
```

## 2.2 Last-N-Turn Window

Only the latest N conversation turns are retained.

This prevents unbounded growth of the context.

## 2.3 Summarization

Older messages can be compressed into a summary.

```text
Old Conversation
      ↓
Summary
      ↓
Recent Messages
```

## 2.4 Token-Aware Truncation

Messages can be selected according to an estimated token budget instead of a fixed number of messages.

## 2.5 Summary Buffer

A hybrid strategy combines:

```text
Older Conversation Summary
+
Recent Full Messages
```

This provides better context retention while controlling context size.

Test:

```powershell
python -m tests.test_short_term_memory
```

---

# Topic 3 - Long-Term Memory with Vector Stores

This topic uses embeddings and FAISS to store and retrieve semantically relevant memories.

## 3.1 User Facts as Embeddings

Example:

```text
"The user prefers Chennai."
        ↓
Embedding
        ↓
FAISS
```

## 3.2 Conversation Summaries

Past interactions can be summarized and stored as memory records.

## 3.3 Relevant Memory Retrieval

```text
User Query
    ↓
Query Embedding
    ↓
FAISS Search
    ↓
Top-K Memories
```

## 3.4 Memory Consolidation

Related memories can be grouped or merged into a cleaner representation.

## 3.5 Memory Expiry and Freshness

Memories can include:

```text
created_at
expires_at
freshness
importance
```

Expired memories are excluded or removed.

Test:

```powershell
python -m tests.test_vector_memory
```

---

# Topic 4 - External State Stores

## 4.1 Redis

Redis can be used for fast session-oriented state such as:

```text
session_id
current_task
current_step
recent_state
```

A Redis adapter is implemented in:

```text
app/stores/redis_session_store.py
```

A running Redis server is not required for the local hands-on.

## 4.2 PostgreSQL

PostgreSQL can be used for durable structured memory with fields such as:

```text
user_id
memory_type
content
created_at
updated_at
metadata
```

A PostgreSQL adapter is implemented in:

```text
app/stores/postgres_memory_store.py
```

A PostgreSQL server is not required for the local hands-on.

## 4.3 SQLite

SQLite provides local persistence without requiring a database server.

Implemented in:

```text
app/stores/sqlite_state_store.py
```

## 4.4 LangGraph Checkpointers

LangGraph checkpoints preserve graph/thread state and support:

* Conversation persistence
* Workflow recovery
* Interrupt/resume
* State inspection
* Thread-based execution

The hands-on uses a local SQLite-backed checkpointer.

Tests:

```powershell
python -m tests.test_external_state_stores
```

```powershell
python -m tests.test_langgraph_checkpoint
```

---

# Topic 5 - Memory in Practice

## 5.1 Injecting Retrieved Memories into the System Prompt

The flow is:

```text
User Query
    ↓
Memory Retrieval
    ↓
Relevant Memories
    ↓
System Prompt
    ↓
Ollama
    ↓
Answer
```

## 5.2 User Profile Memory

Persistent user information can be stored and retrieved across logical sessions.

Examples:

```text
preferred_city
role
preferences
```

## 5.3 Project Context Memory

Project-specific information can also be stored.

Example:

```text
Current Module = Module 11
Previous Module = Module 10
Completed Work = FAISS + LangGraph checkpointing
```

User profile and project context are different concepts:

```text
User Profile
→ Who is the user?

Project Context
→ What is happening in the current project?
```

## 5.4 Mem0

Mem0 is an open-source memory layer that provides higher-level memory management, including memory extraction, storage, retrieval, and updates.

Conceptually:

```text
Conversation
    ↓
Mem0
    ↓
Useful Memories
    ↓
Memory Retrieval
    ↓
LLM
```

The local implementation in this module demonstrates the underlying concepts without requiring Mem0 as a mandatory dependency.

## 5.5 Zep

Zep is an LLM-oriented memory platform that provides user/session memory and context construction.

Conceptually:

```text
Conversation
    ↓
Zep Memory
    ↓
Relevant Context
    ↓
System Prompt
    ↓
LLM
```

Zep is discussed as an external memory platform and is not required for the local hands-on.

Test:

```powershell
python -m tests.test_memory_in_practice
```

---

# Memory Architecture

The complete Module 11 architecture is:

```text
                         MEMORY SYSTEM
                              |
        +---------------------+---------------------+
        |                     |                     |
   Short-Term            Long-Term              State
        |                     |                     |
 Messages / Buffer       Vector Store         SQLite / Redis /
 Summary / Tokens        Embeddings           PostgreSQL /
        |                     |                Checkpoints
        +---------------------+---------------------+
                              |
                       Memory Retrieval
                              |
                       Context Injection
                              |
                             LLM
```

---

# Memory Lifecycle

A mature memory system can follow:

```text
Conversation
    ↓
Extract Candidate Memory
    ↓
Classify
    ↓
Store
    ↓
Consolidate
    ↓
Retrieve When Relevant
    ↓
Inject Into Context
    ↓
Refresh / Expire
```

---

# RAG Memory vs Agent Memory

Traditional RAG:

```text
Documents
    ↓
Embeddings
    ↓
Vector Store
    ↓
Relevant Documents
```

Agent Memory:

```text
Past Interactions / User Facts
    ↓
Embeddings
    ↓
Memory Store
    ↓
Relevant Memories
```

The retrieval technology may be similar, but the **data lifecycle and purpose are different**.

---

# Topic Tests

Run the following tests individually:

```powershell
python -m tests.test_memory_types
```

```powershell
python -m tests.test_short_term_memory
```

```powershell
python -m tests.test_vector_memory
```

```powershell
python -m tests.test_external_state_stores
```

```powershell
python -m tests.test_langgraph_checkpoint
```

```powershell
python -m tests.test_memory_in_practice
```

---

# Module 11 Final Checklist

```text
1. Types of Memory
   Hands-on 1 ✅

2. Short-Term Memory Management
   Hands-on 2 ✅

3. Long-Term Memory with Vector Stores
   Hands-on 3 ✅

4. External State Stores
   Hands-on 4 ✅

5. Memory in Practice
   Hands-on 5 ✅
```

---

# Key Interview Questions

## What is short-term memory?

The information currently available in the model's conversation/context window.

## What is long-term memory?

Information persisted outside the current context and retrieved when needed.

## What is episodic memory?

Memory of events or specific interactions.

## What is semantic memory?

Memory of facts and knowledge.

## What is procedural memory?

Memory of how to perform tasks or workflows.

## Why use a summary buffer?

It preserves important older context while keeping recent messages in full detail.

## Why use vector stores for memory?

They allow semantically related memories to be retrieved even when the user's query does not use the same words as the stored memory.

## What is memory consolidation?

Combining related or duplicated memories into cleaner long-term representations.

## Why does memory need expiry?

Some memories become stale and should no longer influence agent behavior.

## SQLite vs Redis vs PostgreSQL?

SQLite is ideal for local persistence, Redis for fast session-oriented state, and PostgreSQL for durable structured data and relational querying.

## What does a LangGraph checkpointer do?

It persists graph/thread state so workflows can maintain state, recover, inspect history, and resume interrupted execution.
