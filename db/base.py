#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : base.py
# @Time   : 2021/06/04 22:15
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import Session


@as_declarative()
class Base:
    __name__: str
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def save(self, db, obj):
        db.add(obj)
        db.commit()
        db.flush(obj)

    @classmethod
    def query(cls, db: Session):
        return db.query(cls)
