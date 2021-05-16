from sqlalchemy.orm import Session

import models


class User:
    def get_user_by_id(self, db: Session, user_id: int):
        return db.query(models.User).filter_by(id=user_id).first()

    def get_user_by_username(self, db: Session, username: str):
        return db.query(models.User).filter_by(username=username).first()

    def get_user_by_phone(self, db: Session, phone: str):
        return db.query(models.User).filter_by(phone=phone).first()

    def get_user_by_email(self, db: Session, email: str):
        return db.query(models.User).filter_by(email=email).first()

    def get_user_list(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.User).all()


user = User()
