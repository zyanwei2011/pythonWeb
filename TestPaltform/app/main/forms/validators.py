# -*- coding: utf-8 -*-
# @Time : 2021/5/14 8:09 上午
# @Author : zy
# @Email : zyanwei2011@163.com
# @File : validators.py
# @Project : TestPaltform

from wtforms import ValidationError


class Unique:
    """
    验证器，验证某个表里的某个数据是否已存在
    """

    def __init__(self, db_class, db_column, msg='数据已存在'):
        self.db_class = db_class
        self.db_column = db_column
        if msg:
            self.msg = msg

    def __call__(self, form, field):
        res = self.db_class.query.filter(self.db_column == field.data).first()
        if res:
            raise ValidationError(self.msg)
        return res



