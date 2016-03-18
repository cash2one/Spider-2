#coding:utf-8

from mytools.MyDatabaseClass import MyDatabase
from main_func import *
import time

if __name__ == '__main__':
    headers = {
            'cookie':'SUHB=0pHhOPHjFBWmE9; _T_WM=bef2c515f1bcb67425331213a5262a1b; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5Bokdk76BM8YbOXb2aDXwh5JpX5o2p; SUB=_2A25775RuDeTRGeNG41cV9ifJwzWIHXVZEzwmrDV6PUJbrdANLUj3kW1LHeszo6piaNIZKRm5dlFwlkbINh7Agg..; SSOLoginState=1458299956; gsid_CTandWM=4uBsa35c1mq952lsicrhsoH4V9v',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'           
       }
    
    weiboDB = MyDatabase(host='localhost',user='root',passwd='',db='weibo',port=3306,charset='utf8')
#     while 1:
    #CrawlSpecificUserFansInfo('5360104594',headers,weiboDB,start=0,end=20)
    
    CrawlSpecificUserWeibosInfo('2138751751',headers,weiboDB)
    
    #CrawlMyFocusWeibo(headers,weiboDB)
    

#     weiboDB.cur.execute(
#         "insert into time(time)"
#                   "values (%s)",
#                   ('2016-01-26 10:23:58')
#                         )
#     weiboDB.conn.commit()

    local_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print(local_time)
    print(type(local_time))