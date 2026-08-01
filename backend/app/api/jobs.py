from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database.database import SessionLocal
from app.models.job import Job
from app.services.ranking_service import rank_jobs



router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)





def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()






class JobUpdate(BaseModel):

    status: str | None = None

    notes: str | None = None







@router.get("/top")
def top_jobs(
    db: Session = Depends(get_db)
):

    try:

        jobs = db.query(Job).all()


        print(
            "TOTAL JOBS:",
            len(jobs)
        )


        result = rank_jobs(jobs)


        print(result)


        return result



    except Exception as e:


        print(
            "TOP JOB ERROR:",
            e
        )


        return {
            "error": str(e)
        }









@router.get("/{job_id}")
def get_job(

    job_id: int,

    db: Session = Depends(get_db)

):


    job = db.query(Job).filter(

        Job.id == job_id

    ).first()



    if not job:

        return {

            "error":
            "Job not found"

        }




    return {


        "id": job.id,


        "title": job.title,


        "company": job.company,


        "location": job.location,


        "url": job.url,


        "description": job.description,


        "ai_score": job.ai_score,


        "cv_type": job.cv_type,


        "status": job.status,


        "notes": job.notes

    }









@router.patch("/{job_id}")
def update_job(

    job_id: int,

    update: JobUpdate,

    db: Session = Depends(get_db)

):


    job = db.query(Job).filter(

        Job.id == job_id

    ).first()



    if not job:

        return {

            "error":
            "Job not found"

        }





    if update.status:


        job.status = update.status



        if update.status == "APPLIED":

            job.applied_date = datetime.utcnow()





    if update.notes:

        job.notes = update.notes





    db.commit()


    db.refresh(job)



    return job