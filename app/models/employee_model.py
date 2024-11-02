from datetime import datetime

from core.db.base import Base
from sqlalchemy import Column, String, Integer, func, Date


class Employee(Base):
    __tablename__ = "employees"
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    department = Column(String, nullable=True)
    role = Column(String, nullable=True)
    date_joined = Column(Date, server_default=func.now())