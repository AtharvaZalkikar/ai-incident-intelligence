from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    node_id = Column(String)
    alarm_type = Column(String)
    severity = Column(String)
    region = Column(String)
    failure_reason = Column(String)