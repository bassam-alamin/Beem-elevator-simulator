import datetime

from sqlalchemy import Column, Text, DateTime, Integer, func, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ElevatorLogs(Base):
    __tablename__ = "elevator_logs"

    id = Column(Integer, primary_key=True)
    elevator_id = Column(Integer, nullable=False)
    event = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    timestamp = Column(DateTime, nullable=True)
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow())
    updated_at = Column(
        DateTime,
        onupdate=func.now())


class QueryLogger(Base):
    __tablename__ = "query_logger"

    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    query = Column(Text, nullable=True)
    location = Column(Text, nullable=True)
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow())
    updated_at = Column(
        DateTime,
        onupdate=func.now())
