#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def smtp_alert(accountlist, msg):
  mail_host = "smtp.chinadaas.com"  # 设置服务器
  mail_user = "zabbix@chinadaas.com"  # 用户名
  mail_pass = "Zs_123456"  # 口令

  sender = 'zabbix@chinadaas.com'
  # receivers = ['1498472791@qq.com','2316656047@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
  message = MIMEText(msg, 'plain', 'utf-8')
  message['From'] = Header(mail_user, 'utf-8')
  #    message['To'] =  Header(b, 'utf-8')

  subject = 'Dns need to add some record'
  message['Subject'] = Header(subject, 'utf-8')
  smtpObj = smtplib.SMTP()
  smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
  smtpObj.login(mail_user, mail_pass)
  smtpObj.helo('zabbix')
  for receivers in accountlist:
    try:
      smtpObj.sendmail(sender, receivers, message.as_string())
      yield "邮件发送成功"
    except Exception:
      yield "Error: 无法发送邮件"

p = smtp_alert(["1498472791@qq.com","xuhui@chinadaas.com"],'hehe')
for send in p:
  print send
