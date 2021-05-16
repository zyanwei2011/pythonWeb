# -*- coding: utf-8 -*-
# @Time : 2021/5/12 11:10 下午
# @Author : zy
# @Email : zyanwei2011@163.com
# @File : main.py
# @Project : TestPaltform

from ..models import BaseDb, db, current_app
from app.main.errors.exceptions import DatabaseException


class Project(BaseDb):
    __tablename__ = 'project'
    project_name = db.Column(db.String(32), nullable=False, unique=True)
    project_desc = db.Column(db.String(128), nullable=False)
    status = 0

    @classmethod
    def insert(cls, data):
        """添加项目"""
        p = cls(project_name=data.get('project_name', ''),
                project_desc=data.get('project_desc', ''),
                )
        try:
            db.session.add(p)
            db.session.commit()
        except Exception as e:
            current_app.logger.error(f'添加项目错误出错')
            raise DatabaseException('数据库添加出错')    # 后端异常

    @classmethod
    def update(cls, data):
        """更新项目"""
        p = cls(project_name=data.get('project_name', ''),
                project_desc=data.get('project_desc', ''),
                )
        try:
            db.session.add(p)
            db.session.commit()
        except Exception as e:
            current_app.logger.error(f'添加项目错误出错')
            raise DatabaseException('数据库更新出错')    # 后端异常

    def delete(self):
        """删除项目"""
        self.status = self.status
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except Exception as e:
            current_app.logger.error(f'删除项目出错')
            raise DatabaseException('数据库删除出错')    # 后端异常
