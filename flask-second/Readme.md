### 前后端分离部署nginx配置

```shell
worker_processes  1;
error_log  logs/error.log  info;
pid        logs/nginx.pid;
events {
    worker_connections  1024;
}
http {
    include       mime.types;
    default_type  application/octet-stream;
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
    access_log  logs/access.log  main;
    sendfile        on;
    keepalive_timeout  65;
    server {
        listen       80;
        server_name  www.testzy.com localhost;
        # 输入127.0.0.1/ 返回index.html
        location / {
            root   html;
            index  index.html index.htm;
        }

        # 访问/api/*路径时，后端服务器处理
        location /api {
            proxy_pass http://127.0.0.1:8000/api;
        }

        # 访问静态资源时，从nginx html目录下查找
        location ~ .*\.(html|htm|jpg|png|bmp|gif|jepg|css|js|css|ico|txt){
            root   html;
            index  index.html index.htm;
        }
        
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }
}
```
