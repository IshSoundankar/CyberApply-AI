from app.database.database import SessionLocal

from app.scraper.job_sources import load_companies
from app.scraper.registry import get_scraper

from app.services.job_service import save_job
from app.services.job_filter import is_relevant_job


def main():

    db = SessionLocal()

    companies = load_companies()

    total_saved = 0


    for company in companies:

        print(
            f"\nChecking {company['company']}..."
        )


        scraper = get_scraper(
            company.get("platform")
        )


        if scraper is None:

            print(
                f"Skipping {company['company']} - "
                f"{company['platform']} scraper not available"
            )

            continue


        try:

            jobs = scraper(
                company["board"]
            )


        except Exception as error:

            print(
                f"Failed {company['company']}: {error}"
            )

            continue



        for job in jobs:


            if not is_relevant_job(job):

                continue



            job["company"] = company["company"]


            saved = save_job(
                db,
                job
            )


            total_saved += 1


            print(
                "Saved:",
                saved.title
            )


    db.close()


    print(
        f"\nFinished. Saved {total_saved} jobs."
    )



if __name__ == "__main__":

    main()