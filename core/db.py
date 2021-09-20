#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : db.py
# @Time   : 2021/09/21 2:09
from sqlmodel import Session

from db.session import engine


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
