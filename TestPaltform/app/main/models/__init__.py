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
        data = cls.query.all()
        return str(data)

    @classmethod
    def paginate(cls):
        """
        分页查询
        """
        page = request.args.get('page', 1)
        per_page = current_app.config.get('PER_PAGE')
        return cls.query.paginate(page=page, per_page=per_page, error_out=False)




