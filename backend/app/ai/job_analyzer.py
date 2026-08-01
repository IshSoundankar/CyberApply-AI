from app.ai.matcher import calculate_match



def analyze_job(job):

    result = calculate_match(job)


    score = result["match"]


    if score >= 70:

        recommendation = "APPLY"


    elif score >= 40:

        recommendation = "CONSIDER"


    else:

        recommendation = "SKIP"



    return {

        "title":
            job.get(
                "title",
                ""
            ),


        "company":
            job.get(
                "company",
                ""
            ),


        "score":
            score,


        "cv_type":
            result["profile"],


        "matched_skills":
            result["matched_skills"],


        "missing_skills":
            result["missing_skills"],


        "recommendation":
            recommendation

    }