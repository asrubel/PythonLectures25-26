from pydantic import BaseModel, EmailStr, Field
from uuid import UUID, uuid4
from datetime import date
from enum import Enum


class Department(Enum):
    HR = "HR"
    SALES = "SALES"
    IT = "IT"
    ENGINEERING = "ENGINEERING"


class Employee(BaseModel):
    employee_id: UUID = uuid4()
    name: str
    email: EmailStr
    date_of_birth: date
    salary: float
    department: Department
    elected_benefits: bool


class CustomEmployee(BaseModel):
    employee_id: UUID = Field(default_factory=uuid4, frozen=True)
    name: str = Field(min_length=1, max_length=50, frozen=True)
    email: EmailStr = Field(pattern=r".+@example\.com$", max_length=50)
    date_of_birth: date = Field(alias="birth_date", repr=False, frozen=True)
    salary: float = Field(gt=0, repr=False)
    department: Department
    elected_benefits: bool
