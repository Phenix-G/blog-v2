#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : user.py
# @Time   : 2021/06/04 23:12
from typing import Optional
from uuid import uuid4, uuid5, UUID

from pydantic import EmailStr
from sqlmodel import Boolean, Column, Field, SQLModel, String
from werkzeug.security import generate_password_hash, check_password_hash

from .base import Base, TimeStampMixin


class UserBase(Base, TimeStampMixin):
    uuid: UUID = Field(sa_column=Column(String(36), unique=True, nullable=False))
    username: str = Field(sa_column=Column(String(20), unique=True, index=True, nullable=False, comment='用户名'))
    email: Optional[EmailStr] = Field(
        sa_column=Column(String(40), unique=True, index=True, nullable=True, comment='邮箱')
    )
    password: str = Field(sa_column=Column(String(102), nullable=False, comment='密码'))
    phone: str = Field(sa_column=Column(String(11), unique=True, index=True, nullable=False, comment='手机号'))
    description: Optional[str] = Field(default='', index=False)  # 描述
    is_active: bool = Field(sa_column=Column(Boolean, default=False, comment='激活状态'))
    is_admin: bool = Field(sa_column=Column(Boolean, default=False, comment='管理员状态'))
    ip_address: str = Field(default='', index=False)  # ip地址


class User(UserBase, table=True):
    pass


class UserCreate(SQLModel):
    username: str
    password: str
    phone: str
    email: str
    description: Optional[str]


class UserRead(UserBase):
    id: int
    description: str
    email: str


class UserUpdate(SQLModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    phone: Optional[str] = None
    description: Optional[str] = None
