from fastapi import Depends
from sqlalchemy.orm import Session

from db.session import SessionLocal


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def get_current_user(db: Session = Depends(get_db)):
    return
