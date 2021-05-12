"""
初始化
"""

from flask import Flask


def create_app():
    # 初始化
    app = Flask(__name__)

    # 配置
    from app.config.dev_config import config
    app.config.from_object(config)

    # 蓝图注册
    from app.main import main
    app.register_blueprint(main)

    # 添加过滤器
    from app.main.template_env import str_time
    app.add_template_filter(str_time)

    # 数据库初始化
    from app.main.models.user import db
    db.init_app(app)


    from flask_migrate import Migrate
    migrate = Migrate()
    migrate.init_app(app, db)

    return app
