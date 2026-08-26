# Module 14 - Caching and Cost Optimization

## Overview

Module 14 focuses on reducing LLM latency, token consumption, model cost, and unnecessary model calls through caching, semantic similarity, model routing, prompt compression, and cost-aware generation strategies.

The module uses the local **Ollama `llama3.2:3b`** model wherever practical and builds the optimization concepts incrementally.

The overall optimization pipeline is:

```text
User Request
     |
     v
Exact Cache
     |
     +---- HIT ----> Return Cached Response
     |
     +---- MISS
             |
             v
       Semantic Cache
             |
             +---- HIT ----> Return Cached Response
             |
             +---- MISS
                     |
                     v
               Prompt Compression
                     |
                     v
                Task Classifier
                     |
             +-------+-------+
             |               |
          Simple          Complex
             |               |
             v               v
        Cheap Model     Powerful Model
             |               |
             +-------+-------+
                     |
                Quality Check
                     |
             +-------+-------+
             |               |
           Good            Poor
             |               |
          Return        Escalate
                             |
                             v
                      Powerful Model
```

---

# Learning Objectives

By the end of this module, you will understand:

* Why LLM caching is important
* Exact-match caching
* Prompt hashing
* Redis-based cache architecture
* Cache TTL
* Cache invalidation
* Semantic caching
* Embedding-based similarity
* Similarity threshold tuning
* GPTCache architecture
* Redis vector-cache architecture
* Cache hit-rate measurement
* LiteLLM unified model access
* Model routing
* Budget management
* Fallback chains
* API-key rotation concepts
* Cost tracking
* LLMLingua
* LongLLMLingua
* Extractive compression
* Abstractive compression
* Compression-ratio vs quality trade-offs
* Task-complexity classification
* Cheap-model-first routing
* Powerful-model routing
* Cascading and escalation

---

# Environment

```text
Python 3.13.15
Ollama
llama3.2:3b
```

Additional libraries are installed progressively as each hands-on is introduced.

---

# Project Structure

```text
Module14Handson/
│
├── .venv/
│
├── app/
│   ├── __init__.py
│   │
│   ├── cache/
│   │   ├── __init__.py
│   │   ├── exact_cache.py
│   │   ├── redis_exact_cache.py
│   │   ├── local_exact_cache.py
│   │   └── cache_factory.py
│   │
│   ├── semantic_cache/
│   │   ├── __init__.py
│   │   ├── embedding_service.py
│   │   └── semantic_cache.py
│   │
│   ├── routing/
│   │   ├── __init__.py
│   │   ├── litellm_service.py
│   │   ├── model_router.py
│   │   ├── fallback_router.py
│   │   ├── key_rotator.py
│   │   ├── complexity_classifier.py
│   │   ├── cost_aware_router.py
│   │   ├── response_quality.py
│   │   ├── cascade_router.py
│   │   └── model_generation.py
│   │
│   ├── compression/
│   │   ├── __init__.py
│   │   ├── extractive.py
│   │   ├── abstractive.py
│   │   ├── metrics.py
│   │   ├── quality.py
│   │   └── llmlingua_compressor.py
│   │
│   ├── cost/
│   │   ├── __init__.py
│   │   ├── budget_manager.py
│   │   └── litellm_cost.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── llm_benchmark.py
│   │   ├── cached_benchmark.py
│   │   ├── cached_llm.py
│   │   └── semantic_cached_llm.py
│   │
│   └── config/
│       ├── __init__.py
│       └── cache_config.py
│
├── tests/
│   ├── test_cache_baseline.py
│   ├── test_exact_cache.py
│   ├── test_semantic_cache.py
│   ├── test_thresholds.py
│   ├── test_semantic_hit_rate.py
│   ├── test_litellm_basic.py
│   ├── test_litellm_fallback.py
│   ├── test_litellm_routing.py
│   ├── test_extractive_compression.py
│   ├── test_abstractive_compression.py
│   ├── test_compression_tradeoff.py
│   ├── test_complexity_classifier.py
│   ├── test_model_router.py
│   └── test_cascading.py
│
├── data/
├── logs/
│
├── .gitignore
├── README.md
├── requirements.txt
└── main.py
```

