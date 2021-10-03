#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : __init__.py
# @Time   : 2021/06/04 22:25
from fastapi import APIRouter

from . import blog

api_router = APIRouter()
api_router.include_router(blog.router)
