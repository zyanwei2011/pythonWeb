### 蓝图
>+ 蓝图----->子系统。可以理解为应用模块化，针对大型应用。

```python
from flask import Blueprint

# 1. 定义蓝图
main = Blueprint('main', __name__, url_prefix='/main')  访问url：127.0.0.1:5000/main

# 2. 路由导入蓝图位置
from .views import index

# 3. 初始化app时注册蓝图
from app.main import main
app.register_blueprint(main)
```
