#coding: utf-8  
from mytools.emailClass import Email
import time
from main_func import *
from mytools.MyDatabaseClass import MyDatabase

# WeiboId_list = ('2691260383','5360104594','5842071290')
WeiboId_list = ('2691260383',)
headers = {
            'cookie':'SUHB=0pHhOPHjFBWmE9; _T_WM=bef2c515f1bcb67425331213a5262a1b; SUB=_2A2576H8KDeTRGeNG41cV9ifJwzWIHXVZEwFCrDV6PUJbrdAKLRGjkW1LHetTiZrR6KlYX3rTUfmzZffK35IRbw..; gsid_CTandWM=4upCa35c1Je5sDcDifB2doH4V9v',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'           
       }
    
weiboDB = MyDatabase(host='localhost',user='root',passwd='',db='weibo',port=3306,charset='utf8')

data = weiboDB.getData('weibos', 'id')
ex_length = len(data)
# 
# local_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# receiver = '2733641279@qq.com'  
# sender = '15262057539@163.com'  
#    
# subject = '陆阳又发微博了！快去回复他吧！' + local_time
# host = 'smtp.163.com'  
# port = 25
# username = '15262057539@163.com'  
# password = 'luyang716'   
# content = weiboDB.getData('weibos', 'content',order_by_row_name='create_time DESC')
# content = str(content[0][0])
# print('content:',content)
 
while 1:    
    for userID in WeiboId_list:
        status = CrawlSpecificUserWeibosInfo(userID, headers, weiboDB)
        if status is 1:
            local_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            receiver = '2733641279@qq.com'  
            sender = '15262057539@163.com'  
                
            subject = '陆阳又发微博了！快去回复他吧！' + local_time
            host = 'smtp.163.com'  
            port = 25
            username = '15262057539@163.com'  
            password = 'luyang716'   
            content = weiboDB.getData('weibos', 'content',order_by_row_name='create_time DESC')
            content = str(content[0][0])
            print('content:',content)
            emailObj = Email(sender,receiver,subject,content)
            emailObj.conn_server(host,port)
            emailObj.login(username, password)
            emailObj.send()
            emailObj.close()
        else:
            pass
    print('\n又要重新爬一遍，好烦\n')