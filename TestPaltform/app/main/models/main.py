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
        # <input id="project_name" name="project_name" required type="text" value="123">
        # 从html对象form中取值
        p = cls(project_name=form.project_name.data,
                project_desc=form.project_desc.data,
                )
        try:
            db.session.add(p)
            db.session.commit()
            return p
        except Exception as e:
            current_app.logger.error(f'添加项目错误：{e}')
            raise e
