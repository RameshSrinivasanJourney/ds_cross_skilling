# Module 15 - Guardrails and Safety

## Overview

Module 15 focuses on building safer and more trustworthy Generative AI applications through input validation, output validation, guardrails, PII protection, and content moderation.

The module uses local **Ollama with `llama3.2:3b`** wherever practical and demonstrates defense-in-depth safety architecture.

The overall safety pipeline is:

```text
User
 |
 v
Input Validation
 |
 +--> Prompt Injection Detection
 +--> Topic Filtering
 +--> Length Validation
 +--> Encoding Sanitization
 +--> Language Validation
 |
 v
Safety / Moderation
 |
 v
LLM
 |
 v
Output Validation
 |
 +--> Rule Checks
 +--> Schema Validation
 +--> Content Policy
 +--> Faithfulness
 +--> Post-processing
 |
 v
Output Moderation
 |
 v
Response
```

---

# Learning Objectives

By the end of this module, you will understand:

* Why GenAI safety matters
* Harmful and biased content risks
* Business and legal risk
* User trust and reliability
* GDPR concepts
* HIPAA concepts
* SOC 2 concepts
* Prompt-injection detection
* Disallowed-topic filtering
* Input length limits
* Character/Unicode sanitization
* Language detection
* Rule-based output validation
* JSON schema validation
* Content policy checks
* Faithfulness validation
* Regex post-processing
* Guardrails AI
* Custom validators
* Reask strategies
* `reask`, `filter`, `exception`, and `noop`
* NeMo Guardrails
* Colang
* Input rails
* Output rails
* Dialog rails
* LangChain integration concepts
* PII detection
* Microsoft Presidio
* PII anonymization
* PII deanonymization
* Safe logging
* Content moderation
* Llama Guard
* OpenAI Moderation API concepts
* Perspective API concepts and service sunset
* Custom moderation classifiers
* Input and output moderation

---

# Environment

```text
Python 3.13.15
Ollama
llama3.2:3b
Pydantic
Guardrails AI
NeMo Guardrails
Microsoft Presidio
langdetect
```

---

# Project Structure

```text
Module15Handson/
|
├── app/
│   ├── __init__.py
│   |
│   ├── safety/
│   │   ├── __init__.py
│   │   ├── risk_categories.py
│   │   ├── safety_result.py
│   │   └── safety_classifier.py
│   |
│   ├── validation/
│   │   ├── __init__.py
│   │   ├── validation_result.py
│   │   ├── prompt_injection.py
│   │   ├── topic_filter.py
│   │   ├── length_validator.py
│   │   ├── encoding.py
│   │   ├── language.py
│   │   ├── input_validator.py
│   │   ├── output_rules.py
│   │   ├── output_schema.py
│   │   ├── output_policy.py
│   │   ├── faithfulness.py
│   │   ├── post_processor.py
│   │   └── output_validator.py
│   |
│   ├── guardrails/
│   │   ├── __init__.py
│   │   ├── basic_guard.py
│   │   ├── custom_validators.py
│   │   └── reask_service.py
│   |
│   ├── nemo/
│   │   ├── __init__.py
│   │   ├── nemo_service.py
│   │   └── config/
│   │       ├── config.yml
│   │       ├── prompts.yml
│   │       └── rails.co
│   |
│   ├── pii/
│   │   ├── __init__.py
│   │   ├── presidio_detector.py
│   │   ├── anonymizer.py
│   │   ├── pii_service.py
│   │   ├── token_mapper.py
│   │   └── safe_logging.py
│   |
│   ├── moderation/
│   │   ├── __init__.py
│   │   ├── categories.py
│   │   ├── result.py
│   │   └── classifier.py
│   |
│   ├── services/
│   │   ├── __init__.py
│   │   ├── safe_llm.py
│   │   ├── validated_llm.py
│   │   ├── output_validated_llm.py
│   │   ├── pii_safe_llm.py
│   │   └── moderated_llm.py
│   |
│   └── config/
│       └── __init__.py
│
├── tests/
│   ├── test_safety_classifier.py
│   ├── test_safe_llm.py
│   ├── test_input_validation.py
│   ├── test_validated_llm.py
│   ├── test_output_rules.py
│   ├── test_output_schema.py
│   ├── test_faithfulness.py
│   ├── test_post_processor.py
│   ├── test_output_validated_llm.py
│   ├── test_guardrails_basic.py
│   ├── test_guardrails_custom.py
│   ├── test_nemo_guardrails.py
│   ├── test_presidio_detection.py
│   ├── test_pii_safe_llm.py
│   ├── test_safe_logging.py
│   ├── test_moderation_classifier.py
│   └── test_moderated_llm.py
│
├── data/
├── logs/
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Topic 1 - Why Safety Matters

## 1.1 Harmful and Biased Content Risks

GenAI systems can produce harmful, biased, or otherwise inappropriate content.

The first hands-on established a rule-based safety layer that classifies requests as:

```text
SAFE
REVIEW
BLOCK
```

This provides an initial application-level control before the request reaches the model.

## 1.2 Business and Legal Risk

Safety failures can result in:

* Privacy exposure
* Unauthorized disclosure
* Incorrect business decisions
* Reputational damage
* Contractual risk
* Regulatory risk

Safety therefore needs to be treated as an application architecture concern rather than only a model behavior concern.

## 1.3 User Trust and Reliability

A useful GenAI application must be:

```text
Safe
Predictable
Controllable
Reliable
Transparent
```

Correctness alone is not sufficient.

## 1.4 GDPR, HIPAA, and SOC 2

These frameworks have different purposes and requirements.

Technical guardrails can support a compliance program, but a Python safety layer by itself does not make an application GDPR, HIPAA, or SOC 2 compliant.

---

# Topic 2 - Input Validation

The input validation pipeline covers:

```text
User Input
 |
 v
