import requests


def get_smartrecruiter_jobs(company):

    url = (
        f"https://api.smartrecruiters.com/"
        f"v1/companies/{company}/postings"
    )

    results = []


    try:

        response = requests.get(
            url,
            timeout=10
        )


        if response.status_code != 200:
            return results


        data = response.json()


        for job in data.get(
            "content",
            []
        ):

            results.append(
                {
                    "title": job.get(
                        "name",
                        ""
                    ),

                    "location": job.get(
                        "location",
                        {}
                    ).get(
                        "city",
                        ""
                    ),

                    "description": "",

                    "url": job.get(
                        "ref",
                        ""
                    ),

                    "source": "SmartRecruiters"
                }
            )


    except Exception as e:

        print(
            "SmartRecruiters error:",
            company,
            e
        )


    return results