#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : user.py
# @Time   : 2021/06/04 22:53
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from core.dependencies import get_db
from models import user as model_user
from schemas import user as schema_user
from utils.email import send_email2

router = APIRouter()


@router.get('/')
async def get_list(db: Session = Depends(get_db)) -> dict:
    users = model_user.User.query(db).all()
    return {'code': 200, 'result': '获取成功', 'data': filter_info(jsonable_encoder(users))}


@router.get('/{user_id}')
async def get(user_id: int, db: Session = Depends(get_db)) -> dict:
    user = model_user.User.query(db).filter(model_user.User.id == user_id).first()
    if user:
        return {'code': 200, 'result': '获取成功', 'data': filter_info(jsonable_encoder(user))}
    else:
        return {'code': 200, 'result': '获取成功', 'data': []}


@router.post('/')
async def create(obj: schema_user.UserCreate, db: Session = Depends(get_db)) -> dict:
    obj = obj.dict()
    obj['password'] = obj.pop('raw_password')
    user = model_user.User(**obj)
    obj.pop('password')
    user.save(db, user)
    return {'code': 201, 'result': '注册成功', 'data': obj}


@router.put('/{user_id}')
async def update(obj: schema_user.UserUpdate, user_id: int, db: Session = Depends(get_db)) -> dict:
    user = model_user.User.query(db).filter(model_user.User.id == user_id)
    if user.first():
        user.update(update_info(obj.dict()))
        db.commit()
        return {'code': 200, 'result': '修改成功', 'data': []}
    else:
        return {'code': 200, 'result': '用户不存在', 'data': []}


@router.post('/verify')
def send(email: str):
    send_email2(to_account=email)
    return {'code': 200, 'result': '验证码以发送', 'data': []}


@router.post('/reset')
async def reset(obj: schema_user.Reset, db: Session = Depends(get_db)) -> dict:
    user = model_user.User.query(db).filter(model_user.User.email == obj.email).first()
    if user is None:
        return {'code': 200, 'result': '密码重置完成', 'data': []}

    if 'verify_code' == '':
        return {'code': 200, 'result': '验证码已失效', 'data': []}

    if obj.verify_code == 'verify_code':
        if obj.password == obj.check_password:
            user.set_password('123456')
            user.save(db, user)
            return {'code': 200, 'result': '密码重置完成', 'data': []}
        else:
            return {'code': 200, 'result': '两次密码不一样', 'data': []}
    else:
        return {'code': 200, 'result': '验证码错误', 'data': []}


def filter_info(origin_data):
    if isinstance(origin_data, list):
        for data in origin_data:
            data.pop('password')
            data.pop('updated_at')
            data.pop('uuid')
            data.pop('ip_address')
            data.pop('description')

    elif isinstance(origin_data, dict):
        origin_data.pop('password')
    return origin_data


def update_info(origin_dict):
    update_dict = {k: v for k, v in origin_dict.items() if v is not None}
    origin_dict.clear()
    origin_dict.update(update_dict)
    return origin_dict
