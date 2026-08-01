JUNIOR_KEYWORDS = [
    "junior",
    "graduate",
    "entry",
    "associate",
    "intern",
    "trainee",
    "early career"
]


CYBER_KEYWORDS = [
    "security",
    "cyber",
    "soc",
    "security analyst",
    "incident response",
    "penetration",
    "vulnerability",
    "threat",
    "firewall",
    "network security",
    "cloud security"
]


REJECT_KEYWORDS = [
    "senior",
    "staff",
    "principal",
    "manager",
    "director",
    "lead"
]


def is_relevant_job(job):

    text = (
        job.get("title", "")
        + " "
        + job.get("description", "")
    ).lower()


    # Reject senior roles
    for word in REJECT_KEYWORDS:
        if word in text:
            return False


    cyber_match = any(
        word in text
        for word in CYBER_KEYWORDS
    )


    if not cyber_match:
        return False


    return True