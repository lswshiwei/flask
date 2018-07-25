from flask import Blueprint, render_template, flash, redirect, url_for, current_app
from itsdangerous import JSONWebSignatureSerializer as Serializer

from app.email import send_mail
from app.extentions import db
from app.forms import Register, login_form
from app.models import User

user = Blueprint('user', __name__)


# 注册
@user.route('/register/', methods=['GET', 'POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        # form.validate_email(form.email.data)
        # form.validate_username(form.username.data)
        # 根据表单数据 创建用户对象
        u = User(username=form.username.data,
                 password=form.password.data,
                 emil=form.email.data)
        # 把用户信息保存到数据库
        db.session.add(u)
        # 发送账户激活邮件
        # 标识身份数据
        s = Serializer(current_app.config['SECRET_KEY'])
        # 当前用户id为空，要手动提交
        db.session.commit()
        token = s.dumps({'id': u.id})
        send_mail('账户激活', u.emil, 'email/ectivate.html', username=u.username, token=token)
        flash('您已经注册成功，请点击邮件中链接进行激活！')
        return redirect(url_for('main.index'))
    return render_template('user/register.html', form=form)


# 激活
@user.route('/activate/<token>')
def activate(token):
    # 根据已有的元素和秘钥生成一个加密的令牌
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except:
        flash('激活失败')
        return redirect(url_for('main.index'))
    u = User.query.get(data['id'])
    if not u.cinfirmed:
        u.cinfirmed = True
        db.session.add(u)
    flash('激活成功！')
    return redirect(url_for('user.login'))



# 登陆
@user.route('/login/', methods=['GET', 'POST'])
def login():
    form = login_form()
    if form.validate_on_submit():
        u = User.query.filter(User.username == form.username.data).first()
        if not u:
            flash('无效用户')
        elif not u.cinfirmed:
            flash('账户未激活，请先激活')
        elif u.password != form.password.data:
            flash('密码错误')
        else:
            flash('登陆成功')
            return redirect(url_for('main.index'))
    return render_template('user/login.html', form=form)
