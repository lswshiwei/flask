# 用户模型
from app.extentions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    emil = db.Column(db.String(50), unique=True)
    cinfirmed = db.Column(db.Boolean, dafault=False)
