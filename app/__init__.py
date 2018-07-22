# 创建实例
from flask import Flask

from app.config import config
from app.extentions import init_extension
from app.views import register_blueprint


def creat_app(config_name):
    app = Flask(__name__)
    # 初始化配置
    if config_name not in config:
        config_name = 'develop'
    app.config.from_object(config[config_name])
    # 初始化函数调用
    init_extension(app)
    # 注册蓝图
    register_blueprint(app)
    return app
