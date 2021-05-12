# -*- coding: utf-8 -*-
# @Time : 2021/5/11 6:41 下午
# @Author : zy
# @Email : zyanwei2011@163.com
# @File : user.py
# @Project : TestPaltform

from ..models import BaseDb, db


class User(BaseDb):
    __tablename__ = 'user'
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)