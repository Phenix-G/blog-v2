#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : session.py
# @Time   : 2021/06/04 22:18
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import DATABASES, ENVIRONMENT

ENVIRONMENT = ENVIRONMENT if ENVIRONMENT else 'development'

DATABASE_URL = 'mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}?charset=utf8'.format(**DATABASES[ENVIRONMENT])

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
