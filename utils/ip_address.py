#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : ip_address.py
# @Time   : 2021/06/04 22:20
from fastapi import Request


def set_ip_address(request: Request):
    client_host = request.client.host
    return client_host
