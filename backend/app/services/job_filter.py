CYBER_KEYWORDS = [
    "security",
    "cyber",
    "soc",
    "siem",
    "incident response",
    "threat",
    "vulnerability",
    "penetration",
    "pentest",
    "network security",
    "cloud security",
    "application security",
    "iam",
    "identity",
    "risk",
    "compliance",
    "malware",
    "forensics",
    "firewall",
    "security operations"
]


ENTRY_KEYWORDS = [
    "graduate",
    "junior",
    "associate",
    "analyst",
    "intern",
    "entry",
    "early career",
    "level 1",
    "l1",
    "new grad",
    "trainee"
]


SENIOR_KEYWORDS = [
    "senior",
    "sr ",
    "staff",
    "principal",
    "lead",
    "manager",
    "director",
    "head",
    "architect",
    "vp",
    "chief",
    "5+ years",
    "4+ years",
    "7+ years",
    "10+ years"
]


ALLOWED_TITLES = [
    "security engineer",
    "security analyst",
    "cyber security analyst",
    "network security engineer",
    "soc analyst",
    "vulnerability analyst",
    "incident response analyst",
    "threat analyst",
    "security operations analyst"
]


def is_relevant_job(job):

    title = job.get(
        "title",
        ""
    ).lower()

    description = job.get(
        "description",
        ""
    ).lower()

    text = f"{title} {description}"


    cyber_match = any(
        keyword in text
        for keyword in CYBER_KEYWORDS
    )

    if not cyber_match:
        return False


    senior_match = any(
        keyword in title
        for keyword in SENIOR_KEYWORDS
    )

    if senior_match:
        return False


    entry_match = any(
        keyword in text
        for keyword in ENTRY_KEYWORDS
    )

    if entry_match:
        return True


    for role in ALLOWED_TITLES:
        if role in title:
            return True


    return False