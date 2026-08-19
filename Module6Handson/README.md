# Module 6 - Advanced Retrieval Techniques & RAG

## Overview

This module focuses on the next major stage of **Retrieval-Augmented Generation (RAG): Advanced Retrieval Techniques and End-to-End RAG Architecture**.

The module builds on the vector database and similarity-search concepts learned in **Module 5** and introduces practical techniques for improving retrieval quality, relevance, grounding, and final answer generation.

The implementation follows a clean, modular, production-oriented **FastAPI architecture**.

The module covers the complete RAG pipeline:

```text
Documents
    │
    ▼
Ingestion
    │
    ▼
Parsing
    │
    ▼
Chunking
    │
    ▼
Embedding Generation
    │
    ▼
Vector Index
    │
    ▼
Retrieval
    │
    ▼
Advanced Retrieval
    │
    ├── Multi-Query Retrieval
    │
    ├── Self-RAG
    │
    ├── Corrective RAG
    │
    ├── Hybrid Retrieval
    │
    └── Re-ranking
    │
    ▼
Context Augmentation
    │
    ▼
LLM Generation
    │
    ▼
Grounded Answer
    │
    ▼
Source Attribution
    │
    ▼
Evaluation
```

The major technologies and concepts covered are:

* RAG Architecture
* Document Ingestion
* Document Parsing
* PDF Processing
* PyMuPDF
* pdfplumber
* DOCX Processing
* HTML Processing
* CSV and Excel Processing
* Source Code Processing
* OCR Concepts
* Table Extraction
* Text Cleaning
* Chunking Strategies
* Fixed-Size Chunking
* Overlapping Chunks
* Recursive Chunking
* Semantic Chunking Concepts
* Embedding Generation
* Sentence Transformers
* FAISS
* Dense Retrieval
* Multi-Query Retrieval
* Query Expansion
* Query Variations
* Result Deduplication
* Hybrid Retrieval
* Reciprocal Rank Fusion
* Self-RAG
* Corrective RAG
* Retrieval Evaluation
* Reranking
* Bi-Encoder
* Cross-Encoder
* Cohere Rerank
* BGE Reranker
* FlashRank
* Context Augmentation
* LLM Generation
* Ollama
* Llama 3.2
* Source Attribution
* Grounded Generation
* RAG Evaluation
* RAGAS Concepts
* FastAPI
* Service-Based Architecture
* SOLID Principles
* Layered Architecture

---

# Project Architecture

```text
Module6Handson
│
├── app
│   │
│   ├── api
│   │   ├── health.py
│   │   ├── ingestion.py
│   │   ├── rag.py
│   │   ├── multi_query.py
│   │   ├── reranking.py
│   │   └── ...
│   │
│   ├── core
│   │   └── config.py
│   │
│   ├── data
│   │   └── ...
│   │
│   ├── models
│   │   ├── ingestion.py
│   │   ├── rag.py
│   │   ├── multi_query.py
│   │   └── reranking.py
│   │
│   ├── services
│   │   ├── embedding_service.py
│   │   ├── ingestion_service.py
│   │   ├── chunking_service.py
│   │   ├── rag_service.py
│   │   ├── multi_query_service.py
│   │   ├── reranker_service.py
│   │   └── ...
│   │
│   ├── utils
│   │   └── logger.py
│   │
│   └── main.py
│
├── data
│
├── indexes
│
├── faiss
│
├── requirements.txt
├── README.md
├── .env
├── .env.example
└── .gitignore
```

---

# Folder Structure

| Folder     | Purpose                                  |
| ---------- | ---------------------------------------- |
| `api`      | REST API endpoints                       |
| `core`     | Application configuration                |
| `data`     | Source documents and knowledge-base data |
| `models`   | FastAPI request/response models          |
| `services` | Business logic and RAG services          |
| `utils`    | Logging and utility functionality        |
| `indexes`  | Persistent vector indexes                |
| `faiss`    | FAISS index storage                      |

---

# Technologies Used

* Python 3.13
* FastAPI
* Uvicorn
* Sentence Transformers
* Hugging Face Transformers
* FAISS
* NumPy
* Pydantic
* pydantic-settings
* python-dotenv
* PyMuPDF
* pdfplumber
* Ollama
* Llama 3.2
* FlashRank
* RAGAS concepts
* OpenAI Python SDK
* Cohere API concepts
* BGE Reranker concepts

---

# RAG Architecture

Retrieval-Augmented Generation combines information retrieval with Large Language Model generation.

A traditional LLM:

```text
User Query
    │
    ▼
LLM
    │
    ▼
Answer
```

A RAG system:

```text
User Query
    │
    ▼
Query Processing
    │
    ▼
Retriever
    │
    ▼
Relevant Documents
    │
    ▼
Context Construction
    │
    ▼
LLM
    │
    ▼
Grounded Answer
```

The major advantage of RAG is that the LLM can use external knowledge instead of relying only on information learned during model training.

---

# End-to-End RAG Pipeline

```text
                    Documents
                        │
                        ▼
                 Document Ingestion
                        │
                        ▼
                   Text Parsing
                        │
                        ▼
                    Chunking
                        │
                        ▼
                Embedding Generation
                        │
                        ▼
                   Vector Index
                        │
                        ▼
                    Retrieval
                        │
             ┌──────────┼──────────┐
             │          │          │
             ▼          ▼          ▼
         Multi-Query  Hybrid    Dense Search
             │          │          │
             └──────────┼──────────┘
                        │
                        ▼
                    Re-ranking
                        │
                        ▼
                 Context Selection
                        │
                        ▼
                    LLM Prompt
                        │
                        ▼
                 Generated Answer
                        │
                        ▼
                 Source Attribution
```

---

# Document Ingestion

Document ingestion is the first stage of the RAG pipeline.

The purpose of ingestion is to convert different document formats into usable textual information.

Supported document types and concepts include:

