#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : command.py
# @Time   : 2021/10/04 23:07
import uvicorn
from fastapi import FastAPI

from api import api_router
from core.settings.register import register_exception


def create_app():
    app = FastAPI()
    app.include_router(api_router)
    register_exception(app)

    return app


def register_command(typer):
    @typer.command()
    def runserver():
        uvicorn.run('core.extensions.command:create_app', reload=True, debug=True, factory=True)

    return typer
