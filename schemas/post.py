from typing import Optional

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str


class PostCreate(PostBase):
    content: str
    category: str
    description: Optional[str] = None


class Post(PostCreate):
    id: int
    tag: str

    class Config:
        orm_mode = True
