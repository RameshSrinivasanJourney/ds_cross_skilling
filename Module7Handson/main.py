from fastapi import FastAPI

app = FastAPI(
    title="Module 7 - Function Calling and Tool Use",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "module": "Module 7",
        "topic": "Function Calling and Tool Use",
        "status": "running",
    }