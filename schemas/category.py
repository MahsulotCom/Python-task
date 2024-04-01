from pydantic import BaseModel
from typing import Optional


class CategoryBase(BaseModel):
    title: str
    description: Optional[str] = ''


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    id: int
