from sqlalchemy import Column, TIMESTAMP


class TimeStampMixin:
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP)
