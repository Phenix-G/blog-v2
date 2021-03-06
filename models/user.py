#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : user.py
# @Time   : 2021/06/04 23:12
from uuid import uuid4, uuid5

from sqlalchemy import Column, String, Boolean
from werkzeug.security import generate_password_hash, check_password_hash

from db import Base
from models.mixins import TimeStampMixin


class User(Base, TimeStampMixin):
    __tablename__ = "users"

    username = Column(String(20), unique=True, index=True, nullable=False)
    email = Column(String(40), unique=True, index=True)
    uuid = Column(String(255), unique=True, index=True)
    password = Column(String(255), nullable=False)
    phone = Column(String(11), unique=True, index=True, nullable=True)
    description = Column(String(255))
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    ip_address = Column(String(255))

    def save(self, db, obj):
        self._generate_uuid()
        self._make_password(obj.password)
        super().save(db, obj)

    def set_password(self, raw_password):
        return self._make_password(raw_password)

    def _make_password(self, raw_password):
        self.password = generate_password_hash(raw_password, method="pbkdf2:sha256:216000", salt_length=16)

    def _check_password(self, raw_password: str) -> bool:
        return check_password_hash(self.password, raw_password)

    def _generate_uuid(self):
        namespace = uuid4()
        self.uuid = uuid5(namespace, self.username)
