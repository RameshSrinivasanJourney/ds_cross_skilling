# Module 13 - Observability and Monitoring

## Overview

Module 13 focuses on **Observability and Monitoring for Generative AI applications**.

GenAI systems are non-deterministic, can produce quality regressions, may have variable latency, consume different amounts of tokens, and can become expensive when external models are introduced.

This module demonstrates how to capture traces, metrics, costs, errors, user feedback, structured logs, correlation IDs, and PII-safe application telemetry.

The hands-on implementations use **local Ollama with `llama3.2:3b`** wherever practical.

---

# Learning Objectives

By the end of this module, you will understand:

* Why observability matters for GenAI
* Debugging prompt-related issues
* Cost visibility by user and feature
* Quality degradation detection
* TTFT and total latency
* LangSmith tracing concepts
* Manual tracing for non-LangChain applications
* LangSmith datasets and evaluations
* Prompt-version experiments
* Langfuse Cloud vs self-hosting
* Langfuse Python SDK tracing
* Spans and generations
* User and session tracking
* Token and cost tracking
* Langfuse dashboards
* Prompt management
* GenAI latency metrics
* Token metrics
* Cost metrics
* Error rates
* Cache hit rate
* Retrieval relevance
* User satisfaction
* PII scrubbing
* Structured JSON logging
* Correlation IDs
* Log levels
* Production log-storage architecture

---

# Environment

```text
Python 3.13.15
Ollama
llama3.2:3b
FastAPI
LangSmith SDK
Langfuse SDK
```

The primary LLM is local Ollama.

---

# Project Structure

```text
Module13Handson/
│
├── .venv/
│
├── app/
│   ├── __init__.py
│   │
│   ├── observability/
│   │   ├── __init__.py
│   │   ├── metrics.py
│   │   ├── structured_logger.py
│   │   └── observable_llm.py
│   │
│   ├── tracing/
│   │   ├── __init__.py
│   │   ├── langsmith_ollama.py
│   │   ├── langsmith_pipeline.py
│   │   ├── langfuse_client.py
│   │   ├── langfuse_ollama.py
│   │   ├── langfuse_pipeline.py
│   │   └── langfuse_prompt.py
│   │
│   ├── metrics/
│   │   ├── __init__.py
│   │   ├── metric_record.py
│   │   ├── metrics_collector.py
│   │   └── pricing.py
│   │
│   ├── logging/
│   │   ├── __init__.py
│   │   ├── pii_scrubber.py
│   │   ├── json_formatter.py
│   │   ├── correlation.py
│   │   └── logger.py
│   │
│   ├── evaluation/
│   │   ├── __init__.py
│   │   ├── create_dataset.py
│   │   └── run_evaluation.py
│   │
│   ├── services/
│   │   └── __init__.py
│   │
│   └── config/
│       ├── __init__.py
│       └── langfuse_config.py
│
├── tests/
│   ├── test_observability.py
│   ├── test_langsmith_tracing.py
│   ├── test_langfuse.py
│   ├── test_metrics.py
│   └── test_logging.py
│
├── data/
├── logs/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── main.py
```

---

# Topic 1 - Why Observability Matters

## 1.1 Non-deterministic outputs need visibility

An LLM can produce different outputs for similar inputs.

Observability captures information such as:

```text
correlation_id
user_id
feature
model
prompt_version
latency
tokens
cost
quality
errors
```

## 1.2 Debugging prompt issues

The implementation records:

```text
prompt_version
prompt_hash
model
feature
```

This helps correlate changes in prompt versions with application behavior.

## 1.3 Cost visibility

The application records:

```text
input_tokens
output_tokens
total_tokens
estimated_cost
```

For local Ollama the configured cost is zero, but the same model-pricing abstraction can be used with paid providers.

## 1.4 Quality degradation detection

A lightweight quality evaluator records:

```text
quality_score
quality_status
```

The implementation demonstrates the mechanics of quality monitoring without claiming to replace a production-grade evaluation system.

## 1.5 Latency monitoring

Streaming requests record:

```text
TTFT
total generation latency
chunk count
```

This allows separation of:

```text
Time to first output
```

from:

```text
Time to complete generation
```

Test:

```powershell
python -m tests.test_observability
```

---

# Topic 2 - LangSmith

## 2.1 Setting up tracing

LangSmith was evaluated as an observability platform and its Python tracing model was implemented using the SDK.

## 2.2 Automatic tracing with LangChain

LangChain can automatically emit tracing information when LangSmith tracing is configured.

