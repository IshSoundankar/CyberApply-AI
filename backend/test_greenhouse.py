from app.scraper.greenhouse import get_greenhouse_jobs


jobs = get_greenhouse_jobs(
    "cloudflare"
)


for job in jobs:
    print(job)