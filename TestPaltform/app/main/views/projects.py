# -*- coding: utf-8 -*-
# @Time : 2021/4/27 6:23 下午
# @Author : zy
# @Email : zyanwei2011@163.com
# @File : projects.py
# @Project : TestPaltform

from app.main import main


@main.route('/list_projects')
def list_projects():
    return 'projects'


@main.route('/create_projects')
def create_projects():
    return 'projects'
