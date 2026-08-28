# Module 16 - LLM Evaluation

## Overview

Module 16 focuses on systematic evaluation of Large Language Model applications.

LLM outputs are non-deterministic, so traditional unit testing alone is not sufficient. This module demonstrates how to build evaluation datasets, calculate task-appropriate metrics, use an LLM as a judge, detect hallucinations, and establish regression gates for CI/CD.

The overall evaluation lifecycle is:

```text
Golden Dataset
      |
      v
Candidate Model / Prompt
      |
      v
Generate Responses
      |
      +-------------------+
      |                   |
      v                   v
Automated Metrics      LLM-as-Judge
      |                   |
      +---------+---------+
                |
                v
       Hallucination Checks
                |
                v
          Quality Gate
                |
        +-------+-------+
        |               |
       PASS            FAIL
        |               |
        v               v
     Deploy          Block
        |
        v
 Metric History
        |
        v
 Regression Detection
```

---

# Learning Objectives

By the end of this module, you will understand:

* Why systematic LLM evaluation is necessary
* Evaluation-driven development
* Reference-based evaluation
* Reference-free evaluation
* Automated evaluation
* Human evaluation
* Offline evaluation
* Online evaluation
* Unit tests
* Regression suites
* Benchmark suites
* Golden evaluation datasets
* Adversarial evaluation datasets
* Dataset versioning
* Exact Match
* BLEU
* ROUGE-1
* ROUGE-2
* ROUGE-L
* BERTScore
* METEOR
* Perplexity
* Metric selection by task
* LLM-as-a-Judge
* Pointwise scoring
* Pairwise comparison
* Judge prompt design
* Position bias
* Verbosity bias
* Self-preference bias
* Judge calibration
* Summarization evaluation
* Question-answering evaluation
* Code-generation evaluation
* Classification evaluation
* Dialogue evaluation
* Instruction-following evaluation
* Hallucination detection
* Entailment-based checking
* SelfCheckGPT-style consistency checking
* FactScore-style claim-level evaluation
* ChainPoll-style multi-sample polling
* Regression testing
* Quality thresholds
* CI/CD evaluation gates
* Metric trend tracking
* Quality regression detection
* Prompt version tracking

---

# Environment

```text
Python 3.13.15
Ollama
llama3.2:3b
```

Additional evaluation libraries are installed progressively for the different hands-ons.

---

# Project Structure

```text
Module16Handson/
|
├── app/
│   ├── __init__.py
│   |
│   ├── datasets/
│   │   ├── __init__.py
│   │   ├── dataset_loader.py
│   │   └── dataset_validator.py
│   |
│   ├── metrics/
│   │   ├── __init__.py
│   │   ├── text_metrics.py
│   │   └── perplexity.py
│   |
│   ├── judges/
│   │   ├── __init__.py
│   │   ├── llm_judge.py
│   │   └── calibration.py
│   |
│   ├── hallucination/
│   │   ├── __init__.py
│   │   ├── entailment.py
│   │   ├── self_check.py
│   │   ├── claims.py
│   │   ├── polling.py
│   │   └── evaluator.py
│   |
│   └── evaluation/
│       ├── __init__.py
│       ├── faithfulness.py
│       ├── summarization.py
│       ├── qa.py
│       ├── code.py
│       ├── classification.py
│       ├── dialogue.py
│       ├── instruction_following.py
│       ├── config.py
│       ├── result.py
│       ├── gate.py
│       ├── golden_runner.py
│       ├── history.py
│       ├── regression.py
│       ├── alerts.py
│       └── metadata.py
│
├── tests/
│   ├── test_datasets.py
│   ├── test_exact_match.py
│   ├── test_bleu_rouge.py
│   ├── test_meteor.py
│   ├── test_bertscore.py
│   ├── test_text_metrics.py
│   ├── test_perplexity.py
│   ├── test_pointwise_judge.py
│   ├── test_pairwise_judge.py
│   ├── test_position_bias.py
│   ├── test_judge_calibration.py
│   ├── test_dataset_with_judge.py
│   ├── test_task_summarization.py
│   ├── test_task_qa.py
│   ├── test_task_code.py
│   ├── test_task_classification.py
│   ├── test_task_dialogue.py
│   ├── test_task_instruction.py
│   ├── test_entailment.py
│   ├── test_self_check.py
│   ├── test_factscore_style.py
│   ├── test_chainpoll_style.py
│   ├── test_hallucination_evaluator.py
│   ├── test_evaluation_gate.py
│   ├── test_golden_runner.py
│   ├── test_metric_history.py
│   ├── test_regression.py
│   ├── test_alerts.py
│   └── test_evaluation_metadata.py
│
├── scripts/
│   └── run_evaluation.py
│
├── data/
│   ├── golden/
│   │   └── qa_golden.json
│   ├── adversarial/
│   │   └── qa_adversarial.json
│   └── evaluation_history.json
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

The exact set of generated runtime files may vary because evaluation-history files are produced during testing.

---

# Hands-on 1 - Evaluation Fundamentals + Evaluation Dataset

The first hands-on established the evaluation foundation.

## Golden Dataset

The golden dataset stores:

```text
ID
Question
Expected answer
Required facts
```

Example:

```json
{
  "id": "qa-001",
  "question": "What is Retrieval-Augmented Generation?",
  "expected_answer": "RAG retrieves relevant information and provides that context to a language model to generate an answer.",
  "required_facts": [
    "retrieves relevant information",
    "context",
    "language model"
  ]
}
```

## Adversarial Dataset

The adversarial dataset covers:

```text
Prompt injection
Ambiguous queries
Out-of-scope inputs
```

## Evaluation Fundamentals

Reference-based evaluation compares generated output with known expected information.

Reference-free evaluation evaluates the response without requiring one exact answer.

Offline evaluation runs against a fixed dataset before deployment.

Online evaluation uses sampled production traffic.

The eval-driven development cycle is:

```text
Build
  |