Character Sanitization
 |
 v
Length Validation
 |
 v
Prompt Injection Detection
 |
 v
Disallowed Topic Filtering
 |
 v
Language Validation
 |
 v
Allowed / Rejected
```

## 2.1 Prompt Injection Detection

The project detects common patterns such as attempts to:

```text
Ignore previous instructions
Reveal system prompt
Reveal developer instructions
Bypass safety rules
```

This is a deterministic baseline and should not be treated as a complete defense against all prompt injection attacks.

## 2.2 Disallowed Topics

The topic filter separates unsafe content policy from prompt-injection detection.

## 2.3 Input Length Limits

The validator rejects oversized inputs before performing unnecessary downstream processing.

## 2.4 Character Encoding Sanitization

Unicode normalization and control-character cleanup reduce input normalization problems.

## 2.5 Language Detection and Filtering

The example application initially permits English input.

Language detection is treated as a policy input rather than an infallible truth source, especially for very short or ambiguous text.

---

# Topic 3 - Output Validation

The output-validation pipeline checks the model response before it reaches the user.

```text
LLM Output
 |
 +--> Rules
 +--> Schema
 +--> Content Policy
 +--> Faithfulness
 +--> Post-processing
 |
 v
Valid / Invalid
```

## 3.1 Rule-Based Output Checks

Checks include:

* Empty output
* Maximum output size
* Sensitive-data patterns
* Forbidden patterns

## 3.2 JSON Schema Validation

Pydantic validates structured output such as:

```json
{
  "answer": "...",
  "confidence": 0.92,
  "sources": ["knowledge-base"]
}
```

The schema checks structure and field constraints.

## 3.3 Content Policy Checks

The previously built safety classifier is reused for generated output.

## 3.4 Faithfulness Check

For RAG-style applications, the output is compared against the supplied context.

The educational implementation uses word overlap.

This is a baseline demonstration and not a production-grade factuality evaluator.

## 3.5 Post-processing

The project removes common Markdown fence wrappers and normalizes excessive whitespace.

---

# Topic 4 - Guardrails AI

Guardrails AI provides a framework for attaching validators and validation behavior around model outputs.

Covered concepts:

```text
Validators
Custom validators
Reask
Filter
Exception
No-op
```

## Custom Validators

The project demonstrates custom checks for:

```text
PII
URLs
Configured toxic terms
```

## Reask

The reask pattern is:

```text
LLM
 ↓
Validation failure
 ↓
Feedback / corrected instruction
 ↓
LLM
 ↓
New response
```

This is useful for retrying recoverable validation failures.

## on_fail Actions

Conceptually:

```text
reask
→ regenerate

filter
→ remove or sanitize

exception
→ fail explicitly

noop
→ continue without enforcement
```

The appropriate action depends on severity and application policy.

---

# Topic 5 - NeMo Guardrails

NeMo Guardrails was used to demonstrate conversational rails around the LLM.

Architecture:

```text
User
 |
 v
Input Rail
 |
 v
Dialog Rail
 |
 v
LLM
 |
 v
Output Rail
 |
 v
Response
```

## Colang

Colang is used to express conversational rules and flows declaratively.

## Input Rails

Protect the application before model generation.

## Output Rails

Validate or constrain generated output.

## Dialog Rails

Control the allowed conversational behavior.

## LangChain Integration

The integration concept was covered:

```text
LangChain
 |
 +-- Retriever
 +-- Tools
 +-- Agent
 +-- LLM
 |
 v
NeMo Guardrails
```

The project uses local Ollama rather than requiring a paid provider.

---

# Topic 6 - PII Detection and Redaction

The PII pipeline is:

```text
User Input
 |
 v
PII Detection
 |
 v
Anonymization
 |
 v
