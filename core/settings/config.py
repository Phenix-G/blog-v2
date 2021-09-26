#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : config.py
# @Time   : 2021/06/04 22:21


# Build paths inside the project like this: BASE_DIR / 'subdir'.
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Config:
    DEBUG = True
    DATABASE = {
        'NAME': 'fastapi',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }


class Development(Config):
    pass


class Production(Config):
    DEBUG = False
    DATABASE = {
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '3306',
    }
