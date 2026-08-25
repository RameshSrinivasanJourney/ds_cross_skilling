# Module 12 - Building Production APIs

## Overview

Module 12 focuses on building production-oriented APIs for Generative AI applications using **FastAPI**, **Ollama**, asynchronous processing, streaming, WebSockets, session management, and file-processing workflows.

The module uses the local **Ollama `llama3.2:3b`** model wherever practical and demonstrates how a simple GenAI API evolves toward a production-style backend architecture.

---

# Learning Objectives

By the end of this module, you will understand:

* Synchronous vs asynchronous API endpoints
* Streaming endpoints
* Server-Sent Events (SSE)
* WebSocket endpoints
* Background tasks
* Status polling
* REST vs SSE vs WebSocket
* Production-oriented FastAPI project structure
* Pydantic request and response models
* Dependency injection
* StreamingResponse
* WebSocket routing
* BackgroundTasks
* CORS middleware
* Authentication dependencies
* Rate limiting
* Custom LLM exception handling
* Stateless API design
* UUID conversation identifiers
* Redis-backed session architecture
* Multi-tenant session isolation
* Session expiry and cleanup
* Multipart file uploads
* File type validation
* File size validation
* Asynchronous file processing
* Temporary file storage
* Temporary file cleanup

---

# Environment

```text
Python 3.13.15
FastAPI
Uvicorn
Ollama
llama3.2:3b
Redis Python client
```

The primary LLM runtime is local Ollama.

---

# Project Structure

```text
Module12Handson/
│
├── .venv/
│
├── app/
│   ├── __init__.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       ├── chat.py
│   │       ├── jobs.py
│   │       ├── websocket.py
│   │       ├── sessions.py
│   │       └── files.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── chat.py
│   │   ├── session.py
│   │   └── file.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── llm_service.py
│   │
│   ├── dependencies/
│   │   ├── __init__.py
│   │   └── common.py
│   │
│   ├── middleware/
│   │   ├── __init__.py
│   │   └── security.py
│   │
│   ├── sessions/
│   │   ├── __init__.py
│   │   └── session_store.py
│   │
│   ├── files/
│   │   ├── __init__.py
│   │   ├── file_processor.py
│   │   ├── file_service.py
│   │   └── file_jobs.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── exceptions.py
│   │
│   └── config/
│       └── __init__.py
│
├── tests/
│   └── test_websocket.py
│
├── data/
├── uploads/
├── temp/
│
├── .gitignore
├── README.md
├── requirements.txt
└── main.py
```

---

# Topic 1 - API Design for GenAI

## 1.1 Sync vs Async Endpoints

Synchronous:

```text
Client
  ↓
POST /chat/sync
  ↓
Ollama
  ↓
Complete Response
```

Asynchronous:

```text
Client
  ↓
POST /chat/async
  ↓
Async route
  ↓
Ollama
  ↓
Response
```

Blocking Ollama operations are moved to a worker thread using `asyncio.to_thread()`.

## 1.2 Streaming Endpoints

The complete response does not need to wait until all generated content is available.

```text
Client
  ↓
StreamingResponse
  ↑
chunk
  ↑
chunk
  ↑
chunk
```

## 1.3 WebSocket

WebSockets provide bidirectional communication:

```text
Client ←────────→ FastAPI
```

The hands-on implements:

```text
/ws/chat
```

## 1.4 Background Tasks and Polling

Longer operations can be started separately:

```text
POST /jobs
      ↓
job_id
      ↓
GET /jobs/{job_id}
      ↓
queued
running
completed
failed
```

## 1.5 REST vs SSE vs WebSocket

| Pattern              | Direction          | Best use                          |
| -------------------- | ------------------ | --------------------------------- |
| REST                 | Request → Response | Standard API operations           |
| SSE                  | Server → Client    | Streaming server events           |
| WebSocket            | Bidirectional      | Realtime interactive applications |
| Background + polling | Job → Status       | Long-running operations           |

### Tests

```powershell
python -m uvicorn main:app --reload
```

Health:

```text
GET /health
```

REST:

```text
POST /chat/sync
POST /chat/async
```

