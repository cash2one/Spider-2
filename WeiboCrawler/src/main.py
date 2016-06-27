#coding:utf-8

from MyDatabaseClass import MyDatabase
from main_func import *
import time

if __name__ == '__main__':
    headers = {
            'Cookie':'SUHB=02M_JC0c3Gnn_F; _T_WM=bef2c515f1bcb67425331213a5262a1b; SUB=_2A257-_-QDeTxGeNG41cV9ifJwzWIHXVZB4HYrDV6PUJbrdAKLVHMkW1LHetH5nGNPNyOQVaxXy03HO1tKXiXPQ..; gsid_CTandWM=4ub2a35c1OOuIglooYT8OoH4V9v',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
            'userID':'5885469589',
            'Referer':'',
            'Connection':'keep-alive',
            'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            'Accept-Encoding':"gzip, deflate"
       }
    
    weiboDB = MyDatabase(host='localhost',user='root',passwd='',db='weibo',port=3306,charset='utf8')
#     while 1:
    #CrawlSpecificUserFansInfo('5360104594',headers,weiboDB,start=0,end=20)
    
    
    #CrawlSpecificUserFriendsInfo('2691260383', headers, weiboDB, mode=0,start=30)
    data_tuple = weiboDB.getData('lyAttention', 'account_id')
    for data in data_tuple[180:]:
        id = data[0]
        if data == data_tuple[-1]:
            print("恭喜全部跑完")
        userHomePageLink = 'http://weibo.cn/' + id
        print(userHomePageLink)
        headers['Referer'] = userHomePageLink
        try:
            PayAttentionUser(id, headers)
        except Exception as e:
            print(e)
    local_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print(local_time)