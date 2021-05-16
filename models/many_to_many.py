from sqlalchemy import Table, Column, Integer, ForeignKey

from db import Base

post_tag_table = Table(
    'post_tag',
    Base.metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('post_id', Integer, ForeignKey('posts.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)