* PDF
* DOCX
* HTML
* TXT
* CSV
* Excel
* Source Code
* Scanned Documents
* Tables

Conceptually:

```text
Source Documents
      │
      ▼
Document Loader
      │
      ▼
Parser
      │
      ▼
Clean Text
      │
      ▼
Document Objects
```

---

# PDF Ingestion

PDF documents are one of the most common sources used in enterprise RAG systems.

The module covers PDF processing using:

* PyMuPDF
* pdfplumber

Example flow:

```text
PDF
 │
 ▼
PDF Parser
 │
 ▼
Pages
 │
 ▼
Text Extraction
 │
 ▼
Clean Text
 │
 ▼
Chunks
```

---

# PyMuPDF

PyMuPDF can be used for fast PDF text extraction.

Typical use cases include:

* Extracting text
* Reading pages
* Reading metadata
* Processing large PDF files
* Page-level document processing

Conceptually:

```text
PDF
 │
 ▼
PyMuPDF
 │
 ▼
Page Text
 │
 ▼
Document Chunks
```

---

# pdfplumber

pdfplumber is useful when working with structured PDF content.

It can be useful for:

* Text extraction
* Table extraction
* Page-level processing
* Layout-aware document processing

Conceptually:

```text
PDF
 │
 ├── Text
 │
 └── Tables
```

---

# Other Document Formats

The RAG architecture can be extended to support:

## DOCX

```text
DOCX
 │
 ▼
DOCX Parser
 │
 ▼
Paragraphs
 │
 ▼
Clean Text
```

## HTML

```text
HTML
 │
 ▼
HTML Parser
 │
 ▼
Visible Content
 │
 ▼
Clean Text
```

## CSV / Excel

```text
CSV / Excel
 │
 ▼
Tabular Parser
 │
 ▼
Rows / Columns
 │
 ▼
Text Representation
```

## Source Code

Code can be processed using language-aware chunking strategies.

```text
Source Code
    │
    ▼
Language Parser
    │
    ▼
Functions / Classes
    │
    ▼
Code Chunks
```

---

# OCR Concepts

Scanned PDFs may not contain machine-readable text.

In such cases:

```text
Scanned PDF
    │
    ▼
OCR
    │
    ▼
Recognized Text
    │
    ▼
Cleaning
    │
    ▼
Chunking
```

OCR is especially useful for:

* Scanned documents
* Images
* Historical documents
* Forms
* Image-based PDFs

---

# Table Extraction

Tables require special handling because simply extracting text may destroy their structure.

Example:

```text
Employee | Department | Leave Days
---------|------------|-----------
John     | HR         | 20
Mary     | IT         | 18
```

A RAG system may convert this into a structured textual representation before embedding.

---

# Text Cleaning

Before chunking, extracted text should be cleaned.

Common operations include:

* Removing unnecessary whitespace
* Removing repeated line breaks
* Removing unwanted characters
* Normalizing spacing
* Removing headers/footers when appropriate
* Preserving meaningful document structure

Conceptually:

```text
Raw Text
   │
   ▼
Cleaning
   │
   ▼
Normalized Text
```

---

# Chunking

Chunking divides large documents into smaller pieces.

A complete document is usually too large to retrieve as a single unit.

```text
Large Document
      │
      ▼
   Chunking
      │
      ├── Chunk 1
      ├── Chunk 2
      ├── Chunk 3
      ├── Chunk 4
      └── Chunk N
```

The goal is to create chunks that are:

* Small enough for efficient retrieval
* Large enough to preserve meaning
* Semantically coherent
* Useful as LLM context

---

# Fixed-Size Chunking

Fixed-size chunking divides text according to a fixed number of characters or tokens.

Example:

```text
Document
   │
   ▼
500 characters
   │
   ▼
500 characters
   │
   ▼
500 characters
```

Advantages:

* Simple
* Predictable
* Easy to implement

Disadvantages:

* May split sentences
* May split concepts
* May lose semantic context

---

# Overlapping Chunks

Overlap allows adjacent chunks to share some content.

Example:

```text
Chunk 1
------------------------
A B C D E F G

Chunk 2
              E F G H I J K
              ----------------

Chunk 3
                        I J K L M N
                        ----------------
```

Overlap helps preserve context across chunk boundaries.

---

# Recursive Chunking

Recursive chunking attempts to split text using increasingly smaller separators.

Conceptually:

```text
Document
   │
   ▼
Paragraph
   │
   ▼
Sentence
   │
   ▼
Word
```

The goal is to preserve meaningful semantic boundaries before falling back to smaller units.

---

# Semantic Chunking

Semantic chunking attempts to create chunks based on meaning rather than only character or token count.

Conceptually:

```text
Document
   │
   ▼
Semantic Boundaries
   │
   ├── Topic A
   ├── Topic B
   └── Topic C
```

This can improve retrieval quality when document structure is complex.

---

# Embedding Generation

After chunking, each chunk is converted into a numerical vector.

```text
Text Chunk
    │
    ▼
Embedding Model
    │
    ▼
Vector
```

The module uses Sentence Transformers for local embedding generation.

Example model:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Embedding dimension:

```text
384
```

---

# FAISS Vector Index

The generated embeddings are stored in a FAISS index.

```text
Document Chunks
      │
      ▼
Sentence Transformer
      │
      ▼
384-dimensional vectors
      │
      ▼
FAISS Index
```

FAISS provides efficient similarity search over vectors.

---

# RAG Retrieval

Retrieval is the process of finding documents relevant to a user query.

Basic retrieval:

```text
User Query
    │
    ▼
Query Embedding
    │
    ▼
Vector Search
    │
    ▼
Top-K Documents
```

The retrieved documents become candidate context for the LLM.

---

# Top-K Retrieval

Top-K controls the number of documents returned by the retriever.

Example:

```text
Query
 │
 ▼
Vector Search
 │
 ├── Result 1
 ├── Result 2
 ├── Result 3
 ├── Result 4
 └── Result 5
```

