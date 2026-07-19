from sqlalchemy import Column, Integer, DateTime, Text

from app.database import Base


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)

    start_time = Column(DateTime)

    end_time = Column(DateTime)

    log_count = Column(Integer)

    nodes = Column(Text)

    failure_analysis = Column(Text)

    summary = Column(Text)

    created_at = Column(DateTime)