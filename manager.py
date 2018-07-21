import os

from flask_script import Manager

from app import creat_app

app = creat_app(os.getenv('BLOG_config', 'default'))
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