If:

```text
top_k = 5
```

the retriever returns the five highest-ranked results.

---

# Retrieval-K vs Top-K

The module distinguishes between the initial retrieval size and the final number of results.

Example:

```text
retrieval_k = 20
        │
        ▼
20 candidate documents
        │
        ▼
Re-ranking
        │
        ▼
top_k = 5
        │
        ▼
5 final documents
```

This is important for improving final retrieval quality.

---

# RAGService

The central retrieval orchestration is implemented through the `RAGService`.

Conceptually:

```text
RAGService
    │
    ├── EmbeddingService
    │
    ├── FAISS Retrieval
    │
    └── RerankerService
```

The service is responsible for:

* Query processing
* Embedding generation
* Vector retrieval
* Retrieval-K handling
* Optional reranking
* Top-K selection
* Returning retrieval results

---

# EmbeddingService

`EmbeddingService` is responsible for generating query and document embeddings.

```text
Text
 │
 ▼
EmbeddingService
 │
 ▼
Embedding Vector
```

This separates embedding functionality from the RAG orchestration layer.

---

# Multi-Query Retrieval

A single user query may not capture all possible ways in which the required information is represented in the knowledge base.

Multi-Query Retrieval solves this by generating multiple query variations.

Basic flow:

```text
Original Query
      │
      ▼
Query Generation
      │
      ├── Query 1
      ├── Query 2
      ├── Query 3
      └── Query N
      │
      ▼
Individual Retrieval
      │
      ▼
Result Combination
      │
      ▼
Deduplication
      │
      ▼
Final Candidate Results
```

---

# Multi-Query Example

Original query:

```text
What is the employee leave policy?
```

Possible query variations:

```text
What is the employee leave policy?

What is the policy regarding employee leave?

What are the employee entitlements related to leave?
```

Each query is independently retrieved.

```text
Query 1
   │
   ▼
Results 1

Query 2
   │
   ▼
Results 2

Query 3
   │
   ▼
Results 3
```

The results are then combined.

---

# MultiQueryService

The `MultiQueryService` manages query expansion and multi-query retrieval.

Conceptually:

```text
MultiQueryService
      │
      ├── Original Query
      │
      ├── Generated Query 1
      │
      ├── Generated Query 2
      │
      └── Generated Query N
               │
               ▼
          RAG Retrieval
               │
               ▼
         Deduplicated Results
```

The implementation generates multiple query variations and retrieves documents for each variation.

---

# Multi-Query Deduplication

The same document may be returned by multiple query variations.

Example:

```text
Query 1 → Document A, Document B
Query 2 → Document B, Document C
Query 3 → Document A, Document C
```

Without deduplication:

```text
A B B C A C
```

After deduplication:

```text
A B C
```

This prevents duplicate context from consuming the LLM context window.

---

# Multi-Query Retrieval Flow

```text
                   Original Query
                         │
                         ▼
                 Query Variations
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
       Query 1        Query 2        Query 3
          │              │              │
          ▼              ▼              ▼
      Retrieval      Retrieval      Retrieval
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                    Deduplication
                         │
                         ▼
                  Candidate Results
                         │
                         ▼
                     Re-ranking
                         │
                         ▼
                    Final Context
```

---

# Reciprocal Rank Fusion

When multiple retrieval systems or query variations produce ranked lists, their results can be combined using **Reciprocal Rank Fusion (RRF)**.

Conceptually:

```text
Retriever 1
    │
    ▼
Ranked Results

Retriever 2
    │
    ▼
Ranked Results

Retriever 3
    │
    ▼
Ranked Results

       │
       ▼

Reciprocal Rank Fusion

       │
       ▼

Combined Ranking
```

RRF rewards documents that consistently appear near the top across multiple retrieval lists.

---

# Hybrid Retrieval

Hybrid retrieval combines lexical and semantic retrieval.

```text
User Query
     │
     ├───────────────┐
     ▼               ▼
Keyword Search   Dense Search
     │               │
     ▼               ▼
Keyword Results  Vector Results
     │               │
     └───────┬───────┘
             ▼
        Result Fusion
             │
             ▼
       Combined Ranking
```

Hybrid retrieval can improve retrieval quality by combining:

* Lexical precision
* Semantic understanding

---

# Self-RAG

Self-RAG is an approach where the model evaluates whether retrieval is required and whether the retrieved information is useful for producing the answer.

Traditional RAG:

```text
Query
 │
 ▼
Retrieve
 │
 ▼
Generate
```

Self-RAG:

```text
Query
 │
 ▼
Determine Retrieval Need
 │
 ├── No Retrieval
 │      │
 │      ▼
 │    Generate
 │
 └── Retrieval Required
        │
        ▼
      Retrieve
        │
        ▼
   Evaluate Context
        │
        ▼
      Generate
```

Self-RAG introduces an additional reasoning and evaluation stage around retrieval.

---

# Self-RAG Concepts

Important Self-RAG concepts include:

* Retrieval decision
* Retrieved-context evaluation
* Relevance assessment
* Grounded generation
* Self-evaluation
* Iterative retrieval

The purpose is to avoid blindly using retrieved documents when they are not useful.

---

# Corrective RAG

Corrective RAG, commonly referred to as **CRAG**, introduces a corrective step when retrieved documents are insufficient or low quality.

Traditional RAG:

```text
Query
 │
 ▼
Retrieve
 │
 ▼
Generate
```

Corrective RAG:

```text
Query
 │
 ▼
Retrieve
 │
 ▼
Evaluate Retrieval
 │
 ├── Relevant
 │      │
 │      ▼
 │   Generate
 │
 └── Not Relevant
        │
        ▼
     Correction
        │
        ├── Improved Retrieval
        ├── Alternative Search
        └── External Knowledge
        │
        ▼
      Generate
```

---

# CRAG Retrieval Evaluation

