#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : email.py
# @Time   : 2021/06/04 22:20
from fastapi import Request


def set_ip_address(request: Request):
    client_host = request.client.host
    return client_host


import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # SMTP服务器
mail_user = "chris_guoc@163.com"  # 用户名
mail_pass = "IIPXCHVYYTYSZCON"  # 授权密码，非登录密码

sender = 'chris_guoc@163.com'
# 发件人邮箱(最好写全, 不然会失败)
receivers = ['1486316634@qq.com']
# 接收邮件，可设置为你的QQ邮箱或者其他邮箱

title = 'main'  # 邮件主题
content = 'password generate done'


def sendEmail(text=content):
    message = MIMEText(text, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)


def send_email2(SMTP_host=mail_host, from_account=mail_user, from_passwd=mail_pass, to_account=receivers[0],
                subject=title, content=content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())

    email_client.quit()


# from moviepy.editor import *
#
# video = VideoFileClip('../【从零开始学英语】掌握这625个单词，让你的英语水平突飞猛进.mp4')
# audio = video.audio
# audio.write_audiofile('test.mp3')

