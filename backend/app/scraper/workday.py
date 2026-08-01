import requests


def get_workday_jobs(company_url):

    jobs = []


    try:

        response = requests.get(
            company_url,
            timeout=15
        )


        if response.status_code != 200:
            return jobs


        data = response.json()


        for item in data.get("jobPostings", []):

            jobs.append(
                {
                    "title": item.get(
                        "title",
                        ""
                    ),

                    "location": item.get(
                        "locationsText",
                        ""
                    ),

                    "url": item.get(
                        "externalPath",
                        ""
                    ),

                    "description": item.get(
                        "jobDescription",
                        ""
                    ),

                    "source": "Workday"
                }
            )


    except Exception as error:

        print(
            "Workday error:",
            error
        )


    return jobs