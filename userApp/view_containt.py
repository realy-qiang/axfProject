from django.conf import settings
from django.core.mail import send_mail
from django.template import loader


def sendEmail(name, emial, token):
    # 其他代码
    # ...

    # 主题
    subject = '爱鲜蜂欢迎注册'
    # message表示发送的纯文本，
    # 如果需要发送带样式的，则使用html_message
    # 用html_message时，message为空字符串
    message = ''
    # 收件人列表
    receiver = [emial]
    context = {
        'name': name,
        'url': 'http://139.9.120.83/userApp/activeUser/?token='+str(token)
    }
    # 需要发送的带样式内容
    html_message = loader.get_template('active.html').render(context=context)
    # 发送者
    sender = settings.EMAIL_FROM
    # 　发送邮件
    send_mail(subject, message, sender, receiver, html_message=html_message)
