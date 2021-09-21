#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : user.py
# @Time   : 2021/06/04 22:53
from fastapi import APIRouter

from models.user import User, UserCreate, UserUpdate

router = APIRouter()


@router.get('/')
async def get_list():
    users = User.all()
    return {'data': users}


@router.get('/{user_id}')
async def get(user_id: int):
    user = User.get(user_id)
    return {'data': user}


@router.post('/')
async def create(obj: UserCreate):
    user = User.create(**obj.dict())
    return {'data': user}


@router.put('/{user_id}')
async def update(user_id: int, obj: UserUpdate):
    user = User.get(user_id)
    data = obj.dict(exclude_unset=True)
    user.update(data)
    return {'data': user}


@router.delete('/{user_id}')
async def delete(user_id: int):
    user = User.get(user_id)
    user.row_delete()
    return {'data': ''}