Streaming:

```text
POST /chat/stream
GET /chat/sse
```

Background:

```text
POST /jobs
GET /jobs/{job_id}
```

WebSocket:

```powershell
python -m tests.test_websocket
```

---

# Topic 2 - FastAPI for GenAI Backends

## 2.1 Project Structure

The API is separated into:

```text
Routes
Services
Models
Dependencies
Middleware
Core Configuration
```

The main architectural principle is:

```text
API Route
   ↓
Service
   ↓
LLM
```

rather than placing all application logic directly inside route functions.

## 2.2 Async Route Handlers

Async routes are used for I/O-oriented operations.

Blocking Ollama calls are delegated through `asyncio.to_thread()`.

## 2.3 Pydantic Models

Request:

```json
{
  "question": "Explain RAG."
}
```

Response:

```json
{
  "answer": "...",
  "model": "llama3.2:3b"
}
```

Validation includes minimum and maximum question length.

## 2.4 Dependency Injection

FastAPI `Depends()` is used for:

* LLM service
* API-key authentication
* Shared application dependencies

## 2.5 StreamingResponse

Streaming output is returned with:

```text
POST /api/v1/chat/stream
```

## 2.6 WebSocket

Realtime chat is implemented at:

```text
/ws/chat
```

## 2.7 BackgroundTasks

Long-running API tasks can be started and polled through:

```text
POST /api/v1/jobs
GET /api/v1/jobs/{job_id}
```

## 2.8 CORS, Authentication, Rate Limiting

The application includes:

* CORS middleware
* API-key validation
* Lightweight in-memory rate limiting

The API key is:

```text
module12-demo-key
```

for local learning.

The rate limiter is intentionally in-memory and is not intended for a multi-instance production deployment.

## 2.9 LLM Exception Handling

LLM errors are translated into:

```text
503 Service Unavailable
```

with a controlled application-level error response.

---

# Topic 3 - Session and State Management

## 3.1 Stateless API Design

Conversation state is not stored directly inside the FastAPI process.

Conceptually:

```text
Server A ─┐
Server B ─┼──→ External Session Store
Server C ─┘
```

## 3.2 Redis for Server-Side Session Storage

The project includes a Redis-backed:

```text
app/sessions/session_store.py
```

Session keys follow:

```text
session:{tenant_id}:{conversation_id}
```

Stored state includes:

```text
tenant_id
conversation_id
messages
created_at
last_accessed_at
```

## 3.3 Conversation ID with UUID

New conversations use UUID identifiers.

Example:

```text
550e8400-e29b-41d4-a716-446655440000
```

## 3.4 Multi-Tenant Session Isolation

Tenant identity is part of the Redis key.

Therefore:

```text
tenant-a + conversation-a
```

cannot access:

```text
tenant-b + conversation-a
```

The API validates the tenant and conversation combination.

## 3.5 Session Expiry and Cleanup

Sessions use Redis TTL:

```text
1800 seconds
```

The TTL is refreshed when the session is accessed.

Conceptually:

```text
Create
 ↓
TTL = 1800
 ↓
Access
 ↓
TTL refreshed
 ↓
No access
 ↓
Expired
```

### Redis Runtime Note

The Redis Python client and the Redis-backed session implementation are included in the project.

The local Redis server could not be started in this environment because the available Docker engine was not running and Memurai was not installed. Therefore:

```text
Redis adapter implementation    ✅
Redis session design            ✅
UUID/session isolation          ✅
TTL implementation              ✅
Redis server runtime test      ⚠️ not executed locally
```

This limitation does not affect the FastAPI session-store implementation itself.

---

# Topic 4 - File Handling

## 4.1 Multipart File Upload

The API accepts:

```text
multipart/form-data
```

through FastAPI `UploadFile`.

Endpoint:

```text
POST /api/v1/files/upload
```

Supported examples:

```text
.txt
.json
.pdf
```

## 4.2 File Type and Size Validation

Allowed extensions:

```text
.txt
.json
.pdf
```

Maximum file size:

```text
5 MB
```

