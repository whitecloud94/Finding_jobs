from typing import Optional
from pydantic import BaseModel, EmailStr


#유저 생성하는
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str