This module demonstrates the concept but does not require a LangChain application for the main hands-on.

## 2.3 Manual tracing for non-LangChain code

Because the application uses local Ollama directly, manual tracing is implemented with:

```text
@traceable
```

This demonstrates how non-LangChain application code can be instrumented.

## 2.4 Trace explorer

Traced execution can be inspected in LangSmith to view:

* Inputs
* Outputs
* Intermediate steps
* Metadata
* Tags
* Timing

## 2.5 Inputs, outputs and intermediate steps

The tracing example creates a nested pipeline:

```text
observable_pipeline
│
├── build_prompt
│
└── ollama_generation
```

## 2.6 Metadata

The tracing implementation records metadata such as:

```text
application
environment
model_provider
feature
prompt_version
```

## 2.7 Datasets and evaluations

The project contains examples demonstrating:

```text
Dataset
+
Target Application
+
Evaluator
=
Experiment
```

Dataset and evaluation code:

```text
app/evaluation/create_dataset.py
app/evaluation/run_evaluation.py
```

## 2.8 Prompt-version experiments

The application demonstrates comparing prompt versions using different experiment identifiers.

### LangSmith account note

A LangSmith account was intentionally not made a prerequisite for this training. The syllabus concepts, tracing model, datasets, evaluations, metadata, and experiments were covered, while the actual platform hands-on was performed with Langfuse.

---

# Topic 3 - Langfuse

Langfuse Cloud was used for the actual observability implementation.

## 3.1 Self-hosting vs Langfuse Cloud

### Cloud

```text
Application
    ↓
Langfuse Cloud
```

Advantages for this training:

* No Docker dependency
* No local observability infrastructure
* Faster setup
* Works with local Ollama

### Self-hosted

```text
Application
    ↓
Self-hosted Langfuse
    ↓
Supporting infrastructure
```

Self-hosting is useful when infrastructure control, data residency, or enterprise deployment requirements justify the additional operational complexity.

## 3.2 Python SDK decorator

The implementation uses:

```python
@observe(...)
```

to trace application functions.

## 3.3 Manual tracing with spans and generations

The implementation creates:

```text
genai_request
│
├── prepare-request
│
└── ollama_generation
```

The generation records model and usage information.

## 3.4 User and session tracking

The tracing pipeline propagates:

```text
user_id
session_id
```

Example:

```text
User:
employee-001

Session:
module13-<UUID>
```

## 3.5 Cost tracking per model

For local Ollama:

```text
Model:
llama3.2:3b

Input tokens:
captured

Output tokens:
captured

Cost:
0
```

The implementation also demonstrates how model pricing can be supplied explicitly.

## 3.6 Dashboards

The module covers dashboard-oriented analysis for:

```text
Latency
Cost
Error rate
Token usage
User/session activity
```

Individual traces provide detailed events while dashboards aggregate application behavior.

## 3.7 Prompt management

A Langfuse-managed prompt named:

```text
module13-answer-prompt
```

was created and retrieved from the application.

Template:

```text
You are a helpful AI tutor.

Answer the user's question clearly and concisely.

User question:
{{question}}
```

The application uses:

```python
langfuse.get_prompt(...)
```

followed by:

```python
prompt.compile(...)
```

to produce the final prompt.

Verified examples:

```text
What is RAG?
```

and:

```text
Explain embeddings
```

both compiled successfully.

---

# Topic 4 - Metrics to Track

## 4.1 Latency

Metrics:

```text
TTFT
total latency
```

## 4.2 Token usage

Metrics:

```text
input tokens
output tokens
total tokens
```

## 4.3 Cost

Metrics are aggregated by:

```text
request
user
feature
```

The local Ollama model is configured with zero monetary cost.

## 4.4 Error rate

The collector tracks:

```text
total requests
successful requests
failed requests
error types
```

Example:

```text
5 requests
1 failure

Error rate = 20%
```

## 4.5 Cache hit rate

The collector records:

```text
cache hits
cache misses
cache hit rate
```

## 4.6 Retrieval relevance

The collector accepts normalized retrieval relevance scores:

```text
0.0 → irrelevant
1.0 → highly relevant
```

## 4.7 User satisfaction

The collector accepts user scores:

```text
1 → very poor
5 → excellent
```

Test:

```powershell
python -m tests.test_metrics
```

---

# Topic 5 - Logging Best Practices

## 5.1 Prompt / response logging

Recommended fields include:

```text
timestamp
level
service
correlation_id
user identifier
feature
model
prompt version
latency
token usage
cost
status
error type
```

Sensitive prompt/response content should not automatically be written in full.

