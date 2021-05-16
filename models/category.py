from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from db import Base


class Category(Base):
    __tablename__ = "categories"

    name = Column(String(20), unique=True, index=True)
    posts = relationship("Post", backref="category")
