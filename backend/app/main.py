from fastapi import FastAPI

from app.database.database import Base, engine
from app.api.jobs import router as job_router
from app.models import job


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="CyberApply AI",
    description="AI Cybersecurity Job Assistant",
    version="1.0.0"
)


app.include_router(job_router)


@app.get("/")
def home():

    return {
        "status": "running",
        "app": "CyberApply AI"
    }