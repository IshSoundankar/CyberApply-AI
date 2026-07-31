from sqlalchemy.orm import Session

from app.models.job import Job


def save_job(
    db: Session,
    job_data: dict
):

    existing = db.query(Job).filter(
        Job.url == job_data.get("url")
    ).first()


    if existing:
        return existing


    new_job = Job(
        title=job_data.get("title"),
        company=job_data.get("company", "Unknown"),
        location=job_data.get("location"),
        url=job_data.get("url"),
        source=job_data.get("source"),
        description=job_data.get("description"),
        status="NEW"
    )


    db.add(new_job)
    db.commit()
    db.refresh(new_job)


    return new_job