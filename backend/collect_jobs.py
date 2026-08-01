from app.scraper.greenhouse import get_greenhouse_jobs
from app.scraper.lever import get_lever_jobs
from app.scraper.smartrecruiters import get_smartrecruiter_jobs
from app.scraper.workday import get_workday_jobs

from app.scraper.company_loader import (
    GREENHOUSE_COMPANIES,
    LEVER_COMPANIES,
    SMARTRECRUITERS_COMPANIES
)

from app.database.database import SessionLocal, Base, engine
from app.models.job import Job
from app.services.job_filter import is_relevant_job

Base.metadata.create_all(bind=engine)

def save_job(job):

    db = SessionLocal()

    existing = db.query(Job).filter(
        Job.url == job["url"]
    ).first()


    if existing:

        db.close()
        return False


    new_job = Job(
        title=job.get(
            "title",
            ""
        ),

        company=job.get(
            "company",
            job.get(
                "source",
                ""
            )
        ),

        location=job.get(
            "location",
            ""
        ),

        description=job.get(
            "description",
            ""
        ),

        url=job.get(
            "url",
            ""
        )
    )


    db.add(new_job)

    db.commit()

    db.close()

    return True



def collect_jobs():

    jobs = []


    print("Checking Greenhouse...")


    for company in GREENHOUSE_COMPANIES:

        print(company)

        jobs.extend(
            get_greenhouse_jobs(
                company
            )
        )


    print("Checking Lever...")


    for company in LEVER_COMPANIES:

        print(
            company["name"]
        )

        jobs.extend(
            get_lever_jobs(
                company["board"]
            )
        )


    print("Checking SmartRecruiters...")


    for company in SMARTRECRUITERS_COMPANIES:

        print(company)

        jobs.extend(
            get_smartrecruiter_jobs(
                company
            )
        )


    print(
        "TOTAL FOUND:",
        len(jobs)
    )


    saved = 0
    filtered = 0
    duplicate = 0


    for job in jobs:

        title = job.get(
            "title",
            ""
        )


        if not is_relevant_job(job):

            print(
                "Filtered:",
                title
            )

            filtered += 1
            continue


        result = save_job(job)


        if result:

            print(
                "Saved:",
                title
            )

            saved += 1

        else:

            print(
                "Duplicate:",
                title
            )

            duplicate += 1



    print("\nSummary")
    print(
        "Saved:",
        saved
    )

    print(
        "Filtered:",
        filtered
    )

    print(
        "Duplicates:",
        duplicate
    )



if __name__ == "__main__":

    collect_jobs()