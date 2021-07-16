FROM python:3-alpine3.13

LABEL maintainer='zy'
LABEL description='simple deploying flask_project'

WORKDIR /usr/src/app

# COPY ./demo ./

# 解压
ADD ./demo.tar.gz ./


WORKDIR demo

RUN pip install -i https://pypi.douban.com/simple -r rqm.txt

# 将源代码映射到宿主机
VOLUME /usr/src/app/demo


EXPOSE 5000
# CMD [ "gunicorn", "demo:app", "-c", "./demo.py" ]

CMD [ "python", "./demo.py" ]