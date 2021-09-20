#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : tag.py
# @Time   : 2021/06/04 23:13
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Boolean, Column, Field, SQLModel, String, Relationship

from . import Base
from .base import TimeStampMixin
from .article_tag_link import ArticleTagLink

if TYPE_CHECKING:
    from . import Article


class TagBase(Base, TimeStampMixin):
    title: str = Field(sa_column=Column(String(50), nullable=False, comment='标题'))
    is_delete: bool = Field(sa_column=Column(Boolean, default=False, nullable=False, comment='是否删除'))
    article: List["Article"] = Relationship(back_populates="tag", link_model=ArticleTagLink)  # 文章


class Tag(TagBase, table=True):
    pass


class TagCreate(SQLModel):
    title: str


class TagUpdate(SQLModel):
    title: Optional[str] = None


class TagRead(TagBase):
    id: int