---

# Topic 1 - Why Caching is Critical

## 1.1 LLM Calls Are Slow and Expensive

Repeated requests cause repeated model inference.

Even with local Ollama, repeated model calls consume:

* Processing time
* CPU/GPU resources
* Tokens
* Memory
* Latency

For hosted paid models, repeated calls can also directly increase cost.

## 1.2 Semantically Similar Queries Are Common

These queries are different strings:

```text
What is RAG?
```

and:

```text
Explain Retrieval-Augmented Generation.
```

but can have the same intent.

Exact caching cannot identify them as equivalent. Semantic caching can.

## 1.3 Measuring Cache Benefit

The baseline experiment compares:

```text
Without cache
    ↓
LLM called for every request
```

with:

```text
With exact cache
    ↓
First request → LLM
Repeated requests → Cache
```

Metrics include:

```text
Request count
LLM calls
Latency
Token usage
Cache hit rate
```

Test:

```powershell
python -m tests.test_cache_baseline
```

---

# Topic 2 - Exact-Match Caching

## 2.1 Prompt Hashing

Prompts are normalized and hashed with SHA-256.

Example:

```text
"What is RAG?"
```

and:

```text
"  WHAT IS RAG?  "
```

normalize to the same cache representation.

The cache key also includes the model so responses generated by different models are not mixed.

## 2.2 Redis

The project includes:

```text
RedisExactCache
```

for Redis-backed caching.

Keys use the pattern:

```text
module14:exact:<sha256>
```

The implementation stores:

```text
response
model
created_at
input_tokens
output_tokens
```

## 2.3 TTL

The default TTL is:

```text
300 seconds
```

After expiry, the next request causes a cache miss and fresh model generation.

## 2.4 Cache Invalidation

The implementation supports:

* Invalidate one entry
* Invalidate all entries
* Natural invalidation through TTL

The project also makes the cache key model-aware to avoid stale responses across different models.

### Redis runtime note

The Redis implementation is included, but the local Windows Redis runtime was not available in this environment. Therefore a local in-memory fallback is included so the hands-on remains runnable without Docker/Redis.

Test:

```powershell
python -m tests.test_exact_cache
```

---

# Topic 3 - Semantic Caching

## 3.1 How Semantic Caching Works

The query is converted into an embedding:

```text
Query
 ↓
Embedding
 ↓
Similarity Search
 ↓
Threshold
 ↓
Hit / Miss
```

Semantically similar queries can reuse an existing response.

## 3.2 GPTCache

GPTCache was covered as an open-source semantic-cache architecture.

Conceptually:

```text
Application
    ↓
GPTCache
    ├── Embeddings
    ├── Similarity
    ├── Cache Storage
    └── LLM
```

The underlying mechanism was implemented manually first to demonstrate the concepts without making the library a prerequisite.

## 3.3 Redis Vector Architecture

A production implementation can store:

```text
query
embedding
response
model
metadata
TTL
```

and perform vector similarity search inside Redis.

## 3.4 Similarity Threshold

Example:

```text
0.90+ → strongly similar
0.80+ → potentially similar
lower → increasingly risky
```

The actual threshold must be tuned against representative application queries.

A low threshold can create false cache hits.

A high threshold can produce too many misses.

## 3.5 Cache Hit Rate

Measured as:

```text
semantic hits
----------------------------
total semantic-cache requests
```

Additional useful metrics:

```text
LLM calls avoided
Token savings
Latency savings
False-hit rate
```

Tests:

```powershell
python -m tests.test_semantic_cache
```

```powershell
python -m tests.test_thresholds
```

```powershell
python -m tests.test_semantic_hit_rate
```

---

# Topic 4 - LiteLLM

