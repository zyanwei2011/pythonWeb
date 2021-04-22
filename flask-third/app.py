from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

app = Flask(__name__)

app.config.from_object(config)  # 配置mysql连接

db = SQLAlchemy(app)  # 绑定app和db

migrate = Migrate(app, db)


# 表1
class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)

# 表2
class Article(db.Model):
    __tablename = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # 设置关联-关键字参数`secondary=中间表`来进行关联
    tags = db.relationship('Tag',secondary= articleTag,backref=db.backref('articles'))
    
# 表3 中间表    
# secondary只能接收 `db.Table`对象，不能通过`class`的方式实现，
article_tag = db.Table('article_tag',
           db.Column('article_id', db.Integer, db.ForeignKey('article.id'), primary_key=True),
           db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True))

db.create_all()





