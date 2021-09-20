#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : article_tag_link.py
# @Time   : 2021/09/20 23:03
from typing import Optional

from sqlmodel import Field
from .base import Base, TimeStampMixin


class ArticleTagLink(Base, TimeStampMixin, table=True):
    article_id: Optional[int] = Field(
        default=None, foreign_key="article.id", primary_key=True
    )
    tag_id: Optional[int] = Field(
        default=None, foreign_key="tag.id", primary_key=True
    )
