FROM python:3.7-alpine3.13

LABEL maintainer='zy'
LABEL description='simple deploying flask_project'

WORKDIR /usr/src/app

COPY ./TestPaltform ./demo

# 解压
# ADD ./demo.tar.gz ./


WORKDIR demo

RUN pip install -i https://pypi.douban.com/simple -r requirements.txt

# 将源代码映射到宿主机
VOLUME /usr/src/app/demo


EXPOSE 5000
# CMD [ "gunicorn", "demo:app", "-c", "./demo.py" ]

CMD [ "python", "./run.py" ]