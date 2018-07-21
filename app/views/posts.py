from flask import Blueprint

posts = Blueprint('posts', __name__)


@posts.route('/posts/')
def send_posts():
    return '回复成功'
