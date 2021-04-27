from app.config.base_config import BaseConfig


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@47.96.67.53:3306/db04?charset=utf8mb4'


config = DevConfig()
