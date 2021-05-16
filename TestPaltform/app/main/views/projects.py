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
from flask import render_template, abort, jsonify
from app.main.errors.exceptions import DatabaseException, ValidationException
from app.main.errors.http_errors import JsonDatabaseError, JsonValidateError


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
        try:
            Project.insert(form.data)
            return 'insert成功'
        except DatabaseException as e:
            # abort(401)   # abort + response封装响应，交给前端处理
            return f'{form.errors}'
    else:
        return f'{form.errors}'


@main.route('/project_edit/<int:p_id>', methods=['GET', 'POST'])
def project_edit(p_id):
    """编辑项目"""
    project = Project.query.get(p_id)
    if not project:
        return '项目不存在'
    form = ProjectAddForm(request.form)
    if request.method == 'GET':
        form = ProjectAddForm(obj=project)
        return render_template('addProject.html', form=form, project=project)
    form = ProjectAddForm(request.form)
    if form.validate():
        try:
            Project.update(form.data)
            return 'udate成功'
        except DatabaseException as e:
            # abort(401)   # abort + response封装响应，交给前端处理
            return f'{form.errors}'
    else:
        return f'{form.errors}'


@main.route('/project_delete', methods=['GET', 'POST'])
def project_delete():
    """删除项目"""
    p_id = request.json.get('id', '')
    try:
        res = Project.query.get(int(p_id))
        if res:
            # 删除
            res.delete()
            pass
        # return jsonify({'msg': '删除成功'})
        raise JsonDatabaseError('没有这个项目')
    except:
        raise JsonValidateError('id格式不正确')
        # return jsonify({'msg': 'id格式不正确或不存在'})




