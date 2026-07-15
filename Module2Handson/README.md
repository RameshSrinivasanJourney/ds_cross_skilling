# Module 2 - AI Chat Application

## Overview

This project demonstrates how to build a production-style AI Chat application using FastAPI and GitHub Models.

The application supports multi-turn conversations, conversation history, streaming architecture, logging, exception handling, and token counting while following a clean project structure.

---

## Project Architecture

```
Module2Handson
│
├── app
│   ├── api
│   ├── core
│   ├── models
│   ├── services
│   ├── utils
│   └── main.py
│
├── requirements.txt
├── README.md
└── .env
```

---

## Folder Structure

| Folder | Purpose |
|----------|----------|
| api | REST API endpoints |
| core | Application configuration and AI settings |
| models | Request and Response models |
| services | Business logic and AI integration |
| utils | Logger and Token Counter utilities |

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
- Server Sent Events (SSE)

---

## Features Implemented

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

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /chat | AI Chat |
| POST | /chat/stream | Streaming Response |
| POST | /chat/streamSSE | Server Sent Events |
| POST | /chat/partial | Partial Response Simulation |

---

## Learning Outcomes

After completing this module, I learned:

- Building REST APIs using FastAPI
- Integrating GitHub Models
- Managing Conversation History
- Designing reusable AI services
- Streaming AI responses
- Implementing Server Sent Events (SSE)
- Centralizing AI configuration
- Logging application events
- Counting LLM tokens
- Structuring a production-ready AI application

---

## Future Enhancements

The following features will be implemented in Module 3:

- Prompt Engineering
- Prompt Builder Pattern
- System Prompt
- Prompt Templates
- Role-based Prompting
- Few-shot Prompting
- Structured Outputs

---

## Author

**Ramesh Srinivasan**

Generative AI Cross-Skilling Journey