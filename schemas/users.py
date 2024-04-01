from pydantic import BaseModel
from typing import Optional, List


class UserBase(BaseModel):
    name: str
    username: str
    roll: str
    password: str
    number: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    id: int


class Token(BaseModel):
    access_token = str
    token = str


class TokenData(BaseModel):
    id: Optional[str] = None


class UserCurrent(UserBase):
    id: int
    status: bool
    user_status:bool
