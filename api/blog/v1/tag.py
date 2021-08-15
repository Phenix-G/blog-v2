#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : tag.py
# @Time   : 2021/06/05 1:41
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.dependencies import get_db
from models.tag import Tag
from schemas.tag import TagCreate

router = APIRouter()


@router.get('/')
async def index(db: Session = Depends(get_db)) -> dict:
    tags = Tag.query(db).all()
    return {'code': 0, 'data': tags}


@router.get('/{tag_id}')
async def index(tag_id: int, db: Session = Depends(get_db)) -> dict:
    tag = Tag.query(db).filter(Tag.id == tag_id).first()
    return {'code': 0, 'data': tag}


@router.post('/')
async def create(obj: TagCreate, db: Session = Depends(get_db)):
    obj = obj.dict()
    if obj['name']:
        tag = Tag.query(db).filter_by(name=obj['name']).first()
        if tag:
            return {'code': 200, 'result': '标签已存在', 'data': []}
        category = tag(**obj)
        category.save(db, category)
        return {'code': 201, 'result': '创建标签成功', 'data': []}
    else:
        return {'code': 400, 'result': '标签名称不能为空', 'data': []}


@router.put('/{tag_id}')
async def update(obj: TagCreate, tag_id: int, db: Session = Depends(get_db)):
    tag = Tag.query(db).filter_by(id=tag_id)
    if tag.first():
        obj = obj.dict()
        if obj['name']:
            tag.update(obj)
            db.commit()
        return {'code': 200, 'result': '标签修改成功', 'data': []}
    else:
        return {'code': 404, 'result': '标签不存在', 'data': []}


@router.delete('/{tag_id}')
async def delete(tag_id: int, db: Session = Depends(get_db)):
    tag = Tag.query(db).filter_by(id=tag_id)
    if tag.first():
        tag.delete()
        db.commit()
        return {'code': 200, 'result': '标签删除成功', 'data': []}
    else:
        return {'code': 404, 'result': '标签不存在', 'data': []}
