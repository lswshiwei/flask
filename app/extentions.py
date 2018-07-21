# 添加扩展

from flask_bootstrap import Bootstrap
# 导入类库
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

# 创建对象
mail = Mail()
bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate(db=db)
moment = Moment()


# 初始化
def init_extension(app):
    mail.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    moment.init_app(app)