The retrieval result can conceptually be classified as:

```text
Relevant
    │
    ▼
Use Retrieved Context

Ambiguous
    │
    ▼
Perform Additional Retrieval

Irrelevant
    │
    ▼
Correct Retrieval Strategy
```

The purpose is to prevent low-quality retrieval results from directly reaching the generation stage.

---

# Reranking

Vector search provides an initial ranking.

However, the first ranking may not always produce the best semantic ordering.

Reranking introduces a second-stage ranking process.

```text
Query
 │
 ▼
Vector Retrieval
 │
 ▼
Top 20 Candidates
 │
 ▼
Reranker
 │
 ▼
Top 5 Relevant Documents
```

This is called **two-stage retrieval**.

---

# Two-Stage Retrieval

```text
Stage 1
───────

Fast Retriever
     │
     ▼
Candidate Documents
     │
     ▼
Top 20


Stage 2
───────

Reranker
     │
     ▼
Relevance Scoring
     │
     ▼
Top 5
```

The first stage prioritizes retrieval speed.

The second stage prioritizes relevance.

---

# Bi-Encoder

A Bi-Encoder encodes the query and document independently.

```text
Query
 │
 ▼
Encoder
 │
 ▼
Query Vector


Document
 │
 ▼
Encoder
 │
 ▼
Document Vector
```

Similarity is calculated between the two vectors.

Advantages:

* Fast
* Efficient
* Suitable for large-scale retrieval
* Embeddings can be precomputed

Disadvantage:

* Query-document interaction is limited

---

# Cross-Encoder

A Cross-Encoder processes the query and document together.

```text
Query
   │
   ├─────────────┐
   │             │
   ▼             ▼
             Document
       \       /
        \     /
         ▼   ▼
       Cross-Encoder
             │
             ▼
       Relevance Score
```

The model directly evaluates the relationship between the query and document.

Advantages:

* Better relevance understanding
* Stronger ranking quality

Disadvantage:

* More computationally expensive
* Slower than Bi-Encoder retrieval

---

# Bi-Encoder vs Cross-Encoder

| Feature               | Bi-Encoder            | Cross-Encoder          |
| --------------------- | --------------------- | ---------------------- |
| Query encoding        | Separate              | Together with document |
| Document encoding     | Separate              | Together with query    |
| Speed                 | Fast                  | Slower                 |
| Large-scale retrieval | Excellent             | Expensive              |
| Ranking quality       | Good                  | Usually better         |
| Typical usage         | First-stage retrieval | Second-stage reranking |

Typical production architecture:

```text
Bi-Encoder
    │
    ▼
Fast Retrieval
    │
    ▼
Candidate Documents
    │
    ▼
Cross-Encoder
    │
    ▼
Final Ranking
```

---

# RerankerService

The `RerankerService` is responsible for second-stage ranking.

Conceptually:

```text
RerankerService
       │
       ├── Query
       │
       ├── Candidate Documents
       │
       ▼
Relevance Scoring
       │
       ▼
Sorted Results
```

The service allows the RAG pipeline to keep retrieval and reranking responsibilities separate.

---

# FlashRank

FlashRank is used for lightweight local reranking.

The module uses:

```text
FlashRank
```

for local reranking experiments.

The installed package version used during the implementation is:

```text
FlashRank 0.2.10
```

---

# FlashRank Reranking Flow

```text
User Query
    │
    ▼
FAISS Retrieval
    │
    ▼
Candidate Documents
    │
    ▼
FlashRank
    │
    ▼
Rerank Scores
    │
    ▼
Sorted Documents
```

FlashRank provides a lightweight option for experimenting with reranking without requiring an external reranking API.

---

# Cohere Rerank

The module also covers the concept of using the **Cohere Rerank API** for production-oriented reranking.

Conceptually:

```text
Query
 │
 ▼
Vector Retrieval
 │
 ▼
Candidate Documents
 │
 ▼
Cohere Rerank
 │
 ▼
Relevance Scores
 │
 ▼
Top Documents
```

Advantages include:

* Dedicated reranking models
* Strong query-document relevance scoring
* Managed API
* Production-oriented integration

The Cohere implementation is covered as a reranking technology and architecture option.

---

# BGE Reranker

The module also covers **BGE Reranker** models.

BGE reranking can be used as a local second-stage ranking model.

Conceptually:

```text
Query
 │
 ▼
Retriever
 │
 ▼
Candidate Documents
 │
 ▼
BGE Reranker
 │
 ▼
Relevance Scores
 │
 ▼
Final Ranking
```

This provides another alternative to managed reranking APIs.

---

# Reranking Architecture Comparison

| Technology    | Type                          | Execution | Typical Usage                |
| ------------- | ----------------------------- | --------- | ---------------------------- |
| FlashRank     | Reranker                      | Local     | Lightweight reranking        |
| BGE Reranker  | Cross-Encoder style reranking | Local     | Higher-quality local ranking |
| Cohere Rerank | Managed reranking API         | Cloud     | Production API-based ranking |

---

# RAGService with Reranking

The RAG service supports optional reranking.

Conceptually:

```text
RAGService
    │
    ▼
EmbeddingService
    │
    ▼
FAISS Retrieval
    │
    ▼
retrieval_k
    │
    ▼
RerankerService
    │
    ▼
top_k
    │
    ▼
Final Results
```

The retrieval pipeline can therefore operate with or without reranking.

---

# RAG Retrieval Parameters

Important parameters include:

```text
query
top_k
rerank
retrieval_k
```

Example:

```text
query = "What is the employee leave policy?"

retrieval_k = 20

rerank = true

top_k = 5
```

Flow:

```text
Query
 │
 ▼
Retrieve 20
 │
 ▼
Rerank 20
 │
 ▼
Return Top 5
```

---

# Retrieval Without Reranking

```text
Query
 │
 ▼
Embedding
 │
 ▼
FAISS
 │
 ▼
Top-K
 │
 ▼
Results
```

