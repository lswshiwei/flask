# 用户模型
# 查看用户处于啥状态
from flask_login import UserMixin
# 加密方案
from werkzeug.security import generate_password_hash, check_password_hash

from app.extentions import db, login_manager


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(150))
    emil = db.Column(db.String(50), unique=True)
    cinfirmed = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError('密码不告诉你')

    #     加密存储密码
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    #     密码校验
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)




# 回到函数
# 根据用户id找到用户对象
@login_manager.user_loader
def load_user(uid):
    return User.query.get(uid)
