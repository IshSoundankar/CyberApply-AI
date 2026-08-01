from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.database.database import Base


class Job(Base):

    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)
    company = Column(String)
    location = Column(String)

    url = Column(String, nullable=True)

    source = Column(String)

    description = Column(Text, nullable=True)

    # AI
    ai_score = Column(Integer, default=0)
    cv_type = Column(String, nullable=True)

    # Application tracking
    status = Column(
        String,
        default="NEW"
    )

    applied_date = Column(
        DateTime,
        nullable=True
    )

    notes = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )