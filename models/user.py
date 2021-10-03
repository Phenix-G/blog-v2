#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : user.py
# @Time   : 2021/06/04 23:12
from typing import Optional
from uuid import uuid4, uuid5, UUID

from sqlmodel import Boolean, Column, Field, SQLModel, String
from werkzeug.security import generate_password_hash, check_password_hash

from . import base


class UserBase(base.Model):
    uuid: UUID = Field(sa_column=Column(String(36), unique=True, nullable=False))
    username: str = Field(sa_column=Column(String(20), unique=True, index=True, nullable=False, comment='用户名'))
    email: Optional[str] = Field(
        sa_column=Column(String(40), unique=True, index=True, nullable=True, comment='邮箱')
    )
    password: str = Field(sa_column=Column(String(102), nullable=False, comment='密码'))
    phone: str = Field(sa_column=Column(String(11), unique=True, index=True, nullable=False, comment='手机号'))
    description: Optional[str] = Field(default='', index=False)  # 描述
    is_active: bool = Field(sa_column=Column(Boolean, default=False, comment='激活状态'))
    is_admin: bool = Field(sa_column=Column(Boolean, default=False, comment='管理员状态'))
    ip_address: str = Field(default='', index=False)  # ip地址


class User(UserBase, table=True):
    def save(self):
        self.__generate_uuid()
        self.__make_password(self.password)
        super().save()

    def set_password(self, raw_password):
        return self.__make_password(raw_password)

    def __make_password(self, raw_password):
        self.password = generate_password_hash(raw_password, method="pbkdf2:sha256:216000", salt_length=16)

    def check_password(self, raw_password: str) -> bool:
        return check_password_hash(self.password, raw_password)

    def __generate_uuid(self):
        namespace = uuid4()
        self.uuid = uuid5(namespace, self.username)


class UserCreate(SQLModel):
    username: str
    password: str
    phone: str
    email: str
    description: Optional[str]


class UserRead(SQLModel):
    id: int
    uuid: UUID
    username: str
    email: str
    phone: str
    description: str
    is_active: bool
    is_admin: bool
    ip_address: str


class UserUpdate(SQLModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[str] = None
    description: Optional[str] = None
