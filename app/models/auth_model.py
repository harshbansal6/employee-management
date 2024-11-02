from core.db.base import Base
from sqlalchemy import Column, String, Integer, func, Date, DateTime


class Auth(Base):
    __tablename__ = "auth"
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())