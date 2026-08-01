from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database.database import SessionLocal
from app.models.job import Job
from app.schemas.job import JobCreate, JobResponse


router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)

from datetime import datetime
from pydantic import BaseModel

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
        
class JobUpdate(BaseModel):

    status: str | None = None

    notes: str | None = None



@router.patch("/{job_id}")
def update_job(
    job_id:int,
    update:JobUpdate,
    db:Session=Depends(get_db)
):

    job = db.query(Job).filter(
        Job.id == job_id
    ).first()


    if not job:
        return {
            "error":"Job not found"
        }


    if update.status:
        job.status = update.status

        if update.status == "APPLIED":
            job.applied_date=datetime.utcnow()


    if update.notes:
        job.notes=update.notes


    db.commit()
    db.refresh(job)

    return job