Evaluate
  |
Analyze failures
  |
Improve
  |
Evaluate again
  |
Deploy
```

---

# Hands-on 2 - Metrics for Text Generation

The module implements:

```text
Exact Match
BLEU
ROUGE-1
ROUGE-2
ROUGE-L
BERTScore
METEOR
Perplexity
```

## Exact Match

Useful for:

```text
Exact labels
Identifiers
Short factual answers
Structured answers
```

## BLEU

Measures n-gram precision against reference text.

Most commonly associated with machine translation and reference-overlap evaluation.

## ROUGE

Useful especially for summarization.

```text
ROUGE-1
→ unigram overlap

ROUGE-2
→ bigram overlap

ROUGE-L
→ longest common subsequence
```

## BERTScore

Uses contextual embeddings to measure semantic similarity.

Useful when paraphrased wording can still represent the same meaning.

## METEOR

Uses flexible word alignment and can use stemming/synonym information through WordNet.

The Module 16 environment requires the NLTK WordNet data resource:

```powershell
python -c "import nltk; nltk.download('wordnet'); nltk.download('omw-1.4')"
```

## Perplexity

Perplexity measures how probable a sequence is under a language model.

It is useful for language-model analysis but should not be interpreted as a direct factuality or helpfulness metric.

---

# Hands-on 3 - LLM-as-a-Judge

The local Ollama model is used as an evaluation judge.

## Pointwise

One answer receives an absolute score.

```text
Question
   |
Answer
   |
Judge
   |
1 - 5 score
```

Evaluation criteria include:

```text
Correctness
Relevance
Completeness
Clarity
```

## Pairwise

Two answers are compared:

```text
Question
   |
+--+--+
|     |
A     B
 \   /
  Judge
    |
 A / B / tie
```

Useful for:

```text
Prompt comparisons
Model comparisons
A/B evaluation
```

## Judge Bias

The module demonstrates:

```text
Position bias
Verbosity bias
Self-preference bias
```

A robust evaluation pipeline should test whether the judge changes its decision merely because answer ordering changes.

## Judge Calibration

Judge scores can be compared against human labels.

Example:

```text
Human scores
      |
      v
Compare
      |
      v
Judge scores
```

This helps determine whether the judge is sufficiently aligned with human evaluation.

---

# Hands-on 4 - Task-Specific Evaluation

Different tasks require different evaluation approaches.

| Task                  | Evaluation                               |
| --------------------- | ---------------------------------------- |
| Summarization         | ROUGE, semantic similarity, faithfulness |
| Question Answering    | Correctness, groundedness                |
| Code Generation       | Execution/test pass rate                 |
| Classification        | Precision, Recall, F1                    |
| Dialogue              | Coherence, task completion               |
| Instruction Following | Constraint compliance                    |

## Summarization

The implementation combines:

```text
ROUGE
+
Faithfulness
```

## Question Answering

The implementation evaluates:

```text
Exact Match
Groundedness
```

## Code Generation

Generated code is executed against tests to measure functional correctness.

Generated code should never be executed directly on a production host without isolation.

## Classification

The implementation calculates:

```text
Accuracy
Precision
Recall
F1
```

## Dialogue

The baseline evaluator measures:

```text
Coherence
Context usage
Task completion
```

## Instruction Following

The evaluator checks:

```text
Required terms
Maximum words
Bullet count
JSON validity
```

---

# Hands-on 5 - Hallucination Detection

Hallucination detection covers several complementary approaches.

## Entailment

```text
Context
 +
Claim
 ↓
Supported / Unsupported
```

The project uses a lightweight lexical baseline to demonstrate the architecture.

## SelfCheckGPT-Style Sampling

Multiple model generations are compared:

```text
Prompt
 |
 +--> Sample 1
 +--> Sample 2
 +--> Sample 3
 +--> Sample 4
 +--> Sample 5
 |
 v
