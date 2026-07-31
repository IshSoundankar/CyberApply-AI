from fastapi import FastAPI


app = FastAPI(
    title="CyberApply AI",
    description="AI Cybersecurity Job Assistant",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "status": "running",
        "app": "CyberApply AI"
    }