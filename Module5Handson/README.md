# Module 5 - Vector Databases & Similarity Search

## Overview

This module focuses on one of the most important components of **Retrieval-Augmented Generation (RAG): Vector Databases and Similarity Search**.

The module provides hands-on implementation of multiple vector database and vector search technologies using a clean, modular, production-oriented **FastAPI architecture**.

The following technologies and concepts are covered:

* ChromaDB
* Qdrant
* FAISS
* Sentence Transformers
* Dense Vector Search
* Keyword Search
* Hybrid Search
* Payload Filtering
* Named Vectors
* IndexFlatL2
* IndexFlatIP
* Approximate Nearest Neighbor Search
* Persistent Vector Indexes

The implementation follows **SOLID principles**, layered architecture, service-based design, and reusable API interfaces.

---

# Project Architecture

```text
Module5Handson
│
├── app
│   ├── api
│   │   ├── chroma
│   │   ├── qdrant
│   │   ├── faiss
│   │   └── ...
│   │
│   ├── core
│   │   └── config.py
│   │
│   ├── data
│   │   └── employee_documents.py
│   │
│   ├── models
│   │   ├── chroma
│   │   ├── qdrant
│   │   ├── faiss
│   │   └── ...
│   │
│   ├── services
│   │   ├── embedding_service.py
│   │   ├── chroma_service.py
│   │   ├── qdrant_service.py
│   │   ├── faiss_service.py
│   │   └── faiss_st_service.py
│   │
│   ├── utils
│   │   └── logger.py
│   │
│   └── main.py
│
├── chroma_db/
├── faiss/
├── requirements.txt
├── README.md
├── .env
├── .env.example
└── .gitignore
```

---

# Folder Structure

| Folder      | Purpose                                   |
| ----------- | ----------------------------------------- |
| `api`       | REST API endpoints                        |
| `core`      | Application configuration                 |
| `data`      | Employee knowledge-base documents         |
| `models`    | FastAPI request/response models           |
| `services`  | Database and vector-search business logic |
| `utils`     | Logging and utility functionality         |
| `chroma_db` | Persistent ChromaDB storage               |
| `faiss`     | FAISS index storage                       |

---

# Technologies Used

* Python 3.13
* FastAPI
* Uvicorn
* ChromaDB
* Qdrant
* FAISS
* Sentence Transformers
* Hugging Face Transformers
* NumPy
* OpenAI Python SDK
* Pydantic
* pydantic-settings
* python-dotenv

---

# Embedding Model

The module initially used GitHub Models for embedding generation.

Due to GitHub Models availability limitations, the implementation was extended to support a local **Sentence Transformer** model.

Current local embedding model:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Embedding dimension:

```text
384
```

The local model removes the dependency on an external embedding API for FAISS and related experiments.

---

# Employee Knowledge Base

The project uses a small employee knowledge base containing documents related to:

* HR
* Finance
* IT
* Learning
* Administration

Example:

```text
Employees are eligible for 20 days of annual leave every calendar year.
```

Documents contain metadata such as:

```text
id
department
category
text
```

This makes the dataset useful for demonstrating both semantic search and metadata/payload filtering.

---

# ChromaDB

## ChromaDB Fundamentals

Implemented:

* ChromaDB installation
* Persistent client
* In-memory client
* Collection creation
* Collection management
* CRUD operations
* Collection information
* Document count
* Document peek

---

## Document Management

Implemented:

* Load employee documents
* Delete single document
* Delete multiple documents
* Delete all documents

---

## Semantic Search

Implemented:

* Semantic document search
* Top-K retrieval
* Similarity/distance scores
* Search result ranking

---

## Embedding Search

Implemented:

* Explicit embedding generation
* Store embeddings
* Vector similarity search
* Embedding-based retrieval

---

## Metadata Filtering

Implemented:

* Department filtering
* Category filtering
* Combined metadata filtering
* Semantic + metadata search

