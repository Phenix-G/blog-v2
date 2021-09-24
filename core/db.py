#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : db.py
# @Time   : 2021/09/21 2:09
from sqlmodel import Session, create_engine

DATABASE_URL = 'mysql://root:root@localhost:3306/fastapi?charset=utf8'
engine = create_engine(DATABASE_URL)


class DBSession:
    session = None
    init = None

    def __new__(cls):
        if cls.session is None:
            cls.session = Session(engine)
            super().__new__(cls)
        return cls.session

    def __init__(self):
        if DBSession.init:
            return

        DBSession.init = True


session = DBSession()
