# 用户模型
# 查看用户处于啥状态
from flask_login import UserMixin

from app.extentions import db, login_manager


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    emil = db.Column(db.String(50), unique=True)
    cinfirmed = db.Column(db.Boolean, default=False)


# 回到函数
# 根据用户id找到用户对象
@login_manager.user_loader
def load_user(uid):
    return User.query.get(uid)
