from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, EqualTo, Email, ValidationError, DataRequired

from .models import User


# 注册表单
class Register(FlaskForm):
    username = StringField('用户名:', validators=[Length(6, 12, message='用户名必为6到12个字符长度的字符串')])
    password = PasswordField('密码:', validators=[Length(3, 12, message='密码必须为3到12个字符长度')])
    confirm = PasswordField('确认密码:', validators=[EqualTo('password', message='密码不一致')])
    email = StringField('邮箱:', validators=[Email(message='邮箱格式不正确')])
    submit = SubmitField('马上注册')
    #     o自定义验证
    def validate_username(self, field):
        # 自定义验证username
        if User.query.filter(User.username == field.data).first():
            raise ValidationError('用户已经存在，请使用其他用户名！')
        # 自定义验证emai
    def validate_email(self, field):
        if User.query.filter(User.emil == field.data).first():
            raise ValidationError('该邮箱已经注册！')


# 登陆表单
class login_form(FlaskForm):
    username = StringField('用户名:', validators=[DataRequired(message='请填入用户名')])
    password = PasswordField('密码:', validators=[DataRequired(message='请填入密码')])
    remember = BooleanField('记住我？')
    submit = SubmitField('登陆')
