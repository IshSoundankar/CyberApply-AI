import requests


def get_workday_jobs(
    tenant,
    domain,
    limit=50
):
    """
    Example:
    tenant = "tcs"
    domain = "myworkdayjobs.com"
    
    URL:
    https://tcs.wd5.myworkdayjobs.com/wday/cxs/tcs/External/jobs
    """

    url = (
        f"https://{tenant}.{domain}"
        f"/wday/cxs/{tenant}/External/jobs"
    )


    payload = {
        "limit": limit,
        "offset": 0,
        "searchText": ""
    }


    try:

        response = requests.post(
            url,
            json=payload,
            timeout=15
        )


        if response.status_code != 200:
            print(
                "Workday error:",
                response.status_code,
                tenant
            )
            return []


        data = response.json()


    except Exception as e:

        print(
            "Workday exception:",
            e
        )

        return []



    results = []


    for job in data.get(
        "jobPostings",
        []
    ):

        results.append(
            {
                "title": job.get(
                    "title",
                    ""
                ),

                "location": job.get(
                    "locationsText",
                    ""
                ),

                "url": (
                    f"https://{tenant}.{domain}"
                    + job.get(
                        "externalPath",
                        ""
                    )
                ),

                "description": "",

                "source": "Workday"
            }
        )


    return results