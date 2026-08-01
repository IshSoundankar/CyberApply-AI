from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import Base, engine
from app.api.jobs import router as job_router
from app.api.analyze import router as analyze_router

from app.models.job import Job


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="CyberApply AI",
    description="AI Cybersecurity Job Assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(job_router)
app.include_router(analyze_router)


@app.get("/")
def home():

    return {
        "status": "running",
        "app": "CyberApply AI"
    }