---

## ChromaDB Storage

Implemented:

* Persistent storage
* In-memory storage
* Collection recreation

---

# Qdrant

Qdrant was implemented to understand a production-oriented dedicated vector database.

## Qdrant Fundamentals

Implemented:

* Qdrant Cloud connection
* Collection creation
* Point insertion
* Payload storage
* Vector search
* Payload filtering
* Payload indexes

---

## Qdrant Payload Filtering

Implemented filtering using:

```text
department
category
```

Example:

```text
department = HR
```

Qdrant payload indexes were created for keyword filtering.

---

## Qdrant Hybrid Search

Implemented:

* Keyword search
* Dense vector search
* Hybrid search
* Result merging
* Combined ranking

The hybrid-search flow combines lexical/keyword relevance with semantic vector relevance.

Conceptually:

```text
                    Query
                      │
             ┌────────┴────────┐
             │                 │
             ▼                 ▼
       Keyword Search     Dense Search
             │                 │
             └────────┬────────┘
                      ▼
                Result Merge
                      │
                      ▼
               Combined Ranking
                      │
                      ▼
                Top-K Results
```

---

# Qdrant Named Vectors

Named vectors were implemented to understand multi-vector use cases.

The collection contains two vector representations:

```text
text
summary
```

Conceptually:

```text
Document
   │
   ├── text vector
   │
   └── summary vector
```

Implemented:

```text
POST /qdrant/named-vectors/create-collection
POST /qdrant/named-vectors/load
POST /qdrant/named-vectors/search
```

This demonstrates how the same document can have multiple vector representations inside a single Qdrant point.

---

# FAISS

FAISS was introduced to understand high-performance vector similarity search without requiring a vector database server.

FAISS experiments include:

* IndexFlatL2
* IndexFlatIP
* Vector insertion
* Similarity search
* Index counting
* Persistent index storage
* Sentence Transformer embeddings

---

# FAISS IndexFlatL2

`IndexFlatL2` performs exact nearest-neighbor search using **L2 / Euclidean distance**.

Implemented APIs:

```text
POST /faiss/index/create-flat-l2
POST /faiss/load
POST /faiss/search
GET  /faiss/count
```

The flow is:

```text
Document
    │
    ▼
Sentence Transformer
    │
    ▼
384-dimensional vector
    │
    ▼
FAISS IndexFlatL2
    │
    ▼
L2 similarity search
```

---

# FAISS IndexFlatIP

`IndexFlatIP` performs exact search using **Inner Product**.

Inner Product can also be used as cosine similarity when vectors are normalized.

For normalized vectors:

```text
cosine_similarity(A, B) = A · B
```

Therefore:

```text
Normalize vectors
       │
       ▼
IndexFlatIP
       │
       ▼
Cosine-like similarity search
```

This is an important technique used in many real-world semantic-search systems.

---

# FAISS + Sentence Transformers

A separate FAISS implementation was created using the local Sentence Transformer model:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Embedding dimension:

```text
384
```

Implemented APIs:

```text
POST /faiss/st/create-flat-l2
POST /faiss/st/load
POST /faiss/st/search
GET  /faiss/st/count
```

---

## Sentence Transformer FAISS Flow

```text
Employee Documents
        │
        ▼
Sentence Transformer
        │
        ▼
384-dimensional embeddings
        │
        ▼
FAISS IndexFlatL2
        │
        ▼
Similarity Search
        │
        ▼
Top-K Documents
```

The `/faiss/st/load` endpoint loads the employee documents from the application's employee-document dataset and generates the embeddings locally.

---

# FAISS Approximate Search

The module also covers the concepts behind approximate nearest-neighbor indexes:

## IndexIVFFlat

Used for faster approximate search by dividing the vector space into clusters.

Concept:

```text
Vectors
   │
   ▼
Cluster / Partition
   │
   ▼
Search selected clusters
   │
   ▼
Nearest vectors
```

