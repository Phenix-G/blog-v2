from uuid import uuid4, uuid5

from sqlalchemy import Boolean, Column, String
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

    def save(self, db, obj):
        self.generate_uuid()
        self.make_password(obj.password)
        super().save(db, obj)

    def make_password(self, raw_password):
        self.password = generate_password_hash(raw_password, method="pbkdf2:sha256:216000", salt_length=16)

    def check_password(self, raw_password: str) -> bool:
        return check_password_hash(self.password, raw_password)

    def generate_uuid(self):
        namespace = uuid4()
        self.uuid = uuid5(namespace, self.username)
