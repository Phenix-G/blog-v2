#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : main.py
# @Time   : 2021/06/04 22:09
from typer import Typer

from core.extensions.command import register_command

typer = Typer()
app = register_command(typer)
if __name__ == '__main__':
    app()
