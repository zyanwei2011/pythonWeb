# -*- coding: utf-8 -*-
# @Time : 2021/5/14 8:08 上午
# @Author : zy
# @Email : zyanwei2011@163.com
# @File : __init__.py.py
# @Project : TestPaltform


from wtforms import Form
from wtforms import StringField, PasswordField, IntegerField,TextAreaField,RadioField, DecimalField, SelectField, DateField, SelectMultipleField
from wtforms.validators import DataRequired, Email, NumberRange, Regexp, Length, EqualTo
from app.main.forms.validators import Unique
from app.main.models.main import Project


class ProjectAddForm(Form):
    # 属性名要和前端html的name保持一致

    project_name = StringField(label='项目名称', validators=[
        DataRequired('项目名称不能为空'), Length(1, 32, message='项目名称仅支持1-32位长度'),
        Unique(Project, Project.project_name)
    ])

    project_desc = StringField(label='项目简介', validators=[
        Length(0, 128, message='项目简介长度不超过128位')
    ])


