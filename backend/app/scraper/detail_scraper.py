import requests
from bs4 import BeautifulSoup


def extract_job_description(url):

    if not url:
        return ""


    try:

        response = requests.get(
            url,
            timeout=15,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )


        if response.status_code != 200:
            return ""


        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )


        # Remove unwanted elements

        for tag in soup(
            [
                "script",
                "style",
                "nav",
                "footer"
            ]
        ):
            tag.extract()



        text = soup.get_text(
            separator=" ",
            strip=True
        )


        return text[:5000]


    except Exception as error:

        print(
            "Description extraction error:",
            error
        )

        return ""