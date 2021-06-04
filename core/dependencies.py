#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : dependencies.py
# @Time   : 2021/06/04 22:21
from db.session import SessionLocal


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
