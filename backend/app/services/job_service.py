from sqlalchemy.orm import Session

from app.models.job import Job
from app.ai.matcher import match_job


def save_job(
    db: Session,
    job_data: dict
):

    # Prevent duplicate jobs
    existing = db.query(Job).filter(
        Job.url == job_data.get("url")
    ).first()

    if existing:
        return existing


    # AI CV matching
    matches = match_job(job_data)

    best_match = matches[0]


    # Create database entry
    new_job = Job(

        title=job_data.get(
            "title",
            "Unknown"
        ),

        company=job_data.get(
            "company",
            "Unknown"
        ),

        location=job_data.get(
            "location"
        ),

        url=job_data.get(
            "url"
        ),

        source=job_data.get(
            "source",
            "Unknown"
        ),

        description=job_data.get(
            "description",
            ""
        ),

        status="NEW",

        ai_score=best_match["match"],

        cv_type=best_match["profile"]
    )


    db.add(new_job)

    db.commit()

    db.refresh(new_job)


    return new_job