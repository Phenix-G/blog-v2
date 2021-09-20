#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : base.py
# @Time   : 2021/09/11 1:26
from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from sqlmodel import Column, SQLModel, Field, TIMESTAMP, select

from core.db import session


class Base(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)

    @classmethod
    def get(cls, obj_id):
        return cls.__session().get(cls, obj_id)

    @classmethod
    def all(cls):
        return cls.__session().exec(select(cls)).all()

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        cls.save(obj)
        return obj

    def update(self, update_obj):
        for key, value in update_obj.items():
            setattr(self, key, value)
        self.save(self)
        return self

    @classmethod
    def save(cls, obj):
        cls.__session().add(obj)
        cls.__session().commit()
        cls.__session().refresh(obj)

    def delete(self):
        self.__session().delete(self)
        self.__session().commit()

    def row_delete(self):
        setattr(self, 'is_delete', True)
        self.save(self)

    @classmethod
    def __session(cls):
        return session


class TimeStampMixin(BaseModel):
    created_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP,
            default=datetime.now,
            comment='创建时间'
        )
    )

    updated_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP,
            onupdate=datetime.now,
            comment='更新时间'
        )
    )
