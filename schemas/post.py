#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : post.py
# @Time   : 2021/06/04 22:12
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