## 4.1 Unified Interface

LiteLLM provides a common model-calling interface so the application does not have to embed separate provider SDK patterns everywhere.

In this module the local model is:

```text
ollama/llama3.2:3b
```

## 4.2 Model Routing

The routing layer classifies requests and chooses a model role.

Example:

```text
Simple
 ↓
Cheap Model
```

```text
Complex
 ↓
Powerful Model
```

## 4.3 Budget Management

The project includes project/user/feature budget tracking.

Example:

```text
Project budget
User budget
Feature budget
```

The request is allowed only when the applicable budgets have sufficient remaining capacity.

## 4.4 Fallback Chains

Models can be tried in sequence:

```text
Model A
 ↓ failure
Model B
 ↓ failure
Model C
```

The implementation records failed attempts.

## 4.5 API-Key Rotation

A round-robin key router demonstrates:

```text
Key A
Key B
Key C
Key A
Key B
Key C
```

This is primarily relevant to hosted providers. It has no practical purpose for the local Ollama model.

## 4.6 Cost Tracking

The implementation tracks:

```text
User
Project
Feature
Model
Input tokens
Output tokens
Estimated cost
```

For local Ollama:

```text
Estimated provider cost = 0
```

Tests:

```powershell
python -m tests.test_litellm_basic
```

```powershell
python -m tests.test_litellm_fallback
```

```powershell
python -m tests.test_litellm_routing
```

---

# Topic 5 - Prompt Compression

## 5.1 LLMLingua

LLMLingua compresses prompts by removing redundant content while attempting to preserve task-critical information.

The project includes:

```text
LLMLinguaCompressor
```

using the `PromptCompressor` interface.

## 5.2 LongLLMLingua

LongLLMLingua extends the compression strategy for long-context scenarios with techniques such as:

* Question-aware compression
* Context reordering
* Dynamic compression
* Long-context relevance ranking

This is particularly relevant to large RAG contexts.

## 5.3 Extractive Compression

The project implements a lightweight extractive compressor that:

1. Splits text into sentences
2. Scores sentence relevance
3. Keeps the most relevant sentences
4. Preserves original wording

## 5.4 Abstractive Compression

The project uses local Ollama to rewrite content into a shorter representation.

Unlike extractive compression, wording can change.

This creates a higher risk of information loss.

## 5.5 Compression Ratio vs Quality

Metrics include:

```text
Original words
Compressed words
Compression ratio
Reduction percentage
Quality score
```

Example:

```text
100 words
25 words

Compression ratio = 4x
Reduction = 75%
```

Higher compression is not automatically better.

The real objective is:

```text
Token reduction
        +
acceptable quality
        +
acceptable compression latency
```

Tests:

```powershell
python -m tests.test_extractive_compression
```

```powershell
python -m tests.test_abstractive_compression
```

```powershell
python -m tests.test_compression_tradeoff
```

LLMLingua installation verification:

```powershell
python -c "from llmlingua import PromptCompressor; print('LLMLingua import OK')"
```

---

# Topic 6 - Model Routing Strategy

## 6.1 Cheap Models for Simple Tasks

Simple requests can use a smaller model to reduce latency and cost.

Examples:

```text
What is RAG?
What is an embedding?
Summarize this sentence.
```

## 6.2 Powerful Models for Complex Tasks

Complex requests may require a more capable model.

Examples:

```text
Design a multi-tenant RAG architecture.
Compare distributed system architectures.
Analyze scalability and security trade-offs.
```

## 6.3 Classifying Task Complexity

The implementation considers:

```text
Prompt length
Complexity keywords
Multiple task indicators
Analytical reasoning indicators
```

and returns:

```text
simple
medium
complex
```

## 6.4 Cascading

The implementation tries the cheaper model first:

```text
Cheap Model
    ↓
Quality Check
    |
    +── Good → Return
    |
    +── Poor → Powerful Model
```

This can reduce the number of requests sent to expensive models.

Important routing metrics include:

