from flask_sqlalchemy import SQLAlchemy
from flask import current_app
import time


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
        return cls.query.order_by(cls.id.desc).all()  # 倒序

    @classmethod
    def paginate(cls, page):
        """
        分页查询
        """
        return cls.query.paginate(page=page, per_page=current_app.config.get('PER_PAGE'), error_out=False)




