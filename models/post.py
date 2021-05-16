from sqlalchemy import Column, Integer, String, ForeignKey, Text

from db import Base


class Post(Base):
    __tablename__ = "posts"

    title = Column(String(50), index=True)
    description = Column(String(255), nullable=True)
    content = Column(Text)
    category_id = Column(Integer, ForeignKey("categories.id"))
