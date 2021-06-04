#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : main.py
# @Time   : 2021/06/04 22:09
from fastapi import FastAPI

from api import api_router
from core.config import BASE_DIR

app = FastAPI()
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    # uvicorn.run('main:app', debug=True, reload=True)
    print(BASE_DIR)