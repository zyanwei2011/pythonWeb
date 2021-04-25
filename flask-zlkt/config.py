#encoding: utf-8
import os

DEBUG = True

SECRET_KEY = os.urandom(24)

# 连接数据库字符串
# dialect+driver://username:password@host:port/database?charset=utf8mb4

dialect = 'mysql'  
driver = 'pymysql' 
username = 'root'
password = '123456'
host = '47.96.67.53'
port = 3306
database = 'zlkt'


SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4'.format(dialect, driver, username, password, host,port, database)

SQLALCHEMY_TRACK_MODIFICATIONS = False
