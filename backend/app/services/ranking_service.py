from app.services.job_filter import is_relevant_job


def calculate_rank_score(job):

    score = job.ai_score or 0

    title = (job.title or "").lower()
    description = (job.description or "").lower()

    text = title + " " + description

    cyber_terms = [
        "security",
        "cyber",
        "soc",
        "siem",
        "incident response",
        "vulnerability"
    ]

    if any(term in text for term in cyber_terms):
        score += 5

    entry_terms = [
        "graduate",
        "junior",
        "associate",
        "intern",
        "entry"
    ]

    if any(term in text for term in entry_terms):
        score += 10

    senior_terms = [
        "senior",
        "staff",
        "principal",
        "manager",
        "director",
        "lead"
    ]

    if any(term in title for term in senior_terms):
        score -= 30

    return score


def rank_jobs(jobs):

    ranked = []

    for job in jobs:

        job_dict = {
            "title": job.title,
            "description": job.description or ""
        }

        if not is_relevant_job(job_dict):
            continue

        ranked.append({
            "id": job.id,
            "title": job.title,
            "company": job.company,
            "location": job.location,
            "ai_score": calculate_rank_score(job),
            "cv_type": job.cv_type,
            "status": job.status,
            "url": job.url
        })

    ranked.sort(
        key=lambda x: x["ai_score"],
        reverse=True
    )

    return ranked[:10]