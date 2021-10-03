#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : __init__.py
# @Time   : 2021/09/26 23:35
from fastapi import APIRouter

from . import v1

router = APIRouter()
router.include_router(v1.router)
