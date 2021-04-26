## 服务部署
### 初始化数据库
```shell
# 初始化文件夹
python manage.py db init

# 生成脚本
python manage.py db migrate

# 执行脚本
python manage.py db upgrate
```