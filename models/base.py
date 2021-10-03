#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : base.py
# @Time   : 2021/09/11 1:26
from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from sqlmodel import Column, SQLModel, Field, TIMESTAMP, select

from core.settings import session


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
        obj.save()
        return obj

    def update(self, update_obj):
        for key, value in update_obj.items():
            setattr(self, key, value)
        self.save()
        return self

    def save(self):
        self.__session().add(self)
        self.__session().commit()
        self.__session().refresh(self)

    def delete(self):
        self.__session().delete(self)
        self.__session().commit()

    def row_delete(self):
        setattr(self, 'is_delete', True)
        self.save()

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


class Model(Base, TimeStampMixin):
    pass
