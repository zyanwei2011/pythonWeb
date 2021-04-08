
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,IntegerField
from wtforms.validators import DataRequired, NumberRange, Regexp, Length, EqualTo

class RegisterForm(FlaskForm):
    # 属性名要和前端html的name保持一致
    phone = StringField(label='手机号码', validators=[
        Regexp(r'^1[3,5,7,8,9]\d{9}$',message='手机号码格式错误'), 
        DataRequired('手机号码不能为空')])
    pwd = PasswordField(label='密码', validators=[
        Regexp(r'[a-zA-Z0-9]+',message='仅支持字母和数字'),
        Length(6,32, message='密码仅支持6-32位长度'), 
        DataRequired('密码不能为空')])
    confirm_pwd = PasswordField(label='确认密码', validators=[
        EqualTo('pwd', message='确认密码与密码不一致')])
    age = IntegerField(label='年龄',validators=[
        NumberRange(min=1, max=200, message='年龄仅支持1-200'), 
        DataRequired('年龄不能为空')])
    


