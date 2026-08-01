import json

from app.database.database import Base, engine, SessionLocal

# Register SQLAlchemy models BEFORE create_all
from app.models.job import Job

from app.services.job_service import save_job
from app.scraper.registry import get_scraper
from app.services.job_filter import is_relevant_job



def load_companies():

    with open("companies.json", "r") as file:
        return json.load(file)



def main():

    print(
        "Tables:",
        Base.metadata.tables.keys()
    )


    Base.metadata.create_all(
        bind=engine
    )


    db = SessionLocal()


    try:

        companies = load_companies()


        for company in companies:


            print(
                f"\nChecking {company['company']}..."
            )


            scraper = get_scraper(
                company["platform"]
            )


            if not scraper:

                print(
                    "No scraper found"
                )

                continue



            jobs = scraper(
                company["board"]
            )



            for job_data in jobs:


                print(
                    f"Extracting: {job_data.get('title')}"
                )


                # Add company name
                job_data["company"] = company["company"]



                # Filter jobs before saving
                if not is_relevant_job(job_data):

                    print(
                        f"Skipped: {job_data.get('title')}"
                    )

                    continue




                saved = save_job(
                    db,
                    job_data
                )



                print(
                    f"Saved: {saved.title} | Score: {saved.ai_score}"
                )



    except Exception as e:

        print(
            "ERROR:",
            e
        )



    finally:

        db.close()




if __name__ == "__main__":

    main()