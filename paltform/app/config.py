#encoding: utf-8


class BaseConfig:
    DEBUG = False
    # 分页数量
    PER_PAGE = 10
    # 数据库url
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@47.96.67.53:3306/db04?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    DEBUG = True


config = DevConfig()


