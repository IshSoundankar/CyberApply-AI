from app.scraper.greenhouse import get_greenhouse_jobs


SCRAPER_REGISTRY = {

    "greenhouse": get_greenhouse_jobs

}


def get_scraper(platform):

    return SCRAPER_REGISTRY.get(platform)