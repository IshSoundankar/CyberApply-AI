from app.scraper.greenhouse import get_greenhouse_jobs
from app.scraper.lever import get_lever_jobs
from app.scraper.workday import get_workday_jobs


SCRAPER_REGISTRY = {

    "greenhouse": get_greenhouse_jobs,

    "lever": get_lever_jobs,

    "workday": get_workday_jobs

}


def get_scraper(platform):

    return SCRAPER_REGISTRY.get(platform)