#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : category.py
# @Time   : 2021/06/05 1:47
from fastapi import APIRouter

from models.category import Category, CategoryCreate, CategoryUpdate

router = APIRouter()


@router.get('/')
async def get_list() -> dict:
    categories = Category.all()
    return {'data': categories}


@router.get('/{category_id}')
async def get(category_id: int) -> dict:
    category = Category.get(category_id)
    return {'data': category}


@router.post('/')
async def create(obj: CategoryCreate):
    category = Category.create(**obj.dict())
    return {'data': category}


@router.put('/{category_id}')
async def update(obj: CategoryUpdate, category_id: int):
    category = Category.get(category_id)
    data = obj.dict(exclude_unset=True)
    category.update(data)
    return {'data': category}


@router.delete('/{category_id}')
async def delete(category_id: int):
    category = Category.get(category_id)
    category.row_delete()
    return {'data': ''}
