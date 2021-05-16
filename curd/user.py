from sqlalchemy.orm import Session

import models
from models.user import make_password
from schemas.user import UserCreate, User


class CRUDUser:
    def create_user(self, db: Session, obj: UserCreate):
        password = make_password(obj.raw_password)
        delattr(obj, "raw_password")
        print(obj.dict())
        user = models.User(**obj.dict(), password=password)
        self.save(db, user)
        return user

    def get_user_by_id(self, db: Session, user_id: int):
        return db.query(models.User).filter_by(id=user_id).first()

    def get_user_by_phone(self, db: Session, phone: str):
        return db.query(models.User).filter_by(phone=phone).first()

    def get_user_by_email(self, db: Session, email: str):
        return db.query(models.User).filter_by(email=email).first()

    def get_user_list(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.User).all()

    def update_user(self, db: Session, user_id: int, obj: User):
        user = self.get_user_by_id(db, user_id)
        user = user(**obj.dict())
        self.save(db, user)
        return user

    def delete_user(self, db: Session, user_id: int):
        user = db.query(models.User).filter_by(id=user_id).first()
        print(user)
        db.delete(user)
        db.commit()
        return

    def save(self, db, obj):
        db.add(obj)
        db.commit()
        db.flush(obj)


user_obj = CRUDUser()
