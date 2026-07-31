from app.ai.profile_loader import load_profiles


def calculate_score(job_text, profile):

    job_text = job_text.lower()

    score = 0

    skills = profile.get(
        "skills",
        []
    )

    roles = profile.get(
        "roles",
        []
    )


    for skill in skills:

        if skill.lower() in job_text:
            score += 5


    for role in roles:

        if role.lower() in job_text:
            score += 10


    return score



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
                "score": score,
                "cv": profile["cv_file"]
            }
        )


    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )


    return results



if __name__ == "__main__":


    test_job = {
        "title": "SOC Analyst",
        "description":
        """
        SIEM monitoring,
        Wazuh,
        incident response,
        threat detection
        """
    }


    result = match_job(test_job)


    for r in result:
        print(r)