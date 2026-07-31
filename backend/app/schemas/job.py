from pydantic import BaseModel


class JobCreate(BaseModel):
    title: str
    company: str
    location: str | None = None
    url: str | None = None
    source: str | None = None
    description: str | None = None


class JobResponse(JobCreate):
    id: int
    status: str
    ai_score: int
    cv_type: str | None

    class Config:
        from_attributes = True