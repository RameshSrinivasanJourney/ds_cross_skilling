# Module 5 - ChromaDB Vector Database

## Overview

This module focuses on one of the most important components of Retrieval-Augmented Generation (RAG): **Vector Databases**.

The project demonstrates how to store documents inside ChromaDB, manage collections, perform semantic vector search, metadata filtering, and compare persistent versus in-memory storage.

The implementation follows a clean, modular, production-ready FastAPI architecture using SOLID principles and layered design.

---

# Project Architecture

```
Module5Handson
│
├── app
│   ├── api
│   ├── core
│   ├── data
│   ├── models
│   ├── services
│   ├── utils
│   └── main.py
│
├── chroma_db
├── requirements.txt
├── README.md
└── .env
```

---

# Folder Structure

| Folder | Purpose |
|---------|----------|
| api | REST API Endpoints |
| core | Application Configuration |
| data | Employee Knowledge Base |
| models | Request / Response Models |
| services | ChromaDB Business Logic |
| utils | Logging Utilities |
| chroma_db | Persistent Chroma Storage |

---

# Technologies Used

* Python 3.13
* FastAPI
* Uvicorn
* ChromaDB
* OpenAI SDK
* GitHub Models
* Pydantic
* python-dotenv

---

# Features Implemented

## ChromaDB Fundamentals

Implemented

* ChromaDB Installation
* Persistent Client
* Collection Creation
* Collection Management
* CRUD Operations
* Collection Information
* Collection Count
* Peek Documents

---

## Document Management

Implemented

* Load Employee Documents
* Delete Single Document
* Delete Multiple Documents
* Delete All Documents

---

## Semantic Search

Implemented

* Document Search
* Top-K Retrieval
* Distance Score
* Search Result Ranking

---

## Embedding Search

Implemented

* Explicit Embedding Generation
* Store Embeddings
* Vector Similarity Search
* Embedding-based Retrieval

---

## Metadata Filtering

Implemented

* Department Filtering
* Category Filtering
* Combined Metadata Filtering
* Semantic + Metadata Search

---

## Storage

Implemented

* Persistent Storage
* In-Memory Storage
* Collection Recreation

---

# API Endpoints

## Health APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /chroma/health | Check ChromaDB Health |

---

## Document APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /chroma/load | Load Documents |
| DELETE | /chroma/document/{id} | Delete Document |
| DELETE | /chroma/documents | Delete Multiple Documents |
| DELETE | /chroma/documents/all | Delete All Documents |

---

## Collection APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /chroma/collections | List Collections |
| POST | /chroma/collection-info | Collection Information |
| GET | /chroma/count | Document Count |
| POST | /chroma/peek | Peek Documents |

---

## Search APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /chroma/search | Semantic Search |
| POST | /chroma/vector-search | Embedding Vector Search |
| POST | /chroma/metadata-search | Metadata Filtering |

---

## Storage APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /chroma/load-embeddings | Store Explicit Embeddings |
| POST | /chroma/memory-demo | In-Memory ChromaDB Demo |

---

# Project Flow

```
Employee Documents
        │
        ▼
Load into ChromaDB
        │
        ▼
Persistent Collection
        │
        ▼
Semantic Search
        │
        ▼
Vector Search
        │
        ▼
Metadata Filtering
        │
        ▼
Search Results
```

---

# Learning Outcomes

After completing this module, I learned:

* Introduction to Vector Databases
* ChromaDB Architecture
* Persistent vs In-Memory Storage
* Collection Management
* CRUD Operations in ChromaDB
* Explicit Embedding Storage
* Vector Similarity Search
* Metadata Filtering
* Top-K Retrieval
* FastAPI Integration
* Production-ready Layered Architecture
* SOLID Design Principles

---

# Production Concepts Covered

* Vector Databases
* ChromaDB
* Persistent Storage
* Collection Management
* CRUD Operations
* Semantic Search
* Vector Search
* Metadata Filtering
* Embedding Storage
* Knowledge Retrieval
* FastAPI Integration

---

# Future Enhancements

The following topics will be implemented in the continuation of Module 5:

## Advanced Vector Databases

* Qdrant
* FAISS
* Pinecone
* Milvus
* Hybrid Search
* Vector Database Comparison
* Performance Benchmarking

---

# Author

**Ramesh Srinivasan**

Generative AI Cross-Skilling Journey