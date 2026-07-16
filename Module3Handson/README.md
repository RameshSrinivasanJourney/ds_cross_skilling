# Module 3 - Prompt Engineering

## Overview

This project extends the AI Chat Application developed in Module 2 by implementing Prompt Engineering techniques used in production Generative AI applications.

The application demonstrates how different prompting strategies influence Large Language Models (LLMs) while following a clean, modular, and production-ready FastAPI architecture.

---

## Project Architecture

```
Module3Handson
│
├── app
│   ├── api
│   ├── core
│   ├── models
│   ├── prompts
│   │   ├── versions
│   │   ├── prompt_builder.py
│   │   └── system_prompt.py
│   │
│   ├── security
│   │   ├── base_guard.py
│   │   ├── input_validator.py
│   │   ├── prompt_injection.py
│   │   ├── prompt_leak_guard.py
│   │   ├── jailbreak_guard.py
│   │   └── output_filter.py
│   │
│   ├── services
│   ├── utils
│   └── main.py
│
├── docs
├── requirements.txt
├── README.md
└── .env
```

---

## Folder Structure

| | Folder   | Purpose                                         |
| -------- | ----------------------------------------------- |
| api      | REST API endpoints                              |
| core     | Application configuration and AI settings       |
| models   | Request and Response models                     |
| prompts  | System prompts, Prompt Builder, Prompt Versions |
| security | Input validation and Prompt Security            |
| services | AI integration and Prompt Engineering logic     |
| utils    | Logger and Token Counter utilities              |
| docs     | Module documentation                            |


---

## Technologies Used

- Python 3.13
- FastAPI
- Uvicorn
- GitHub Models
- OpenAI SDK
- Pydantic
- tiktoken
- Logging
- Prompt Engineering
- Server Sent Events (SSE)
- JSON Schema
- XML
- Markdown
- Prompt Engineering
- Prompt Security

---

## Features Implemented

### AI Chat Application

- FastAPI REST API
- GitHub Models Integration
- AI Chat Service
- Conversation History
- Multi-turn Conversation
- Streaming Architecture
- Server Sent Events (SSE)
- AI Configuration
- Exception Handling
- Logging
- Token Counter

### Prompt Design Foundations

- System Prompt
- Prompt Builder Pattern
- Implicit Prompting
- Explicit Prompting
- Positive Instructions
- Negative Instructions

### Core Prompting & Reasoning Techniques

- Zero-shot Prompting
- One-shot Prompting
- Few-shot Prompting
- Instruction Hierarchy
- Chain-of-Thought (CoT)
- Zero-shot Chain-of-Thought (Zero-shot CoT)
- Few-shot Chain-of-Thought (Few-shot CoT)
- Tree-of-Thought (ToT)
- ReAct Prompting
- Meta Prompting

Structured Output Prompting
JSON Output Prompting
XML Output Prompting
Markdown Output Prompting
Few-shot Structured JSON
JSON Mode
Structured Output using JSON Schema
Tool Use Simulation

System Prompt Engineering
Production-ready System Prompt
Persona-based Prompting
Dynamic Context Injection
Out-of-Scope Handling
Prompt Versioning
Prompt A/B Testing

Prompt Security
Input Validation
Prompt Injection Protection
Prompt Leakage Prevention
Jailbreak Protection
Output Filtering
Centralized Security Service

---

## API Endpoints

### Chat APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /chat | AI Chat |
| POST | /chat/stream | Streaming Response |
| POST | /chat/streamSSE | Server Sent Events |
| POST | /chat/partial | Partial Response Simulation |

### Prompt Engineering APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /prompt/implicit | Implicit Prompting |
| POST | /prompt/explicit | Explicit Prompting |
| POST | /prompt/positive | Positive Instructions |
| POST | /prompt/negative | Negative Instructions |
| POST | /prompt/zeroshot | Zero-shot Prompting |
| POST | /prompt/oneshot | One-shot Prompting |
| POST | /prompt/fewshot | Few-shot Prompting |
| POST | /prompt/instruction-hierarchy | Instruction Hierarchy |
| POST | /prompt/chainofthought | Chain-of-Thought |
| POST | /prompt/zeroshot-cot | Zero-shot CoT |
| POST | /prompt/fewshot-cot | Few-shot CoT |
| POST | /prompt/treeofthought | Tree-of-Thought |
| POST | /prompt/react | ReAct Prompting |
| POST | /prompt/meta | Meta Prompting |
| POST   | /prompt/json         | JSON Output Prompting          |
| POST   | /prompt/xml          | XML Output Prompting           |
| POST   | /prompt/markdown     | Markdown Output Prompting      |
| POST   | /prompt/fewshot-json | Few-shot Structured Output     |
| POST   | /prompt/json-mode    | JSON Mode                      |
| POST   | /prompt/schema       | Structured Output using Schema |
| POST   | /prompt/tool-use     | Tool Use Simulation            |
| POST   | /prompt/ab-test      | Prompt Version A/B Testing     |


---

## Learning Outcomes

After completing this module, I learned:

- Designing production-ready System Prompts
- Building reusable Prompt Builder patterns
- Understanding Prompt Design Foundations
- Writing effective prompts using implicit and explicit instructions
- Using positive and negative prompting techniques
- Implementing Zero-shot, One-shot and Few-shot prompting
- Applying Chain-of-Thought reasoning
- Implementing Zero-shot CoT and Few-shot CoT
- Using Tree-of-Thought reasoning
- Understanding ReAct Prompting
- Implementing Meta Prompting
- Generating structured outputs using JSON, XML and Markdown
- Using JSON Mode with GitHub Models
- Validating responses using JSON Schema
- Simulating Tool Calling
- Designing production-ready System Prompts
- Injecting dynamic context into prompts
- Managing Prompt Versions
- Performing Prompt A/B Testing
- Implementing Input Validation
- Preventing Prompt Injection attacks
- Preventing Prompt Leakage
- Detecting Jailbreak attempts
- Filtering unsafe AI outputs
- Designing scalable Prompt Engineering APIs
- Organizing Prompt Engineering components for enterprise AI applications

---

## Future Enhancements

The following topics will be implemented next in Module 4:

### Embeddings & Semantic Search:

Text Embeddings
Embedding Models
Vector Similarity
Cosine Similarity
Semantic Search
Chunking Strategies
Vector Databases
Retrieval Pipelines
Embedding-based Search API

---

## Author

**Ramesh Srinivasan**

Generative AI Cross-Skilling Journey