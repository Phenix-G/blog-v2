#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : __init__.py
# @Time   : 2021/06/04 22:26
from fastapi import APIRouter

from . import user, category, tag

router = APIRouter()
router.include_router(user.router, prefix='/users', tags=['users'])
router.include_router(category.router, prefix='/categories', tags=['categories'])
router.include_router(tag.router, prefix='/tags', tags=['tags'])
