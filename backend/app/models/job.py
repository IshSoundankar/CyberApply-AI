from sqlalchemy import Column, Integer, String, Text

from app.database.database import Base


class Job(Base):

    __tablename__ = "jobs"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    title = Column(
        String,
        nullable=False
    )


    company = Column(
        String,
        nullable=False
    )


    location = Column(
        String
    )


    url = Column(
        String
    )


    source = Column(
        String
    )


    description = Column(
        Text
    )


    status = Column(
        String,
        default="NEW"
    )


    ai_score = Column(
        Integer,
        default=0
    )


    cv_type = Column(
        String
    )