---

# Retrieval With Reranking

```text
Query
 │
 ▼
Embedding
 │
 ▼
FAISS
 │
 ▼
Retrieval-K Candidates
 │
 ▼
Reranker
 │
 ▼
Top-K
 │
 ▼
Results
```

The second approach generally provides a stronger ranking stage.

---

# Context Augmentation

After retrieval and reranking, the selected documents are added to the LLM prompt.

```text
User Query
     │
     ▼
Retrieved Documents
     │
     ▼
Context Builder
     │
     ▼
Prompt
     │
     ▼
LLM
```

Example conceptual prompt:

```text
Use the following context to answer the question.

Context:
<retrieved documents>

Question:
<user question>

Answer:
```

---

# Grounded Generation

The purpose of grounded generation is to make the LLM answer using the retrieved context.

```text
Retrieved Context
       │
       ▼
      LLM
       │
       ▼
Grounded Answer
```

The system should avoid introducing unsupported information.

---

# Source Attribution

A production RAG system should provide the sources used to construct the answer.

Conceptually:

```text
Answer
   │
   ├── Source 1
   ├── Source 2
   └── Source 3
```

This improves:

* Transparency
* Traceability
* User trust
* Debugging
* Retrieval evaluation

---

# Complete Advanced RAG Architecture

```text
                         User Query
                              │
                              ▼
                       Query Processing
                              │
                              ▼
                       Multi-Query
                              │
                 ┌────────────┼────────────┐
                 │            │            │
                 ▼            ▼            ▼
              Query 1      Query 2      Query 3
                 │            │            │
                 └────────────┼────────────┘
                              ▼
                         FAISS Search
                              │
                              ▼
                       Candidate Results
                              │
                              ▼
                       Deduplication
                              │
                              ▼
                          Reranker
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
             Relevant                 Irrelevant
                 │                         │
                 │                         ▼
                 │                       CRAG
                 │                         │
                 │                         ▼
                 │                  Correct Retrieval
                 │                         │
                 └────────────┬────────────┘
                              ▼
                         Final Context
                              │
                              ▼
                             LLM
                              │
                              ▼
                        Generated Answer
                              │
                              ▼
                       Source Attribution
```

---

# Ollama

The module uses **Ollama** for local LLM experimentation.

Ollama provides a local runtime for running compatible Large Language Models.

Conceptually:

```text
RAG Context
     │
     ▼
Ollama
     │
     ▼
Local LLM
     │
     ▼
Generated Answer
```

---

# Llama 3.2

The local LLM used for generation experiments is:

```text
llama3.2:3b
```

The model can be executed through Ollama.

Conceptually:

```text
Retrieved Context
       │
       ▼
Llama 3.2 3B
       │
       ▼
Final Answer
```

Using a local model allows the RAG generation stage to be tested without requiring every generation request to use an external hosted model.

---

# RAG Generation Flow

```text
User Query
    │
    ▼
Multi-Query Retrieval
    │
    ▼
Candidate Documents
    │
    ▼
Reranking
    │
    ▼
Top Documents
    │
    ▼
Context Construction
    │
    ▼
Llama 3.2
    │
    ▼
Generated Answer
```

---

# FastAPI Architecture

The module follows a service-based FastAPI architecture.

```text
                    FastAPI
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
      Ingestion      RAG API     Reranking API
          │            │            │
          │            │            │
          ▼            ▼            ▼
     Ingestion      RAGService  RerankerService
      Service
                       │
              ┌────────┴────────┐
              │                 │
              ▼                 ▼
      EmbeddingService       FAISS
              │
              ▼
       Sentence Transformer
```

---

# Service Responsibilities

| Service             | Responsibility                                  |
| ------------------- | ----------------------------------------------- |
| `EmbeddingService`  | Generate embeddings                             |
| `IngestionService`  | Load and process documents                      |
| `ChunkingService`   | Split documents into chunks                     |
| `RAGService`        | Orchestrate retrieval                           |
| `MultiQueryService` | Generate query variations and combine retrieval |
| `RerankerService`   | Re-rank retrieved documents                     |

---

# SOLID Principles

The architecture follows SOLID principles.

## Single Responsibility

Each service has one major responsibility.

```text
EmbeddingService
    → Embeddings

RerankerService
    → Reranking

MultiQueryService
    → Multi-query retrieval

RAGService
    → RAG orchestration
```

## Dependency Inversion

The business logic is separated from infrastructure-specific implementation details.

This makes the system easier to:

* Test
* Extend
* Replace components
* Maintain

---

# RAG API

The RAG API provides a single entry point for retrieval operations.

Conceptually:

```text
POST /rag/query
```

Request:

```json
{
  "query": "What is the employee leave policy?",
  "top_k": 5,
  "rerank": true,
  "retrieval_k": 20
}
```

Conceptually:

```text
Request
   │
   ▼
RAG API
   │
   ▼
RAGService
   │
   ├── EmbeddingService
   │
   ├── FAISS
   │
   └── RerankerService
   │
   ▼
Response
```

---

# Multi-Query API

The multi-query functionality can be exposed through a dedicated API.

Conceptually:

```text
POST /rag/multi-query
```

The API accepts the original query and performs:

```text
Original Query
      │
      ▼
Query Expansion
      │
      ▼
Multiple Retrievals
      │
      ▼
Deduplication
      │
      ▼
Results
```

---

# Reranking API

The reranking functionality can be exposed independently for testing.

Conceptually:

```text
POST /rag/rerank
```

Flow:

```text
Query
 │
 ▼
Candidate Documents
 │
 ▼
RerankerService
 │
 ▼
Ranked Results
```

---

# Multi-Query Testing

The multi-query retrieval implementation was tested using a sample query.

Example:

```text
What is the employee leave policy?
```

The system generates multiple query variations.

Example:

