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

### curl
```shell script
# 创建项目
 curl 'http://127.0.0.1:5000/main/project_create' -X POST -d 'project_name=99991237&project_desc=88881'

# 查询项目
 curl 'http://127.0.0.1:5000/main/project_list' 
```
### 项目运行
#### gunicorn服务器
```shell script
# 安装
 pip install guincorn

# 启动服务
 nohup gunicorn -w 4 -b 0.0.0.0:5555 run:app &
```
#### nginx反向代理

```shell script
# 配置nginx
cd /usr/local/nginx
vi conf/nginx.conf

server {
    listen       80;
    server_name  localhost;


    location / {
        proxy_pass http://127.0.0.1:5555;
        proxy_set_header HOST Shost;
    }
}   
# 启动
./sbin/nginx 

# 重启
./sbin/nginx -s reload 
```