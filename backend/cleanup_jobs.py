from app.database.database import SessionLocal
from app.models.job import Job
from app.services.job_filter import is_relevant_job


db = SessionLocal()


jobs = db.query(Job).all()

removed = 0


for job in jobs:

    job_dict = {
        "title": job.title,
        "description": job.description or ""
    }


    if not is_relevant_job(job_dict):

        print(
            "Removing:",
            job.title
        )

        db.delete(job)
        removed += 1


db.commit()
db.close()


print(
    "Removed:",
    removed
)