#coding:utf-8
import smtplib,time
from email.mime.text import MIMEText  
from email.header import Header
 
class Email(object):
    def __init__(self,sender,receiver,subject,content,logObj,
                 host='',port=0,username='',password='',subtype='plain'):
        self.logObj = logObj
        self.msg = MIMEText(content,_subtype=subtype,_charset='utf-8')
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
        #连接服务器,并启动tls服务
        if self.host is '' and self.port is 0:
            self.host = host
            self.port = port
        try:
            self.smtp.connect(self.host,self.port)
            self.smtp.starttls() 
        except Exception as e:
            print('conn_server():',e)
                
    def login(self,username='',password=''):
        if self.username is '' and self.password is '':
            self.username = username
            self.password = password
        try:
            self.smtp.login(username, password)
            log_string = self.username+'登陆成功'+'\n'
            print(log_string)
            self.logObj.open()
            self.logObj.write(log_string)
            self.logObj.close()
        except Exception as e:
            print('login():',e)
    
    def send(self):
        try:
            self.smtp.sendmail(self.sender, self.receiver, self.msg.as_string())
            log_string = '邮件已投至'+self.receiver+'\n'
            print(log_string)
            now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            self.logObj.open()
            self.logObj.write(log_string+now+'\n\n')
            self.logObj.close()
        except Exception as e:
            print('send():',e)
    
    def close(self):
        self.smtp.close()