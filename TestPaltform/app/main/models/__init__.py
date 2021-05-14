from flask_sqlalchemy import SQLAlchemy
from flask import current_app, jsonify, request
import time
import json


db = SQLAlchemy()


class BaseDb(db.Model):
    """
    定义基类表,其他表可继承该类
    `__abstract__`属性为True时不建表
    """
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.SmallInteger, default=1, nullable=False)
    created_time = db.Column(db.Integer, default=int(time.time()))
    updated_time = db.Column(db.Integer, default=int(time.time()), onupdate=int(time.time()))

    @classmethod
    def all(cls):
        """
        查询全部
        """
        data = cls.query.filter_by(status=1).order_by(cls.id.desc()).all()
        return str(data)

    @classmethod
    def paginate(cls, page=1):
        """
        分页查询
        """
        per_page = current_app.config.get('PER_PAGE')
        # error_out: 部分小错误不提醒
        return cls.query.filter_by(status=1).paginate(page=page, per_page=per_page, error_out=False)




