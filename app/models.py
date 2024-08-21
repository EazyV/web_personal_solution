from pydantic import BaseModel, EmailStr
from typing import Optional


class ApplicantData(BaseModel):
    applicant_name: str
    applicant_phone: str


class CustomerData(BaseModel):
    customer_name: str
    customer_phone: str
    customer_email: Optional[EmailStr]
