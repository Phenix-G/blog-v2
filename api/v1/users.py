from typing import List

from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from core.dependencies import get_db
from curd.user import user_obj
from schemas import user

router = APIRouter()


@router.get('/', response_model=List[user.User])
def get_users(db: Session = Depends(get_db)):
    users = user_obj.get_user_list(db)
    return users


@router.post("/", response_model=user.User, status_code=status.HTTP_201_CREATED)
def post_user(obj: user.UserCreate, db: Session = Depends(get_db)):
    return user_obj.create_user(db, obj)


@router.get('/{user_id}', response_model=user.User, status_code=status.HTTP_200_OK)
def get_user(user_id: int, db: Session = Depends(get_db)):
    obj_user = user_obj.get_user_by_id(db, user_id)
    return obj_user


@router.put('/{user_id}', response_model=user.User, status_code=status.HTTP_200_OK)
def get_user(*, user_id: int, db: Session = Depends(get_db)):
    obj_user = user_obj.update_user(db, user_id)
    return obj_user


@router.delete('/{user_id}')
def delete(user_id: int, db: Session = Depends(get_db)):
    return user_obj.delete_user(db, user_id)
