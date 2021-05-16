from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    phone: Optional[str] = None
    description: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: bool = False
    is_admin: bool = False


class UserCreate(UserBase):
    raw_password: str


class UserUpdate(UserBase):
    raw_password: Optional[str] = None


class UserAdmin(UserBase):
    pass


class User(UserBase):
    pass

    class Config:
        orm_mode = True
