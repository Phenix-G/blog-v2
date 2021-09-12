#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : __init__.py
# @Time   : 2021/06/04 22:21
import os

from fastapi import FastAPI
from typer import Typer

from api import api_router
from .config import BASE_DIR

main = Typer()
SHELL_COMMAND = os.system
MIGRATIONS_DIR = BASE_DIR.joinpath('migrations')


@main.command()
def db_init():
    if MIGRATIONS_DIR.exists():
        raise RuntimeError('FAILED: Directory migrations already exists and is not empty')

    SHELL_COMMAND('alembic init migrations')


@main.command()
def migrations(message=''):
    command = 'alembic revision --autogenerate -m "{}"'.format(message)
    SHELL_COMMAND(command)


@main.command()
def migrate():
    command = 'alembic upgrade head'
    SHELL_COMMAND(command)


def create_app():
    app = FastAPI()
    app.include_router(api_router)
    return app


@main.command()
def runserver(host='', port=''):
    base_command = 'uvicorn core:create_app --reload --debug'
    if host and port:
        command = f'{base_command} --host {host} --port {port}'
    elif host:
        command = f'{base_command} --host {host}'
    elif port:
        command = f'{base_command} --port {port}'
    else:
        command = base_command
    SHELL_COMMAND(command)
