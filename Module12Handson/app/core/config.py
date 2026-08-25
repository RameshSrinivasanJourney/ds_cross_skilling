import os


APP_NAME = os.getenv(
    "MODULE12_APP_NAME",
    "Module 12 Production API",
)

API_KEY = os.getenv(
    "MODULE12_API_KEY",
    "module12-demo-key",
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.2:3b",
)

OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://localhost:11434",
)

RATE_LIMIT = int(
    os.getenv(
        "MODULE12_RATE_LIMIT",
        "20",
    )
)