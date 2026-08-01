from sqlalchemy.orm import Session

from app.models.job import Job
from app.ai.job_analyzer import analyze_job



def save_job(
    db:Session,
    job_data:dict
):


    existing = db.query(Job).filter(
        Job.url == job_data.get("url")
    ).first()



    if existing:

        return existing



    analysis = analyze_job(
        job_data
    )



    job = Job(

        title=job_data.get(
            "title"
        ),

        company=job_data.get(
            "company"
        ),

        location=job_data.get(
            "location"
        ),

        url=job_data.get(
            "url"
        ),

        description=job_data.get(
            "description",
            ""
        ),

        source=job_data.get(
            "source"
        ),


        status="NEW",


        ai_score=
            analysis["score"],


        cv_type=
            analysis["cv_type"]

    )


    db.add(job)

    db.commit()

    db.refresh(job)


    return job