## 5.2 PII scrubbing

The implementation redacts common patterns such as:

```text
Email
Phone
Credit card
```

Example:

```text
My email is [REDACTED_EMAIL]
My phone is [REDACTED_PHONE]
```

## 5.3 Structured JSON logging

Logs are emitted as JSON:

```json
{
  "timestamp": "...",
  "level": "INFO",
  "logger": "module13",
  "service": "module13",
  "message": "llm_request_completed",
  "context": {
    "correlation_id": "...",
    "model": "llama3.2:3b",
    "input_tokens": 120,
    "output_tokens": 250,
    "total_tokens": 370,
    "latency_ms": 2300
  }
}
```

## 5.4 Correlation IDs

A UUID correlation ID follows a request across application operations.

Example:

```text
API Gateway
    ↓
GenAI Service
    ↓
Retrieval
    ↓
LLM
```

All logs can reference the same correlation ID.

## 5.5 Log levels

The implementation supports:

```text
DEBUG
INFO
ERROR
```

Use DEBUG for detailed diagnostics, INFO for normal business/application events, and ERROR for failures.

## 5.6 Log storage

Production architectures can forward structured logs to:

### Elasticsearch

```text
Application
    ↓
Fluent Bit / Filebeat
    ↓
Elasticsearch
    ↓
Kibana
```

### Loki

```text
Application
    ↓
Collector
    ↓
Loki
    ↓
Grafana
```

### CloudWatch

```text
Application
    ↓
CloudWatch Logs
    ↓
Logs Insights / Alarms
```

The hands-on itself uses local structured JSON output and does not require these platforms.

Test:

```powershell
python -m tests.test_logging
```

---

# Module 13 Observability Architecture

```text
                           GenAI Application
                                   |
             +---------------------+---------------------+
             |                     |                     |
           Logs                 Metrics               Traces
             |                     |                     |
        JSON + PII            Latency                  Langfuse
        Correlation           Tokens
        Log Levels            Cost
             |                Errors
             |                Cache
             |                Retrieval
             |                Satisfaction
             |
             +---------------------+---------------------+
                                   |
                            Observability
```

---

# End-to-End Request Lifecycle

```text
Request
   ↓
Correlation ID
   ↓
Prompt / feature / user metadata
   ↓
LLM
   ↓
Tracing
   ↓
Metrics
   ↓
PII-safe structured logging
   ↓
Response
```

---

# Final Test Commands

Run:

```powershell
python -m tests.test_observability
```

```powershell
python -m tests.test_langsmith_tracing
```

```powershell
python -m tests.test_langfuse
```

```powershell
python -m tests.test_metrics
```

```powershell
python -m tests.test_logging
```

---

# Module 13 Final Checklist

```text
1. Why Observability Matters
   Hands-on 1 ✅

2. LangSmith
   Concepts and implementation examples ✅
   Account intentionally skipped

3. Langfuse
   Hands-on 3 ✅

4. Metrics to Track
   Hands-on 4 ✅

5. Logging Best Practices
   Hands-on 5 ✅
```

---

# Key Interview Questions

## Why is observability more important for GenAI?

LLM applications are probabilistic, so failures can involve prompt quality, retrieval quality, model behavior, latency, token usage, and cost rather than only traditional application exceptions.

## What is TTFT?

Time To First Token: the elapsed time between the request and the first generated output.

## Why distinguish TTFT from total latency?

A user may tolerate a long overall response if useful output starts quickly. TTFT reflects perceived responsiveness, while total latency measures completion time.

## Why track tokens?

Tokens drive model context usage and, for paid providers, are typically the foundation for cost calculation.

## Why track cost by user and feature?

It allows teams to identify expensive users, workflows, or product features.

## What is a correlation ID?

A unique request identifier used to connect logs and traces across multiple services.

## Why scrub PII before logging?

Logs often have broader access and longer retention than application data. Sensitive information should not be unnecessarily copied into observability systems.

## Why use structured JSON logs?

Machines can reliably parse, index, filter, aggregate, and alert on structured fields.

## LangSmith vs Langfuse?

Both provide LLM observability, tracing, evaluation, and related capabilities. LangSmith is strongly integrated with the LangChain ecosystem, while Langfuse provides an open-source/OpenTelemetry-oriented observability platform and was the practical tracing implementation used in this module.

---

# Module 13 Completion

All five module topics have been implemented and tested.

```text
Topic 1  ✅
Topic 2  ✅
Topic 3  ✅
Topic 4  ✅
Topic 5  ✅
```