```text
Original Query

What is the employee leave policy?

Variation 1

What is the policy regarding:
What is the employee leave policy?

Variation 2

What are the employee entitlements related to:
What is the employee leave policy?
```

Each variation is sent through retrieval.

The results are then combined and deduplicated.

---

# Reranking Testing

The RAG pipeline was also tested with reranking enabled.

Conceptually:

```text
Query
 │
 ▼
FAISS
 │
 ▼
Candidate Results
 │
 ▼
FlashRank
 │
 ▼
Reranked Results
```

The test verified the integration between:

```text
RAGService
    │
    ├── EmbeddingService
    │
    ├── FAISS
    │
    └── RerankerService
```

---

# Retrieval Score

Initial vector retrieval and reranking use different scoring mechanisms.

Vector retrieval may return:

```text
distance
```

or similarity values depending on the index and configuration.

Reranking can return:

```text
rerank_score
```

These scores should not be assumed to be directly comparable because they originate from different scoring systems.

---

# Retrieval Quality

Retrieval quality is one of the most important factors in RAG.

Poor retrieval:

```text
Query
 │
 ▼
Wrong Documents
 │
 ▼
LLM
 │
 ▼
Incorrect Answer
```

Good retrieval:

```text
Query
 │
 ▼
Relevant Documents
 │
 ▼
LLM
 │
 ▼
Grounded Answer
```

This is why advanced retrieval techniques are important.

---

# RAG Evaluation

A RAG system should be evaluated at multiple levels.

## Retrieval Evaluation

Important retrieval metrics include:

* Precision
* Recall
* Hit Rate
* MRR
* Context Relevance
* Context Recall

## Generation Evaluation

Important generation metrics include:

* Faithfulness
* Answer Relevance
* Context Utilization
* Groundedness

---

# RAGAS

The module introduces the concepts behind **RAGAS** for evaluating RAG pipelines.

Conceptually:

```text
Question
   │
   ├── Retrieved Context
   │
   └── Generated Answer
             │
             ▼
           RAGAS
             │
      ┌──────┼──────┐
      │      │      │
      ▼      ▼      ▼
 Context  Faithfulness  Answer
 Relevance              Relevance
```

RAGAS can be used to evaluate the quality of retrieval and generation separately.

---

# RAG Evaluation Pipeline

```text
Test Questions
      │
      ▼
RAG Pipeline
      │
      ▼
Retrieved Context
      │
      ▼
Generated Answers
      │
      ▼
Evaluation
      │
      ├── Retrieval Quality
      ├── Context Relevance
      ├── Faithfulness
      └── Answer Relevance
```

---

# Advanced Retrieval Comparison

| Technique         | Primary Purpose                             |
| ----------------- | ------------------------------------------- |
| Dense Retrieval   | Semantic retrieval                          |
| Keyword Retrieval | Exact/lexical retrieval                     |
| Hybrid Retrieval  | Combine lexical + semantic retrieval        |
| Multi-Query       | Improve query coverage                      |
| RRF               | Combine ranked retrieval results            |
| Reranking         | Improve candidate ordering                  |
| Self-RAG          | Evaluate retrieval necessity and usefulness |
| CRAG              | Correct poor retrieval                      |
| Cross-Encoder     | High-quality query-document scoring         |
| FlashRank         | Lightweight local reranking                 |
| BGE Reranker      | Local high-quality reranking                |
| Cohere Rerank     | Managed reranking service                   |

---

# Traditional RAG vs Advanced RAG

## Traditional RAG

```text
Query
 │
 ▼
Embedding
 │
 ▼
Vector Search
 │
 ▼
Top-K
 │
 ▼
LLM
```

## Advanced RAG

```text
Query
 │
 ▼
Query Expansion
 │
 ▼
Multi-Query Retrieval
 │
 ▼
Candidate Pool
 │
 ▼
Deduplication
 │
 ▼
Hybrid / Dense Retrieval
 │
 ▼
Reranking
 │
 ▼
Relevance Evaluation
 │
 ▼
Correction if Required
 │
 ▼
Context Construction
 │
 ▼
LLM
 │
 ▼
Grounded Answer
 │
 ▼
Sources
```

---

# Module 6 Architecture

```text
                         FastAPI
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
   Ingestion API         RAG API          Reranking API
        │                   │                   │
        ▼                   ▼                   ▼
 IngestionService       RAGService       RerankerService
        │                   │                   │
        ▼                   ├───────────────────┤
    Chunking                │                   │
        │                   ▼                   ▼
        ▼            MultiQueryService    EmbeddingService
        │                   │                   │
        └───────────────────┤                   ▼
                            │             Sentence Transformer
                            │                   │
                            ▼                   ▼
                         FAISS              Embeddings
                            │
                            ▼
                       Candidate Results
                            │
                            ▼
                         Reranking
                            │
                            ▼
                      Final Context
                            │
                            ▼
                          Ollama
                            │
                            ▼
                       Llama 3.2
                            │
                            ▼
                    Grounded Response
                            │
                            ▼
                    Source Attribution
```

---

# Complete Project Flow

```text
                         Documents
                             │
                             ▼
                       Document Loader
                             │
                             ▼
                          Parser
                             │
                             ▼
                       Text Cleaning
                             │
                             ▼
                          Chunking
                             │
                             ▼
                   Sentence Transformer
                             │
                             ▼
                        Embeddings
                             │
                             ▼
                           FAISS
                             │
                             ▼
                        User Query
                             │
                             ▼
                      Multi-Query
                             │
                             ▼
                   Multiple Query Results
                             │
                             ▼
                       Deduplication
                             │
                             ▼
                    Candidate Documents
                             │
                             ▼
                        Reranking
                             │
                             ▼
                      Relevant Context
                             │
                             ▼
                         CRAG Check
                             │
                 ┌───────────┴───────────┐
                 │                       │
                 ▼                       ▼
              Relevant              Not Relevant
                 │                       │
                 │                       ▼
                 │                   Correction
                 │                       │
                 └───────────┬───────────┘
                             ▼
                       Context Builder
                             │
                             ▼
                           Ollama
                             │
                             ▼
                        Llama 3.2
                             │
                             ▼
                       Final Answer
                             │
                             ▼
                     Source Attribution
                             │
                             ▼
                         Evaluation
```

