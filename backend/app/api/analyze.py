from fastapi import APIRouter
from pydantic import BaseModel

from app.ai.job_analyzer import analyze_job


router = APIRouter(
    prefix="/analyze",
    tags=["AI Analysis"]
)


class JobAnalysisRequest(BaseModel):
    title: str
    company: str
    description: str = ""


@router.post("/")
def analyze(job: JobAnalysisRequest):

    return analyze_job(
        job.model_dump()
    )