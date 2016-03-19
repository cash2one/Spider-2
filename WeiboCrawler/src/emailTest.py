#coding: utf-8  
from mytools.emailClass import Email
import time
from main_func import *
from mytools.MyDatabaseClass import MyDatabase

#'5885469589',
WeiboId_list = ('5885469589','5360104594','5842071290')
#WeiboId_list = ('5885469589',)
headers = {
            'cookie':'SUHB=0pHhOPHjFBWmE9; _T_WM=bef2c515f1bcb67425331213a5262a1b; SUB=_2A2576W9XDeTRGeNG41cV9ifJwzWIHXVZEnEfrDV6PUJbrdANLRmgkW1LHetVs-vBtEvuclLd9jOYOsk2j6EU_g..; gsid_CTandWM=4uMWa35c1k9HA57IX4advoH4V9v',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'           
       }
    
weiboDB = MyDatabase(host='localhost',user='root',passwd='',db='weibo',port=3306,charset='utf8')

while 1:    
    for userID in WeiboId_list:
        status = CrawlSpecificUserWeibosInfo(userID, headers, weiboDB)
        if status is 1 or status is 3:
            weiboData = weiboDB.getData(table_name_string='weibos', 
                            row_name='via_reason,content,userID',
                            order_by_row_name='create_time DESC',limit=1)
            author_id = weiboData[0][2]
            sql = "SELECT username FROM user WHERE account_id=" + author_id
            weiboDB.cur.execute(sql)
            author_name_list = weiboDB.cur.fetchall()
            author_name = author_name_list[0][0]
            print(author_name)
            content = str(weiboData[0][0]) + str(weiboData[0][1])
            send_email(author_name,content)
    print('\n又要重新爬一遍，好烦\n')