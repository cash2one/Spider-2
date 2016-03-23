#coding: utf-8  
from mytools.emailClass import Email
import time
from main_func import *
from mytools.MyDatabaseClass import MyDatabase
from mytools.fileClass import File


#'5885469589',
WeiboId_list = ('5885469589','2691260383','5360104594','5842071290')
#WeiboId_list = ('5885469589',)

weiboDB = MyDatabase(host='localhost',user='root',passwd='',db='weibo',port=3306,charset='utf8')

cookie_list = ('SUHB=0pHhOPHjFBWmE9; _T_WM=bef2c515f1bcb67425331213a5262a1b; gsid_CTandWM=4udVa35c1dW73448sBMwdbi7q6b; SUB=_2A2579JvyDeRxGeRI4lMT9i7Pwz-IHXVZFiW6rDV6PUJbrdANLXDykW1LHesATt0ju3lSVjv4AYl5bImahXQjpw..',

    '_T_WM=9c937db8943c8dc9bd404af31c6a9034; gsid_CTandWM=4u2lb1311aM2iATFPEn7coH4V9v; SUB=_2A2579JxADeTxGeNG41cV9ifJwzWIHXVZFiQIrDV6PUJbrdANLUmmkW1LHeshEnRyH0kdGBqKrCXW8zRtL3wGFQ..')

headers_luyang = {
            'cookie':'SUHB=0pHhOPHjFBWmE9; _T_WM=bef2c515f1bcb67425331213a5262a1b; gsid_CTandWM=4udVa35c1dW73448sBMwdbi7q6b; SUB=_2A2579JvyDeRxGeRI4lMT9i7Pwz-IHXVZFiW6rDV6PUJbrdANLXDykW1LHesATt0ju3lSVjv4AYl5bImahXQjpw..',
            'cookie_user_id':'2691260383',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'           
       }
headers_kidlin = {
            'cookie':'_T_WM=9c937db8943c8dc9bd404af31c6a9034; gsid_CTandWM=4u2lb1311aM2iATFPEn7coH4V9v; SUB=_2A2579JxADeTxGeNG41cV9ifJwzWIHXVZFiQIrDV6PUJbrdANLUmmkW1LHeshEnRyH0kdGBqKrCXW8zRtL3wGFQ..',
            'cookie_user_id':'5885469589',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'           
                  }

headers_list = (headers_luyang,headers_kidlin)

global headers
headers = headers_list[0]

def switch_cookie():
    global headers
    if headers == headers_list[0]:
        headers = headers_list[1]
    else:
        headers = headers_list[0]
    return


sql = "select account_id from user where username='xgl'"
weiboDB.cur.execute(sql)
data = weiboDB.cur.fetchall()
print(data)

delete_string = ''

for i in data:
    userID = i[0]
    print(userID)
    sql = "select id from weibos where userID=" + userID
    print(sql)
    weiboDB.cur.execute(sql)
    wbdata = weiboDB.cur.fetchall()
    if wbdata:
        for j in wbdata:
            item = "'"
            item += j[0] + "'"
            delete_string += item + ','

print(delete_string)
weiboDB.exeDelete('weibos', 'id', delete_string)
    