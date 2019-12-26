# -*-coding:utf-8-*-
# Author:Lu Wei


####1.函数

import smtplib,time
from email.mime.text import MIMEText
from email.utils import formataddr

# linchaoxi@eccom.com.cn
a=0
while a<10:
    msg = MIMEText('测试项内容', 'plain', 'utf-8')
    msg['from'] = formataddr(['123', 'davidlu1994@163.com'])
    msg['to'] = formataddr(['qwe', 'linjie@eccom.com.cn'])
    msg['subject'] = '测试'

    server = smtplib.SMTP('smtp.163.com', 25)
    server.login('davidlu1994@163.com', '')
    server.sendmail('davidlu1994@163.com', ['linjie@eccom.com.cn', ], msg.as_string())
    server.quit()
    time.sleep(5)
    a+=1
