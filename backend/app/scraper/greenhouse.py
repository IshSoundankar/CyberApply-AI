import requests


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

            jobs.append(
                {
                    "title": title,
                    "location": location,
                    "url": job.get("absolute_url"),
                    "source": "Greenhouse"
                }
            )


    return jobs