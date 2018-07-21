import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from app import creat_app

app = creat_app(os.getenv('BLOG_config', 'default'))
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
