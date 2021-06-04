#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : mixins.py
# @Time   : 2021/06/04 23:14
from sqlalchemy import Column, TIMESTAMP


class TimeStampMixin:
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP)