Important concepts:

* Number of clusters (`nlist`)
* Number of clusters searched (`nprobe`)
* Training requirement
* Search-speed vs accuracy trade-off

---

## IndexHNSWFlat

HNSW (Hierarchical Navigable Small World) provides graph-based approximate nearest-neighbor search.

Important concepts:

* Graph-based indexing
* Hierarchical layers
* Fast approximate search
* Search accuracy vs performance
* `efSearch`
* `M`

---

# FAISS Index Persistence

The module also covers saving and loading FAISS indexes.

Concept:

```text
FAISS Index
     │
     ▼
Write to Disk
     │
     ▼
.index file
     │
     ▼
Read from Disk
     │
     ▼
FAISS Index restored
```

This demonstrates how a FAISS index can survive application restarts instead of being rebuilt every time.

---

# GPU-Accelerated FAISS

The module also introduces GPU-accelerated FAISS concepts.

GPU acceleration can be useful when:

* Vector collections become large
* Search volume increases
* Index construction becomes expensive
* High-throughput similarity search is required

Concept:

```text
CPU
 │
 ├── Vector preparation
 │
 ▼
GPU
 │
 ├── Index construction
 ├── Vector search
 └── Similarity calculations
 │
 ▼
Search Results
```

GPU support depends on the FAISS package/build and the available CUDA-compatible hardware.

---

# API Endpoints

## ChromaDB APIs

### Health

| Method | Endpoint         | Description           |
| ------ | ---------------- | --------------------- |
| GET    | `/chroma/health` | Check ChromaDB health |

### Documents

| Method | Endpoint                | Description               |
| ------ | ----------------------- | ------------------------- |
| POST   | `/chroma/load`          | Load documents            |
| DELETE | `/chroma/document/{id}` | Delete document           |
| DELETE | `/chroma/documents`     | Delete multiple documents |
| DELETE | `/chroma/documents/all` | Delete all documents      |

### Collections

| Method | Endpoint                  | Description            |
| ------ | ------------------------- | ---------------------- |
| GET    | `/chroma/collections`     | List collections       |
| POST   | `/chroma/collection-info` | Collection information |
| GET    | `/chroma/count`           | Document count         |
| POST   | `/chroma/peek`            | Peek documents         |

### Search

| Method | Endpoint                  | Description        |
| ------ | ------------------------- | ------------------ |
| POST   | `/chroma/search`          | Semantic search    |
| POST   | `/chroma/vector-search`   | Vector search      |
| POST   | `/chroma/metadata-search` | Metadata filtering |

### Storage

| Method | Endpoint                  | Description               |
| ------ | ------------------------- | ------------------------- |
| POST   | `/chroma/load-embeddings` | Store explicit embeddings |
| POST   | `/chroma/memory-demo`     | In-memory ChromaDB demo   |

---

# Qdrant APIs

### Collections

| Method | Endpoint                    | Description              |
| ------ | --------------------------- | ------------------------ |
| POST   | `/qdrant/create-collection` | Create Qdrant collection |

### Search

| Method | Endpoint                 | Description                   |
| ------ | ------------------------ | ----------------------------- |
| POST   | `/qdrant/search`         | Dense vector search           |
| POST   | `/qdrant/keyword-search` | Keyword search                |
| POST   | `/qdrant/hybrid-search`  | Dense + keyword hybrid search |
| POST   | `/qdrant/payload-search` | Payload-filtered search       |

### Named Vectors

| Method | Endpoint                                  | Description                       |
| ------ | ----------------------------------------- | --------------------------------- |
| POST   | `/qdrant/named-vectors/create-collection` | Create multi-vector collection    |
| POST   | `/qdrant/named-vectors/load`              | Load documents with named vectors |
| POST   | `/qdrant/named-vectors/search`            | Search using a selected vector    |

---

# FAISS APIs

