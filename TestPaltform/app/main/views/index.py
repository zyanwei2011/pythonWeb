# -*- coding: utf-8 -*-
# @Time : 2021/4/27 10:57 上午
# @Author : zy
# @Email : zyanwei2011@163.com
# @File : index.py
# @Project : TestPaltform


from flask import render_template
from app.main import main


@main.route('/')
def index():
    return render_template('index.html')