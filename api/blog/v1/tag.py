#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : tag.py
# @Time   : 2021/06/05 1:41
from fastapi import APIRouter

from models.tag import Tag, TagCreate, TagUpdate

router = APIRouter()


@router.get('/')
async def get_list() -> dict:
    tags = Tag.all()
    return {'data': tags}


@router.get('/{tag_id}')
async def get(tag_id: int) -> dict:
    tag = Tag.get(tag_id)
    return {'data': tag}


@router.post('/')
async def create(obj: TagCreate):
    tag = Tag.create(**obj.dict())
    return {'data': tag}


@router.put('/{tag_id}')
async def update(obj: TagUpdate, tag_id: int):
    tag = Tag.get(tag_id)
    data = obj.dict(exclude_unset=True)
    tag.update(data)
    return {'data': tag}


@router.delete('/{tag_id}')
async def delete(tag_id: int):
    tag = Tag.get(tag_id)
    tag.row_delete()
    return {'data': ''}
