#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : article.py
# @Time   : 2021/06/04 23:13
from typing import Optional, TYPE_CHECKING, List

from sqlmodel import Boolean, Column, String, Text, Field, Integer, SQLModel, Relationship

from .base import Base, TimeStampMixin
from .article_link_tag import ArticleLinkTag

if TYPE_CHECKING:
    from . import Category, Tag


class ArticleBase(Base, TimeStampMixin):
    title: str = Field(sa_column=Column(String(50), nullable=False, comment='标题'))
    description: Optional[str] = Field(default='', index=False)  # 描述
    content: str = Field(sa_column=Column(Text, nullable=False, comment='内容'))
    views: int = Field(sa_column=Column(Integer, default=0, comment='浏览量'))
    likes: int = Field(sa_column=Column(Integer, default=0, comment='点赞量'))
    collects: int = Field(sa_column=Column(Integer, default=0, comment='收藏量'))
    shares: int = Field(sa_column=Column(Integer, default=0, comment='分享量'))
    is_delete: bool = Field(sa_column=Column(Boolean, default=False, comment='是否删除'))
    category_id: int = Field(default=None, foreign_key="category.id")
    category: 'Category' = Relationship(back_populates="article")  # 分类
    tag: Optional['Tag'] = Relationship(back_populates='article', link_model=ArticleLinkTag)  # 标签


class Article(ArticleBase, table=True):
    pass


class ArticleCreate(SQLModel):
    title: str
    description: Optional[str] = None
    content: str
    category_id: Optional[int] = None


class ArticleRead(ArticleBase):
    id: int


class ArticleUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    content: Optional[str] = None
