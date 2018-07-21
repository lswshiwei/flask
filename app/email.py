from threading import Thread

from flask import current_app, render_template
from flask_mail import Message

from app.extentions import mail


# 异步发送邮件任务
def async_send_mail(app, msg):
    # 邮件发送必须在程序上下文
    # 新的线程中没有上下文，因此需要手动创建
    with app.app_context():
        mail.send(msg)


# 封装函数发送邮件
def send_mail(subject, to, template, *args, **kwargs):
    if isinstance(to, list):
        recipients = to
    elif isinstance(to, str):
        recipients = to.split(',')
    else:
        raise Exception('邮件接收者参数类型有误')
    # 创建邮件消息对象
    msg = Message(subject,
                  recipients=recipients,
                  sender=current_app.config['MAIL_USERNAME'])
    # 将邮件模板渲染后作为邮件内容
    msg.html = render_template(template, *args, **kwargs)
    # 发送邮件
    # mail.send(msg)
    # current_app是app的代理对象
    # 根据代理对象current_app找到原始的app
    app = current_app._get_current_object()
    # 创建线程
    thr = Thread(target=async_send_mail, args=(app, msg))
    # 启动线程
    thr.start()
    # 返回线程
    return thr