Files are read in chunks so the size limit can be enforced while uploading.

## 4.3 Async File Processing Pipeline

The pipeline is:

```text
Upload
  ↓
Validation
  ↓
Temporary Storage
  ↓
Background Processing
  ↓
Text Extraction
  ↓
Ollama Summary
  ↓
Job Completion
```

## 4.4 Temporary Storage and Cleanup

Temporary uploaded files are placed in:

```text
temp/
```

After processing, the file is deleted.

Job information is exposed through:

```text
GET /api/v1/files/{job_id}
```

Statuses:

```text
queued
processing
completed
failed
```

---

# File Processing Architecture

```text
Client
  ↓
Multipart Upload
  ↓
FastAPI
  ↓
Validate Extension
  ↓
Validate Size
  ↓
Temporary File
  ↓
Background Processing
  ↓
Extract Text
  ↓
Ollama
  ↓
Summary
  ↓
Cleanup
  ↓
Job Status
```

---

# Swagger Testing

Start:

```powershell
python -m uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

Important endpoints:

```text
GET  /health

POST /api/v1/chat
POST /api/v1/chat/stream

POST /api/v1/jobs
GET  /api/v1/jobs/{job_id}

POST /api/v1/sessions
POST /api/v1/sessions/chat

POST /api/v1/files/upload
GET  /api/v1/files/{job_id}
```

WebSocket:

```text
ws://127.0.0.1:8000/ws/chat
```

---

# Module 12 Final Architecture

```text
                             Client
                               |
                +--------------+--------------+
                |              |              |
               REST           SSE        WebSocket
                |              |              |
                +--------------+--------------+
                               |
                             FastAPI
                               |
                  +------------+------------+
                  |            |            |
               Routes      Middleware    Dependencies
                  |            |            |
                  +------------+------------+
                               |
                 +-------------+-------------+
                 |                           |
              Services                    Sessions
                 |                           |
              Ollama                     Redis
                 |
             File Service
                 |
       +---------+---------+
       |                   |
 Temporary Storage      Background Job
       |
    Cleanup
```

---

# Production Considerations

This module intentionally uses lightweight local implementations for learning.

For production systems:

```text
In-memory rate limiter
→ Redis / API gateway

In-memory job store
→ Redis / PostgreSQL

FastAPI BackgroundTasks
→ Durable worker queue

Local temporary files
→ Object storage

Simple API key
→ OAuth2 / JWT / enterprise identity

Single Uvicorn process
→ Production application server / container deployment
```

The purpose of this module is to understand the API architecture before introducing the full production infrastructure stack.

---

# Module 12 Final Checklist

```text
1. API Design for GenAI
   Hands-on 1 ✅

2. FastAPI for GenAI Backends
   Hands-on 2 ✅

3. Session and State Management
   Hands-on 3 ✅

4. File Handling
   Hands-on 4 ✅
```

# Key Interview Questions

## Sync vs async endpoint?

A synchronous handler blocks while executing synchronous work. An async handler can cooperate with the event loop for asynchronous I/O, but blocking calls still need to be moved to a thread/process or replaced by a truly async client.

## REST vs SSE vs WebSocket?

REST is request/response, SSE is server-to-client streaming, and WebSocket provides persistent bidirectional communication.

## Why use StreamingResponse?

It allows generated output or other data to be returned incrementally rather than waiting for the entire response.

## Why use Pydantic models?

They provide explicit request validation, parsing, and response serialization.

## Why use dependency injection?

It separates route logic from reusable services such as authentication, LLM clients, databases, and configuration.

## Why should APIs be stateless?

Stateless APIs can scale horizontally because requests do not depend on process-local conversation state.

## Why use Redis for sessions?

Redis provides fast shared state and TTL-based expiration.

## Why use UUID conversation IDs?

They provide unique identifiers for independently addressable conversations.

## How do you isolate tenants?

Always scope session lookup by both tenant identity and conversation identifier.

## Why validate file size during upload?

It prevents excessively large files from consuming application memory and storage resources.

## Why clean up temporary files?

Temporary storage should not accumulate indefinitely and become a storage or security problem.
