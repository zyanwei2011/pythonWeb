# -*- coding: utf-8 -*-
# @Time : 2021/4/27 6:23 下午
# @Author : zy
# @Email : zyanwei2011@163.com
# @File : cases.py
# @Project : TestPaltform

from app.main import main


@main.route('/list_cases')
def list_cases():
    return 'cases'


@main.route('/create_cases')
def create_cases():
    return 'cases'
