# -*- coding: utf-8 -*-
# @Time : 2021/4/27 6:23 下午
# @Author : zy
# @Email : zyanwei2011@163.com
# @File : modules.py
# @Project : TestPaltform

from app.main import main


@main.route('/list_modules')
def list_modules():
    return 'modules'


@main.route('/create_modules')
def create_modules():
    return 'modules'
