from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class JobCreate(BaseModel):

    title: str
    company: str
    location: str

    url: Optional[str] = None

    source: str

    description: Optional[str] = None



class JobResponse(BaseModel):

    id: int

    title: str
    company: str
    location: str

    url: Optional[str]

    source: str

    description: Optional[str]

    status: str

    ai_score: int

    cv_type: Optional[str]

    applied_date: Optional[datetime]

    notes: Optional[str]


    class Config:
        from_attributes = True