LLM
 |
 v
Deanonymization
 |
 v
User Response
```

## PII Categories

Examples include:

```text
Names
Emails
Phone numbers
SSNs
Credit cards
```

## Microsoft Presidio

Presidio was used to demonstrate PII detection and anonymization.

## Reversible Tokenization

The application can replace:

```text
ramesh@example.com
```

with:

```text
<EMAIL_1>
```

and maintain an application-side mapping.

The real PII should remain inside the trusted application boundary and must not be sent to the LLM unnecessarily.

## Logging

A separate log sanitizer prevents original PII from being copied into observability logs.

---

# Topic 7 - Content Moderation

The moderation pipeline is:

```text
                User
                 |
                 v
          Input Moderation
                 |
           +-----+-----+
           |           |
          SAFE       UNSAFE
           |           |
           v           v
          LLM        Block
           |
           v
      Output Moderation
           |
      +----+----+
      |         |
    SAFE      UNSAFE
      |         |
      v         v
   Return     Block
```

## 7.1 OpenAI Moderation API

Covered as a hosted moderation option.

The actual runtime implementation does not require OpenAI because the project uses local Ollama.

## 7.2 Llama Guard

Covered as a dedicated safety-classification model.

Llama Guard can be used for classifying model inputs and outputs against defined safety categories.

The project keeps the primary hands-on lightweight and local instead of requiring a large dedicated safety-model download.

## 7.3 Perspective API

Covered as a toxicity-oriented moderation option.

Perspective API is treated as a transition/legacy technology in this module because the service is scheduled to sunset after 2026.

## 7.4 Custom Moderation Classifier

The project implements a deterministic classifier with:

```text
ALLOW
REVIEW
BLOCK
```

and categories such as:

```text
Violence
Self-harm
Illegal activity
Privacy
Prompt injection
```

## 7.5 Input and Output Moderation

Both directions are protected:

```text
Input → moderation → LLM
LLM output → moderation → user
```

This defense-in-depth model prevents relying on only one side of the interaction.

---

# Module 15 Safety Architecture

```text
                              USER
                                |
                                v
                     +--------------------+
                     | Input Validation   |
                     +--------------------+
                                |
               +----------------+----------------+
               |                |               |
          Injection          Topic            PII
           Check            Filter          Detection
               |                |               |
               +----------------+----------------+
                                |
                                v
                       Input Moderation
                                |
                                v
                         NeMo Input Rail
                                |
                                v
                               LLM
                                |
                                v
                      NeMo Output Rail
                                |
                  +-------------+-------------+
                  |             |             |
                Rules        Schema       Policy
                  |             |             |
                  +-------------+-------------+
                                |
                           Faithfulness
                                |
                         Output Moderation
                                |
                                v
                            RESPONSE
```

---

# Defense-in-Depth Principles

No single control is sufficient.

```text
Regex
 +
Rules
 +
Schema
 +
PII Detection
 +
Guardrails
 +
Moderation
 +
Human Review
```

The correct architecture depends on application risk.

High-risk applications should use stronger controls and human oversight rather than relying solely on deterministic keyword filters.

---

# Final Test Commands

Run the applicable module tests:

```powershell
python -m tests.test_safety_classifier
```

```powershell
python -m tests.test_safe_llm
```

```powershell
python -m tests.test_input_validation
```

```powershell
python -m tests.test_validated_llm
```

```powershell
python -m tests.test_output_rules
```

```powershell
python -m tests.test_output_schema
```

```powershell
python -m tests.test_faithfulness
```

```powershell
python -m tests.test_post_processor
```

```powershell
python -m tests.test_output_validated_llm
```

```powershell
python -m tests.test_guardrails_basic
```

```powershell
python -m tests.test_guardrails_custom
```

```powershell
python -m tests.test_nemo_guardrails
```

```powershell
python -m tests.test_presidio_detection
```

```powershell
python -m tests.test_pii_safe_llm
```

```powershell
python -m tests.test_safe_logging
```

```powershell
python -m tests.test_moderation_classifier
```

```powershell
python -m tests.test_moderated_llm
```

---

# Final Module Checklist

```text
1. Why Safety Matters
   Hands-on 1 ✅

2. Input Validation
   Hands-on 2 ✅

3. Output Validation
   Hands-on 3 ✅

4. Guardrails AI
   Hands-on 4 ✅

5. NeMo Guardrails
   Hands-on 5 ✅

6. PII Detection and Redaction
   Hands-on 6 ✅

7. Content Moderation
   Hands-on 7 ✅
```

# Module 15 Completion

All seven topics have been implemented and tested.

```text
Topic 1 ✅
Topic 2 ✅
Topic 3 ✅
Topic 4 ✅
Topic 5 ✅
Topic 6 ✅
Topic 7 ✅
```
