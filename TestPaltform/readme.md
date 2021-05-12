### 目录介绍
```shell script
├── app
│   ├── __init__.py
│   ├── config                       // 项目配置
│   │   ├── __init__.py
│   │   ├── base_config.py
│   │   └── dev_config.py
│   ├── main                         // 蓝图1 
│   │   ├── __init__.py
│   │   ├── models                   // sql
│   │   │   ├── __init__.py
│   │   │   └── user.py
│   │   └── views                    // 视图或
│   │       ├── __init__.py
│   │       ├── cases.py
│   │       └── index.py
│   ├── static                       // 静态文件位置
│   ├── templates                    // html模板位置
│   └── user                         // 蓝图2
│       └── __init__.py
├── app.py                           // 项目入口
├── doc                              // 项目文档
├── init.sh                          // 项目部署脚本
├── migrations
├── readme.md
└── requirements.txt
```
### 数据库
```shell script

set FLASK_APP=run.py
# 初始化，生成文件夹
flask db init
# 初始化脚本
flask db migrate
# 执行脚本
flask db upgrade
# 执行脚本
flask db downgrade
```

