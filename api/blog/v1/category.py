#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : category.py
# @Time   : 2021/06/05 1:47
from fastapi import APIRouter, Depends
from sqlalchemy import exists
from sqlalchemy.orm import Session
from starlette.requests import Request

from core.dependencies import get_db
from models.category import Category
from schemas.category import CategoryCreate

router = APIRouter()


@router.get('/')
async def index(db: Session = Depends(get_db)) -> dict:
    categories = Category.query(db).all()
    return {'code': 0, 'data': categories}


@router.get('/{category_id}')
async def show(category_id: int, db: Session = Depends(get_db)) -> dict:
    category = Category.query(db).filter(Category.id == category_id).first()
    return {'code': 0, 'data': category}


@router.post('/')
async def create(obj: CategoryCreate, db: Session = Depends(get_db)):
    obj = obj.dict()
    if obj['name']:
        category = Category.query(db).filter_by(name=obj['name']).first()
        if category:
            return {'code': 200, 'result': '分类已存在', 'data': []}
        category = Category(**obj)
        category.save(db, category)
        return {'code': 201, 'result': '创建分类成功', 'data': []}
    else:
        return {'code': 400, 'result': '分类名称不能为空', 'data': []}


@router.put('/{category_id}')
async def update(obj: CategoryCreate, category_id: int, db: Session = Depends(get_db)):
    category = Category.query(db).filter_by(id=category_id)
    if category.first():
        obj = obj.dict()
        if obj['name']:
            category.update(obj)
            db.commit()
        return {'code': 200, 'result': '分类修改成功', 'data': []}
    else:
        return {'code': 404, 'result': '分类不存在', 'data': []}


@router.delete('/{category_id}')
async def delete(category_id: int, db: Session = Depends(get_db)):
    category = Category.query(db).filter_by(id=category_id)
    if category.first():
        category.delete()
        db.commit()
        return {'code': 200, 'result': '分类删除成功', 'data': []}
    else:
        return {'code': 404, 'result': '分类不存在', 'data': []}
