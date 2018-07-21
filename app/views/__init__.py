# 封装注册蓝图函数
from .main import main
from .posts import posts
from .user import user

# 蓝图
BEFAULT_BLUEPRINT = (
    main,
    user,
    posts
)


def register_blueprint(app):
    for blue_name in BEFAULT_BLUEPRINT:
        app.register_blueprint(blue_name)
