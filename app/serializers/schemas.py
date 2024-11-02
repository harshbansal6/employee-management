from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, datetime


class EmployeeBase(BaseModel):
    name: str = Field(..., min_length=1, description="Name cannot be empty")
    email: EmailStr
    department: Optional[str] = None
    role: Optional[str] = None

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    department: Optional[str] = None
    role: Optional[str] = None

class EmployeeOut(EmployeeBase):
    id: int
    date_joined: datetime

    class Config:
        from_attributes = True

    @classmethod
    def from_orm(cls, obj):
        instance = super().from_orm(obj)
        return instance

class UserCreate(BaseModel):
    username: str
    password: str
