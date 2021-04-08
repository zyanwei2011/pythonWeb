
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,IntegerField,TextAreaField,RadioField, DecimalField, SelectField, DateField, SelectMultipleField
from wtforms.validators import DataRequired, Email, NumberRange, Regexp, Length, EqualTo


class RegisterForm(FlaskForm):
    # 属性名要和前端html的name保持一致
    
    phone = StringField(label='手机号码', validators=[
        Regexp(r'^1[3,5,7,8,9]\d{9}$',message='手机号码格式错误'), 
        DataRequired('手机号码不能为空')],render_kw={'placeholder': '请输入手机号'})
    
    pwd = PasswordField(label='密码', validators=[
        Regexp(r'[a-zA-Z0-9]+',message='仅支持字母和数字'),
        Length(6,32, message='密码仅支持6-32位长度'), 
        DataRequired('密码不能为空')])
    
    confirm_pwd = PasswordField(label='确认密码', validators=[
        EqualTo('pwd', message='确认密码与密码不一致')])
    
    # render_kw={"class": "age"} 给标签添加class="age"属性
    # default 设置默认值
    age = IntegerField(label='年龄',validators=[
        NumberRange(min=1, max=200, message='年龄仅支持1-200'), 
        DataRequired('年龄不能为空')], render_kw={"class": "age"}, default=18)
    
    email = StringField(label='邮箱', validators=[
        Email(message='邮箱格式不合法'),
        DataRequired('邮箱不能为空')])
    
    gender = RadioField(label='性别', choices=[('m', 'Male'),('f', 'Female')])
    
    # DecimalField(label='身高', places=1) 必须输入数值，保留一位小数
    height = DecimalField(label='身高(cm): ', places=1)
    
    birthday = DateField('出生日期', format='%Y-%m-%d') 
    
    # 单选
    job = SelectField('职业：', choices=[
        ('teacher', '教师'),
        ('doctor', '医生'),
        ('engineer', '工程师'),
        ('lawyer', '律师')
    ])
      
    # 多选
    hobby = SelectMultipleField('爱好：', choices=[
        ('0', '吃饭'),
        ('1', '睡觉'),
        ('2', '敲代码')
    ])
    
    comment = TextAreaField(label='备注', validators=[
        Length(0,512)])
    


