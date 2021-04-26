class BaseConfig:
    DEBUG = False
    PER_PAGE = 10
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@47.96.67.53:3306/zlkt?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False