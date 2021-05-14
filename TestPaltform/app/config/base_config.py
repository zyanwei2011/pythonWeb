import os

class BaseConfig:
    DEBUG = False
    PER_PAGE = 10
    # dialect+driver://username:password@host:port/database?charset=utf8mb4
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@47.96.67.53:3306/db01?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = str(123)
    # SECRET_KEY = os.urandom(32)
