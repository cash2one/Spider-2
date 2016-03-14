#coding:utf-8

from mytools.MyDatabaseClass import MyDatabase
from main_func import *

if __name__ == '__main__':
    headers = {
            'cookie':'SUHB=0z1B1fhZjG7DCe; _T_WM=bef2c515f1bcb67425331213a5262a1b; SUB=_2A2574RbNDeRxGeRI4lMT9i7Pwz-IHXVZLbqFrDV6PUJbrdANLRH6kW1LHetxlcUhmY6ME57DOcClitlj_c9o_w..; gsid_CTandWM=4uINa35c1jX4SthOuMlNCbi7q6b',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'           
       }
    
    weiboDB = MyDatabase(host='localhost',user='root',passwd='',db='weibo',port=3306,charset='utf8')
    
    while 1:
        CrawlSpecificUserFansInfo('2691260383',headers,weiboDB,start=20)