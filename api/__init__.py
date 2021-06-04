#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : __init__.py.py
# @Time   : 2021/06/04 22:25
from fastapi import APIRouter

from . import v1

api_router = APIRouter()
api_router.include_router(v1.router)
