# -*- coding: utf-8 -*-
# @Time : 2021/4/27 6:23 下午
# @Author : zy
# @Email : zyanwei2011@163.com
# @File : projects.py
# @Project : TestPaltform

from app.main import main
from app.main import request
from app.main.models.main import Project


@main.route('/list_projects')
def list_projects():
    return 'projects'


@main.route('/create_projects', methods=['GET', 'POST'])
def create_projects():
    if request.method == 'GET':
        return 'projects'
    form = request.form
    Project().add_by_form(form)

    return 'POST'
