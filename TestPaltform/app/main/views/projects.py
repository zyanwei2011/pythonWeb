# -*- coding: utf-8 -*-
# @Time : 2021/4/27 6:23 下午
# @Author : zy
# @Email : zyanwei2011@163.com
# @File : projects.py
# @Project : TestPaltform

from app.main import main
from app.main import request
from app.main.models.main import Project
from app.main.forms import ProjectAddForm
from flask import render_template


@main.route('/project_list', methods=['GET'])
def project_list():
    """查询项目"""
    return str(Project.all())
    # return str(Project.paginate().items)


@main.route('/project_create', methods=['GET', 'POST'])
def project_create():
    """新增项目"""
    form = ProjectAddForm(request.form)
    if request.method == 'GET':
        return render_template('addProject.html', form=form)
    if form.validate():
        Project.add_by_form(form)
        return 'success'
    else:
        return f'{form.errors}'


