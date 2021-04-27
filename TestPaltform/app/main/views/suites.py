# -*- coding: utf-8 -*-
# @Time : 2021/4/27 6:23 下午
# @Author : zy
# @Email : zyanwei2011@163.com
# @File : suites.py
# @Project : TestPaltform

from app.main import main


@main.route('/list_suites')
def list_suites():
    return 'suites'


@main.route('/create_suites')
def create_suites():
    return 'suites'
