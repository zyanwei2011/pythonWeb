from flask_sqlalchemy import SQLAlchemy
import time


db = SQLAlchemy()


class Base(db.Model):
    """
    定义基类表,其他表可继承该类
    `__abstract__`属性为True时不建表
    """
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.SmallInteger, default=1, nullable=False)
    created_time = db.Column(db.Integer, default=int(time.time()))
    updated_time = db.Column(db.Integer, default=int(time.time()), onupdate=int(time.time()))


class User(Base):
    __tablename__ = 'user'
    telephone = db.Column(db.String(11), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
