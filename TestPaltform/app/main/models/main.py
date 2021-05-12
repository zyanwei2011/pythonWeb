# -*- coding: utf-8 -*-
# @Time : 2021/5/12 11:10 下午
# @Author : zy
# @Email : zyanwei2011@163.com
# @File : main.py
# @Project : TestPaltform

from ..models import BaseDb, db, current_app


class Project(BaseDb):
    __tablename__ = 'project'
    project_name = db.Column(db.String(32), nullable=False, unique=True)
    project_desc = db.Column(db.String(128), nullable=False)

    @classmethod
    def add_by_form(cls, form):
        """添加项目"""
        p = cls(project_name=form.get('project_name'),
                project_desc=form.get('project_desc'))
        try:
            db.session.add(p)
            db.session.commit()
            return p
        except Exception as e:
            current_app.logger.error(f'添加项目错误：{e}')
            raise e
