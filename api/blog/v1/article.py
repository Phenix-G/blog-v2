#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : article.py
# @Time   : 2021/09/19 14:45
from fastapi import APIRouter

from models.article import ArticleCreate, Article, ArticleUpdate

router = APIRouter()


@router.get('/')
async def get_list():
    articles = Article.all()
    return {'data': articles}


@router.get('/{article_id}')
async def get(article_id: int):
    db_article = Article.get(article_id)
    return {'data': db_article}


@router.post('/')
async def create(obj: ArticleCreate):
    article = Article.create(**obj.dict())
    return {'data': article}


@router.put('/{article_id}')
async def update(article_id: int, obj: ArticleUpdate):
    article = Article.get(article_id)
    data = obj.dict(exclude_unset=True)
    article.update(data)
    return {'data': article}


@router.delete('/{article_id}')
async def delete(article_id: int):
    article = Article.get(article_id)
    article.row_delete()
    return {'data': ''}
