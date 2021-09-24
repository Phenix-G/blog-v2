#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : article_link_tag.py
# @Time   : 2021/09/20 23:03
from typing import Optional

from sqlmodel import Field
from .base import Base, TimeStampMixin


class ArticleLinkTag(Base, TimeStampMixin, table=True):
    __tablename__ = 'article_link_tag'
    article_id: Optional[int] = Field(
        default=None, foreign_key="article.id", primary_key=True
    )
    tag_id: Optional[int] = Field(
        default=None, foreign_key="tag.id", primary_key=True
    )
