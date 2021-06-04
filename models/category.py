#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : category.py
# @Time   : 2021/06/04 23:14
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from db import Base


class Category(Base):
    __tablename__ = "categories"

    name = Column(String(20), unique=True, index=True)
    posts = relationship("Post", backref="category")
