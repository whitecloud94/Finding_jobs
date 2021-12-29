from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel

# Job의 기본 스키마.
class JobBase(BaseModel):
    title : Optional[str] = None
    company : Optional[str] = None
    company_url : Optional[str] = None
    location : Optional[str] = "Remote"
    description : Optional[str] = None
    date_posted : Optional[date] = datetime.now().date()


# Job 생성 시, 유효성 검사
class JobCreate(JobBase):
    title: str
    company: str
    location: str
    description: str


# 사용자에게 보여지는 Job 스키마.
class ShowJob(BaseModel):
    title: str
    company: str
    company_url: Optional[str]
    location: str
    date_posted: date
    description: Optional[str]

    # 
    class Config():
        orm_mode = True