Consistency Analysis
```

Higher consistency can reduce suspicion, while strong disagreement can indicate possible hallucination.

Consistency is a signal, not proof of truth.

## FactScore-Style Evaluation

The answer is broken into claims:

```text
Answer
 |
 +--> Claim 1
 +--> Claim 2
 +--> Claim 3
 |
 v
Supported / Unsupported
 |
 v
Fact Score
```

## ChainPoll-Style Evaluation

Multiple model judgments are collected:

```text
Judge 1
Judge 2
Judge 3
Judge 4
Judge 5
   |
   v
Majority decision
```

The implementation is a lightweight local demonstration of the multi-sample polling concept.

---

# Hands-on 6 - Regression Testing + CI/CD

The final hands-on connects the previous work into a quality gate.

## Quality Thresholds

The evaluation configuration tracks:

```text
Minimum Exact Match
Minimum ROUGE-L
Minimum Faithfulness
Minimum Judge Score
Maximum Hallucination Rate
```

Example:

```text
Exact Match      >= 0.60
ROUGE-L          >= 0.50
Faithfulness     >= 0.60
Judge Score      >= 3.50
Hallucination    <= 0.20
```

## Quality Gate

```text
Evaluation Results
       |
       v
Threshold Check
       |
   +---+---+
   |       |
 PASS     FAIL
   |       |
 Deploy   Block
```

## Metric History

Evaluation runs store:

```text
Timestamp
Prompt version
Model version
Dataset version
Metrics
Pass/fail result
```

This makes it possible to observe changes over time.

## Regression Detection

A metric regression is detected when the current metric drops beyond the configured tolerance.

Example:

```text
Previous ROUGE-L = 0.80
Current ROUGE-L  = 0.68
Drop             = 0.12
```

With a maximum allowed drop of `0.05`, this becomes a regression.

## Alerts

Regression messages are generated for failed metrics.

In production these can feed:

```text
Slack
Microsoft Teams
Email
PagerDuty
Monitoring systems
```

## Prompt Versioning

Evaluation results track:

```text
Prompt version
Model version
Dataset version
```

This makes prompt/model changes measurable and reproducible.

---

# CI/CD Strategy

A practical production approach is to separate evaluation speed.

## Fast Evaluation

Run on every pull request:

```text
Deterministic tests
Golden dataset
Schema checks
Basic metrics
```

## Full Evaluation

Run on model/prompt changes, release builds, or scheduled jobs:

```text
LLM-as-a-Judge
Self-consistency
Multi-sample polling
Additional hallucination evaluation
Human sampling
```

The important principle is:

```text
Code Change
    |
Fast Evaluation
    |
PASS / FAIL
    |
Release Evaluation
    |
PASS / FAIL
    |
Production
```

---

# Production Evaluation Architecture

```text
                         Golden Dataset
                               |
                               v
                         Candidate Model
                               |
                               v
                        Generated Answers
                               |
                +--------------+--------------+
                |              |              |
             Metrics       LLM Judge     Hallucination
                |              |              |
                +--------------+--------------+
                               |
                               v
                       Quality Thresholds
                               |
                       +-------+-------+
                       |               |
                     PASS             FAIL
                       |               |
                       v               v
                    Deploy           Block
                       |
                       v
                  Metric History
                       |
                       v
                 Regression Alerts
```

---

# Important Evaluation Principles

## Do not rely on one metric

Different metrics capture different properties.

```text
Lexical similarity
+
Semantic similarity
+
Faithfulness
+
Correctness
+
Human judgment
```

is generally more useful than one aggregate score.

## Do not trust an LLM judge blindly

The judge can have:

```text
Position bias
Verbosity bias
Self-preference
Calibration problems
```

## Do not treat perplexity as factuality

A fluent incorrect answer can still have relatively low perplexity.

## Do not treat consistency as truth

A model can consistently repeat the same incorrect statement.

## Evaluation must be task-specific

The right metric for:

```text
Summarization
```

is not necessarily the right metric for:

```text
Code generation
```

---

# Module 16 Completion

All six practical hands-ons are complete:

```text
Hands-on 1 — Evaluation Fundamentals + Dataset       ✅
Hands-on 2 — Text Generation Metrics                  ✅
Hands-on 3 — LLM-as-a-Judge                           ✅
Hands-on 4 — Task-Specific Evaluation                 ✅
Hands-on 5 — Hallucination Detection                  ✅
Hands-on 6 — Regression Testing + CI/CD               ✅
```

The major evaluation capabilities covered are:

```text
Dataset construction
Metric evaluation
LLM judging
Task-specific evaluation
Hallucination detection
Regression detection
CI/CD quality gates
```

---

# Final Notes

This project is intentionally designed as a **learning implementation**.

Some components are simplified baselines:

```text
Lexical entailment
Simple faithfulness scoring
Rule-based task evaluation
SelfCheck lexical similarity
FactScore-style sentence claims
ChainPoll-style polling
```

Production systems should use stronger evaluators, validated datasets, human calibration, security isolation, monitoring, and task-specific evaluation strategies.
