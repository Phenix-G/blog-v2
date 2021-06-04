#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : user.py
# @Time   : 2021/06/04 22:13
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    phone: Optional[str] = None
    description: Optional[str] = None
    email: Optional[EmailStr] = None


class UserCreate(UserBase):
    raw_password: str


class User(UserBase):
    pass

    class Config:
        orm_mode = True
