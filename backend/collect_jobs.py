from app.database.database import SessionLocal
from app.scraper.greenhouse import get_greenhouse_jobs
from app.services.job_service import save_job
from app.services.job_filter import is_relevant_job

db = SessionLocal()


companies = [
    "cloudflare"
]


for company in companies:

    jobs = get_greenhouse_jobs(company)

    for job in jobs:
        if not is_relevant_job(job):
            continue
        job["company"] = company

        saved = save_job(
            db,
            job
        )

        print(
            "Saved:",
            saved.title
        )


db.close()