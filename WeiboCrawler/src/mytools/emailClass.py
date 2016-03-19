#coding:utf-8
import smtplib
from email.mime.text import MIMEText  
from email.header import Header 
 
class Email(object):
    def __init__(self,sender,receiver,subject,content,
                 host='',port=0,username='',password='',):
        self.msg = MIMEText(content,_subtype='plain',_charset='gb2312')
        self.msg['Subject'] = Header(subject, 'utf-8')
        self.msg['From'] = sender
        self.msg['To'] = receiver
        self.sender = sender
        self.receiver = receiver
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.smtp = smtplib.SMTP()
    
    def conn_server(self,host='',port=0):
        if self.host is '' and self.port is 0:
            self.host = host
            self.port = port
        res = self.smtp.connect(self.host,self.port)
        print(res)
        return res
                
    def login(self,username='',password=''):
        if self.username is '' and self.password is '':
            self.username = username
            self.password = password
        try:
            res = self.smtp.login(username, password)
            print(self.username,'登陆成功')
        except:
            pass
        print(res)
        return res
    
    def send(self):
        try:
            res = self.smtp.sendmail(self.sender, self.receiver, self.msg.as_string())
            print('邮件已投至',self.receiver)
        except:
            pass
        return res
    
    def close(self):
        self.smtp.close()