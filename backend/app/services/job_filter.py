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
    "forensics"
]


ENTRY_KEYWORDS = [
    "graduate",
    "junior",
    "associate",
    "analyst",
    "engineer",
    "intern",
    "entry",
    "l1",
    "level 1",
    "early career"
]


SENIOR_KEYWORDS = [
    "senior",
    "sr.",
    "staff",
    "principal",
    "lead",
    "manager",
    "director",
    "head",
    "architect",
    "vp",
    "5+ years",
    "7+ years",
    "10+ years"
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


    text = title + " " + description



    # Must be cybersecurity related

    cyber_match = any(
        keyword in text
        for keyword in CYBER_KEYWORDS
    )


    if not cyber_match:
        return False



    # Reject senior roles

    senior_match = any(
        keyword in title
        for keyword in SENIOR_KEYWORDS
    )


    if senior_match:
        return False



    # Prefer entry roles

    entry_match = any(
        keyword in text
        for keyword in ENTRY_KEYWORDS
    )


    if entry_match:
        return True



    # Allow security engineer/analyst titles

    if (
        "security engineer" in title
        or
        "security analyst" in title
    ):
        return True



    return False