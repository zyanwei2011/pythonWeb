from flask import Blueprint

# 定义蓝图
main = Blueprint('main', __name__)

# 路由
from .views import index