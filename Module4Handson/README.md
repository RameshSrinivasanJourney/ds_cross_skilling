# Module 4 - Embeddings and Semantic Search

## Overview

This module focuses on one of the core technologies behind modern Generative AI applications: **Embeddings and Semantic Search**.

The project demonstrates how text embeddings capture semantic meaning, how similarity between vectors is calculated, and how semantic search can be implemented using cosine similarity, NumPy, FAISS, and Hybrid Search.

This module follows a clean, modular, and production-ready FastAPI architecture while integrating GitHub Models for embedding generation.

---

# Project Architecture

```
Module4Handson
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
├── requirements.txt
├── README.md
└── .env
```

---

# Folder Structure

| Folder   | Purpose                                             |
| -------- | --------------------------------------------------- |
| api      | REST API endpoints                                  |
| core     | Application configuration                           |
| data     | Sample employee knowledge base                      |
| models   | Request and Response models                         |
| services | Embedding, Search, FAISS and Hybrid Search services |
| utils    | Helper utilities                                    |

---

# Technologies Used

* Python 3.13
* FastAPI
* Uvicorn
* OpenAI SDK
* GitHub Models
* NumPy
* FAISS (Facebook AI Similarity Search)
* Pydantic
* python-dotenv

---

# Features Implemented

## Embeddings

* Understanding Embeddings
* Dense Vector Representation
* Embedding Generation
* Embedding API
* Embedding Service

---

## Embedding Models

Studied various embedding models including:

* OpenAI text-embedding-3-small
* OpenAI text-embedding-3-large
* Google text-embedding-004
* Cohere Embedding Models
* sentence-transformers
* Code Embeddings
* Image Embeddings (CLIP)

---

## Similarity Metrics

Implemented and learned:

* Cosine Similarity
* Dot Product Similarity
* Euclidean Distance (L2)
* Similarity Score Interpretation
* NumPy Vector Operations

---

## Semantic Search

Implemented:

* Employee Knowledge Base
* Document Embeddings
* Query Embeddings
* Top-K Retrieval
* Semantic Search Service
* Semantic Search API

---

## Vector Search

Implemented:

* FAISS Index
* IndexFlatIP
* Vector Normalization
* Vector Index Search
* FAISS Search API

---

## Hybrid Search

Implemented:

* Keyword Matching
* Semantic Search
* Score Fusion
* Hybrid Ranking
* Hybrid Search API

---

# API Endpoints

## Embedding APIs

| Method | Endpoint            | Description             |
| ------ | ------------------- | ----------------------- |
| POST   | /embedding/generate | Generate text embedding |

---

## Semantic Search APIs

| Method | Endpoint         | Description                             |
| ------ | ---------------- | --------------------------------------- |
| POST   | /search/semantic | Semantic Search using Cosine Similarity |

---

## FAISS APIs

| Method | Endpoint      | Description               |
| ------ | ------------- | ------------------------- |
| POST   | /faiss/search | Vector Search using FAISS |

---

## Hybrid Search APIs

| Method | Endpoint       | Description                               |
| ------ | -------------- | ----------------------------------------- |
| POST   | /hybrid/search | Hybrid Search (Keyword + Semantic Search) |

---

# Project Flow

```
Employee Documents
        │
        ▼
Generate Embeddings
        │
        ▼
Store as NumPy Arrays
        │
        ▼
Semantic Search
        │
        ▼
FAISS Vector Search
        │
        ▼
Hybrid Search
```

---

# Learning Outcomes

After completing this module, I learned:

* What embeddings are and why they are important.
* How embedding models capture semantic meaning.
* Difference between sparse vectors and dense vectors.
* Understanding embedding dimensions.
* Working with OpenAI and GitHub embedding models.
* Computing cosine similarity using NumPy.
* Implementing semantic document retrieval.
* Building a semantic search engine.
* Creating vector indexes using FAISS.
* Performing fast nearest-neighbor search.
* Designing Hybrid Search using keyword matching and semantic similarity.
* Organizing embedding and search components using clean architecture.

---

# Production Concepts Covered

* Dense Vector Embeddings
* Semantic Similarity
* Vector Databases
* FAISS Indexing
* Top-K Retrieval
* Hybrid Search
* Knowledge Retrieval
* Foundation for Retrieval-Augmented Generation (RAG)

---

# Future Enhancements

The following topics will be implemented in the next module:

## Module 5 – Retrieval-Augmented Generation (RAG)

* Introduction to RAG
* Chunking Strategies
* Document Loaders
* Text Splitters
* Vector Databases
* Retrieval Pipelines
* Context Injection
* Prompt Augmentation
* End-to-End RAG Application

---

# Author

**Ramesh Srinivasan**

Generative AI Cross-Skilling Journey
