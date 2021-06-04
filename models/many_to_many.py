#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : many_to_many.py
# @Time   : 2021/06/04 23:15
from sqlalchemy import Table, Column, Integer, ForeignKey

from db import Base

post_tag_table = Table(
    'post_tag',
    Base.metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('post_id', Integer, ForeignKey('posts.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)