### Exact Vector Search

| Method | Endpoint                      | Description               |
| ------ | ----------------------------- | ------------------------- |
| POST   | `/faiss/index/create-flat-l2` | Create IndexFlatL2        |
| POST   | `/faiss/load`                 | Load documents into FAISS |
| POST   | `/faiss/search`               | Search FAISS index        |
| GET    | `/faiss/count`                | Count vectors             |

### Sentence Transformer FAISS

| Method | Endpoint                   | Description                                           |
| ------ | -------------------------- | ----------------------------------------------------- |
| POST   | `/faiss/st/create-flat-l2` | Create Sentence Transformer IndexFlatL2               |
| POST   | `/faiss/st/load`           | Load employee documents and generate local embeddings |
| POST   | `/faiss/st/search`         | Search Sentence Transformer FAISS index               |
| GET    | `/faiss/st/count`          | Count vectors                                         |

---

# Project Flow

```text
                 Employee Documents
                         │
                         ▼
                Document Processing
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
       ChromaDB        Qdrant          FAISS
          │              │              │
          ▼              ▼              ▼
      Vector Search   Vector Search   ANN Search
          │              │              │
          │        ┌─────┴─────┐        │
          │        │           │        │
          │        ▼           ▼        │
          │     Payload     Hybrid      │
          │     Filtering    Search     │
          │                    │        │
          └────────────┬───────┴────────┘
                       │
                       ▼
                 Search Results
```

---

# Similarity Search Concepts

This module covers the difference between:

### L2 Distance

Measures Euclidean distance.

```text
Smaller distance = more similar
```

Used by:

```text
IndexFlatL2
IndexIVFFlat
IndexHNSWFlat
```

depending on configuration.

---

### Inner Product

Measures the dot product between vectors.

```text
Larger score = more similar
```

When vectors are normalized:

```text
Inner Product ≈ Cosine Similarity
```

---

### Cosine Similarity

Measures the angle between two vectors.

It is commonly used for semantic search because the direction of the embedding is often more important than its magnitude.

---

# Dense vs Keyword vs Hybrid Search

## Keyword Search

Finds exact or lexical matches.

Example:

```text
Query: leave
```

Keyword search primarily looks for matching terms.

---

## Dense Search

Uses embeddings to understand semantic meaning.

Example:

```text
Query:
vacation allowance

Document:
Employees are eligible for 20 days of annual leave.
```

Even though the words are different, the semantic meaning is similar.

---

## Hybrid Search

Combines both approaches:

```text
Keyword Search
       +
Dense Vector Search
       │
       ▼
Result Fusion
       │
       ▼
Combined Ranking
```

Hybrid search can provide better retrieval quality because it combines lexical precision with semantic understanding.

---

# Learning Outcomes

After completing Module 5, I learned:

* What vector databases are
* Why vector databases are important for RAG
* ChromaDB architecture
* Persistent vs in-memory vector storage
* Collection management
* CRUD operations
* Explicit embedding storage
* Semantic search
* Vector similarity search
* Metadata filtering
* Qdrant architecture
* Qdrant payloads
* Qdrant payload indexes
* Qdrant dense search
* Qdrant keyword search
* Qdrant hybrid search
* Qdrant named vectors
* Multi-vector collections
* FAISS architecture
* IndexFlatL2
* IndexFlatIP
* L2 distance
* Inner Product
* Cosine similarity
* Sentence Transformer embeddings
* 384-dimensional embeddings
* Approximate nearest-neighbor search
* IndexIVFFlat
* IndexHNSWFlat
* FAISS persistence
* GPU-accelerated FAISS concepts
* FastAPI integration
* REST API design
* SOLID principles
* Layered architecture

---

# Production Concepts Covered

This module provides practical exposure to:

