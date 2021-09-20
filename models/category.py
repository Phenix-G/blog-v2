#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : category.py
# @Time   : 2021/06/04 23:14
from typing import Optional, List, TYPE_CHECKING

from sqlmodel import Boolean, Field, Column, String, SQLModel, Relationship

from .base import Base, TimeStampMixin

if TYPE_CHECKING:
    from . import Article


class CategoryBase(Base, TimeStampMixin):
    title: str = Field(sa_column=Column(String(50), nullable=False, comment='标题'))
    is_delete: bool = Field(sa_column=Column(Boolean, default=False, nullable=False, comment='是否删除'))
    article: List["Article"] = Relationship(back_populates="category")


class Category(CategoryBase, table=True):
    pass


class CategoryCreate(SQLModel):
    title: str


class CategoryUpdate(SQLModel):
    title: Optional[str] = None


class CategoryRead(CategoryBase):
    id: int
