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
    "new grad"

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
    "chief"

]



EXPERIENCE_REJECT = [

    "5+ years",
    "7+ years",
    "8+ years",
    "10+ years",
    "minimum 5 years",
    "minimum 7 years"

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






    # Remove obvious senior titles

    senior_match = any(

        keyword in title

        for keyword in SENIOR_KEYWORDS

    )



    if senior_match:

        return False







    # Remove jobs requiring too much experience

    experience_match = any(

        keyword in description

        for keyword in EXPERIENCE_REJECT

    )



    if experience_match:

        return False








    # Accept junior indicators

    entry_match = any(

        keyword in text

        for keyword in ENTRY_KEYWORDS

    )



    if entry_match:

        return True







    # Allow common starter cybersecurity roles

    allowed_titles = [

        "security engineer",

        "security analyst",

        "cyber security analyst",

        "cybersecurity analyst",

        "network security engineer",

        "soc analyst",

        "vulnerability analyst",

        "incident response analyst",

        "security operations analyst"

    ]




    for role in allowed_titles:


        if role in title:

            return True





    return False