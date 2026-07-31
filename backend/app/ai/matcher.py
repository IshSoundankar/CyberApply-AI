from app.ai.profile_loader import load_profiles


JUNIOR_WORDS = [
    "junior",
    "graduate",
    "entry",
    "associate",
    "intern",
    "trainee"
]


def calculate_score(job_text, profile):

    job_text = job_text.lower()

    score = 0

    skills = profile.get("skills", [])
    roles = profile.get("roles", [])


    for skill in skills:

        if skill.lower() in job_text:
            score += 5


    for role in roles:

        if role.lower() in job_text:
            score += 10


    # bonus for graduate/junior roles
    if any(
        word in job_text
        for word in JUNIOR_WORDS
    ):
        score += 10


    return score



def normalize_score(score):

    # cap score at 100
    return min(score, 100)



def match_job(job):

    profiles = load_profiles()


    text = (
        job.get("title", "")
        + " "
        + job.get("description", "")
    )


    results = []


    for profile in profiles:

        score = calculate_score(
            text,
            profile
        )


        results.append(
            {
                "profile": profile["name"],
                "match": normalize_score(score),
                "cv": profile["cv_file"]
            }
        )


    results.sort(
        key=lambda x: x["match"],
        reverse=True
    )


    return results



if __name__ == "__main__":


    test_job = {

        "title":
        "Graduate SOC Analyst",

        "description":
        """
        SIEM monitoring
        Wazuh
        incident response
        Linux
        Python
        threat detection
        """
    }


    matches = match_job(test_job)


    print("\nJob Match Results\n")


    for match in matches:

        print(
            f'{match["profile"]}: '
            f'{match["match"]}% '
            f'({match["cv"]})'
        )