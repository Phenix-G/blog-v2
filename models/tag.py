#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : tag.py
# @Time   : 2021/06/04 23:13
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .many_to_many import post_tag_table
from db import Base


class Tag(Base):
    __tablename__ = "tags"

    name = Column(String(20), unique=True, index=True)
    posts = relationship("Post", secondary=post_tag_table, backref='tags')
