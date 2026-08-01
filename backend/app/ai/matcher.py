from app.ai.profile_loader import load_profiles


profiles = load_profiles()


def calculate_match(job):

    title = job.get(
        "title",
        ""
    ).lower()


    description = job.get(
        "description",
        ""
    ).lower()


    text = title + " " + description


    best_profile = None
    best_score = 0

    best_matches = []


    for profile in profiles:

        score = 0

        matches = []


        # Skill matching

        for skill in profile["skills"]:

            if skill.lower() in text:

                score += 5

                matches.append(skill)



        # Role matching

        for role in profile["roles"]:

            if role.lower() in title:

                score += 20



        # Bonus for junior roles

        junior_keywords = [
            "junior",
            "graduate",
            "associate",
            "analyst",
            "intern",
            "entry",
            "early career"
        ]


        for keyword in junior_keywords:

            if keyword in title:

                score += 10



        if score > best_score:

            best_score = score

            best_profile = profile

            best_matches = matches



    missing = []

    if best_profile:

        missing = [
            skill
            for skill in best_profile["skills"]
            if skill not in best_matches
        ]



    return {

        "profile":
            best_profile["name"]
            if best_profile
            else "Unknown",


        "match":
            min(best_score,100),


        "matched_skills":
            best_matches,


        "missing_skills":
            missing
    }