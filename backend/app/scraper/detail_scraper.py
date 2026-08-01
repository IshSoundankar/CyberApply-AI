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


        # Remove unwanted sections

        for tag in soup(
            [
                "script",
                "style",
                "nav",
                "footer",
                "header"
            ]
        ):
            tag.decompose()



        # Greenhouse specific content

        description = soup.find(
            id="content"
        )


        if description:

            text = description.get_text(
                separator=" ",
                strip=True
            )

        else:

            text = soup.get_text(
                separator=" ",
                strip=True
            )


        # Remove repeated whitespace

        text = " ".join(
            text.split()
        )


        return text[:8000]


    except Exception as error:

        print(
            "Description extraction error:",
            error
        )

        return ""