* Vector database selection
* Dense retrieval
* Lexical retrieval
* Hybrid retrieval
* Metadata filtering
* Multi-vector retrieval
* Exact nearest-neighbor search
* Approximate nearest-neighbor search
* Embedding model selection
* Local embedding generation
* Vector index persistence
* Search performance considerations
* Retrieval architecture
* RAG infrastructure
* FastAPI service architecture

---

# Technology Comparison

| Technology            | Primary Purpose                            | Search         |
| --------------------- | ------------------------------------------ | -------------- |
| ChromaDB              | Developer-friendly vector database         | Dense          |
| Qdrant                | Production vector database                 | Dense / Hybrid |
| FAISS                 | High-performance vector similarity library | Dense          |
| Sentence Transformers | Local embedding generation                 | Embeddings     |

---

# Module 5 Architecture

```text
                    FastAPI
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
    Chroma API     Qdrant API     FAISS API
        │              │              │
        ▼              ▼              ▼
    ChromaDB         Qdrant          FAISS
                       │
                       │
                 Named Vectors
                       │
                       ▼
                Hybrid Retrieval


              Sentence Transformers
                       │
                       ▼
                 Local Embeddings
                       │
                       ▼
                    FAISS
```

---

# Module 5 Completion Status

| Topic                           | Status    |
| ------------------------------- | --------- |
| ChromaDB                        | Completed |
| ChromaDB CRUD                   | Completed |
| ChromaDB Semantic Search        | Completed |
| ChromaDB Metadata Filtering     | Completed |
| Qdrant                          | Completed |
| Qdrant Payloads                 | Completed |
| Qdrant Payload Filtering        | Completed |
| Qdrant Keyword Search           | Completed |
| Qdrant Dense Search             | Completed |
| Qdrant Hybrid Search            | Completed |
| Qdrant Named Vectors            | Completed |
| FAISS                           | Completed |
| IndexFlatL2                     | Completed |
| IndexFlatIP                     | Completed |
| Sentence Transformer Embeddings | Completed |
| FAISS + Sentence Transformers   | Completed |
| IndexIVFFlat                    | Covered   |
| IndexHNSWFlat                   | Covered   |
| FAISS Persistence               | Covered   |
| GPU-accelerated FAISS           | Covered   |

---

# Future Enhancements

Potential future topics include:

* Pinecone
* Milvus
* Weaviate
* Vector database benchmarking
* Retrieval evaluation
* RAG pipeline optimization
* Re-ranking models
* Cross-encoder re-ranking
* Advanced hybrid-search strategies
* Production-scale vector indexing

---

# Running the Application

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell execution policy blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate:

```powershell
.\.venv\Scripts\Activate.ps1
```

Start the FastAPI application:

```powershell
python -m uvicorn app.main:app --reload --port 8005
```

Swagger UI:

```text
http://127.0.0.1:8005/docs
```

OpenAPI:

```text
http://127.0.0.1:8005/openapi.json
```

---

# Configuration

Create a `.env` file containing the required configuration.

Example:

```text
# GitHub Models
GITHUB_TOKEN=
GITHUB_ENDPOINT=
EMBEDDING_MODEL=

# ChromaDB
CHROMA_DB_PATH=./chroma_db
CHROMA_COLLECTION_NAME=employee_documents

# Qdrant
QDRANT_API_KEY=
QDRANT_URL=
QDRANT_COLLECTION=employee_documents
QDRANT_HOST=localhost
QDRANT_PORT=6333

# FAISS - Sentence Transformer
FAISS_ST_INDEX_PATH=./faiss_st_index
FAISS_ST_DIMENSION=384
```

The local Sentence Transformer model is used for the FAISS Sentence Transformer implementation.

---

# Git

The project is maintained using Git and the completed Module 5 implementation is committed to the repository.

Typical workflow:

```powershell
git status

git add .

git commit -m "Complete Module 5 vector database implementations"

git push
```

---

# Author

**Ramesh Srinivasan**

Generative AI Cross-Skilling Journey
