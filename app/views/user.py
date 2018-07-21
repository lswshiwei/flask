from flask import Blueprint, render_template, flash, redirect, url_for

from app.forms import Register

user = Blueprint('user', __name__)


# 注册
@user.route('/register/', methods=['GET', 'POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        # 根据表单数据 创建用户对象
        # 把用户信息保存到数据库
        # 发送账户激活邮件
        flash('您已经注册成功，请点击邮件中链接进行激活！')
        return redirect(url_for('main.index'))
    return render_template('user/register.html', form=form)


# 登陆
@user.route('/login/')
def index():
    return '终迎来到登陆'