---

# API Endpoints

## RAG APIs

| Method | Endpoint           | Description                   |
| ------ | ------------------ | ----------------------------- |
| POST   | `/rag/query`       | Perform RAG retrieval         |
| POST   | `/rag/multi-query` | Perform multi-query retrieval |
| POST   | `/rag/rerank`      | Rerank candidate documents    |

---

# RAG Query Parameters

The RAG service supports parameters conceptually represented by:

| Parameter     | Purpose                      |
| ------------- | ---------------------------- |
| `query`       | User question                |
| `top_k`       | Number of final results      |
| `retrieval_k` | Number of initial candidates |
| `rerank`      | Enable/disable reranking     |

Example:

```json
{
  "query": "What is the employee leave policy?",
  "top_k": 5,
  "retrieval_k": 20,
  "rerank": true
}
```

---

# Configuration

Create a `.env` file containing the required configuration.

Example:

```text
# Embedding

EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
EMBEDDING_DIMENSION=384

# FAISS

FAISS_INDEX_PATH=./faiss
FAISS_INDEX_FILE=./faiss/index.faiss

# RAG

TOP_K=5
RETRIEVAL_K=20

# Ollama

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2:3b

# Optional External Models

OPENAI_API_KEY=
COHERE_API_KEY=
```

The local Sentence Transformer model is used for embedding generation.

Ollama is used for local LLM generation experiments.

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
python -m uvicorn app.main:app --reload
```

If the project is configured for a specific port:

```powershell
python -m uvicorn app.main:app --reload --port 8006
```

Swagger UI:

```text
http://127.0.0.1:8006/docs
```

OpenAPI:

```text
http://127.0.0.1:8006/openapi.json
```

---

# Ollama

Start the local Ollama model:

```powershell
ollama run llama3.2:3b
```

The RAG application can then use the local model for generation.

Conceptually:

```text
FastAPI
   │
   ▼
RAGService
   │
   ▼
Retrieved Context
   │
   ▼
Ollama
   │
   ▼
Llama 3.2 3B
   │
   ▼
Answer
```

---

# Requirements

The project requires the major dependencies used by the implementation.

Example:

```text
fastapi
uvicorn
pydantic
pydantic-settings
python-dotenv
numpy
faiss-cpu
sentence-transformers
transformers
PyMuPDF
pdfplumber
flashrank
ollama
openai
cohere
```

---

# Production Concepts Covered

This module provides practical exposure to:

* End-to-end RAG architecture
* Document ingestion
* Document parsing
* PDF processing
* Text extraction
* OCR concepts
* Table extraction
* Text cleaning
* Chunking
* Overlapping chunks
* Recursive chunking
* Semantic chunking concepts
* Embedding generation
* Dense retrieval
* Multi-query retrieval
* Query expansion
* Result deduplication
* Hybrid retrieval
* Reciprocal Rank Fusion
* Two-stage retrieval
* Reranking
* Cross-Encoder
* Bi-Encoder
* FlashRank
* BGE Reranker
* Cohere Rerank
* Self-RAG
* Corrective RAG
* Context augmentation
* Grounded generation
* Source attribution
* Local LLM generation
* Ollama
* Llama 3.2
* Retrieval evaluation
* RAG evaluation
* RAGAS concepts
* FastAPI service architecture
* SOLID principles
* Layered architecture

---

# Learning Outcomes

After completing Module 6, I learned:

* What RAG architecture is
* How retrieval and generation work together
* How documents are ingested
* How PDFs can be parsed
* PyMuPDF
* pdfplumber
* DOCX processing concepts
* HTML processing concepts
* CSV and Excel processing concepts
* Source-code processing concepts
* OCR concepts
* Table extraction concepts
* Text cleaning
* Fixed-size chunking
* Overlapping chunks
* Recursive chunking
* Semantic chunking concepts
* Embedding generation
* Sentence Transformers
* FAISS retrieval
* Dense vector search
* Top-K retrieval
* Retrieval-K
* Multi-Query Retrieval
* Query expansion
* Query variation generation
* Multi-query deduplication
* Hybrid retrieval
* Reciprocal Rank Fusion
* Self-RAG
* Corrective RAG
* Reranking
* Two-stage retrieval
* Bi-Encoder architecture
* Cross-Encoder architecture
* Cross-Encoder vs Bi-Encoder
* Cohere Rerank
* BGE Reranker
* FlashRank
* RerankerService
* RAGService
* EmbeddingService
* Context augmentation
* Grounded generation
* Source attribution
* Ollama
* Llama 3.2
* RAG evaluation
* RAGAS concepts
* FastAPI integration
* REST API design
* SOLID principles
* Layered architecture

---

# Module 6 Completion Status

| Topic                           | Status    |
| ------------------------------- | --------- |
| RAG Architecture                | Completed |
| Document Ingestion              | Completed |
| PDF Ingestion                   | Completed |
| PyMuPDF                         | Covered   |
| pdfplumber                      | Covered   |
| DOCX Processing                 | Covered   |
| HTML Processing                 | Covered   |
| CSV / Excel Processing          | Covered   |
| OCR Concepts                    | Covered   |
| Table Extraction                | Covered   |
| Text Cleaning                   | Completed |
| Chunking                        | Completed |
| Overlapping Chunks              | Covered   |
| Recursive Chunking              | Covered   |
| Semantic Chunking               | Covered   |
| Sentence Transformer Embeddings | Completed |
| FAISS Retrieval                 | Completed |
| Dense Retrieval                 | Completed |
| Top-K Retrieval                 | Completed |
| Retrieval-K                     | Completed |
| RAGService                      | Completed |
| EmbeddingService                | Completed |
| Multi-Query Retrieval           | Completed |
| Query Expansion                 | Completed |
| Query Deduplication             | Completed |
| Hybrid Retrieval                | Covered   |
| Reciprocal Rank Fusion          | Covered   |
| Reranking                       | Completed |
| RerankerService                 | Completed |
| FlashRank                       | Completed |
| Cross-Encoder                   | Covered   |
| Bi-Encoder                      | Covered   |
| Cohere Rerank                   | Covered   |
| BGE Reranker                    | Covered   |
| Self-RAG                        | Covered   |
| Corrective RAG                  | Covered   |
| Context Augmentation            | Completed |
| Grounded Generation             | Completed |
| Source Attribution              | Completed |
| Ollama                          | Completed |
| Llama 3.2 3B                    | Completed |
| RAG Evaluation                  | Covered   |
| RAGAS                           | Covered   |
| FastAPI Integration             | Completed |
| SOLID Architecture              | Completed |

---

# Module 6 Architecture Summary

The complete architecture can be summarized as:

```text
                     DOCUMENTS
                         │
                         ▼
                  INGESTION / PARSING
                         │
                         ▼
                      CHUNKING
                         │
                         ▼
                  EMBEDDING MODEL
                         │
                         ▼
                       FAISS
                         │
                         ▼
                     USER QUERY
                         │
                         ▼
                  MULTI-QUERY
                         │
             ┌───────────┼───────────┐
             │           │           │
             ▼           ▼           ▼
          Query 1     Query 2     Query 3
             │           │           │
             └───────────┼───────────┘
                         ▼
                    RETRIEVAL
                         │
                         ▼
                   DEDUPLICATION
                         │
                         ▼
                    RERANKING
                         │
          ┌──────────────┴──────────────┐
          │                             │
          ▼                             ▼
       Relevant                    Not Relevant
          │                             │
          │                             ▼
          │                           CRAG
          │                             │
          │                             ▼
          │                      Correct Retrieval
          │                             │
          └──────────────┬──────────────┘
                         ▼
                   FINAL CONTEXT
                         │
                         ▼
                       OLLAMA
                         │
                         ▼
                    LLAMA 3.2
                         │
                         ▼
                 GROUNDED ANSWER
                         │
                         ▼
                SOURCE ATTRIBUTION
                         │
                         ▼
                     EVALUATION
