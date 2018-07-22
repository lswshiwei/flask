import os

base_dir = os.path.dirname(__file__)


# 配置基类
class Config:
    # 秘钥
    SECRET_KEY = 'abcd'
    # 模板自动更新
    TEMPLATES_AUTO_RELOAD = True
    # 数据库
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 追踪取消
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 邮件发送
    MAIL_SERVER = 'smtp.163.com'
    # 邮箱账号
    MAIL_USERNAME = '17324811724@163.com'
    # 授权码
    MAIL_PASSWORD = 'shiwei163'
    MAIL_PORT = 25


# 开发环境
class Develop_config(Config):
    # 数据库名字
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'blog-dev.db')


# 测试环境
class Testing_congif(Config):
    SQLALCHEMY_DATABASE_URLI = 'sqlite:///' + os.path.join(base_dir, 'blog-test.db')


# 生产环境
class Product_config(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'blog.db')


# 配置字典
config = {
    'develop': Develop_config,
    'testing': Testing_congif,
    'product': Product_config,
    #     默认
    'default': Develop_config,
}
