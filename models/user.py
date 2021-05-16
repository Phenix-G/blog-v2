from sqlalchemy import Boolean, Column, String, LargeBinary
from werkzeug.security import generate_password_hash, check_password_hash

from db import Base
from models.mixins import TimeStampMixin


def make_password(raw_password: str) -> str:
    return generate_password_hash(raw_password, method="pbkdf2:sha256:216000", salt_length=16)


def check_password(password: str, raw_password: str) -> bool:
    return check_password_hash(password, raw_password)


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