```

---

# Module 5 → Module 6 Progression

Module 5 focused primarily on **vector databases and similarity search**.

```text
Module 5

Documents
    │
    ▼
Embeddings
    │
    ▼
Vector Databases
    │
    ├── ChromaDB
    ├── Qdrant
    └── FAISS
    │
    ▼
Similarity Search
```

Module 6 builds the complete RAG intelligence layer on top of those concepts.

```text
Module 6

Documents
    │
    ▼
Ingestion
    │
    ▼
Chunking
    │
    ▼
Embeddings
    │
    ▼
FAISS
    │
    ▼
Advanced Retrieval
    │
    ├── Multi-Query
    ├── Hybrid Search
    ├── RRF
    ├── Self-RAG
    ├── CRAG
    └── Reranking
    │
    ▼
Context
    │
    ▼
LLM
    │
    ▼
Grounded Answer
    │
    ▼
Evaluation
```

---

# Technology Comparison

| Technology            | Primary Purpose          | Usage                           |
| --------------------- | ------------------------ | ------------------------------- |
| Sentence Transformers | Embedding generation     | Local embeddings                |
| FAISS                 | Vector similarity search | Dense retrieval                 |
| Multi-Query           | Query expansion          | Retrieval improvement           |
| RRF                   | Rank fusion              | Combining retrieval results     |
| FlashRank             | Reranking                | Local lightweight reranking     |
| BGE Reranker          | Reranking                | Local high-quality ranking      |
| Cohere Rerank         | Reranking                | Managed cloud reranking         |
| Ollama                | Local model runtime      | LLM generation                  |
| Llama 3.2             | LLM                      | Local answer generation         |
| RAGAS                 | RAG evaluation           | Retrieval/generation evaluation |

---

# Future Enhancements

Potential future topics include:

* Advanced semantic chunking
* Parent-child retrieval
* Contextual retrieval
* Hierarchical retrieval
* Knowledge graph RAG
* Graph RAG
* Query routing
* Agentic RAG
* Adaptive RAG
* Production RAG evaluation
* Retrieval benchmarking
* Vector database benchmarking
* Advanced RRF strategies
* Advanced reranking models
* Fine-tuned embedding models
* Fine-tuned rerankers
* Streaming RAG responses
* RAG caching
* Production observability
* RAG tracing
* Latency optimization
* Cost optimization
* Production-scale RAG deployment

---

# Git

The project is maintained using Git and the completed Module 6 implementation is committed to the repository.

Typical workflow:

```powershell
git status

git add .

git commit -m "Complete Module 6 advanced retrieval and RAG implementation"

git push
```

---

# Module 6 Summary

Module 6 moves from basic vector search into **production-oriented RAG architecture**.

The learning progression is:

```text
Vector Search
      │
      ▼
Basic Retrieval
      │
      ▼
Multi-Query Retrieval
      │
      ▼
Hybrid Retrieval
      │
      ▼
Result Fusion
      │
      ▼
Reranking
      │
      ▼
Self-RAG / CRAG
      │
      ▼
Context Augmentation
      │
      ▼
LLM Generation
      │
      ▼
Grounded Answers
      │
      ▼
Evaluation
```

The key objective of this module is to understand that **RAG quality depends not only on the LLM, but heavily on document preparation, chunking, retrieval quality, query formulation, reranking, context selection, and evaluation**.

---

# Author

**Ramesh Srinivasan**

Generative AI Cross-Skilling Journey
