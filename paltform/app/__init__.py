# -*- coding: utf-8 -*-
# @Time : 2021/4/26 10:03 下午
# @Author : zy
# @Email : zyanwei2011@163.com
# @File : __init__.py.py
# @Project : paltform

from flask import Flask
from app.config import config


def create_app():
    """
    # 初始化
    # 初始化数据库
    配置文件
    自定义错误处理机制
    模板过滤器注册
    """
    app = Flask(__name__)

    # 配置文件
    app.config.from_object(config)

    # 蓝图配置
    from app.main import main
    app.register_blueprint(main)

    # 数据库配置
    from app.main.models import db
    db.init_app(app)

    return app