```text
Simple request count
Complex request count
Cheap-model requests
Powerful-model requests
Escalation count
Escalation rate
Quality score
Total cost
```

Tests:

```powershell
python -m tests.test_complexity_classifier
```

```powershell
python -m tests.test_model_router
```

```powershell
python -m tests.test_cascading
```

---

# Complete Module 14 Optimization Architecture

```text
                           User Request
                                |
                                v
                         Exact Cache
                                |
                     +----------+----------+
                     |                     |
                    HIT                   MISS
                     |                     |
                  Return           Semantic Cache
                                           |
                                +----------+----------+
                                |                     |
                               HIT                   MISS
                                |                     |
                             Return                  |
                                                      v
                                             Prompt Compression
                                                      |
                                                      v
                                            Complexity Classifier
                                                      |
                                      +---------------+---------------+
                                      |                               |
                                    SIMPLE                         COMPLEX
                                      |                               |
                                      v                               v
                                 Cheap Model                    Powerful Model
                                      |                               |
                                      +---------------+---------------+
                                                      |
                                                  Quality
                                                    Check
                                                      |
                                      +---------------+---------------+
                                      |                               |
                                    GOOD                            POOR
                                      |                               |
                                   Return                         Escalate
                                                                      |
                                                                      v
                                                                Powerful Model
```

---

# Module 14 Key Metrics

```text
Cache hit rate
Semantic cache hit rate
LLM calls avoided
Token savings
Latency savings
Compression ratio
Compression latency
Quality score
Escalation rate
Model distribution
Cost by user
Cost by feature
Cost by model
```

---

# Key Interview Questions

## Why use caching in GenAI applications?

Caching avoids repeated inference for reusable requests, reducing latency, compute, token usage, and potentially provider costs.

## Exact cache vs semantic cache?

Exact caching matches normalized request identity. Semantic caching converts requests to embeddings and reuses responses when similarity exceeds a configured threshold.

## Why include model and prompt version in a cache key?

The same question can produce different valid answers under different models or prompt versions. Reusing an incompatible cached response can produce stale or incorrect results.

## Why is semantic-cache threshold tuning important?

A low threshold increases hits but risks false positives. A high threshold is safer but reduces the hit rate.

## What is LiteLLM?

LiteLLM provides a common interface for calling many LLM providers and supports routing, fallbacks, and related operational controls.

## Why compress prompts?

Reducing redundant context can decrease token processing and potentially lower latency and cost.

## Extractive vs abstractive compression?

Extractive compression removes existing content while preserving original wording. Abstractive compression rewrites content into a shorter form and therefore introduces more transformation risk.

## What is cascading?

Start with a lower-cost model and escalate to a more capable model only when the first response fails a quality or confidence check.

---

# Final Module 14 Checklist

```text
1. Why Caching is Critical
   Hands-on 1 ✅

2. Exact-Match Caching
   Hands-on 2 ✅

3. Semantic Caching
   Hands-on 3 ✅

4. LiteLLM
   Hands-on 4 ✅

5. Prompt Compression
   Hands-on 5 ✅

6. Model Routing Strategy
   Hands-on 6 ✅
```

---

# Module 14 Completion Notes

The module intentionally uses local implementations where external infrastructure is unavailable.

### Redis

The Redis-backed exact-cache implementation is complete, but the local Windows Redis server was not available. The implementation therefore includes an in-memory fallback for testing.

### Hosted model costs

The primary model is local Ollama, so the demonstrated provider cost is zero. The architecture supports model-pricing and budget abstractions for hosted providers.

### Production model routing

The cheap and powerful model roles may point to the same local model in the training environment. The routing and cascading architecture is implemented so the roles can later be mapped to genuinely different models.

### LLMLingua

LLMLingua is integrated through its `PromptCompressor` interface. The actual compression-model download/runtime requirements depend on the selected compressor model and local hardware.

---

# Module 14 Complete

All six topics and their practical implementations are complete.
