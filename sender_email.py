#!/usr/bin/python3

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib

'''
生成邮件内容

email_from     发件人
email_to       收件人
email_subject  主题
email_text     正文
annex_path     附件路径
annex_name     附件名称
'''
def create_email(email_from, email_to, email_subject, email_text, annex_path, annex_name):
    # 生成一个空的带附件的邮箱实例
    message = MIMEMultipart()
    # 将正文以text的形式插入邮件中
    message.attach(MIMEText(email_text, 'plain', 'utf-8'))
    # 生成邮件人名称
    # sina邮箱要求发件人和邮箱地址一致，并且没有第二个参数
    message['From'] = Header(email_from)
    # 生成收件人名称
    message['To'] = Header(email_to, 'utf-8')
    # 生成邮件主题
    message['Subject'] = Header(email_subject, 'utf-8')
    # 读取附件的内容
    attl = MIMEText(open(annex_path, 'rb').read(), 'base64', 'utf-8')
    attl['Content-Type'] = 'application/octet-stream'
    # 生成附件的名称
    attl['Content-Disposition'] = 'attachment; filename=' + annex_name
    # 将附件插入邮件中
    message.attach(attl)
    # 返回邮件
    return message

'''
发送邮件

sender   邮箱地址
password 邮箱密码
reciver  收件人
msg      邮件内容
'''
def send_email_sina(sender, password, receiver, msg):
    try:
        # 找到发送邮箱的服务器地址，已加密形式发送
        server = smtplib.SMTP_SSL('smtp.sina.com', 465)
        server.set_debuglevel(1)
        server.starttls()
        # 登录邮箱
        server.login(sender, password)
        # 发送邮件
        server.sendmail(sender, receiver, msg.as_string())
        print('send email success')
        # 关闭连接
        server.quit()
    except Exception as err:
        print(err)
        print('send email failed')

def send_email_163(sender, password, receiver, msg):
    try:
        # 找到发送邮箱的服务器地址，已加密形式发送
        server = smtplib.SMTP_SSL('smtp.163.com', 465)
        server.set_debuglevel(1)
        #server.starttls() # 163普通用户不能加密发送，VIP用户可以
        # 登录邮箱
        server.login(sender, password)
        # 发送邮件
        server.sendmail(sender, receiver, msg.as_string())
        print('send email success')
        # 关闭连接
        server.quit()
    except Exception as err:
        print(err)
        print('send email failed')

def main():
    email_from = '18811475054@163.com'
    email_to = '我'
    email_subject = 'zgp 2018/09/01'
    email_text = '邮件正文....'
    annex_path = 'D:/workspace/JsonTest.java'
    annex_name = 'JsonTest.java'

    msg = create_email(email_from, email_to, email_subject, email_text, annex_path, annex_name)

    sender = '18811475054@163.com'
    password = 'zhugp125'
    receiver = 'zhugp125@sina.com'
    send_email_163(sender, password, receiver, msg)

if __name__ == '__main__':
    main()
    