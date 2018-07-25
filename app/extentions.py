# 添加扩展

from flask_bootstrap import Bootstrap
from flask_login import LoginManager
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
login_manager = LoginManager()

# 初始化
def init_extension(app):
    mail.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
