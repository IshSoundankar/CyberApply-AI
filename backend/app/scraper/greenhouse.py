import requests
from app.scraper.detail_scraper import extract_job_description

GREENHOUSE_URL = "https://boards-api.greenhouse.io/v1/boards/{}/jobs"


CYBER_KEYWORDS = [
    "security",
    "cyber",
    "soc",
    "penetration",
    "pentest",
    "network",
    "vulnerability",
    "threat",
    "incident"
]


LEVEL_KEYWORDS = [
    "junior",
    "graduate",
    "entry",
    "associate",
    "intern",
    "trainee"
]


def get_greenhouse_jobs(company_board):

    url = GREENHOUSE_URL.format(company_board)

    response = requests.get(
        url,
        timeout=10
    )

    if response.status_code != 200:
        return []

    data = response.json()

    jobs = []

    for job in data.get("jobs", []):

        title = job.get("title", "")

        location = job.get(
            "location",
            {}
        ).get(
            "name",
            ""
        )


        title_lower = title.lower()


        if any(
            word in title_lower
            for word in CYBER_KEYWORDS
        ):

            job_url = job.get("absolute_url")

            description = extract_job_description(job_url)
            print(
                f"Description length: {len(description)}"
            )
            jobs.append(
                {
                    "title": title,
                    "company": company_board,
                    "location": location,
                    "url": job_url,
                    "description": description,
                    "source": "Greenhouse"
                }
            )


    return jobs