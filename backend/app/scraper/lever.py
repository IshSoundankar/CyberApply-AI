import requests


def get_lever_jobs(company):

    url = f"https://api.lever.co/v0/postings/{company}?mode=json"


    response = requests.get(
        url,
        timeout=10
    )


    if response.status_code != 200:
        return []


    jobs = response.json()


    results = []


    for job in jobs:

        results.append(
            {
                "title": job.get("text"),

                "location": job.get(
                    "categories",
                    {}
                ).get(
                    "location",
                    ""
                ),

                "url": job.get(
                    "hostedUrl"
                ),

                "description": job.get(
                    "descriptionPlain",
                    ""
                ),

                "source": "Lever"
            }
        )


    return results