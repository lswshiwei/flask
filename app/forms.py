from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email


# 注册表单
class Register(FlaskForm):
    username = StringField('用户名:', validators=[Length(6, 12, message='用户名必为6到12个字符长度的字符串')])
    password = PasswordField('密码:', validators=[Length(3, 12, message='密码必须为3到12个字符长度')])
    confirm = PasswordField('确认密码:', validators=[EqualTo('password', message='密码不一致')])
    email = StringField('邮箱:', validators=[Email(message='邮箱格式不正确')])
    submit = SubmitField('马上注册')
